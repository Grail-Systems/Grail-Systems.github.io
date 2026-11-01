"""Bastrop: add the EdgeConneX Cedar Creek campuses (missing from the map) and fill the records-request company list. Add a Sabey profile."""
import json
K = "EdgeConneX Cedar Creek campuses"
p = "data/details.json"; d = json.load(open(p))
if K not in d:
    d[K] = {"loc": "Near Wolf Lane and FM 535, Cedar Creek, Bastrop County; about 7 miles north of Pacifico's Earl Callahan Road site. Pin approximate",
            "llc": "EdgeConneX (one campus filed as DFW33220N Operations 1, LLC)",
            "incent": "10-year, 75% county property tax abatement (2024)",
            "dates": "Three campuses planned; the first building was nearly complete by mid-2026. More than 100 residents attended a July 22, 2026 town hall on Cedar Creek data centers",
            "links": [["Community Impact: data centers raise questions across Bastrop County (four sites, about 4,306 acres)", "https://communityimpact.com/bastrop-cedar-creek/development/data-centers-raise-questions-across-bastrop-county/"],
                      ["Community Impact: residents organize; first EdgeConneX building nearly complete; 2024 abatement", "https://communityimpact.com/bastrop-cedar-creek/government/bastrop-county-residents-organize-for-data-center-transparency-local-guardrails/"],
                      ["Elgin Courier: one data center under construction near Wolf Lane and FM 535, two more in development", "https://www.elgincourier.com/article/4795,community-led-town-hall-calls-for-data-center-oversight"]]}
json.dump(d, open(p, "w"), ensure_ascii=False, separators=(",", ":"))
CARD = (',\n'
 '  {name:"EdgeConneX Cedar Creek campuses", county:"Bastrop", type:"data", status:"construction", lat:30.09, lng:-97.48,\n'
 '   dev:"EdgeConneX", power:"Not disclosed", water:"Not disclosed", conf:"Reporting", note:"Three campuses planned near Wolf Lane and FM 535 in Cedar Creek; the first building was nearly complete by mid-2026. The county granted a 10-year, 75% property tax abatement in 2024. Together with Pacifico\'s site seven miles south, Cedar Creek has more than 4,000 acres in data center plans. Pin is approximate.", link:"/bastrop/", src:"Community Impact; Elgin Courier"}')
s = open("texas.html").read()
if 'name:"EdgeConneX Cedar Creek campuses"' not in s:
    anchor = '\n];\n\nconst actions'
    assert s.count(anchor) == 1, "array end not found"
    s = s.replace(anchor, CARD + anchor, 1)
    open("texas.html", "w").write(s)
b = open("bastrop/index.html").read()
old = 'data-county="Bastrop" data-city="" data-edc="" data-gcd="" data-companies=""'
new = 'data-county="Bastrop" data-city="" data-edc="" data-gcd="" data-companies="Pacifico Energy, Pacifico Cedar Creek LLC, Black Chamber Partners, EdgeConneX"'
if new not in b:
    assert b.count(old) == 1, "bastrop ask section not found"
    open("bastrop/index.html", "w").write(b.replace(old, new))
c = open("companies.html").read()
anchor = 'Its Childress site is registered for the state data center tax exemption.", conf:"Reporting"},'
sabey = '\n  {name:"Sabey Data Centers", kind:"Data center developer", counties:["Hays","Wilbarger"], entities:"Sabey Data Centers (Seattle); landowner partner Carson Select Investments LP in San Marcos", know:"Operates a campus in Round Rock and is planning two more in Texas: about 786 acres south of San Marcos near the Hays Energy gas plant, where the landowner said it had been overwhelmed with unsolicited offers, and land held near Oklaunion in Wilbarger County.", conf:"Reporting"},'
if 'name:"Sabey Data Centers"' not in c:
    assert c.count(anchor) == 1, "companies.html anchor not found"
    open("companies.html", "w").write(c.replace(anchor, anchor + sabey, 1))
print("Batch 56: EdgeConneX Cedar Creek added; Bastrop request list filled; Sabey profile added")
