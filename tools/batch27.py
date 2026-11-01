"""Originals batch 27: Beacon Point (Hut 8), Nueces County."""
import json
K = "Beacon Point"
L = [["KRIS 6: outside Robstown, no city or county permitting authority", "https://www.kristv.com/news/local-news/in-your-neighborhood/corpus-christi/calallen/beacon-point-ai-massive-data-center-planned-for-nueces-county"],
     ["Data Center Dynamics: 1 GW interconnection; first lease, 352 MW", "https://datacenterdynamics.com/en/news/hut-8-signs-352mw-data-center-lease-in-texas-with-investment-grade-tenant/"],
     ["Pulse 2.0: second $9.8B lease brings the campus to $19.6B (July 2026)", "https://pulse2.com/hut-8-secures-second-9-8-billion-ai-data-center-lease-bringing-beacon-point-contract-value-to-19-6-billion/"],
     ["BIC Magazine: construction begins, $399M first building", "https://www.bicmagazine.com/departments/AI-Infrastructure/construction-begins-on-hut-8-data-center-south-texas/"],
     ["Light Reading: cooling water to come from outside Nueces County", "https://www.lightreading.com/data-centers/hut-8-commits-to-responsible-data-center-development-following-directive-from-texas-governor-greg-abbott"],
     ["Hut 8: Beacon Point campus page", "https://www.hut8.com/data-centers/beacon-point"]]
p = "data/details.json"; d = json.load(open(p)); e = d.setdefault(K, {})
have = {u for _, u in e.get("links", [])}
e.setdefault("links", []).extend(x for x in L if x[1] not in have)
e["loc"] = "Between Robstown and Calallen, just outside Robstown city limits"
e["acres"] = "About 525 acres"
e["llc"] = "Beacon Point DC LLC (Hut 8 Corp., Miami; a former bitcoin miner); tenant unnamed, described as investment-grade"
e["incent"] = "Hut 8 declined to say whether it sought abatements; the county judge said the county could not have given one because its policy was out of date"
e["dates"] = "First 15-year, $9.8B lease (352 MW) May 2026; second identical lease July 2026 ($19.6B total, 704 MW). Construction underway: first building 657,130 sq ft, $399M, due Nov 2027. Power from AEP Texas expected Q1 2027"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
old = 'dev:"Hut 8", power:"1 GW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."'
new = 'dev:"Hut 8 (former bitcoin miner), for an unnamed big tech tenant", power:"1 GW interconnection with AEP Texas; 704 MW leased so far", water:"Company says closed-loop cooling, filled with water brought from outside Nueces County", conf:"Reporting", note:"525 acres outside Robstown, so no city or county permit was needed. Two 15-year leases worth $19.6B. Construction began in 2026; power expected early 2027."'
s = open("texas.html").read()
if new not in s:
    assert s.count(old) == 1, "Beacon Point card not found"; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 27: Beacon Point (Hut 8) checked against originals")
