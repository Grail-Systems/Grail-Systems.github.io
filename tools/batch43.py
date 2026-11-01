"""Originals batch 43: CyrusOne Jack County. Beside Vistra's gas plant on Hwy 199 at the Wise County line; pin was in Jacksboro."""
import json
K = "CyrusOne Jack County campus"
L = [
 ["CyrusOne: Jack County project page (land next to the Vistra power plant)", "https://www.cyrusone.com/data-centers/north-america/jack-county-tx"],
 ["Jacksboro Herald-Gazette: county to consider tax abatement; reinvestment zone of 485 to 940 acres", "https://www.jacksboronewspapers.com/news/county-consider-tax-abatement-data-center-0"],
 ["Jacksboro Herald-Gazette: locals look for answers at CyrusOne meeting (May 28, 2026)", "https://www.jacksboronewspapers.com/news/locals-look-answers-cyrusone-meeting"],
 ["Jacksboro Herald-Gazette: hearing rescheduled to July 27, moved to a bigger courtroom", "https://www.jacksboronewspapers.com/news/hearing-rescheduled-july"],
 ["Wise County Messenger: neighboring county asks the state for a special session; 200,000-gallon water claim questioned", "https://www.wcmessenger.com/articles/commissioners-call-for-state-action-on-data-center-development"],
]
p = "data/details.json"; d = json.load(open(p))
e = d.setdefault(K, {}); have = {u for _, u in e.get("links", [])}
e.setdefault("links", []).extend(x for x in L if x[1] not in have)
e["loc"] = "Southeastern Jack County, south of State Highway 199 near County Road 3940 and East Gibtown Road, at the Wise County line, next to Vistra's existing power plant"
e["acres"] = "Abatement covers about 250 acres for the first phase; reinvestment zone 485 to 940 acres; a 453-acre property registered to NCA Holdings"
e["llc"] = "C1 Jack I LLC (CyrusOne)"
e["dates"] = "Abatement application filed Jan 2026; community meeting May 28, 2026; June 8 hearing postponed to July 27 and moved to the district courtroom for the crowd. Outcome not yet confirmed here"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('{name:"CyrusOne Jack County campus", county:"Jack", type:"data", status:"announced", lat:33.22, lng:-98.16,\n   dev:"CyrusOne", power:"144 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  '{name:"CyrusOne Jack County campus", county:"Jack", type:"data", status:"announced", lat:33.16, lng:-97.92,\n   dev:"CyrusOne (C1 Jack I LLC)", power:"144 MW in the first phase", water:"Company says closed-loop cooling with a one-time fill of 200,000 gallons; Wise County residents questioned that figure", conf:"Reporting", note:"A $600M first phase beside Vistra\'s gas plant on Hwy 199 at the Wise County line. The crowd was big enough that the county moved its hearing to the district courtroom, and neighboring Wise County asked the state for a special session on data centers. This is CyrusOne\'s pattern in Texas: Freestone, Bosque, Jack, and now Sulphur Springs all pair a data center with a gas plant."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>CyrusOne Jack County pin</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>The CyrusOne pin sat in Jacksboro. The site is in southeastern Jack County off Highway 199 at the Wise County line, next to Vistra\'s power plant, about 15 miles east. The pin has been moved; the exact parcel is approximate.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 43: CyrusOne Jack County (beside a gas plant; pin moved from Jacksboro) checked")
