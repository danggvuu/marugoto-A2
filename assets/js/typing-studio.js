/**
 * typing-studio.js
 * Modular Typing Studio engine for L11-L18 Sentences, Kanji -> Hiragana, and A2 Vocab.
 * Relies on JpTypingGrader (assets/js/jp-typing-grader.js) for flexible natural-Japanese grading.
 */
(function (window) {
    'use strict';

    window.tpInitialized = false;
    window.tpState = {
        mode: 'sentence', // 'sentence' | 'kanji' | 'vocab'
        filterByMode: { sentence: 'all', kanji: '15-18', vocab: 'all' },
        idxByBucket: {},
        orderByBucket: {},
        history: {}, // id -> { status: 'ok'|'err'|'reveal', lastInput, whyWrong, isKanjiMatch, variantNote }
        drafts: {},  // id -> raw unsaved input text
        allowKanji: false,
        autoAdvance: false,
        showOverview: false,
        streak: 0,
        gradedCurrent: false
    };

    function getDataSource(key) {
        if (window.MINI_15_18_DATA && window.MINI_15_18_DATA[key]) {
            return window.MINI_15_18_DATA[key];
        }
        return window[key] || [];
    }

    function escapeHtml(str) {
        return String(str || '')
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;');
    }

    function toHiragana(str) {
        return window.JpTypingGrader ? window.JpTypingGrader.toHiragana(str) : String(str || '').toLowerCase();
    }

    function cleanJpCompare(str, convertKata) {
        return window.JpTypingGrader
            ? window.JpTypingGrader.cleanCompare(str, convertKata)
            : String(str || '').toLowerCase().trim();
    }

    function containsKanji(str) {
        return window.JpTypingGrader
            ? window.JpTypingGrader.containsKanji(str)
            : /[\u4E00-\u9FAF\u3400-\u4DBF]/.test(str || '');
    }

    function stripDakutenChar(ch) {
        var map = {
            'が': 'か', 'ぎ': 'き', 'ぐ': 'く', 'げ': 'け', 'ご': 'こ',
            'ざ': 'さ', 'じ': 'し', 'ず': 'す', 'ぜ': 'せ', 'ぞ': 'そ',
            'だ': 'た', 'ぢ': 'ち', 'づ': 'つ', 'で': 'て', 'ど': 'と',
            'ば': 'は', 'び': 'ひ', 'ぶ': 'ふ', 'べ': 'へ', 'ぼ': 'ほ',
            'ぱ': 'は', 'ぴ': 'ひ', 'ぷ': 'ふ', 'ぺ': 'へ', 'ぽ': 'ほ',
            'ゔ': 'う'
        };
        return map[ch] || ch;
    }

    function stripDakutenStr(s) {
        return Array.from(s || '').map(stripDakutenChar).join('');
    }

    function collapseLongVowels(s) {
        return (s || '')
            .replace(/ー/g, '')
            .replace(/([おこそとのほもよろをごぞどぼぽうくすつぬふむゆるぐずづぶぷ])う/g, '$1')
            .replace(/([えけせてねへめれげぜでべぺい])い/g, '$1')
            .replace(/([あかさたなはまやらわがざだばぱ])あ/g, '$1');
    }

    function bigSmallKana(s) {
        return (s || '')
            .replace(/ゃ/g, 'や').replace(/ゅ/g, 'ゆ').replace(/ょ/g, 'よ')
            .replace(/っ/g, 'つ').replace(/ぁ/g, 'あ').replace(/ぃ/g, 'い')
            .replace(/ぅ/g, 'う').replace(/ぇ/g, 'え').replace(/ぉ/g, 'お');
    }

    function buildCharDiffHtml(typedRaw, targetRaw) {
        var a = Array.from(cleanJpCompare(typedRaw, true));
        var b = Array.from(cleanJpCompare(targetRaw, true));
        var typedHtml = '';
        var targetHtml = '';
        var prefix = 0;
        while (prefix < a.length && prefix < b.length && a[prefix] === b[prefix]) prefix++;
        var suffix = 0;
        while (
            suffix < (a.length - prefix) &&
            suffix < (b.length - prefix) &&
            a[a.length - 1 - suffix] === b[b.length - 1 - suffix]
        ) suffix++;

        for (var i = 0; i < prefix; i++) {
            typedHtml += '<span class="diff-good">' + escapeHtml(a[i]) + '</span>';
            targetHtml += '<span class="diff-good">' + escapeHtml(b[i]) + '</span>';
        }
        var midA = a.slice(prefix, a.length - suffix);
        var midB = b.slice(prefix, b.length - suffix);
        if (midA.length) typedHtml += '<span class="diff-bad">' + escapeHtml(midA.join('')) + '</span>';
        if (midB.length) targetHtml += '<span class="diff-good" style="background:#fde68a;color:#92400e;">' + escapeHtml(midB.join('')) + '</span>';
        for (var j = a.length - suffix; j < a.length; j++) {
            typedHtml += '<span class="diff-good">' + escapeHtml(a[j]) + '</span>';
        }
        for (var k = b.length - suffix; k < b.length; k++) {
            targetHtml += '<span class="diff-good">' + escapeHtml(b[k]) + '</span>';
        }
        return {
            typedHtml: typedHtml || '<em style="color:var(--gray-400);">(trống)</em>',
            targetHtml: targetHtml,
            expectedChunk: midB.join(''),
            gotChunk: midA.join('')
        };
    }

    function diagnoseTypingMistake(rawUser, item, mode) {
        var reasons = [];
        var normUserHira = cleanJpCompare(rawUser, true);
        var targetSample = mode === 'sentence' ? item.hira : (mode === 'kanji' ? item.kana : (item.kana || item.jp));
        var acceptedList = mode === 'sentence'
            ? (item.acceptedHira || [item.hira])
            : (mode === 'kanji' ? (item.accepted || [item.kana]) : [item.jp, item.kana, item.romaji].filter(Boolean));
        var normTarget = cleanJpCompare(targetSample, true);

        // 1. Item-specific targeted grammar / reading traps
        if (item.traps && Array.isArray(item.traps)) {
            for (var i = 0; i < item.traps.length; i++) {
                var t = item.traps[i];
                if (t.regex) {
                    var re = new RegExp(t.regex, 'i');
                    if (re.test(normUserHira) || re.test(rawUser)) {
                        reasons.push('🎯 <strong>Bẫy hay sai ở câu/từ này:</strong> ' + t.why);
                    }
                } else if (t.wrong && Array.isArray(t.wrong)) {
                    if (t.wrong.some(function (w) { return cleanJpCompare(w, true) === normUserHira; })) {
                        reasons.push('🎯 <strong>Lỗi nhầm cách đọc phổ biến:</strong> ' + t.why);
                    }
                }
            }
        }

        // 2. Typed Kanji check
        if (containsKanji(rawUser)) {
            if (mode === 'kanji') {
                reasons.push('⛩️ <strong>Bạn vừa nhập lại mặt chữ Kanji!</strong> Chế độ này yêu cầu nhập <strong>cách đọc Hiragana</strong> (không giữ chữ Hán).');
            } else if (mode === 'sentence') {
                var kanjiMatches = (item.kanjiAccepted || []).some(function (k) { return cleanJpCompare(k, true) === normUserHira; });
                if (kanjiMatches) {
                    reasons.push('⛩️ Câu bạn gõ khớp bản có chữ Hán nhưng chế độ hiện đang chấm <strong>thuần Hiragana</strong>. Hãy tắt chuyển chữ Kanji hoặc bật mục <em>"Cho phép kèm Kanji"</em> ở phía trên!');
                } else {
                    reasons.push('⛩️ Trong bài gõ có dính ký tự <strong>Kanji</strong> — hãy chuyển IME sang thuần <strong>Hiragana</strong> rồi kiểm tra lại cách chia ngữ pháp bên dưới.');
                }
            }
        }

        // 3. Forgot IME (ASCII letters typed in Hiragana modes)
        var asciiLettersOnly = (rawUser || '').replace(/fpt|youtube/ig, '');
        if (mode !== 'vocab' && /[a-zA-Z]{2,}/.test(asciiLettersOnly)) {
            reasons.push('⌨️ <strong>Có chữ cái Latinh (Romaji):</strong> Có vẻ bạn quên bật bộ gõ Hiragana tiếng Nhật (chế độ này yêu cầu nhập bằng Hiragana chứ không để Romaji thô).');
        }

        // 4. Phonological spelling diagnostics
        for (var aIdx = 0; aIdx < acceptedList.length; aIdx++) {
            var nt = cleanJpCompare(acceptedList[aIdx], true);
            if (!nt || !normUserHira) continue;
            if (normUserHira.replace(/っ/g, '') === nt.replace(/っ/g, '') && normUserHira !== nt) {
                reasons.push('✂️ <strong>Thiếu hoặc thừa âm ngắt chữ 「っ」 nhỏ:</strong> Hãy kiểm tra lại các chữ có ngắt âm đôi (như <code>さっか, けっこん, いった, かった, とった, まって, きっさてん, しゅっぱつ</code>).');
                break;
            }
            if (collapseLongVowels(normUserHira) === collapseLongVowels(nt) && normUserHira !== nt) {
                reasons.push('🔊 <strong>Sai / thiếu trường âm (<code>う, い, ー</code>):</strong> Ví dụ <code>せんしゅう</code> (có う), <code>たんじょうび</code> (có う), <code>とけい / かいけい</code> (có い), hoặc <code>セーター</code> (có ー).');
                break;
            }
            if (stripDakutenStr(normUserHira) === stripDakutenStr(nt) && normUserHira !== nt) {
                reasons.push('゛ <strong>Nhầm âm đục / bán đục (tenten <code>゛</code> hoặc maru <code>゜</code>):</strong> Ví dụ <code>が/か, ぎ/き, ぐ/く, ざ/さ, じ/し, ぞ/そ, だ/た, で/て, ば/は, ぱ/は</code>.');
                break;
            }
            if (bigSmallKana(normUserHira) === bigSmallKana(nt) && normUserHira !== nt) {
                reasons.push('🔡 <strong>Nhầm chữ nhỏ với chữ thường:</strong> Cần dùng <code>ゃ, ゅ, ょ, っ</code> nhỏ chứ không phải <code>や, ゆ, よ, つ</code> lớn (ví dụ <code>しゃ / きょ / しゅ</code>).');
                break;
            }
        }

        // 5. General comparison fallback & global PDF trap checks
        if (mode === 'sentence' && !reasons.length) {
            var isRelClause = (item.pattern || '').indexOf('＋ N') !== -1 ||
                (item.pattern || '').indexOf('＋ 人') !== -1 ||
                (item.category || '').indexOf('Bổ nghĩa') !== -1;
            var relNoFix = normUserHira.replace(/([ただいるうくぐすつぬぶむ])の/g, '$1');
            if (isRelClause && relNoFix !== normUserHira && acceptedList.some(function (acc) { return cleanJpCompare(acc, true) === relNoFix; })) {
                reasons.push('🚫 <strong>BẪY PDF L16–17 (Thừa trợ từ 「の」 trong mệnh đề bổ nghĩa):</strong> Sau động từ thể thông thường đứng trước Danh từ, TUYỆT ĐỐI KHÔNG chen 「の」 (ví dụ <em>とった しゃしん ✅</em>, không dùng <s>とったのしゃしん</s> ❌)!');
            } else {
                var diff = buildCharDiffHtml(rawUser, targetSample);
                if (normUserHira.indexOf('わ') !== -1 && normTarget.indexOf('は') !== -1 && normUserHira.replace(/わ/g, 'は') === normTarget.replace(/わ/g, 'は')) {
                    reasons.push('📌 <strong>Nhầm trợ từ 「は」 thành 「わ」:</strong> Trợ từ chủ đề câu phát âm là <em>wa</em> nhưng viết bằng chữ <strong>「は」</strong>!');
                } else if (diff.expectedChunk || diff.gotChunk) {
                    reasons.push('🔎 <strong>Lệch tại cụm ký tự:</strong> Bạn gõ <code>' + escapeHtml(diff.gotChunk || '(thiếu)') + '</code> trong khi đáp án chuẩn cần <code>' + escapeHtml(diff.expectedChunk || '(không có)') + '</code>.');
                }
            }
        } else if (mode === 'kanji' && !reasons.length) {
            var kDiff = buildCharDiffHtml(rawUser, targetSample);
            reasons.push('🔎 <strong>Đối chiếu mặt âm đọc:</strong> Bạn gõ <code>' + escapeHtml(normUserHira) + '</code>, phần khác biệt so với cách đọc chuẩn nằm ở <code>' + escapeHtml(kDiff.expectedChunk || normTarget) + '</code>.');
        }

        if (!reasons.length) {
            reasons.push('💡 Hãy kiểm tra lại trợ từ (<code>は, が, を, に, で, と</code>), cách chia thể thông thường (<code>Vる / Vない / Vた / ている / だ</code>) và đối chiếu từng vế câu bên dưới.');
        }
        return reasons;
    }

    function getModeItems(mode) {
        if (mode === 'sentence') return getDataSource('SENTENCE_TYPING_DATA');
        if (mode === 'kanji') return getDataSource('KANJI_15_18_DATA').concat(getDataSource('KANJI_11_14_DATA'));
        return getDataSource('VOCAB_DATA').map(function (v, i) {
            return {
                id: 'v_' + i + '_' + (v.jp || ''),
                lesson: v.l || 'A2',
                vi: v.vi,
                jp: v.jp,
                kana: v.kana,
                romaji: v.romaji,
                kanji: v.kanji
            };
        });
    }

    function getFilterDefs(mode) {
        var wrongIds = new Set(Object.keys(window.tpState.history).filter(function (id) {
            return window.tpState.history[id] && window.tpState.history[id].status === 'err';
        }));
        var items = getModeItems(mode);
        if (mode === 'sentence') {
            return [
                { key: 'all', label: 'Tất cả L11-18 (' + items.length + ')' },
                { key: 'focus-15-18', label: 'Trọng tâm L15-18 (' + items.filter(function (x) { return !/^A2-1[1-4]$/.test(x.lesson); }).length + ')' },
                { key: 'A2-15', label: 'Bài 15 (' + items.filter(function (x) { return x.lesson === 'A2-15'; }).length + ')' },
                { key: 'A2-16', label: 'Bài 16 (' + items.filter(function (x) { return x.lesson === 'A2-16'; }).length + ')' },
                { key: 'Kaiwa Mid 2', label: 'Kaiwa Mid 2 (' + items.filter(function (x) { return x.lesson === 'Kaiwa Mid 2'; }).length + ')' },
                { key: 'A2-17', label: 'Bài 17 (' + items.filter(function (x) { return x.lesson === 'A2-17'; }).length + ')' },
                { key: 'A2-18', label: 'Bài 18 (' + items.filter(function (x) { return x.lesson === 'A2-18'; }).length + ')' },
                { key: 'review-11-14', label: 'Ôn thêm L11-14 (' + items.filter(function (x) { return /^A2-1[1-4]$/.test(x.lesson); }).length + ')' },
                { key: 'wrong', label: '🔁 Câu sai (' + items.filter(function (x) { return wrongIds.has(x.id); }).length + ')' }
            ];
        }
        if (mode === 'kanji') {
            var k15 = getDataSource('KANJI_15_18_DATA');
            var k11 = getDataSource('KANJI_11_14_DATA');
            return [
                { key: '15-18', label: 'Kanji L15-18 (' + k15.length + ')' },
                { key: '11-14', label: 'Kanji L11-14 (' + k11.length + ')' },
                { key: 'all', label: 'Tất cả (' + items.length + ')' },
                { key: 'wrong', label: '🔁 Chữ hay sai (' + items.filter(function (x) { return wrongIds.has(x.id); }).length + ')' }
            ];
        }
        return [
            { key: 'all', label: 'Tất cả (' + items.length + ')' },
            { key: 'A2-15', label: 'Bài 15' },
            { key: 'A2-16', label: 'Bài 16' },
            { key: 'A2-17', label: 'Bài 17' },
            { key: 'A2-18', label: 'Bài 18' },
            { key: 'wrong', label: '🔁 Từ sai (' + items.filter(function (x) { return wrongIds.has(x.id); }).length + ')' }
        ];
    }

    function getActiveBucketKey() {
        var m = window.tpState.mode;
        var f = window.tpState.filterByMode[m] || (m === 'kanji' ? '15-18' : 'all');
        return m + '::' + f;
    }

    function getFilteredTypingPool() {
        var m = window.tpState.mode;
        var f = window.tpState.filterByMode[m] || (m === 'kanji' ? '15-18' : 'all');
        var all = getModeItems(m);
        var base;
        if (f === 'wrong') {
            base = all.filter(function (x) { return window.tpState.history[x.id] && window.tpState.history[x.id].status === 'err'; });
        } else if (f === 'all') {
            base = all.slice();
        } else if (m === 'sentence' && f === 'focus-15-18') {
            base = all.filter(function (x) { return !/^A2-1[1-4]$/.test(x.lesson); });
        } else if (m === 'sentence' && f === 'review-11-14') {
            base = all.filter(function (x) { return /^A2-1[1-4]$/.test(x.lesson); });
        } else if (m === 'kanji') {
            base = all.filter(function (x) { return x.group === f; });
        } else {
            base = all.filter(function (x) { return x.lesson === f; });
        }

        var bucket = getActiveBucketKey();
        var savedOrder = window.tpState.orderByBucket[bucket];
        if (Array.isArray(savedOrder) && savedOrder.length > 0 && f !== 'wrong') {
            var mapById = new Map(base.map(function (it) { return [it.id, it]; }));
            var ordered = savedOrder.map(function (id) { return mapById.get(id); }).filter(Boolean);
            var missing = base.filter(function (it) { return savedOrder.indexOf(it.id) === -1; });
            return ordered.concat(missing);
        }
        return base;
    }

    function persistCheckpoint() {
        if (typeof window.saveMini15_18Checkpoint === 'function') {
            window.saveMini15_18Checkpoint();
        }
    }

    function notify(msg) {
        if (typeof window.showToast === 'function') window.showToast(msg);
    }

    function getSpeakableTypingText(item) {
        if (!item) return '';
        if (window.tpState.mode === 'sentence') {
            var natural = item.kanjiModel || item.hira || '';
            return String(natural).replace(/[（(]\s*[／/][^）)]*[）)]/g, '').trim();
        }
        return item.kanji || item.jp || item.kana || '';
    }

    function say(txt, btn) {
        if (!txt) return;
        if (window.AudioEngine && typeof window.AudioEngine.speak === 'function') {
            window.AudioEngine.speak(txt, btn);
        } else if (typeof window.speakText === 'function') {
            window.speakText(txt, btn);
        }
    }

    function updateTypingModeButtons() {
        ['sentence', 'kanji', 'vocab'].forEach(function (m) {
            var btn = document.getElementById('tpModeBtn_' + m);
            if (btn) btn.classList.toggle('active', window.tpState.mode === m);
        });
        var kWrap = document.getElementById('tpKanjiAllowWrap');
        if (kWrap) kWrap.style.display = window.tpState.mode === 'sentence' ? 'inline-flex' : 'none';
    }

    function renderTypingControlsState() {
        var kTog = document.getElementById('tpAllowKanjiToggle');
        var aTog = document.getElementById('tpAutoAdvToggle');
        if (kTog) kTog.checked = Boolean(window.tpState.allowKanji);
        if (aTog) aTog.checked = Boolean(window.tpState.autoAdvance);
        var drawer = document.getElementById('tpOverviewDrawer');
        var oBtn = document.getElementById('tpOverviewBtn');
        if (drawer) drawer.classList.toggle('show', Boolean(window.tpState.showOverview));
        if (oBtn) oBtn.classList.toggle('active', Boolean(window.tpState.showOverview));
    }

    function renderTypingFilters() {
        var grp = document.getElementById('typingFilterGroup');
        if (!grp) return;
        var m = window.tpState.mode;
        var curF = window.tpState.filterByMode[m] || (m === 'kanji' ? '15-18' : 'all');
        var defs = getFilterDefs(m);
        grp.innerHTML = defs.map(function (d) {
            return '<button type="button" class="v-filter-btn ' + (d.key === curF ? 'active' : '') + '" onclick="switchTypingLesson(\'' + d.key + '\')">' + d.label + '</button>';
        }).join('');
    }

    function updateTypingStats(pool) {
        var items = pool && pool.length ? pool : getModeItems(window.tpState.mode);
        var ok = 0, err = 0;
        items.forEach(function (it) {
            var h = window.tpState.history[it.id];
            if (h && h.status === 'ok') ok++;
            else if (h && h.status === 'err') err++;
        });
        document.getElementById('tpStatCorrect').innerText = ok;
        document.getElementById('tpStatWrong').innerText = err;
        var touched = ok + err;
        var pct = items.length === 0 ? 0 : Math.round((ok / items.length) * 100);
        document.getElementById('tpStatPercent').innerText = pct + '% (' + touched + '/' + items.length + ')';
        var bar = document.getElementById('tpProgressBar');
        if (bar) bar.style.width = pct + '%';
    }

    function renderTypingOverview() {
        var drawer = document.getElementById('tpOverviewDrawer');
        if (!drawer || !window.tpState.showOverview) return;
        var pool = getFilteredTypingPool();
        var bucket = getActiveBucketKey();
        var curIdx = window.tpState.idxByBucket[bucket] || 0;
        if (!pool.length) {
            drawer.innerHTML = '<div style="grid-column:1/-1; color:var(--gray-500); font-size:0.9rem;">Chưa có mục nào trong bộ lọc này.</div>';
            return;
        }
        drawer.innerHTML = pool.map(function (it, idx) {
            var hist = window.tpState.history[it.id];
            var stCls = hist ? (hist.status === 'ok' ? 'done-ok' : (hist.status === 'err' ? 'done-err' : '')) : '';
            var icon = hist ? (hist.status === 'ok' ? '✅' : (hist.status === 'err' ? '❌' : '👁️')) : (idx + 1) + '.';
            var title = window.tpState.mode === 'kanji'
                ? (it.kanji + ' (' + it.vi + ')')
                : (window.tpState.mode === 'sentence' ? it.vi : (it.vi + ' (' + it.jp + ')'));
            return '<button type="button" class="tp-overview-item ' + (idx === curIdx ? 'active' : '') + ' ' + stCls + '" onclick="jumpToTypingItem(' + idx + ')">' +
                '<span>' + icon + '</span>' +
                '<span style="overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">' + escapeHtml(title) + '</span>' +
                '</button>';
        }).join('');
    }

    function renderTypingDetailBox(item, hist) {
        var detailPanel = document.getElementById('tpDetailPanel');
        if (!detailPanel) return;

        var headerHtml = '';
        var panelCls = 'tp-detail-panel show ';
        if (hist.status === 'ok') {
            panelCls += 'is-ok';
            headerHtml = '<div style="font-size:1.08rem; font-weight:800; color:#15803d; margin-bottom:10px;">' +
                '✅ CHÍNH XÁC! ' +
                (hist.isKanjiMatch ? '<span style="font-size:0.84rem; color:#0369a1; font-weight:700;">(Chấp nhận dạng kèm Kanji)</span>' : '') +
                '</div>' +
                (hist.variantNote ? '<div style="margin-bottom:8px; font-size:0.86rem; color:#047857; background:#ecfdf5; border:1px solid #a7f3d0; padding:6px 10px; border-radius:8px;">' + escapeHtml(hist.variantNote) + '</div>' : '');
        } else if (hist.status === 'reveal') {
            panelCls += 'is-reveal';
            headerHtml = '<div style="font-size:1.08rem; font-weight:800; color:#b45309; margin-bottom:10px;">👁️ XEM ĐÁP ÁN CHUẨN</div>';
        } else {
            panelCls += 'is-err';
            headerHtml = '<div style="font-size:1.08rem; font-weight:800; color:#be123c; margin-bottom:10px;">❌ CHƯA ĐÚNG — CÙNG XEM VÌ SAO SAI NHÉ!</div>';
        }

        var compareHtml = '';
        var primaryReading = window.tpState.mode === 'sentence' ? item.hira : (window.tpState.mode === 'kanji' ? item.kana : (item.kana || item.jp));
        if (hist.status === 'err' && hist.lastInput !== undefined) {
            var diff = buildCharDiffHtml(hist.lastInput, primaryReading);
            compareHtml = '<div class="tp-diff-row">' +
                '<div><strong style="color:#be123c;">Bạn đã gõ:</strong> <span class="jp-text" style="font-size:1.06rem;">' + diff.typedHtml + '</span></div>' +
                '<div><strong style="color:#15803d;">Đáp án đúng:</strong> <span class="jp-text" style="font-size:1.06rem;">' + diff.targetHtml + '</span></div>' +
                '</div>';
        }

        var whyHtml = '';
        if (hist.status === 'err' && hist.whyWrong && hist.whyWrong.length) {
            whyHtml = '<div class="tp-why-box">' +
                '<div style="font-weight:800; margin-bottom:6px;">🚨 Phân tích vì sao sai:</div>' +
                '<ul style="margin:0 0 0 18px; padding:0;">' +
                hist.whyWrong.map(function (r) { return '<li style="margin-bottom:4px;">' + r + '</li>'; }).join('') +
                '</ul></div>';
        }

        var meaningHtml = '';
        if (window.tpState.mode === 'sentence') {
            var alts = (item.acceptedHira || []).slice(1, 4);
            meaningHtml = '<div class="tp-meaning-box">' +
                '<div style="margin-bottom:6px;"><strong>🔊 Câu Hiragana chuẩn:</strong> ' +
                '<span class="jp-text" style="font-size:1.12rem; font-weight:800; color:var(--primary-dark);">' + escapeHtml(item.hira) + '</span> ' +
                '<button type="button" class="audio-btn" onclick="speakCurrentTypingWord()" style="vertical-align:middle; margin-left:6px;" title="Nghe phát âm">🔊</button></div>' +
                '<div style="margin-bottom:6px;"><strong>⛩️ Tham khảo kèm Kanji:</strong> <span class="jp-text" style="font-weight:700; color:#334155;">' + escapeHtml(item.kanjiModel) + '</span></div>' +
                '<div style="margin-bottom:6px;"><strong>🇻🇳 Nghĩa tiếng Việt:</strong> ' + escapeHtml(item.vi) + '</div>' +
                '<div style="margin-bottom:6px;"><strong>📐 Ngữ pháp (' + escapeHtml(item.pattern) + '):</strong> ' + item.grammarRule + '</div>' +
                '<div><strong>🧩 Bóc tách câu:</strong> ' + item.breakdown + '</div>' +
                (alts.length ? '<div style="margin-top:6px; font-size:0.84rem; color:#475569;"><strong>✔️ Biến thể cô cũng chấp nhận:</strong> ' + alts.map(function (a) { return '<code class="jp-text">' + escapeHtml(a) + '</code>'; }).join(' • ') + '</div>' : '') +
                '</div>';
        } else if (window.tpState.mode === 'kanji') {
            meaningHtml = '<div class="tp-meaning-box">' +
                '<div style="margin-bottom:6px; display:flex; align-items:center; gap:10px; flex-wrap:wrap;">' +
                '<span><strong>⛩️ Kanji:</strong> <span class="jp-text" style="font-size:1.35rem; font-weight:900; color:var(--primary-dark);">' + escapeHtml(item.kanji) + '</span></span>' +
                '<span><strong>🔤 Hiragana chuẩn:</strong> <span class="jp-text" style="font-size:1.2rem; font-weight:800; color:#15803d;">' + escapeHtml(item.kana) + '</span></span>' +
                '<button type="button" class="audio-btn" onclick="speakCurrentTypingWord()" title="Nghe phát âm">🔊</button></div>' +
                '<div style="margin-bottom:6px;"><strong>🏮 Âm Hán Việt:</strong> <span style="font-weight:800; color:#b45309; background:#fef3c7; padding:2px 8px; border-radius:6px;">' + escapeHtml(item.hv) + '</span></div>' +
                '<div style="margin-bottom:6px;"><strong>🇻🇳 Ý nghĩa:</strong> <strong>' + escapeHtml(item.vi) + '</strong></div>' +
                '<div><strong>🧠 Mẹo nhớ &amp; Phân biệt:</strong> ' + item.note + '</div></div>';
        } else {
            meaningHtml = '<div class="tp-meaning-box">' +
                '<div style="margin-bottom:6px;"><strong>🇯🇵 Tiếng Nhật:</strong> <span class="jp-text" style="font-size:1.15rem; font-weight:800; color:var(--primary-dark);">' + escapeHtml(item.jp) + '</span> ' +
                (item.kana ? '<span class="jp-text" style="color:var(--primary);">【' + escapeHtml(item.kana) + '】</span>' : '') +
                '<button type="button" class="audio-btn" onclick="speakCurrentTypingWord()" style="vertical-align:middle; margin-left:6px;">🔊</button></div>' +
                '<div style="margin-bottom:6px;"><strong>🔤 Romaji:</strong> ' + escapeHtml(item.romaji || '') + '</div>' +
                '<div><strong>🇻🇳 Nghĩa tiếng Việt:</strong> ' + escapeHtml(item.vi) + '</div></div>';
        }

        detailPanel.className = panelCls;
        detailPanel.innerHTML = headerHtml + compareHtml + whyHtml + meaningHtml +
            '<div style="margin-top:12px; display:flex; gap:10px; flex-wrap:wrap; align-items:center;">' +
            '<button type="button" class="btn-primary" style="padding:7px 14px; font-size:0.86rem; background:var(--secondary);" onclick="skipTypingWord()">➔ Sang câu tiếp theo (Enter)</button>' +
            (hist.status === 'err' ? '<button type="button" class="btn-primary" style="padding:7px 14px; font-size:0.86rem; background:var(--gray-600);" onclick="retryCurrentTypingCard()">🔄 Thử gõ lại câu này</button>' : '') +
            '</div>';
    }

    function renderTypingCard(shouldFocus) {
        var pool = getFilteredTypingPool();
        var bucket = getActiveBucketKey();
        var idx = window.tpState.idxByBucket[bucket] || 0;
        if (idx >= pool.length) idx = Math.max(0, pool.length - 1);
        if (idx < 0) idx = 0;
        window.tpState.idxByBucket[bucket] = idx;

        var badge = document.getElementById('tpCardBadge');
        var patBadge = document.getElementById('tpPatternBadge');
        var subEl = document.getElementById('tpPromptSubtitle');
        var promptEl = document.getElementById('tpPromptVi');
        var dirEl = document.getElementById('tpInputDirective');
        var hintPrev = document.getElementById('tpHintPreview');
        var inp = document.getElementById('tpCardInput');
        var checkBtn = document.getElementById('tpCardCheckBtn');
        var detailPanel = document.getElementById('tpDetailPanel');
        var streakEl = document.getElementById('tpStreakBadge');
        if (streakEl) streakEl.innerText = '🔥 Chuỗi: ' + window.tpState.streak;

        if (!pool.length) {
            if (badge) badge.innerText = '0 / 0';
            if (patBadge) patBadge.innerText = 'Bộ lọc trống';
            if (subEl) subEl.innerText = 'TRẠNG THÁI';
            if (promptEl) {
                promptEl.className = 'tp-vi-hero';
                promptEl.innerText = '🎉 Tuyệt vời! Không có câu/chữ nào đang sai trong bộ lọc này.';
            }
            if (inp) {
                inp.value = '';
                inp.disabled = true;
            }
            if (detailPanel) { detailPanel.className = 'tp-detail-panel'; detailPanel.innerHTML = ''; }
            updateTypingStats(pool);
            renderTypingOverview();
            return;
        }

        var item = pool[idx];
        if (hintPrev) { hintPrev.style.display = 'none'; hintPrev.innerHTML = ''; }

        if (window.tpState.mode === 'sentence') {
            badge.innerText = 'Câu ' + (idx + 1) + ' / ' + pool.length + ' • ' + item.lesson;
            patBadge.innerText = item.category || item.pattern || 'Bài 15-18';
            subEl.innerText = 'ĐỀ BÀI TIẾNG VIỆT — DỊCH & GÕ HIRAGANA';
            promptEl.className = 'tp-vi-hero';
            promptEl.innerText = item.vi;
            dirEl.innerHTML = '⬇️ Nhập câu tiếng Nhật bằng <strong>Hiragana</strong> rồi nhấn <strong>Enter</strong>:';
            inp.placeholder = 'Ví dụ: ねる まえに、よく ほんを よみます。';
            inp.rows = 2;
        } else if (window.tpState.mode === 'kanji') {
            badge.innerText = 'Chữ Hán ' + (idx + 1) + ' / ' + pool.length + ' • PDF Kanji ' + item.group + ' (#' + item.stt + ')';
            patBadge.innerText = 'Kanji Lesson ' + item.group;
            subEl.innerText = 'NHÌN CHỮ HÁN (KANJI) — GÕ CÁCH ĐỌC HIRAGANA';
            promptEl.className = 'tp-kanji-hero jp-text';
            promptEl.innerText = item.kanji;
            dirEl.innerHTML = '⬇️ Nhập <strong>cách đọc Hiragana</strong> của chữ Hán trên rồi nhấn <strong>Enter</strong>:';
            inp.placeholder = 'Gõ cách đọc bằng Hiragana (ví dụ: らいねん)...';
            inp.rows = 1;
        } else {
            badge.innerText = 'Từ ' + (idx + 1) + ' / ' + pool.length + ' • ' + item.lesson;
            patBadge.innerText = 'Từ Vựng A2 • ' + item.lesson;
            subEl.innerText = 'NGHĨA TIẾNG VIỆT — GÕ TỪ TIẾNG NHẬT';
            promptEl.className = 'tp-vi-hero';
            promptEl.innerText = item.vi;
            dirEl.innerHTML = '⬇️ Nhập bằng Hiragana / Kanji / Romaji rồi nhấn <strong>Enter</strong>:';
            inp.placeholder = 'Nhập từ tiếng Nhật...';
            inp.rows = 1;
        }

        inp.disabled = false;
        var hist = window.tpState.history[item.id];
        var draftVal = window.tpState.drafts[item.id];
        if (hist && (hist.status === 'ok' || hist.status === 'err' || hist.status === 'reveal')) {
            inp.value = draftVal !== undefined ? draftVal : (hist.lastInput || '');
            renderTypingDetailBox(item, hist);
            window.tpState.gradedCurrent = true;
            checkBtn.innerText = 'Câu Tiếp Theo ➔ (Enter)';
            checkBtn.style.background = 'var(--secondary)';
        } else {
            inp.value = draftVal || '';
            detailPanel.className = 'tp-detail-panel';
            detailPanel.innerHTML = '';
            window.tpState.gradedCurrent = false;
            checkBtn.innerText = 'Kiểm Tra Đáp Án ⏎';
            checkBtn.style.background = 'var(--primary)';
        }

        updateTypingStats(pool);
        renderTypingOverview();
        if (shouldFocus) inp.focus();
    }

    function handleTypingSubmit() {
        var pool = getFilteredTypingPool();
        var bucket = getActiveBucketKey();
        var idx = window.tpState.idxByBucket[bucket] || 0;
        if (!pool.length || idx >= pool.length) return;

        var item = pool[idx];
        var inp = document.getElementById('tpCardInput');
        var rawVal = (inp.value || '').trim();
        if (!rawVal) {
            notify('Vui lòng gõ đáp án trước khi kiểm tra!');
            inp.focus();
            return;
        }

        var res = window.JpTypingGrader.grade(rawVal, item, window.tpState.mode, { allowKanji: window.tpState.allowKanji });
        var audioTxt = getSpeakableTypingText(item);

        if (res.ok) {
            window.tpState.streak++;
            window.tpState.history[item.id] = {
                status: 'ok',
                lastInput: rawVal,
                whyWrong: [],
                isKanjiMatch: res.matchType === 'kanji',
                variantNote: res.variantNote || ''
            };
            delete window.tpState.drafts[item.id];
            window.tpState.gradedCurrent = true;
            say(audioTxt);
            renderTypingFilters();
            renderTypingCard(false);
            persistCheckpoint();
            if (window.tpState.autoAdvance) {
                setTimeout(skipTypingWord, 900);
            }
        } else {
            window.tpState.streak = 0;
            var whyWrong = diagnoseTypingMistake(rawVal, item, window.tpState.mode);
            window.tpState.history[item.id] = {
                status: 'err',
                lastInput: rawVal,
                whyWrong: whyWrong,
                isKanjiMatch: false,
                variantNote: ''
            };
            window.tpState.drafts[item.id] = rawVal;
            window.tpState.gradedCurrent = true;
            say(audioTxt);
            renderTypingFilters();
            renderTypingCard(false);
            persistCheckpoint();
        }
    }

    function initTypingPractice() {
        window.tpInitialized = true;
        updateTypingModeButtons();
        renderTypingFilters();
        renderTypingControlsState();
        renderTypingCard(false);
    }

    function switchTypingMode(mode) {
        window.tpState.mode = mode;
        window.tpState.gradedCurrent = false;
        updateTypingModeButtons();
        renderTypingFilters();
        renderTypingCard(true);
        persistCheckpoint();
    }

    function switchTypingLesson(lessonKey) {
        window.tpState.filterByMode[window.tpState.mode] = lessonKey;
        window.tpState.gradedCurrent = false;
        renderTypingFilters();
        renderTypingCard(true);
        persistCheckpoint();
    }

    function toggleTypingOption(optName, val) {
        if (optName === 'allowKanji') window.tpState.allowKanji = Boolean(val);
        if (optName === 'autoAdvance') window.tpState.autoAdvance = Boolean(val);
        persistCheckpoint();
    }

    function toggleTypingOverview() {
        window.tpState.showOverview = !window.tpState.showOverview;
        renderTypingControlsState();
        renderTypingOverview();
        persistCheckpoint();
    }

    function jumpToTypingItem(idx) {
        var bucket = getActiveBucketKey();
        window.tpState.idxByBucket[bucket] = idx;
        window.tpState.gradedCurrent = false;
        renderTypingCard(true);
        persistCheckpoint();
    }

    function shuffleTypingPool() {
        var pool = getFilteredTypingPool();
        if (!pool.length) return;
        var shuffled = pool.map(function (x) { return x.id; }).sort(function () { return Math.random() - 0.5; });
        var bucket = getActiveBucketKey();
        window.tpState.orderByBucket[bucket] = shuffled;
        window.tpState.idxByBucket[bucket] = 0;
        window.tpState.gradedCurrent = false;
        renderTypingCard(true);
        persistCheckpoint();
        notify('Đã xáo trộn thứ tự các thẻ!');
    }

    function handleTypingPrimaryBtn() {
        if (window.tpState.gradedCurrent) {
            skipTypingWord();
        } else {
            handleTypingSubmit();
        }
    }

    function retryCurrentTypingCard() {
        var pool = getFilteredTypingPool();
        var bucket = getActiveBucketKey();
        var item = pool[window.tpState.idxByBucket[bucket] || 0];
        if (!item) return;
        window.tpState.gradedCurrent = false;
        window.tpState.drafts[item.id] = '';
        delete window.tpState.history[item.id];
        renderTypingFilters();
        renderTypingCard(true);
        persistCheckpoint();
    }

    function speakCurrentTypingWord(btn) {
        var pool = getFilteredTypingPool();
        var bucket = getActiveBucketKey();
        var idx = window.tpState.idxByBucket[bucket] || 0;
        if (pool[idx]) {
            var triggerBtn = (btn && btn.classList) ? btn : null;
            try {
                if (!triggerBtn && window.event && window.event.currentTarget && window.event.currentTarget.tagName === 'BUTTON') {
                    triggerBtn = window.event.currentTarget;
                }
            } catch (e) {}
            if (!triggerBtn) triggerBtn = document.getElementById('tpCardSpeakBtn');
            say(getSpeakableTypingText(pool[idx]), triggerBtn);
        }
    }

    function showTypingHint() {
        var pool = getFilteredTypingPool();
        var bucket = getActiveBucketKey();
        var idx = window.tpState.idxByBucket[bucket] || 0;
        var item = pool[idx];
        var box = document.getElementById('tpHintPreview');
        if (!item || !box) return;

        if (window.tpState.mode === 'sentence') {
            var words = item.hira.split(/\s+/);
            box.innerHTML = '💡 <strong>Gợi ý công thức:</strong> <code>' + escapeHtml(item.pattern) + '</code> • <strong>Bắt đầu bằng:</strong> <span class="jp-text">' + escapeHtml(words.slice(0, 2).join(' ')) + '...</span>';
        } else if (window.tpState.mode === 'kanji') {
            box.innerHTML = '💡 <strong>Gợi ý Hán Việt &amp; Nghĩa:</strong> <span style="color:#b45309;font-weight:800;">' + escapeHtml(item.hv) + '</span> (' + escapeHtml(item.vi) + ') • Chữ đầu: <strong class="jp-text">' + escapeHtml((item.kana || '').charAt(0)) + '...</strong>';
        } else {
            box.innerHTML = '💡 <strong>Gợi ý chữ cái đầu:</strong> <strong class="jp-text">' + escapeHtml((item.kana || item.jp).charAt(0)) + '...</strong>';
        }
        box.style.display = 'block';
        document.getElementById('tpCardInput').focus();
    }

    function revealTypingAnswer() {
        var pool = getFilteredTypingPool();
        var bucket = getActiveBucketKey();
        var idx = window.tpState.idxByBucket[bucket] || 0;
        var item = pool[idx];
        if (!item) return;

        window.tpState.streak = 0;
        var ans = window.tpState.mode === 'sentence' ? item.hira : (window.tpState.mode === 'kanji' ? item.kana : (item.kana || item.jp));
        window.tpState.history[item.id] = { status: 'reveal', lastInput: ans, whyWrong: [] };
        delete window.tpState.drafts[item.id];
        window.tpState.gradedCurrent = true;
        say(getSpeakableTypingText(item));
        renderTypingCard(false);
        persistCheckpoint();
    }

    function prevTypingItem() {
        var pool = getFilteredTypingPool();
        if (!pool.length) return;
        var bucket = getActiveBucketKey();
        var cur = window.tpState.idxByBucket[bucket] || 0;
        window.tpState.idxByBucket[bucket] = (cur - 1 + pool.length) % pool.length;
        window.tpState.gradedCurrent = false;
        renderTypingCard(true);
        persistCheckpoint();
    }

    function skipTypingWord() {
        var pool = getFilteredTypingPool();
        if (!pool.length) return;
        var bucket = getActiveBucketKey();
        var cur = window.tpState.idxByBucket[bucket] || 0;
        window.tpState.idxByBucket[bucket] = (cur + 1) % pool.length;
        window.tpState.gradedCurrent = false;
        renderTypingCard(true);
        persistCheckpoint();
    }

    function resetCurrentTypingMode() {
        var label = window.tpState.mode === 'sentence' ? 'Câu Tiếng Việt ➔ Hiragana' : (window.tpState.mode === 'kanji' ? 'Chữ Hán ➔ Hiragana' : 'Từ Vựng A2');
        if (!window.confirm('Đặt lại tiến độ luyện gõ chế độ "' + label + '"?')) return;
        getModeItems(window.tpState.mode).forEach(function (it) {
            delete window.tpState.history[it.id];
            delete window.tpState.drafts[it.id];
        });
        var bucket = getActiveBucketKey();
        window.tpState.idxByBucket[bucket] = 0;
        delete window.tpState.orderByBucket[bucket];
        window.tpState.streak = 0;
        window.tpState.gradedCurrent = false;
        renderTypingFilters();
        renderTypingCard(true);
        persistCheckpoint();
        notify('Đã làm mới chế độ ' + label + '!');
    }

    function bindTypingInputEvents() {
        var inp = document.getElementById('tpCardInput');
        if (!inp || inp.dataset.tpBound) return;
        inp.dataset.tpBound = '1';
        inp.addEventListener('keydown', function (e) {
            if (e.key === 'Enter' && !e.shiftKey && !e.isComposing && e.keyCode !== 229) {
                e.preventDefault();
                handleTypingPrimaryBtn();
            }
        });
        inp.addEventListener('input', function () {
            var pool = getFilteredTypingPool();
            var bucket = getActiveBucketKey();
            var item = pool[window.tpState.idxByBucket[bucket] || 0];
            if (item) {
                window.tpState.drafts[item.id] = inp.value;
                if (window.tpState.gradedCurrent) {
                    window.tpState.gradedCurrent = false;
                    var btn = document.getElementById('tpCardCheckBtn');
                    if (btn) {
                        btn.innerText = 'Kiểm Tra Đáp Án ⏎';
                        btn.style.background = 'var(--primary)';
                    }
                }
                persistCheckpoint();
            }
        });
    }

    // Export public handlers for inline HTML buttons and mini-test-15-18 coordinator
    window.initTypingPractice = initTypingPractice;
    window.switchTypingMode = switchTypingMode;
    window.switchTypingLesson = switchTypingLesson;
    window.toggleTypingOption = toggleTypingOption;
    window.toggleTypingOverview = toggleTypingOverview;
    window.jumpToTypingItem = jumpToTypingItem;
    window.shuffleTypingPool = shuffleTypingPool;
    window.prevTypingItem = prevTypingItem;
    window.handleTypingPrimaryBtn = handleTypingPrimaryBtn;
    window.retryCurrentTypingCard = retryCurrentTypingCard;
    window.speakCurrentTypingWord = speakCurrentTypingWord;
    window.showTypingHint = showTypingHint;
    window.revealTypingAnswer = revealTypingAnswer;
    window.skipTypingWord = skipTypingWord;
    window.resetCurrentTypingMode = resetCurrentTypingMode;
    window.getActiveBucketKey = getActiveBucketKey;
    window.getFilteredTypingPool = getFilteredTypingPool;
    window.bindTypingInputEvents = bindTypingInputEvents;
})(window);
