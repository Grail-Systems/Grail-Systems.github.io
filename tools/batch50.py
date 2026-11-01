"""Originals batch 50: Airport Drive, Wichita Falls. Council unanimously rejected rezoning homes-adjacent land for an unnamed developer; later approved a small reuse next door."""
import json
K = "Airport Drive data center"
L = [
 ["KAUZ: council tables Airport Drive rezoning; concern it could open the land to other industrial uses (Feb 2026)", "https://www.newschannel6now.com/2026/02/17/another-data-center-could-be-coming-wichita-falls/"],
 ["KAUZ: council unanimously rejects the rezoning (May 5, 2026)", "https://newschannel6now.com/2026/05/05/wichita-falls-city-council-rejects-airport-drive-data-center-rezoning/"],
 ["KAUZ: DataNovaX's small data center in a former grocery store at 2236 Airport Drive approved with conditions (Aug 2026)", "https://www.newschannel6now.com/2026/08/13/datanovax-data-center-approved-airport-drive-wichita-falls/"],
]
p = "data/details.json"; d = json.load(open(p))
e = d.setdefault(K, {}); have = {u for _, u in e.get("links", [])}
e.setdefault("links", []).extend(x for x in L if x[1] not in have)
e["loc"] = "2100 and 2226 Airport Drive, north Wichita Falls, near existing homes"
e["acres"] = "About 37 acres to rezone, for a campus described as up to 98 acres"
e["llc"] = "Applicant Brad Altman, an attorney and developer; the data center operator was never identified"
e["dates"] = "Rezoning from multifamily residential to light industrial tabled Feb 3, 2026; rejected unanimously May 5, 2026. In Aug 2026, P&Z approved a separate, smaller DataNovaX data center reusing an empty 37,000 sq ft building at 2236 Airport Drive, with conditions"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Not identified", power:"Size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Listed as canceled. Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Applicant Brad Altman; data center operator never identified", power:"Size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Rejected. The applicant asked to rezone land zoned for apartments, beside existing homes, to light industrial. The council worried the rezoning would allow other industrial uses too, and voted unanimously no in May 2026, citing the homes and the unknown developer. Three months later the city approved a much smaller data center next door that reuses an empty grocery store building, with conditions."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 50: Airport Drive (rejected unanimously; unknown developer) checked")
