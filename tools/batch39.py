"""Originals batch 39: Nolan County. Crusoe ($7B, abatement approved), CloudBurst Sweetwater (abatement vote), IREN county question."""
import json
L = {
 "Crusoe Nolan County data center": [
   ["KTXS: 10-year tax abatement approved for $7 billion data center (Apr 2026)", "https://ktxs.com/news/local/it-will-change-our-rural-town-tax-abatement-for-7-billion-texas-data-center-approved"],
   ["News 4 San Antonio / KTXS: residents react, 'I might want to move out'", "https://news4sanantonio.com/news/local/i-might-want-to-move-out-new-7-billion-texas-data-center-sparks-mixed-reactions"],
   ["Advocate & Democrat: Sweetwater passes ordinance on where data centers can locate (Jun 2026)", "http://www.advocateanddemocrat.com/news/article_7368ef83-bc9f-4c20-90e3-56210ae33b57.html"]],
 "CloudBurst AI data center (Sweetwater)": [
   ["Sweetwater Reporter via Ground News: CloudBurst moving forward after commissioners' vote (Jun 25, 2026)", "https://ground.news/article/cloudburst-ai-data-center-moving-forward-in-sweetwater-after-commissioners-vote_9d2684"],
   ["Advocate & Democrat: Sweetwater passes ordinance on where data centers can locate (Jun 2026)", "http://www.advocateanddemocrat.com/news/article_7368ef83-bc9f-4c20-90e3-56210ae33b57.html"]],
 "IREN Sweetwater 1": [
   ["Data Center Dynamics: IREN energizes Sweetwater (says both sites are in Fisher County)", "https://www.datacenterdynamics.com/en/news/iren-energizes-first-phase-of-2gw-sweetwater-data-center-campus-in-texas/"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
c = d["Crusoe Nolan County data center"]
c["loc"] = "Near Sweetwater, Nolan County (exact site not published)"
c["llc"] = "Crusoe Energy Systems"
c["dates"] = "Nolan County commissioners approved a 10-year tax abatement Apr 13, 2026. City of Sweetwater passed an ordinance on where data centers may locate Jun 2026"
b = d["CloudBurst AI data center (Sweetwater)"]
b["loc"] = "Sweetwater area, Nolan County (exact site not published)"
b["llc"] = "CloudBurst Data Centers (co-founder Cynthia Thompson), the developer of the 706-acre campus near New Braunfels"
b["dates"] = "Nolan County commissioners voted on a tax abatement agreement in late Jun 2026, as Sweetwater finalized its data center location ordinance"
d["IREN Sweetwater 1"]["loc"] = "Near FM 611 outside Sweetwater. Some reporting places both IREN Sweetwater sites in Fisher County, not Nolan; not yet confirmed"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Crusoe", power:"200 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Crusoe Energy Systems", power:"200 MW listed; investment reported at $7 billion", water:"Not disclosed", conf:"Reporting", note:"Nolan County approved a 10-year tax abatement in April 2026. A commissioner said the break was key to keeping the project in the county. One resident told reporters, \\"It will change our rural town.\\""'),
 ('dev:"CloudBurst", power:"300 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"CloudBurst Data Centers", power:"300 MW listed", water:"Not disclosed", conf:"Reporting", note:"The same developer behind the contested campus near New Braunfels. Nolan County commissioners voted on its tax abatement in June 2026, the same month Sweetwater passed an ordinance limiting where data centers can go. With Crusoe and IREN, this is at least the third large project around one town of about 10,000."'),
 ('1.4 GW of grid power reserved before a single tenant."',
  '1.4 GW of grid power reserved before a single tenant. Some reporting places both IREN sites in neighboring Fisher County; we are confirming the county."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 39: Nolan County (Crusoe $7B abatement, CloudBurst, IREN county question) checked")
