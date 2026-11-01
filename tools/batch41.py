"""Originals batch 41: Abernathy. Aligned's Project Caprock (540 MW, Xcel/SPP) and TeraWulf/Fluidstack (168 MW, Google-backed lease) are two separate campuses."""
import json
L = {
 "Project Caprock (Abernathy)": [
   ["Aligned: groundbreaking on Project Caprock, 540 MW on 313 acres (Apr 2026)", "https://aligneddc.com/?p=9019"],
   ["Data Center Dynamics: Aligned breaks ground near Abernathy", "https://www.datacenterdynamics.com/en/news/aligned-breaks-ground-on-540mw-data-center-campus-in-texas"],
   ["W.Media: six buildings, 1.65 million sq ft, $5B", "https://w.media/project-caprock-aligned-data-centers-breaks-ground-on-540-mw-dc-campus-in-texas/"]],
 "TeraWulf / Fluidstack Abernathy": [
   ["Data Center Dynamics: TeraWulf and Fluidstack venture, Google backs $1.3B of the lease", "https://www.datacenterdynamics.com/en/news/terawulf-and-fluidstack-to-develop-texas-data-center-in-google-backed-deal/"],
   ["Baxtel: 168 MW IT (240 MW gross) on 120 acres, due second half of 2026", "https://baxtel.com/posts/terawulf-and-fluidstack-to-develop-texas-data-center"],
   ["Cooley: the tenant is a frontier AI model developer (Oct 2025)", "https://www.cooley.com/news/coverage/2025/2025-10-28-fluidstack-announces-joint-venture-with-terawulf"],
   ["Cleanview: tracker entry naming the customer as Anthropic", "https://cleanview.co/data-centers/texas/1875/abernathy-data-center-fluidstack--anthropic"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
a = d["Project Caprock (Abernathy)"]
a["loc"] = "Just outside Abernathy, Hale County; served by Xcel Energy (Southwest Power Pool, not ERCOT)"
a["acres"] = "313 acres"
a["llc"] = "Aligned Data Centers"
a["dates"] = "Target reported Feb 2026; ground broken Apr 2026; six buildings, 1.65 million sq ft"
t = d["TeraWulf / Fluidstack Abernathy"]
t["loc"] = "Abernathy, Hale County, about 2 miles from Aligned's Project Caprock (exact site not confirmed; may be Outlaw Ventures' 120-acre site)"
t["acres"] = "About 120 acres"
t["llc"] = "Joint venture: TeraWulf 51%, Fluidstack 49%; Google backs about $1.3B of Fluidstack's lease"
t["dates"] = "Announced Oct 28, 2025; 25-year lease; delivery expected second half of 2026"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Aligned Data Centers", power:"540 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Aligned Data Centers", power:"540 MW, from Xcel Energy on the Southwest Power Pool grid, not ERCOT", water:"Not disclosed", conf:"Reporting", note:"Ground broken April 2026 on 313 acres just outside Abernathy: six buildings, about $5B. A separate campus from TeraWulf and Fluidstack, about 2 miles away."'),
 ('dev:"TeraWulf and Fluidstack", power:"168 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"TeraWulf (51%) and Fluidstack (49%), with Google backing $1.3B of the lease", power:"168 MW of computing (about 240 MW total)", water:"Not disclosed", conf:"Reporting", note:"About 120 acres, due in the second half of 2026 under a 25-year lease. The companies describe the customer only as a developer of frontier AI models; one industry tracker names it as Anthropic. A separate campus from Aligned\'s Project Caprock."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 41: Abernathy (Aligned Project Caprock; TeraWulf/Fluidstack, Google-backed) checked")
