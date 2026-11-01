"""Originals batch 34: LAMP (BaRupOn, Liberty County; county was told plastics) and Cipher Milsing (Walker County)."""
import json
L = {
 "LAMP power and innovation hub": [
   ["The Vindicator: Liberty County says it was told of a plastics plant, not a data center", "https://www.thevindicator.com:443/article/2867,liberty-county-says-not-so-fast-to-accidental-data-center"],
   ["Data Center Knowledge: 2029 grid wait drives BaRupOn to build its own power", "https://www.datacenterknowledge.com/build-design/unconventional-texas-data-center-explores-off-grid-power"],
   ["Data Center Dynamics: a medical equipment maker pivots to a data center campus", "https://www.datacenterdynamics.com/en/news/medical-equipment-manufacturer-pivots-chemical-plant-to-data-center-and-manufacturing-campus/"],
   ["NANO Nuclear: feasibility study for up to 1 GW of microreactors at LAMP", "https://www.nasdaq.com/press-release/nano-nuclear-announces-1-gw-feasibility-study-barupon-llc-technology-driven-0"],
   ["Spectrum News: construction underway; gas power on site", "https://spectrumlocalnews.com/tx/austin/news/2026/05/01/liberty-energy-campus"]],
 "Cipher Milsing HPC data center": [
   ["Baxtel: Cipher's 187-acre Milsing site near Huntsville", "https://baxtel.com/data-center/cipher-digital-milsing"],
   ["Blockspace: Cipher lists Milsing (500 MW) at 2030 or later", "https://blockspace.media/insight/which-sites-will-benefit-from-cipher-digitals-2-5-gw-gas-pipeline/"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
m = d["LAMP power and innovation hub"]
m["loc"] = "Near FM 770 and County Road 182, Raywood area, Liberty County; about 6.6 miles from Trinity River National Wildlife Refuge (pin approximate)"
m["acres"] = "About 701 acres"
m["llc"] = "BaRupOn LLC (a California medical equipment maker) and its subsidiary QYK Brands LLC"
m["dates"] = "The county attorney said the county had only heard from QYK Brands about a plant making plastics for PPE, and learned of a data center from a Houston Business Journal article. BaRupOn calls itself an 'accidental data center builder.' Facing a 2029 grid wait, it is building a 240 MW gas plant and a 200,000 sq ft data center, and studied up to 1 GW of nuclear microreactors with NANO Nuclear. The area is in a federal air quality nonattainment region"
c = d["Cipher Milsing HPC data center"]
c["acres"] = "About 187 acres"
c["loc"] = "Outside Huntsville, Walker County"
c["dates"] = "Originally bought for bitcoin mining; Cipher lists 500 MW potential pending ERCOT approval, on a 2030-or-later timeline"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('{name:"LAMP power and innovation hub", county:"Liberty", type:"data", status:"announced", lat:30.06, lng:-94.8,\n   dev:"Not identified", power:"3 GW listed", water:"Not disclosed", conf:"Reporting", note:"Liberty American Multi-Sourced Power and Innovation Hub, east of Houston. Listed by the More Than Just Parks tracker; needs verification."',
  '{name:"LAMP power and innovation hub", county:"Liberty", type:"data", status:"construction", lat:30.06, lng:-94.68,\n   dev:"BaRupOn LLC (via QYK Brands LLC)", power:"240 MW gas plant being built on site; studying up to 1 GW of nuclear microreactors; the tracker lists 3 GW", water:"Company says it will not rely only on local aquifers; amount not disclosed", conf:"Reporting", note:"701 acres near Raywood. The county says it was told about a plastics plant for PPE and learned of the data center from a newspaper. The company calls itself an accidental data center builder."'),
 ('dev:"Cipher Digital", power:"500 MW listed", water:"Not disclosed", conf:"Reporting", note:"Walker County, near Huntsville. Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Cipher Digital (formerly Cipher Mining)", power:"500 MW potential, pending ERCOT approval", water:"Not disclosed", conf:"Reporting", note:"About 187 acres outside Huntsville, first bought for bitcoin mining. Cipher lists it for 2030 or later, behind its Tom Green, McLennan and McCulloch sites."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>LAMP, Liberty County</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We showed LAMP as announced with the developer not identified. It is BaRupOn LLC\'s 701-acre campus near Raywood, under construction with its own gas plant. Developer, status and pin are fixed.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 34: LAMP (BaRupOn; county was told plastics) and Cipher Milsing checked")
