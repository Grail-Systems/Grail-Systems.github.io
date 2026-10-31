"""Add the Live data section to county pages. Safe to run again; skips pages that have it."""
import os
LIVE = {
 "anderson": ("Anderson", ["Palestine", "Elkhart", "Frankston", "Tennessee Colony"], False),
 "navarro": ("Navarro", ["Corsicana", "Kerens", "Blooming Grove", "Dawson"], False),
 "henderson": ("Henderson", ["Athens", "Malakoff", "Gun Barrel City", "Chandler", "Brownsboro", "Eustace"], False),
 "milam": ("Milam", ["Rockdale", "Thorndale", "Milano", "Buckholts"], False),
 "hood": ("Hood", ["Granbury", "Tolar", "Lipan", "Cresson"], False),
 "ellis": ("Ellis", ["Waxahachie", "Ennis", "Midlothian", "Red Oak", "Ferris"], False),
 "hays": ("Hays", ["San Marcos", "Kyle", "Buda", "Dripping Springs", "Wimberley"], False),
 "young": ("Young", ["Olney", "Newcastle"], False),
 "somervell": ("Somervell", ["Glen Rose"], False),
 "elpaso": ("El Paso", ["Socorro", "Horizon City", "Anthony", "Clint", "Fabens"], True),
 "newton": ("Newton", ["Deweyville", "Bon Wier", "Burkeville"], True),
}
for slug, (name, places, noercot) in LIVE.items():
    p = os.path.join(slug, "index.html")
    if not os.path.exists(p): print("no page:", p); continue
    s = open(p).read()
    if 'id="live"' in s: print("already has live data:", slug); continue
    block = '\n<section id="live" data-county="%s" data-places="%s"%s></section>\n<script src="/assets/livewatch.js" defer></script>\n' % (name, "|".join(places), ' data-noercot="1"' if noercot else "")
    i = s.find("<h2>At a glance</h2>")
    j = s.find("</section>", i) + len("</section>") if i >= 0 else s.find("<footer>")
    s = s[:j] + block + s[j:]
    open(p, "w").write(s); print("live data added:", slug)
