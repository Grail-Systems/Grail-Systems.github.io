"""Originals batch 12: Prometheus Hyperscale (Kaufman); log the Wichita Falls developer correction."""
import json
K = "Prometheus Hyperscale Kaufman campus"
L = [["Data Center Dynamics: Prometheus details its 500-acre Kaufman County campus (Feb 2026)", "https://www.datacenterdynamics.com/en/news/prometheus-hyperscale-details-plans-for-dallas-data-center-campus/"],
     ["Baxtel: four 50 MW buildings at FM 1641 and County Road 213", "https://baxtel.com/data-center/prometheus-hyperscale-dallas-4"],
     ["Data Center Dynamics: Prometheus also plans up to 2.5 GW in Reeves County", "https://www.datacenterdynamics.com/en/news/prometheus-hyperscale-partners-with-istmo-to-develop-up-to-25gw-gas-powered-data-center-in-reeves-county-texas/"]]
p = "data/details.json"; d = json.load(open(p)); e = d.setdefault(K, {})
have = {u for _, u in e.get("links", [])}
e.setdefault("links", []).extend(x for x in L if x[1] not in have)
e["loc"] = "FM 1641 and County Road 213, between Talty and Post Oak Bend City (near Flexential's Talty campus)"
e["acres"] = "About 500 acres"
e["llc"] = "Prometheus Hyperscale (formerly Wyoming Hyperscale White Box LLC), partnered with Engie North America"
e["dates"] = "Plans detailed Feb 2026. Four 50 MW buildings: first listed for 2026, then mid 2027, early 2028 and late 2028"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
old = 'dev:"Prometheus Hyperscale", power:"200 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."'
new = 'dev:"Prometheus Hyperscale, with Engie North America", power:"200 MW in four 50 MW buildings; listed with on-site gas generation and batteries", water:"Liquid-cooled; amount not disclosed", conf:"Reporting", note:"About 500 acres between Talty and Post Oak Bend City, a few miles from Flexential\'s Talty campus. The same company plans up to 2.5 GW in Reeves County."'
s = open("texas.html").read()
if new not in s:
    assert s.count(old) == 1, "Prometheus card not found"; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Wichita Falls Business Park</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We named only a shell company, "Texas Data Center Campus LLC," and listed 800 MW. The developer is Skybox Datacenters, buying through Texas Data Centers Campus LLC. Skybox markets the campus at 300+ MW; the card now shows both figures. Groundbreaking has been pushed to early 2027 after the state audit.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 12: Prometheus checked against originals; Wichita Falls correction logged")
