"""Originals batch 15: CleanSpark (Austin County) and Applewhite Technology Park (Bexar)."""
import json
L = {
 "CleanSpark Austin County AI campus": [
   ["CleanSpark: the 271-acre, 285 MW purchase (Oct 29, 2025)", "https://investors.cleanspark.com/news/news-details/2025/CleanSpark-Enters-Texas-Market-with-Land-and-Large-Scale-Power-Acquisition-to-Rapidly-Deploy-an-AI-Data-Center-in-Greater-Houston/default.aspx"],
   ["KPRC: residents protest in tractors and trailers (Aug 15, 2026)", "https://www.click2houston.com/news/local/2026/08/15/austin-county-residents-protest-cleanspark-data-center-in-sealy/"]],
 "Applewhite Technology Park": [
   ["Baxtel: Tract's 339-acre site on Mauermann Road", "https://baxtel.com/data-center/tract-applewhite-tech-park"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
c = d["CleanSpark Austin County AI campus"]
c["loc"] = "Sealy area, Austin County"
c["acres"] = "About 271 acres; the company says the building itself would use about 10"
c["dates"] = "Land and power bought Oct 2025; company aims to switch on more than 200 MW in the first half of 2027, with a substation already under construction. Austin County adopted a moratorium July 2026. Residents protested CleanSpark's community meeting Aug 15, 2026"
a = d["Applewhite Technology Park"]
a["loc"] = "Mauermann Road, south San Antonio, near the Toyota plant and Texas A&M-San Antonio"
a["acres"] = "339 acres of industrial land"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"CleanSpark", power:"285 MW listed", water:"Not disclosed", conf:"Reporting", note:"Austin County adopted a moratorium on new AI data centers in July 2026; CleanSpark spoke against it. Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"CleanSpark (a bitcoin miner moving into AI)", power:"285 MW under contract; over 200 MW targeted for early 2027", water:"Company says closed-loop cooling using less than 10 homes\' worth of water a day; not independently confirmed", conf:"Reporting", note:"271 acres near Sealy. Austin County adopted a moratorium on new AI data centers in July 2026 over CleanSpark\'s objection; in August residents drove tractors and trailers to the company\'s community meeting in protest."'),
 ('dev:"Tract", power:"720 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Tract", power:"The tracker lists 720 MW; not confirmed elsewhere", water:"Not disclosed", conf:"Reporting", note:"339 acres of industrial land on Mauermann Road in south San Antonio, near the Toyota plant. Tract sells powered land to data center operators; no tenant named."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 15: CleanSpark and Applewhite checked against originals")
