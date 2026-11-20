import { test, expect } from '@playwright/test';

test('exam grading, review, best score and retry use repository answers', async ({page}) => {
 await page.goto('/tests');
 const sets = await page.evaluate(async () => { const module = await import(/* @vite-ignore */ '/src/services/dataLoader.ts'); return module.examSets; });
 const exam = sets[0];
 await page.getByRole('button', {name: `${exam.code} · ${exam.name}`, exact:true}).click();
 const articles = page.locator('main article');
 const items = exam.sections.flatMap((section:any) => section.groups.flatMap((group:any) => group.items));
 await expect(articles).toHaveCount(items.length);
 for(let index=0;index<items.length;index++) {
  const item=items[index];
  if(item.options?.length && Number.isInteger(item.correct)) await articles.nth(index).getByRole('radio').nth(item.correct).check();
 }
 await page.getByRole('button',{name:'Nộp bài',exact:true}).click();
 await expect(page.getByText('100%',{exact:true})).toBeVisible();
 await expect(page.getByText(/100% · Đã nộp/)).toBeVisible();
 await expect(page.getByRole('radio').first()).toBeDisabled();
 await page.getByRole('button',{name:'Làm lại đề',exact:true}).click();
 await expect(page.getByRole('radio').first()).not.toBeChecked();
 await expect(page.getByRole('radio').first()).toBeEnabled();
 await page.getByRole('button',{name:'Chọn bộ đề khác',exact:true}).click();
 await expect(page.getByRole('heading',{name:'Chọn một mã đề',exact:true})).toBeVisible();
});

test('exam deadline automatically submits when browser time advances', async ({page}) => {
 await page.clock.install();
 await page.goto('/tests');
 const exam = await page.evaluate(async () => { const module = await import(/* @vite-ignore */ '/src/services/dataLoader.ts'); return module.examSets[0]; });
 await page.getByRole('button',{name:`${exam.code} · ${exam.name}`,exact:true}).click();
 await page.clock.fastForward(exam.timeLimit*60*1000+1000);
 await expect(page.getByText(/0% · Đã nộp/)).toBeVisible();
 await expect(page.getByRole('radio').first()).toBeDisabled();
});
