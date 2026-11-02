"""Batch 70: (1) aquifer cross-section drawing (assets/aquifer-section.svg) on the map and the Angelina page; (2) show privacy notes in the Angelina records section."""
import math, random, re, hashlib
def f(x): return f"{x:.1f}"
def longleaf(x, base, h, sw=1.4, seed=1):
    r = random.Random(seed); p = []
    top = (x + r.uniform(-4, 4), base - h)
    p.append(f'<path d="M{f(x)} {f(base)} C{f(x+1)} {f(base-h*0.4)} {f(top[0]-1)} {f(base-h*0.7)} {f(top[0])} {f(top[1])}" stroke-width="{sw*1.3}"/>')
    tufts = []; n = r.randint(4, 6)
    for i in range(n):
        t = 0.62 + 0.38 * i / (n - 1); y = base - h * t; side = -1 if i % 2 else 1
        bl = h * r.uniform(0.07, 0.14); bx = x + (top[0] - x) * t; ex, ey = bx + side * bl, y - bl * 0.35
        p.append(f'<path d="M{f(bx)} {f(y)} Q{f(bx+side*bl*0.5)} {f(y-bl*0.05)} {f(ex)} {f(ey)}" stroke-width="{sw}"/>'); tufts.append((ex, ey))
    tufts.append(top)
    for (tx, ty) in tufts:
        k = r.randint(9, 13)
        for j in range(k):
            a = -math.pi/2 + (j/(k-1) - 0.5) * math.pi * 1.5; L = h * r.uniform(0.055, 0.085)
            p.append(f'<path d="M{f(tx)} {f(ty)} L{f(tx+math.cos(a)*L)} {f(ty+math.sin(a)*L*0.8+L*0.25)}" stroke-width="{sw*0.6}"/>')
    return "".join(p)
def bluebonnet(cx, base, h, sw=1.3):
    p = [f'<path d="M{f(cx)} {f(base)} C{f(cx-2)} {f(base-h*0.4)} {f(cx+2)} {f(base-h*0.7)} {f(cx)} {f(base-h)}" stroke-width="{sw}"/>']
    for side in (-1, 1):
        lx, ly = cx, base - h*0.18
        for k in range(4):
            a = math.radians(-90 + side*(25 + k*18)); L = h*0.2
            ex, ey = lx + math.cos(a)*L, ly + math.sin(a)*L; mx, my = lx + math.cos(a)*L*0.5, ly + math.sin(a)*L*0.5
            nx, ny = -math.sin(a)*L*0.09, math.cos(a)*L*0.09
            p.append(f'<path d="M{f(lx)} {f(ly)} Q{f(mx+nx)} {f(my+ny)} {f(ex)} {f(ey)} Q{f(mx-nx)} {f(my-ny)} {f(lx)} {f(ly)}" stroke-width="{sw*0.8}"/>')
    n = 9
    for i in range(n):
        t = 0.45 + 0.55 * i / n; y = base - h * t; s = (1 - i/n) * h*0.05 + h*0.018
        for side in (-1, 1):
            if i == n-1 and side == 1: continue
            fx = cx + side * s * 0.9
            p.append(f'<path d="M{f(cx)} {f(y)} Q{f(fx+side*s*0.9)} {f(y-s*1.3)} {f(fx+side*s*0.2)} {f(y-s*1.6)} Q{f(fx-side*s*0.6)} {f(y-s*0.9)} {f(cx)} {f(y)}" stroke-width="{sw*0.75}"/>')
    return "".join(p)
def cross(W=1400, H=380):
    r = random.Random(8); G = 150
    def gy(x): return G + 5*math.sin(x/W*6.28*1.3+0.4) + 2.5*math.sin(x/W*6.28*3.1+0.8)
    def wave(y0, a, ph): return [(x, y0 + a*math.sin(x/W*6.28*1.3+ph) + a*0.5*math.sin(x/W*6.28*3.1+ph*2)) for x in range(0, W+1, 20)]
    def line(pts, sw): return '<path d="M' + " L".join(f"{f(x)} {f(y)}" for x,y in pts) + f'" stroke-width="{sw}"></path>'
    surf = []; x = 18
    while x < W - 18:
        h = r.uniform(0.55, 1.0) * (G - 8)
        surf.append(longleaf(x, gy(x), h, sw=1.1, seed=r.randint(0, 9999)))
        for k in range(3):
            a = math.radians(r.uniform(60, 120)); L = r.uniform(14, 26)
            surf.append(f'<path d="M{f(x)} {f(gy(x))} q{f(math.cos(a)*L*0.4)} {f(L*0.5)} {f(math.cos(a)*L)} {f(math.sin(a)*L)}" stroke-width="0.7"></path>')
        x += r.uniform(46, 96)
    for i in range(120):
        x = r.uniform(0, W); y = gy(x)
        for k in range(3):
            a = math.radians(-90 + r.uniform(-30, 30)); L = r.uniform(5, 11)
            surf.append(f'<path d="M{f(x)} {f(y)} l{f(math.cos(a)*L)} {f(math.sin(a)*L)}" stroke-width="0.8"></path>')
    for x in (230, 248, 610, 980, 1000, 1260): surf.append(bluebonnet(x, gy(x), 34, sw=0.9))
    surf.append(line([(x, gy(x)) for x in range(0, W+1, 20)], 1.6))
    soil = [line(wave(G+42, 4, 1.7), 1.0)]
    for i in range(380):
        x = r.uniform(0, W); y = r.uniform(gy(x)+5, G+38)
        soil.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="1.1" stroke-width="1.1"></circle>')
    aq = [line(wave(G+132, 9, 2.1), 1.1), line(wave(H-28, 7, 2.9), 1.1)]
    for i in range(520):
        x = r.uniform(0, W); y = r.uniform(G+52, G+122)
        aq.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="0.9" stroke-width="0.9"></circle>')
    for i in range(170):
        x = r.uniform(0, W-10); y = r.uniform(G+148, H-40)
        aq.append(f'<path d="M{f(x)} {f(y)} l10 0" stroke-width="0.8"></path>')
    return (f'<g style="color:#1F4A36">{"".join(surf)}</g><g style="color:#7A5A3A">{"".join(soil)}</g><g style="color:#2F5A6F">{"".join(aq)}</g>')
S = 'fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"'
def lab(y, t, c): return f'<g><rect x="14" y="{y-22}" width="{round(len(t)*12.2+22)}" height="30" rx="5" fill="#F4F6F3" fill-opacity="0.93"/><text x="25" y="{y}" fill="{c}" font-family="system-ui,-apple-system,Segoe UI,Roboto,sans-serif" font-size="21" font-weight="700">{t}</text></g>'
inner = re.sub(r'(\d+\.\d)', lambda m: m.group(1).rstrip('0').rstrip('.'), cross())
svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 380" role="img" aria-labelledby="t d">'
 '<title id="t">Cross-section of the Carrizo-Wilcox Aquifer</title>'
 '<desc id="d">Longleaf pines and grasses on the surface, a layer of topsoil, then the Carrizo sand and the Wilcox formation below. Not to scale.</desc>'
 f'<rect width="1400" height="380" fill="#F4F6F3"/><g {S}>{inner}</g>'
 + lab(124,"Piney Woods","#1F4A36") + lab(181,"Topsoil","#7A5A3A") + lab(246,"Carrizo sand","#2F5A6F") + lab(336,"Wilcox","#2F5A6F") + '</svg>')
open("assets/aquifer-section.svg", "w").write(svg)
print("drawing written, fingerprint", hashlib.md5(svg.encode()).hexdigest())
def fig(caption):
    return ('<!--aquifer:start-->\n<figure class="aquifer" style="margin:1.4rem 0">'
            '<img src="/assets/aquifer-section.svg" alt="Cross-section: longleaf pines and topsoil on the surface, with the Carrizo sand and the Wilcox formation underneath. Not to scale." '
            'style="display:block;width:100%;height:clamp(200px,27vw,380px);object-fit:cover;object-position:left center;border-radius:8px">'
            f'<figcaption style="margin-top:6px;font-size:.9em;color:#555">{caption}</figcaption></figure>\n<!--aquifer:end-->')
def place(path, html, before=None):
    s = open(path).read()
    if "<!--aquifer:start-->" in s:
        a = s.index("<!--aquifer:start-->"); b = s.index("<!--aquifer:end-->") + len("<!--aquifer:end-->")
        s = s[:a] + html + s[b:]
    elif before:
        i = s.find(before); assert i >= 0, before + " not found in " + path
        s = s[:i] + html + "\n" + s[i:]
    else:
        i = s.find('class="joinbox'); assert i >= 0, "alert box not found in " + path
        j = s.find("</div>", i) + len("</div>")
        s = s[:j] + "\n" + html + s[j:]
    open(path, "w").write(s); print(path, "has the cross-section")
place("texas.html", fig("Not to scale. The Carrizo-Wilcox Aquifer lies under the Piney Woods. It is the water these projects ask to pump."))
place("angelina/index.html", fig("Not to scale. The water under Angelina County: the Carrizo-Wilcox Aquifer."), before="<!--records:start-->")
b = open("tools/batch68.py").read()
OLD = "f'{docs_html}</li>')"
NEW = "f'{docs_html}' + ''.join(f'<p style=\"margin:6px 0 0;color:#555\">{E(n)}</p>' for n in (r.get(\"privacy_notes\") or [])) + '</li>')"
if NEW not in b:
    assert b.count(OLD) == 1, "batch68 line not found"; open("tools/batch68.py", "w").write(b.replace(OLD, NEW))
print("Batch 70: cross-section on the map and Angelina page; privacy notes added to batch 68")
