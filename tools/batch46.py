"""Originals batch 46: Cipher Mikeska (one of four 500 MW Cipher 'options', timeline slipping) and InfraTech Carson County ($2.7B, 5,000 acres, every partner unnamed)."""
import json
L = {
 "Cipher Mikeska HPC data center": [
   ["Data Center Dynamics: Cipher holds options on Mikeska, Milsing and McLennan, 500 MW each, to energize 2027", "https://www.datacenterdynamics.com/en/news/cipher-mining-acquires-more-than-500-acres-across-two-sites-in-texas-for-crypto-and-hpc-use"],
   ["Data Center Dynamics: Fluidstack as customer and Google as investor in Cipher", "https://www.datacenterdynamics.com/en/news/cipher-mining-secures-fluidstack-as-a-customer-and-google-as-an-investor/"],
   ["Baxtel: Mikeska, a 100-acre property outside Brady, now planned 2028 with expansions to 2030", "https://baxtel.com/data-center/cipher-digital-mikeska"]],
 "InfraTech Capital campus": [
   ["KFDA: proposed $2.7 billion data center announced for Carson County (Aug 18, 2026)", "https://www.newschannel10.com/2026/08/18/proposed-27-billion-data-center-announced-carson-county/"],
   ["Data Center Dynamics: more than 5,000 acres near Amarillo", "https://www.datacenterdynamics.com/en/news/infratech-to-invest-27bn-to-develop-data-center-campus-in-carson-county-texas/"],
   ["Construction Review: no final investment decision and no construction date", "https://constructionreviewonline.com/proposed-2-7b-5000-acre-data-center-campus-advances-in-carson-county-texas/"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
m = d["Cipher Mikeska HPC data center"]
m["loc"] = "Outside Brady, McCulloch County; address listed as East County Road 368 (Doole area). Pin approximate"
m["acres"] = "About 100 acres"
m["llc"] = "Cipher Digital (formerly Cipher Mining), backed in part by Google and SoftBank"
m["dates"] = "Held as an option site since at least 2024 with power expected 2027; trackers now list 2028 with expansions to 2030"
i = d["InfraTech Capital campus"]
i["loc"] = "Carson County near Amarillo (exact site not published); same county as Fermi America's Project Matador"
i["acres"] = "More than 5,000 acres"
i["llc"] = "InfraTech Capital (CEO Luiz Fuschini); data center partner, tenant and co-investors not named"
i["dates"] = "Announced Aug 18, 2026; no final investment decision or construction date"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Cipher Digital", power:"500 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Cipher Digital (formerly Cipher Mining)", power:"500 MW planned", water:"Not disclosed", conf:"Reporting", note:"About 100 acres outside Brady, first bought as a bitcoin mining site. One of three Cipher option sites in Texas marketed at 500 MW each (with Milsing and McLennan); Cipher also plans Colchis near San Angelo. Power was promised for 2027; trackers now say 2028 to 2030. Pin is approximate."'),
 ('dev:"InfraTech Capital", power:"Campus; size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Same county as Fermi America. Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"InfraTech Capital", power:"Size not disclosed", water:"Not disclosed", conf:"Reporting", note:"A proposed $2.7B campus on more than 5,000 acres near Amarillo, announced August 2026. The tenant, the data center partner and the co-investors are all unnamed, and there is no construction date. Same county as Fermi America\'s Project Matador."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 46: Cipher Mikeska (option site, slipping) and InfraTech Carson ($2.7B, all partners unnamed) checked")
