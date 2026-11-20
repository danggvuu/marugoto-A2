import { test, expect } from '@playwright/test';

test('malformed stored progress cannot crash dashboard', async ({page}) => {
 await page.addInitScript(() => localStorage.setItem('marugoto_astryx_progress_v1', '{"vocab":12,"kanji":null,"quizAttempts":"bad","lastLesson":"//evil.invalid"}'));
 await page.goto('/');
 await expect(page.getByRole('heading', {level:1})).toContainText('Học tiếng Nhật');
 await expect(page.getByText('0 từ đã học', {exact:true})).toBeVisible();
 await expect(page.getByRole('link').filter({has:page.getByRole('button',{name:'Tiếp tục học',exact:true})})).toHaveAttribute('href','/lessons/a2-1/1');
});

test('blocked storage retains usable in-memory learning progress', async ({page}) => {
 await page.addInitScript(() => { Storage.prototype.getItem = () => {throw new DOMException('blocked','SecurityError');}; Storage.prototype.setItem = () => {throw new DOMException('blocked','SecurityError');}; });
 await page.goto('/lessons/a2-2/1');
 await page.getByRole('button', {name:'Tiếp',exact:true}).click();
 await page.getByRole('link', {name:'Dashboard',exact:true}).click();
 await expect(page.getByText('1 từ đã học', {exact:true})).toBeVisible();
});
