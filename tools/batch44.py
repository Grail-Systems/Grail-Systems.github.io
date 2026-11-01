"""Originals batch 44: Crusoe Jayton ($4.8B in a county of under 1,000 people) and BlockchAIn Wise County (in an investor pipeline; county says no one has approached it)."""
import json
L = {
 "Crusoe Jayton campus": [
   ["Baxtel: Crusoe files for $4.8B campus in Jayton; Kent County abatement hearing notice (Aug 24, 2026)", "https://baxtel.com/news/crusoe-files-for-4-8b-data-center-campus-in-jayton-texas"],
   ["TechRadar: two buildings of about 759,000 sq ft each; construction Jan 2027, operating 2029", "https://techradar.com/pro/massive-1-5-million-sq-ft-data-center-campus-planned-for-west-texas-bringing-total-regional-ai-investment-to-usd12-billion"]],
 "BlockchAIn Wise County mining site": [
   ["Data Center Dynamics: BlockchAIn's pipeline lists a 20 MW Wise County site, in due diligence, power targeted Q4 2026", "https://www.datacenterdynamics.com/en/news/blockchain-outlines-99bn-plan-for-715mw-data-center-portfolio/"],
   ["Wise County Messenger: county officials say no data center has approached Wise County", "https://www.wcmessenger.com/articles/commissioners-call-for-state-action-on-data-center-development"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
j = d["Crusoe Jayton campus"]
j["loc"] = "Along County Road 233 and P2390 near Jayton, Kent County (no street address filed)"
j["llc"] = "Crusoe Energy Systems, LLC (tracker calls it Project Kent, tied to Crusoe's 'Project Hyper')"
j["dates"] = "Kent County posted a tax abatement hearing notice Aug 24, 2026; state building filings reported Oct 2026; construction set for Jan 2027, operating 2029. Crusoe also has a complex proposed in neighboring Stonewall County"
w = d["BlockchAIn Wise County mining site"]
w["loc"] = "Wise County (exact site not published)"
w["llc"] = "BlockchAIn Digital Infrastructure, Inc."
w["dates"] = "Listed in the company's 2026 investor pipeline as in due diligence, with power targeted for Q4 2026"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Crusoe", power:"Campus; size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Crusoe Energy Systems", power:"Size not disclosed; two buildings of about 759,000 sq ft each", water:"Not disclosed", conf:"Reporting", note:"A $4.8B campus filed with the state in October 2026, in a county of fewer than 1,000 people. Kent County noticed a tax abatement hearing in August. Construction is set for January 2027. It sits between Crusoe\'s Abilene and Childress builds, with another Crusoe complex proposed next door in Stonewall County."'),
 ('dev:"BlockchAIn Digital Infrastructure", power:"20 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"BlockchAIn Digital Infrastructure", power:"20 MW planned", water:"Not disclosed", conf:"Reporting", note:"A bitcoin mining site the company lists in its investor pipeline as in due diligence, with power targeted for late 2026. Wise County officials said in 2026 that no data center project had approached the county. Exact site not published."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 44: Crusoe Jayton ($4.8B, under 1,000 people) and BlockchAIn Wise (county not approached) checked")
