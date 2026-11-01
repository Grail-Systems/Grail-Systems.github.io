"""Build a County Watch page for every county on the Texas map that does not have one yet. Safe to run again."""
import json, re, os
P = json.load(open("data/projects.json"))
s = open("legislators.html").read()
H = json.loads(re.search(r"^const H = (\{.*?\});", s, re.M).group(1)); S = json.loads(re.search(r"^const S = (\{.*?\});", s, re.M).group(1))
json.dump({"H": H, "S": S}, open("data/districts.json", "w"), ensure_ascii=False)
FEED = {"Angelina","Nacogdoches","Anderson","Henderson","Cherokee","Rusk","Navarro","Houston","Smith","Shelby","San Augustine","Trinity","Polk",
        "Tyler","Jasper","Sabine","Panola","Gregg","Milam","Hood","Ellis","Hays","Young","Somervell","El Paso","Newton"}
cty = lambda c: re.sub(r"\s*\(.*\)\s*", "", c).strip()
slug = lambda c: re.sub(r"[^a-z]", "", c.lower())
counties = sorted({cty(p["county"]) for p in P})
T = open("tools/county_template.html").read()
pages, made = {}, 0
for c in counties:
    sl = slug(c); path = os.path.join(sl, "index.html"); pages[c] = f"/{sl}/"
    if os.path.exists(path): continue
    n = sum(1 for p in P if cty(p["county"]) == c)
    live = c in FEED
    html = (T.replace("{{COUNTY}}", c).replace("{{SLUG}}", sl).replace("{{N}}", str(n)).replace("{{S}}", "" if n == 1 else "s")
             .replace("{{LIVE}}", "1" if live else "0")
             .replace("{{LIVEBLOCK}}", f'<section id="live" data-county="{c}" data-places=""></section>\n<script src="/assets/livewatch.js" defer></script>' if live else ""))
    os.makedirs(sl, exist_ok=True); open(path, "w").write(html); made += 1
json.dump(pages, open("data/county_pages.json", "w"), ensure_ascii=False, indent=0)
print(f"{made} new county pages; {len(pages)} counties total")
# Index page of every county
from html import escape as E
rows = []
for c in counties:
    ps = [p for p in P if cty(p["county"]) == c]; act = sum(1 for p in ps if p["status"] != "stopped")
    rows.append(f'<li><h3><a href="{pages[c]}">{E(c)} County</a></h3><p>{len(ps)} project{"s" if len(ps) != 1 else ""} on the map, {act} still active</p></li>')
idx = T.split("<div class=\"hero\">")[0].replace(f"{{{{COUNTY}}}} County Watch | Grail Systems", "Every County Watch page | Grail Systems")
idx = re.sub(r"\{\{[A-Z]+\}\}", "", idx).replace(' County Watch | Grail Systems', 'Every County Watch page | Grail Systems', 1)
idx = idx.replace('<meta name="description" content="Data center, crypto mine and power plant projects in  County, Texas: who is behind them, what they need, upcoming dates and how to ask for records.">',
                  '<meta name="description" content="A County Watch page for every Texas county with a tracked data center, crypto mine or power plant project.">')
idx = re.sub(r'<meta property="og:[^>]*>\n', '', idx)
idx += f'''<div class="hero">
  <h1>Every County Watch page</h1>
  <p>{len(counties)} Texas counties have at least one data center, crypto mine or large power project on the Texas Watch map. Each page lists the projects, upcoming dates, your legislators and a records-request letter writer.</p>
</div>
<section><ul class="rows">
{chr(10).join(rows)}
</ul></section>
<footer>
  <span>County Watch · Grail Systems</span>
  <a href="/texas">Texas Watch</a>
  <a href="/legislators">Legislators</a>
  <a href="mailto:contact@grailsystems.io">contact@grailsystems.io</a>
</footer>
</div>
</body>
</html>
'''
open("counties.html", "w").write(idx); print("counties.html lists", len(counties), "counties")
