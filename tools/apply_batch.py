import sys, json
sys.path.insert(0, "tools")
from mtjp_batch import D
p = "texas.html"
s = open(p).read()
J = json.dumps
out, skipped = [], 0
for row in D:
    name, county, typ, status, lat, lng, dev, power, note = row[:9]
    link = row[9] if len(row) > 9 else None
    if 'name:' + J(name) in s: skipped += 1; continue
    note = (note + " " if note else "") + "Listed by the More Than Just Parks tracker; needs verification."
    e = "  {name:%s, county:%s, type:%s, status:%s, lat:%s, lng:%s,\n   dev:%s, power:%s, water:\"Not disclosed\", conf:\"Reporting\", note:%s%s}" % (
        J(name), J(county), J(typ), J(status), lat, lng, J(dev), J(power), J(note), (", link:" + J(link)) if link else "")
    out.append(e)
if out:
    s = s.replace("\n];\n\nconst actions", ",\n" + ",\n".join(out) + "\n];\n\nconst actions", 1)

def setfield(name, field, value):
    global s
    i = s.find('name:"' + name + '"')
    if i < 0: print("missing", name); return
    j = s.find(field + ':"', i); k = s.find('"', j + len(field) + 2)
    s = s[:j] + field + ':"' + value + s[k:]
setfield("Stargate Milam County", "dev", "SB Energy, for OpenAI's Stargate")
setfield("Stargate Milam County", "power", "1.2 GW listed")
setfield("Stargate Milam County", "status", "construction")
setfield("Fort Bliss data center", "power", "3 GW listed")
setfield("RCM Hill data center", "power", "1.2 GW listed (Project Aquila)")
setfield("Infrakey Lacy Lakeview", "power", "925 MW listed")
setfield("Harlingen data center", "status", "stopped")
setfield("Harlingen data center", "dev", "Eneus Energy (RGV Data Center)")
setfield("Harlingen data center", "power", "2 GW listed")
setfield("Harlingen data center", "note", "Residents asked the City Commission to oppose it over water and power. A public tracker lists it as blocked by a moratorium; which government acted needs verification.")
setfield("Pacifico Cedar Creek Campus", "status", "stopped")
setfield("Pacifico Cedar Creek Campus", "power", "490 MW listed")
setfield("Pacifico Cedar Creek Campus", "note", "Same developer as Fort Spunky in Hood County. A public tracker lists it as blocked by a moratorium; which government acted needs verification.")
setfield("Project Saltworks", "dev", "Stream Data Centers, with Headwaters Site Development")

old = "One public tracker counts 465 data centers in Texas as of October 2026: 269 operating, 89 under construction and 107 proposed.</p>"
new = 'The <a href="https://morethanjustparks.com/data-center-tracker/state/texas">More Than Just Parks tracker</a> counts 466 data centers in Texas as of October 2026: 270 operating, 88 under construction and 108 proposed, each tied to a public source. Our map focuses on the large and contested projects; see their list for the full census.</p>'
if old in s: s = s.replace(old, new)
else: print("big picture sentence not found")
open(p, "w").write(s)
print("Added", len(out), "| skipped", skipped, "| total:", s.count("{name:"), "projects")
