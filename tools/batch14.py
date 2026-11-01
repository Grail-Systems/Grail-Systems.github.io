"""Originals batch 14: Project Raptor (Archer) and Energy Ranch (Atascosa)."""
import json
L = {
 "Project Raptor (Google)": [
   ["KAUZ: Archer County denies the tax abatement unanimously (June 22, 2026)", "https://www.newschannel6now.com/2026/06/22/archer-county-commissioners-deny-tax-abatement-proposed-data-center/"],
   ["Archer County News: county denies Project Raptor an abatement", "https://www.archercountynews.com/news/county-denies-project-raptor-tax-abatement"],
   ["Archer County News: county releases details on the $1B project", "https://www.archercountynews.com/news/more-information-released-1b-data-center-project"]],
 "Energy Ranch": [
   ["Data Center Dynamics: oil and gas investors plan a 1,500-acre campus", "https://www.datacenterdynamics.com/en/news/oil-gas-investors-plan-1500-acre-data-center-and-energy-campus-outside-san-antonio-texas/"],
   ["Pleasanton Express: county officials left in the dark", "https://www.pleasantonexpress.com/news/atascosa-county-officials-left-in-the-dark-over-rumored-data-center-project/article_ad248361-bc14-4e71-b3b6-958d3def2fc9.html"],
   ["KSAT: residents pack the Justice Center (July 2026)", "https://www.ksat.com/news/local/2026/07/08/atascosa-county-residents-voice-concerns-over-potential-data-centers/"],
   ["Fox San Antonio: Atascosa County residents fight the project", "https://foxsanantonio.com/news/local/atascosa-county-residents-fight-proposed-data-center"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
r = d["Project Raptor (Google)"]
r["loc"] = "About 2,800 acres along Three Way Road, west of Wichita Falls"
r["llc"] = "Dynamo Ventures filed the abatement request; state officials say Google is the interested company"
r["dates"] = "Details released by the county Apr 27, 2026; public forum May 21; abatement request filed June 3; Commissioners Court denied it unanimously June 22, 2026"
r["incent"] = "Tax abatement requested and denied unanimously"
e = d["Energy Ranch"]
e["loc"] = "Eagle Ford Shale property owned by the Herrmann family, a few miles northwest of Jourdanton"
e["acres"] = "More than 1,500 acres"
e["llc"] = "HC Capital Partners and Herrmann Family Companies; power from Wrangler Infrastructure (HC Infrastructure Partners)"
e["dates"] = "Announced Jan 2026. In July 2026 county officials said no project had been submitted and the developers had not contacted them; residents packed the Justice Center"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('county:"Archer", type:"data", status:"announced", lat:33.6, lng:-98.63,\n   dev:"Google", power:"Campus; size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'county:"Archer", type:"data", status:"announced", lat:33.6, lng:-98.63,\n   dev:"Google, per state officials (request filed by Dynamo Ventures)", power:"Size not disclosed", water:"Not disclosed", conf:"Reporting", note:"A $1B campus on about 2,800 acres along Three Way Road. After a packed meeting, Archer County commissioners denied the tax abatement unanimously in June 2026."'),
 ('dev:"HC Capital Partners / Herrmann Family Companies", power:"250 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"HC Capital Partners and Herrmann Family Companies", power:"Gas power built on site by Wrangler Infrastructure; the tracker lists 250 MW", water:"Company cites a water strategy; amount not disclosed", conf:"Reporting", note:"A gas-powered campus on 1,500+ acres of Eagle Ford oil land near Jourdanton, announced Jan 2026. County officials said the developers had not contacted them. Residents formed Atascosa County Against Data Centers."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 14: Project Raptor and Energy Ranch checked against originals")
