"""Originals batch 17: Project Mustang / Taylor Technology Campus (Williamson). Status: approved."""
import json
K = "Project Mustang (Taylor)"
L = [["KUT: Taylor approves the annexation deal over residents' objections (Oct 9, 2026)", "https://www.kut.org/energy-environment/2026-10-09/taylor-tx-annex-data-center-power-plant"],
     ["CBS Austin: council vote after months of debate", "https://cbsaustin.com/news/local/taylor-city-council-greenlights-data-center-after-months-of-debate"],
     ["CBS Austin: planning commission tables the proposal for 90 days", "https://cbsaustin.com/news/local/taylor-planning-commission-tables-data-center-proposal-for-90-days-after-pushback"],
     ["Data Center Dynamics: up to 1 GW behind-the-meter", "https://datacenterdynamics.com/en/news/powerhouse-big-watt-secure-approval-for-1gw-behind-the-meter-campus-in-taylor-texas"],
     ["KUT: Taylor rejects residents' petition for a temporary ban (July 2026)", "https://www.kut.org/energy-environment/2026-07-09/taylor-city-council-ban-data-centers"]]
p = "data/details.json"; d = json.load(open(p)); e = d.setdefault(K, {})
have = {u for _, u in e.get("links", [])}
e.setdefault("links", []).extend(x for x in L if x[1] not in have)
e["loc"] = "3301 FM 112, east of Taylor, between FM 112 and U.S. 79; was outside city limits"
e["acres"] = "664 acres"
e["llc"] = "Big Watt Digital and PowerHouse Data Centers (a division of American Real Estate Partners); renamed Taylor Technology Campus"
e["incent"] = "Developers pledged about $28.2M in community investments, including more than $10M for Taylor ISD and students, and to fund reclaimed-water upgrades"
e["dates"] = "July 2026: council rejected a citizen petition (1,400+ signatures) for a temporary ban. Aug 2026: planning commission tabled the application for 90 days; the developers withdrew it about two weeks later and negotiated directly with the city. Oct 8, 2026: council approved the annexation agreement 5 to 0 before an overflow crowd. Construction targeted 2027 to 2029"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
old = 'status:"announced", lat:30.57, lng:-97.41,\n   dev:"Big Watt Digital / PowerHouse Data Centers", power:"477 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."'
new = 'status:"approved", lat:30.57, lng:-97.41,\n   dev:"Big Watt Digital and PowerHouse Data Centers", power:"Up to 1 GW from an on-site gas power plant (behind the meter); the tracker lists 477 MW", water:"Company says reclaimed-water cooling; amount not disclosed", conf:"Reporting", note:"Now called Taylor Technology Campus, 664 acres east of town. When the planning commission delayed it 90 days, the developers withdrew and negotiated directly with city staff; the council approved the deal 5 to 0 in Oct 2026 over an overflow crowd of objecting residents."'
s = open("texas.html").read()
if new not in s:
    assert s.count(old) == 1, "Mustang card not found"; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 17: Project Mustang / Taylor Technology Campus checked; status now approved")
