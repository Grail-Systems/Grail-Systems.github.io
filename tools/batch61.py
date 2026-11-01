"""Pacifico Cedar Creek pin: move from east of Bastrop to the Earl Callahan Road area south of Cedar Creek; mark approximate on the card."""
T = [
 ('{name:"Pacifico Cedar Creek Campus", county:"Bastrop", type:"data", status:"announced", lat:30.110, lng:-97.320,',
  '{name:"Pacifico Cedar Creek Campus", county:"Bastrop", type:"data", status:"announced", lat:29.99, lng:-97.48,'),
 ('the county asked TCEQ for a public meeting on the air permit. Same developer as Fort Spunky in Hood County."',
  'the county asked TCEQ for a public meeting on the air permit. Same developer as Fort Spunky in Hood County. Pin is approximate."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Pacifico Cedar Creek pin</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>The Pacifico Cedar Creek pin sat east of Bastrop, about 13 miles from the site. The project is at 382 Earl Callahan Road, south of Cedar Creek and about 7 miles south of the EdgeConneX campuses. The pin has been moved; it remains approximate.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 61: Pacifico Cedar Creek pin moved south of Cedar Creek")
