"""Originals batch 23: CloudBurst on Francis Harris Lane. The Guadalupe and Hays cards are one project."""
import json
G, H = "Guadalupe County Technology Center", "CloudBurst San Marcos Gigacenter"
SRC = [["Data Center Dynamics: 706-acre CloudBurst campus approved (Apr 2026)", "https://www.datacenterdynamics.com/en/news/706-acre-data-center-approved-for-development-outside-san-antonio-texas/"],
       ["Seguin Gazette: split vote approves abatements and development agreement", "https://seguingazette.com/alert/guadalupe-county-oks-data-center-tax-abatements-development-agreement/article_145b1c67-afbd-4fca-ab70-197665e8fad3.html"],
       ["Community Impact: lawsuit against Guadalupe County (July 2026)", "https://communityimpact.com/san-marcos-buda-kyle/government/guadalupe-county-sued-over-data-center-development-agreements/"],
       ["San Marcos Record: suit alleges Open Meetings violations and a conflict of interest", "https://www.sanmarcosrecord.com/news/article_1e543d19-d3a3-41d3-89cb-fb8ae20c8d5b.html"],
       ["Texas Standard: Hays County residents and the gas power plant", "https://texasstandard.org/stories/hays-county-data-center-cloudburst-natural-gas-power/"]]
p = "data/details.json"; d = json.load(open(p))
for k in (G, H):
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in SRC if x[1] not in have)
g = d[G]
g["loc"] = "2955 Francis Harris Lane, between Center Point Road, Francis Harris Lane and Huber Road, straddling the Guadalupe-Hays county line south of San Marcos (pin approximate)"
g["acres"] = "706 acres (grew from 96 acres bought in Feb 2025)"
g["llc"] = "CloudBurst Texas LLC (CloudBurst Data Centers, a Denver startup founded in 2022); gas supply deal with Energy Transfer"
g["incent"] = "$500M county property tax abatement (Chapter 312) and development agreement"
g["dates"] = "Feb 24, 2026: commissioners rejected the $500M abatement 3 to 2. Apr 21, 2026: they approved it 3 to 2, with the county judge in favor. A first 50 MW phase broke ground, due online late 2026. July 20, 2026: the Data Center Action Coalition and residents sued, alleging Open Meetings Act violations and a conflict of interest by the county judge"
d[H]["dates"] = "Same project as the Guadalupe County Technology Center card; see that card for the full record"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('{name:"Guadalupe County Technology Center", county:"Guadalupe", type:"data", status:"announced", lat:29.57, lng:-97.96,\n   dev:"Not identified", power:"1.2 GW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  '{name:"Guadalupe County Technology Center", county:"Guadalupe", type:"data", status:"construction", lat:29.79, lng:-97.88,\n   dev:"CloudBurst Data Centers (CloudBurst Texas LLC)", power:"1.2 GW from an on-site gas plant (behind the meter), with gas from Energy Transfer", water:"Not disclosed", conf:"Reporting", note:"A $14.5B, 10 to 12 building campus on 706 acres along the Hays County line. Commissioners rejected a $500M tax break 3 to 2 in Feb 2026, then approved it 3 to 2 two months later. Residents have sued over open meetings and a conflict of interest."'),
 ('dev:"CloudBurst", power:"1.2 GW listed", water:"Not disclosed", conf:"Reporting", note:"Near San Marcos, which banned data centers inside city limits in June 2026. Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"CloudBurst", power:"1.2 GW", water:"Not disclosed", conf:"Reporting", note:"The same project as the Guadalupe County Technology Center card: CloudBurst\'s campus at 2955 Francis Harris Lane straddles the Hays-Guadalupe line. It sits outside San Marcos, which banned data centers inside city limits in June 2026. See the Guadalupe card for the full record."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>CloudBurst: one project, two cards</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>"Guadalupe County Technology Center" and "CloudBurst San Marcos Gigacenter" are the same CloudBurst campus on Francis Harris Lane, which straddles the county line. We had the Guadalupe card with no developer, pinned near Seguin. Both cards now say they are one project, and the pin is moved to the site.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 23: CloudBurst checked; Guadalupe and Hays cards marked as one project")
