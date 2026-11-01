"""Add the 'What's changed lately' box to every county page, and build /updates. Safe to run again."""
import json, os, re
pages = json.load(open("data/county_pages.json")); done, skipped = 0, []
for county, url in pages.items():
    p = url.strip("/") + "/index.html"
    if not os.path.exists(p): skipped.append(county); continue
    s = open(p).read()
    if 'id="changes"' in s: continue
    a = s.find('<section id="ask"')
    if a < 0: a = s.find('<footer')
    if a < 0: skipped.append(county); continue
    s = s[:a] + f'<section id="changes" data-county="{county}"></section>\n<script src="/assets/changes.js" defer></script>\n' + s[a:]
    open(p, "w").write(s); done += 1
print(f"Changes box added to {done} county pages.", ("Skipped: " + ", ".join(skipped)) if skipped else "")
T = open("counties.html").read()
head = T.split('<div class="hero">')[0].replace("Every County Watch page | Grail Systems", "What changed | Grail Systems")
head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Every change on Texas Watch, newest first: new projects, status changes, grid requests, records and hearing dates.">', head)
open("updates.html", "w").write(head + '''<div class="hero">
  <h1>What changed</h1>
  <p>Every night, Texas Watch checks for new projects, status changes, new ERCOT grid requests, new records, new hearing dates and new state tax-break records. Everything it finds lands here, and on the county page where it happened.</p>
</div>
<section id="changes" data-county=""><p>Loading…</p></section>
<script src="/assets/changes.js" defer></script>
<footer>
  <span>Texas Watch · Grail Systems</span>
  <a href="/texas">Texas Watch</a>
  <a href="/counties">Every county</a>
  <a href="mailto:contact@grailsystems.io">contact@grailsystems.io</a>
</footer>
</div>
</body>
</html>
''')
p = "texas.html"; s = open(p).read()
if 'href="/updates"' not in s:
    s = s.replace('<a href="/counties">See a County Watch page for every county on the map.</a></p>', '<a href="/counties">See a County Watch page for every county on the map</a>, or <a href="/updates">what changed lately</a>.</p>', 1)
    open(p, "w").write(s)
print("updates.html built; map links to it" if 'href="/updates"' in s else "updates.html built; map link NOT added")
