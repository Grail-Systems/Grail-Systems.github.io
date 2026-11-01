"""Originals batch 47: Zydeco Hutto (stopped by a formal written protest) and Sabey San Marcos (not under construction; third campus by the Hays Energy gas plant)."""
import json
L = {
 "Zydeco Hutto data center": [
   ["City of Hutto: Zydeco withdraws rezoning request (Apr 17, 2026)", "https://www.huttotx.gov/CivicAlerts.aspx?AID=424"],
   ["KUT: withdrawal ends the project; residents were filing a formal protest that would require a 3/4 council vote", "https://www.kut.org/energy-environment/2026-04-20/hutto-tx-zydeco-data-center-rezoning-request"],
   ["Fox 7: residents filed two written protests a week before the withdrawal", "https://www.fox7austin.com/news/hutto-data-center-developer-withdraws-rezone-request"],
   ["Community Impact: withdrawn just before the special P&Z meeting; Stop the Hutto Data Center", "https://communityimpact.com/pflugerville-hutto/government/zydeco-development-withdraws-zoning-request-for-data-center-in-hutto/"]],
 "Sabey / Carson Select San Marcos campus": [
   ["Data Center Dynamics: Sabey seeks 786 acres in San Marcos; council starts negotiating (June 2025)", "https://www.datacenterdynamics.com/en/news/sabey-looks-to-develop-data-center-campus-outside-austin-texas/"],
   ["Community Impact: three data centers proposed around San Marcos; river foundation tracking seven in the watershed", "https://communityimpact.com/san-marcos-buda-kyle/government/3-data-centers-newly-proposed-in-and-around-san-marcos/"],
   ["San Antonio Express-News via GovTech: third data center within 1.5 miles of the Hays Energy gas plant", "https://insider.govtech.com/texas/news/plans-call-for-third-data-center-in-growing-hill-county-cluster"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
z = d["Zydeco Hutto data center"]
z["loc"] = "450 Ed Schmidt Boulevard, Hutto (land zoned for multifamily housing)"
z["acres"] = "About 40 acres; 225,000 sq ft building planned"
z["llc"] = "Zydeco Development Corporation (Austin)"
z["dates"] = "City staff recommended denial Apr 7, 2026; residents filed two formal written protests about a week before; Zydeco withdrew Apr 17, 2026, just before a special P&Z meeting, which was canceled"
s_ = d["Sabey / Carson Select San Marcos campus"]
s_["loc"] = "Southwest of South Old Bastrop Highway and Centerpoint Road, about 7.5 miles south of downtown San Marcos, within 1.5 miles of the Hays Energy gas plant"
s_["acres"] = "About 786 acres"
s_["llc"] = "Sabey Data Centers with Carson Select Investments LP (Carson Properties), the landowner"
s_["dates"] = "San Marcos City Council began negotiating a development agreement June 3, 2025; no construction found"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Zydeco", power:"70 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed as withdrawn. Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Zydeco Development", power:"70 MW planned", water:"Not disclosed", conf:"Reporting", note:"Stopped by residents. Zydeco needed land zoned for apartments rezoned to heavy industrial. City staff recommended denial, and the Stop the Hutto Data Center group filed formal written protests that would have forced a three-fourths council vote. Zydeco withdrew in April 2026, days before the P&Z hearing."'),
 ('{name:"Sabey / Carson Select San Marcos campus", county:"Hays", type:"data", status:"construction", lat:29.85, lng:-97.95,\n   dev:"Sabey and Carson Select", power:"Campus; size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  '{name:"Sabey / Carson Select San Marcos campus", county:"Hays", type:"data", status:"announced", lat:29.80, lng:-97.90,\n   dev:"Sabey Data Centers, with landowner Carson Select Investments", power:"Size not disclosed", water:"Not disclosed", conf:"Reporting", note:"About 786 acres south of San Marcos, the third data center proposed within 1.5 miles of the Hays Energy gas plant. The landowner told the city it had been \\"overwhelmed with unsolicited offers\\" before choosing Sabey. The council began negotiating in June 2025; we found no construction. The San Marcos River Foundation is tracking seven proposed data centers in the river\'s watershed."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Sabey San Marcos status and pin</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We showed Sabey\'s San Marcos campus as under construction, pinned in town. The last public step we found was the city starting development agreement talks in June 2025. Status changed to announced and the pin moved about 5 miles south near Old Bastrop Highway and Centerpoint Road.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 47: Zydeco Hutto (stopped by written protest) and Sabey San Marcos (not under construction) checked")
