import os, datetime
base = "https://grailsystems.io"
today = datetime.date.today().isoformat()
urls = []
for root, dirs, files in os.walk("."):
    if any(x in root for x in (".git", "tools", "data", "assets", "carrizo_wilcox_aquifer")): continue
    for f in files:
        if not f.endswith(".html"): continue
        path = os.path.join(root, f)[2:]
        if f == "index.html":
            u = "/" + os.path.dirname(path) + ("/" if os.path.dirname(path) else "")
        else:
            u = "/" + path[:-5]
        urls.append(u)
urls = sorted(set(urls))
with open("sitemap.xml", "w") as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in urls:
        fh.write("  <url><loc>%s%s</loc><lastmod>%s</lastmod></url>\n" % (base, u, today))
    fh.write("</urlset>\n")
if not os.path.exists("robots.txt"):
    open("robots.txt", "w").write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % base)
print("Sitemap:", len(urls), "pages")
for u in urls: print(" ", u)
