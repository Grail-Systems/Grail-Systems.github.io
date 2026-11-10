// County Watch page built from Ground Truth Texas data. Settings: <main id="auto" data-county="X" data-live="1|0">
(() => {
  const root = document.getElementById('auto'); if (!root) return;
  const COUNTY = root.dataset.county, LIVE = root.dataset.live === '1';
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const cty = c => c.replace(/\s*\(.*\)\s*/, '').trim();
  const slug = n => n.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  const ST = {announced:'Announced or reported', filed:'Filed with a government', approved:'Approved by a government', construction:'Under construction', operating:'Operating', stopped:'Withdrawn or stopped'};
  const TY = {data:'Data center', crypto:'Crypto mine', power:'Power plant'};
  const fmtD = d => new Date(d + 'T12:00:00').toLocaleDateString('en-US', {month:'short', day:'numeric', year:'numeric'});
  const get = u => fetch(u).then(r => r.ok ? r.json() : Promise.reject(u));
  Promise.all([get('/data/projects.json'), get('/data/details.json').catch(() => ({})), get('/data/events.json').catch(() => []), get('/data/districts.json')])
  .then(([P, D, E, DIST]) => {
    const mine = P.filter(p => cty(p.county) === COUNTY).map(p => Object.assign({}, p, D[p.name] || {}));
    const names = new Set(mine.map(p => p.name));
    const today = new Date(); today.setHours(0, 0, 0, 0);
    const soon = E.filter(e => new Date(e.date + 'T12:00:00') >= today && e.projects.some(n => names.has(n)));
    const parse = v => (v || '').split(';').filter(x => x.trim()).map(x => { const m = x.trim().match(/^(\d+)\s*(.*)$/); return {d: m[1], who: m[2]}; });
    const H = parse(DIST.H[COUNTY]), S = parse(DIST.S[COUNTY]);
    const active = mine.filter(p => p.status !== 'stopped').length;
    let h = `<section><h2>At a glance</h2><div class="counts">
      <div><b>${mine.length}</b><span>project${mine.length === 1 ? '' : 's'} on the Texas map</span></div>
      <div><b>${active}</b><span>still active</span></div>
      <div><b>${soon.length}</b><span>upcoming date${soon.length === 1 ? '' : 's'}</span></div></div></section>`;
    h += `<section><h2>The projects</h2><ul class="rows">` + mine.map(p => {
      const links = (p.links || []).map(([t, u]) => `<a href="${esc(u)}" rel="noopener">${esc(t)}</a>`).join(' · ');
      const extra = [['State sales tax break (Comptroller record)', p.comp], ['Location', p.loc], ['Related companies', p.llc], ['Land', p.land], ['Incentives', p.incent], ['Key dates', p.dates]].filter(x => x[1]).map(([k, v]) => `<p><b>${k}:</b> ${esc(v)}</p>`).join('');
      return `<li><span class="tag">${ST[p.status] || esc(p.status)}</span><span class="tag">${TY[p.type] || ''}</span><span class="tag">${esc(p.conf)}</span>
        <h3><a href="/texas#${slug(p.name)}">${esc(p.name)}</a></h3>
        <p><b>Developer:</b> ${esc(p.dev)}. <b>Power:</b> ${esc(p.power)}. <b>Water:</b> ${esc(p.water)}.</p>${extra}<p>${esc(p.note)}</p>
        <span class="src">Sources: ${esc(p.src)}${links ? ' · ' + links : ''}</span></li>`;
    }).join('') + `</ul></section>`;
    if (soon.length) h += `<section><h2>Coming up</h2><ul class="rows">` + soon.map(e => `<li><span class="tag">${esc(fmtD(e.date))}${e.time ? ', ' + esc(e.time) : ''}</span><h3>${esc(e.what)}</h3><p>${esc(e.where || '')}</p></li>`).join('') + `</ul></section>`;
    h += `<section><h2>Your legislators</h2><ul class="rows">
      <li><h3>Texas House</h3><p>${H.length ? H.map(x => `District ${x.d}${x.who ? ', Rep. ' + esc(x.who) : ''}`).join('; ') : 'Not listed in the source table; check Who Represents Me.'}</p></li>
      <li><h3>Texas Senate</h3><p>${S.map(x => `District ${x.d}${x.who ? ', Sen. ' + esc(x.who) : ' (member not listed in the source table)'}`).join('; ')}</p></li></ul>
      <span class="src">Members of the 89th Legislature (2025); the Nov. 3, 2026 election may change seats. See <a href="/legislators">every district</a>.</span></section>`;
    if (!LIVE) h += `<section><h2>Live data</h2><p>${esc(COUNTY)} County is not yet in the Aquifer Defense Grid's nightly data feed (grid requests, state wells, EPA violations). <a href="mailto:contact@grailsystems.io?subject=Add%20${encodeURIComponent(COUNTY)}%20County%20to%20the%20nightly%20feed">Ask us to add it</a>.</p></section>`;
    root.innerHTML = h;
  }).catch(() => { root.innerHTML = '<section><p>This page could not load its data. Please try again in a minute.</p></section>'; });
})();
