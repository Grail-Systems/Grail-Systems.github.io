"""Originals batch 42: Fluidstack Cameron County. Under construction near Rio Hondo after a county worksite permit; project shifted out of Harlingen's reach."""
import json
K = "FluidStack Cameron County campus"
L = [
 ["KRGV: Fluidstack breaks ground on $4B campus near Harlingen (Sept 10, 2026)", "https://www.krgv.com/news/fluidstack-breaks-ground-on-4-billion-data-center-project-in-cameron-county"],
 ["KRGV: Harlingen tables Fluidstack drainage request after public pushback (Sept 4, 2026)", "https://www.krgv.com/news/harlingen-tables-fluidstack-data-center-drainage-request-after-public-pushback"],
 ["Telemundo 40: a permit changed the project, and now Harlingen is left out", "https://www.telemundo40.com/noticias/local/el-centro-de-datos-de-fluidstack-avanza-fuera-de-harlingen/2544864/"],
 ["KRGV: concerns over water and power along FM 106; county's limited zoning authority", "https://www.krgv.com/news/concerns-arise-over-data-center-s-water-and-power-usage-in-cameron-county"],
 ["Construction Review: more than 1,100 acres near Rio Hondo; first project in the county to start building", "https://constructionreviewonline.com/fluidstack-starts-site-work-on-4-billion-cameron-county-ai-data-center-campus/"],
 ["Valley Morning Star via GovTech: Harlingen sets 120-day moratorium on data center applications", "https://www.govtech.com/artificial-intelligence/south-texas-city-sets-moratorium-amid-data-center-interest"],
]
p = "data/details.json"; d = json.load(open(p))
e = d.setdefault(K, {}); have = {u for _, u in e.get("links", [])}
e.setdefault("links", []).extend(x for x in L if x[1] not in have)
e["loc"] = "Along FM 106 near Rio Hondo, unincorporated Cameron County (Harlingen area); about 6 miles from the Lower Rio Grande Valley National Wildlife Refuge"
e["acres"] = "More than 1,100 acres"
e["llc"] = "Fluidstack (the same AI cloud company leasing the TeraWulf campus in Abernathy)"
e["dates"] = "Harlingen tabled a drainage request after public pushback Sept 4, 2026; county issued a worksite permit and site work began Sept 10, 2026; more permits needed before buildings go up. Harlingen has a 120-day moratorium on data center applications"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('{name:"FluidStack Cameron County campus", county:"Cameron", type:"data", status:"announced", lat:26.1, lng:-97.5,\n   dev:"FluidStack", power:"1.5 GW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  '{name:"FluidStack Cameron County campus", county:"Cameron", type:"data", status:"construction", lat:26.23, lng:-97.55,\n   dev:"Fluidstack", power:"1.5 GW listed; first phase $4B", water:"Company promises closed-loop cooling; water from the East Rio Hondo Water Supply Corporation", conf:"Reporting", note:"More than 1,100 acres along FM 106 near Rio Hondo. After Harlingen tabled the company\'s drainage request following public pushback, the project went ahead in unincorporated county land, where the county says it has little zoning power. Site work began in September 2026 on a county worksite permit. Harlingen now has a moratorium on new data center applications."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Fluidstack, Cameron County</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We showed Fluidstack\'s campus as announced, pinned south of its site. Site work began in September 2026 along FM 106 near Rio Hondo. Status changed to under construction and the pin moved about 10 miles north; the exact parcel is not published.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 42: Fluidstack Cameron County (under construction, went around Harlingen) checked")
