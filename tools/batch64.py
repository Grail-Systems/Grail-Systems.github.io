"""Know Your Tools: add tool 11, checking the state's permit records (TCEQ STEERS shutdown, Oct 2026). Then print how the updates log is stored, read-only."""
import re, os
f = "know-your-tools.html"; s = open(f).read()
NEW = ('<section class="tool"><h2>11. Check the state&#x27;s permit records yourself</h2>'
 '<p>TCEQ keeps public records of the permits it issues, including stormwater, wastewater and air permits. Anyone can check whether approvals match what officials say is happening.</p>'
 '<p class="ex"><b>Where it worked:</b> After the governor ordered a pause on data center permits on Sept. 21, 2026, Public Citizen and FracTracker Alliance found permits still being approved through TCEQ&#x27;s automated system. TCEQ suspended at least 17 stormwater and wastewater permits and shut down its STEERS filing portal in October 2026. Air permits for gas plants, which require public notice, were not part of the suspension, so they are still worth watching.</p>'
 '<p class="src"><a href="https://www.texastribune.org/2026/10/21/data-center-permits-tceq-texas/">Texas Tribune, Oct 21, 2026</a> \u00b7 <a href="https://www.marfapublicradio.org/news/2026-10-22/tceq-closes-online-permitting-system-after-watchdogs-accuse-agency-of-violating-data-center-pause">Marfa Public Radio, Oct 22, 2026</a></p></section>')
if "11. Check the state" not in s:
    m = re.search(r'<section class="tool"><h2>10\. .*?</section>', s, re.S)
    assert m, "tool 10 not found"
    s = s[:m.end()] + "\n" + NEW + s[m.end():]
    s = s.replace("Ten tools", "Eleven tools")
    open(f, "w").write(s)
print("Batch 64: Know Your Tools now has 11 tools (TCEQ permit check)")
print("--- updates log storage (read-only) ---")
for c in ["updates.html", "data/updates.json"]:
    print(c, "exists" if os.path.exists(c) else "missing")
if os.path.exists("data/updates.json"):
    print(open("data/updates.json").read()[:600])
