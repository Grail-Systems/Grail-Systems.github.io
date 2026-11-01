p = "companies.html"; s = open(p).read()
if "PROJ" in s:
    print("already patched"); raise SystemExit
def rep(old, new):
    global s
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
rep('const extra = c => { const r = REC[c.name]; return r ? block("Who runs it", r.people) + block("Track record", r.record) : ""; };',
r'''let PROJ = [];
const ALIAS = {"AmpZ / EPG Champion":["AmpZ","Amp Z"],"WattBridge":["WattBridge","Longleaf Generating"],"1606 Corp":["Aspen Power","1606"],
 "MARA Holdings":["MARA"],"Riot Platforms":["Riot"],"Galaxy Digital":["Galaxy"],"Vantage Data Centers":["Vantage"],
 "Crusoe / Oracle / OpenAI (Stargate)":["Stargate"],"Compass Datacenters":["Compass"],"Fermi America":["Fermi"],"Diode Ventures":["Diode"],
 "RCM Hill LLC":["RCM Hill"],"Stream Data Centers":["Stream Data","Saltworks"],"QTS and Lancium":["QTS"],"Amazon":["Amazon","AWS"],
 "Sailfish Development":["Sailfish","Comanche Circle"],"Bilateral Energy":["Bilateral","Project Patriot"],"Big Digital Energy / 10NetZero":["Big Digital","10NetZero"],
 "NextEra Energy":["NextEra"],"Cipher Digital":["Cipher"],"Black Mountain Power":["Black Mountain"],"Pacifico Energy":["Pacifico","GW Ranch"]};
const pslug = n => n.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const rx = a => new RegExp("(^|[^A-Za-z0-9])" + a.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "([^A-Za-z0-9]|$)");
const projectsOf = c => { const keys = (ALIAS[c.name] || [c.name]).map(rx); return PROJ.filter(p => keys.some(k => k.test(p.dev + " | " + p.name))); };
const extra = c => { const r = REC[c.name], ps = projectsOf(c);
  const pl = ps.length ? `<p><b>Projects on the Texas map (${ps.length})</b></p><ul style="margin:4px 0 8px;padding-left:1.1rem">` +
    ps.map(p => `<li style="border:0;padding:2px 0"><a href="/texas#${pslug(p.name)}">${esc(p.name)}</a> <span class="src" style="display:inline">(${esc(p.county)} County)</span></li>`).join("") + `</ul>` : "";
  return pl + (r ? block("Who runs it", r.people) + block("Track record", r.record) : ""); };''')
rep('fetch("/data/company_records.json").then(r => r.json()).then(d => { REC = d; render(); }).catch(() => {});',
    'fetch("/data/company_records.json").then(r => r.json()).then(d => { REC = d; render(); }).catch(() => {});\nfetch("/data/projects.json").then(r => r.json()).then(d => { PROJ = d; render(); }).catch(() => {});')
open(p, "w").write(s); print("companies now list their projects")
