"""Originals batch 38: Marfa (Open Origin: 'zero water' vs 800 acre-feet), Project Roman (Google, Hereford), IREN Sweetwater 1 (energized, not operating)."""
import json
L = {
 "Ziastra (Marfa)": [
   ["Big Bend Sentinel: AI data center could be coming to Marfa (800 acre-feet of groundwater a year)", "https://bigbendsentinel.com/2025/04/16/ai-data-center-could-be-coming-to-marfa"],
   ["Big Bend Sentinel: officials still meeting with developers (Oct 2025)", "https://bigbendsentinel.com/2025/10/01/proposed-marfa-data-center-still-in-discussions/"],
   ["Data Center Dynamics: 80,000-acre campus proposed in West Texas", "https://datacenterdynamics.com/en/news/80000-acre-data-center-campus-proposed-in-west-texas"],
   ["Baxtel: Open Origin's own claim of zero water for cooling", "https://baxtel.com/data-centers/open-origin"]],
 "Project Roman (Hereford)": [
   ["KFDA: residents seek answers at Hereford meeting; hospital district to vote on abatement only", "https://www.newschannel10.com/2026/07/15/community-members-seek-answers-hereford-meeting-proposed-google-data-center/"],
   ["ABC 7 Amarillo: hundreds pack the Hereford Civic Center", "https://abc7amarillo.com/news/local/hundreds-in-deaf-smith-county-seek-answers-on-google-data-center-renewables-project-hereford-texas-project-roman-intersect-blattner-marilyn-bell-county-judge-dj-wagner-junie-wagner-chamber-of-commerce"],
   ["ABC 7 Amarillo: Hereford water plan warns of Ogallala shortages", "https://abc7amarillo.com/news/local/hereford-water-plan-warns-of-ogallala-aquifer-shortages-as-city-grows-taqueria-el-vaquero-ryan-polster-data-centers-hereford-economic-development-corporation-deaf-smith-county-agriculture"],
   ["Interconnection.fyi: IP Roman Solar, 500 MW, planned for 2028", "https://www.interconnection.fyi/eia/project/68201-roms"]],
 "IREN Sweetwater 1": [
   ["IREN: Sweetwater 1 substation energized (May 1, 2026)", "https://www.globenewswire.com/news-release/2026/05/01/3286213/0/en/IREN-Announces-Successful-Energization-of-Sweetwater-1.html"],
   ["Baxtel: Sweetwater 2 (600 MW, about 28 miles away) targeted for late 2027", "https://baxtel.com/data-center/iren-sweetwater"],
   ["Nasdaq / Motley Fool: no customer yet for Sweetwater 1 (mid-2026)", "https://www.nasdaq.com/articles/iren-next-winner-nvidias-neocloud-spending-spree"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
m = d["Ziastra (Marfa)"]
m["loc"] = "Grasslands southeast of Marfa, Presidio County, near U.S. 67"
m["acres"] = "About 80,000 acres owned by Texas Mountain Cattle Company; sale not final as of 2025"
m["llc"] = "Open Origin (ammonia and green fuels company); CEO Wesley Powell"
m["dates"] = "First reported Apr 2025; county and city officials still meeting with the company in Oct 2025. Company said its Ziastra supercomputer would go live in Q1 2025"
r = d["Project Roman (Hereford)"]
r["loc"] = "North of Hereford, Deaf Smith County; related Roman Energy Center about 17 miles northeast of Hereford near County Road MM"
r["llc"] = "Google, with Intersect (a power developer Google acquired) and Blattner (builder)"
r["dates"] = "Public meeting at the Hereford Civic Center Jul 2026; hospital district board considered Google's tax abatement Jul 23, 2026, without considering water; 500 MW Roman solar project planned for 2028"
i = d["IREN Sweetwater 1"]
i["loc"] = "Near FM 611, Nolan County"
i["acres"] = "Sweetwater 1 and 2 together about 1,800 acres"
i["llc"] = "IREN Limited (formerly Iris Energy), a former bitcoin miner"
i["dates"] = "Substation connected to ERCOT May 1, 2026; data halls to be built and brought online in phases; Sweetwater 2 (600 MW) targeted for late 2027"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Open Origin", power:"Campus; size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Open Origin (an ammonia and green fuels company)", power:"Planned to be all on-site solar, off the grid", water:"The company advertises zero water for cooling, but a county official said it plans to pump 800 acre-feet of groundwater a year, about 714,000 gallons a day, more than the City of Marfa uses", conf:"Reporting", note:"Proposed on about 80,000 acres of ranchland southeast of Marfa. The company promised 900 to 1,100 jobs; none were posted. It said its supercomputer would go live in early 2025."'),
 ('lat:34.82, lng:-102.4,\n   dev:"Google", power:"Campus; size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'lat:34.82, lng:-102.4,\n   dev:"Google, with Intersect and Blattner", power:"Size not disclosed; a related 500 MW solar project is planned for 2028", water:"Not disclosed, over the Ogallala Aquifer, where Hereford\'s water plan warns of shortages", conf:"Reporting", note:"Planned north of Hereford (map pin is the town, not the site). Hundreds packed the civic center for answers. The hospital district board took up Google\'s tax break while saying it would not consider water or environmental impact."'),
 ('status:"operating", lat:32.47, lng:-100.41,\n   dev:"IREN", power:"1.4 GW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'status:"construction", lat:32.47, lng:-100.41,\n   dev:"IREN (formerly Iris Energy)", power:"1.4 GW connected to ERCOT; 2 GW planned with Sweetwater 2", water:"Not disclosed", conf:"Reporting", note:"Not operating yet. The substation was connected to the grid in May 2026, and data halls are being built in phases. A mid-2026 analysis said no customer had signed for the site: 1.4 GW of grid power reserved before a single tenant."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>IREN Sweetwater 1 status</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We showed Sweetwater 1 as operating. Its substation was connected to the grid in May 2026, but the data halls are still being built in phases. Status changed to under construction.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 38: Marfa (zero water vs 800 acre-feet), Project Roman, IREN Sweetwater 1 (not operating) checked")
