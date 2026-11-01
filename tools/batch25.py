"""Originals batch 25: Medina County. Cinco is Rowan's campus near Lytle (developer and pin fixed); Tract Medina."""
import json
L = {
 "Cinco data center": [
   ["Rowan: groundbreaking at Cinco, minimum $900M (Aug 7, 2025)", "https://rowan.digital/?p=1150"],
   ["Rowan: $550M construction financing (Feb 11, 2026)", "https://rowan.digital/?p=1222"],
   ["Data Center Dynamics: Lytle and Medina County approved it unanimously", "https://www.datacenterdynamics.com/en/news/rowan-digital-breaks-ground-on-300mw-data-center-campus-outside-san-antonio-texas/"],
   ["Quinbrook (Rowan's owner): Cinco offers up to 1 GW from 2026 to 2030", "https://www.quinbrook.com/?p=3994"]],
 "Tract Medina Technology Park": [
   ["Baxtel (Cinco listing): notes Tract's 265-acre Medina Technology Park nearby", "https://baxtel.com/data-center/rowan-cinco-tx"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
c = d["Cinco data center"]
c["loc"] = "State Highway 132 at County Road 683, near Lytle and the Coal Mine neighborhood, just north of I-35 (pin approximate)"
c["acres"] = "About 440 acres"
c["llc"] = "Rowan Cinco LLC (Rowan Digital Infrastructure, owned by Quinbrook Infrastructure Partners)"
c["dates"] = "Open house Mar 2025; Lytle City Council and Medina County commissioners approved all applications unanimously; ground broken Aug 2025; $550M construction loan Feb 2026; first phase due 2027"
t = d["Tract Medina Technology Park"]
t["acres"] = "About 265 acres, with an expansion parcel"
t["loc"] = "Medina County, west of San Antonio, about 11 miles from Rowan's Cinco campus"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('{name:"Cinco data center", county:"Medina", type:"data", status:"announced", lat:29.3, lng:-98.95,\n   dev:"Not identified", power:"300 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  '{name:"Cinco data center", county:"Medina", type:"data", status:"construction", lat:29.25, lng:-98.78,\n   dev:"Rowan Digital Infrastructure (owned by Quinbrook)", power:"300 MW in the first phase; the owner lists up to 1 GW by 2030", water:"Not disclosed", conf:"Reporting", note:"A $900M+ campus on about 440 acres near Lytle, under construction since Aug 2025 with a $550M loan. Lytle and Medina County approved it unanimously. Same developer as Rowan Temple."'),
 ('dev:"Tract", power:"500 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Tract", power:"The tracker lists 500 MW; not confirmed elsewhere", water:"Not disclosed", conf:"Reporting", note:"About 265 acres west of San Antonio, with an expansion parcel. Tract sells powered land to data center operators; no tenant named. Same company as Applewhite in south San Antonio."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Cinco, Medina County</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We showed Cinco as announced, developer not identified, pinned west of Castroville. It is Rowan Digital Infrastructure\'s campus near Lytle, under construction since Aug 2025. Developer, status and pin are fixed.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 25: Cinco is Rowan near Lytle (under construction); Tract Medina checked")
