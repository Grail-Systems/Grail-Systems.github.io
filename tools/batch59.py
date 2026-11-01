"""Sitemap: add any live pages missing from the existing sitemap.xml (keeps every existing entry as is)."""
import os, re, datetime
SKIP_DIRS = {"tools", "data", "assets", "img", ".git", "node_modules"}
pages = set()
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
    for f in files:
        if not f.endswith(".html") or f.startswith("google") or f == "404.html":
            continue
        rel = os.path.join(root, f)[2:]
        if rel == "index.html": pages.add("/")
        elif f == "index.html": pages.add("/" + os.path.dirname(rel) + "/")
        else: pages.add("/" + rel[:-5])
s = open("sitemap.xml").read()
have = {re.sub(r"^https?://[^/]+", "", u) or "/" for u in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", s)}
have |= {h.rstrip("/") for h in have} | {h + "/" for h in have}
missing = sorted(p for p in pages if p not in have and p.rstrip("/") not in have)
if missing:
    today = datetime.date.today().isoformat()
    add = "".join("  <url><loc>https://grailsystems.io%s</loc><lastmod>%s</lastmod></url>\n" % (p, today) for p in missing)
    assert s.count("</urlset>") == 1, "sitemap end tag not found"
    s = s.replace("</urlset>", add + "</urlset>")
    open("sitemap.xml", "w").write(s)
print("Batch 59: added", len(missing), "missing pages to sitemap:", " ".join(missing) or "(none)")
