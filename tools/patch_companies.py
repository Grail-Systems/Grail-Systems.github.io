p = "companies.html"; s = open(p).read()
if "company_records.json" in s:
    print("already patched"); raise SystemExit
def rep(old, new):
    global s
    assert s.count(old) == 1, "not found: " + old[:50]; s = s.replace(old, new)
rep('    <p>${esc(c.know)}</p></li>`).join("")',
    '    <p>${esc(c.know)}</p>${extra(c)}</li>`).join("")')
rep('function render() {', r'''let REC = {};
const block = (title, rows) => rows && rows.length ? `<p><b>${title}</b></p><ul style="margin:4px 0 8px;padding-left:1.1rem">` +
  rows.map(([t, src]) => `<li style="border:0;padding:2px 0">${esc(t)} <span class="src" style="display:inline">(${esc(src)})</span></li>`).join("") + `</ul>` : "";
const extra = c => { const r = REC[c.name]; return r ? block("Who runs it", r.people) + block("Track record", r.record) : ""; };
function render() {''')
rep('const shown = companies.filter(c => !q || [c.name, c.kind, c.entities, c.know, c.counties.join(" ")].join(" ").toLowerCase().includes(q));',
    'const shown = companies.filter(c => !q || [c.name, c.kind, c.entities, c.know, c.counties.join(" "), JSON.stringify(REC[c.name] || "")].join(" ").toLowerCase().includes(q));')
rep('document.getElementById("search").addEventListener("input", render);\nrender();',
    'document.getElementById("search").addEventListener("input", render);\nrender();\nfetch("/data/company_records.json").then(r => r.json()).then(d => { REC = d; render(); }).catch(() => {});')
rep('{name:"Diode Ventures", kind:"Data center developer", counties:["Henderson"]', '{name:"Diode Ventures", kind:"Data center developer", counties:["Henderson","Ellis"]')
open(p, "w").write(s); print("companies page patched")
