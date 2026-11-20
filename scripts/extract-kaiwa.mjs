import { readFileSync, writeFileSync } from 'node:fs';
import { runInNewContext } from 'node:vm';

// Repository-owned data script only. Never evaluate user-provided JavaScript.
const source = readFileSync(new URL('../assets/data/kaiwa_topics_data.js', import.meta.url), 'utf8');
const context = { window: {} };
runInNewContext(source, context, { timeout: 1000 });
const topics = context.window.KAIWA_TOPICS_DATA;
if (!Array.isArray(topics) || topics.length !== 4) throw new Error('Expected four Kaiwa topics');
writeFileSync(new URL('../data/kaiwa_topics.json', import.meta.url), JSON.stringify(topics, null, 2) + '\n');
console.log(`Extracted ${topics.length} Kaiwa topics`);
