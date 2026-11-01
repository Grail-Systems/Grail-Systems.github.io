"""Originals batch 32: Athens (Data Factory; council votes 3-2 for a ban) and Port Arthur (pitched to council Apr 2026)."""
import json
L = {
 "Data Factory Athens": [
   ["Athens Review: council pauses data centers after a packed meeting", "https://www.athensreview.com/news/athens-council-pauses-data-centers-after-packed-meeting/article_e2855be7-eccb-4309-b63a-3006eb9ce349.html"],
   ["KETK: residents push back on a proposed 10 MW facility", "https://www.ketk.com/news/local-news/data-center-boom-hits-a-wall-in-athens-after-resident-opposition/amp/"],
   ["KLTV: Athens council votes 3 to 2 for an ordinance banning data centers (Aug 2026)", "https://www.kltv.com/2026/08/25/athens-city-council-votes-3-2-favor-ordinance-banning-data-centers/"],
   ["KETK: Athens pauses other local infrastructure rules during the state audit", "https://www.ketk.com/energy-and-infrastructure-texas/data-centers/city-of-athens-pauses-work-on-local-infrastructure-regulations-amid-states-data-center-audit/amp/"]],
 "Port Arthur AI data center": [
   ["Port Arthur City Council video, Apr 21, 2026 (data center pitch)", "https://portarthurtx.new.swagit.com/videos/382908"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
a = d["Data Factory Athens"]
a["llc"] = "Data Factory, which had leased land in the city; it calls its sites flexible power farms and also planned bitcoin mining"
a["dates"] = "More than 100 people packed a council meeting and the council paused data centers; Aug 2026 the council voted 3 to 2 in favor of an ordinance banning data centers. The city later paused other infrastructure rules pending state action in Jan 2027"
pa = d["Port Arthur AI data center"]
pa["dates"] = "Apr 21, 2026: presenters pitched the City Council on a data center around Pleasure Island with its own renewable power (onshore wind, floating solar), battery storage and a small port. The developer's name is not yet confirmed in written records"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Data Factory", power:"10 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed as canceled. Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Data Factory", power:"10 MW to start, with bitcoin mining", water:"Not disclosed", conf:"Reporting", note:"After a packed council meeting, Athens paused data centers, then voted 3 to 2 in Aug 2026 for an ordinance banning them. A win for residents, near the separate Diode project at Cedar Creek Lake that was also withdrawn."'),
 ('dev:"Not identified", power:"300 MW listed", water:"Not disclosed", conf:"Reporting", note:"About 1.5 miles from protected public land, per the tracker. Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Not yet confirmed in written records", power:"The tracker lists 300 MW", water:"Not disclosed", conf:"Reporting", note:"Pitched to the Port Arthur City Council in Apr 2026 as a data center around Pleasure Island with its own wind, solar, battery storage and a small port. About 1.5 miles from protected public land, per the tracker. Needs a written record."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 32: Athens (3-2 ban vote) and Port Arthur (council pitch) checked")
