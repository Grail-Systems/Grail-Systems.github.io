"""Originals batch 22: Meta El Paso (BlackRock venture, 1 GW) and the 'EdgeCore El Paso' card, likely the same campus."""
import json
L = {
 "Meta El Paso": [
   ["KFOX: Meta and BlackRock form a $14B venture; BlackRock 80%, Meta 20%", "https://kfoxtv.com/news/local/meta-blackrock-announce-strategic-venture-for-14b-el-paso-ai-data-center-campus"],
   ["SiliconANGLE: 1 GW campus; BlackRock contributes $7B (July 28, 2026)", "https://siliconangle.com/2026/07/28/meta-build-14b-el-paso-data-center-campus-blackrock/"],
   ["Data Center Frontier: the 366 MW gas plant tied to the campus", "https://www.datacenterfrontier.com/energy/article/55368331/byop-moves-to-the-center-of-data-center-strategy"]],
 "EdgeCore El Paso": [
   ["SiliconANGLE: Meta's 1 GW El Paso campus (the likely match)", "https://siliconangle.com/2026/07/28/meta-build-14b-el-paso-data-center-campus-blackrock/"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
m = d["Meta El Paso"]
add = "July 28, 2026: Meta and BlackRock formed a venture to own the campus (BlackRock 80%, Meta 20%), about $14B total; capacity to start coming online in 2028"
if add not in m.get("dates", ""):
    m["dates"] = (m.get("dates", "").rstrip(". ") + ". " + add) if m.get("dates") else add
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('note:"Up to $10B planned. The city gave', 'note:"About $14B with BlackRock (was up to $10B). The city gave'),
 ('dev:"Meta (land bought as Wurldwide LLC)", power:"Not disclosed",',
  'dev:"Meta (land bought as Wurldwide LLC); now 80% owned by BlackRock", power:"1 GW of computing; El Paso Electric is building a 366 MW gas plant for it",'),
 ('dev:"EdgeCore", power:"1 GW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Listed as EdgeCore; the tracker names Meta as operator", power:"1 GW listed", water:"Not disclosed", conf:"Reporting", note:"Likely the same campus as Meta El Paso: the tracker lists Meta as operator at the same 1 GW, and we found no EdgeCore project in El Paso. See the Meta El Paso card for the full record."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>El Paso: likely one campus, two cards</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>The map shows "EdgeCore El Paso" and "Meta El Paso" separately. The tracker behind the EdgeCore card lists Meta as its operator at the same 1 GW, and we found no EdgeCore project in El Paso. They are likely the same campus; both cards now say so. Meta El Paso also now shows the July 2026 BlackRock venture.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 22: Meta El Paso updated (BlackRock, 1 GW); EdgeCore card flagged as likely duplicate")
