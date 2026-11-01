"""Source batch 3: Google's Texas campuses and Compass. Moves Alamo Mission LLC to the Red Oak card (correction)."""
import json
L = {
 "Google Midlothian campus": [["Data Center Dynamics: Sharka LLC files for Building 4", "https://www.datacenterdynamics.com/en/news/google-files-to-build-fourth-data-center-at-midlothian-campus-in-texas"],
   ["Data Center Dynamics: fifth building filed", "https://www.datacenterdynamics.com/en/news/google-files-for-fifth-data-center-at-midlothian-campus-in-texas/"],
   ["Bisnow: $880 million expansion", "https://www.bisnow.com/dallas-ft-worth/news/data-center/google-to-expand-data-center-campus-south-of-dallas-132282"],
   ["FOX 7: which Google sites use evaporative cooling", "https://www.fox7austin.com/news/texas-data-centers-google-water-fund-stewardship-plan"]],
 "Google Red Oak campus": [["Data Center Dynamics: Google announces Red Oak (2023)", "https://datacenterdynamics.com/en/news/google-announces-plans-for-red-oak-data-center-campus-in-texas"],
   ["Data Center Knowledge / Bloomberg: the 1.46 billion gallon filing", "https://www.datacenterknowledge.com/hyperscalers/google-data-centers-secret-cost-billions-of-gallons-of-water"],
   ["Energy Capital HTX: first building operating (Nov 2025)", "https://energycapitalhtx.com/amp/google-40-billion-texas-2674298469"]],
 "Google Haskell County campuses": [["Energy Capital HTX: Google's $40 billion Texas plan", "https://energycapitalhtx.com/amp/google-40-billion-texas-2674298469"],
   ["Community Impact: three new Texas campuses, air cooled", "https://beta2.communityimpact.com/dallas-fort-worth/mckinney/business/2025/11/14/google-commits-40b-to-3-new-data-centers-infrastructure-in-texas-through-2027"]],
 "Google Armstrong County campus": [["Energy Capital HTX: Google's $40 billion Texas plan", "https://energycapitalhtx.com/amp/google-40-billion-texas-2674298469"],
   ["Community Impact: three new Texas campuses, air cooled", "https://beta2.communityimpact.com/dallas-fort-worth/mckinney/business/2025/11/14/google-commits-40b-to-3-new-data-centers-infrastructure-in-texas-through-2027"]],
 "Compass Red Oak campus": [["Data Center Dynamics: Compass's Red Oak filings and land", "https://datacenterdynamics.com/en/news/google-announces-plans-for-red-oak-data-center-campus-in-texas"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
m, r = d["Google Midlothian campus"], d.setdefault("Google Red Oak campus", {})
m["llc"] = "Sharka LLC files the campus's state building permits; occupant Design LLC"
m["comp"] = "Registered as Sharka Data Center (owner Sharka LLC; operator Google LLC; occupant Design LLC), certified Oct 1, 2018."
m["dates"] = "First building 2019; filings for Buildings 4 and 5; about $880M expansion"
r["llc"] = "Alamo Mission LLC; occupant Design LLC"
r["comp"] = "Registered as Alamo Data Center (owner Alamo Mission LLC; operator Google LLC; occupant Design LLC), certified Nov 2, 2022."
r["dates"] = "Announced 2023 ($600M); first building operating Nov 2025. Part of Google's $40B Texas plan through 2027"
for k in ("Google Haskell County campuses", "Google Armstrong County campus"):
    d[k]["dates"] = "Announced Nov 2025 in Google's $40B Texas plan; Google says the new campuses will be air cooled, using water only for site operations such as kitchens"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Google, built through shell company Alamo Mission LLC (project name Sharka)"', 'dev:"Google, through Sharka LLC"'),
 ('name:"Google Red Oak campus", county:"Ellis", type:"data", status:"operating", lat:32.550, lng:-96.840,\n   dev:"Google", power:"Not disclosed", water:"Not disclosed"',
  'name:"Google Red Oak campus", county:"Ellis", type:"data", status:"operating", lat:32.550, lng:-96.840,\n   dev:"Google, through Alamo Mission LLC", power:"Not disclosed", water:"Up to 1.46 billion gallons a year sought in a 2020 legal filing, about 4 million gal/day (Bloomberg)"'),
 ('link:"/ellis/", src:"Energy Capital HTX; Dallas Morning News"}', 'link:"/ellis/", src:"Energy Capital HTX; Dallas Morning News; Bloomberg via Data Center Knowledge; Data Center Dynamics"}'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:70]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Google\'s shell companies in Ellis County</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We listed Alamo Mission LLC as the company behind Google\'s Midlothian campus. State building filings tie Midlothian to Sharka LLC, and Alamo Mission LLC is tied to Google\'s Red Oak campus, both in the Comptroller\'s records and in a 2020 water filing. Moved to the right cards, with sources.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 3: 5 cards linked, Google's shell companies sorted, 1 correction logged")
