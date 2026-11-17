// Known out-of-scope grammar guard after manual review of all Kaiwa text.
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert');
const root = path.resolve(__dirname, '../..');
const c = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(root, 'assets/data/kaiwa_topics_data.js'), 'utf8'), c);
const topics = c.window.KAIWA_TOPICS_DATA;
const tips = c.window.KAIWA_TIPS;
const banned = /ように|ようです|ほうがいい|方がいい|ながら|[てで]しま(?:う|っ|いま)|なければ|なくては|聞かせて|くださって|お願いできます|もし|行くなら|終わったら|飲むと|話すと|あげると|食べられ|答えられ|〜ので/;
function scan(value, where) {
    if (typeof value === 'string') {
        assert(!banned.test(value.replace(/\s+/g, '')), `${where}: ${value}`);
    } else if (Array.isArray(value)) value.forEach((item, i) => scan(item, `${where}[${i}]`));
    else if (value && typeof value === 'object') Object.entries(value).forEach(([key, item]) => scan(item, `${where}.${key}`));
}
scan(topics, 'topics');
scan(tips, 'tips');
assert.strictEqual(topics.length, 4);
assert.strictEqual(tips.length, 5);
assert.strictEqual(topics.reduce((n, t) => n + t.coreQuestions.length, 0), 22);
let answers = 0;
for (const topic of topics) {
    assert(fs.existsSync(path.join(root, topic.image)));
    assert.strictEqual(new Set(topic.coreQuestions.map(q => q.id)).size, topic.coreQuestions.length);
    for (const q of topic.coreQuestions) {
        assert(q.qJp && q.qVi && q.intent && q.mindmap.length && q.vocab.length);
        assert(q.sampleAnswers.length);
        for (const answer of q.sampleAnswers) {
            assert(['basic', 'easy'].includes(answer.level));
            assert(answer.jp && answer.vi && answer.keyPoints);
            answers++;
        }
    }
    for (const line of topic.fullDialogue) assert(line.jp && line.vi && line.name);
}
console.log(`Kaiwa reviewed: 4 topics, 22 questions, ${answers} answers, all dialogues and 5 tips.`);
