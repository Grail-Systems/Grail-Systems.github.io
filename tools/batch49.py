"""Originals batch 49: Pacifico Cedar Creek. Not stopped: the moratorium was in Ohio. Gas plant prep permit issued, abatement requests withdrawn, 'Project Longhorn' filed for a Nov 30, 2026 start."""
import json
K = "Pacifico Cedar Creek Campus"
L = [
 ["Community Impact: $2.2B Cedar Creek project; JETI application with Bastrop ISD; the 12-month moratorium was at Pacifico's alternate Ohio site", "https://communityimpact.com/bastrop-cedar-creek/business/new-22b-cedar-creek-data-center-project-abatements-under-review/"],
 ["KXAN: county confirms a site-prep permit for the gas facility was issued July 23", "https://www.kxan.com/investigations/texas-data-center-growth-fuels-ai-boom-debate/amp/"],
 ["Community Impact: 100+ residents at a July 22 town hall; 2,842 acres with 710 MW of gas generation", "https://communityimpact.com/bastrop-cedar-creek/government/bastrop-county-residents-organize-for-data-center-transparency-local-guardrails/"],
 ["CBS Austin: county asks TCEQ for a public meeting on the 48-turbine gas plant air permit", "https://cbsaustin.com/news/local/bastrop-county-commissioners-ok-request-for-tceq-meeting-on-gas-plant-concerns"],
 ["Elgin Courier: developers withdraw county tax break requests (Aug 2026)", "https://www.elgincourier.com/article/4854,developers-withdraw-tax-break-requests"],
 ["Data Center Dynamics: 'Project Longhorn' Building One filed, $366M, construction Nov 30, 2026", "https://datacenterdynamics.com/en/news/anthropic-linked-366m-data-center-project-filed-for-in-cedar-creek-texas"],
 ["CBS Austin: residents urge transparency; residents say Anthropic is tied to the project", "https://cbsaustin.com/news/local/bastrop-county-residents-urge-transparency-on-proposed-data-center-gas-plant-project"],
]
p = "data/details.json"; d = json.load(open(p))
e = d.setdefault(K, {}); have = {u for _, u in e.get("links", [])}
e.setdefault("links", []).extend(x for x in L if x[1] not in have)
e["loc"] = "382 Earl Callahan Road, near Walter Hoffman Road, Cedar Creek, Bastrop County; about 7 miles south of the EdgeConneX campuses. Pin approximate"
e["acres"] = "2,842 acres, about 600 to be developed; first building about 498,000 sq ft"
e["llc"] = "Pacifico Cedar Creek LLC (Pacifico Energy) for the gas plant; Black Chamber Partners tied to the data center; Anthropic named in reporting as linked"
e["dates"] = "Comptroller JETI application with Bastrop ISD June 24, 2026; gas site-prep permit issued July 23; town halls July 22 and Aug 20; county tax abatement requests withdrawn Aug 2026; county asked TCEQ for a public meeting on the air permit; 'Project Longhorn' Building One ($366M) filed Oct 2026 with construction set for Nov 30, 2026. Same developer as Fort Spunky (Hood)"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('{name:"Pacifico Cedar Creek Campus", county:"Bastrop", type:"data", status:"stopped",',
  '{name:"Pacifico Cedar Creek Campus", county:"Bastrop", type:"data", status:"announced",'),
 ('dev:"Pacifico Energy", power:"490 MW listed", water:"Not disclosed", conf:"Reporting",\n   note:"Same developer as Fort Spunky in Hood County. A public tracker lists it as blocked by a moratorium; which government acted needs verification."',
  'dev:"Pacifico Energy (gas plant), with Black Chamber Partners; reporting links the data center to Anthropic", power:"On-site gas plant: 710 MW reported, and a state air permit filing for about 1,300 MW from 48 turbines", water:"Not disclosed", conf:"Reporting",\n   note:"Not stopped. The moratorium a tracker cited was in Ohio, at Pacifico\'s alternate site. In Bastrop County, a site-prep permit for the gas plant was issued in July, the developers withdrew their county tax break requests in August, and the first $366M building (\\"Project Longhorn\\") was filed with the state to start November 30, 2026. More than 100 residents packed a July town hall; the county asked TCEQ for a public meeting on the air permit. Same developer as Fort Spunky in Hood County."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Pacifico Cedar Creek is not stopped</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We showed Pacifico\'s Cedar Creek campus as stopped by a moratorium. The moratorium was in Muhlenberg Township, Ohio, Pacifico\'s alternate site. In Bastrop County the project is moving: a gas plant site permit was issued in July 2026 and the first building is filed to start construction November 30, 2026. Status changed to announced.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 49: Pacifico Cedar Creek (not stopped; moratorium was in Ohio) checked")
