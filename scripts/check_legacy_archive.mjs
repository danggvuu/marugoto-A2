import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';

// Usage: node scripts/check_legacy_archive.mjs [http://127.0.0.1:5173]
const root = path.resolve('legacy_html');
const entries = fs.readdirSync(root, { recursive: true })
  .filter(file => fs.statSync(path.join(root, file)).isFile());
const pages = entries.filter(file => file.endsWith('.html'));
assert.equal(pages.length, 59, 'The archive must contain all 59 original HTML pages');
assert.equal(pages.filter(file => file.startsWith('lessons/')).length, 36);
assert.equal(pages.filter(file => file.startsWith('tests/')).length, 11);

const references = new Set();
for (const file of pages) {
  const html = fs.readFileSync(path.join(root, file), 'utf8');
  assert.ok(!html.includes('/src/main.tsx'), `${file} must not be a SPA wrapper`);
  for (const match of html.matchAll(/(?:src|href|poster|data-src)\s*=\s*["']([^"']+)["']/gi)) {
    const ref = match[1];
    if (/^(?:[a-z]+:|\/\/|#)/i.test(ref)) continue;
    const clean = decodeURIComponent(ref.split(/[?#]/)[0]);
    if (!clean) continue;
    const resolved = path.resolve(root, path.dirname(file), clean);
    assert.ok(resolved.startsWith(`${root}${path.sep}`), `${file} escapes archive: ${ref}`);
    assert.ok(fs.existsSync(resolved), `${file} has missing local resource: ${ref}`);
    references.add(path.relative(root, resolved));
  }
}

const base = process.argv[2];
if (base) {
  // Compare every byte to catch SPA fallbacks even when they incorrectly return HTTP 200.
  for (const file of entries) {
    const url = `${base.replace(/\/$/, '')}/legacy_html/${file.split(path.sep).map(encodeURIComponent).join('/')}`;
    const response = await fetch(url);
    assert.equal(response.status, 200, `${url} must return HTTP 200`);
    const actual = Buffer.from(await response.arrayBuffer());
    const expected = fs.readFileSync(path.join(root, file));
    assert.ok(actual.equals(expected), `${url} is not the original archived file`);
  }
  console.log(`HTTP verification passed: ${entries.length} archived files served byte-for-byte from ${base}`);
}
console.log(`Archive checks passed: ${pages.length} HTML pages, ${references.size} distinct local links/resources, ${entries.length} total files.`);
