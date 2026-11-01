"""Originals batch 9: Bowie County (Datahub, Project Big Pine) and Hunt County (Core Scientific Quinlan), checked against original reporting."""
import json
L = {
 "Datahub Developers AI data center": [["Atlanta Journal-Constitution: the buyer is tied to Rick Jackson (Sept 2026)", "https://www.ajc.com/politics/2026/09/why-a-texas-data-center-project-is-roiling-georgias-race-for-governor/"],
   ["Texarkana Today: the $12 million sale and its confidentiality clause", "https://txktoday.com/news/bowie-countys-data-center-deal-just-got-dragged-into-the-georgia-governors-race/"],
   ["KSLA: residents confront the Hooks council (Sept 24, 2026)", "https://www.ksla.com/2026/09/24/bowie-county-residents-confront-council-over-data-center-land-sale/"]],
 "Project Big Pine": [["Data Center Dynamics: Potentia's behind-the-meter site", "https://www.datacenterdynamics.com/en/news/potentia-plans-450-acre-behind-the-meter-site-in-bowie-county-texas-for-potential-data-center/"],
   ["Railway Age: the SWEPCO/SPP grid queue, water and gas", "https://www.railwayage.com/freight/texamericas-center-advances-rail-served-data-center-site-project/"],
   ["Business Facilities: the incentives offered", "https://businessfacilities.com/texamericas-center-potentia-development-advance-3-5b-project-big-pine/"],
   ["Texarkana Today: Black Mountain separately buys 600 acres in Bowie County", "https://txktoday.com/news/data-center-developer-quietly-buys-600-acres-in-bowie-county/"]],
 "Telios Quinlan Campus": [["Baxtel: Core Scientific's Hunt County campus", "https://connect.baxtel.com/data-centers/core-scientific"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
dh = d["Datahub Developers AI data center"]
dh["llc"] = "Datahub Developers LLC, registered at Jackson Healthcare's office in Alpharetta, Ga.; related LLCs include Datahub Developers Texarkana I. Officials say it is now called Foundrie Hyperscale Data"
dh["loc"] = "East Texas Logistics Center, between Hooks and New Boston, off I-30"
dh["dates"] = "Bowie County commissioners approved a $12M sale Aug 28, 2026, over a courtroom of objecting residents; the contract has a confidentiality clause. The Hooks and New Boston development boards followed, and the deed was signed Sept 11"
bp = d["Project Big Pine"]
bp["llc"] = "Potentia Development (The Woodlands; CEO Carl Quesinberry), with TexAmericas Center"
bp["land"] = "About 450 to 500 acres on TexAmericas Center's East Campus"
bp["dates"] = "Announced Apr 28, 2026; still seeking an anchor tenant. Planned on-site gas power with batteries; in the SWEPCO grid queue in the Southwest Power Pool, not ERCOT. TexAmericas acts as the only local permitting authority"
bp["incent"] = "Foreign Trade Zone 258, Opportunity Zone, New Markets Tax Credits, no municipal property tax, and the state's large data center sales tax exemption"
d["Telios Quinlan Campus"]["dates"] = "Core Scientific: about 285 MW on 265 acres, scalable to 430 MW with an on-site substation; first power expected 2027, full buildout 2029"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Datahub Developers", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"I-30 megasite at the East Texas Logistics Center, Hooks. Needs verification.", src:"More Than Just Parks data center tracker"}',
  'dev:"Datahub Developers LLC, tied to Georgia businessman and governor candidate Rick Jackson; now called Foundrie Hyperscale Data", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"Bowie County, Hooks and New Boston sold public industrial land at the East Texas Logistics Center for $12M in Aug and Sept 2026, under a contract with a confidentiality clause, over residents\' objections.", src:"Atlanta Journal-Constitution; Texarkana Today; KSLA"}'),
 ('dev:"Not identified (TexAmericas Center)", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"Near Texarkana. Needs verification.", src:"More Than Just Parks data center tracker"}',
  'dev:"Potentia Development, with TexAmericas Center", power:"Planned on-site gas with batteries; size not disclosed", water:"Company cites regional water availability; amount not disclosed", conf:"Reporting",\n   note:"About $3.5B and 120 jobs at full buildout on 450 to 500 acres, still looking for a tenant. On the SPP grid, not ERCOT.", src:"Data Center Dynamics; Railway Age; KSLA; Texarkana Today"}'),
 ('dev:"Core Scientific", power:"430 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Core Scientific", power:"About 285 MW, scalable to 430 MW", water:"Not disclosed", conf:"Reporting", note:"265 acres near Quinlan with an on-site substation; first power expected 2027."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:70]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 9: 3 cards checked against originals (Datahub, Big Pine, Quinlan)")
