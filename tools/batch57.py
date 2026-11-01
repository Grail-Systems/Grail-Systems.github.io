"""Build the Know Your Tools page (/know-your-tools) from lessons verified in the Texas Watch originals check. Reuses the checklist page's header and menu."""
import re
ck = open("checklist.html").read()
nav = re.search(r'<nav class="top">.*?</nav>', ck, re.S).group(0)
head_links = re.search(r'(<link rel="preconnect".*?<link rel="stylesheet" href="/assets/watch.css">)', ck, re.S).group(1)
TOOLS = [
 ("Ask who the end user is",
  "If the developer will not say who will actually use the facility, that is a legitimate reason to say no.",
  "Wichita Falls City Council voted unanimously in May 2026 against rezoning land beside homes for a data center whose operator was never identified. Councilors cited the homes and the unknown developer.",
  [("KAUZ: Wichita Falls rejects Airport Drive rezoning", "https://newschannel6now.com/2026/05/05/wichita-falls-city-council-rejects-airport-drive-data-center-rezoning/")]),
 ("File a written zoning protest (city rezoning only)",
  "When a city is asked to rezone land, nearby owners can file a formal written protest. Under Texas Local Government Code section 211.006, if the owners of at least 20 percent of the land within 200 feet of the property protest, the change needs a three-fourths vote of the city council instead of a simple majority. Ask your city secretary for the exact rules and deadline.",
  "In Hutto, residents organized as Stop the Hutto Data Center and filed written protests against rezoning apartment land for a 70 MW data center. A week later, in April 2026, the developer withdrew.",
  [("KUT: Hutto developer withdraws, ending the project", "https://www.kut.org/energy-environment/2026-04-20/hutto-tx-zydeco-data-center-rezoning-request")]),
 ("Watch unincorporated county land",
  "City rules and city moratoriums stop at the city limits. Texas counties generally have no zoning power, so projects that meet resistance in town often move just outside it.",
  "After Harlingen tabled a drainage request from Fluidstack following public pushback in September 2026, the company began building a $4B campus on unincorporated county land near Rio Hondo with only a county worksite permit.",
  [("KRGV: Harlingen tables Fluidstack drainage request", "https://www.krgv.com/news/harlingen-tables-fluidstack-data-center-drainage-request-after-public-pushback"),
   ("KRGV: Fluidstack breaks ground in Cameron County", "https://www.krgv.com/news/fluidstack-breaks-ground-on-4-billion-data-center-project-in-cameron-county")]),
 ("A withdrawn tax break is not a retreat",
  "A developer can drop its tax break request and keep building, which removes the county's main bargaining table. Keep other levers in view: road use agreements, public meetings on air permits, and every state permit.",
  "In Bastrop County, Pacifico's Cedar Creek developers withdrew their county tax break requests in August 2026, and the first building was filed to start construction that November. In Brazoria County, commissioners denied the Old Ocean project's tax break 5-0, and it can still go forward.",
  [("Elgin Courier: developers withdraw tax break requests", "https://www.elgincourier.com/article/4854,developers-withdraw-tax-break-requests"),
   ("CBS Austin: county asks TCEQ for a public meeting on the gas plant", "https://cbsaustin.com/news/local/bastrop-county-commissioners-ok-request-for-tceq-meeting-on-gas-plant-concerns")]),
 ("Require bonds and parent company guarantees",
  "Projects are often held by single-purpose companies that can go bankrupt or be sold. Agreements should require a bond or letter of credit for cleanup and road damage, and the parent company's guarantee.",
  "In Crystal City, a bitcoin mine in a leased warehouse caught fire, and its owner filed for bankruptcy in February 2026 while facing lawsuits from its own investors.",
  [("Data Center Dynamics: NFN8 files for bankruptcy after fire", "https://www.datacenterdynamics.com/en/news/cryptominer-nfn8-files-for-bankruptcy-following-data-center-fire-and-bitcoin-price-crash/")]),
 ("Lower-water designs exist in Texas",
  "When a developer says it needs fresh groundwater for cooling, point to Texas projects that do not.",
  "Google's campus near Vernon is air-cooled and designed to eliminate operational water use. Chevron has committed to brackish water, not fresh water, for the power plant it is planning for a Microsoft data center in West Texas.",
  [("KAUZ: Google's air-cooled Wilbarger County plan", "https://www.newschannel6now.com/2026/02/24/google-announces-new-clean-energy-data-center-agreement-with-wilbarger-county")]),
 ("Check old deeds before any deal",
  "Former industrial sites can carry deed restrictions that limit what can be built. Pull the deed history from the county clerk before anyone signs anything.",
  "In Sulphur Springs, a deed restriction barring power generation led to a court order that stopped construction on a data center campus.",
  [("Texas Watch map: Sulphur Springs card", "/texas")]),
 ("Keep tax abatement guidelines current",
  "Texas counties must adopt abatement guidelines before granting any abatement and review them every two years. Out-of-date guidelines can leave a county with no leverage, and current ones are where permanent standards belong.",
  "Nueces County's abatement guidelines were out of date when a large campus came forward near Robstown, so the county could not have offered one.",
  [("Texas Watch map: Beacon Point card", "/texas")]),
 ("Do not move faster than the state",
  "Texas is reviewing data center demand on the grid and pausing some permits. A county can reasonably wait for those reviews before signing long agreements.",
  "In September 2026 the state paused new data center permits while it reviews water and power use, and the ERCOT audit of large loads is expected to finish in December 2026.",
  [("KSAT: Texas pauses new data center permits", "https://www.ksat.com/news/local/2026/09/25/texas-pauses-new-data-center-permits-as-state-reviews-water-power-use-texas-has-temporarily-stopped-approving-constru/")]),
 ("Ask for the records",
  "Agreements a county signs, including nondisclosure agreements, are generally public information under the Texas Public Information Act. To withhold any part, the government generally has to ask the Attorney General for a ruling.",
  "Every County Watch page has a free tool that writes a records request for that county, city and groundwater district.",
  [("The checklist", "/checklist"), ("Records library", "/records")]),
]
def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
items = []
for i, (title, what, example, links) in enumerate(TOOLS, 1):
    ls = " · ".join('<a href="%s">%s</a>' % (u, esc(n)) for n, u in links)
    items.append('<section class="tool"><h2>%d. %s</h2><p>%s</p><p class="ex"><b>Where it worked:</b> %s</p><p class="src">%s</p></section>' % (i, esc(title), esc(what), esc(example), ls))
page = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Know Your Tools | Texas Watch</title>
<meta name="description" content="Ten tools Texans have used to get a fair deal, or a no, on data centers, crypto mines and power plants, each with a Texas example and its source.">
<meta property="og:title" content="Know your tools">
<meta property="og:description" content="Ten tools that have worked in Texas, each with a real example and a source.">
<meta property="og:url" content="https://grailsystems.io/know-your-tools">
<meta property="og:image" content="https://grailsystems.io/img/grail_share.jpg">
""" + head_links + """
<style>
.tool{margin:1.6rem 0;padding-top:1rem;border-top:1px solid rgba(127,127,127,.25)}
.tool h2{margin:.2rem 0 .5rem}
.tool .ex{color:var(--muted)}
.tool .src{font-size:.92rem}
@media print{nav.top,footer,.noprint{display:none}}
</style>
</head>
<body>
<div class="wrap">
""" + nav + """
<div class="hero">
  <h1>Know your tools</h1>
  <p>Ten tools Texans have used to get a fair deal, or a no, on data centers, crypto mines and power plants. Each one comes with a real Texas example and its source. This is general information, not legal advice; check the details with your county or city before you rely on them.</p>
</div>
""" + "\n".join(items) + """
<p class="noprint">Found a tool that worked in your county? Tell us at <a href="mailto:contact@grailsystems.io">contact@grailsystems.io</a>.</p>
<footer>
  <span>Know Your Tools · Texas Watch · Grail Systems</span>
  <a href="/texas">Texas Watch</a>
  <a href="/checklist">Checklist</a>
  <a href="/standards">The Standard</a>
  <a href="mailto:contact@grailsystems.io">contact@grailsystems.io</a>
</footer>
</div>
</body>
</html>
"""
open("know-your-tools.html", "w").write(page)
old = '<span>Checklist · Texas Watch · Grail Systems</span>'
if 'href="/know-your-tools"' not in ck:
    assert ck.count(old) == 1, "checklist footer not found"
    open("checklist.html", "w").write(ck.replace(old, old + '\n  <a href="/know-your-tools">Know your tools</a>', 1))
print("Batch 57: Know Your Tools page built (10 tools); linked from the checklist")
