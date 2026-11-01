"""Source batch 5: DataBank and Cawley (Ellis), Core Scientific and CoreWeave (Denton, likely one site)."""
import json
L = {
 "DataBank Red Oak campus": [["TDLR: DFW9 filing, $256 million", "https://www.tdlr.texas.gov/TABS/Search/Project/TABS2024020821"],
   ["Data Center Dynamics: $2 billion loan and 400 MW substation", "https://www.datacenterdynamics.com/en/news/databank-secures-2bn-construction-financing-for-dallas-data-centers"],
   ["Dallas Innovates: Oracle is the tenant", "https://dallasinnovates.com/?p=286676"]],
 "Cawley Partners data center park": [["Cawley Partners: South Creek Ranch purchase (Apr 29, 2025)", "https://www.cawleypartners.com/post/press-release-cawley-partners-acquires-south-creek-ranch-honoring-a-legacy-and-shaping-the"],
   ["Data Center Dynamics: plans for a data center park", "https://www.datacenterdynamics.com/en/news/cawley-partners-acquires-5200-acres-outside-dallas-plans-data-center-park/"],
   ["FOX 4: what it means for Ferris", "https://www.fox4news.com/news/massive-new-land-development-city-ferris"]],
 "Core Scientific Denton": [["CoStar: the $6.1 billion conversion to AI", "https://www.costar.com/article/394849102"],
   ["Government Technology / Dallas Morning News: Denton approvals, 8171 Jim Christal Rd", "https://www.govtech.com/artificial-intelligence/4b-bitcoin-to-ai-data-center-project-eyed-in-denton-texas"],
   ["The Energy Mag: CoreWeave deploys GPUs for OpenAI (Jan 2026)", "https://theenergymag.com/news/2026-01-14/coreweave-gpu-openai"]],
 "CoreWeave Denton AI data center": [["The Energy Mag: CoreWeave at Core Scientific's Denton site", "https://theenergymag.com/news/2026-01-14/coreweave-gpu-openai"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
d["DataBank Red Oak campus"]["dates"] = "TDLR: DFW9, Stainback Rd, $256M, Sept 2024 to Feb 2027; DFW14, 3600 Batchler Rd, $325M, start Dec 1, 2026. $2B loan for the first three buildings (Apr 2026); first phase served by a 400 MW Oncor substation. Oracle is the tenant"
c = d.setdefault("Cawley Partners data center park", {})
c["loc"] = "South Creek Ranch, in the Ferris area, straddling the Dallas and Ellis county line along I-45 and the future Loop 9"
c["dates"] = "Bought Apr 2025. Cawley says the first 2,000 acres, on the north end, will become data center parks"
cs = d["Core Scientific Denton"]
cs["loc"] = "8171 Jim Christal Rd, Denton, next to the city-owned Denton Energy Center"
cs["dates"] = "Built for bitcoin mining in 2021; construction stopped during Core Scientific's 2022 bankruptcy. Now being converted to AI for CoreWeave, which leases it to OpenAI; Core Scientific put the cost at up to $6.1B. Weather delayed the build; GPUs began going in Jan 2026"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('name:"Cawley Partners data center park", county:"Ellis (to verify)", type:"data", status:"announced", lat:32.450, lng:-96.750,\n   dev:"Cawley Partners", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"About 5,200 acres south of Dallas, acquired 2025.", link:"/ellis/", src:"Baxtel"}',
  'name:"Cawley Partners data center park", county:"Ellis (straddles the Dallas County line)", type:"data", status:"announced", lat:32.534, lng:-96.666,\n   dev:"Cawley Partners (Dallas)", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"South Creek Ranch, about 5,200 acres near Ferris, bought in April 2025. Cawley says the first 2,000 acres will become data center parks.", link:"/ellis/", src:"Cawley Partners; Data Center Dynamics; FOX 4"}'),
 ('dev:"Core Scientific", power:"Not confirmed", water:"Not confirmed", conf:"Reporting",\n   note:"Bitcoin mining site shifting toward AI hosting.", src:"CoinShares"}',
  'dev:"Core Scientific; tenant CoreWeave, which leases it to OpenAI", power:"Not confirmed", water:"Not confirmed", conf:"Reporting",\n   note:"A bitcoin mine being converted into an AI data center, at a cost Core Scientific put at up to $6.1B. The state lists CoreWeave as the occupant.", src:"CoStar; Dallas Morning News via Government Technology; The Energy Mag; Texas Comptroller"}'),
 ('dev:"CoreWeave", power:"394 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"CoreWeave", power:"394 MW listed (not confirmed)", water:"Not disclosed", conf:"Reporting", note:"This appears to be the same site as Core Scientific Denton, which CoreWeave leases. We are keeping both cards until a record settles it; see that card for details."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:70]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Denton: likely one site, two cards</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>The map shows Core Scientific Denton and a CoreWeave Denton AI data center as separate projects. Reporting indicates CoreWeave is the tenant at Core Scientific\'s Denton site, so these are likely the same place. Both cards now say so, and the 394 MW figure on the CoreWeave card is marked unconfirmed.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 5: 4 cards linked and filled in; Denton duplicate flagged")
