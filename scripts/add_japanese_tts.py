#!/usr/bin/env python3
"""
Inject browser-native Japanese Web Speech API (TTS) support into:
  - eju_chemistry_solutions.html
  - eju_physics_solutions.html
  - eju_math_solutions.html

Features:
  1. Auto-detects Japanese vocabulary items (both <li><strong>...</strong> and plain <li>...)
     and extracts the kana reading inside parentheses so specialized kanji terms are never mispronounced.
  2. Auto-detects formula oral reading items (Chemistry 读法 <code>, Physics 「...」 <td>, Math 课堂读法 <strong>).
  3. Adds click-to-speak on terms & speaker buttons, plus "▶ 朗读本节" sequential playback on vocab sections.
  4. Adds floating "🔊 朗读日语" button when selecting any Japanese text on the page.
  5. Adds speed toggle (1.0x / 0.75x / 1.2x) to the unified topbar, respecting light/warm/dark themes and @media print.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TARGETS = [
    ROOT / "eju_chemistry_solutions.html",
    ROOT / "eju_physics_solutions.html",
    ROOT / "eju_math_solutions.html",
]

CSS_START = "/* === EJU Japanese TTS START === */"
CSS_END = "/* === EJU Japanese TTS END === */"

TTS_CSS = f"""
    {CSS_START}
    .jp-tts-term {{
      cursor: pointer;
      border-radius: 4px;
      transition: background-color 0.15s ease, color 0.15s ease;
    }}
    .jp-tts-term:hover {{
      background-color: var(--primary-light, #eff6ff);
      color: var(--accent, #2563eb);
    }}
    .jp-tts-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      vertical-align: middle;
      margin-left: 5px;
      margin-right: 2px;
      padding: 1px 6px;
      font-size: 0.8em;
      line-height: 1.3;
      border: 1px solid var(--border, #e2e8f0);
      border-radius: 999px;
      background: var(--surface, #ffffff);
      color: var(--accent, #2563eb);
      cursor: pointer;
      user-select: none;
      transition: transform 0.12s ease, background-color 0.15s ease, border-color 0.15s ease, color 0.15s ease;
    }}
    .jp-tts-btn:hover {{
      background: var(--primary-light, #eff6ff);
      border-color: var(--accent, #2563eb);
      transform: scale(1.06);
    }}
    .jp-tts-btn:active {{
      transform: scale(0.95);
    }}
    .jp-tts-speaking {{
      background-color: var(--primary-light, #eff6ff) !important;
      color: var(--accent, #2563eb) !important;
      outline: 1.5px solid var(--accent, #2563eb);
      border-radius: 4px;
    }}
    .jp-tts-btn.jp-tts-speaking {{
      background: var(--accent, #2563eb) !important;
      color: #ffffff !important;
      border-color: var(--accent, #2563eb) !important;
      outline: none;
      animation: jpTtsPulse 0.9s ease-in-out infinite;
    }}
    @keyframes jpTtsPulse {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.12); }}
    }}
    .jp-tts-section-btn {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      margin-left: 10px;
      padding: 2px 10px;
      font-size: 12px;
      font-weight: 600;
      line-height: 1.5;
      vertical-align: middle;
      border: 1px solid var(--border, #e2e8f0);
      border-radius: 999px;
      background: var(--surface, #ffffff);
      color: var(--accent, #2563eb);
      cursor: pointer;
      user-select: none;
      transition: background-color 0.15s ease, border-color 0.15s ease, color 0.15s ease;
    }}
    .jp-tts-section-btn:hover {{
      background: var(--primary-light, #eff6ff);
      border-color: var(--accent, #2563eb);
    }}
    .jp-tts-section-btn.is-playing {{
      background: var(--accent, #2563eb);
      color: #ffffff;
      border-color: var(--accent, #2563eb);
    }}
    .jp-tts-oral {{
      cursor: pointer;
      border-radius: 4px;
      transition: background-color 0.15s ease;
    }}
    .jp-tts-oral:hover {{
      background-color: var(--primary-light, #eff6ff);
    }}
    #jp-tts-float {{
      position: fixed;
      z-index: 1500;
      display: none;
      align-items: center;
      gap: 4px;
      padding: 5px 11px;
      font-size: 13px;
      font-weight: 600;
      border: 1px solid var(--accent, #2563eb);
      border-radius: 999px;
      background: var(--surface, #ffffff);
      color: var(--accent, #2563eb);
      box-shadow: 0 4px 14px rgba(15, 23, 42, 0.18);
      cursor: pointer;
      user-select: none;
    }}
    #jp-tts-float:hover {{
      background: var(--accent, #2563eb);
      color: #ffffff;
    }}
    #jp-tts-toast {{
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 1600;
      display: none;
      max-width: 90vw;
      padding: 8px 16px;
      font-size: 13px;
      border-radius: 8px;
      background: rgba(15, 23, 42, 0.92);
      color: #f8fafc;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
    }}
    @media print {{
      .jp-tts-btn,
      .jp-tts-section-btn,
      #jp-tts-float,
      #jp-tts-toast,
      #ejuTtsSpeedBtn {{
        display: none !important;
      }}
    }}
    {CSS_END}
"""

JS_START = "<!-- EJU_JP_TTS_START -->"
JS_END = "<!-- EJU_JP_TTS_END -->"

TTS_JS = f"""{JS_START}
<script>
(function () {{
  'use strict';

  var KANA_RE = /[\\u3041-\\u3096\\u30A1-\\u30FA\\u30FC]/;
  var SPEEDS = [
    {{ rate: 1.0, label: '🔊 1.0x', title: '日语发音语速：正常（点击切换 0.75x 慢速）' }},
    {{ rate: 0.75, label: '🔊 0.75x', title: '日语发音语速：慢速（点击切换 1.2x 快速）' }},
    {{ rate: 1.2, label: '🔊 1.2x', title: '日语发音语速：快速（点击切换 1.0x 正常）' }}
  ];

  var speedIdx = 0;
  try {{
    var savedIdx = parseInt(localStorage.getItem('eju_jp_tts_speed_idx') || '0', 10);
    if (!isNaN(savedIdx) && savedIdx >= 0 && savedIdx < SPEEDS.length) speedIdx = savedIdx;
  }} catch (e) {{}}

  var jpVoice = null;
  var activeEls = [];
  var seqState = null; // {{ btn, items, index, timer }}
  var toastTimer = null;

  function showToast(msg) {{
    var el = document.getElementById('jp-tts-toast');
    if (!el) {{
      el = document.createElement('div');
      el.id = 'jp-tts-toast';
      document.body.appendChild(el);
    }}
    el.textContent = msg;
    el.style.display = 'block';
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {{ el.style.display = 'none'; }}, 3600);
  }}

  function pickJapaneseVoice() {{
    if (!('speechSynthesis' in window)) return null;
    var voices = window.speechSynthesis.getVoices() || [];
    var jaVoices = voices.filter(function (v) {{
      return v.lang && v.lang.toLowerCase().replace('_', '-').indexOf('ja') === 0;
    }});
    if (!jaVoices.length) return null;

    // Prefer high-quality natural Japanese voices
    var prefs = [
      /Google\\s*日本語/i,
      /Nanami/i,
      /Keita/i,
      /Kyoko/i,
      /Hattori/i,
      /O-Ren/i,
      /Otoya/i,
      /Haruka/i,
      /Ayumi/i
    ];
    for (var i = 0; i < prefs.length; i++) {{
      for (var j = 0; j < jaVoices.length; j++) {{
        if (prefs[i].test(jaVoices[j].name)) return jaVoices[j];
      }}
    }}
    return jaVoices[0];
  }}

  if ('speechSynthesis' in window) {{
    jpVoice = pickJapaneseVoice();
    window.speechSynthesis.onvoiceschanged = function () {{
      jpVoice = pickJapaneseVoice();
    }};
  }}

  function clearActiveHighlight() {{
    for (var i = 0; i < activeEls.length; i++) {{
      activeEls[i].classList.remove('jp-tts-speaking');
    }}
    activeEls = [];
  }}

  function stopSequence() {{
    if (!seqState) return;
    clearTimeout(seqState.timer);
    if (seqState.btn) {{
      seqState.btn.classList.remove('is-playing');
      seqState.btn.textContent = seqState.btn.getAttribute('data-idle-label') || '▶ 朗读本节';
    }}
    seqState = null;
  }}

  function cleanTtsText(raw) {{
    if (!raw) return '';
    return raw
      .replace(/[「」『』]/g, '')
      .replace(/[・／\\/]/g, '、')
      .replace(/\\s+/g, ' ')
      .trim();
  }}

  function speakJapanese(text, highlightEls, onEnd) {{
    if (!('speechSynthesis' in window)) {{
      showToast('当前浏览器不支持原生语音合成（Web Speech API），建议使用 Chrome / Safari / Edge。');
      return;
    }}
    var cleaned = cleanTtsText(text);
    if (!cleaned) return;

    if (!jpVoice) jpVoice = pickJapaneseVoice();

    try {{
      window.speechSynthesis.cancel();
    }} catch (e) {{}}
    clearActiveHighlight();

    var utt = new SpeechSynthesisUtterance(cleaned);
    utt.lang = 'ja-JP';
    utt.rate = SPEEDS[speedIdx].rate;
    if (jpVoice) utt.voice = jpVoice;

    // Keep reference to avoid Chrome GC bug
    window.__ejuTtsUtterance = utt;

    if (highlightEls && highlightEls.length) {{
      activeEls = highlightEls;
      for (var i = 0; i < activeEls.length; i++) {{
        activeEls[i].classList.add('jp-tts-speaking');
      }}
    }}

    var finished = false;
    function done() {{
      if (finished) return;
      finished = true;
      clearActiveHighlight();
      if (typeof onEnd === 'function') onEnd();
    }}

    utt.onend = done;
    utt.onerror = function (ev) {{
      done();
      if (ev && ev.error && ev.error !== 'interrupted' && ev.error !== 'canceled') {{
        if (!jpVoice) {{
          showToast('未检测到系统日语语音包，建议在 Chrome 联网使用或安装系统日语语音。');
        }}
      }}
    }};

    window.speechSynthesis.speak(utt);
  }}

  /**
   * Extract Japanese kana reading from "Term（kana / romaji）" or "Term（kana）".
   * Returns null if not a Japanese vocabulary pattern.
   */
  function extractVocabReading(fullText) {{
    var t = (fullText || '').trim();
    if (!t || t.length > 160) return null;
    // Match outer parentheses at the end: 物質の構成（ぶっしつのこうせい / busshitsu no kōsei）
    var m = t.match(/^(.+?)[（(]([^）)]+)[）)]$/);
    if (!m) return null;
    var head = m[1].trim();
    var inside = m[2].trim();

    // Case 1: "kana / romaji" format (our primary vocab & glossary format)
    if (inside.indexOf('/') !== -1) {{
      var parts = inside.split('/');
      var reading = parts[0].trim();
      if (KANA_RE.test(reading)) {{
        return reading;
      }}
    }}
    // Case 2: "中文（日文含假名）" or "日文（纯假名）"
    if (KANA_RE.test(inside) && !/\\$/.test(inside) && inside.length <= 45) {{
      // Skip explanatory Chinese notes that happen to contain a stray kana
      var cnPunct = /[。，：；！？]/.test(inside);
      if (!cnPunct) {{
        return inside;
      }}
    }}
    // Fallback: if head itself has kana and inside has no kana, don't misread Chinese
    if (KANA_RE.test(head) && KANA_RE.test(inside)) {{
      return inside;
    }}
    return null;
  }}

  function createSpeakBtn(ttsText, targetEl) {{
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'jp-tts-btn';
    btn.textContent = '🔊';
    btn.title = '点击朗读日语：' + ttsText;
    btn.setAttribute('aria-label', '朗读日语：' + ttsText);
    btn.addEventListener('click', function (e) {{
      e.preventDefault();
      e.stopPropagation();
      stopSequence();
      speakJapanese(ttsText, targetEl ? [targetEl, btn] : [btn]);
    }});
    return btn;
  }}

  function bindTermElement(el, ttsText) {{
    if (el.getAttribute('data-tts-bound') === '1') return null;
    el.setAttribute('data-tts-bound', '1');
    el.setAttribute('data-tts-text', ttsText);
    el.classList.add('jp-tts-term');
    el.title = '点击朗读日语：' + ttsText;

    var btn = createSpeakBtn(ttsText, el);
    el.insertAdjacentElement('afterend', btn);

    el.addEventListener('click', function (e) {{
      // Don't hijack text selection
      var sel = window.getSelection ? String(window.getSelection()).trim() : '';
      if (sel.length > 0) return;
      e.stopPropagation();
      stopSequence();
      speakJapanese(ttsText, [el, btn]);
    }});

    return {{ el: el, btn: btn, text: ttsText }};
  }}

  function getCleanElementText(el) {{
    if (!el) return '';
    if (!el.querySelector('.katex')) return el.textContent || '';
    var clone = el.cloneNode(true);
    var katexNodes = clone.querySelectorAll('.katex');
    for (var i = 0; i < katexNodes.length; i++) {{
      katexNodes[i].remove();
    }}
    return clone.textContent || '';
  }}

  function enhanceVocabLists(root) {{
    var lis = root.querySelectorAll('li');
    for (var i = 0; i < lis.length; i++) {{
      var li = lis[i];
      if (li.closest('aside, nav, .sidebar, .toc-sub')) continue;

      // Pattern 1: <li><strong>Term（kana / romaji）</strong> — ...</li>
      var firstEl = li.firstElementChild;
      if (firstEl && firstEl.tagName === 'STRONG' && (!li.firstChild || firstEl === li.firstChild || (li.firstChild.nodeType === 3 && !li.firstChild.nodeValue.trim()))) {{
        var reading = extractVocabReading(getCleanElementText(firstEl));
        if (reading) {{
          bindTermElement(firstEl, reading);
          continue;
        }}
      }}

      // Pattern 2: Plain text <li>Term（kana / romaji） — ...</li> (Math 2.1 & Chemistry glossary-all)
      var firstNode = li.firstChild;
      if (firstNode && firstNode.nodeType === 3) {{
        var txt = firstNode.nodeValue || '';
        var m = txt.match(/^(\\s*)([^—–\\n]+?[（(][^）)\\n]+[）)])(\\s*[—–\\-].*|$)/);
        if (m) {{
          var leadSpace = m[1];
          var termPart = m[2];
          var restPart = m[3];
          var reading2 = extractVocabReading(termPart);
          if (reading2) {{
            var span = document.createElement('span');
            span.textContent = termPart;
            if (leadSpace) {{
              li.insertBefore(document.createTextNode(leadSpace), firstNode);
            }}
            li.insertBefore(span, firstNode);
            firstNode.nodeValue = restPart;
            bindTermElement(span, reading2);
          }}
        }}
      }}
    }}
  }}

  function enhanceOralReadings(root) {{
    // 1) Chemistry: <li class="sub-item">读法：<code>...kana...</code>...</li>
    var codes = root.querySelectorAll('li code');
    for (var i = 0; i < codes.length; i++) {{
      var code = codes[i];
      if (code.getAttribute('data-tts-bound') === '1') continue;
      var li = code.closest('li');
      if (!li || !/读法|念法/.test(li.textContent || '')) continue;
      var txt = (code.textContent || '').trim();
      if (txt.length >= 2 && KANA_RE.test(txt)) {{
        code.setAttribute('data-tts-bound', '1');
        code.classList.add('jp-tts-oral');
        code.title = '点击朗读日语口语读法';
        var btn = createSpeakBtn(txt, code);
        code.insertAdjacentElement('afterend', btn);
        (function (c, b, t) {{
          c.addEventListener('click', function () {{
            stopSequence();
            speakJapanese(t, [c, b]);
          }});
        }})(code, btn, txt);
      }}
    }}

    // 2) Math: <li>课堂读法：<strong>...kana...</strong></li>
    var strongs = root.querySelectorAll('li strong');
    for (var j = 0; j < strongs.length; j++) {{
      var st = strongs[j];
      if (st.getAttribute('data-tts-bound') === '1') continue;
      var prev = st.previousSibling;
      if (prev && prev.nodeType === 3 && /课堂读法|读法/.test(prev.nodeValue || '')) {{
        var txt2 = (st.textContent || '').trim();
        if (txt2.length >= 2 && KANA_RE.test(txt2)) {{
          st.setAttribute('data-tts-bound', '1');
          st.classList.add('jp-tts-oral');
          st.title = '点击朗读日语课堂读法';
          var btn2 = createSpeakBtn(txt2, st);
          st.insertAdjacentElement('afterend', btn2);
          (function (s, b, t) {{
            s.addEventListener('click', function () {{
              stopSequence();
              speakJapanese(t, [s, b]);
            }});
          }})(st, btn2, txt2);
        }}
      }}
    }}

    // 3) Physics: <td>「...kana...」</td> in formula oral reading tables
    var tds = root.querySelectorAll('td');
    for (var k = 0; k < tds.length; k++) {{
      var td = tds[k];
      if (td.getAttribute('data-tts-bound') === '1') continue;
      var txt3 = (td.textContent || '').trim();
      if (txt3.length >= 4 && txt3.charAt(0) === '「' && txt3.charAt(txt3.length - 1) === '」' && KANA_RE.test(txt3)) {{
        td.setAttribute('data-tts-bound', '1');
        td.classList.add('jp-tts-oral');
        td.title = '点击朗读公式日语读法';
        var btn3 = createSpeakBtn(txt3, td);
        td.appendChild(btn3);
        (function (cell, b, t) {{
          cell.addEventListener('click', function (e) {{
            if (e.target === b) return;
            var sel = window.getSelection ? String(window.getSelection()).trim() : '';
            if (sel.length > 0) return;
            stopSequence();
            speakJapanese(t, [cell, b]);
          }});
        }})(td, btn3, txt3);
      }}
    }}
  }}

  function addSectionPlayButtons(root) {{
    var lists = root.querySelectorAll('ul');
    for (var i = 0; i < lists.length; i++) {{
      var ul = lists[i];
      if (ul.closest('aside, nav, .sidebar, .toc-sub')) continue;
      var terms = ul.querySelectorAll('.jp-tts-term');
      if (terms.length < 3) continue;

      // Find preceding heading (h3 or h2)
      var prev = ul.previousElementSibling;
      while (prev && prev.tagName === 'P') {{
        prev = prev.previousElementSibling;
      }}
      if (!prev || (prev.tagName !== 'H3' && prev.tagName !== 'H2')) continue;
      if (prev.querySelector('.jp-tts-section-btn')) continue;

      var idleLabel = '▶ 朗读本节 (' + terms.length + '词)';
      var secBtn = document.createElement('button');
      secBtn.type = 'button';
      secBtn.className = 'jp-tts-section-btn';
      secBtn.textContent = idleLabel;
      secBtn.setAttribute('data-idle-label', idleLabel);
      secBtn.title = '依次自动朗读本节全部日语词汇（再次点击停止）';

      (function (listEl, buttonEl) {{
        buttonEl.addEventListener('click', function (e) {{
          e.preventDefault();
          e.stopPropagation();

          if (seqState && seqState.btn === buttonEl) {{
            stopSequence();
            try {{ window.speechSynthesis.cancel(); }} catch (err) {{}}
            clearActiveHighlight();
            return;
          }}

          stopSequence();
          var items = Array.prototype.slice.call(listEl.querySelectorAll('.jp-tts-term'));
          if (!items.length) return;

          buttonEl.classList.add('is-playing');
          seqState = {{ btn: buttonEl, items: items, index: 0, timer: null }};

          function playNext() {{
            if (!seqState || seqState.btn !== buttonEl) return;
            if (seqState.index >= seqState.items.length) {{
              stopSequence();
              return;
            }}
            var cur = seqState.items[seqState.index];
            var curBtn = cur.nextElementSibling && cur.nextElementSibling.classList.contains('jp-tts-btn')
              ? cur.nextElementSibling : null;
            var text = cur.getAttribute('data-tts-text') || '';
            buttonEl.textContent = '⏹ 停止 (' + (seqState.index + 1) + '/' + seqState.items.length + ')';

            // Gently scroll into view if outside viewport
            var rect = cur.getBoundingClientRect();
            if (rect.top < 64 || rect.bottom > window.innerHeight - 40) {{
              cur.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            }}

            seqState.index += 1;
            speakJapanese(text, curBtn ? [cur, curBtn] : [cur], function () {{
              if (!seqState || seqState.btn !== buttonEl) return;
              seqState.timer = setTimeout(playNext, 550);
            }});
          }}

          playNext();
        }});
      }})(ul, secBtn);

      prev.appendChild(secBtn);
    }}
  }}

  function setupTopbarSpeedControl() {{
    var controls = document.querySelector('.eju-topbar .topbar-controls, header.topbar .topbar-controls');
    if (!controls || document.getElementById('ejuTtsSpeedBtn')) return;

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.id = 'ejuTtsSpeedBtn';
    btn.className = 'btn';
    btn.textContent = SPEEDS[speedIdx].label;
    btn.title = SPEEDS[speedIdx].title;

    btn.addEventListener('click', function () {{
      speedIdx = (speedIdx + 1) % SPEEDS.length;
      btn.textContent = SPEEDS[speedIdx].label;
      btn.title = SPEEDS[speedIdx].title;
      try {{ localStorage.setItem('eju_jp_tts_speed_idx', String(speedIdx)); }} catch (e) {{}}
      showToast('日语朗读语速已切换为 ' + SPEEDS[speedIdx].rate + 'x');
    }});

    controls.insertBefore(btn, controls.firstChild);
  }}

  function setupSelectionSpeak() {{
    var floatBtn = document.createElement('button');
    floatBtn.type = 'button';
    floatBtn.id = 'jp-tts-float';
    floatBtn.textContent = '🔊 朗读日语';
    document.body.appendChild(floatBtn);

    var selectedText = '';

    floatBtn.addEventListener('mousedown', function (e) {{
      e.preventDefault();
    }});
    floatBtn.addEventListener('click', function (e) {{
      e.preventDefault();
      e.stopPropagation();
      if (selectedText) {{
        stopSequence();
        speakJapanese(selectedText);
      }}
      floatBtn.style.display = 'none';
    }});

    function updateFloat() {{
      var sel = window.getSelection ? window.getSelection() : null;
      var txt = sel ? String(sel).trim() : '';
      if (!txt || txt.length > 140 || !KANA_RE.test(txt)) {{
        floatBtn.style.display = 'none';
        selectedText = '';
        return;
      }}
      try {{
        var range = sel.getRangeAt(0);
        var rect = range.getBoundingClientRect();
        if (!rect || (rect.width === 0 && rect.height === 0)) {{
          floatBtn.style.display = 'none';
          return;
        }}
        selectedText = txt;
        var top = Math.max(58, rect.top - 38);
        var left = Math.min(window.innerWidth - 130, Math.max(12, rect.left + rect.width / 2 - 52));
        floatBtn.style.top = top + 'px';
        floatBtn.style.left = left + 'px';
        floatBtn.style.display = 'inline-flex';
      }} catch (e) {{
        floatBtn.style.display = 'none';
      }}
    }}

    document.addEventListener('mouseup', function () {{ setTimeout(updateFloat, 20); }});
    document.addEventListener('touchend', function () {{ setTimeout(updateFloat, 60); }});
    document.addEventListener('scroll', function () {{
      if (floatBtn.style.display !== 'none') floatBtn.style.display = 'none';
    }}, {{ passive: true }});
  }}

  function init() {{
    setupTopbarSpeedControl();
    var root = document.querySelector('main, #main, .main, .content') || document.body;
    enhanceVocabLists(root);
    enhanceOralReadings(root);
    addSectionPlayButtons(root);
    setupSelectionSpeak();
  }}

  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', init);
  }} else {{
    init();
  }}
}})();
</script>
{JS_END}"""


def inject_into_file(path: Path) -> None:
    html = path.read_text(encoding="utf-8")

    # 1. Replace or inject CSS right before </style>
    css_pattern = re.compile(
        re.escape(CSS_START) + r".*?" + re.escape(CSS_END),
        re.S,
    )
    if css_pattern.search(html):
        html = css_pattern.sub(lambda _: TTS_CSS.strip(), html, count=1)
    else:
        idx = html.rfind("</style>")
        if idx == -1:
            raise RuntimeError(f"No </style> found in {path}")
        html = html[:idx] + TTS_CSS + "\n  " + html[idx:]

    # 2. Replace or inject JS right before </body>
    js_pattern = re.compile(
        re.escape(JS_START) + r".*?" + re.escape(JS_END),
        re.S,
    )
    if js_pattern.search(html):
        html = js_pattern.sub(lambda _: TTS_JS, html, count=1)
    else:
        idx = html.rfind("</body>")
        if idx == -1:
            raise RuntimeError(f"No </body> found in {path}")
        html = html[:idx] + TTS_JS + "\n" + html[idx:]

    path.write_text(html, encoding="utf-8")
    print(f"Injected Japanese TTS into {path.name} ({len(html):,} chars)")


def main() -> None:
    for p in TARGETS:
        if not p.exists():
            print(f"WARNING: {p} not found, skipping.")
            continue
        inject_into_file(p)


if __name__ == "__main__":
    main()
