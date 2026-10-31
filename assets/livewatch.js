// Live data block for county pages. Reads the Aquifer Defense Grid's nightly feeds.
(() => {
  const box = document.getElementById('live'); if (!box) return;
  const COUNTY = box.dataset.county, PLACES = (box.dataset.places || '').split('|').filter(Boolean), NOERCOT = box.dataset.noercot === '1';
  const GRID = '/carrizo_wilcox_aquifer/frontend/';
  const $ = id => document.getElementById(id);
  const plain = s => { const d = document.createElement('div'); d.innerHTML = String(s || '').replace(/<br\s*\/?>/gi, ' '); return d.textContent.replace(/\s+/g, ' ').trim(); };
  const inCounty = s => new RegExp('\\b' + COUNTY + ' County\\b', 'i').test(s) || PLACES.some(p => new RegExp('\\b' + p + '\\b').test(s));
  const get = f => fetch(GRID + f, {cache: 'no-cache'}).then(r => { if (!r.ok) throw new Error(f); return r.json(); });
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };
  const link = (href, text) => { const a = el('a', null, text); a.href = href; a.rel = 'noopener'; return a; };
  const EMPTY = 'Nothing on file yet. This county was added to the nightly data job on Oct 31, 2026.';
  const fail = (id, n) => { $(id).innerHTML = ''; $(id).appendChild(el('li', null, 'Couldn’t load this list right now. Try again in a minute.')); $(n).textContent = '–'; };
  box.innerHTML = `<h2>Live data</h2>
    <p>Updated every night from public state and federal records. Last checked <span id="lvChecked">…</span>.</p>
    <div class="counts"><div><b id="lvP">…</b><span>grid requests and big projects</span></div><div><b id="lvW">…</b><span>state-monitored wells</span></div><div><b id="lvE">…</b><span>EPA violations on file</span></div></div>
    <h3 style="margin-top:22px">Grid requests and big projects</h3><ul class="rows" id="lvPList"></ul>
    <h3 style="margin-top:22px">Groundwater levels</h3><p id="lvWSum"></p><ul class="rows" id="lvWList"></ul>
    <h3 style="margin-top:22px">EPA violations</h3><ul class="rows" id="lvEList"></ul>
    <span class="src">Sources: ERCOT, Texas Water Development Board, EPA ECHO. Pulled nightly by the <a href="/carrizo_wilcox_aquifer/">Aquifer Defense Grid</a>.</span>`;
  get('feed_status.json').then(d => { const x = new Date(d.checked); $('lvChecked').textContent = isNaN(x) ? d.checked : x.toLocaleDateString('en-US', {month: 'short', day: 'numeric', year: 'numeric'}); }).catch(() => $('lvChecked').textContent = 'nightly');
  get('mega_permits.json').then(list => {
    const rows = list.filter(x => inCounty(x.title + ' ' + x.applicant + ' ' + x.bottom_line)).sort((a, b) => (b.raw_volume || 0) - (a.raw_volume || 0));
    $('lvP').textContent = rows.length; const ul = $('lvPList'); ul.innerHTML = '';
    if (NOERCOT) ul.appendChild(el('li', null, COUNTY + ' County is outside the ERCOT grid, so ERCOT grid requests don’t apply here. Other big projects still show below when found.'));
    if (!rows.length && !NOERCOT) ul.appendChild(el('li', null, EMPTY));
    rows.forEach(x => {
      const li = el('li'); li.appendChild(el('span', 'tag', /ERCOT/.test(x.title) ? 'Grid request' : 'Project'));
      li.appendChild(el('h3', null, plain(x.title).replace(/^ERCOT grid request:\s*/, '')));
      const t = plain(x.bottom_line), p = el('p', null, t.slice(0, 320) + (t.length > 320 ? '…' : ''));
      if (x.source_url) { p.appendChild(document.createTextNode(' ')); p.appendChild(link(x.source_url, 'Source')); }
      li.appendChild(p); ul.appendChild(li);
    });
  }).catch(() => fail('lvPList', 'lvP'));
  get('usgs_telemetry.json').then(list => {
    const rows = list.filter(x => inCounty(x.title)).sort((a, b) => (b.drop_ft || 0) - (a.drop_ft || 0));
    $('lvW').textContent = rows.length; const ul = $('lvWList'); ul.innerHTML = '';
    if (rows.length) $('lvWSum').textContent = rows.filter(x => (x.drop_ft || 0) > 0).length + ' of ' + rows.length + ' have dropped since their first measurement. Records start in different years, so compare each well to itself. Not every well here draws from the Carrizo-Wilcox; in some counties they tap other aquifers, such as the Trinity or the Hueco Bolson.';
    else ul.appendChild(el('li', null, EMPTY));
    rows.slice(0, 12).forEach(x => {
      const li = el('li'), txt = plain(x.bottom_line), since = (txt.match(/since (\d{4})/) || [])[1], dft = x.drop_ft == null ? null : Math.round(x.drop_ft);
      li.appendChild(el('h3', null, 'State well ' + (x.state_well_number || '') + ': ' + (dft == null ? 'level on file' : dft > 0 ? 'down ' + dft + ' ft' : dft < 0 ? 'up ' + (-dft) + ' ft' : 'no change') + (since ? ' since ' + since : '')));
      const p = el('p', null, txt + ' '); if (x.source_url) p.appendChild(link(x.source_url, 'Source'));
      li.appendChild(p); ul.appendChild(li);
    });
    if (rows.length > 12) ul.appendChild(el('li', null, '…and ' + (rows.length - 12) + ' more on the Aquifer Defense Grid map.'));
  }).catch(() => fail('lvWList', 'lvW'));
  get('toxin_feed.json').then(list => {
    const rows = list.filter(x => inCounty(x.bottom_line) && /violation/i.test(x.status || '') && !/^no /i.test(x.status || '')).sort((a, b) => (b.severity || 0) - (a.severity || 0));
    $('lvE').textContent = rows.length; const ul = $('lvEList'); ul.innerHTML = '';
    if (!rows.length) ul.appendChild(el('li', null, 'No EPA violations on file for this county.'));
    rows.slice(0, 10).forEach(x => {
      const li = el('li'); li.appendChild(el('h3', null, plain(x.facility)));
      const p = el('p', null, plain(x.bottom_line) + ' '); if (x.source_url) p.appendChild(link(x.source_url, 'EPA record'));
      li.appendChild(p); ul.appendChild(li);
    });
    if (rows.length > 10) ul.appendChild(el('li', null, '…and ' + (rows.length - 10) + ' more on the Aquifer Defense Grid map.'));
  }).catch(() => fail('lvEList', 'lvE'));
})();
