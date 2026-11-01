"""Batch 20: new card for Blueprint Projects Data Center in Taylor (deeded parkland; AG investigation)."""
import json
K = "Blueprint Projects data center (Taylor parkland)"
L = [["Texas Attorney General: investigation announced (Sept 17, 2026)", "https://www.texasattorneygeneral.gov/news/releases/attorney-general-paxton-investigates-ai-data-center-development-taylor-over-potential-misuse-land"],
     ["KERA/KUT: the 1999 deed held the land in trust for a park", "https://www.keranews.org/texas-news/2026-09-17/attorney-general-data-center-taylor-tx"],
     ["Texas Scorecard: 60 MW, to be powered by 2027", "https://texasscorecard.com/local/paxton-begins-investigation-into-planned-data-center-in-taylor/"],
     ["Austin Free Press: residents want a court order to pause work", "https://austinfreepress.org/misdeeds-paxton/"],
     ["Fox 7: neighbors sue to stop the project", "https://www.fox7austin.com/news/taylor-residents-fight-sale-property-tech-developer"]]
p = "data/details.json"; d = json.load(open(p)); e = d.setdefault(K, {})
have = {u for _, u in e.get("links", [])}
e.setdefault("links", []).extend(x for x in L if x[1] not in have)
e["loc"] = "Carlos G. Parker Blvd, between Martin Luther King Blvd and the railroad tracks, Taylor (pin approximate)"
e["acres"] = "87-acre tract; the data center plan covers about 52 acres"
e["llc"] = "NCP Travis TPP Project, LLC (Delaware), for Blueprint Projects Data Centers"
e["dates"] = "1999: the Bland family deeded the land for $10 to the Texas Parks and Recreation Foundation, to be held in trust for future use as parkland. Apr 2025: the Taylor Economic Development Corp. sold it to Blueprint for $10M. 2025: neighbors led by Pamela Griffin sued. Sept 17, 2026: the Attorney General opened an investigation"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
anchor = 'campus this year.", src:"More Than Just Parks data center tracker"},\n'
card = ('  {name:"' + K + '", county:"Williamson", type:"data", status:"approved", lat:30.58, lng:-97.42,\n'
        '   dev:"Blueprint Projects Data Centers (NCP Travis TPP Project, LLC)", power:"About 60 MW, with an on-site substation; power expected 2027", water:"Not disclosed", conf:"Reporting", note:"Three buildings totaling 135,000 sq ft on land a family deeded in 1999 to be held for a public park. The city\'s development corporation sold it for $10M in 2025. Neighbors sued, and the Attorney General opened an investigation in Sept 2026.", src:"Texas Attorney General; KUT; Texas Scorecard; Fox 7"},\n')
s = open("texas.html").read()
if K not in s:
    assert s.count(anchor) == 1, "anchor not found"; s = s.replace(anchor, anchor + card)
open("texas.html", "w").write(s)
print("Batch 20: Blueprint Taylor parkland card added")
