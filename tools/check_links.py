import os, re
bad = []
for root, dirs, files in os.walk("."):
    if ".git" in root: continue
    for f in files:
        if not f.endswith(".html"): continue
        path = os.path.join(root, f)
        for href in re.findall(r'href="(/[^"#?]*)"', open(path, encoding="utf-8", errors="ignore").read()):
            t = href.strip("/")
            ok = (t == "" or os.path.exists(t) or os.path.exists(t + ".html") or os.path.exists(os.path.join(t, "index.html")))
            if not ok: bad.append((path, href))
for p, h in sorted(set(bad)): print("BROKEN:", p, "->", h)
print("Checked. Broken links:", len(set(bad)))
