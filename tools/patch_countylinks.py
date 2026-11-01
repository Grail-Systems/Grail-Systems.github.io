p = "texas.html"; s = open(p).read()
if "county_pages.json" in s:
    print("already patched"); raise SystemExit
def rep(old, new):
    global s
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
rep('Tell us if you know of one.</p>', 'Tell us if you know of one. <a href="/counties">See a County Watch page for every county on the map.</a></p>')
rep('goToHash();\n\nPromise.all([fetch("/data/details.json")', '''goToHash();
fetch("/data/county_pages.json").then(r => r.json()).then(C => {
  projects.forEach(p => { if (!p.link) { const u = C[p.county.replace(/\\s*\\(.*\\)\\s*/, "").trim()]; if (u) p.link = u; } });
  markers.forEach((m, i) => m.setPopupContent(popupHTML(projects[i]))); render();
}).catch(() => {});

Promise.all([fetch("/data/details.json")''')
open(p, "w").write(s); print("map cards now link to every county page")
