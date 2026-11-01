"""Originals batch 29: Reeves County. Project Kilby (Chevron/Microsoft) and the 'Solar Data Ranch' (LandBridge/NRG, a gas plant)."""
import json
L = {
 "Project Kilby": [
   ["Galveston Daily News: Chevron's Energy Forge One; brackish groundwater for the plant", "https://www.galvnews.com/chevron-microsoft-deal-fuels-west-texas-data-center-expansion/article_6d04dac1-eacd-443f-8e59-f3ba1887248e.html"],
   ["Quartz: 2,000+ acres near Pecos; off-grid by design; power from late 2028", "https://qz.com/chevron-microsoft-natural-gas-data-center-west-texas-062226"],
   ["Washington Examiner: construction not started; Reeves County judge welcomes it", "https://washingtonexaminer.com/policy/technology/4618489/chevron-agreement-microsoft-power-texas-data-center-natural-gas"],
   ["Journal of Petroleum Technology: 2.67 GW, built in phases", "https://jpt.spe.org/chevron-strikes-deal-with-microsoft-to-power-ai-for-20-years"]],
 "Reeves County Solar Data Ranch": [
   ["POWER Magazine: LandBridge and NRG strike a 1.1 GW gas-fired deal in Reeves County", "https://www.powermag.com/tag/ercot"],
   ["TipRanks/The Fly: LandBridge and NRG agreement on a potential data center site", "https://www.tipranks.com/news/the-fly/landbridge-enters-pact-with-nrg-energy-to-power-potential-texas-data-center-thefly"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
k = d["Project Kilby"]
k["loc"] = "Near Pecos, Reeves County (exact site not published)"
k["acres"] = "More than 2,000 acres"
k["llc"] = "Energy Forge One LLC (Chevron subsidiary), with Joulent (Engine No. 1) holding an option on half; power sold to Microsoft for 20 years"
k["dates"] = "20-year agreement announced June 22, 2026; construction not yet started; Chevron expects a final investment decision by the end of 2026; first power targeted for 2028, with Microsoft adding about 2 GW over five to seven years"
r = d["Reeves County Solar Data Ranch"]
r["llc"] = "LandBridge (landowner) with NRG Energy"
r["dates"] = "Agreement announced Sept 2025 for a 1.1 GW gas-fired plant to power a hyperscale data center; could run by late 2029 if approved"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Chevron and Microsoft", power:"2.7 GW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Chevron (Energy Forge One LLC), selling power to Microsoft", power:"2.67 GW gas plant built on site, off the grid; Microsoft data center about 2 GW", water:"Chevron says the power plant will use brackish groundwater, not fresh water; data center water not disclosed", conf:"Reporting", note:"A 20-year deal announced June 2026 for 2,000+ acres near Pecos. Construction has not started; Chevron decides by the end of 2026. First power targeted for 2028."'),
 ('dev:"Not identified", power:"1.1 GW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"LandBridge with NRG Energy", power:"1.1 GW natural gas plant (despite the solar-sounding name)", water:"Not disclosed", conf:"Reporting", note:"NRG would build a gas plant on LandBridge land in the Delaware Basin to power a hyperscale data center; could run by late 2029. LandBridge also owns the Alpha Digital Campus land."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Reeves County "Solar Data Ranch"</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We showed this with the developer not identified, under a name that suggests solar. It is LandBridge and NRG Energy\'s plan for a 1.1 GW natural gas plant to power a data center. The developer and power source are now shown.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 29: Project Kilby and the Reeves 'Solar Data Ranch' (a gas plant) checked")
