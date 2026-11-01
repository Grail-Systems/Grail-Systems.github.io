"""Company profiles: add PowerHouse Data Centers and Skybox Datacenters; add McLennan County to Cipher."""
import re
s = open("companies.html").read()
TRACT = '  {name:"Tract", kind:"Data center land developer", counties:["Bexar","Medina","Caldwell"], entities:"Tract", know:"Assembles large powered sites, including 720 MW at Applewhite in Bexar County and 500 MW in Medina County.", conf:"Reporting"},\n'
NEW = (
 '  {name:"PowerHouse Data Centers", kind:"Data center developer", counties:["Tarrant","Williamson","Ellis","Caldwell"], entities:"PowerHouse Data Centers (American Real Estate Partners); partners Big Watt Digital and Provident Data Centers", know:"Behind four Texas sites. Ellis County Data Ranch: 24 buildings on 768 acres outside Grand Prairie, with a 1.8 GW switchyard. Taylor Technology Campus: up to 1 GW from an on-site gas plant; when the planning commission delayed it, the developers withdrew and negotiated with city staff, and council approved it 5 to 0. Westlake: Circle T, up to 300 MW, temporarily blocked by a Tarrant County judge in Aug 2026. Caldwell County: about 500 acres.", conf:"Reporting"},\n'
 '  {name:"Skybox Datacenters", kind:"Data center developer", counties:["Williamson","Wichita","Tom Green"], entities:"Skybox Datacenters; Texas Data Centers Campus LLC (Wichita Falls); partner Prologis", know:"Building PowerCampus Austin in Hutto with Prologis, 600 MW planned; a $550M fourth building was filed in Oct 2026. Wichita Falls campus groundbreaking pushed to early 2027 after the state audit; its executive said the audit will weed out projects that weren\'t real or ready. Also part of a 1.2 GW proposal with Emergent next to Cipher\'s site near San Angelo.", conf:"Reporting"},\n'
)
if 'name:"PowerHouse Data Centers"' not in s:
    assert s.count(TRACT) == 1, "Tract line not found"; s = s.replace(TRACT, TRACT + NEW)
OLDC = 'counties:["Tom Green","McCulloch","Walker","Mitchell","Ector","Winkler","La Salle"], entities:"Cipher Mining / Cipher Digital"'
NEWC = 'counties:["Tom Green","McCulloch","Walker","Mitchell","Ector","Winkler","La Salle","McLennan"], entities:"Cipher Mining / Cipher Digital"'
if NEWC not in s:
    assert s.count(OLDC) == 1, "Cipher line not found"; s = s.replace(OLDC, NEWC)
ADD = ' In McLennan County, a commissioner said Texas law gives the county little authority over the project.'
if ADD not in s:
    s, n = re.subn(r'(\{name:"Cipher Digital".*?know:"[^"]*?)(", conf:)', lambda m: m.group(1) + ADD + m.group(2), s, count=1)
    assert n == 1, "Cipher know not found"
open("companies.html", "w").write(s)
print("Batch 62: PowerHouse and Skybox profiles added; Cipher now lists McLennan")
