#!/usr/bin/env node
// Capture a live site with Playwright/Chromium: computed styles, fonts, motion and a screenshot.
// Usage: node tools/capture.js <url> <out-dir> [--width 1440] [--height 900]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const [url, outDir, ...rest] = process.argv.slice(2);
if (!url || !outDir) {
  console.error('usage: node tools/capture.js <url> <out-dir> [--width N] [--height N]');
  process.exit(1);
}
const opt = (k, d) => { const i = rest.indexOf('--' + k); return i >= 0 ? Number(rest[i + 1]) : d; };
const width = opt('width', 1440), height = opt('height', 900);

(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width, height } });
  await page.goto(url, { waitUntil: 'networkidle', timeout: 45000 }).catch(() => {});
  await page.waitForTimeout(1500);
  // scroll through once so lazy content and scroll-triggered motion run
  await page.evaluate(async () => {
    for (let y = 0; y < document.body.scrollHeight; y += innerHeight) {
      scrollTo(0, y); await new Promise(r => setTimeout(r, 250));
    }
    scrollTo(0, 0);
  });

  const data = await page.evaluate(() => {
    const count = (arr) => Object.entries(arr.reduce((m, v) => (v && (m[v] = (m[v] || 0) + 1), m), {}))
      .sort((a, b) => b[1] - a[1]).slice(0, 15);
    const els = [...document.querySelectorAll('body *')].slice(0, 4000);
    const cs = els.map(e => getComputedStyle(e));
    const pick = (p) => count(cs.map(s => s[p]));
    const fonts = [...document.fonts].map(f => ({ family: f.family, weight: f.weight, style: f.style, status: f.status }));
    const keyframes = [];
    for (const sheet of document.styleSheets) {
      try { for (const r of sheet.cssRules) if (r.type === CSSRule.KEYFRAMES_RULE) keyframes.push(r.cssText.slice(0, 600)); } catch (e) {}
    }
    const headings = ['h1', 'h2', 'h3', 'p', 'a', 'button'].map(t => {
      const e = document.querySelector(t); if (!e) return null; const s = getComputedStyle(e);
      return { tag: t, font: s.fontFamily, size: s.fontSize, weight: s.fontWeight, lh: s.lineHeight, ls: s.letterSpacing, color: s.color, text: e.textContent.trim().slice(0, 60) };
    }).filter(Boolean);
    return {
      title: document.title,
      colors: pick('color'), backgrounds: pick('backgroundColor'), borders: pick('borderTopColor'),
      fontFamilies: pick('fontFamily'), fontSizes: pick('fontSize'), radii: pick('borderTopLeftRadius'),
      shadows: pick('boxShadow'), filters: pick('backdropFilter'), transitions: pick('transitionProperty').concat(pick('transitionDuration'), pick('transitionTimingFunction')),
      animations: count(cs.map(s => s.animationName !== 'none' ? `${s.animationName} ${s.animationDuration} ${s.animationTimingFunction}` : null)),
      keyframes, fonts, headings,
      cssVars: [...document.styleSheets].flatMap(sh => { try { return [...sh.cssRules].flatMap(r => r.style ? [...r.style].filter(n => n.startsWith('--')).map(n => `${n}: ${r.style.getPropertyValue(n).trim()}`) : []); } catch (e) { return []; } }).slice(0, 200),
    };
  });

  fs.writeFileSync(path.join(outDir, 'capture.json'), JSON.stringify({ url, capturedAt: new Date().toISOString(), viewport: { width, height }, ...data }, null, 2));
  await page.screenshot({ path: path.join(outDir, 'viewport.png') });
  await page.screenshot({ path: path.join(outDir, 'full.png'), fullPage: true }).catch(() => {});
  await browser.close();
  console.log(`captured ${url} -> ${outDir}`);
})().catch(e => { console.error('capture failed:', e.message); process.exit(1); });
