#!/usr/bin/env node
// Traverse a whole site with Playwright: discover every same-origin page (breadth first), then
// capture each one (computed styles, fonts, motion, screenshot) and write site-map.json.
// Usage: node tools/crawl.js <start-url> <out-dir> [--max 60] [--skip <regex>] [--delay 3000]
// Respects robots.txt, reuses one browser context, paces requests, and stops if a bot challenge appears.
const { chromium } = require('playwright');
const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const [start, outDir, ...rest] = process.argv.slice(2);
if (!start || !outDir) { console.error('usage: node tools/crawl.js <start-url> <out-dir> [--max N] [--skip regex]'); process.exit(1); }
const arg = (k, d) => { const i = rest.indexOf('--' + k); return i >= 0 ? rest[i + 1] : d; };
const max = Number(arg('max', 60));
const skip = arg('skip') ? new RegExp(arg('skip')) : null;
const origin = new URL(start).origin;
const delay = Number(arg('delay', 3000));
let disallow = [];  // robots.txt `User-agent: *` Disallow rules; the crawl never visits these paths
const allowed = (u) => !disallow.some(d => d && new URL(u).pathname.startsWith(d));
const norm = (u) => { const x = new URL(u); x.hash = ''; return x.origin === origin ? x.origin + x.pathname.replace(/\/$/, '') + x.search : null; };
const slug = (u) => (new URL(u).pathname.replace(/^\/|\/$/g, '').replace(/\//g, '__') || 'home') + (new URL(u).search ? '--' + new URL(u).search.replace(/\W+/g, '-').slice(1) : '');

(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  try {
    const txt = await (await fetch(origin + '/robots.txt')).text();
    let star = false;
    for (const line of txt.split('\n')) {
      const m = line.match(/^\s*([A-Za-z-]+)\s*:\s*(.*?)\s*$/); if (!m) continue;
      if (/user-agent/i.test(m[1])) star = m[2] === '*';
      else if (star && /disallow/i.test(m[1])) disallow.push(m[2]);
    }
    console.log('robots.txt disallows:', disallow.join(' ') || '(none)');
  } catch (e) { console.log('no robots.txt'); }
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } }); // one context so static assets are cached between pages
  let challenged = false;
  const queue = [norm(start)], seen = new Set(queue), pages = [];
  while (queue.length && pages.length < max) {
    const url = queue.shift();
    const page = await ctx.newPage();
    page.on('response', r => { if (r.headers()['x-vercel-mitigated'] === 'challenge' || (r.status() === 429 && r.request().resourceType() !== 'document')) challenged = true; });
    let status = null;
    try {
      const r = await page.goto(url, { waitUntil: 'networkidle', timeout: 45000 }).catch(() => page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 }));
      status = r && r.status();
      await page.waitForTimeout(1200);
      const info = await page.evaluate(() => ({
        title: document.title, h1: (document.querySelector('h1') || {}).textContent?.trim().slice(0, 120) || '', height: document.documentElement.scrollHeight,
        links: [...document.querySelectorAll('a[href]')].map(a => a.href), external: [],
      }));
      const out = { url, slug: slug(url), status, title: info.title, h1: info.h1, height: info.height, linkCount: info.links.length };
      for (const l of info.links) {
        let n = null; try { n = norm(l); } catch (e) {}
        if (n && !seen.has(n) && allowed(n) && !(skip && skip.test(n)) && !/\.(pdf|zip|dmg|png|jpe?g|svg|webp|mp4)$/i.test(n)) { seen.add(n); queue.push(n); }
        else if (!n) { try { const o = new URL(l); if (/^https?:/.test(o.protocol)) out.external = [...new Set([...(out.external || []), o.origin + o.pathname])]; } catch (e) {} }
      }
      pages.push(out);
      console.log(`[${pages.length}] ${status} ${url} (${info.height}px) queue=${queue.length}`);
    } catch (e) { pages.push({ url, slug: slug(url), error: e.message }); console.log('ERR', url, e.message); }
    await page.close();
    if (challenged) { console.log('STOP: the site is serving a bot challenge / 429 for assets. Not retrying or working around it; pages captured so far are unstyled.'); break; }
    await new Promise(r => setTimeout(r, delay));
  }
  await browser.close();

  if (challenged) { fs.writeFileSync(path.join(outDir, 'site-map.json'), JSON.stringify({ start, blocked: true, pages, unvisited: queue }, null, 2)); process.exit(2); }
  for (const p of pages) {
    if (p.error) continue;
    const dir = path.join(outDir, p.slug);
    const args = ['tools/capture.js', p.url, dir, '--nofull'];
    spawnSync('node', args, { stdio: 'inherit' });
  }
  fs.writeFileSync(path.join(outDir, 'site-map.json'), JSON.stringify({ start, crawledAt: new Date().toISOString(), pages, unvisited: queue }, null, 2));
  console.log(`crawled ${pages.length} pages, ${queue.length} left in queue -> ${outDir}/site-map.json`);
})();
