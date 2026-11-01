"""Originals batch 48: CleanSpark Brazoria (land deal, not construction), NFN8 Crystal City (fire, then bankruptcy), Harlingen/Eneus (city moratorium)."""
import json
L = {
 "CleanSpark Valley Gamma": [
   ["CleanSpark: agreement to buy up to 447 acres in Brazoria County, 300 MW expandable to 600 MW (Jan 14, 2026)", "https://investors.cleanspark.com/news/news-details/2026/CleanSpark-Expands-Texas-Footprint-with-Major-Power-Acquisition-Near-Houston-to-Support-Scaled-AI-and-HPC-Development/default.aspx"],
   ["Data Center Dynamics: CleanSpark acquires 447 acres for second Texas AI site", "https://www.datacenterdynamics.com/en/news/cleanspark-acquires-447-acres-for-second-texas-ai-data-center-site/"]],
 "NFN8 Crystal City bitcoin mine": [
   ["Data Center Dynamics: NFN8 files for bankruptcy after data center fire and price crash", "https://www.datacenterdynamics.com/en/news/cryptominer-nfn8-files-for-bankruptcy-following-data-center-fire-and-bitcoin-price-crash/"],
   ["Chapter 11 Cases: filing details, 2205 Old Uvalde Highway site and fire", "https://chapter11cases.com/blogs/news/bitcoin-mining-company-nfn8-group-files-chapter-11-after-fire-cuts-capacity-in-half"],
   ["The Energy Mag: fire cut capacity and revenue by as much as half", "https://theenergymag.com/news/2026-02-09/bitcoin-nfn8-bankruptcy"]],
 "Harlingen data center": [
   ["Valley Morning Star via GovTech: Harlingen sets 120-day moratorium on data center applications", "https://www.govtech.com/artificial-intelligence/south-texas-city-sets-moratorium-amid-data-center-interest"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
c = d["CleanSpark Valley Gamma"]
c["loc"] = "Brazoria County, greater Houston region (exact site not published); pin approximate"
c["acres"] = "Up to 447 acres"
c["llc"] = "CleanSpark, Inc. (a bitcoin miner moving into AI data centers)"
c["dates"] = "Purchase agreement announced Jan 14, 2026, closing expected Q1 2026 pending utility and property approvals; company still seeking tenants"
n = d["NFN8 Crystal City bitcoin mine"]
n["loc"] = "2205 Old Uvalde Highway, Crystal City, Zavala County (leased warehouse)"
n["acres"] = "About 78,377 sq ft of leased warehouse space"
n["llc"] = "NFN8 Group, Inc. (NFN8 Capital LLC and NFN8 Holdings LLC); building owned by Midnight Enterprises, LLC"
n["dates"] = "Fire at the facility around the 2025 holidays halved mining capacity; Chapter 11 filed Feb 2, 2026 in the Western District of Texas (case 26-10193); company pursuing an asset sale"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('status:"construction", lat:29.1, lng:-95.6,\n   dev:"CleanSpark", power:"300 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'status:"announced", lat:29.1, lng:-95.6,\n   dev:"CleanSpark", power:"300 MW, expandable to 600 MW", water:"Not disclosed", conf:"Reporting", note:"A land and power deal for up to 447 acres, announced January 2026, with the company still seeking tenants. The same company built a substation in Austin County despite a county moratorium. Pin is approximate."'),
 ('dev:"NFN8 Group", power:"10 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed as suspended. Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"NFN8 Group", power:"About 10 MW", water:"Not disclosed", conf:"Reporting", note:"A bitcoin mine in a leased warehouse on Old Uvalde Highway. A fire at the site around the 2025 holidays cut the company\'s capacity in half, and NFN8 filed for bankruptcy in February 2026 and is selling its assets. A reminder to ask any developer: who pays to clean up if the company goes under?"'),
 ('note:"Residents asked the City Commission to oppose it over water and power. A public tracker lists it as blocked by a moratorium; which government acted needs verification."',
  'note:"Residents asked the City Commission to oppose it over water and power. The City of Harlingen then set a 120-day moratorium on data center applications. Fluidstack later started building outside city limits, out of the moratorium\'s reach."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>CleanSpark Brazoria County status</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We showed CleanSpark\'s Brazoria County site as under construction. CleanSpark announced an agreement to buy the land in January 2026 and is still seeking tenants; we found no construction. Status changed to announced.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 48: CleanSpark Brazoria (not built), NFN8 (fire and bankruptcy), Harlingen moratorium checked")
