// "What's changed lately" for a county page: <section id="changes" data-county="X">. The whole-state list: data-county="".
(() => {
  const el = document.getElementById('changes'); if (!el) return;
  const C = el.dataset.county || '', N = C ? 10 : 300;
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const fmt = d => new Date(d + 'T12:00:00').toLocaleDateString('en-US', {month:'short', day:'numeric', year:'numeric'});
  fetch('/carrizo_wilcox_aquifer/frontend/changes.json', {cache: 'no-store'}).then(r => r.json()).then(L => {
    const all = L.changes || [], mine = (C ? all.filter(c => (c.county || []).includes(C)) : all).slice(0, N);
    const row = c => `<li><span class="tag">${esc(fmt(c.date))}</span>${C ? '' : `<span class="tag">${esc((c.county || []).length ? c.county.join(', ') + ' County' : 'Statewide')}</span>`}<p>${c.link ? `<a href="${esc(c.link)}" rel="noopener">${esc(c.text)}</a>` : esc(c.text)}</p></li>`;
    el.innerHTML = `<h2>${C ? "What's changed lately" : 'Every change, newest first'}</h2>` +
      (mine.length ? `<ul class="rows">${mine.map(row).join('')}</ul>` : `<p>No changes logged${C ? ' for ' + esc(C) + ' County' : ''} since tracking began on ${esc(fmt(L.since))}.</p>`) +
      `<span class="src">Checked every night: new projects, status changes, ERCOT grid requests, records, hearing dates and state tax-break records.${C ? ' <a href="/updates">See every change statewide</a>.' : ''}</span>`;
  }).catch(() => { el.innerHTML = ''; });
})();
