"""New cards found during verification: Sabey Oklaunion and GDA Rowdy (Wilbarger), Calvano and DataNovaX (Wichita Falls)."""
import json
NEW = {
 "Sabey Oklaunion": {"loc": "Oklaunion, Wilbarger County, east of Vernon (exact site not published)", "llc": "Sabey Data Centers", "dates": "Described by Sabey as an upcoming development; trackers list it as land secured for future development",
   "links": [["Data Center Dynamics: Sabey describes its upcoming Oklaunion development", "https://datacenterdynamics.com/en/marketwatch/the-texas-nexus"], ["Baxtel: Sabey Oklaunion, land secured for future development", "https://baxtel.com/data-center/sabey-oklaunion"]]},
 "GDA Rowdy (Vernon)": {"loc": "Near Vernon, Wilbarger County, served by the Oklaunion substation", "llc": "Genesis Digital Assets", "dates": "Operating since 2024 at about 60 MW, with expansions through 2026",
   "links": [["Bitcoin Magazine: GDA's Rowdy site operating at 60 MW off the Oklaunion substation", "https://bitcoinmagazine.com/?p=389"], ["Baxtel: GDA expanding its Rowdy data center in Vernon", "https://baxtel.com/data-center/gda-rowdy-data-center"]]},
 "Calvano data center (Wichita Falls)": {"loc": "Northwest Freeway near City View Drive, Wichita Falls, next to an Oncor facility", "llc": "Calvano Development (Mark Calvano)", "dates": "Wichita Falls City Council approved the rezoning in 2026; planned for a single tenant, up to 2.3 million sq ft",
   "links": [["Data Center Dynamics: Wichita Falls council approves rezoning for 300 MW data center", "https://www.datacenterdynamics.com/en/news/wichita-falls-council-approves-land-rezoning-for-300mw-data-center-in-texas/"]]},
 "DataNovaX (Airport Drive)": {"loc": "2236 Airport Drive, Wichita Falls (former grocery store and call center), near Sheppard Air Force Base", "acres": "About 37,000 sq ft in an existing building", "llc": "DataNovaX", "dates": "Planning and Zoning Commission approved a conditional use, with conditions, Aug 2026",
   "links": [["KAUZ: DataNovaX data center approved for Airport Drive (Aug 2026)", "https://www.newschannel6now.com/2026/08/13/datanovax-data-center-approved-airport-drive-wichita-falls/"]]},
}
p = "data/details.json"; d = json.load(open(p))
for k, v in NEW.items():
    if k not in d: d[k] = v
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
CARDS = (',\n'
 '  {name:"Sabey Oklaunion", county:"Wilbarger", type:"data", status:"announced", lat:34.13, lng:-99.13,\n'
 '   dev:"Sabey Data Centers", power:"Size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Land Sabey is holding for a future campus near Oklaunion, a few miles from Google\'s Vernon campus and an operating bitcoin mine. The same developer behind the San Marcos and Round Rock projects. Pin is approximate.", src:"Data Center Dynamics; Baxtel"},\n'
 '  {name:"GDA Rowdy (Vernon)", county:"Wilbarger", type:"crypto", status:"operating", lat:34.15, lng:-99.18,\n'
 '   dev:"Genesis Digital Assets", power:"About 60 MW, expanding", water:"Not disclosed", conf:"Reporting", note:"A bitcoin mine operating near Vernon since 2024, fed by the Oklaunion substation. With Google\'s campus and Sabey\'s planned site nearby, Wilbarger County now has three. Pin is approximate.", src:"Bitcoin Magazine; Baxtel"},\n'
 '  {name:"Calvano data center (Wichita Falls)", county:"Wichita", type:"data", status:"approved", lat:33.94, lng:-98.55,\n'
 '   dev:"Calvano Development", power:"300 MW reported", water:"Not disclosed", conf:"Reporting", note:"Rezoning approved by the Wichita Falls City Council for a single-tenant hyperscale building of up to 2.3 million sq ft, placed beside an Oncor facility on purpose. The tenant has not been named. Pin is approximate.", src:"Data Center Dynamics"},\n'
 '  {name:"DataNovaX (Airport Drive)", county:"Wichita", type:"data", status:"approved", lat:33.975, lng:-98.495,\n'
 '   dev:"DataNovaX", power:"Small; size not disclosed", water:"Not disclosed", conf:"Reporting", note:"A small data center reusing an empty grocery store and call center building, approved with conditions in August 2026. Right next to the Airport Drive site the city rejected three months earlier: a contrast worth noting.", src:"KAUZ"}')
s = open("texas.html").read()
if 'name:"Sabey Oklaunion"' not in s:
    anchor = '\n];\n\nconst actions'
    assert s.count(anchor) == 1, "array end not found"
    s = s.replace(anchor, CARDS + anchor, 1)
    open("texas.html", "w").write(s)
print("Batch 53: four new cards (Sabey Oklaunion, GDA Rowdy, Calvano, DataNovaX)")
