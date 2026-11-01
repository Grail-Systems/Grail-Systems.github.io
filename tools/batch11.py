"""Originals batch 11: Wichita Falls Business Park (Skybox), checked against KAUZ and Data Center Dynamics."""
import json
K = "Wichita Falls Business Park data center"
L = [["KAUZ: Skybox groundbreaking pushed to early 2027 (Oct 6, 2026)", "https://www.newschannel6now.com/2026/10/06/skybox-data-center-project-delayed-company-provides-wichita-falls-update/"],
     ["KAUZ: Skybox named as developer (Feb 19, 2026)", "https://www.newschannel6now.com/2026/02/19/skybox-data-centers-announced-developer-wichita-falls-first-data-center"],
     ["KAUZ: city approves record land sale (Oct 8, 2025)", "https://www.newschannel6now.com/2025/10/08/city-wichita-falls-approves-record-land-sale-data-center/"],
     ["Data Center Dynamics: Skybox bought 225 acres for $14.5M", "https://www.datacenterdynamics.com/en/news/skybox-to-develop-data-center-campus-in-wichita-falls-texas/"]]
p = "data/details.json"; d = json.load(open(p)); e = d.setdefault(K, {})
have = {u for _, u in e.get("links", [])}
e.setdefault("links", []).extend(x for x in L if x[1] not in have)
e["llc"] = "Texas Data Centers Campus LLC (Skybox Datacenters)"
e["acres"] = "About 225 acres bought from the Wichita Falls Economic Development Corp. for more than $14.5M"
e["dates"] = "City approved the land sale Oct 2025; Skybox named developer Feb 2026 (\"PowerCampus\"); groundbreaking delayed to early 2027 after the governor's statewide data center audit (Oct 2026)"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
old = 'dev:"Texas Data Center Campus LLC", power:"800 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."'
new = 'dev:"Skybox Datacenters, through Texas Data Centers Campus LLC", power:"Skybox markets 300+ MW; the tracker lists 800 MW", water:"Not disclosed", conf:"Reporting", note:"Six to 10 buildings; Skybox says 300 to 500 permanent jobs and 2,000 to 3,000 construction workers. Groundbreaking pushed to early 2027 after the state audit."'
s = open("texas.html").read()
if new not in s:
    assert s.count(old) == 1, "not found"; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 11: Wichita Falls (Skybox) checked against originals")
