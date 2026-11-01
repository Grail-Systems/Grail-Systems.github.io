"""Originals batch 24: McLennan County. The 'Data Campus' is Cipher near Riesel (pin moved); Project Merlin is Galaxy in McGregor."""
import json
L = {
 "McLennan County Data Campus": [
   ["Data Center Dynamics: Cipher plans 500 MW next to the Sandy Creek coal plant", "https://www.datacenterdynamics.com/en/news/cipher-looks-to-build-500mw-campus-near-coal-plant-outside-waco-texas/"],
   ["KXXV: Cipher answers Riesel residents' questions", "https://www.kxxv.com/news/local-news/in-your-neighborhood/mclennan-county/cipher-digital-addresses-riesel-data-center-questions-with-25-news"]],
 "Project Merlin (McGregor)": [
   ["Galaxy: 500-acre McGregor campus, initial 74 MW (July 28, 2026)", "https://www.prnewswire.com/news-releases/galaxy-expands-data-center-footprint-with-acquisition-of-500-acre-campus-in-mcgregor-texas-302836014.html"],
   ["Data Center Dynamics: Galaxy buys land outside Waco", "https://www.datacenterdynamics.com/en/news/galaxy-digital-buys-land-outside-waco-texas/"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
c = d["McLennan County Data Campus"]
c["loc"] = "East State Highway 6 near Riesel, next to the Sandy Creek coal power plant, McLennan County Precinct 2 (pin approximate)"
c["acres"] = "About 319 acres"
c["llc"] = "Cipher Digital (formerly Cipher Mining), a bitcoin miner moving into AI"
c["dates"] = "First reported Mar 2025. The precinct commissioner said he opposes it but that Texas law gives the county little authority to stop it"
m = d["Project Merlin (McGregor)"]
m["loc"] = "McGregor, McLennan County"
m["acres"] = "About 500 acres"
m["llc"] = "Galaxy Digital (Nasdaq: GLXY), under a development agreement with the City of McGregor"
m["dates"] = "Announced July 28, 2026 with a utility services agreement for interconnection; first phase about 74 MW, which Galaxy says could grow to several hundred MW"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('{name:"McLennan County Data Campus", county:"McLennan", type:"data", status:"announced", lat:31.55, lng:-97.15,\n   dev:"Not identified", power:"500 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  '{name:"McLennan County Data Campus", county:"McLennan", type:"data", status:"announced", lat:31.48, lng:-96.95,\n   dev:"Cipher Digital (formerly Cipher Mining)", power:"Up to 500 MW, next to the 932 MW Sandy Creek coal plant", water:"Not disclosed", conf:"Reporting", note:"About 319 acres near Riesel. The local commissioner opposes it but says Texas law gives the county little power to stop it. Cipher also has cards in Tom Green, McCulloch and Walker counties."'),
 ('status:"announced", lat:31.44, lng:-97.41,\n   dev:"Galaxy Digital", power:"74 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'status:"approved", lat:31.44, lng:-97.41,\n   dev:"Galaxy Digital", power:"About 74 MW to start; Galaxy says it could grow to several hundred MW", water:"Not disclosed", conf:"Reporting", note:"About 500 acres bought July 2026 under a development agreement with the City of McGregor. Galaxy\'s second Texas campus after Helios in Dickens County."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>McLennan County Data Campus</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We showed this with the developer not identified, pinned in Waco. It is Cipher Digital\'s planned campus near Riesel, next to the Sandy Creek coal plant, about 13 miles southeast. Developer and pin are fixed.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 24: McLennan County Data Campus is Cipher near Riesel; Project Merlin approved")
