import { readFile, readdir, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';

const root = process.cwd();
const sourceDir = path.join(root, 'assets/js/lessons');
const outputDir = path.join(root, 'data/lessons');
await mkdir(outputDir, { recursive: true });

function extractArray(source, name) {
  const match = source.match(new RegExp(`(?:const|let|var) ${name}\\s*=\\s*(\\[[\\s\\S]*?\\]);`));
  if (!match) return [];
  try { return JSON.parse(match[1]); }
  catch { return Function(`"use strict"; return (${match[1]});`)(); }
}

for (const file of (await readdir(sourceDir)).filter(name => /^lesson_(?:a2_2_)?\d{2}\.js$/.test(name)).sort()) {
  const source = await readFile(path.join(sourceDir, file), 'utf8');
  const lesson = Number(file.match(/(\d{2})\.js$/)[1]);
  const level = file.includes('a2_2') ? 'A2-2' : 'A2-1';
  const data = {
    level, lesson,
    vocab: extractArray(source, 'VOCAB_DATA'),
    verbs: extractArray(source, 'VERB_DATA'),
    quiz: extractArray(source, 'QUIZ_DATA'),
  };
  await writeFile(path.join(outputDir, `${level.toLowerCase().replace('-', '_')}_${String(lesson).padStart(2, '0')}.json`), `${JSON.stringify(data, null, 2)}\n`);
}
console.log(`Extracted 36 lesson JSON files to ${path.relative(root, outputDir)}`);
