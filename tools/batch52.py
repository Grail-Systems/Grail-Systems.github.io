"""Open facts: IREN Sweetwater county (Sweetwater 2 is in Fisher; Sweetwater 1 address 883 FM 611, county reported both ways) and Delta County (developer still unconfirmed; judge's water concerns, Cooper Lake)."""
import json
L = {
 "IREN Sweetwater 1": [
   ["Data Center Dynamics: Sweetwater 2, a 500-acre site outside Sweetwater in Fisher County", "https://www.datacenterdynamics.com/en/news/iren-plans-75mw-liquid-cooled-ai-data-center-in-texas/"],
   ["Datacenterhawk: Sweetwater 1 on Farm to Market 611", "https://datacenterhawk.com/marketplace/providers/iren/farm-to-market-611/sweetwater-1"]],
 "Delta County data center": [
   ["KETR: Delta County schedules a March 2 town hall; posts cite Cooper Lake water contracts", "https://www.ketr.org/news/2026-02-25/delta-county-schedules-march-2-town-hall-on-proposed-data-center"],
   ["KETR: county judge says the data center is not a good fit; water is his main concern", "https://www.ketr.org/news/2026-03-02/delta-county-judge-says-data-center-not-a-good-fit-cites-limited-authority"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
d["IREN Sweetwater 1"]["loc"] = "883 FM 611, north of Sweetwater, near the Nolan-Fisher county line; reporting places it in both counties. Sweetwater 2 (about 28 miles away) is in Fisher County"
dc = d["Delta County data center"]
dc["loc"] = "Delta County (exact site not published); residents raised water contracts tied to Jim Chapman (Cooper) Lake"
dc["dates"] = "Informational town hall Mar 2, 2026 at Cooper ISD. County Judge Tanner Crutcher said the project was not a good fit, with water his main concern, and noted counties lack zoning power. Commissioners then passed a resolution in Mar 2026 opposing tax abatements for data centers; the judge has called for state disclosure rules"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 (' Some reporting places both IREN sites in neighboring Fisher County; we are confirming the county."',
  ' Its address, 883 FM 611, sits just north of Sweetwater near the Fisher County line, and reporting places it in both counties; IREN\'s second site, Sweetwater 2, is in Fisher County."'),
 ('note:"Delta County commissioners voted in March 2026 to oppose tax abatements for data centers."',
  'note:"County Judge Tanner Crutcher said the project was not a good fit, with water his main worry, and residents raised water contracts tied to Cooper Lake. Commissioners voted in March 2026 to oppose tax abatements for data centers. The developer\'s name has not appeared in local reporting."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 52: IREN Sweetwater county and Delta County facts updated")
