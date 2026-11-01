"""Originals batch 40: Childress. Crusoe/Lancium 1 GW for Meta (likely same site as Lancium Childress card); IREN Childress 750 MW with Microsoft halls; the town's water crisis."""
import json
L = {
 "Crusoe / Lancium Childress campus": [
   ["Crusoe and Lancium: 1 GW campus on 270 acres in Childress (Jul 15, 2026)", "https://www.globenewswire.com/news-release/2026/07/15/3327869/0/en/Crusoe-and-Lancium-Announce-1-0-Gigawatt-AI-Data-Center-Campus-in-Childress-Texas.html"],
   ["Data Center Dynamics: Meta signs for 1.6 GW from Crusoe, including Childress (Bloomberg report)", "https://www.datacenterdynamics.com/en/news/meta-signs-16gw-capacity-agreement-with-crusoe-report/"],
   ["ABC 7 Amarillo: Childress boil-water notice; Lancium offers a water source (Sept 2026)", "https://abc7amarillo.com/news/local/childress-distributes-bottled-water-as-boil-notice-stretches-past-a-week-mayor-cary-preston-greenbelt-reservoir-city-manager-kevin-hodges-ross-gardens-randa-giter"]],
 "Lancium Childress": [
   ["Crusoe and Lancium: 1 GW campus on 270 acres in Childress (Jul 15, 2026)", "https://www.globenewswire.com/news-release/2026/07/15/3327869/0/en/Crusoe-and-Lancium-Announce-1-0-Gigawatt-AI-Data-Center-Campus-in-Childress-Texas.html"]],
 "IREN Childress AI and mining campus": [
   ["Baxtel: IREN Horizon halls at Childress for Microsoft", "https://baxtel.com/data-center/iren-horizon-1"],
   ["Baxtel: Childress reaches 750 MW operating, IREN's largest campus", "https://baxtel.com/data-center/iren-horizon-8"],
   ["CNHI: a neighbor a quarter mile away describes living next to the site", "https://www.cnhinews.com/oklahoma/news/article_99bbf86a-9856-5eb3-88a9-f9516239e489.html"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
c = d["Crusoe / Lancium Childress campus"]
c["loc"] = "Lancium's Clean Campus in Childress, Childress County"
c["acres"] = "270 acres owned by Lancium (Lancium lists more than 3,000 acres for the wider Childress campus)"
c["llc"] = "Crusoe (builds and runs the data centers) and Lancium (owns land, power hookup and energy); Meta reported as the customer"
c["dates"] = "Announced Jul 15, 2026; construction expected to begin Q3 2026; 1 GW grid connection already approved by ERCOT. In Sept 2026 the City of Childress was under a boil-water notice and disaster declaration"
i = d["IREN Childress AI and mining campus"]
i["loc"] = "Along U.S. 287, Childress County"
i["llc"] = "IREN Limited, through IE US Development Holdings 3"
i["dates"] = "Bitcoin mining site certified 2022; AI 'Horizon' halls added from 2025, with capacity for Microsoft; reached about 750 MW operating"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Crusoe and Lancium", power:"1 GW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Crusoe and Lancium, with Meta reported as the customer", power:"1 GW, grid connection already approved by ERCOT", water:"Not disclosed; the companies say they will invest in local water infrastructure", conf:"Reporting", note:"Announced July 2026 on 270 acres Lancium owns, with construction set to start that fall. Likely the same site as our Lancium Childress card. Two months later, the town was under a boil-water notice and a disaster declaration after extreme heat."'),
 ('note:"Same developer as the Stargate Abilene campus."',
  'note:"Same developer as the Stargate Abilene campus. Likely the same site as our Crusoe / Lancium Childress card, where Crusoe is building a 1 GW campus; we are confirming what is operating here today."'),
 ('dev:"IREN", power:"750 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"IREN (formerly Iris Energy)", power:"About 750 MW operating, IREN\'s largest site", water:"Not disclosed", conf:"Reporting", note:"Started as a bitcoin mine in 2022. IREN has since added liquid-cooled AI halls, including capacity for Microsoft. Together with the Crusoe/Lancium campus, Childress would host close to 2 GW of data centers."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 40: Childress (Crusoe/Lancium for Meta, IREN 750 MW, water crisis) checked")
