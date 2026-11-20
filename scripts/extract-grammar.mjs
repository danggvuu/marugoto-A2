import { readFileSync, writeFileSync } from 'node:fs';
import { DOMParser } from 'linkedom';
const entries = {};
for(const level of ['A2-1','A2-2']) for(let lesson=1;lesson<=18;lesson++) {
 const file = level === 'A2-2' ? `Marugoto_A2_2_Lesson_${lesson}.html` : `Marugoto_A2_Lesson_${lesson}.html`;
 const html = readFileSync(new URL(`../legacy_html/lessons/${file}`, import.meta.url),'utf8');
 const document = new DOMParser().parseFromString(html,'text/html');
 entries[`${level}/${lesson}`] = [...document.querySelectorAll('section[id^="sec-grammar"]')].map((section,index) => ({
  id:lesson*100+index, level, lesson, lessonTitle:'',
  title:section.querySelector('.section-title')?.textContent?.trim() || `Mẫu câu ${index+1}`,
  formula:section.querySelector('.rule-formula')?.textContent?.trim() || '',
  meaning:section.querySelector('.rule-meaning')?.textContent?.trim() || [...section.querySelectorAll(':scope > p')].map(node=>node.textContent?.trim()).filter(Boolean).join(' '),
  examples:[...section.querySelectorAll('.example-item')].map(example=>({jp:example.querySelector('.ex-jp')?.textContent?.trim()||'',vi:example.querySelector('.ex-vi')?.textContent?.trim()||''})).filter(example=>example.jp&&example.vi),
 }));
}
writeFileSync(new URL('../data/lesson_grammar.json',import.meta.url),JSON.stringify(entries,null,2)+'\n');
console.log(`Extracted grammar for ${Object.keys(entries).length} lessons`);
