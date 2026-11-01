"""Originals batch 30: Cipher Colchis (Tom Green; pin moved) and PowerPlay AI / Sharon AI (Abilene area)."""
import json
L = {
 "Cipher Colchis Project": [
   ["KKSA: 1 GW data center proposed near US 67 North and City Farm Road (Sept 22, 2026)", "https://www.kksa-am.com/2026/09/22/massive-1-gigawatt-data-center-proposed-near-san-angelo-heres-what-we-know/"],
   ["Cipher: Colchis joint venture and 1 GW direct-connect agreement with AEP", "https://www.nasdaq.com/press-release/cipher-mining-provides-third-quarter-2025-business-update-2025-11-03"],
   ["San Angelo LIVE: Colchis sits about 2,500 feet from the Skybox/Emergent site", "https://sanangelolive.com/news/business/2026-06-19/how-steve-ahlenius-took-tough-controversies-and-revived-san-angelos-chamber"],
   ["San Angelo LIVE: Cipher wants 1 GW, Emergent 1.2 GW; local power may not cover both", "https://sanangelolive.com/news/politics/2026-06-22/recall-san-angelos-mayor-fails"]],
 "Greater Abilene gas-powered data center": [
   ["Data Center Dynamics: PowerPlay AI and Sharon AI plan 400 MW; little known about PowerPlay", "https://www.datacenterdynamics.com/en/news/powerplay-ai-sharon-ai-plan-400mw-behind-the-meter-gas-powered-data-center-in-abilene-texas/"],
   ["BIC Magazine: an unincorporated site free of zoning", "https://www.bicmagazine.com/departments/AI-Infrastructure/powerplay-ai-announces-texas-ai-data-center/"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
c = d["Cipher Colchis Project"]
c["loc"] = "Private land near U.S. 67 North and City Farm Road, northeast of San Angelo, about 2,500 feet from the Skybox/Emergent site (pin approximate)"
c["acres"] = "About 620 acres"
c["llc"] = "Cipher Digital (formerly Cipher Mining), about 95% owner of the Colchis joint venture"
c["dates"] = "Announced Nov 2025 with a 1 GW direct-connect agreement with AEP; ERCOT gave 1 GW conditional base-load status; Cipher also plans gas pipelines for on-site generation. First public presentation to Tom Green County commissioners Sept 2026; power targeted for 2028"
a = d["Greater Abilene gas-powered data center"]
a["loc"] = "Unincorporated land in the greater Abilene area (exact site not published)"
a["llc"] = "PowerPlay AI (new company; one disclosed executive, Luke Velterop) in a joint venture with Sharon AI (Australian neocloud, founded 2024)"
a["dates"] = "Announced July 20, 2026; still negotiating gas supply and choosing a power producer; 400 MW targeted for 2028. Sharon AI earlier dropped out of a Texas Critical Data Centers project"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('{name:"Cipher Colchis Project", county:"Tom Green", type:"data", status:"announced", lat:31.3, lng:-100.45,\n   dev:"Cipher Digital", power:"1 GW listed", water:"Not disclosed", conf:"Reporting", note:"Tom Green County dropped its own moratorium plans after the Hill County lawsuit. Listed by the More Than Just Parks tracker; needs verification."',
  '{name:"Cipher Colchis Project", county:"Tom Green", type:"data", status:"announced", lat:31.50, lng:-100.38,\n   dev:"Cipher Digital (formerly Cipher Mining)", power:"1 GW, with a direct-connect agreement with AEP; ERCOT gave conditional approval", water:"Not disclosed", conf:"Reporting", note:"Cipher\'s largest site: about 620 acres northeast of San Angelo, next door to a separate 1.2 GW Skybox/Emergent proposal. Tom Green County dropped its own moratorium plans after the Hill County lawsuit."'),
 ('dev:"PowerPlay AI / Sharon AI", power:"400 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"PowerPlay AI and Sharon AI (joint venture)", power:"400 MW from an on-site gas plant (behind the meter), targeted for 2028", water:"Not disclosed", conf:"Reporting", note:"Pitched as an unincorporated site free of zoning. PowerPlay is a new company with one disclosed executive, from hydrogen exploration; it has not yet secured gas or a power producer."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Cipher Colchis map pin</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>The Colchis pin sat south of San Angelo. Reporting places the site near U.S. 67 North and City Farm Road, northeast of the city, next to the Skybox/Emergent proposal. The pin has been moved; the exact parcel is not published.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 30: Cipher Colchis (pin moved) and PowerPlay AI Abilene checked")
