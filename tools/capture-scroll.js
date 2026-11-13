#!/usr/bin/env node
// Record scroll-linked motion: steps down the page and samples every element that can animate.
// Usage: node tools/capture-scroll.js <url> <out-dir> [--step 120] [--width 1440] [--height 900]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const [url, outDir, ...rest] = process.argv.slice(2);
if (!url || !outDir) { console.error('usage: node tools/capture-scroll.js <url> <out-dir> [--step N]'); process.exit(1); }
const opt = (k, d) => { const i = rest.indexOf('--' + k); return i >= 0 ? Number(rest[i + 1]) : d; };
const step = opt('step', 120), width = opt('width', 1440), height = opt('height', 900);

(async () => {
  fs.mkdirSync(path.join(outDir, 'frames'), { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width, height } });

  // Record every IntersectionObserver (options + what it watches) and scroll/wheel listeners before page scripts run.
  await page.addInitScript(() => {
    window.__io = [];
    const IO = window.IntersectionObserver;
    window.IntersectionObserver = class extends IO {
      constructor(cb, o = {}) {
        super(cb, o);
        this.__rec = { threshold: o.threshold ?? 0, rootMargin: o.rootMargin ?? '0px', targets: [] };
        window.__io.push(this.__rec);
      }
      observe(el) { this.__rec.targets.push(el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '')); return super.observe(el); }
    };
    window.__listeners = {};
    const add = EventTarget.prototype.addEventListener;
    EventTarget.prototype.addEventListener = function (t, ...a) {
      if (['scroll', 'wheel', 'touchmove', 'pointermove', 'mousemove'].includes(t)) window.__listeners[t] = (window.__listeners[t] || 0) + 1;
      return add.call(this, t, ...a);
    };
  });

  await page.goto(url, { waitUntil: 'networkidle', timeout: 45000 }).catch(() => {});
  await page.waitForTimeout(3000); // let entrance animations finish before sampling

  const env = await page.evaluate(() => {
    const rules = [];
    for (const sh of document.styleSheets) { try { for (const r of sh.cssRules) if (/animation-timeline|scroll-timeline|view-timeline|scroll-snap|position:\s*sticky|background-attachment:\s*fixed/.test(r.cssText)) rules.push(r.cssText.slice(0, 400)); } catch (e) {} }
    return {
      docHeight: document.documentElement.scrollHeight,
      scrollTimelineCss: rules.slice(0, 30),
      libs: { gsap: !!window.gsap, ScrollTrigger: !!window.ScrollTrigger, Lenis: !!window.Lenis, lenis: !!window.lenis, locomotive: !!window.LocomotiveScroll, three: !!window.THREE, framer: !!document.querySelector('[data-framer-name]'), nextjs: !!window.__NEXT_DATA__ || !!window.next },
      htmlClasses: document.documentElement.className,
      smoothScrollCss: getComputedStyle(document.documentElement).scrollBehavior,
      canvases: [...document.querySelectorAll('canvas')].map(c => ({ cls: c.className, w: c.width, h: c.height, fixed: getComputedStyle(c.parentElement).position })),
    };
  });

  // Elements worth tracking: anything with transform/opacity/filter/transition/animation/sticky/fixed, plus images and canvases.
  const handles = await page.evaluateHandle(() => {
    const out = [];
    for (const e of document.querySelectorAll('body *')) {
      const s = getComputedStyle(e), r = e.getBoundingClientRect();
      if (r.width < 24 || r.height < 12) continue;
      const interesting = s.transform !== 'none' || s.opacity !== '1' || s.filter !== 'none' || s.position === 'sticky' || s.position === 'fixed' ||
        s.transitionProperty.match(/transform|opacity|filter|clip-path/) || s.animationName !== 'none' || ['CANVAS', 'IMG', 'VIDEO', 'SVG'].includes(e.tagName.toUpperCase()) || s.willChange !== 'auto';
      if (interesting) out.push(e);
      if (out.length >= 160) break;
    }
    return out;
  });
  const count = await page.evaluate(h => h.length, handles);

  const sample = (els) => els.map((e) => {
    const s = getComputedStyle(e), r = e.getBoundingClientRect();
    return { top: Math.round(r.top), h: Math.round(r.height), tf: s.transform === 'none' ? '' : s.transform.replace(/\s+/g, ''), op: +(+s.opacity).toFixed(3), fl: s.filter === 'none' ? '' : s.filter, cp: s.clipPath === 'none' ? '' : s.clipPath.slice(0, 60), pos: s.position };
  });
  const meta = await page.evaluate((els) => els.map((e) => {
    const c = typeof e.className === 'string' ? e.className.trim().split(/\s+/).slice(0, 3).join('.') : '';
    const s = getComputedStyle(e);
    return { sel: e.tagName.toLowerCase() + (c ? '.' + c : ''), text: (e.textContent || '').trim().slice(0, 30), transition: s.transitionProperty + ' ' + s.transitionDuration + ' ' + s.transitionTimingFunction, willChange: s.willChange, anim: s.animationName };
  }), handles);

  const frames = [];
  const max = env.docHeight - height;
  let n = 0;
  for (let y = 0; y <= max; y += step) {
    await page.mouse.wheel(0, y === 0 ? 0 : step); // real wheel events so scroll-linked JS runs
    await page.waitForTimeout(160);
    const actual = await page.evaluate(() => Math.round(scrollY));
    const state = await page.evaluate(sample, handles).catch(() => null);
    frames.push({ y: actual, state });
    if (n % 5 === 0) await page.screenshot({ path: path.join(outDir, 'frames', `y${String(actual).padStart(5, '0')}.png`) });
    n++;
  }

  const io = await page.evaluate(() => ({ observers: window.__io, listeners: window.__listeners }));

  // Per element: which properties changed across the scroll, and where.
  const changes = meta.map((m, i) => {
    const series = frames.map(f => ({ y: f.y, ...(f.state && f.state[i]) }));
    const first = (k) => new Set(series.map(s => s[k]));
    const vary = ['tf', 'op', 'fl', 'cp'].filter(k => first(k).size > 1);
    // viewport-relative top changes at exactly -step per step means plain scroll; anything else is parallax/sticky
    let drift = 0;
    for (let j = 1; j < series.length; j++) { const d = (series[j - 1].top - series[j].top) - (series[j].y - series[j - 1].y); if (Math.abs(d) > 2) drift++; }
    return { ...m, varies: vary, parallaxOrStickySteps: drift, samples: vary.length || drift ? series.filter((_, j) => j % 2 === 0).map(s => ({ y: s.y, top: s.top, tf: s.tf, op: s.op, fl: s.fl, cp: s.cp })) : undefined };
  }).filter(c => c.varies.length || c.parallaxOrStickySteps);

  const out = { url, capturedAt: new Date().toISOString(), viewport: { width, height }, step, env, ...io, tracked: count, animatedOnScroll: changes };
  fs.writeFileSync(path.join(outDir, 'scroll.json'), JSON.stringify(out, null, 2));
  await browser.close();
  console.log(`scroll capture: ${frames.length} frames, ${changes.length} elements change on scroll -> ${outDir}`);
})().catch(e => { console.error('scroll capture failed:', e.message); process.exit(1); });
