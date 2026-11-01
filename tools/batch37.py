"""Originals batch 37: Crusoe Victoria (gas first, then nuclear; timeline slipped) and Data City Texas (5 GW claim, no application filed)."""
import json
L = {
 "Crusoe Victoria AI Factory": [
   ["Crusoe: partnership with Blue Energy at the Port of Victoria", "https://www.crusoe.ai/resources/newsroom/blue-energy-and-crusoe-partner-to-develop-nuclear-powered-ai-data-center"],
   ["Data Center Dynamics: 1,600-acre campus; gas from 2028, nuclear by 2031 (original plan)", "https://www.datacenterdynamics.com/en/news/crusoe-taps-blue-energy-to-supply-nuclear-power-for-up-to-15gw-data-center-in-port-of-victoria-texas/"],
   ["Baxtel: revised plan, 1 GW of gas turbines in 2030, five small reactors from 2032", "https://baxtel.com/news/blue-energy-ge-vernova-hitachi-advance-2-5gw-texas-power-plant-for-data-center"],
   ["World Nuclear News: Blue Energy files its first NRC construction application", "https://www.world-nuclear-news.org/articles/blue-energy-submits-first-construction-application-to-nrc"]],
 "Data City Texas": [
   ["Energy Abundance: Data City announcement, 5 GW on 50,000 acres (Mar 2025)", "https://smb.lobservateur.com/article/C-O-R-R-E-C-T-I-O-N-Energy-Abundance-Development-Corporation/67dcee79e68a6d77f58081d7"],
   ["Laredo Morning Times via GovTech: no application filed with the city or county", "https://www.govtech.com/artificial-intelligence/laredo-texas-moves-to-set-permanent-data-center-standards"],
   ["Texas Monthly: Webb County colonias and water insecurity", "https://www.texasmonthly.com/news-politics/data-centers-sapping-texas-water-electricity/"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
v = d["Crusoe Victoria AI Factory"]
v["loc"] = "Port of Victoria (Texas Logistics Center), Victoria County"
v["acres"] = "About 1,600 acres for the Crusoe campus, with Blue Energy's power plant on a nearby site"
v["llc"] = "Crusoe (data centers) and Blue Energy (power plant), with GE Vernova and GE Vernova Hitachi"
v["dates"] = "Announced Oct 2025: gas power from 2028, nuclear by 2031. Revised in 2026: two gas turbines (1 GW) in 2030, then up to 1.5 GW from five small modular reactors from 2032; final investment decision expected 2027; first NRC construction application filed"
c = d["Data City Texas"]
c["loc"] = "Near Laredo, Webb County (exact site not published)"
c["acres"] = "50,000 acres claimed"
c["llc"] = "Energy Abundance Development Corporation (Houston); founder and CEO Brian Maxwell"
c["dates"] = "Announced Mar 2025 as a 5 GW hub with a 300 MW first phase. In 2026 the City of Laredo and Webb County said they had received no application; Laredo is drafting permanent data center standards"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('dev:"Crusoe, with Blue Energy", power:"1.5 GW listed", water:"Not disclosed", conf:"Reporting", note:"Port of Victoria campus. Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Crusoe, with Blue Energy and GE Vernova", power:"1 GW of gas turbines first, then up to 1.5 GW from five small nuclear reactors", water:"Not disclosed", conf:"Reporting", note:"A 1,600-acre campus at the Port of Victoria. The power timeline has already slipped: gas was promised for 2028 and nuclear for 2031; the revised plan says gas in 2030 and reactors from 2032."'),
 ('dev:"Energy Abundance", power:"300 MW listed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'dev:"Energy Abundance Development Corp (Houston)", power:"Claims 5 GW, starting with 300 MW, all behind the meter", water:"Not disclosed, in a county where colonias already face water insecurity", conf:"Reporting", note:"Announced in 2025 as the world\'s largest behind-the-meter data center hub, on 50,000 acres near Laredo. As of 2026, the city and county say no application has been filed. Laredo is writing permanent data center rules."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 37: Crusoe Victoria (timeline slipped) and Data City Texas (no application) checked")
