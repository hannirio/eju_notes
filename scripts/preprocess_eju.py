#!/usr/bin/env python3
"""
EJU 扫描版 PDF 本地预处理流水线：
1. 按每 15 页（或有效章级书签）切分 PDF 至 chunks/
2. 导出 110 DPI 灰度低分辨率参考图至 ref_imgs/
3. 调用 macOS 原生 Apple Vision (VNRecognizeTextRequest) 进行高精度日文+英文/符号离线 OCR
4. 按切片输出结构化 Markdown 底稿至 ocr_md/
"""

import os
import sys
import time
from pathlib import Path
import pymupdf
import objc
import Foundation
import Vision


BOOKS = [
    ("physics", "raw_eju_physics.pdf"),
    ("chemistry", "raw_eju_chemistry.pdf"),
    ("math", "raw_eju_math.pdf"),
]

CHUNK_SIZE = 15
REF_IMG_DPI = 110
OCR_DPI = 250


def has_valid_chapter_toc(doc: pymupdf.Document) -> list[tuple[int, int, str]]:
    """
    检查 PDF 是否包含有效的章级书签目录。
    若书签只是逐页合并生成的伪目录（如每页一条、或大量页码为 -1），则返回空列表并回退到固定页数切分。
    """
    toc = doc.get_toc()
    total_pages = len(doc)
    if not toc:
        return []

    # 若大量书签页码无效（如 -1），说明不是有效目录
    valid_toc = [entry for entry in toc if 1 <= entry[2] <= total_pages]
    if len(valid_toc) < len(toc) * 0.8:
        return []

    # 提取有效的一级书签 (level == 1, page >= 1)
    l1_entries = [(title.strip(), page) for level, title, page in valid_toc if level == 1]
    if len(l1_entries) < 3:
        return []

    # 去重并按页码排序
    unique_starts = []
    seen_pages = set()
    for title, page in sorted(l1_entries, key=lambda x: x[1]):
        if page not in seen_pages:
            seen_pages.add(page)
            unique_starts.append((page, title))

    # 如果章节数过少或过多（如每页一条），则回退到固定页数切分
    if len(unique_starts) < 3 or len(unique_starts) > max(3, total_pages // 5):
        return []

    ranges = []
    for i, (start_p, title) in enumerate(unique_starts):
        end_p = unique_starts[i + 1][0] - 1 if i + 1 < len(unique_starts) else total_pages
        if start_p <= end_p:
            if (end_p - start_p + 1) > 50:
                return []
            ranges.append((start_p, end_p, title))
    return ranges


def build_chunk_ranges(doc: pymupdf.Document, chunk_size: int = CHUNK_SIZE) -> list[tuple[int, int]]:
    """生成 1-indexed 的切片页码范围列表 [(start_page, end_page), ...]"""
    chapter_ranges = has_valid_chapter_toc(doc)
    if chapter_ranges:
        return [(s, e) for s, e, _ in chapter_ranges]

    total_pages = len(doc)
    return [
        (start, min(start + chunk_size - 1, total_pages))
        for start in range(1, total_pages + 1, chunk_size)
    ]


def ocr_png_bytes_with_vision(png_bytes: bytes) -> list[str]:
    """使用 macOS 原生 Apple Vision 对 PNG 字节流执行高精度 OCR"""
    with objc.autorelease_pool():
        ns_data = Foundation.NSData.dataWithBytes_length_(png_bytes, len(png_bytes))
        handler = Vision.VNImageRequestHandler.alloc().initWithData_options_(ns_data, None)

        request = Vision.VNRecognizeTextRequest.alloc().init()
        request.setRecognitionLanguages_(["ja-JP", "en-US"])
        request.setRecognitionLevel_(Vision.VNRequestTextRecognitionLevelAccurate)
        request.setUsesLanguageCorrection_(True)

        success, error = handler.performRequests_error_([request], None)
        if not success:
            err_msg = str(error) if error else "Unknown Vision error"
            raise RuntimeError(f"Apple Vision OCR failed: {err_msg}")

        lines = []
        for obs in request.results() or []:
            candidates = obs.topCandidates_(1)
            if candidates and len(candidates) > 0:
                text = str(candidates[0].string()).strip()
                if text:
                    lines.append(text)
        return lines


def process_book(subject: str, pdf_path: Path, base_dir: Path) -> dict:
    """处理单本教材：切分 PDF、导出参考图、执行 OCR 并输出 Markdown"""
    work_dir = base_dir / f"work_{subject}"
    chunks_dir = work_dir / "chunks"
    ocr_dir = work_dir / "ocr_md"
    ref_dir = work_dir / "ref_imgs"

    for d in (chunks_dir, ocr_dir, ref_dir):
        d.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(str(pdf_path))
    total_pages = len(doc)
    chunk_ranges = build_chunk_ranges(doc, CHUNK_SIZE)
    total_chunks = len(chunk_ranges)

    print(f"\n{'='*60}", flush=True)
    print(f"开始处理: {pdf_path.name} -> {work_dir.name}/", flush=True)
    print(f"总页数: {total_pages} | 切片总数: {total_chunks}", flush=True)
    print(f"{'='*60}", flush=True)

    t0 = time.time()
    completed_chunks = 0
    total_ocr_pages = 0

    for idx, (start_p, end_p) in enumerate(chunk_ranges, start=1):
        chunk_pdf_name = f"chunk_{idx:03d}_p{start_p}-{end_p}.pdf"
        chunk_md_name = f"ocr_{idx:03d}_p{start_p}-{end_p}.md"
        chunk_pdf_path = chunks_dir / chunk_pdf_name
        chunk_md_path = ocr_dir / chunk_md_name

        # 1. 切分小 PDF（若不存在则生成）
        if not chunk_pdf_path.exists():
            sub_doc = pymupdf.open()
            sub_doc.insert_pdf(doc, from_page=start_p - 1, to_page=end_p - 1)
            sub_doc.save(str(chunk_pdf_path), deflate=True)
            sub_doc.close()

        # 2. 导出低分辨率灰度参考图 + 执行 OCR
        md_blocks = []
        need_ocr = not chunk_md_path.exists()

        for pno in range(start_p, end_p + 1):
            page = doc[pno - 1]
            ref_img_name = f"page_{pno:04d}.jpg"
            ref_img_path = ref_dir / ref_img_name

            if not ref_img_path.exists():
                gray_pix = page.get_pixmap(dpi=REF_IMG_DPI, colorspace=pymupdf.csGRAY, alpha=False)
                gray_pix.save(str(ref_img_path), jpg_quality=75)

            if need_ocr:
                ocr_pix = page.get_pixmap(dpi=OCR_DPI, colorspace=pymupdf.csGRAY, alpha=False)
                png_bytes = ocr_pix.tobytes("png")
                lines = ocr_png_bytes_with_vision(png_bytes)

                header = f"--- 第 {pno} 页 (对应参考图: ref_imgs/{ref_img_name}) ---"
                body = "\n".join(lines) if lines else "(本页未识别到文本)"
                md_blocks.append(f"{header}\n{body}\n")
                total_ocr_pages += 1

        if need_ocr:
            chunk_md_path.write_text("\n".join(md_blocks), encoding="utf-8")
        else:
            total_ocr_pages += (end_p - start_p + 1)

        completed_chunks += 1
        elapsed = time.time() - t0
        print(
            f"[{subject}] 切片 {idx:03d}/{total_chunks:03d} ({chunk_pdf_name}) 完成 "
            f"| 累计耗时: {elapsed:.1f}s",
            flush=True,
        )

    doc.close()
    total_time = time.time() - t0
    return {
        "subject": subject,
        "pdf": pdf_path.name,
        "total_pages": total_pages,
        "total_chunks": total_chunks,
        "completed_chunks": completed_chunks,
        "total_ocr_pages": total_ocr_pages,
        "elapsed_sec": round(total_time, 1),
    }


def main() -> int:
    base_dir = Path(__file__).resolve().parent.parent
    summaries = []

    for subject, filename in BOOKS:
        pdf_path = base_dir / filename
        if not pdf_path.exists():
            print(f"警告: 未找到 {pdf_path}，跳过。", file=sys.stderr, flush=True)
            continue
        summary = process_book(subject, pdf_path, base_dir)
        summaries.append(summary)

    print("\n" + "=" * 60, flush=True)
    print("全部教材预处理完成！汇总报告：", flush=True)
    for s in summaries:
        print(
            f"- {s['pdf']} (work_{s['subject']}/): "
            f"共 {s['total_pages']} 页, {s['total_chunks']} 个切片, "
            f"OCR 完成 {s['completed_chunks']}/{s['total_chunks']} 切片 "
            f"({s['total_ocr_pages']} 页), 耗时 {s['elapsed_sec']}s",
            flush=True,
        )
    print("=" * 60, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
