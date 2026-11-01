"""Duplicates: merge Lancium Childress into Crusoe / Lancium Childress (one campus, now under construction); remove EdgeCore El Paso (the Meta El Paso campus listed twice)."""
import json, subprocess, sys
GONE = ["Lancium Childress", "EdgeCore El Paso"]
# Safety: stop if any other page in the repo refers to a card we are removing.
for name in GONE:
    r = subprocess.run(["git", "grep", "-l", "-F", "\"" + name + "\"", "--", ".", ":!texas.html", ":!data/", ":!tools/", ":!corrections.html"], capture_output=True, text=True)
    if r.stdout.strip():
        sys.exit("STOP: '" + name + "' is referenced in: " + r.stdout.strip())
p = "data/details.json"; d = json.load(open(p))
KEEP = "Crusoe / Lancium Childress campus"
k = d.setdefault(KEEP, {}); old = d.get("Lancium Childress", {})
have = {u for _, u in k.get("links", [])}
k.setdefault("links", []).extend(x for x in old.get("links", []) if x[1] not in have)
have = {u for _, u in k["links"]}
x = ["TechRadar: two Childress buildings already under construction (Oct 2026)", "https://www.techradar.com/pro/massive-1-5-million-sq-ft-data-center-campus-planned-for-west-texas-bringing-total-regional-ai-investment-to-usd12-billion"]
if x[1] not in have: k["links"].append(x)
if "comp" in old: k["comp"] = old["comp"]
k["dates"] = "Comptroller certified 'Lancium Clean Campus - Childress 1' Mar 25, 2025. Lancium testified to a Texas House committee Apr 2026. Crusoe and Lancium announced the 1 GW campus Jul 15, 2026; by Oct 2026 two buildings were under construction. In Sept 2026 Childress was under a boil-water notice and a disaster declaration; the city manager said Lancium had offered a possible new water source"
m = d.setdefault("Meta El Paso", {}); have = {u for _, u in m.get("links", [])}
for x in d.get("EdgeCore El Paso", {}).get("links", []):
    if "morethanjustparks" in x[1] and x[1] not in have:
        m.setdefault("links", []).append(["More Than Just Parks: the same campus listed as 'EdgeCore El Paso', operator Meta", x[1]])
for name in GONE: d.pop(name, None)
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
CUT = [
 '  {name:"Lancium Childress", county:"Childress", type:"data", status:"operating", lat:34.430, lng:-100.200,\n   dev:"Lancium", power:"Not disclosed", water:"About 11,000 gal/day from the Red River Water Authority; company says it will return 1 million gal/day", conf:"Reporting",\n   note:"Same developer as the Stargate Abilene campus. Likely the same site as our Crusoe / Lancium Childress card, where Crusoe is building a 1 GW campus; we are confirming what is operating here today.", src:"Inside Climate News (Texas House committee testimony, April 2026)"},\n',
 '  {name:"EdgeCore El Paso", county:"El Paso", type:"data", status:"announced", lat:31.8, lng:-106.25,\n   dev:"Listed as EdgeCore; the tracker names Meta as operator", power:"1 GW listed", water:"Not disclosed", conf:"Reporting", note:"Likely the same campus as Meta El Paso: the tracker lists Meta as operator at the same 1 GW, and we found no EdgeCore project in El Paso. See the Meta El Paso card for the full record.", src:"More Than Just Parks data center tracker"},\n',
]
T = [
 ('{name:"Crusoe / Lancium Childress campus", county:"Childress", type:"data", status:"announced", lat:34.42, lng:-100.22,\n   dev:"Crusoe and Lancium, with Meta reported as the customer", power:"1 GW, grid connection already approved by ERCOT", water:"Not disclosed; the companies say they will invest in local water infrastructure", conf:"Reporting", note:"Announced July 2026 on 270 acres Lancium owns, with construction set to start that fall. Likely the same site as our Lancium Childress card. Two months later, the town was under a boil-water notice and a disaster declaration after extreme heat.", src:"More Than Just Parks data center tracker"}',
  '{name:"Crusoe / Lancium Childress campus", county:"Childress", type:"data", status:"construction", lat:34.43, lng:-100.20,\n   dev:"Crusoe and Lancium, with Meta reported as the customer", power:"1 GW, grid connection already approved by ERCOT", water:"Lancium told a Texas House committee it would draw about 11,000 gal/day from the Red River Water Authority and return 1 million gal/day; the companies promise closed-loop cooling", conf:"Reporting", note:"One campus: Lancium owns the 270 acres and the power hookup, and Crusoe builds the data centers. Announced July 2026 with Meta reported as the customer; by October two buildings were under construction. Two months after the announcement, the town was under a boil-water notice and a disaster declaration after extreme heat, and Lancium offered the city a possible new water source.", src:"Crusoe and Lancium; Inside Climate News; TechRadar"}'),
]
s = open("texas.html").read()
for blk in CUT:
    if blk in s: s = s.replace(blk, "")
for name in GONE:
    assert 'name:"' + name + '"' not in s, "card still present: " + name
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read()
c = c.replace('<h3>El Paso: likely one campus, two cards</h3>', '<h3>El Paso: one campus, two cards (resolved)</h3>', 1)
for entry, body in [
 ('<li><span class="tag">Nov 1, 2026</span><h3>El Paso duplicate removed</h3>', '<p>We removed the "EdgeCore El Paso" card. It was Meta\'s El Paso campus listed a second time; the tracker behind it names Meta as operator, and no EdgeCore project exists in El Paso. Its source now sits on the Meta El Paso card.</p></li>\n'),
 ('<li><span class="tag">Nov 1, 2026</span><h3>Childress: two cards merged</h3>', '<p>"Lancium Childress" and "Crusoe / Lancium Childress campus" were the same site: Lancium owns the land and Crusoe builds there. We merged them into one card. We had shown Lancium Childress as operating; reporting from October 2026 shows two buildings under construction, so the merged card is marked under construction.</p></li>\n'),
]:
    if entry not in c:
        c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + body, 1)
open("corrections.html", "w").write(c)
print("Batch 51: duplicates resolved (Childress merged; EdgeCore El Paso removed)")
