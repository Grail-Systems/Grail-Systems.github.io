"""Originals batch 45: Google Wilbarger ('Project Rise', under construction, air-cooled) and Project North (Bolt, a second Shackelford campus west of Albany)."""
import json
L = {
 "Google Wilbarger County data center": [
   ["Google: new data center under construction in Wilbarger County, with AES power", "https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/data-center-wilbarger-county/"],
   ["KAUZ: air-cooled 'power-first' plan with AES, aiming to eliminate operational water use (Feb 2026)", "https://www.newschannel6now.com/2026/02/24/google-announces-new-clean-energy-data-center-agreement-with-wilbarger-county"],
   ["Data Center Dynamics: Google files two $500M buildings ('Project Rise') in Vernon; work began Mar 31, 2026", "https://www.datacenterdynamics.com/en/news/google-files-for-two-data-centers-in-vernon-texas/"],
   ["KAUZ: Google open house in Vernon; $4.5M to city infrastructure (Oct 2026)", "https://www.newschannel6now.com/2026/10/14/google-holds-open-house-wilbarger-county-data-center-project/"]],
 "Project North (Shackelford)": [
   ["KTXS: second data center proposed west of Albany draws mixed reactions", "https://ktxs.com/news/local/second-data-center-proposed-west-of-albany-draws-mixed-reactions-in-shackelford-county"],
   ["KTXS: 'Do we need another one?'", "https://ktxs.com/news/local/do-we-need-another-one-proposed-2nd-data-center-draws-concerns-in-shackelford-county"],
   ["KTXS: county judge responds to backlash with one-on-one meetings", "https://ktxs.com/news/local/shackelford-county-judge-responds-to-backlash-over-second-proposed-data-center"]],
}
p = "data/details.json"; d = json.load(open(p))
for k, links in L.items():
    e = d.setdefault(k, {}); have = {u for _, u in e.get("links", [])}
    e.setdefault("links", []).extend(x for x in links if x[1] not in have)
g = d["Google Wilbarger County data center"]
g["loc"] = "FM 2897 South, Vernon, Wilbarger County"
g["llc"] = "Google ('Project Rise' 1A and 2A), with power from AES built on site"
g["dates"] = "Announced 2025; work began Mar 31, 2026; two buildings of about 991,000 sq ft each filed with the state, about $1B; open house Oct 2026. Nearby: Sabey's planned Oklaunion data center and Genesis Digital's 'Rowdy' bitcoin site, which are not yet on our map"
n = d["Project North (Shackelford)"]
n["loc"] = "West of Albany, Shackelford County (exact site not published); Vantage's $25B Frontier campus is southwest of Albany"
n["llc"] = "Bolt Data and Energy (which raised $150M, including $50M from Texas Pacific Land, to build on TPL land in West Texas)"
n["dates"] = "Proposed 2026; residents pushed back and County Judge John Viertel held one-on-one meetings"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
T = [
 ('status:"announced", lat:34.15, lng:-99.3,\n   dev:"Google", power:"Campus; size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Listed by the More Than Just Parks tracker; needs verification."',
  'status:"construction", lat:34.15, lng:-99.3,\n   dev:"Google, with AES building power on site", power:"Size not disclosed by Google; one tracker lists 850 MW", water:"Air-cooled; Google says the design aims to eliminate operational water use", conf:"Reporting", note:"Two buildings of about 991,000 sq ft each near Vernon, about $1B, with work begun March 2026. Google is giving the city $4.5M for infrastructure. Worth noting: if Google can air-cool here, other developers can be asked to do the same."'),
 ('status:"announced", lat:32.7, lng:-99.25,\n   dev:"Bolt Data and Energy", power:"Size not disclosed", water:"Not disclosed", conf:"Reporting", note:"Second project in the county after Vantage Frontier. Listed by the More Than Just Parks tracker; needs verification."',
  'status:"announced", lat:32.72, lng:-99.36,\n   dev:"Bolt Data and Energy (backed in part by Texas Pacific Land)", power:"Size not disclosed", water:"Not disclosed", conf:"Reporting", note:"A second campus proposed west of Albany, in a county already hosting Vantage\'s $25B Frontier site. Residents asked, \\"Do we need another one?\\" and the county judge held one-on-one meetings after the backlash. Pin is approximate."'),
]
s = open("texas.html").read()
for old, new in T:
    if new in s: continue
    assert s.count(old) == 1, "not found: " + old[:60]; s = s.replace(old, new)
open("texas.html", "w").write(s)
c = open("corrections.html").read(); entry = '<li><span class="tag">Nov 1, 2026</span><h3>Google Wilbarger County status</h3>'
if entry not in c:
    c = c.replace('  <ul class="rows">\n', '  <ul class="rows">\n    ' + entry + '<p>We showed Google\'s Wilbarger County data center as announced. Work began in March 2026 and Google describes it as under construction. Status changed.</p></li>\n', 1)
    open("corrections.html", "w").write(c)
print("Batch 45: Google Wilbarger (under construction, air-cooled) and Project North (second Shackelford campus) checked")
