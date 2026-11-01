"""The cards my case-sensitive check missed: Fort Bliss, Alpha Digital, Old Ocean, FO Permian, Glass Mountains, JMG Conroe, Glen Rose; and Fort Spunky's wording (map and Hood page)."""
import json
L = {
 "Fort Bliss data center": [
   ["Bisnow: Army taps Carlyle for 1,384 acres at Fort Bliss, 2.5 to 3 GW", "https://www.bisnow.com/news/national/data-center-development/us-army-data-center-kkr-cyrusone-carlyle-133840"],
   ["El Paso Matters via WTOP: would use more power than all of El Paso; water from wells on the Hueco Bolson", "https://wtop.com/national/2026/05/proposed-fort-bliss-data-center-could-use-more-power-than-all-of-el-paso/"],
   ["Data Center Dynamics: Army selects Carlyle and CyrusOne", "https://www.datacenterdynamics.com/en/news/us-army-taps-carlyle-and-cyrusone-to-develop-data-centers-on-army-owned-land"]],
 "Alpha Digital Campus": [
   ["LandBridge: option to lease up to 3,400 acres to PowerBridge for a 2 GW powered campus (Apr 2, 2026)", "https://www.nasdaq.com/press-release/landbridge-announces-agreement-powerbridge-development-2-gw-powered-data-center"],
   ["Data Center Dynamics: Liberty Energy and PowerBridge venture to power the campus", "https://www.datacenterdynamics.com/en/news/liberty-energy-powerbridge-form-jv-to-power-planned-2gw-data-center-in-west-texas/"]],
 "Old Ocean data center": [
   ["Bisnow: Brazoria County rejects tax break for $3.5B data center and power plant", "https://www.bisnow.com/houston/news/data-center-development/houston-area-county-rejects-tax-abatement-for-35b-data-center-development-133616"],
   ["Public Citizen: commissioners vote 5-0 against the $10.5M abatement", "https://www.citizen.org/?p=120764"]],
 "FO Permian Partners data center": [
   ["Data Center Dynamics: 320 acres in Midland County, 150 MW of off-grid gas, 5 GW pitched", "https://www.datacenterdynamics.com/en/news/fo-permian-partners-unveils-5gw-off-grid-gas-power-solution-for-texas-data-centers/"],
   ["DataCenterNews: 150 MW off-grid power platform in the Permian Basin (Aug 2025)", "https://datacenter.news/story/permian-basin-launches-150mw-off-grid-power-for-ai-data-centres"]],
 "Glass Mountains Ranch campus": [
   ["Marfa Public Radio: Pacifico pitches an 8,400-acre Glass Mountains ranch to Brewster County (Sept 2026)", "https://www.marfapublicradio.org/news/2026-09-18/developer-behind-amazons-pecos-county-data-center-approaches-brewster-county-officials"]],
 "JMG data center, Conroe": [
   ["Data Center Dynamics: Jarvis Media Group to convert an office building into a data center", "https://datacenterdynamics.com/en/news/jarvis-media-group-seeks-to-convert-texas-office-building-into-data-center"],
   ["Datacentermap: four-story, 68,000 sq ft office building at 100 Plantation Drive", "https://datacentermap.com/usa/texas/houston/jmg-data-center/"]],
 "Glen Rose AI data center": [
   ["KERA: Black Mountain's 450-acre data center bordering Dinosaur Valley State Park", "https://www.keranews.org/environment-nature/2026-06-17/dinosaur-valley-data-center-impact"],
   ["KERA: Somervell County voted down the data center May 11, 2026", "https://www.keranews.org/news/2026-08-07/dinosaur-valley-power-lines-fight"]],
 "Fort Spunky": [
   ["Texas Scorecard: Hood County rejects Pacifico's Fort Spunky concept plan, 3-2", "https://texasscorecard.com/local/hood-county-rejects-data-center-concept-plan/"],
   ["Republik (Oct 30, 2026): the county stopped Fort Spunky for now; residents still fighting", "https://www.republik.ch/2026/10/30/das-monster-im-wald"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Carlyle Group, with the U.S. military", power:"3 GW listed", water:"Not disclosed", conf:"Reporting", note:"Needs verification."',
  'dev:"Carlyle Group, on Army land under a 50-year lease", power:"2.5 to 3 GW with its own power plant; more electricity than all of El Paso Electric\'s customers combined", water:"Army promises a closed system and \\"water neutral\\" operation, but its own solicitation rates El Paso\'s water risk \\"extremely high\\"; base wells draw on the Hueco Bolson, the city\'s main aquifer", conf:"Reporting", note:"About $2B on 1,384 acres of Fort Bliss, which the Army calls the Pentagon\'s first hyperscale data center. Operations targeted for fiscal 2027, after an environmental review. Pin is approximate."'),
 ('dev:"LandBridge and PowerBridge", power:"2 GW announced", water:"Not disclosed", conf:"Reporting", note:"Needs verification."',
  'dev:"PowerBridge, on land optioned from LandBridge; power venture with Liberty Energy", power:"Up to 2 GW of on-site power, near the Waha gas hub", water:"Not disclosed", conf:"Reporting", note:"An option to lease up to 3,400 acres, signed April 2026, with first power targeted for 2027. No tenant named. LandBridge, which owns about 320,000 acres in the Permian, is also the landowner behind the Reeves County gas plant with NRG."'),
 ('dev:"Nightpeak Energy", power:"620 MW listed", water:"Not disclosed", conf:"Reporting", note:"Needs verification."',
  'dev:"Nightpeak Energy", power:"Two 310 MW data centers with two 310 MW gas turbine plants", water:"Not disclosed", conf:"Reporting", note:"A $3.5B project on 158 acres outside Sweeny, about a mile from the San Bernard National Wildlife Refuge. Brazoria County commissioners voted 5-0 to deny its $10.5M tax break, but the project can still go forward; the company says it could energize from 2027."'),
 ('dev:"HiVolt Energy", power:"150 MW listed", water:"Not disclosed", conf:"Reporting", note:"Needs verification."',
  'dev:"FO Permian Partners with HiVolt Energy", power:"150 MW of off-grid gas with batteries at first; the company pitches 5 GW", water:"Not disclosed; the company says water is secured", conf:"Reporting", note:"A 320-acre site in Midland County marketed since 2025 as ready-made, off-grid power for data centers. No tenant has been named."'),
 ('note:"Big Bend region. Same developer as Fort Spunky. Needs verification."',
  'note:"An 8,400-acre ranch in the Glass Mountains northeast of Alpine, pitched to Brewster County in September 2026 by the developer of Amazon\'s GW Ranch gas plant. The county agenda said only \\"presentation from Pacifico Energy,\\" never \\"data center,\\" yet about 10 residents came to oppose it. The judge said the county would be extremely sensitive to water use. Same developer as Fort Spunky and Cedar Creek."'),
 ('dev:"JMG", power:"Not disclosed", water:"Not disclosed", conf:"Reporting", note:"100 Plantation Drive. Needs verification."',
  'dev:"Jarvis Media Group (JMG)", power:"Small; not disclosed", water:"Not disclosed", conf:"Reporting", note:"Converting an empty four-story, 68,000 sq ft office building at 100 Plantation Drive into an enterprise data center. A small reuse, not a campus."'),
 ('dev:"Possibly Black Mountain Power, which holds an air permit near the park (verify)"',
  'dev:"Black Mountain (Fort Worth)"'),
 ('note:"North of Dinosaur Valley State Park. Opposed by the county in May 2026."',
  'note:"A 450-acre data center bordering the north side of Dinosaur Valley State Park, home to some of the best-preserved dinosaur tracks in the world. Somervell County voted it down on May 11, 2026, and passed a resolution opposing new data centers until the state acts."'),
 ('note:"862 acres across the Brazos River from Pecan Plantation. Reported canceled."',
  'note:"862 acres across the Brazos River from Pecan Plantation. Hood County commissioners rejected Pacifico\'s concept plan 3-2, citing insufficient water. Stopped for now, not canceled: residents are still fighting it."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
h = open("hood/index.html").read()
old = '<span class="tag">Reported canceled</span><span class="tag">Reporting</span><h3>Fort Spunky</h3><p>Pacifico Energy, 862 acres across the Brazos River from Pecan Plantation, planned with off-grid gas power.</p>'
new = '<span class="tag">Plan rejected</span><span class="tag">Reporting</span><h3>Fort Spunky</h3><p>Pacifico Energy, 862 acres across the Brazos River from Pecan Plantation, planned with off-grid gas power. Commissioners rejected the concept plan 3-2, citing insufficient water. Stopped for now, not canceled.</p>'
if new not in h:
    assert h.count(old) == 1, "hood/index.html Fort Spunky line not found"
    open("hood/index.html", "w").write(h.replace(old, new))
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Fort Spunky wording</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We described Fort Spunky as canceled. Hood County rejected Pacifico\'s concept plan 3-2 over insufficient water, and the project is stopped for now rather than canceled. The map card and the Hood County page now say so.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 55: eight missed cards verified; Fort Spunky wording fixed on map and Hood page")
