p = "texas.html"; s = open(p).read()
if "gridLayer" in s:
    print("already patched"); raise SystemExit
def rep(old, new):
    global s
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
rep('<span id="soonLabel">Hearing or deadline in the next 30 days</span></label>',
    '<span id="soonLabel">Hearing or deadline in the next 30 days</span></label>\n    <label style="display:flex;align-items:center;gap:6px;font-weight:600"><input type="checkbox" id="gridLayer"> <span id="gridLabel">Show ERCOT grid requests (nightly feed)</span></label>')
rep('Promise.all([fetch("/data/details.json")', r'''const gridLayer = L.layerGroup(); let gridLoaded = false;
const plainTxt = h => { const d = document.createElement("div"); d.innerHTML = String(h || "").replace(/<br\s*\/?>/gi, " "); return d.textContent.replace(/\s+/g, " ").trim(); };
document.getElementById("gridLayer").addEventListener("change", e => {
  if (!e.target.checked) { map.removeLayer(gridLayer); return; }
  gridLayer.addTo(map);
  if (gridLoaded) return; gridLoaded = true;
  Promise.all([fetch("/carrizo_wilcox_aquifer/frontend/mega_permits.json").then(r => r.json()),
               fetch("/carrizo_wilcox_aquifer/frontend/feed_status.json").then(r => r.json()).catch(() => ({}))]).then(([F, st]) => {
    const when = st.checked ? new Date(st.checked).toLocaleDateString("en-US", {month:"short", day:"numeric", year:"numeric"}) : "nightly";
    const rows = F.filter(x => /^ERCOT/.test(x.title));
    rows.forEach(x => { let c; try { c = JSON.parse(x.coordinates); } catch (_) { return; }
      L.circleMarker([c[1], c[0]], {radius:5, color:"#1f5f7a", weight:2, fillColor:"#ffffff", fillOpacity:.9}).addTo(gridLayer)
       .bindPopup(`<strong>${esc(x.title.replace(/^ERCOT grid request:\s*/, ""))}</strong><br>${esc(x.applicant)}<br><br>${esc(plainTxt(x.bottom_line))}<br><br><a href="${esc(x.source_url)}" rel="noopener">ERCOT source</a> · Nightly feed, checked ${esc(when)}`);
    });
    document.getElementById("gridLabel").textContent = `Show ERCOT grid requests (${rows.length} from the nightly feed; watched counties only, shown at county level)`;
  }).catch(() => { document.getElementById("gridLabel").textContent = "ERCOT grid requests could not load right now"; });
});

Promise.all([fetch("/data/details.json")''')
open(p, "w").write(s); print("map: nightly ERCOT layer added")
