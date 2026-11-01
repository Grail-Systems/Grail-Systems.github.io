"""County alerts sign-up box: add to the main map (under the heading) and to every county page (just above 'What's changed lately')."""
import re, glob
FORM = "https://forms.gle/XCe1hun4F9XBkCYdA"
def box(label):
    return ('<div class="joinbox noprint" style="margin:1rem 0 1.4rem;padding:1rem 1.2rem;border:2px solid var(--pine,#1f4a36);border-radius:10px">'
            '<a href="' + FORM + '" target="_blank" rel="noopener" style="display:inline-block;background:var(--pine,#1f4a36);color:#fff;font-weight:800;padding:.7rem 1.1rem;border-radius:8px;text-decoration:none">Get alerts for ' + label + ' &rarr;</a>'
            '<p style="margin:.6rem 0 0">Two minutes. Get an email when something new shows up in ' + label + '. We never publish or share your information.</p></div>\n')
MARK = 'class="joinbox'
# main map: right after the hero block
s = open("texas.html").read()
if MARK not in s:
    i = s.find('<div class="hero">'); assert i >= 0, "map hero not found"
    j = s.find("\n</div>", i); assert 0 < j - i < 4000, "map hero end not found"
    j += len("\n</div>")
    s = s[:j] + "\n" + box("your county") + s[j:]
    open("texas.html", "w").write(s); print("texas.html updated")
else: print("texas.html already done")
# county pages: just above the changes feed
done = skip = 0
for f in sorted(glob.glob("*/index.html")):
    s = open(f).read()
    m = re.search(r'<section id="changes" data-county="([^"]+)"', s)
    if not m: continue
    if MARK in s: skip += 1; continue
    s = s[:m.start()] + box(m.group(1) + " County") + "  " + s[m.start():]
    open(f, "w").write(s); done += 1
print("county pages updated:", done, " already done:", skip)
t = open("tools/county_template.html").read()
print("template has changes feed:", 'id="changes"' in t, " (if False, new county pages get the box by rerunning this batch)")
print("Batch 67: county alert box on the map and county pages")
