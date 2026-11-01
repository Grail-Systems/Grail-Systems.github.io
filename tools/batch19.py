"""Originals batch 19: Jarrell (Mesones Prime) and the Williamson County AI Campus (Skybox/Prologis, Hutto)."""
import json
L = {
 "Mesone data center (Jarrell)": [
   ["Data Center Dynamics: Jarrell approves the data center (Oct 2025)", "https://www.datacenterdynamics.com/en/news/jarell-texas-greenlights-plans-for-data-center/"],
   ["Texas Scorecard: residents collect signatures against it", "https://texasscorecard.com/local/locals-oppose-proposed-jarrell-data-center/"],
   ["Williamson County Sun: next to Jarrell High School; $7.2M a year to the city", "https://www.wilcosun.com/node/7478"]],
 "Williamson County AI Campus": [
   ["Data Center Dynamics: Skybox and Prologis file a fourth Hutto building", "https://datacenterdynamics.com/en/news/skybox-prologis-file-for-fourth-data-center-in-hutto-texas"],
   ["Texas Dept. of Licensing and Regulation: Skybox Hutto 1 filing", "https://www.tdlr.texas.gov/TABS/Search/Print/TABS2024003524"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
m = d["Mesone data center (Jarrell)"]
m["loc"] = "3911 County Road 305, Jarrell, directly behind Jarrell High School"
m["acres"] = "About 151 acres"
m["llc"] = "Prominent Property Group, Savannah Developers and Power Infrastructure Partners; called Mesones Prime"
m["dates"] = "Planning and zoning recommended approval Aug 2025; residents objected at a Sept 2025 workshop; city council annexed and rezoned the land Oct 14, 2025. First building planned for 2027"
w = d["Williamson County AI Campus"]
w["loc"] = "4200 County Road 132, Hutto (pin approximate)"
w["llc"] = "Skybox Datacenters with Prologis; site owner Hutto Data Center Campus LLC; called PowerCampus Austin"
w["dates"] = "Announced May 2023. Building 1 built 2024; Building 2 fit-out due June 2026; Building 4 ($550M) filed Oct 2026, construction Jan 2027 to Oct 2028"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('status:"announced", lat:30.82, lng:-97.6,\n   dev:"Mesone", power:"200 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'status:"approved", lat:30.82, lng:-97.6,\n   dev:"Prominent Property Group, Savannah Developers and Power Infrastructure Partners", power:"About 200 MW from gas and grid power", water:"Not disclosed", conf:"Reporting", note:"An $850M campus on about 151 acres right behind Jarrell High School, in a town of under 2,000 people. Approved Oct 2025; it would roughly double the city\'s budget. Residents are collecting signatures against it."'),
 ('{name:"Williamson County AI Campus", county:"Williamson", type:"data", status:"announced", lat:30.65, lng:-97.6,\n   dev:"Not identified", power:"600 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  '{name:"Williamson County AI Campus", county:"Williamson", type:"data", status:"construction", lat:30.57, lng:-97.52,\n   dev:"Skybox Datacenters with Prologis", power:"600 MW planned across about 3.9M sq ft", water:"Not disclosed", conf:"Reporting", note:"PowerCampus Austin in Hutto. The first building is built, a second is being fitted out, and a $550M fourth building was filed with the state in Oct 2026. Same developer as Wichita Falls."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Williamson County AI Campus</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We listed this as an announced project with the developer not identified, pinned near Georgetown. It is Skybox and Prologis\'s PowerCampus Austin in Hutto, and buildings are already built and under construction. Developer, status and pin are fixed.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 19: Jarrell approved; Williamson AI Campus is Skybox in Hutto")
