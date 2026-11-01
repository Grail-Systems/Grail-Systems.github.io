"""Originals batch 28: Pecos County. Project Horizon (Poolside; CoreWeave deal fell apart) and Amazon's GW Ranch (Pacifico Energy)."""
import json
L = {
 "Project Horizon (Longfellow Ranch)": [
   ["Poolside: announcing Project Horizon (Oct 15, 2025)", "https://poolside.ai/blog/announcing-project-horizon"],
   ["Data Center Dynamics: Poolside seeks new partners after the CoreWeave deal falls apart", "https://www.datacenterdynamics.com/en/news/poolside-seeks-partners-for-data-center-in-texas-after-coreweave-deal-falls-apart/"],
   ["Data Center Dynamics: 568 acres on the Mitchell family's Longfellow Ranch", "https://www.datacenterdynamics.com/en/news/ai-startup-poolside-teams-up-with-coreweave-on-2gw-data-center-in-texas/"]],
 "Amazon GW Ranch gas-power campus": [
   ["Marfa Public Radio: Pacifico builds the gas plant and data center for Amazon; now eyeing Brewster County", "https://www.marfapublicradio.org/news/2026-09-18/developer-behind-amazons-pecos-county-data-center-approaches-brewster-county-officials"],
   ["KFDA: TCEQ approves what the developer calls the largest permitted data center campus in the U.S.", "https://www.newschannel10.com/2026/02/01/texas-approves-largest-permitted-data-center-campus-us"],
   ["POWER Magazine: an off-grid gas and battery complex of nearly 7 GW", "https://www.powermag.com/tag/gw-ranch/"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
h = d["Project Horizon (Longfellow Ranch)"]
h["loc"] = "Part of the Mitchell family's 500,000-acre Longfellow Ranch, more than 25 miles outside Fort Stockton, unincorporated Pecos County"
h["acres"] = "About 560 to 568 acres"
h["llc"] = "Poolside (AI startup); infrastructure spun out as Poolside Infrastructure Company in 2026"
h["dates"] = "Announced Oct 15, 2025 with CoreWeave as anchor tenant (250 MW, 15 years). In 2026 the CoreWeave deal fell apart; Poolside has been in talks with other cloud providers, including Google. Poolside says the site could eventually reach 10 GW"
g = d["Amazon GW Ranch gas-power campus"]
g["loc"] = "Pecos County"
g["acres"] = "About 8,000 acres"
g["llc"] = "Pacifico Energy, developing the power plant and data center campus for Amazon"
g["dates"] = "TCEQ approved the project's air permit around Jan 2026; the developer calls it the largest permitted data center campus in the U.S. In Sept 2026 Pacifico pitched a similar project on an 8,400-acre ranch in the Glass Mountains of Brewster County"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Poolside / CoreWeave", power:"2 GW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Poolside (CoreWeave dropped out in 2026)", power:"2 GW planned from on-site gas, in eight 250 MW phases", water:"Not disclosed", conf:"Reporting", note:"On the Mitchell family\'s Longfellow Ranch, 25+ miles outside Fort Stockton. Its anchor tenant, CoreWeave, walked away in 2026; Poolside is looking for a new partner. Shows how fast these deals can change."'),
 ('dev:"Amazon", power:"Gas-powered campus; size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Pacifico Energy, for Amazon", power:"GW Ranch gas plant planned at about 7.65 GW, off the grid, with batteries", water:"Not disclosed", conf:"Reporting", note:"About 8,000 acres. TCEQ approved it in early 2026; the developer calls it the largest permitted data center campus in the U.S. Pacifico is now pitching a similar plant in Brewster County\'s Glass Mountains."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 28: Project Horizon and Amazon GW Ranch checked against originals")
