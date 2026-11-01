"""Originals batch 13: Desert Haven / Hueco Ranch (Hudspeth), checked against KVIA, KFOX and Baxtel."""
import json
K = "Desert Haven data center"
L = [["KVIA: county judge confirms the $15B project; no tax abatement requested (Oct 9, 2026)", "https://kvia.com/news/local-news/2026/10/09/hudspeth-county-confirms-15-billion-proposed-data-center/"],
     ["KFOX: ServerDome CEO apologizes for lack of notice", "https://kfoxtv.com/news/local/serverdome-ceo-apologizes-for-lack-of-notice-on-hudspeth-county-data-center"],
     ["KFOX: residents demand answers on noise, water and power", "https://kfoxtv.com/news/local/hudspeth-county-residents-demand-answers-on-15b-data-centers-noise-water-and-power"],
     ["KVIA: community meeting; residents form a group (Oct 26, 2026)", "https://kvia.com/news/business-technology/2026/10/26/hudspeth-county-ai-data-center/"],
     ["Baxtel: Hueco Ranch site profile (24,000 acres, Rio Grande Electric Co-op)", "https://baxtel.com/data-center/serverdomes-global-hueco-ranch"]]
p = "data/details.json"; d = json.load(open(p)); e = d.setdefault(K, {})
have = {u for _, u in e.get("links", [])}
e.setdefault("links", []).extend(x for x in L if x[1] not in have)
e["loc"] = "Hueco Ranch, private land near Desert Haven, about 28 miles east of El Paso; several miles from the nearest homes"
e["acres"] = "About 24,000 acres of former ranch and oil-and-gas land"
e["llc"] = "Joint venture of ServerDomes Global and Lonestar Kaufman Development Partners (a Kaufman & Company affiliate)"
e["incent"] = "The county judge says the project is not asking the county for tax abatements"
e["dates"] = "Announced July 2026; ground broken Oct 7, 2026, before residents or county officials were told. The county judge confirmed it after rumors (Oct 9); the CEO apologized for the lack of notice; community meeting Oct 26; presentation to the Commissioners Court scheduled Oct 27"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
old = 'dev:"Kaufman & Company / ServerDomes", power:"350 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."'
new = 'dev:"ServerDomes Global with Kaufman & Company (Lonestar Kaufman Development Partners)", power:"350 MW, mostly from its own on-site power; Rio Grande Electric Co-op serves the area", water:"Not disclosed; residents have asked", conf:"Reporting", note:"Hueco Ranch: a $15B campus of geodesic domes on about 24,000 acres. Ground was broken Oct 7, 2026 before neighbors or county officials were told; the CEO later apologized. Residents have formed a group."'
s = open("texas.html").read()
if new not in s:
    assert s.count(old) == 1, "Desert Haven card not found"; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 13: Desert Haven / Hueco Ranch checked against originals")
