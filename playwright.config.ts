import { defineConfig } from '@playwright/test';
export default defineConfig({
 testDir: './tests/spa',
 timeout: 30_000,
 fullyParallel: false,
 workers: 1,
 use: { baseURL: 'http://127.0.0.1:5178', browserName: 'chromium', channel: 'chrome', viewport: { width: 1440, height: 1000 }, screenshot: 'only-on-failure', trace: 'retain-on-failure' },
 webServer: { command: 'npm run dev -- --port 5178 --strictPort', url: 'http://127.0.0.1:5178', reuseExistingServer: !process.env.CI },
});
