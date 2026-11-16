/* Verify lesson scope AND every Han character, including possible distractors. */
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert');
const root = path.resolve(__dirname, '../..');
const read = name => fs.readFileSync(path.join(root, name), 'utf8');
const c = { window: {} };
vm.runInNewContext(read('assets/data/vocab_kanji_check_11_18_data.js'), c);
const data = c.window.VOCAB_KANJI_CHECK_DATA;
const allowedLessons = new Set(Array.from({length:8}, (_,i) => `A2-${i+11}`));
const master = JSON.parse(read('data/kanji_extracted.json'));
const allowedChars = new Set(master.filter(x => /^L1[1-8]$/.test(x.lesson)).map(x => x.char));
assert.strictEqual(data.version, 2);
assert.strictEqual(data.allowedKanji.length, allowedChars.size);
assert(data.allowedKanji.every(char => allowedChars.has(char)));
const all = [...data.vocab, ...data.kanji];
assert.strictEqual(new Set(all.map(x => x.id)).size, all.length);
for (const item of all) {
    assert(allowedLessons.has(item.lesson), `out of scope: ${item.id}`);
    assert(item.kana && item.vi && item.jp);
    assert(!/\p{Script=Han}/u.test(item.kana), `Kana contains Kanji: ${item.id}`);
}
for (const item of data.kanji) {
    const chars = item.jp.replace(/々/g, '').match(/\p{Script=Han}/gu);
    assert(chars?.length);
    assert(chars.every(char => allowedChars.has(char)), `outside character: ${item.jp}`);
}
for (const lesson of allowedLessons) {
    assert(data.kanji.some(item => item.lesson === lesson));
    assert(data.vocab.some(item => item.lesson === lesson));
}
assert(!data.kanji.some(item => item.jp === '日本酒'), 'must exclude compounds with earlier-only characters');
console.log(`Scope validated: ${data.vocab.length} vocab, ${data.kanji.length} Kanji words, ${allowedChars.size} allowed characters.`);
