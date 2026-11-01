"""Originals batch 36: Project Aggie (College Station rejected the land sale) and Project Eagle (Amazon, Boling; county NDA)."""
import json
L = {
 "Project Aggie": [
   ["Data Center Dynamics: College Station rejects the land sale", "https://www.datacenterdynamics.com/en/news/college-station-texas-rejects-land-sale-for-data-center/"],
   ["Data Center Dynamics: the 600 MW plan, two 300 MW substations", "https://www.datacenterdynamics.com/en/news/600mw-data-center-campus-proposed-in-texas/"]],
 "Project Eagle (AWS)": [
   ["Data Center Dynamics: AWS files for Project Eagle near Boling", "https://www.datacenterdynamics.com/en/news/aws-files-for-12bn-data-center-campus-outside-houston-texas/"],
   ["CRE Daily: $10B, 3,000 acres; county signed an NDA with Amazon's consultant", "https://www.credaily.com/?p=221377"],
   ["BIC Magazine: four buildings filed; could be the largest campus in Texas", "https://www.bicmagazine.com/departments/AI-Infrastructure/amazon-data-center-plans-advance-near-boling-texas/"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
a = d["Project Aggie"]
a["loc"] = "Midtown Business Park, Midtown Drive and Corporate Parkway, College Station (city-owned land)"
a["acres"] = "About 200 acres"
a["llc"] = "PPM Data LLC (Priority Power Management, backed by I Squared Capital)"
a["dates"] = "Proposed Sept 2025 as a 600 MW campus with two 300 MW substations; the College Station City Council rejected selling the city land amid strong opposition, which ended the project at this site"
g = d["Project Eagle (AWS)"]
g["loc"] = "240 to 258 Eaglewood Road, near FM 1301 and FM 442, Boling, Wharton County (a town of under 400 people; pin approximate)"
g["acres"] = "About 2,700 to 3,000 acres"
g["llc"] = "Amazon Data Services; Wharton County officials signed a nondisclosure agreement with VisionFirst Advisors, a consultant that has worked with Amazon"
g["dates"] = "Four buildings (A to D) filed with the state in July 2026, six more (E to K) in Aug 2026; site work underway, more county permits needed; target 2027"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Priority Power Management", power:"600 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed as canceled. Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Priority Power Management (PPM Data LLC), backed by I Squared Capital", power:"600 MW planned, with two 300 MW substations", water:"Not disclosed", conf:"Reporting", note:"Planned on about 200 acres of city land in College Station\'s Midtown Business Park. Amid strong opposition, the City Council refused to sell the land, which stopped the project there."'),
 ('{name:"Project Eagle (AWS)", county:"Wharton", type:"data", status:"construction", lat:29.31, lng:-96.1,\n   dev:"Amazon Web Services", power:"Campus; size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  '{name:"Project Eagle (AWS)", county:"Wharton", type:"data", status:"construction", lat:29.27, lng:-95.95,\n   dev:"Amazon (Amazon Data Services)", power:"10 buildings; size not disclosed", water:"Not disclosed", conf:"Reporting", note:"A $10B campus on about 3,000 acres near Boling, a town of under 400. Ten buildings filed with the state in 2026. County officials signed an NDA with Amazon\'s consultant, which limits what the public is told. Could become the largest data center campus in Texas."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 36: Project Aggie (land sale refused) and Project Eagle (Amazon, county NDA) checked")
