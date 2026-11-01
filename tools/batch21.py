"""Originals batch 21: Ellis County Data Ranch (PowerHouse/Provident; pin moved) and Lincoln's South Dallas campus."""
import json
L = {
 "Ellis County Data Ranch": [
   ["Dallas Innovates: Provident and PowerHouse plan 24 buildings on 768 acres", "https://dallasinnovates.com/dallas-provident-data-centers-virginias-powerhouse-partner-on-hyperscale-north-texas-campus/"],
   ["Data Center Dynamics: a 1.8 GW campus in DFW", "https://datacenterdynamics.com/en/news/powerhouse-and-provident-to-develop-18gw-campus-in-dfw-texas"],
   ["Texas Dept. of Licensing and Regulation: Building 1 at 881 Miller Road", "https://www.tdlr.texas.gov/TABS/Projects/TABS2026016734"]],
 "Lincoln Rackhouse Dallas Wholesale II": [
   ["Data Center Dynamics: Lincoln's 131-acre, 540 MW campus", "https://datacenterdynamics.com/en/news/lincoln-announces-131-acre-data-center-campus-in-dallas-texas"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
r = d["Ellis County Data Ranch"]
r["loc"] = "881 Miller Road, Midlothian mailing address, just outside Grand Prairie in northern Ellis County (pin approximate)"
r["acres"] = "768 acres (some listings say 810)"
r["llc"] = "PowerHouse Data Centers (American Real Estate Partners) and Provident Data Centers, joint venture"
r["dates"] = "Announced Feb 2025; first 500 MW approved through ERCOT; Building 1 filed with the state for Apr 2026 to Apr 2028"
l = d["Lincoln Rackhouse Dallas Wholesale II"]
l["loc"] = "South Dallas area; the exact site and county have not been published"
l["acres"] = "131 acres"
l["llc"] = "Lincoln Property Company (the Rackhouse brand was retired)"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('{name:"Ellis County Data Ranch", county:"Ellis", type:"data", status:"construction", lat:32.35, lng:-96.8,\n   dev:"Not identified", power:"500 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  '{name:"Ellis County Data Ranch", county:"Ellis", type:"data", status:"construction", lat:32.54, lng:-96.98,\n   dev:"PowerHouse Data Centers and Provident Data Centers", power:"1.8 GW switchyard; first 500 MW approved through ERCOT", water:"Not disclosed", conf:"Reporting", note:"24 buildings in three phases on 768 acres just outside Grand Prairie. Building 1 is filed with the state for 2026 to 2028. PowerHouse is also behind Taylor and Westlake."'),
 ('dev:"Lincoln Rackhouse", power:"540 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Lincoln Property Company", power:"Up to 540 MW in four buildings (company figure)", water:"Not disclosed", conf:"Reporting", note:"A 131-acre, 800,000 sq ft campus in the South Dallas area. Lincoln has not published the exact site, so the pin and county are approximate."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Ellis County Data Ranch</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We showed this with the developer not identified, pinned at Waxahachie. It is the PowerHouse and Provident campus on Miller Road just outside Grand Prairie, about 17 miles north, planned for 1.8 GW. Developer and pin are fixed.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 21: Ellis County Data Ranch (PowerHouse/Provident) and Lincoln checked")
