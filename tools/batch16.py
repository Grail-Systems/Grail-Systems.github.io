"""Originals batch 16: CloudHQ SAT (map pin moved) and Microsoft's San Antonio campuses."""
import json
L = {
 "CloudHQ SAT Campus": [
   ["CloudHQ: SAT campus, up to 600 MW in five buildings", "https://cloudhq.com/campus/sat-campus/"],
   ["Data Center Dynamics: CloudHQ buys about 123 acres from the UT System", "https://datacenterdynamics.com/en/news/cloudhq-acquires-more-than-120-acres-of-land-in-san-antonio-texas"]],
 "Microsoft South Central Campus": [
   ["Data Center Dynamics: Microsoft's San Antonio sites and the Castroville campus", "https://www.datacenterdynamics.com/en/news/microsoft-files-for-data-center-campus-outside-san-antonio"],
   ["Data Center Dynamics: SAT46 and the 158-acre Texas Research Park campus", "https://datacenterdynamics.com/en/news/microsoft-to-build-another-data-center-in-san-antonio-texas"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
c = d["CloudHQ SAT Campus"]
c["loc"] = "15255 Lambda Drive, Texas Research Park, west San Antonio, across from Microsoft's campus (former UT Health Science Center land)"
c["acres"] = "About 123 acres, bought from the University of Texas System in 2023"
c["dates"] = "Land bought June 2023; company lists the campus as ready for service within 2027"
m = d["Microsoft South Central Campus"]
m["loc"] = "Several west San Antonio sites: 15000 Lambda Drive (158 acres, Texas Research Park), 3545 Wiseman Blvd, 3555 Westover Link, 5200 Rogers Road; plus a separate campus in Castroville (Medina County)"
m["dates"] = "First San Antonio data center opened 2008; repeated expansions filed with the state since"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('{name:"CloudHQ SAT Campus", county:"Bexar", type:"data", status:"announced", lat:29.45, lng:-98.4,\n   dev:"CloudHQ", power:"600 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  '{name:"CloudHQ SAT Campus", county:"Bexar", type:"data", status:"announced", lat:29.417, lng:-98.798,\n   dev:"CloudHQ", power:"Up to 600 MW of computing load in five buildings (company figure)", water:"Not disclosed", conf:"Reporting", note:"About 123 acres in the Texas Research Park, bought from the UT System in 2023, across the street from Microsoft. CloudHQ says it will be ready for tenants within 2027."'),
 ('dev:"Microsoft", power:"450 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Microsoft", power:"The tracker lists 450 MW; Microsoft has not published a figure", water:"Not disclosed", conf:"Reporting", note:"Microsoft\'s Azure hub since 2008, now spread across several west San Antonio sites, including 158 acres in the Texas Research Park, with a further campus in Castroville."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>CloudHQ map pin</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>The pin for CloudHQ\'s San Antonio campus sat about 25 miles east of the real site. The campus is on Lambda Drive in the Texas Research Park, on the west side, across from Microsoft. The pin has been moved.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 16: CloudHQ (pin moved) and Microsoft San Antonio checked against originals")
