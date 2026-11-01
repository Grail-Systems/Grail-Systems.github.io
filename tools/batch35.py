"""Originals batch 35: Kahla Project (Leon County). Belltown Power first, now Crusoe; tax break rejected; residents organized."""
import json
K = "Kahla Project (Marquez)"
L = [["KXXV: commissioners reject Crusoe's initial tax break application; 200+ residents attend", "https://www.kxxv.com/news/local-news/data-centers-controversy/leon-county-commissioners-reject-initial-tax-break-application-for-crusoe-technologies-data-center"],
     ["KBTX: Leon County bracing for a 1,500 MW data center (Dec 2025)", "https://kbtx.com/2025/12/24/leon-county-bracing-1500-megawatt-data-center"],
     ["KXXV: Belltown Power proposes the Kahla Project; residents organize", "https://www.kxxv.com/news/local-news/in-your-neighborhood/leon-county-residents-oppose-proposed-1-500-megawatt-data-center-project"],
     ["KXXV: three proposed data centers in Leon County", "https://www.kxxv.com/news/local-news/in-your-neighborhood/leon-county/fighting-back-against-big-data-leon-county-residents-opposing-three-proposed-data-centers"],
     ["KXXV: commissioners table moratorium talks", "https://www.kxxv.com/news/local-news/in-your-neighborhood/leon-county/development-discussions-no-moratorium-for-leon-county-but-for-residents-the-fight-continues"],
     ["Know Leon County podcast: how residents found the projects", "https://www.audible.it/pd/B0GJYWPRJR"]]
p = "data/details.json"; d = json.load(open(p)); e = d.setdefault(K, {})
have = {u for _, u in e.get("links", [])}
e.setdefault("links", []).extend(x for x in L if x[1] not in have)
e["loc"] = "Private land near Marquez and Jewett, Leon County; one family's land is about a quarter mile away"
e["llc"] = "First proposed by Belltown Power; now Crusoe Technologies. Energy Renewal Partners asked Texas Parks and Wildlife to review the site"
e["incent"] = "Leon County commissioners rejected Crusoe's initial tax break application"
e["dates"] = "Residents learned of it in late 2025; the county judge said he was unsure what the county could do. More than 200 residents packed meetings in Jewett and at the county annex. Commissioners rejected the initial tax break application and tabled a moratorium. Two more data centers have been proposed near Oakwood and Jewett"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
old = 'dev:"Crusoe", power:"1.5 GW listed", water:"Not disclosed", conf:"Reporting", note:"East Texas, between Centerville and Bremond. Listed by the More Than Just Parks tracker; needs verification."'
new = 'dev:"Crusoe Technologies (first proposed by Belltown Power)", power:"1.5 GW", water:"Not disclosed", conf:"Reporting", note:"A $34B campus near Marquez, between Centerville and Bremond. After 200+ residents packed the room, Leon County commissioners rejected Crusoe\'s initial tax break application. Residents organized fast, including a local podcast; two more data centers are proposed in the county."'
s = open("texas.html").read()
if new not in s:
    assert s.count(old) == 1, "Kahla card not found"; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 35: Kahla Project (Crusoe, Leon County) checked against originals")
