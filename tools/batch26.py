"""Batch 26: new card for Palomino Alpha (Guadalupe County): judge's land, water request, lawsuit."""
import json
K = "Palomino Alpha data center"
L = [["Community Impact: lawsuit; judge's family land; 500,000 gal/day water request", "https://communityimpact.com/san-marcos-buda-kyle/government/guadalupe-county-sued-over-data-center-development-agreements/"],
     ["San Marcos Record: water district signals delay or rejection (Sept 2026)", "https://www.sanmarcosrecord.com/news/article_4acd6b6c-ec32-4be8-a6a0-de1a4dd5bc17.html"],
     ["Guadalupe County: Palomino Alpha reinvestment zone notice (942 acres)", "https://www.guadalupetx.gov/upload/page/0106/docs/Palomino.pdf"],
     ["Guadalupe County: TCEQ water quality permit notice WQ0005514000", "https://www.guadalupetx.gov/upload/page/0289/Palomino%20Alpha.pdf"],
     ["Seguin Today: the lawsuit and the conflict-of-interest claim", "https://seguintoday.com/2026/07/23/lawsuit-filed-against-guadalupe-county/"],
     ["KSAT: residents raise water, air and transparency concerns", "https://www.ksat.com/news/local/2026/07/24/data-centers-draw-backlash-lawsuit-in-guadalupe-county-as-residents-raise-transparency-concerns/"]]
p = "data/details.json"; d = json.load(open(p)); e = d.setdefault(K, {})
have = {u for _, u in e.get("links", [])}
e.setdefault("links", []).extend(x for x in L if x[1] not in have)
e["loc"] = "Guadalupe County Precinct 2, in the Kingsbury area (pin approximate)"
e["acres"] = "About 870 to 942 acres (the county's reinvestment zone covers 942.29 acres)"
e["llc"] = "Palomino Alpha, LLC (Austin address)"
e["incent"] = "County tax abatement and development agreement approved"
e["dates"] = "County approved a reinvestment zone, abatement and development agreement. July 20, 2026: the Data Center Action Coalition and three residents sued, alleging Open Meetings violations and that County Judge Kyle Kutscher's family owns about 186 acres under contract to the developer without a filed conflict affidavit. July 23: Crystal Clear Special Utility District heard a request for 500,000 gallons of water a day; in Sept its board signaled it may delay or reject it. A TCEQ water quality (wastewater) permit has been applied for"
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
anchor = 'Residents have sued over open meetings and a conflict of interest.", src:"More Than Just Parks data center tracker"},\n'
card = ('  {name:"' + K + '", county:"Guadalupe", type:"data", status:"approved", lat:29.66, lng:-97.78,\n'
        '   dev:"Palomino Alpha, LLC", power:"Size not disclosed", water:"Asked Crystal Clear Special Utility District for 500,000 gal/day; the board signaled it may delay or reject it", conf:"Reporting", note:"About 900 acres. The county approved a tax abatement while, residents allege, the county judge\'s family had about 186 acres under contract to sell to the developer. Residents sued in July 2026. A TCEQ wastewater permit is pending.", src:"Community Impact; San Marcos Record; Guadalupe County; Seguin Today; KSAT"},\n')
s = open("texas.html").read()
if K not in s:
    assert s.count(anchor) == 1, "anchor not found"; s = s.replace(anchor, anchor + card)
open("texas.html", "w").write(s)
print("Batch 26: Palomino Alpha card added")
