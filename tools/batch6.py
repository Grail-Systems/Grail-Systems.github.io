"""Source batch 6: Vantage West Side (Bexar) and Bitdeer Rockdale (Milam)."""
import json
L = {
 "Vantage West Side campuses": [["Sierra Club: the lawsuit is filed (Sept 2026)", "https://www.sierraclub.org/press-releases/2026/09/sierra-club-other-enviro-groups-sue-illegal-data-center-power-plant-projects"],
   ["Environmental Integrity Project: notice of intent to sue (July 2026)", "https://environmentalintegrity.org/news/environmental-groups-take-legal-action-against-illegal-data-center-and-power-plant-projects-in-san-antonio/"],
   ["Texas Public Radio: the two campuses and 150+ diesel generators", "https://www.tpr.org/environment/2026-07-28/environmental-groups-threaten-lawsuit-over-west-side-san-antonio-data-centers"],
   ["Law360: case 5:26-cv-06032", "https://www.law360.com/articles/2528350"]],
 "Bitdeer Rockdale": [["Bitdeer: first-quarter 2026 results and site table", "https://bitdeer.gcs-web.com/news-releases/news-release-details/bitdeer-reports-unaudited-financial-results-first-quarter-2026"],
   ["Bitdeer SEC filing: Rockdale capacity (Oct 2025)", "https://www.sec.gov/Archives/edgar/data/0001899123/000121390025107866/ea026473802ex99-1_bitdeer.htm"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
d["Vantage West Side campuses"]["dates"] = "Notice of intent to sue July 22, 2026; lawsuit filed Sept 2026, Public Citizen et al. v. Vantage, 5:26-cv-06032, W.D. Tex. The groups say each company faces fines of up to $124,426 a day; the court has not ruled"
b = d.setdefault("Bitdeer Rockdale", {})
b["dates"] = "563 MW online for bitcoin mining; another 179 MW planned on adjacent land for AI or colocation. In 2026 the company said it was in active evaluation of converting the site to AI"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Bitdeer (spun off from Bitmain)", power:"Not confirmed", water:"Not confirmed", conf:"Reporting",\n   note:"Less than half a mile from Riot, also on former Alcoa land.", link:"/milam/", src:"Greenpeace USA research"}',
  'dev:"Bitdeer (spun off from Bitmain)", power:"563 MW online, with 179 MW more planned (company filings)", water:"Not confirmed", conf:"Records",\n   note:"Less than half a mile from Riot, also on former Alcoa land. Bitdeer says it is weighing converting the site from bitcoin to AI.", link:"/milam/", src:"Bitdeer quarterly reports and SEC filings; Greenpeace USA research"}'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:70]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 6: 2 cards linked; Bitdeer's power filled in from its own filings")
