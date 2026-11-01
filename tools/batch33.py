"""Originals batch 33: Sulphur Springs (old Thermo mine). MSB Global is out; CyrusOne is considering it; the deed bars power generation."""
import json
K = "Matrix Data Center Campus (Sulphur Springs)"
L = [["KLTV: CyrusOne holds a community meeting; MSB Global no longer involved (Sept 24, 2026)", "https://www.kltv.com/2026/09/25/data-center-developer-holds-community-meeting-potential-sulphur-springs-project/"],
     ["KLTV: new developer to take over amid legal battles (June 2026)", "https://kltv.com/2026/06/03/new-developer-take-over-data-center-project-sulphur-springs-amid-legal-battles/"],
     ["KLTV: judge denies the city's major motion (Feb 2026)", "https://kltv.com/2026/02/10/judge-denies-major-motion-city-sulphur-springs-data-center-lawsuits/"],
     ["KLTV: a year and a half of council minutes never mention the data center", "https://www.kltv.com/2026/01/21/residents-want-answers-massive-data-center-sulphur-springs"],
     ["KLTV: city budgets $1.2M for lawsuit costs; residents protest (May 2026)", "https://www.kltv.com/2026/05/06/residents-protest-sulphur-springs-allots-12-million-cost-data-center-lawsuits/"],
     ["KETK: injunction against power system construction", "https://digital-release.ketk.com/?p=2838417"],
     ["KETK: MSB's original plan, 30 buildings, 35% abatement for 10 years", "https://digital-release.ketk.com/?p=2670833"]]
p = "data/details.json"; d = json.load(open(p)); e = d.setdefault(K, {})
have = {u for _, u in e.get("links", [])}
e.setdefault("links", []).extend(x for x in L if x[1] not in have)
e["loc"] = "Former Thermo lignite mine southeast of Sulphur Springs, just outside city limits; land donated to the city by Luminant after the mine closed in 2018"
e["acres"] = "About 1,677 acres"
e["llc"] = "Was MSB Global (Fort Lauderdale), in a public-private partnership with the City of Sulphur Springs and Hopkins County; MSB is no longer involved. CyrusOne is now considering the site"
e["incent"] = "MSB's plan cited a 35% property tax abatement for 10 years"
e["dates"] = "MSB broke ground June 2025 and cleared land. KLTV found no mention of a data center in 18 months of council minutes. Vistra/Luminant, the former owner, says the deed bars power generation; a judge has barred power generation on the land until trial in 2027, and construction halted. The city budgeted $1.2M for legal fees. Sept 2026: CyrusOne held a community meeting, pitching a gas-powered campus of about $2.6B"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
old = 'status:"stopped", lat:33.14, lng:-95.6,\n   dev:"MSB Global", power:"800 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed as suspended. East Texas. Listed by the More Than Just Parks tracker; needs verification."'
new = 'status:"stopped", lat:33.14, lng:-95.6,\n   dev:"Was MSB Global; CyrusOne now considering it", power:"MSB planned 3 GW in 30 buildings; CyrusOne pitches an on-site gas plant", water:"CyrusOne says about 1,000 gal/day per building", conf:"Reporting", note:"On a coal mine site Luminant gave the city. The old owner says the deed bars power generation, a judge has barred it until a 2027 trial, and construction stopped. Council minutes never mentioned the project. MSB is out; CyrusOne held a community meeting in Sept 2026."'
s = open("texas.html").read()
if new not in s:
    assert s.count(old) == 1, "Matrix card not found"; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Sulphur Springs developer</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We listed MSB Global as the developer of the Sulphur Springs campus. MSB is no longer involved after lawsuits over the land deed; CyrusOne is now considering the site. The card now explains the deed dispute and the court order against power generation.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 33: Sulphur Springs checked; MSB out, CyrusOne considering, deed bars power generation")
