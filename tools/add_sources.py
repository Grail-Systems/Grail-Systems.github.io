import json
J = json.dumps
P = {
"Amp Z / Project Lufkin":"City of Lufkin records (CRR-2026-315, CRR-2026-316); Angelina County records; Pineywoods GCD; Lufkin Daily News",
"HyperDataGrid":"Pineywoods GCD emails (June to Aug 2026); Angelina County records; Data Center Dynamics",
"Longleaf Generating":"Angelina County records; City of Lufkin CRR-2026-316; Pineywoods GCD; KTRE; ERCOT queue (26INR0294)",
"Former Aspen Power biomass plant":"1606 Corp SEC filings and press releases; Lufkin Daily News",
"Crypto mining operation near the mill site":"Resident observation from a public road; photo documentation in progress",
"Diode Ventures, Cedar Creek Lake":"Office of the Governor (July 23, 2026); Texas Tribune; Fort Worth Report; WFAA",
"RCM Hill data center":"KWTX; Texas Tribune; KWBU; E&E News; More Than Just Parks tracker (size)",
"MARA Granbury bitcoin mine":"Federal court filings (via Blockspace); Earthjustice; Texas Tribune; Fox 4",
"Stargate Abilene":"Epoch AI; Texas Tribune; Bloomberg via TechRadar; Industrial Info Resources",
"Frontier / Stargate Shackelford":"Vantage Data Centers; Epoch AI; Oracle/OpenAI fact sheet; KTAB",
"Fermi America campus":"Industrial Info Resources; Cleanview; CorpWatch; Amarillo Tribune (as reported)",
"Google, Gray County":"Industrial Info Resources",
"Stargate Milam County":"TechRadar; Data Center Dynamics; More Than Just Parks tracker",
"Riot Rockdale":"The Block; Greenpeace USA research; Baxtel",
"Bitdeer Rockdale":"Greenpeace USA research",
"Riot Corsicana":"Riot press releases; Data Center Dynamics; City of Corsicana via Dallas Morning News (2022); Baxtel",
"Galaxy Helios":"The Block; CoinShares",
"MARA Matagorda County campus":"Baxtel",
"Vantage West Side campuses":"Federal court case Public Citizen et al. v. Vantage, 5:26-cv-06032; Law360; San Antonio Current; Texas Public Radio",
"Project Saltworks":"Graham Leader; Baxtel; More Than Just Parks tracker",
"Flexential Talty campus":"Baxtel","Rowan Temple campus":"Baxtel","QTS at Lancium, Hall County":"Baxtel",
"Core Scientific Denton":"CoinShares","Core Scientific Pecos":"Baxtel","PowerHouse Caldwell County":"Baxtel","Pace Glasscock County":"Baxtel",
"DataBank Red Oak campus":"Texas Department of Licensing and Regulation (TDLR) filings; Data Center Dynamics; Dallas Morning News",
"Compass Red Oak campus":"TDLR filings; Baxtel; Cleanview",
"Google Midlothian campus":"Google environmental report (as reported); Dallas Morning News; Baxtel",
"Google Red Oak campus":"Energy Capital HTX; Dallas Morning News",
"Google Haskell County campuses":"Energy Capital HTX","Google Armstrong County campus":"Energy Capital HTX",
"Cawley Partners data center park":"Baxtel","PowerHouse Westlake":"Baxtel (citing NBC)",
"Longleaf II Power Station":"ERCOT interconnection queue (30INR0114)","Sun Angel ESS":"ERCOT interconnection queue (27INR0247)",
"Meta El Paso":"El Paso Water via KFOX14; El Paso Matters / Texas Standard; El Paso Inc.; Blockspace",
"Lancium Childress":"Inside Climate News (Texas House committee testimony, April 2026)",
"Amazon near Comanche Peak":"KERA","Glen Rose AI data center":"KERA; Fort Worth Weekly",
"Infrakey Lacy Lakeview":"Texas Tribune; More Than Just Parks tracker (size)",
"Prosper / FM 1385 data center":"Prosper Planning & Zoning meeting, Aug 18, 2026 (via Citizen Portal)",
"Harlingen data center":"Texas Tribune; More Than Just Parks tracker",
"Comanche Circle":"KERA; CBS Texas; Texas Tribune",
"Fort Spunky":"Texas Tribune; Data Center Dynamics; More Than Just Parks tracker",
"Project Patriot":"KERA; Data Center Dynamics; Baxtel; Cleanview; Texas Tribune",
"Hood County AI campus":"Baxtel; dcmap.us","Amazon AWS, Coates Road":"Baxtel; More Than Just Parks tracker",
"Project Red and Project Yellow":"KERA (July 20, 2026); Fort Worth Weekly",
"Black Mountain Power, Fort Worth":"Fort Worth Weekly",
"Google Pflugerville":"Google environmental report via Global Investigative Journalism Network",
"San Marcos data center (Francis Harris Lane)":"Community Impact; KUT; Texas Tribune",
"Bon Wier Innovation Park":"KJAS (two articles); East Texas Banner; KFDM; Newswire (2022)",
"Project Anderson (NextEra)":"Utility Dive; Data Center Dynamics; Texas Scorecard; KETK; City of Palestine; The Center Square",
"CyrusOne at Freestone Energy Center":"Constellation press release (Business Wire)",
"CyrusOne at Thad Hill Energy Center":"Calpine press release (PR Newswire)",
"Tyler bitcoin mine rezoning":"Tyler Morning Telegraph",
"Texas Critical Data Centers":"Company press release (Business Wire); Odessa American",
}
MTJP = "More Than Just Parks data center tracker"
for n in ["Datahub Developers AI data center","Project Big Pine","Old Ocean data center","Hedgehog USA powered land campus","Alpha Digital Campus","FO Permian Partners data center","Glass Mountains Ranch campus","Fort Bliss data center","JMG data center, Conroe","Pacifico Cedar Creek Campus"]:
    P[n] = MTJP
A = {
"State of Texas, Governor Abbott|July 2026":"Office of the Governor press release (July 23, 2026); Texas Tribune",
"Hill County|May 2026":"KWTX; Texas Tribune; KWBU",
"West Cedar Creek MUD, Henderson County|May 2026":"Fort Worth Report; KETK; KLTV",
"Hood County|2024 to 2026":"Texas Tribune; federal court filings via Blockspace",
"Angelina County|July 2026":"Angelina County records; Texas Tribune",
"Public Citizen, Sierra Club and Environmental Integrity Project|2026":"Law360; San Antonio Current; Texas Public Radio",
"Ellis County, with Compass Datacenters|June 2026":"Baxtel",
"Angelina County, Long Leaf abatement|May 2025":"Angelina County records (via Angelina County Watch)",
"State of Texas: grid audit and freeze|Aug 2026":"Texas Tribune (Aug 3, 2026); Akin Gump; Holland & Knight; POWER Magazine",
"State of Texas: water reporting and permit freeze|Sept 2026":"Texas Tribune (Sept 21 and Oct 20, 2026); KBTX; Troutman; Bracewell; Beveridge & Diamond",
"Somervell County|May 2026":"KERA",
"Caldwell County|May 2026":"Caldwell County news release (Resolution 29-2026)",
"Hood County|Feb 2026":"Texas Tribune; KBTX",
"City of El Paso|2026":"KFOX14",
"Hood County: stricter rules and a special law|March 2026":"Texas Tribune; Texas Scorecard",
"Hood County: court win|July 2026":"KERA (July 20, 2026); Fort Worth Weekly",
"Granbury residents|April and July 2026":"KERA; Data Center Dynamics",
"Austin County|July 2026":"KWHI; Sealy News; Austin County public hearing notice",
"City of El Paso|May to July 2026":"KVIA; KFOX14; El Paso Inc.; City of El Paso news release (July 20, 2026)",
"City of Fort Worth|June 2026":"City of Fort Worth council work session presentation (June 2, 2026); NBC DFW; KRLD",
"City of San Marcos|June 2026":"Texas Tribune (June 30, 2026); KSAT; Community Impact",
"Hays County|Jan to June 2026":"The Real Deal; Hoodline; Community Impact; Texas Tribune",
"City of Tyler|July 2026":"Tyler Morning Telegraph (July 24, 2026)",
"State Reps. Helen Kerwin (R) and Erin Zwiener (D)|2026":"The Center Square",
}
p = "texas.html"; s = open(p).read()
start = s.index("const projects = ["); mid = s.index("const actions = ["); end = s.index("const css")
proj, acts = s[start:mid], s[mid:end]
def tag(block, key_start, keyfun):
    out, i, missing, n = "", 0, [], 0
    while True:
        j = block.find(key_start, i)
        if j < 0: out += block[i:]; break
        e = block.find('"}', j) + 1
        entry = block[j:e]
        if "src:" not in entry:
            src = keyfun(entry)
            if src: entry = entry + ", src:" + J(src); n += 1
            else: missing.append(entry[:60])
        out += block[i:j] + entry; i = e
    return out, n, missing
def pkey(entry):
    name = json.loads(entry[entry.index('name:') + 5 : entry.index('", county') + 1])
    if name in P: return P[name]
    if "More Than Just Parks" in entry: return MTJP
    return None
def akey(entry):
    who = json.loads(entry[entry.index('who:') + 4 : entry.index('", when') + 1])
    when = json.loads(entry[entry.index('when:') + 5 : entry.index('", what') + 1])
    return A.get(who + "|" + when)
proj, n1, m1 = tag(proj, "{name:", pkey)
acts, n2, m2 = tag(acts, "{who:", akey)
s = s[:start] + proj + acts + s[end:]
reps = [
 ("${esc(p.note)}<br><br>", "${esc(p.note)}<br><br>${p.src ? '<b>Sources:</b> ' + esc(p.src) + '<br><br>' : ''}"),
 ("<p>${esc(p.note)}</p>`;", "<p>${esc(p.note)}</p>${p.src ? '<p><b>Sources:</b> ' + esc(p.src) + '</p>' : ''}`;"),
 ("<p><b>Lesson:</b> ${esc(a.lesson)}</p></li>", "<p><b>Lesson:</b> ${esc(a.lesson)}</p>${a.src ? '<p><b>Sources:</b> ' + esc(a.src) + '</p>' : ''}</li>"),
 ('"conf","lat","lng"]', '"conf","src","lat","lng"]'),
 ('["who","when","what","result","lesson"]', '["who","when","what","result","lesson","src"]'),
]
for a, b in reps:
    if a in s: s = s.replace(a, b, 1)
    else: print("template not found:", a[:40])
open(p, "w").write(s)
print("Projects sourced:", n1, "| missing:", len(m1)); [print("  ", x) for x in m1]
print("Actions sourced:", n2, "| missing:", len(m2)); [print("  ", x) for x in m2]
