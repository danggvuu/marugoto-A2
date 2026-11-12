/**
 * jp-typing-grader.js
 * Smart, grammar-aware Japanese sentence & Hiragana grader.
 * Recognizes natural Japanese variations (adverb/object scrambling, optional
 * 1st-person topic わたしは, に/へ direction particles, んです/のです,
 * Katakana <-> Hiragana, numerals <-> Kana, optional ですよ/です) while
 * still strictly enforcing conjugation, grammar traps, and Kanji-vs-Hiragana rules.
 */
(function (root, factory) {
    if (typeof module === 'object' && module.exports) {
        module.exports = factory();
    } else {
        root.JpTypingGrader = factory();
    }
}(typeof self !== 'undefined' ? self : this, function () {
    'use strict';

    var PUNCT_RE = /[()（）「」『』""''…・~～/／、,。.,?!？！\s\-_\t　]/g;
    var KANJI_RE = /[\u4E00-\u9FAF\u3400-\u4DBF]/;

    // Adverbs and standalone time expressions that naturally scramble with
    // particle-marked phrases before the predicate of the same clause.
    var FREE_MODIFIERS = new Set([
        'よく', 'ときどき', 'あまり', 'ぜんぜん', 'いつも', 'まいにち', 'まいあさ',
        'まいばん', 'まいしゅう', 'たまに', 'たくさん', 'ちょっと', 'もう', 'まだ',
        'すぐ', 'ゆっくり', 'きゅうに', 'いちばん', 'とても', 'かなり', 'たぶん',
        'きのう', 'きょう', 'あした', 'おととい', 'あさって', 'こんしゅう',
        'らいしゅう', 'せんしゅう', 'こんばん', 'こんや', 'けさ', 'ひとりで',
        'じぶんで', 'みんなと', 'かぞくと', '30ぷんぐらい', 'さんじゅっぷんぐらい',
        'さんじっぷんぐらい', 'けんこうのために'
    ]);

    var DIGIT_KANAMAP = [
        ['38', ['さんじゅうはち']],
        ['30', ['さんじゅう', 'さんじゅっ', 'さんじっ']],
        ['20', ['にじゅう', 'はた']],
        ['10', ['じゅう', 'じゅっ', 'じっ']],
        ['1', ['いち', 'いっ']],
        ['2', ['に']],
        ['3', ['さん']],
        ['4', ['よん', 'し']],
        ['5', ['ご']],
        ['6', ['ろく', 'ろっ']],
        ['7', ['なな', 'しち']],
        ['8', ['はち', 'はっ']],
        ['9', ['きゅう', 'く']]
    ];

    function toHiragana(str) {
        if (!str) return '';
        var out = '';
        var s = String(str);
        for (var i = 0; i < s.length; i++) {
            var code = s.charCodeAt(i);
            if (code >= 0x30A1 && code <= 0x30F6) {
                out += String.fromCharCode(code - 0x60);
            } else if (code >= 0xFF01 && code <= 0xFF5E) {
                out += String.fromCharCode(code - 0xFEE0);
            } else {
                out += s.charAt(i);
            }
        }
        return out.toLowerCase();
    }

    function containsKanji(str) {
        return KANJI_RE.test(str || '');
    }

    function cleanCompare(str, convertKata) {
        if (!str) return '';
        var base = convertKata ? toHiragana(str) : String(str).toLowerCase();
        return base.trim().replace(PUNCT_RE, '');
    }

    // Normalize common numeral & Katakana/Hiragana & polite-ending equivalences
    // strictly WITHOUT weakening tense, polarity, or grammar particles.
    function normalizeForSemanticEq(cleanedStr) {
        var s = cleanedStr || '';
        // Unify explanatory ~んです / ~のです forms
        s = s
            .replace(/のですか$/g, 'んですか')
            .replace(/のですが/g, 'んですが')
            .replace(/のです$/g, 'んです')
            .replace(/のです([よね])/g, 'んです$1');
        // Unify negative adjective/noun polite endings
        s = s
            .replace(/じゃありません/g, 'じゃないです')
            .replace(/ではありません/g, 'じゃないです')
            .replace(/くありません/g, 'くないです');
        // Unify directional に <-> へ strictly right before motion verbs
        s = s.replace(/([ぁ-んー]+)へ((?:もって)?(?:い|き|かえ)[くきけっ])/g, '$1に$2');
        s = s.replace(/([ぁ-んー]+)へ(いきます|きます|かえります|いきました|きました|かえりました|いく|くる|かえる|いった|きた|かえった)/g, '$1に$2');
        // Unify common lexical pairs & optional を before suru-verbs
        s = s
            .replace(/ゆうごはん|ゆうはん/g, 'ばんごはん')
            .replace(/ほんとに/g, 'ほんとうに')
            .replace(/(かいもの|しょくじ|じょぎんぐ|たいそう|さんぽ|うんてん|うんどう|そうじ|せんたく|べんきょう|けっこん|むり|しんこきゅう|すとれっち|よが|とれーにんぐ|うぉーきんぐ|すいえい|りょこう|りょうり)を(し|す)/g, '$1$2');
        // Normalize small っ in 30ぷん/10ぷん readings (longest match first so さんじゅっぷん -> 30ぷん, not さん10ぷん)
        s = s
            .replace(/さんじゅっぷん|さんじっぷん|さんじゅうぷん/g, '30ぷん')
            .replace(/じゅっぷん|じっぷん|じゅうぷん/g, '10ぷん')
            .replace(/([にさんよん])\s*ねん/g, function (m, num) {
                var map = { 'に': '2', 'さん': '3', 'よん': '4' };
                return (map[num] || num) + 'ねん';
            });
        for (var i = 0; i < DIGIT_KANAMAP.length; i++) {
            var d = DIGIT_KANAMAP[i][0];
            var forms = DIGIT_KANAMAP[i][1];
            // Only replace trailing/numeric compounds where needed
            if (d === '38') s = s.replace(/さんじゅうはち(ど)/g, '38$1');
            if (d === '20') s = s.replace(/にじゅう(にん)/g, '20$1');
            if (d === '10') s = s.replace(/じゅう(にん)/g, '10$1');
            void forms;
        }
        return s;
    }

    function isProtectedBoundaryToken(tok) {
        if (!tok) return true;
        var clean = tok.replace(/[、。,.]/g, '');
        if (!clean) return true;
        // Clause boundaries, topic/subject markers, or predicates must NEVER reorder across
        return /(は|が|も|なら|ます|ました|ません|ませんでした|です|でした|じゃないです|だ|だった|ない|なかった|ている|ていた|て|たり|まえに|あとで|ときに|とき|ために|から|ので|けど|んですが|ですが|ても|たら|おもいます|いっていました|ください|くださいませんか|いただけませんか)$/.test(clean);
    }

    function isAdjunctToken(tok) {
        var clean = tok.replace(/[、。,.]/g, '');
        if (!clean) return false;
        if (FREE_MODIFIERS.has(clean)) return true;
        // Complete adjunct NP ending in safe postposition (not は/が/の)
        if (!isProtectedBoundaryToken(clean) && /[をでにとへ]$/.test(clean) && clean.length >= 2) {
            return true;
        }
        return false;
    }

    // Group glued modifiers (e.g., Xの + Y, adj + Noun) inside a comma-separated clause
    // so relative phrases and NのN compounds never split apart during scrambling.
    function groupAtomicChunks(tokens) {
        var chunks = [];
        var i = 0;
        while (i < tokens.length) {
            var cur = tokens[i];
            var stripped = cur.replace(/[、。,.]/g, '');
            // Glue Xの + following noun chunk, or い-adj / な-adj(な) modifying the following noun chunk
            while (
                i + 1 < tokens.length &&
                !/[、。,.]$/.test(cur) &&
                (/の$/.test(stripped) ||
                    /(?:おいしい|おもしろい|たのしい|あたらしい|ふるい|やすい|たかい|ひろい|せまい|しずかな|にぎやかな|ゆうめいな|きれいな|すてきな|わるい|よい|いい|ちいさい|おおきい|くらい|あかるい|からい)$/.test(stripped))
            ) {
                i++;
                cur += tokens[i];
                stripped = cur.replace(/[、。,.]/g, '');
            }
            chunks.push(cur);
            i++;
        }
        return chunks;
    }

    // Generate grammatically equivalent clause word-order variants from a space-tokenized sentence.
    function generateSpacedVariants(spacedSentence) {
        var results = new Set();
        if (!spacedSentence) return [];

        // Split sentence into comma/period segments (preserve punctuation-free joining)
        var rawSegments = String(spacedSentence).trim().split(/(?<=[、。])|\s+(?=まえに、)/);
        var perSegmentOptions = [];

        for (var sIdx = 0; sIdx < rawSegments.length; sIdx++) {
            var seg = rawSegments[sIdx].trim();
            if (!seg) continue;
            var tokens = groupAtomicChunks(seg.split(/\s+/).filter(Boolean));
            var segForms = new Set([tokens.join('')]);

            // 1. Optional single adjacent swaps between two reorderable adjuncts right before the clause predicate
            for (var i = 0; i < tokens.length - 1; i++) {
                var a = tokens[i];
                var b = tokens[i + 1];
                if (isAdjunctToken(a) && isAdjunctToken(b)) {
                    var swapped = tokens.slice();
                    swapped[i] = b;
                    swapped[i + 1] = a;
                    segForms.add(swapped.join(''));
                }
            }

            // 2. Permute a contiguous run of up to 3 adjunct tokens (e.g., [time] [partner] [place])
            for (var start = 0; start <= tokens.length - 3; start++) {
                if (isAdjunctToken(tokens[start]) && isAdjunctToken(tokens[start + 1]) && isAdjunctToken(tokens[start + 2])) {
                    var sub = [tokens[start], tokens[start + 1], tokens[start + 2]];
                    var perms = [
                        [0, 1, 2], [0, 2, 1], [1, 0, 2],
                        [1, 2, 0], [2, 0, 1], [2, 1, 0]
                    ];
                    for (var p = 0; p < perms.length; p++) {
                        var copy = tokens.slice();
                        copy[start] = sub[perms[p][0]];
                        copy[start + 1] = sub[perms[p][1]];
                        copy[start + 2] = sub[perms[p][2]];
                        segForms.add(copy.join(''));
                    }
                }
            }

            // 3. Also allow switching V1たり、V2たり within comma segments? Keep V1/V2 order deterministic unless handled explicitly
            perSegmentOptions.push(Array.from(segForms));
        }

        // Cartesian product capped safely (most sentences have 1-4 combinations)
        var built = [''];
        for (var k = 0; k < perSegmentOptions.length; k++) {
            var opts = perSegmentOptions[k];
            var next = [];
            for (var bIdx = 0; bIdx < built.length; bIdx++) {
                for (var oIdx = 0; oIdx < opts.length; oIdx++) {
                    if (next.length < 48) {
                        next.push(built[bIdx] + opts[oIdx]);
                    }
                }
            }
            built = next;
        }
        for (var r = 0; r < built.length; r++) {
            results.add(built[r]);
        }
        return Array.from(results);
    }

    function expandSubjectAndTailOptions(normStr, item) {
        var out = new Set([normStr]);
        var vi = (item && item.vi) ? item.vi.toLowerCase() : '';
        var hasFirstPersonVi = /\b(tôi|mình|tớ)\b/.test(vi);

        // Optional trailing よ on advisory/explanatory polite forms
        Array.from(out).forEach(function (v) {
            if (/(いいです|んです)よ$/.test(v)) {
                out.add(v.slice(0, -1));
            } else if (/と(いいです|おもいます)$/.test(v) || /んです$/.test(v)) {
                out.add(v + 'よ');
            }
        });

        // Optional leading わたしは / ぼくは when sentence has implicit/explicit 1st person subject
        Array.from(out).forEach(function (v) {
            if (/^(わたしは|ぼくは)/.test(v)) {
                out.add(v.replace(/^(わたしは|ぼくは)/, ''));
            } else if (hasFirstPersonVi && !/^[ぁ-ん]+さんは/.test(v)) {
                out.add('わたしは' + v);
                out.add('ぼくは' + v);
            }
        });

        // Also allow swap around clause comma for V1たり、V2たり when paired with adverb at front
        return Array.from(out);
    }

    function buildEquivalentSet(item) {
        var exactSet = new Set();
        var variantSet = new Set();
        var rawHiraList = [item.hira].concat(item.acceptedHira || []).filter(Boolean);

        rawHiraList.forEach(function (raw) {
            var cleaned = cleanCompare(raw, true);
            if (cleaned) exactSet.add(cleaned);
            var sem = normalizeForSemanticEq(cleaned);
            if (sem) exactSet.add(sem);

            // Generate natural word-order + optional subject/tail equivalents
            var spacedVars = generateSpacedVariants(raw);
            spacedVars.forEach(function (sv) {
                var c = normalizeForSemanticEq(cleanCompare(sv, true));
                expandSubjectAndTailOptions(c, item).forEach(function (opt) {
                    if (opt && !exactSet.has(opt)) {
                        variantSet.add(opt);
                    }
                });
            });
            expandSubjectAndTailOptions(sem, item).forEach(function (opt) {
                if (opt && !exactSet.has(opt)) {
                    variantSet.add(opt);
                }
            });
        });

        return { exactSet: exactSet, variantSet: variantSet };
    }

    /**
     * Grade a user answer cleanly.
     * @param {string} rawUser
     * @param {object} item
     * @param {'sentence'|'kanji'|'vocab'} mode
     * @param {{allowKanji?: boolean}} opts
     */
    function grade(rawUser, item, mode, opts) {
        opts = opts || {};
        var normUserHira = cleanCompare(rawUser, true);
        if (!normUserHira) {
            return { ok: false, empty: true, matchType: null, variantNote: null };
        }

        if (mode === 'kanji') {
            if (containsKanji(rawUser)) {
                return { ok: false, matchType: null, variantNote: null };
            }
            var kTargets = (item.accepted || [item.kana]).map(function (a) { return cleanCompare(a, false); });
            return {
                ok: kTargets.indexOf(normUserHira) !== -1,
                matchType: 'exact',
                variantNote: null
            };
        }

        if (mode === 'vocab') {
            var rawLower = cleanCompare(rawUser, false);
            var vTargets = [item.jp, item.kana, item.romaji].filter(Boolean);
            var vOk = vTargets.some(function (t) {
                return cleanCompare(t, true) === normUserHira || cleanCompare(t, false) === rawLower;
            });
            return { ok: vOk, matchType: 'exact', variantNote: null };
        }

        // mode === 'sentence'
        // 1. Check Kanji strictness first (Kanji allowed ONLY when allowKanji toggle is ON)
        if (containsKanji(rawUser)) {
            if (opts.allowKanji) {
                var cleanKanjiModel = item.kanjiModel
                    ? String(item.kanjiModel).replace(/（[／/][^）]*）/g, '').trim()
                    : '';
                var rawKanjiSources = [item.kanjiModel, cleanKanjiModel]
                    .concat(item.kanjiAccepted || []).filter(Boolean);
                var kanjiTargets = rawKanjiSources
                    .map(function (k) { return normalizeForSemanticEq(cleanCompare(k, true)); });
                var normSemKanjiUser = normalizeForSemanticEq(normUserHira);
                var spacedKanji = [];
                rawKanjiSources.forEach(function (src) {
                    var spacedSrc = String(src)
                        .replace(/（[／/][^）]*）/g, '')
                        .replace(/([、。])/g, '$1 ')
                        .replace(/(よく|ときどき|いつも|あまり|ぜんぜん|たくさん|すこし|ちょっと|ゆっくり|しっかり|きゅうに|毎日|まいにち)/g, ' $1 ')
                        .replace(/([\u4E00-\u9FAF\u30A0-\u30FF0-9ー][をにへでと])(?=[^\s、。])/g, '$1 ')
                        .replace(/\s+/g, ' ')
                        .trim();
                    spacedKanji = spacedKanji.concat(generateSpacedVariants(spacedSrc));
                });
                var kanjiMatch = kanjiTargets.indexOf(normSemKanjiUser) !== -1 ||
                    spacedKanji.some(function (sk) {
                        return expandSubjectAndTailOptions(normalizeForSemanticEq(cleanCompare(sk, true)), item)
                            .indexOf(normSemKanjiUser) !== -1;
                    });
                if (!kanjiMatch) {
                    return { ok: false, matchType: null, variantNote: null };
                }
                var isExactKanji = kanjiTargets.indexOf(normSemKanjiUser) !== -1;
                return {
                    ok: true,
                    matchType: isExactKanji ? 'kanji' : 'variant',
                    variantNote: isExactKanji ? null : '✨ Hợp lệ! Trật tự từ / cách diễn đạt tự nhiên (kèm Kanji) hoàn toàn đúng ngữ pháp.'
                };
            }
            return { ok: false, matchType: null, variantNote: null };
        }

        // 2. Smart Pure-Hiragana/Katakana Semantic & Word-Order Grading
        var userSem = normalizeForSemanticEq(normUserHira);
        var eq = buildEquivalentSet(item);
        if (eq.exactSet.has(normUserHira) || eq.exactSet.has(userSem)) {
            return { ok: true, matchType: 'exact', variantNote: null };
        }
        if (eq.variantSet.has(userSem)) {
            return {
                ok: true,
                matchType: 'variant',
                variantNote: '✨ Hợp lệ! Trật tự từ / cách diễn đạt tự nhiên hoàn toàn đúng ngữ pháp (đối chiếu câu mẫu gốc của cô bên dưới).'
            };
        }
        return { ok: false, matchType: null, variantNote: null };
    }

    return {
        toHiragana: toHiragana,
        containsKanji: containsKanji,
        cleanCompare: cleanCompare,
        normalizeForSemanticEq: normalizeForSemanticEq,
        generateSpacedVariants: generateSpacedVariants,
        grade: grade
    };
}));
