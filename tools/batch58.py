"""Search Console: add Google's verification file, and a sitemap (plus robots.txt pointer) if the site doesn't have them."""
import os, datetime
V = "googlee48b24b59923d400.html"
open(V, "w").write("google-site-verification: " + V)
SKIP_DIRS = {"tools", "data", "assets", "img", ".git", "node_modules"}
if not os.path.exists("sitemap.xml"):
    urls = []
    for root, dirs, files in os.walk("."):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith("."))
        for f in sorted(files):
            if not f.endswith(".html") or f.startswith("google") or f == "404.html":
                continue
            rel = os.path.join(root, f)[2:]
            if rel == "index.html": path = "/"
            elif f == "index.html": path = "/" + os.path.dirname(rel) + "/"
            else: path = "/" + rel[:-5]
            urls.append(path)
    today = datetime.date.today().isoformat()
    body = "".join("  <url><loc>https://grailsystems.io%s</loc><lastmod>%s</lastmod></url>\n" % (u, today) for u in sorted(set(urls)))
    open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + "</urlset>\n")
    print("sitemap.xml created with", len(set(urls)), "pages")
else:
    print("sitemap.xml already exists; left unchanged")
line = "Sitemap: https://grailsystems.io/sitemap.xml"
if os.path.exists("robots.txt"):
    r = open("robots.txt").read()
    if "Sitemap:" not in r:
        open("robots.txt", "a").write(("" if r.endswith("\n") else "\n") + line + "\n")
        print("robots.txt: sitemap line added")
    else:
        print("robots.txt already lists a sitemap; left unchanged")
else:
    open("robots.txt", "w").write("User-agent: *\nAllow: /\n" + line + "\n")
    print("robots.txt created")
print("Batch 58: verification file " + V + " added")
