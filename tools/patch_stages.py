import re
p = "texas.html"; s = open(p).read()
if '"filed"' in s and "Filed with a government" in s:
    print("already patched"); raise SystemExit
APPROVED = {"Longleaf Generating", "Amazon near Comanche Peak", "Comanche Circle", "Project Patriot", "Black Mountain Power, Fort Worth"}
FILED = {"Amp Z / Project Lufkin", "HyperDataGrid", "Longleaf II Power Station", "Sun Angel ESS", "Prosper / FM 1385 data center", "PowerHouse Westlake", "Project Red and Project Yellow"}
cnt = {"announced": 0, "filed": 0, "approved": 0}
def fix(m):
    name = m.group(1); new = "approved" if name in APPROVED else "filed" if name in FILED else "announced"
    cnt[new] += 1; return m.group(0).replace('status:"proposed"', f'status:"{new}"')
s = re.sub(r'\{name:"([^"]+)"[^\n]*?status:"proposed"', fix, s)
def rep(old, new):
    global s
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
rep('const colors = {proposed:v("--alarm"), construction:v("--brass"), operating:v("--muted"), stopped:"#4cc27a"};',
    'const colors = {announced:"#e8794a", filed:v("--alarm"), approved:"#8b3fa8", construction:v("--brass"), operating:v("--muted"), stopped:"#4cc27a"};')
rep('const statusText = {proposed:"Proposed or under review", construction:"Under construction", operating:"Operating", stopped:"Withdrawn or stopped"};',
    'const statusText = {announced:"Announced or reported", filed:"Filed with a government", approved:"Approved by a government", construction:"Under construction", operating:"Operating", stopped:"Withdrawn or stopped"};')
rep('      <option value="proposed">Proposed or under review</option>\n',
    '      <option value="announced">Announced or reported</option>\n      <option value="filed">Filed with a government</option>\n      <option value="approved">Approved by a government</option>\n')
rep('  <div class="legend" id="legend"></div>',
    '  <div class="legend" id="legend"></div>\n  <p style="font-size:.85rem;color:var(--muted);margin:6px 0 0">"Announced or reported" means we have not yet found an application, permit or rezoning on file. Tell us if you know of one.</p>')
rep('function extraHTML(p) {', '''const srcLinks = (p, br) => {
  const L = (p.links || []).map(([t, u]) => `<a href="${u}" rel="noopener">${esc(t)}</a>`);
  L.push(`<a href="https://news.google.com/search?q=${encodeURIComponent('"' + p.name.replace(/\\s*\\(.*?\\)/g, "") + '" Texas')}" rel="noopener">search the news</a>`);
  return (br ? "<b>Read the sources:</b> " : "<p><b>Read the sources:</b> ") + L.join(" · ") + (br ? "<br><br>" : "</p>");
};
function extraHTML(p) {''')
rep('''    extraFields(p).map(([k, v]) => `<p><b>${k}:</b> ${esc(v)}</p>`).join("");
}''', '''    extraFields(p).map(([k, v]) => `<p><b>${k}:</b> ${esc(v)}</p>`).join("") + srcLinks(p, false);
}''')
rep('''"<b>Sources:</b> " + esc(p.src) + "<br><br>" : ""}` +''', '''"<b>Sources:</b> " + esc(p.src) + "<br><br>" : ""}` + srcLinks(p, true) +''')
open(p, "w").write(s); print("statuses:", cnt)
