/**
 * typing-studio.js
 * Modular Typing Studio engine for L11-L18 Sentences, Kanji -> Hiragana, and A2 Vocab.
 * Relies on JpTypingGrader (assets/js/jp-typing-grader.js) for flexible natural-Japanese grading.
 */
(function (window) {
    'use strict';

    var TYPING_STUDIO_STORAGE_KEY = 'marugoto_typing_studio_v2';

    window.tpInitialized = false;
    window.tpState = {
        mode: 'sentence', // 'sentence' | 'kanji' | 'vocab'
        filterByMode: { sentence: 'all', kanji: 'all', vocab: 'all' },
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

    function saveTypingStudioState() {
        try {
            var data = {
                version: 2,
                savedAt: Date.now(),
                mode: window.tpState.mode,
                filterByMode: window.tpState.filterByMode,
                idxByBucket: window.tpState.idxByBucket,
                orderByBucket: window.tpState.orderByBucket,
                history: window.tpState.history,
                drafts: window.tpState.drafts,
                allowKanji: window.tpState.allowKanji,
                autoAdvance: window.tpState.autoAdvance,
                streak: window.tpState.streak
            };
            localStorage.setItem(TYPING_STUDIO_STORAGE_KEY, JSON.stringify(data));
        } catch (e) {
            console.warn('Could not save typing studio state:', e);
        }
    }

    function restoreTypingStudioState() {
        try {
            var raw = localStorage.getItem(TYPING_STUDIO_STORAGE_KEY);
            if (!raw) return false;
            var data = JSON.parse(raw);
            if (!data || data.version !== 2) return false;
            if (data.mode) window.tpState.mode = data.mode;
            if (data.filterByMode && typeof data.filterByMode === 'object') {
                Object.assign(window.tpState.filterByMode, data.filterByMode);
            }
            if (data.idxByBucket && typeof data.idxByBucket === 'object') {
                Object.assign(window.tpState.idxByBucket, data.idxByBucket);
            }
            if (data.orderByBucket && typeof data.orderByBucket === 'object') {
                Object.assign(window.tpState.orderByBucket, data.orderByBucket);
            }
            if (data.history && typeof data.history === 'object') {
                Object.assign(window.tpState.history, data.history);
            }
            if (data.drafts && typeof data.drafts === 'object') {
                Object.assign(window.tpState.drafts, data.drafts);
            }
            if (typeof data.allowKanji === 'boolean') window.tpState.allowKanji = data.allowKanji;
            if (typeof data.autoAdvance === 'boolean') window.tpState.autoAdvance = data.autoAdvance;
            if (typeof data.streak === 'number') window.tpState.streak = data.streak;
            return true;
        } catch (e) {
            console.warn('Could not restore typing studio state:', e);
            return false;
        }
    }

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
                { key: 'all', label: 'Tất cả L11-18 (' + items.length + ')' },
                { key: 'A2-11', label: 'Bài 11 (' + items.filter(function (x) { return x.lesson === 'A2-11'; }).length + ')' },
                { key: 'A2-12', label: 'Bài 12 (' + items.filter(function (x) { return x.lesson === 'A2-12'; }).length + ')' },
                { key: 'A2-13', label: 'Bài 13 (' + items.filter(function (x) { return x.lesson === 'A2-13'; }).length + ')' },
                { key: 'A2-14', label: 'Bài 14 (' + items.filter(function (x) { return x.lesson === 'A2-14'; }).length + ')' },
                { key: 'A2-15', label: 'Bài 15 (' + items.filter(function (x) { return x.lesson === 'A2-15'; }).length + ')' },
                { key: 'A2-16', label: 'Bài 16 (' + items.filter(function (x) { return x.lesson === 'A2-16'; }).length + ')' },
                { key: 'A2-17', label: 'Bài 17 (' + items.filter(function (x) { return x.lesson === 'A2-17'; }).length + ')' },
                { key: 'A2-18', label: 'Bài 18 (' + items.filter(function (x) { return x.lesson === 'A2-18'; }).length + ')' },
                { key: '15-18', label: 'Cụm L15-18 (' + k15.length + ')' },
                { key: '11-14', label: 'Cụm L11-14 (' + k11.length + ')' },
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
        var f = window.tpState.filterByMode[m] || 'all';
        return m + '::' + f;
    }

    function getFilteredTypingPool() {
        var m = window.tpState.mode;
        var f = window.tpState.filterByMode[m] || 'all';
        var all = getModeItems(m);
        var base;
        if (f === 'wrong') {
            if (!Array.isArray(window.tpState.wrongQueue)) {
                window.tpState.wrongQueue = all.filter(function (x) {
                    return window.tpState.history[x.id] && window.tpState.history[x.id].status === 'err';
                });
            }
            return window.tpState.wrongQueue;
        } else if (f === 'all') {
            base = all.slice();
        } else if (m === 'sentence' && f === 'focus-15-18') {
            base = all.filter(function (x) { return !/^A2-1[1-4]$/.test(x.lesson); });
        } else if (m === 'sentence' && f === 'review-11-14') {
            base = all.filter(function (x) { return /^A2-1[1-4]$/.test(x.lesson); });
        } else if (m === 'kanji') {
            if (f === '15-18' || f === '11-14') {
                base = all.filter(function (x) { return x.group === f; });
            } else if (/^A2-1[1-8]$/.test(f)) {
                base = all.filter(function (x) { return x.lesson === f; });
            } else {
                base = all.slice();
            }
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
        saveTypingStudioState();
        if (typeof window.saveMini15_18Checkpoint === 'function') {
            window.saveMini15_18Checkpoint();
        } else if (window.MarugotoCheckpoint && typeof window.MarugotoCheckpoint.notifySaved === 'function') {
            window.MarugotoCheckpoint.notifySaved();
        }
    }

    function manualSaveTypingProgress() {
        persistCheckpoint();
        var pool = getFilteredTypingPool();
        var bucket = getActiveBucketKey();
        var idx = window.tpState.idxByBucket[bucket] || 0;
        var modeLabel = window.tpState.mode === 'sentence' ? 'Câu' : (window.tpState.mode === 'kanji' ? 'Chữ Hán' : 'Từ');
        notify('💾 Đã lưu tiến độ hiện tại (' + modeLabel + ' ' + (idx + 1) + '/' + pool.length + ')!');
    }

    function skipOrPassCurrentTypingWord() {
        var pool = getFilteredTypingPool();
        var bucket = getActiveBucketKey();
        var idx = window.tpState.idxByBucket[bucket] || 0;
        if (!pool.length || idx >= pool.length) return;

        var item = pool[idx];

        // Nếu câu này chưa được chấm (đang làm bài và muốn bỏ qua):
        if (!window.tpState.gradedCurrent) {
            window.tpState.streak = 0;
            var ans = window.tpState.mode === 'sentence' ? item.hira : (window.tpState.mode === 'kanji' ? item.kana : (item.kana || item.jp));
            window.tpState.history[item.id] = {
                status: 'err',
                lastInput: '(Đã bỏ qua)',
                whyWrong: ['Bạn đã chọn bỏ qua câu này để xem đáp án chuẩn và lưu vào danh sách ôn tập sau.']
            };
            delete window.tpState.drafts[item.id];
            window.tpState.gradedCurrent = true;
            say(getSpeakableTypingText(item));
            renderTypingFilters();
            renderTypingCard(false);
            persistCheckpoint();
            notify('⏭️ Đã bỏ qua! Câu này đã được lưu vào danh sách cần ôn tập.');
        } else {
            // Nếu câu này đã chấm xong (đang ở màn hình xem đáp án): nhảy luôn sang câu sau
            skipTypingWord();
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

    function setCheckButtonState(state) {
        var checkBtn = document.getElementById('tpCardCheckBtn');
        if (!checkBtn) return;
        checkBtn.style.background = '';
        checkBtn.style.backgroundColor = '';
        if (state === 'next') {
            checkBtn.className = 'tp-btn-primary is-next';
            checkBtn.innerHTML = '<span class="tp-btn-icon">➔</span><span class="tp-btn-label">Câu Tiếp Theo</span><kbd class="tp-kbd tp-kbd-light">⏎ Enter</kbd>';
        } else {
            checkBtn.className = 'tp-btn-primary is-check';
            checkBtn.innerHTML = '<span class="tp-btn-icon">✨</span><span class="tp-btn-label">Kiểm Tra Đáp Án</span><kbd class="tp-kbd tp-kbd-light">⏎ Enter</kbd>';
        }
    }

    function ensureTypingLayoutStructure() {
        var cardView = document.querySelector('.typing-card-view');
        if (!cardView) return;

        var inp = document.getElementById('tpCardInput');
        if (inp && !document.getElementById('tpShortcutBar')) {
            var bar = document.createElement('div');
            bar.className = 'tp-shortcut-bar';
            bar.id = 'tpShortcutBar';
            bar.innerHTML =
                '<span class="tp-shortcut-item"><kbd class="tp-kbd">⏎ Enter</kbd> Kiểm Tra / Tiếp</span>' +
                '<span class="tp-shortcut-item"><kbd class="tp-kbd">Tab</kbd> Bỏ qua (Skip)</span>' +
                '<span class="tp-shortcut-item"><kbd class="tp-kbd">Esc</kbd> Gõ lại (Retry)</span>' +
                '<span class="tp-shortcut-item"><kbd class="tp-kbd">Alt + H</kbd> Gợi ý</span>';
            if (inp.parentNode) {
                inp.parentNode.insertBefore(bar, inp.nextSibling);
            }
        }

        var actions = cardView.querySelector('.typing-actions');
        if (actions && !actions.querySelector('.tp-action-row-primary')) {
            var allBtns = Array.prototype.slice.call(actions.querySelectorAll('button'));
            var checkBtn = document.getElementById('tpCardCheckBtn');
            var skipBtn = document.getElementById('tpCardSkipBtn');
            var retryBtn = document.getElementById('tpCardRetryBtn');
            var saveBtn = document.getElementById('tpCardSaveBtn');
            var speakBtn = document.getElementById('tpCardSpeakBtn');

            var prevBtn = allBtns.filter(function (b) {
                var oc = b.getAttribute('onclick') || '';
                return oc.indexOf('prevTypingItem') !== -1;
            })[0];
            var hintBtn = allBtns.filter(function (b) {
                var oc = b.getAttribute('onclick') || '';
                return oc.indexOf('showTypingHint') !== -1;
            })[0];
            var revealBtn = allBtns.filter(function (b) {
                var oc = b.getAttribute('onclick') || '';
                return oc.indexOf('revealTypingAnswer') !== -1;
            })[0];
            var resetBtn = allBtns.filter(function (b) {
                var oc = b.getAttribute('onclick') || '';
                return oc.indexOf('resetCurrentTypingMode') !== -1;
            })[0];

            if (checkBtn) {
                checkBtn.style.background = '';
                checkBtn.style.backgroundColor = '';
                checkBtn.className = 'tp-btn-primary is-check';
                checkBtn.innerHTML = '<span class="tp-btn-icon">✨</span><span class="tp-btn-label">Kiểm Tra Đáp Án</span><kbd class="tp-kbd tp-kbd-light">⏎ Enter</kbd>';
            }
            if (prevBtn) {
                prevBtn.style.background = '';
                prevBtn.style.backgroundColor = '';
                prevBtn.className = 'tp-btn-secondary';
                prevBtn.id = prevBtn.id || 'tpCardPrevBtn';
                prevBtn.innerHTML = '<span>⬅️ Trước</span>';
                prevBtn.title = 'Câu trước';
            }
            if (skipBtn) {
                skipBtn.style.background = '';
                skipBtn.style.backgroundColor = '';
                skipBtn.className = 'tp-btn-secondary';
                skipBtn.innerHTML = '<span>⏭️ Bỏ Qua</span><kbd class="tp-kbd">Tab</kbd>';
                skipBtn.title = 'Bỏ qua câu này (Tab)';
            }
            if (retryBtn) {
                retryBtn.style.background = '';
                retryBtn.style.backgroundColor = '';
                retryBtn.className = 'tp-btn-secondary is-retry';
                retryBtn.innerHTML = '<span>🔄 Gõ Lại</span><kbd class="tp-kbd">Esc</kbd>';
                retryBtn.title = 'Gõ lại câu này (Esc)';
            }
            if (saveBtn) {
                saveBtn.style.background = '';
                saveBtn.style.backgroundColor = '';
                saveBtn.className = 'tp-btn-secondary';
                saveBtn.innerHTML = '<span>💾 Lưu</span>';
                saveBtn.title = 'Lưu tiến độ làm bài';
            }
            if (speakBtn) {
                speakBtn.style.background = '';
                speakBtn.style.backgroundColor = '';
                speakBtn.className = 'tp-btn-utility is-audio';
                speakBtn.innerHTML = '<span>🔊 Nghe Mẫu</span>';
                speakBtn.title = 'Nghe phát âm chuẩn';
            }
            if (hintBtn) {
                hintBtn.style.background = '';
                hintBtn.style.backgroundColor = '';
                hintBtn.className = 'tp-btn-utility is-hint';
                hintBtn.id = hintBtn.id || 'tpCardHintBtn';
                hintBtn.innerHTML = '<span>💡 Gợi Ý</span>';
                hintBtn.title = 'Xem gợi ý công thức';
            }
            if (revealBtn) {
                revealBtn.style.background = '';
                revealBtn.style.backgroundColor = '';
                revealBtn.className = 'tp-btn-utility is-reveal';
                revealBtn.id = revealBtn.id || 'tpCardRevealBtn';
                revealBtn.innerHTML = '<span>👁️ Xem Đáp Án</span>';
                revealBtn.title = 'Xem đáp án chuẩn';
            }
            if (resetBtn) {
                resetBtn.style.background = '';
                resetBtn.style.backgroundColor = '';
                resetBtn.className = 'tp-btn-utility tp-btn-danger-ghost';
                resetBtn.id = resetBtn.id || 'tpCardResetBtn';
                resetBtn.innerHTML = '<span>🔄 Đặt lại</span>';
                resetBtn.title = 'Làm lại chế độ này từ đầu';
            }

            var rowPrimary = document.createElement('div');
            rowPrimary.className = 'tp-action-row-primary';
            if (checkBtn) rowPrimary.appendChild(checkBtn);

            var rowSecondary = document.createElement('div');
            rowSecondary.className = 'tp-action-row-secondary';
            if (prevBtn) rowSecondary.appendChild(prevBtn);
            if (skipBtn) rowSecondary.appendChild(skipBtn);
            if (retryBtn) rowSecondary.appendChild(retryBtn);
            if (saveBtn) rowSecondary.appendChild(saveBtn);

            var rowUtility = document.createElement('div');
            rowUtility.className = 'tp-action-row-utility';
            if (speakBtn) rowUtility.appendChild(speakBtn);
            if (hintBtn) rowUtility.appendChild(hintBtn);
            if (revealBtn) rowUtility.appendChild(revealBtn);
            if (resetBtn) rowUtility.appendChild(resetBtn);

            actions.innerHTML = '';
            actions.className = 'typing-actions typing-actions-wrapper';
            actions.appendChild(rowPrimary);
            actions.appendChild(rowSecondary);
            actions.appendChild(rowUtility);
        }
    }

    function renderTypingDetailBox(item, hist) {
        var detailPanel = document.getElementById('tpDetailPanel');
        if (!detailPanel) return;

        var headerHtml = '';
        var panelCls = 'tp-detail-panel show ';
        if (hist.status === 'ok') {
            panelCls += 'is-ok';
            headerHtml = '<div class="tp-detail-hero">' +
                '<div class="tp-detail-hero-icon">🎉</div>' +
                '<div class="tp-detail-hero-content">' +
                '<div class="tp-detail-hero-title">CHÍNH XÁC! ' +
                (hist.isKanjiMatch ? '<span style="font-size:0.82rem; color:#0369a1; font-weight:700; margin-left:8px;">(Chấp nhận dạng kèm Kanji)</span>' : '') +
                '</div>' +
                '<div class="tp-detail-hero-sub">Bạn đã hoàn thành chính xác câu hỏi này.</div>' +
                '</div>' +
                '</div>' +
                (hist.variantNote ? '<div style="margin-bottom:12px; font-size:0.86rem; color:#047857; background:#ecfdf5; border:1px solid #a7f3d0; padding:8px 12px; border-radius:10px;">💡 ' + escapeHtml(hist.variantNote) + '</div>' : '');
        } else if (hist.status === 'reveal') {
            panelCls += 'is-reveal';
            headerHtml = '<div class="tp-detail-hero">' +
                '<div class="tp-detail-hero-icon">👁️</div>' +
                '<div class="tp-detail-hero-content">' +
                '<div class="tp-detail-hero-title">ĐÁP ÁN THAM KHẢO CHUẨN</div>' +
                '<div class="tp-detail-hero-sub">Hãy quan sát kỹ cách đọc, từ vựng và mẫu ngữ pháp trước khi tiếp tục.</div>' +
                '</div>' +
                '</div>';
        } else {
            panelCls += 'is-err';
            headerHtml = '<div class="tp-detail-hero">' +
                '<div class="tp-detail-hero-icon">💡</div>' +
                '<div class="tp-detail-hero-content">' +
                '<div class="tp-detail-hero-title">CHƯA ĐÚNG — CÙNG ĐỐI CHIẾU VÌ SAO SAI NHÉ!</div>' +
                '<div class="tp-detail-hero-sub">So sánh câu bạn vừa gõ với đáp án chuẩn bên dưới để khắc phục lỗi.</div>' +
                '</div>' +
                '</div>';
        }

        var compareHtml = '';
        var primaryReading = window.tpState.mode === 'sentence' ? item.hira : (window.tpState.mode === 'kanji' ? item.kana : (item.kana || item.jp));
        if (hist.status === 'err' && hist.lastInput !== undefined) {
            var diff = buildCharDiffHtml(hist.lastInput, primaryReading);
            compareHtml = '<div class="tp-diff-container" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:12px; margin:14px 0; width:100%; box-sizing:border-box;">' +
                '<div class="tp-diff-col is-user" style="min-width:0; max-width:100%; box-sizing:border-box; overflow:hidden;">' +
                '<div class="tp-diff-header"><span class="tp-diff-badge is-user">🔴 Bạn đã gõ:</span></div>' +
                '<div class="tp-diff-body jp-text" style="word-break:break-word; overflow-wrap:anywhere; white-space:normal; width:100%; box-sizing:border-box;">' + diff.typedHtml + '</div>' +
                '</div>' +
                '<div class="tp-diff-col is-target" style="min-width:0; max-width:100%; box-sizing:border-box; overflow:hidden;">' +
                '<div class="tp-diff-header"><span class="tp-diff-badge is-target">🟢 Đáp án chuẩn:</span></div>' +
                '<div class="tp-diff-body jp-text" style="word-break:break-word; overflow-wrap:anywhere; white-space:normal; width:100%; box-sizing:border-box;">' + diff.targetHtml + '</div>' +
                '</div>' +
                '</div>' +
                ((diff.expectedChunk || diff.gotChunk) ?
                    '<div class="tp-diff-chunk-note" style="word-break:break-word; overflow-wrap:anywhere; box-sizing:border-box; width:100%;">⚠️ <strong>Lệch ký tự:</strong> bạn gõ <span class="diff-bad">' + escapeHtml(diff.gotChunk || '(thiếu)') + '</span> ➔ chuẩn cần <span class="diff-good">' + escapeHtml(diff.expectedChunk || '(không có)') + '</span></div>' : '');
        }

        var whyHtml = '';
        if (hist.status === 'err' && hist.whyWrong && hist.whyWrong.length) {
            whyHtml = '<div class="tp-why-box">' +
                '<div class="tp-why-title">🚨 Phân tích vì sao sai &amp; Bẫy cần tránh:</div>' +
                '<ul class="tp-why-list">' +
                hist.whyWrong.map(function (r) { return '<li>' + r + '</li>'; }).join('') +
                '</ul></div>';
        }

        var meaningHtml = '';
        if (window.tpState.mode === 'sentence') {
            var alts = (item.acceptedHira || []).slice(1, 4);
            meaningHtml = '<div class="tp-meaning-box">' +
                '<div class="tp-info-grid">' +
                '<div class="tp-info-row">' +
                '<span class="tp-info-label">🔊 Hiragana chuẩn:</span>' +
                '<span class="tp-info-val"><strong class="jp-text tp-hira-highlight">' + escapeHtml(item.hira) + '</strong>' +
                '<button type="button" class="tp-btn-audio-pill" onclick="speakCurrentTypingWord(this)" title="Nghe phát âm chuẩn">🔊 Nghe phát âm</button></span>' +
                '</div>' +
                (item.kanjiModel ?
                    '<div class="tp-info-row">' +
                    '<span class="tp-info-label">⛩️ Kèm Kanji:</span>' +
                    '<span class="tp-info-val jp-text" style="font-weight:700; color:#334155;">' + escapeHtml(item.kanjiModel) + '</span>' +
                    '</div>' : '') +
                '<div class="tp-info-row">' +
                '<span class="tp-info-label">🇻🇳 Nghĩa tiếng Việt:</span>' +
                '<span class="tp-info-val"><strong>' + escapeHtml(item.vi) + '</strong></span>' +
                '</div>' +
                '<div class="tp-info-row">' +
                '<span class="tp-info-label">📐 Ngữ pháp (' + escapeHtml(item.pattern) + '):</span>' +
                '<span class="tp-info-val">' + item.grammarRule + '</span>' +
                '</div>' +
                '<div class="tp-info-row">' +
                '<span class="tp-info-label">🧩 Bóc tách câu:</span>' +
                '<span class="tp-info-val">' + item.breakdown + '</span>' +
                '</div>' +
                (alts.length ?
                    '<div class="tp-info-row" style="margin-top:4px;">' +
                    '<span class="tp-info-label">✔️ Biến thể được chấp nhận:</span>' +
                    '<span class="tp-info-val" style="font-size:0.86rem; color:#475569;">' + alts.map(function (a) { return '<code class="jp-text" style="background:#f1f5f9; padding:2px 6px; border-radius:4px;">' + escapeHtml(a) + '</code>'; }).join(' • ') + '</span>' +
                    '</div>' : '') +
                '</div>' +
                '</div>';
        } else if (window.tpState.mode === 'kanji') {
            meaningHtml = '<div class="tp-meaning-box">' +
                '<div class="tp-kanji-card-grid">' +
                '<div class="tp-kanji-big-box jp-text">' + escapeHtml(item.kanji) + '</div>' +
                '<div class="tp-info-grid">' +
                '<div class="tp-info-row">' +
                '<span class="tp-info-label">🔤 Hiragana:</span>' +
                '<span class="tp-info-val"><strong class="jp-text tp-hira-highlight">' + escapeHtml(item.kana) + '</strong>' +
                '<button type="button" class="tp-btn-audio-pill" onclick="speakCurrentTypingWord(this)" title="Nghe phát âm">🔊 Nghe</button></span>' +
                '</div>' +
                '<div class="tp-info-row">' +
                '<span class="tp-info-label">🏮 Âm Hán Việt:</span>' +
                '<span class="tp-info-val"><span class="tp-badge-hv">' + escapeHtml(item.hv) + '</span></span>' +
                '</div>' +
                '<div class="tp-info-row">' +
                '<span class="tp-info-label">🇻🇳 Ý nghĩa:</span>' +
                '<span class="tp-info-val"><strong>' + escapeHtml(item.vi) + '</strong></span>' +
                '</div>' +
                '</div>' +
                '</div>' +
                (item.note ? '<div class="tp-kanji-mnemonic"><strong>🧠 Mẹo nhớ &amp; Phân biệt:</strong> ' + item.note + '</div>' : '') +
                '</div>';
        } else {
            meaningHtml = '<div class="tp-meaning-box">' +
                '<div class="tp-info-grid">' +
                '<div class="tp-info-row">' +
                '<span class="tp-info-label">🇯🇵 Tiếng Nhật:</span>' +
                '<span class="tp-info-val"><strong class="jp-text tp-hira-highlight">' + escapeHtml(item.jp) + '</strong>' +
                (item.kana ? '<span class="jp-text" style="color:var(--primary); margin-left:6px;">【' + escapeHtml(item.kana) + '】</span>' : '') +
                '<button type="button" class="tp-btn-audio-pill" onclick="speakCurrentTypingWord(this)" style="margin-left:8px;" title="Nghe phát âm">🔊 Nghe</button></span>' +
                '</div>' +
                (item.romaji ?
                    '<div class="tp-info-row">' +
                    '<span class="tp-info-label">🔤 Romaji:</span>' +
                    '<span class="tp-info-val"><code>' + escapeHtml(item.romaji) + '</code></span>' +
                    '</div>' : '') +
                '<div class="tp-info-row">' +
                '<span class="tp-info-label">🇻🇳 Nghĩa tiếng Việt:</span>' +
                '<span class="tp-info-val"><strong>' + escapeHtml(item.vi) + '</strong></span>' +
                '</div>' +
                '</div>' +
                '</div>';
        }

        var actionsHtml = '<div class="tp-detail-actions">' +
            '<button type="button" class="tp-btn-primary is-next" style="max-width:280px;" onclick="skipTypingWord()">' +
            '<span>➔ Sang câu tiếp theo</span>' +
            '<kbd class="tp-kbd tp-kbd-light">⏎ Enter</kbd>' +
            '</button>' +
            (hist.status === 'err' ?
                '<button type="button" class="tp-btn-secondary is-retry" onclick="retryCurrentTypingCard()">' +
                '<span>🔄 Thử gõ lại câu này</span>' +
                '<kbd class="tp-kbd">Esc</kbd>' +
                '</button>' : '') +
            '</div>';

        detailPanel.className = panelCls;
        detailPanel.innerHTML = headerHtml + compareHtml + whyHtml + meaningHtml + actionsHtml;
    }

    function renderTypingCard(shouldFocus) {
        ensureTypingLayoutStructure();

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
        var retryBtn = document.getElementById('tpCardRetryBtn');
        var detailPanel = document.getElementById('tpDetailPanel');
        var streakEl = document.getElementById('tpStreakBadge');
        if (streakEl) streakEl.innerText = '🔥 Chuỗi: ' + window.tpState.streak;

        if (!pool.length) {
            var isWrongEmpty = (window.tpState.filterByMode[window.tpState.mode] === 'wrong');
            if (badge) badge.innerText = '0 / 0';
            if (patBadge) patBadge.innerText = isWrongEmpty ? 'Đã hoàn thành!' : 'Bộ lọc trống';
            if (subEl) subEl.innerText = 'TRẠNG THÁI';
            if (promptEl) {
                promptEl.className = 'tp-vi-hero';
                if (isWrongEmpty) {
                    promptEl.innerHTML = '🎉 <strong style="color:#16a34a;">Xuất sắc!</strong> Bạn đã làm đúng và không còn từ/câu nào bị sai trong danh sách nữa.' +
                        '<div style="margin-top:14px;"><button type="button" class="tp-btn-primary is-next" style="padding:9px 20px; font-size:0.95rem; border-radius:10px; cursor:pointer;" onclick="switchTypingLesson(\'all\')">📚 Quay Lại Học Tiếp Toàn Bộ</button></div>';
                } else {
                    promptEl.innerText = 'Không có câu/chữ nào trong bộ lọc này.';
                }
            }
            if (inp) {
                inp.value = '';
                inp.classList.remove('correct', 'wrong');
                inp.disabled = true;
            }
            if (detailPanel) { detailPanel.className = 'tp-detail-panel'; detailPanel.innerHTML = ''; }
            if (retryBtn) retryBtn.style.display = 'none';
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
            inp.placeholder = 'Nhập câu dịch tiếng Nhật bằng Hiragana rồi nhấn Enter...';
            inp.rows = 2;
        } else if (window.tpState.mode === 'kanji') {
            var lessonLabel = item.lesson ? (item.lesson.replace('A2-', 'Bài ') + ' • ') : '';
            badge.innerText = 'Chữ Hán ' + (idx + 1) + ' / ' + pool.length + ' • ' + lessonLabel + '#' + item.stt;
            patBadge.innerText = item.lesson ? item.lesson.replace('A2-', 'Bài ') : ('Kanji ' + item.group);
            subEl.innerText = 'NHÌN CHỮ HÁN (KANJI) — GÕ CÁCH ĐỌC HIRAGANA';
            promptEl.className = 'tp-kanji-hero jp-text';
            promptEl.innerText = item.kanji;
            dirEl.innerHTML = '⬇️ Nhập <strong>cách đọc Hiragana</strong> của chữ Hán trên rồi nhấn <strong>Enter</strong>:';
            inp.placeholder = 'Nhập cách đọc Hiragana rồi nhấn Enter...';
            inp.rows = 1;
        } else {
            badge.innerText = 'Từ ' + (idx + 1) + ' / ' + pool.length + ' • ' + item.lesson;
            patBadge.innerText = 'Từ Vựng A2 • ' + item.lesson;
            subEl.innerText = 'NGHĨA TIẾNG VIỆT — GÕ TỪ TIẾNG NHẬT';
            promptEl.className = 'tp-vi-hero';
            promptEl.innerText = item.vi;
            dirEl.innerHTML = '⬇️ Nhập bằng Hiragana / Kanji / Romaji rồi nhấn <strong>Enter</strong>:';
            inp.placeholder = 'Nhập từ tiếng Nhật rồi nhấn Enter...';
            inp.rows = 1;
        }

        inp.disabled = false;
        var hist = window.tpState.history[item.id];
        var draftVal = window.tpState.drafts[item.id];
        var isWrongFilter = (window.tpState.filterByMode[window.tpState.mode] === 'wrong');

        if (isWrongFilter && hist && hist.status === 'err' && !window.tpState.gradedCurrent) {
            inp.value = '';
            inp.classList.remove('correct', 'wrong');
            detailPanel.className = 'tp-detail-panel';
            detailPanel.innerHTML = '';
            setCheckButtonState('check');
            if (retryBtn) retryBtn.style.display = 'none';
        } else if (hist && (hist.status === 'ok' || hist.status === 'err' || hist.status === 'reveal')) {
            inp.value = draftVal !== undefined ? draftVal : (hist.lastInput || '');
            if (hist.status === 'ok') {
                inp.classList.remove('wrong');
                inp.classList.add('correct');
            } else if (hist.status === 'err') {
                inp.classList.remove('correct');
                inp.classList.add('wrong');
            } else {
                inp.classList.remove('correct', 'wrong');
            }
            renderTypingDetailBox(item, hist);
            window.tpState.gradedCurrent = true;
            setCheckButtonState('next');
            if (retryBtn) {
                retryBtn.style.background = '';
                retryBtn.className = 'tp-btn-secondary is-retry';
                retryBtn.innerHTML = '<span>🔄 Gõ Lại</span><kbd class="tp-kbd">Esc</kbd>';
                retryBtn.style.display = (hist.status === 'err' || hist.status === 'reveal') ? 'inline-flex' : 'none';
            }
        } else {
            inp.value = draftVal || '';
            inp.classList.remove('correct', 'wrong');
            detailPanel.className = 'tp-detail-panel';
            detailPanel.innerHTML = '';
            window.tpState.gradedCurrent = false;
            setCheckButtonState('check');
            if (retryBtn) retryBtn.style.display = 'none';
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
            if (inp) {
                inp.classList.remove('wrong');
                inp.classList.add('correct');
            }
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
            if (inp) {
                inp.classList.remove('correct');
                inp.classList.add('wrong');
            }
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
        if (!window.tpInitialized) {
            restoreTypingStudioState();
        }
        window.tpInitialized = true;
        ensureTypingLayoutStructure();
        bindTypingInputEvents();
        updateTypingModeButtons();
        renderTypingFilters();
        renderTypingControlsState();
        renderTypingCard(false);
    }

    function switchTypingMode(mode) {
        window.tpState.mode = mode;
        window.tpState.gradedCurrent = false;
        window.tpState.wrongQueue = null;
        updateTypingModeButtons();
        renderTypingFilters();
        renderTypingCard(true);
        persistCheckpoint();
    }

    function switchTypingLesson(lessonKey) {
        var m = window.tpState.mode;
        window.tpState.filterByMode[m] = lessonKey;
        var bucket = getActiveBucketKey();
        window.tpState.idxByBucket[bucket] = 0;
        window.tpState.gradedCurrent = false;

        if (lessonKey === 'wrong') {
            var all = getModeItems(m);
            window.tpState.wrongQueue = all.filter(function (x) {
                return window.tpState.history[x.id] && window.tpState.history[x.id].status === 'err';
            });
        } else {
            window.tpState.wrongQueue = null;
        }

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
        var m = window.tpState.mode;
        var curF = window.tpState.filterByMode[m] || 'all';
        var bucket = getActiveBucketKey();

        if (curF === 'wrong' && Array.isArray(window.tpState.wrongQueue)) {
            window.tpState.wrongQueue.sort(function () { return Math.random() - 0.5; });
        } else {
            var shuffled = pool.map(function (x) { return x.id; }).sort(function () { return Math.random() - 0.5; });
            window.tpState.orderByBucket[bucket] = shuffled;
        }

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
        var inp = document.getElementById('tpCardInput');
        if (inp) {
            inp.value = '';
            inp.classList.remove('correct', 'wrong');
        }
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

    function showRoundSummaryModal(total, wrongCount) {
        var m = window.tpState.mode;
        var modeLabel = m === 'sentence' ? 'câu' : (m === 'kanji' ? 'chữ Hán' : 'từ');
        var modalId = 'tpRoundSummaryModal';
        var existing = document.getElementById(modalId);
        if (existing) existing.remove();

        var okCount = Math.max(0, total - wrongCount);
        var div = document.createElement('div');
        div.id = modalId;
        div.style.cssText = 'position:fixed; inset:0; background:rgba(15,23,42,0.65); z-index:99999; display:flex; align-items:center; justify-content:center; padding:16px; backdrop-filter:blur(4px);';
        div.innerHTML = 
            '<div style="background:#ffffff; border-radius:18px; max-width:480px; width:100%; padding:26px 24px; box-shadow:0 20px 40px rgba(0,0,0,0.25); text-align:center; border:2px solid #e2e8f0;">' +
            '  <div style="font-size:2.8rem; margin-bottom:6px;">🎉</div>' +
            '  <h3 style="font-size:1.3rem; font-weight:900; color:#1e1b4b; margin:0 0 10px 0;">Hoàn Thành 1 Vòng ' + total + ' ' + modeLabel + '!</h3>' +
            '  <p style="color:#475569; font-size:0.95rem; margin:0 0 18px 0; line-height:1.6;">' +
            '    Kết quả vòng này: <strong style="color:#16a34a;">' + okCount + ' Đúng</strong> • <strong style="color:#e11d48;">' + wrongCount + ' Chưa chuẩn</strong>.<br>' +
            '    Bạn có muốn gom ngay <strong>' + wrongCount + ' ' + modeLabel + ' chưa đúng</strong> này để gõ lại cho thuộc không?' +
            '  </p>' +
            '  <div style="display:flex; flex-direction:column; gap:10px;">' +
            '    <button type="button" id="btnGoToWrong" style="background:#e11d48; color:#ffffff; font-weight:800; font-size:1rem; padding:12px 20px; border-radius:10px; border:none; cursor:pointer; box-shadow:0 4px 12px rgba(225,29,72,0.3);">' +
            '      🔁 Bắt Đầu Vòng Gõ Lại ' + wrongCount + ' ' + modeLabel + ' Sai Ngay' +
            '    </button>' +
            '    <button type="button" id="btnRestartRound" style="background:#0284c7; color:#ffffff; font-weight:700; font-size:0.92rem; padding:10px 18px; border-radius:10px; border:none; cursor:pointer;">' +
            '      🔄 Luyện Lại Toàn Bộ Vòng Này Từ Đầu' +
            '    </button>' +
            '    <button type="button" id="btnCloseModal" style="background:#f1f5f9; color:#475569; font-weight:700; font-size:0.88rem; padding:8px 16px; border-radius:8px; border:1px solid #cbd5e1; cursor:pointer;">' +
            '      Tiếp tục xem lại (Đóng)' +
            '    </button>' +
            '  </div>' +
            '</div>';

        document.body.appendChild(div);

        document.getElementById('btnGoToWrong').onclick = function () {
            div.remove();
            switchTypingLesson('wrong');
        };
        document.getElementById('btnRestartRound').onclick = function () {
            div.remove();
            var bucket = getActiveBucketKey();
            window.tpState.idxByBucket[bucket] = 0;
            window.tpState.gradedCurrent = false;
            renderTypingCard(true);
        };
        document.getElementById('btnCloseModal').onclick = function () {
            div.remove();
            var bucket = getActiveBucketKey();
            window.tpState.idxByBucket[bucket] = 0;
            window.tpState.gradedCurrent = false;
            renderTypingCard(true);
        };
    }

    function skipTypingWord() {
        var pool = getFilteredTypingPool();
        if (!pool.length) return;
        var bucket = getActiveBucketKey();
        var cur = window.tpState.idxByBucket[bucket] || 0;
        var m = window.tpState.mode;
        var curF = window.tpState.filterByMode[m] || 'all';

        // Nếu vừa đi qua câu cuối cùng của vòng câu sai:
        if (curF === 'wrong') {
            if (cur >= pool.length - 1) {
                var stillWrong = pool.filter(function (x) {
                    var h = window.tpState.history[x.id];
                    return h && h.status === 'err';
                });
                if (stillWrong.length === 0) {
                    window.tpState.wrongQueue = [];
                    window.tpState.idxByBucket[bucket] = 0;
                    window.tpState.gradedCurrent = false;
                    renderTypingFilters();
                    renderTypingCard(true);
                    persistCheckpoint();
                    notify('🎉 Tuyệt vời! Bạn đã sửa đúng hết toàn bộ các câu sai!');
                    return;
                } else {
                    window.tpState.wrongQueue = stillWrong;
                    window.tpState.idxByBucket[bucket] = 0;
                    window.tpState.gradedCurrent = false;
                    renderTypingFilters();
                    renderTypingCard(true);
                    persistCheckpoint();
                    notify('🔁 Vòng mới: Còn lại ' + stillWrong.length + ' câu chưa đúng, tiếp tục nhé!');
                    return;
                }
            }
        } else {
            // Chế độ bài học bình thường:
            if (cur >= pool.length - 1) {
                var wrongCount = pool.filter(function (x) {
                    var h = window.tpState.history[x.id];
                    return h && (h.status === 'err' || h.status === 'reveal');
                }).length;

                if (wrongCount > 0) {
                    showRoundSummaryModal(pool.length, wrongCount);
                    return;
                }
            }
        }

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
        window.tpState.wrongQueue = null;
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
            } else if (e.key === 'Escape') {
                if (window.tpState.gradedCurrent) {
                    e.preventDefault();
                    retryCurrentTypingCard();
                }
            } else if ((e.key === 'Tab' || (e.altKey && e.key.toLowerCase() === 's')) && !e.shiftKey) {
                e.preventDefault();
                skipOrPassCurrentTypingWord();
            } else if (e.altKey && e.key.toLowerCase() === 'h') {
                e.preventDefault();
                showTypingHint();
            } else if (e.altKey && e.key.toLowerCase() === 'a') {
                e.preventDefault();
                speakCurrentTypingWord();
            }
        });
        inp.addEventListener('input', function () {
            inp.classList.remove('correct', 'wrong');
            var pool = getFilteredTypingPool();
            var bucket = getActiveBucketKey();
            var item = pool[window.tpState.idxByBucket[bucket] || 0];
            if (item) {
                window.tpState.drafts[item.id] = inp.value;
                if (window.tpState.gradedCurrent) {
                    window.tpState.gradedCurrent = false;
                    setCheckButtonState('check');
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
    window.skipOrPassCurrentTypingWord = skipOrPassCurrentTypingWord;
    window.manualSaveTypingProgress = manualSaveTypingProgress;
    window.resetCurrentTypingMode = resetCurrentTypingMode;
    window.getActiveBucketKey = getActiveBucketKey;
    window.getFilteredTypingPool = getFilteredTypingPool;
    window.bindTypingInputEvents = bindTypingInputEvents;
})(window);
