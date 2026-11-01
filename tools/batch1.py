"""Source batch 1: East Texas and Hood County cards. Adds direct links, fixes the Tyler card, logs the correction."""
import json
E = "https://www.ercot.com/mp/data-products/data-product-details?id=PG7-200-ER"
L = {
 "Longleaf II Power Station": [["ERCOT interconnection queue (GIS report)", E]],
 "Sun Angel ESS": [["ERCOT interconnection queue (GIS report)", E]],
 "Project Red and Project Yellow": [["KERA: judge dismisses the developers' suit (July 20, 2026)", "https://www.keranews.org/energy-environment/2026-07-20/hood-county-judge-dismisses-lawsuit-seeking-automatic-approval-of-proposed-data-centers"],
   ["Texas Scorecard: commissioners raise a MARA connection", "https://texasscorecard.com/local/hood-county-commissioners-postpone-further-action-on-two-data-center-projects/"]],
 "Bon Wier Innovation Park": [["KJAS: owner's statement (July 31, 2026)", "https://www.kjas.com/news/local_news/article_320d483f-d7ee-4e47-81e0-87197298bb82.html"],
   ["LoopNet sale listing", "https://www.loopnet.com/Listing/Hwy-363-FM-363-US-HWY-190-Bon-Wier-TX/35440620"],
   ["Area Development: 2022 biorefinery announcement", "https://www.areadevelopment.com/newsitems/2-16-2022/usa-bioenergy-bon-wier-texas.shtml"]],
 "Tyler bitcoin mine rezoning": [["KLTV: Planning and Zoning denies the permit (July 7, 2026)", "https://www.kltv.com/2026/07/07/tyler-planning-commission-denies-permit-proposed-data-center/"],
   ["Data Center Dynamics: site and vote details", "https://www.datacenterdynamics.com/en/news/tyler-texas-rejects-bitcoin-mining-data-center/"],
   ["KLTV: appeal rejected, legal fight continues (Sept 3, 2026)", "https://www.kltv.com/video/2026/09/03/proposed-tyler-data-center-faces-major-setback-legal-battle-continues/"]],
 "Hedgehog USA powered land campus": [["PR Newswire: Hedgehog and Idemitsu gas supply deal (July 21, 2026)", "https://www.prnewswire.com/news-releases/hedgehog-usa-signs-strategic-energy-supply-agreement-with-idemitsu-to-advance-powered-land-data-center-platform-in-texas-302830149.html"],
   ["More Than Just Parks tracker entry", "https://morethanjustparks.com/data-center-tracker/hedgehog-usa-powered-land-campus-navarro-county-tx--70109c07-a39e-4bfb-8ca3-e2eeadbdf725"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Not identified", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"The City of Tyler denied a rezoning near downtown for a bitcoin mining facility in July 2026.", src:"Tyler Morning Telegraph"}',
  'dev:"Vulcan Core LLC", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"Vulcan Core sought a special use permit for a bitcoin mine on 1.92 acres at 1101 and 1105 W. Erwin St., near downtown. The Planning and Zoning Commission denied it 5 to 2 on July 7, 2026. A city board later rejected Vulcan Core\'s appeal over a missed deadline, but KLTV reported in September that a legal fight continues.", src:"KLTV (July 7 and Sept. 3, 2026); KETK; Data Center Dynamics"}'),
 ('dev:"Not identified in reporting", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"Developers sued Hood County for automatic approval',
  'dev:"Starwood, according to the projects\' attorney. Commissioners raised a MARA Holdings connection, which he said was a separate company", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"Developers sued Hood County for automatic approval'),
 ('link:"/hood/", src:"KERA (July 20, 2026); Fort Worth Weekly"}', 'link:"/hood/", src:"KERA (July 20, 2026); Texas Scorecard; Fort Worth Weekly"}'),
 ('dev:"Hedgehog USA", power:"600 MW listed", water:"Not disclosed", conf:"Reporting", note:"Same county as Riot Corsicana. Needs verification.", link:"/navarro/", src:"More Than Just Parks data center tracker"}',
  'dev:"Hedgehog USA (Plano; CEO Jeff Barber)", power:"Up to 600 MW by the end of 2027, on natural gas", water:"Not disclosed", conf:"Reporting", note:"Hedgehog announced a long-term gas supply deal with Idemitsu in July 2026. The same release says Marathon Capital is advising on the sale of 100% of the project, so the company that builds here may not be Hedgehog.", link:"/navarro/", src:"Hedgehog USA release (PR Newswire, July 21, 2026); More Than Just Parks data center tracker"}'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:70]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Tyler bitcoin mine</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We said the City of Tyler denied a rezoning and that the developer was not identified. It was the Planning and Zoning Commission, voting 5 to 2 on Vulcan Core LLC\'s special use permit request, and KLTV reports a legal fight over the denial continues. Corrected, with sources linked.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 1: 6 cards linked, 3 cards updated, 1 correction logged")
