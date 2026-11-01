"""Originals batch 10: Bells (Grayson) and Delta County, checked against Texas Tribune and KXII reporting."""
import json
TT = "https://www.texastribune.org/2026/08/10/texas-data-centers-transparency-information/"
L = {
 "Bells AI data center": [["Texas Tribune: how a Bells family uncovered the project (Aug 10, 2026)", TT],
   ["KXII: Grayson County asks the state for local control (Mar 17, 2026)", "https://www.kxii.com/2026/03/17/grayson-county-pushes-take-local-control-over-future-ai-data-center-developments/"]],
 "Delta County data center": [["Texas Tribune: Delta County opposes data center abatements (Aug 10, 2026)", TT]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
b = d.setdefault("Bells AI data center", {})
b["loc"] = "Rural land near Bells, about an hour north of Dallas"
b["dates"] = "Survey markers appeared in 2025. A Bells resident traced land contracts to Black Mountain and found a power plant permit from a company at Black Mountain's address; Black Mountain's CEO, Rhett Bennett, confirmed in Mar 2026 that it was exploring a data center there. Grayson County passed a resolution asking the Legislature for local authority (Mar 2026)"
dl = d.setdefault("Delta County data center", {})
dl["dates"] = "Delta County commissioners passed a resolution in Mar 2026 opposing tax abatements for data centers; County Judge Tanner Crutcher has called for state disclosure rules instead"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Black Mountain", power:"Campus; size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Same developer as Black Mountain Power projects in Fort Worth and near Dinosaur Valley. Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Black Mountain (CEO Rhett Bennett confirmed it was exploring the site)", power:"Size not disclosed; a power plant permit was filed by a company at Black Mountain\'s address", water:"Not disclosed", conf:"Reporting", note:"Neighbors found it themselves, through survey markers, land records and a permit search, before any public announcement. Same developer as Black Mountain\'s Fort Worth and Dinosaur Valley projects."'),
 ('dev:"LS Power", power:"Size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"LS Power (per the tracker; not yet confirmed in local reporting)", power:"Size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Delta County commissioners voted in March 2026 to oppose tax abatements for data centers."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:70]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 10: Bells and Delta checked against originals")
