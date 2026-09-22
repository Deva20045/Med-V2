#!/usr/bin/env python3
"""Optional real-Chromium offline smoke test (pip install playwright).

Use Playwright's installed Chromium, or set CHROMIUM_EXECUTABLE to a local binary.
No HTTP service, network access or app runtime dependencies are required.
"""
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
with sync_playwright() as p:
    launch = dict(headless=True, args=['--no-sandbox', '--disable-dev-shm-usage', '--no-zygote', '--single-process'])
    if os.environ.get('CHROMIUM_EXECUTABLE'):
        launch['executable_path'] = os.environ['CHROMIUM_EXECUTABLE']
    for width, height in [(1280, 900), (390, 844)]:
        browser = p.chromium.launch(**launch)
        context = browser.new_context(viewport={'width': width, 'height': height}, offline=True)
        page = context.new_page()
        errors = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto((ROOT / 'index.html').as_uri())
        page.wait_for_url('**/pulse-medicine.html')
        result = page.evaluate('''() => {
          const check = (ok, message) => {if (!ok) throw new Error(message);};
          localStorage.clear(); render();
          check(CHAPTERS.length === 57, '57-chapter roadmap');
          check(CHAPTERS.filter(c => c.live).map(c => c.n).join(',') === '1,2,3,4', 'live chapters');
          show('chapters');
          check(document.querySelectorAll('.chrow').length === 57, 'roadmap DOM');
          check(document.querySelectorAll('.chrow:not(.locked)').length === 4, 'live roadmap DOM');
          let count = 0;
          for (const u of UNITS) {
            curCh = u.ch;
            const us = unitsOf(u.ch);
            check(unitState(u, us) === 'current', u.id + ': sequential unlock');
            openGuide(u); beginUnit();
            check(order.map(o => o.q.id).join(',') === u.qs.join(','), u.id + ': fixed book order');
            for (const id of u.qs) {
              const q = order[idx].q;
              check(q.id === id, id + ': current id');
              check($('opts').children.length === 4, id + ': option buttons');
              if (q.fmt === 'match') {
                check(!$('qboard').classList.contains('hidden'), id + ': match board');
                check($('opts').querySelectorAll('.mpair').length > 0, id + ': match options');
              }
              if (q.fmt === 'fillup') check($('qtext').querySelector('.blank'), id + ': visible blank');
              const correctIndex = order[idx].opts.findIndex(o => o.ok);
              $('opts').children[correctIndex].click();
              check($('fb').classList.contains('good'), id + ': correct answer feedback');
              check($('fb').textContent.includes('BOOK P' + q.page), id + ': book citation');
              $('nextBtn').click(); count++;
            }
            check(S.done.includes(u.id), u.id + ': completion persisted');
            check($('dAcc').textContent === '100%', u.id + ': completion score');
          }
          check(S.done.length === UNITS.length, 'all units completed');
          // Wrong-answer feedback and review exercise a distinct path.
          openGuide(UNITS[UNITS.length - 1]); beginUnit();
          $('opts').children[order[0].opts.findIndex(o => !o.ok)].click();
          check($('fb').classList.contains('bad') && wrongList.length === 1, 'wrong-answer path');
          check(document.documentElement.scrollWidth <= innerWidth + 1, 'viewport overflow');
          return {questions: count, units: UNITS.length, live: CHAPTERS.filter(c => c.live).length};
        }''')
        assert not errors, errors
        page.reload()
        assert page.evaluate('S.done.length') == result['units'], 'completion lost on reload'
        print(f'PASS offline Chromium {width}×{height}: {result}; answers, citations, formats, unlock, persistence, wrong-answer path')
        context.close()
        browser.close()
