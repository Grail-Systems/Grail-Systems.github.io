"""Source batch 2: Young, El Paso, McLennan, Taylor and Dickens cards, from the company research."""
import json
L = {
 "Project Saltworks": [["Data Center Dynamics: the 867-acre proposal", "https://www.datacenterdynamics.com/en/news/developer-proposes-867-acre-project-saltworks-data-center-in-graham-texas/"],
   ["Olney Enterprise: Stream buys Plug Power's site", "https://www.olneyenterprise.com/news/stream-plug-power-deal-moves-young-county-data-center-closer-reality"],
   ["Olney Enterprise: abatement talks collapse", "https://www.olneyenterprise.com/main-news/graham-seeks-data-center-safeguards-after-county-abatement-talks-collapse"],
   ["More Than Just Parks tracker entry", "https://morethanjustparks.com/data-center-tracker/project-saltworks-headwaters-site-development-stream-data-centers-tx--c51b3dea-975e-445a-aef3-4571817436a3"]],
 "Meta El Paso": [["Texas Tribune: the gas plant for Meta (Jan 26, 2026)", "https://www.texastribune.org/2026/01/26/texas-el-paso-meta-data-center-natural-gas-power-plant/"],
   ["Inside Climate News: judges' findings on the gas plant (Sept 24, 2026)", "https://insideclimatenews.org/news/24092026/el-paso-electric-only-considered-gas-to-power-meta-data-center/"],
   ["KFOX: Meta's water and grid pledges", "https://kfoxtv.com/news/local/meta-touts-10b-el-paso-data-center-water-and-grid-pledges-as-council-weighs-incentives"]],
 "Infrakey Lacy Lakeview": [["Texas Tribune: who is behind Infrakey (Nov 24, 2025)", "https://www.texastribune.org/2025/11/24/texas-waco-data-center-project/"],
   ["KSAT / Texas Tribune: Lacy Lakeview needs Waco (May 14, 2026)", "https://www.ksat.com/news/texas/2026/05/14/lacy-lakeview-needs-wacos-help-to-realize-its-data-center-dreams-its-not-going-well/"],
   ["Data Center Dynamics: the 925 MW data district", "https://datacenterdynamics.com/en/news/infrakey-city-of-lacy-lakeview-unveil-925mw-data-center-district-in-mclennan-county-texas/"]],
 "Stargate Abilene": [["Tom's Hardware: expansion dropped; Oracle's response (Mar 2026)", "https://tomshardware.com/tech-industry/oracle-rebuts-incorrect-reporting-on-stargate-expansion"],
   ["SDxCentral: Crusoe builds on Lancium land for Oracle", "https://www.sdxcentral.com/news/openai-and-oracle-to-deploy-64000-gb200-gpus-at-stargate-abilene-data-center-by-2026-report/"]],
 "Galaxy Helios": [["KCBD: Phase I delivered to CoreWeave (July 10, 2026)", "https://www.kcbd.com/2026/07/10/galaxy-completes-phase-i-its-helios-data-center-campus-delivering-133-megawatts-critical-it-load-coreweave/"],
   ["KTSM: $3.5 billion Phase 2 permits (Mar 2026)", "https://www.ktsm.com/news/state-news/massive-3-5-billion-expansion-planned-at-ai-data-center-in-dickens-county/amp/"],
   ["Data Center Dynamics: $1.4 billion financing", "https://www.datacenterdynamics.com/en/news/galaxy-digital-closes-14bn-debt-facility-for-helios-data-center-campus-in-texas/"]],
}
DATES = {
 "Project Saltworks": "Announced July 2026; 15 buildings, about $10B. Stream agreed to buy Plug Power's canceled hydrogen site and its grid connection for up to $76.5M (July 2026). Young County accepted its tax abatement application in Aug 2026; Stream later abandoned the abatement talks.",
 "Infrakey Lacy Lakeview": "$10B proposal; town hall Dec 2025; Lacy Lakeview approved a non-binding agreement 6 to 1 (Dec 2025). Depends on Waco releasing the land and supplying treated wastewater; no deal with Waco as of May 2026.",
 "Galaxy Helios": "Phase I (133 MW for CoreWeave) delivered July 2026. Approved for 1.63 GW in total. $3.5B in Phase 2 permits filed Mar 2026.",
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
for k, v in DATES.items(): d[k]["dates"] = v
m = d["Meta El Paso"]
if "judges" not in m.get("dates", ""):
    m["dates"] = m.get("dates", "") + ". El Paso Electric's 366 MW gas plant for the campus: judges found in Sept 2026 that the utility weighed no alternatives and sought no bids."
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
print("Batch 2: 5 cards linked, 4 cards' key dates updated")
