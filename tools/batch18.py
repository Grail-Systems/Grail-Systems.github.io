"""Originals batch 18: KDC Project Comal (Taylor). Status approved; map pin moved to Taylor."""
import json
K = "KDC Project Comal"
L = [["City of Taylor: KDC Project Comal page and site plan", "https://www.taylortx.gov/1383/KDC-Project-Comal"],
     ["City of Taylor: KDC's council package (Dec 19, 2025)", "https://www.taylortx.gov/DocumentCenter/View/15926"],
     ["Spectrum News: Taylor annexes the land (Mar 27, 2026)", "https://spectrumlocalnews.com/tx/austin/news/2026/03/27/taylor-approves-land-annexation-for-kdc-data-center"],
     ["Data Center Dynamics: 360 MW, six buildings, two substations", "https://www.datacenterdynamics.com/en/news/360mw-data-center-to-be-built-outside-austin-texas/"]]
p = "data/details.json"; d = json.load(open(p)); e = d.setdefault(K, {})
have = {u for _, u in e.get("links", [])}
e.setdefault("links", []).extend(x for x in L if x[1] not in have)
e["loc"] = "1051 County Road 401, Taylor, northeast of the Samsung chip plant and near Taylor High School (pin approximate)"
e["acres"] = "About 210 acres"
e["llc"] = "KDC Real Estate Development and Investments (Dallas); planned for a single hyperscale tenant"
e["incent"] = "KDC offered a $75,000 parks donation and to hire and train two Taylor high school students each summer"
e["dates"] = "Council package Dec 19, 2025; residents raised traffic, health and environmental concerns; Taylor annexed the land Mar 2026. Buildings listed for 2028 and 2029"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
old = '{name:"KDC Project Comal", county:"Williamson", type:"data", status:"announced", lat:30.6, lng:-97.7,\n   dev:"KDC", power:"360 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."'
new = '{name:"KDC Project Comal", county:"Williamson", type:"data", status:"approved", lat:30.56, lng:-97.43,\n   dev:"KDC Real Estate Development and Investments (Dallas)", power:"360 MW from Oncor, with two new substations", water:"Not disclosed", conf:"Reporting", note:"A $2.5B, six-building campus on about 210 acres in Taylor, next to the Samsung chip plant and near Taylor High School. The city annexed the land in Mar 2026. It is Taylor\'s second approved data center campus this year."'
s = open("texas.html").read()
if new not in s:
    assert s.count(old) == 1, "Comal card not found"; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>KDC Project Comal</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We placed Project Comal near Georgetown and showed it as only announced. It is in Taylor, at County Road 401 near the Samsung plant, and the city annexed the land for it in March 2026. The pin has been moved and the status changed to approved.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 18: KDC Project Comal checked; pin moved to Taylor; status approved")
