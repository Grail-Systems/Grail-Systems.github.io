"""Source batch 4: San Marcos (Hays), Stargate Milam, Rowan Temple (Bell)."""
import json
L = {
 "San Marcos data center (Francis Harris Lane)": [["Texas Public Radio / KUT: council blocks it 5 to 2 (Feb 18, 2026)", "https://www.tpr.org/news/2026-02-18/san-marcos-city-council-blocks-proposed-data-center"],
   ["Community Impact: the vote and the protest", "https://communityimpact.com/san-marcos-buda-kyle/government/san-marcos-council-denies-map-change-stops-data-center-development/"],
   ["Community Impact: San Marcos bans data centers in every zoning district (June 2026)", "https://beta2.communityimpact.com/austin/san-marcos-buda-kyle/government/2026/06/17/san-marcos-council-votes-to-prohibit-data-centers-in-all-zoning-districts/"]],
 "Stargate Milam County": [["OpenAI: the SB Energy partnership and 1.2 GW lease", "https://openai.com/index/stargate-sb-energy-partnership/"],
   ["Reuters: OpenAI and SoftBank put $1 billion into SB Energy (Jan 9, 2026)", "https://finance.yahoo.com/news/openai-softbank-invest-1-billion-192620783.html"],
   ["Data Center Dynamics: SB Energy to build and run the site", "https://www.datacenterdynamics.com/en/news/softbanks-sb-energy-to-build-and-operate-openais-12gw-stargate-data-center-in-milam-county-texas/"]],
 "Rowan Temple campus": [["Data Center Dynamics: construction starts on 300 MW (Jan 2026)", "https://www.datacenterdynamics.com/en/news/rowan-starts-work-on-300mw-data-center-in-temple-texas/"],
   ["Data Center Dynamics: second building filed", "https://www.datacenterdynamics.com/en/news/rowan-files-for-second-building-at-data-center-campus-in-temple-texas/"],
   ["Temple EDC: council approval and annexation (Sept 2025)", "https://templeedc.com/?p=2928"],
   ["Bisnow: $3 billion in debt financing", "https://www.bisnow.com/austin-san-antonio/news/data-center/sustainable-developer-bringing-data-center-campus-to-temple-134759"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
d["San Marcos data center (Francis Harris Lane)"]["dates"] = "Planning commission recommended denial Mar 2025; council denied it Aug 2025 for lack of a supermajority; denied again 5 to 2 on Feb 17-18, 2026; the city banned data centers in all zoning districts June 16, 2026"
d["San Marcos data center (Francis Harris Lane)"]["llc"] = "Highlander SM One LLC, Fort Worth; earlier reported as a CyrusOne project called Maberry"
d["Stargate Milam County"]["dates"] = "Announced 2025. Jan 9, 2026: OpenAI and SoftBank put $1B into SB Energy, which will build and run the 1.2 GW site; OpenAI signed a 1.2 GW lease. New solar and batteries planned; OpenAI says the design minimizes water use"
d["Stargate Milam County"]["llc"] = "SB Energy (owned by SoftBank); OpenAI is the tenant"
r = d["Rowan Temple campus"]
r["land"] = "About 700 acres along Bob White Road, annexed by Temple in Sept 2025"
r["dates"] = "Council approved unanimously Sept 2025; construction began Jan 2026; $3B in debt financing May 2026; second building ($780M) filed July 2026; first building due 2027"
r["llc"] = "Rowan Temple LLC; Rowan is backed by Quinbrook Infrastructure Partners and Birch Infrastructure. Occupant Polmer LLC, a Meta subsidiary"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Not identified", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"About 200 acres. The City Council denied the rezoning 5-2',
  'dev:"Highlander SM One LLC (Fort Worth)", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"About 200 acres. The City Council denied the rezoning 5-2'),
 ('dev:"Rowan Digital Infrastructure", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"1855 Bob White Road. Plans for a second building filed July 2026.", src:"Baxtel"}',
  'dev:"Rowan Digital Infrastructure", power:"Up to 300 MW at full build-out, from Oncor", water:"Not disclosed", conf:"Reporting",\n   note:"About 700 acres on Bob White Road, about $700M to start. Construction began Jan 2026; a second $780M building was filed in July. The Comptroller lists a Meta subsidiary as the tenant.", src:"Data Center Dynamics; Temple EDC; Bisnow; Texas Comptroller"}'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:70]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 4: 3 cards linked and filled in (San Marcos, Stargate Milam, Rowan Temple)")
