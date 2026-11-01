"""Source batch 8, part B: Prosper (developer withdrew) and Google Pflugerville."""
import json
L = {
 "Prosper / FM 1385 data center": [["CBS Texas: the developer withdraws (Sept 8, 2026)", "https://www.cbsnews.com/texas/news/prosper-tx-project-tomahawk-pulled-9-8-2026/"],
   ["Community Impact: commission recommends denial 7 to 0", "https://communityimpact.com/prosper-celina/development/prosper-commission-recommends-denial-of-580-million-data-center/"],
   ["Hoodline: the site next to the Parvin substation", "https://hoodline.com/2026/08/prosper-yanks-data-center-vote-as-eight-precincts-rise-up-against-it/"]],
 "Google Pflugerville": [["Google 2025 Environmental Report (per-site water figures)", "https://www.gstatic.com/gumdrop/sustainability/google-2025-environmental-report.pdf"],
   ["Global Investigative Journalism Network: reading data center water reports", "https://gijn.org/?p=2485543"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
pr = d["Prosper / FM 1385 data center"]
pr["loc"] = "About 37 acres near FM 1385 and Parvin Road, next to Brazos Electric's Parvin substation"
pr["llc"] = "White Rose Partners (Dallas); project name Project Tomahawk"
pr["dates"] = "Pulled from the Aug 18, 2026 agenda; Planning and Zoning recommended denial 7 to 0 on Sept 1 after more than 400 written objections; the developer withdrew before the Sept 8 council vote"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
old = ('name:"Prosper / FM 1385 data center", county:"Denton (Prosper area)", type:"data", status:"filed", lat:33.240, lng:-96.920,\n   dev:"Not identified", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"Rezoning of farmland along FM 1385. Residents say required notices missed nearby homes.", src:"Prosper Planning & Zoning meeting, Aug 18, 2026 (via Citizen Portal)"}')
new = ('name:"Prosper / FM 1385 data center", county:"Denton (Prosper area)", type:"data", status:"stopped", lat:33.240, lng:-96.920,\n   dev:"White Rose Partners (Dallas)", power:"Not disclosed", water:"Not disclosed", conf:"Reporting",\n   note:"Project Tomahawk: a $580M, 225,000 sq ft data center on about 37 acres. After residents across eight precincts objected, the planning commission recommended denial 7 to 0 and the developer withdrew in September 2026.", src:"CBS Texas; Community Impact; Hoodline; Prosper Planning & Zoning"}')
s = open("texas.html").read()
if new not in s:
    assert s.count(old) == 1, "Prosper card not found"; s = s.replace(old, new); open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Prosper data center</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We showed the Prosper data center along FM 1385 as still filed, with the developer not identified. The developer was White Rose Partners, and it withdrew Project Tomahawk in September 2026 after the planning commission recommended denial 7 to 0. Updated to stopped.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 8B: Prosper corrected to stopped; Google Pflugerville linked to Google's own report")
