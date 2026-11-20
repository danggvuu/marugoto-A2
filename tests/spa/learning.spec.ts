import { test, expect } from '@playwright/test';

test('dashboard mounts React and persists actual light/dark theme colors', async ({ page }) => {
 const errors: string[] = []; page.on('pageerror', error => errors.push(error.message));
 await page.goto('/');
 await expect(page.getByRole('heading', {level: 1})).toContainText('Học tiếng Nhật');
 await expect(page.getByRole('button', {name: 'Vào bài học', exact: true})).toHaveCount(36);
 const light = await page.locator('body').evaluate(e => getComputedStyle(e).backgroundColor);
 await page.getByRole('button', {name: 'Bật chế độ tối', exact: true}).click();
 await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark');
 const dark = await page.locator('body').evaluate(e => getComputedStyle(e).backgroundColor);
 expect(dark).not.toBe(light);
 await page.reload(); await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark');
 await page.screenshot({path: 'artifacts/dashboard-dark.png'});
 expect(errors).toEqual([]);
});

test('lesson flashcards flip, autoplay, speak Japanese and persist learned words', async ({ page }) => {
 await page.addInitScript(() => { Object.defineProperty(window.speechSynthesis, 'speak', {value: (utterance: SpeechSynthesisUtterance) => { (window as any).__speech = {lang: utterance.lang, text: utterance.text}; }}); });
 await page.goto('/lessons/a2-2/1');
 const card = page.getByRole('button', {name: /^Thẻ 1:/});
 await expect(card).toBeVisible(); await card.press('Enter');
 await expect(card).toHaveAttribute('aria-pressed', 'true');
 await page.getByRole('button', {name: 'Nghe', exact: true}).click();
 await expect.poll(() => page.evaluate(() => (window as any).__speech?.lang)).toBe('ja-JP');
 await page.getByRole('button', {name: 'Tiếp', exact: true}).click();
 await expect(page.getByRole('button', {name: /^Thẻ 2:/})).toBeVisible();
 await page.getByRole('button', {name: 'Tự động phát', exact: true}).click();
 await expect(page.getByRole('button', {name: /^Thẻ 2:/})).toHaveAttribute('aria-pressed', 'true');
 await expect(page.getByRole('button', {name: /^Thẻ 3:/})).toBeVisible({timeout: 6000});
 await page.getByRole('button', {name: 'Dừng tự động phát', exact: true}).click();
 await page.getByRole('link', {name: 'Dashboard', exact: true}).click();
 await expect(page.getByText(/2 từ đã học/)).toBeVisible();
});

test('lesson quiz reveals feedback and locks first choice, typing checks kana', async ({ page }) => {
 await page.goto('/lessons/a2-2/1');
 await page.getByRole('button', {name: 'Mini test', exact: true}).click();
 const options = page.locator('main button[aria-pressed]');
 await expect(options).toHaveCount(4); await options.first().click();
 await expect(options.first()).toBeDisabled();
 await expect(page.getByText(/Đúng rồi!|Chưa đúng\./)).toBeVisible();
 for(let question=1;question<15;question++) {
  await page.getByRole('button', {name: 'Câu tiếp', exact:true}).click();
  await page.locator('main button[aria-pressed]').first().click();
 }
 await page.getByRole('button', {name: 'Nộp bài', exact:true}).click();
 await expect(page.getByText('Hoàn thành', {exact:true})).toBeVisible();
 expect(await page.evaluate(() => JSON.parse(localStorage.getItem('marugoto_astryx_progress_v1') || '{}').quizAttempts)).toBe(1);
 await page.getByRole('button', {name:'Làm lại', exact:true}).click();
 await expect(page.locator('main button[aria-pressed]').first()).toBeEnabled();
 await page.getByRole('button', {name: 'Luyện gõ', exact: true}).click();
 await page.getByRole('textbox', {name: 'Đáp án kana hoặc kanji'}).fill('clearly incorrect');
 await page.getByRole('button', {name: 'Kiểm tra', exact: true}).click();
 await expect(page.getByText(/^Đáp án:/)).toBeVisible();
});

test('Kanji filters, real flashcards and canvas work', async ({ page }) => {
 await page.goto('/kanji');
 await expect(page.getByText('291 mục đang hiển thị')).toBeVisible();
 await page.getByRole('button', {name: 'A2-2', exact: true}).click();
 await expect(page.getByText('170 mục đang hiển thị')).toBeVisible();
 await page.getByRole('combobox', {name: 'Lọc bài'}).selectOption('1');
 await page.locator('main details summary').first().click();
 await expect(page.locator('main canvas').first()).toBeVisible();
 await page.getByRole('button', {name: 'Ôn flashcard Kanji', exact: true}).click();
 await expect(page.getByRole('button', {name: /^Thẻ 1:/})).toBeVisible();
});

test('Kaiwa loads source topics and five minute timer counts down', async ({ page }) => {
 await page.goto('/kaiwa');
 await expect(page.getByRole('heading', {level: 1})).toContainText('hội thoại');
 await expect(page.getByRole('timer')).toHaveText('5:00');
 await page.getByRole('button', {name: 'Bắt đầu 5 phút', exact: true}).click();
 await expect(page.getByRole('timer')).not.toHaveText('5:00');
 await page.getByRole('button', {name: 'Tạm dừng', exact: true}).click();
 await page.getByRole('button', {name: 'Đặt lại đồng hồ', exact: true}).click();
 await expect(page.getByRole('timer')).toHaveText('5:00');
 await page.getByRole('button', {name: 'Xem câu trả lời mẫu', exact: true}).first().click();
 await expect(page.getByRole('button', {name: 'Nghe câu trả lời', exact: true}).first()).toBeVisible();
});

test('mobile navigation opens, follows direct route and closes without horizontal overflow', async ({ page }) => {
 await page.setViewportSize({width: 390, height: 844});
 await page.goto('/');
 const menu = page.getByRole('button', {name: 'Mở điều hướng', exact: true});
 await expect(menu).toBeVisible(); await menu.click();
 await page.getByRole('link', {name: 'Trung tâm Kanji', exact: true}).click();
 await expect(page).toHaveURL(/\/kanji$/);
 await expect(page.getByRole('button', {name: 'Mở điều hướng', exact: true})).toBeVisible();
 expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
 await page.screenshot({path:'artifacts/kanji-mobile.png'});
});

test('all lesson deep links render without runtime errors', async ({ page }) => {
 test.setTimeout(120_000);
 const errors: string[] = []; page.on('pageerror', error => errors.push(error.message));
 for (const level of ['a2-1', 'a2-2']) for(let lesson=1;lesson<=18;lesson++) {
  await page.goto(`/lessons/${level}/${lesson}`);
  await expect(page.getByRole('heading', {level:1})).toContainText(`Bài ${lesson}:`);
  await expect(page.getByRole('button', {name: /^Thẻ 1:/})).toBeVisible();
 }
 expect(errors).toEqual([]);
});
