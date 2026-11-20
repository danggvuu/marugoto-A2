import {test, expect} from '@playwright/test';

test('all repository study data meets route, answer and coverage invariants',async({page})=>{
 await page.goto('/');
 const report=await page.evaluate(async()=>{
  const data=await import(/* @vite-ignore */ '/src/services/dataLoader.ts');
  return {
   vocab:data.a2_2VocabularyTotal,
   kanji:data.allKanji.length,
   lessons:data.lessonSummaries.map((lesson:any)=>({level:lesson.level,number:lesson.number,vocab:lesson.vocab.length,grammar:lesson.grammar.length,quiz:lesson.quiz.length,invalid:lesson.quiz.some((q:any)=>q.options.length!==4||q.correct<0||q.correct>=4)})),
   exams:data.examSets.map((set:any)=>({code:set.code,items:set.sections.flatMap((s:any)=>s.groups.flatMap((g:any)=>g.items))})),
  };
 });
 expect(report.vocab).toBe(382);expect(report.kanji).toBe(291);expect(report.lessons).toHaveLength(36);
 for(const lesson of report.lessons){expect(lesson.vocab,JSON.stringify(lesson)).toBeGreaterThan(0);expect(lesson.grammar).toBeGreaterThan(0);expect(lesson.quiz).toBe(15);expect(lesson.invalid).toBe(false);}
 expect(report.exams.some((set:any)=>set.code==='MINI-11-14')).toBe(true);
 expect(report.exams.some((set:any)=>set.code.startsWith('MINI-15-18-'))).toBe(true);
 for(const exam of report.exams){expect(exam.items.length,exam.code).toBeGreaterThan(0);expect(new Set(exam.items.map((q:any)=>q.id)).size,exam.code).toBe(exam.items.length);for(const item of exam.items){expect(item.prompt.trim(),exam.code).not.toBe('');if(item.options?.length){expect(item.correct,`${exam.code} ${item.id}`).toBeGreaterThanOrEqual(0);expect(item.correct).toBeLessThan(item.options.length);}}}
});
