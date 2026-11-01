"""Source batch 8: the last cards with no source link (Freestone, Bosque, Kaufman, Tarrant, Caldwell, Reeves, Childress)."""
import json
L = {
 "CyrusOne at Freestone Energy Center": [["Constellation: the 380 MW agreement (Feb 9, 2026)", "https://investors.constellationenergy.com/news-releases/news-release-details/constellation-and-cyrusone-announce-agreement-support-new-data/"],
   ["Data Center Dynamics: 760 MW over two phases", "https://www.datacenterdynamics.com/en/news/cyrusone-partners-with-constellation-for-760mw-data-center-campus-in-texas/"]],
 "CyrusOne at Thad Hill Energy Center": [["Data Center Dynamics: 400 MW campus, first building due Q4 2026", "https://www.datacenterdynamics.com/en/news/cyrusone-partners-with-constellation-for-760mw-data-center-campus-in-texas/"],
   ["More Than Just Parks tracker entry (CyrusOne DFW17C, Whitney)", "https://morethanjustparks.com/data-center-tracker/cyrusone-dfw17c-whitney-data-center-campus-tx--b3e13681-0733-45ff-8f14-42c407cd5f82"]],
 "Flexential Talty campus": [["Flexential: the 110-acre purchase (July 28, 2026)", "https://www.prnewswire.com/news-releases/flexential-to-build-new-dallas-area-data-center-campus-on-110-acres-in-kaufman-county-302836104.html"],
   ["Town of Talty: location of the campus", "https://www.taltytexas.com/page/article/68"],
   ["NBC DFW: the land left the city's jurisdiction by petition", "https://www.nbcdfw.com/news/local/data-center-spanning-hundreds-of-acres-planned-in-kaufman-county/4055993/"]],
 "PowerHouse Westlake": [["Data Center Dynamics: Circle T plans, 300 MW", "https://www.datacenterdynamics.com/en/news/powerhouse-files-for-300mw-data-center-campus-outside-dallas-fort-worth/"],
   ["KERA: a Tarrant County judge blocks the town's agreement (Aug 2026)", "https://www.keranews.org/news/2026-08-18/westlake-data-center-agreement-temporarily-blocked-by-tarrant-county-court"],
   ["More Than Just Parks tracker entry (Circle T)", "https://morethanjustparks.com/data-center-tracker/circle-t-data-center-westlake-tx--a3187960-4f53-42be-b0a4-3ae2d4cd7b09"]],
 "PowerHouse Caldwell County": [["More Than Just Parks tracker entry (Powerhouse DC, Caldwell County)", "https://morethanjustparks.com/data-center-tracker/powerhouse-dc-tx--73c5f933-48bf-4525-bdf3-74c10bcc5cbe"]],
 "Core Scientific Pecos": [["MarketBeat: Core Scientific's earnings call on the Pecos conversion (Mar 2026)", "https://www.marketbeat.com/instant-alerts/core-scientific-q4-earnings-call-highlights-2026-03-02/"]],
 "Lancium Childress": [["Inside Climate News: the water testimony (Apr 16, 2026)", "https://insideclimatenews.org/?p=107973"],
   ["ABC 7 Amarillo: Childress boil-water notice; Lancium offers a water source (Sept 2026)", "https://abc7amarillo.com/news/local/childress-distributes-bottled-water-as-boil-notice-stretches-past-a-week-mayor-cary-preston-greenbelt-reservoir-city-manager-kevin-hodges-ross-gardens-randa-giter"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
d["CyrusOne at Freestone Energy Center"]["dates"] = "Feb 9, 2026: 380 MW agreement for the first phase, plus an exclusive deal for a second 380 MW phase (760 MW total)"
d["CyrusOne at Thad Hill Energy Center"]["dates"] = "July 2025 agreement; about 400 MW. First data center under construction, due online by the end of 2026"
f = d["Flexential Talty campus"]
f["loc"] = "Talty, north of the Forney ISD learning academy near Helms Trail and FM 1641"
f["dates"] = "Land bought July 2026; work to begin early 2027. First building 375,000 sq ft with 36 MW of power secured. The land was released from a city's jurisdiction by petition under state law"
w = d["PowerHouse Westlake"]
w["loc"] = "13580 Denton Hwy (US 377 at Westport Pkwy), Westlake, at the north edge of Keller"
w["llc"] = "Circle T Owner LP; American Real Estate Partners (AREP); engineer Kimley-Horn"
w["dates"] = "Westlake planning and zoning approved the plans in Aug 2026. A Tarrant County district judge then temporarily barred the town council from approving its development agreement, after Keller residents objected; homes are about 500 feet away"
w["incent"] = "PowerHouse paid for a 350 MW Oncor substation and would pay Westlake $914,000 toward its pump station"
d["Lancium Childress"]["dates"] = "Testimony to a Texas House committee, Apr 2026. In Sept 2026 Childress was under a boil-water notice and a local disaster declaration after extreme heat; the city manager said Lancium had offered a possible new water source"
d["Core Scientific Pecos"]["dates"] = "300 MW secured Apr 2026. In Mar 2026 the company said the conversion was underway, aiming to be ready for a customer within 12 months"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('power:"380 MW agreement", water:"Not disclosed", conf:"Reporting",\n   note:"A data center built right next to an existing gas plant. Announced Feb 2026.", src:"Constellation press release (Business Wire)"}',
  'power:"380 MW, with a second 380 MW phase planned (760 MW)", water:"Not disclosed", conf:"Reporting",\n   note:"A data center built right next to an existing gas plant. Announced Feb 2026.", src:"Constellation press release; Data Center Dynamics"}'),
 ('dev:"PowerHouse Data Centers", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"About 88 acres north of Fort Worth. Plans filed by Kimley-Horn.", src:"Baxtel (citing NBC)"}',
  'dev:"PowerHouse Data Centers (American Real Estate Partners)", power:"Up to 300 MW in four buildings", water:"Not disclosed", conf:"Reporting",\n   note:"Circle T Data Center, about 88 acres at the north edge of Keller. A Tarrant County judge temporarily blocked Westlake from approving the deal in Aug 2026.", src:"Data Center Dynamics; KERA; NBC DFW"}'),
 ('dev:"Flexential", power:"108 MW", water:"Not disclosed", conf:"Reporting",\n   note:"110 acres bought July 2026. First phase 36 MW.", src:"Baxtel"}',
  'dev:"Flexential", power:"108 MW across three buildings; 36 MW secured for the first", water:"Company says closed-loop cooling, aiming for near-zero water use", conf:"Reporting",\n   note:"110 acres bought July 2026. Work to begin early 2027.", src:"Flexential release; Town of Talty; NBC DFW"}'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:70]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 8: 7 cards linked and filled in")
