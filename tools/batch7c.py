import json
p = "data/details.json"; d = json.load(open(p)); n = 0
for k, slug in M.items():
    e = d.setdefault(k, {}); L = e.setdefault("links", [])
    if not any(B + slug == u for _, u in L):
        L.append(["More Than Just Parks tracker entry (names its original source)", B + slug]); n += 1
g = d["Google, Gray County"]
g["comp"] = "Meitner Data Center (owner IP Meitner DTC, LLC; occupant Google LLC), certified Apr 27, 2026. The tracker places Meitner in Gray County."
g.setdefault("links", [])
if not any("comptroller" in u for _, u in g["links"]): g["links"].append(["Texas Comptroller data center list", "https://comptroller.texas.gov/taxes/data-centers/data-center-lists.php"])
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [('dev:"Highlander SM One LLC", power:"Size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Listed as canceled. Listed by the More Than Just Parks tracker; needs verification."',
      'dev:"Highlander SM One LLC", power:"Size not disclosed", water:"Not disclosed", conf:"Reporting", note:"This is the same project as the San Marcos data center on Francis Harris Lane, which the City Council denied in Feb 2026. See that card for the full record."')]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:70]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>San Marcos: one project, two cards</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>The map listed Highlander SM One (San Marcos) and the San Marcos data center on Francis Harris Lane as separate projects. They are the same proposal. Both cards now say so.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print(f"Batch 7: {n} cards now link to their tracker entries; Gray County gets its Comptroller record; San Marcos duplicate flagged")
