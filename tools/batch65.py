"""Know Your Tools: add tool 12, San Marcos citywide zoning ban. Fermi America card: Perry off board, stock collapse, Amazon deal fell through, TensorWave tenant (Texas Tribune, Oct 31, 2026)."""
import re
f = "know-your-tools.html"; s = open(f).read()
NEW = ('<section class="tool"><h2>12. A city can use zoning to say no</h2>'
 '<p>Cities in Texas have zoning power that counties do not. A city council can change which land uses are allowed in each zoning district, including taking data centers off the list.</p>'
 '<p class="ex"><b>Where it worked:</b> In June 2026, the San Marcos City Council voted 4 to 3 to prohibit data centers in every zoning district, the first Texas city to do so. The ban applies only inside city limits, and it faces likely legal challenges, so watch for land asking to leave the city&#x27;s jurisdiction (see the Taylor and Talty examples on the map).</p>'
 '<p class="src"><a href="https://www.texastribune.org/2026/06/30/texas-san-marcos-data-center-ban-zoning-laws/">Texas Tribune, Jun 30, 2026</a> \u00b7 <a href="https://therealdeal.com/texas/2026/06/30/can-san-marcos-data-center-ban-survive-legal-challenges/">The Real Deal, Jun 30, 2026</a></p></section>')
if "12. A city can use zoning" not in s:
    m = re.search(r'<section class="tool"><h2>11\. .*?</section>', s, re.S)
    assert m, "tool 11 not found"
    s = s[:m.end()] + "\n" + NEW + s[m.end():]
    s = s.replace("Eleven tools", "Twelve tools")
    open(f, "w").write(s)
t = open("texas.html").read()
OLD = 'note:"Raised $746M in its IPO. Reported to be at least a year behind schedule.", src:"Industrial Info Resources; Cleanview; CorpWatch; Amarillo Tribune (as reported)"}'
NEWT = 'note:"Project Matador, on about 5,000 acres leased from the Texas Tech University System. Raised $746M in its IPO; reported to be at least a year behind schedule. A tentative Amazon deal fell through late last year; its first tenant, announced in August, is AI cloud startup TensorWave. The stock has fallen more than 90% from its peak, and co-founder Rick Perry lost reelection to the board in late October 2026.", src:"Industrial Info Resources; Cleanview; CorpWatch; Amarillo Tribune (as reported); Texas Tribune, Oct 31, 2026"}'
if NEWT not in t:
    assert t.count(OLD) == 1, "Fermi card not found"; t = t.replace(OLD, NEWT)
    open("texas.html", "w").write(t)
print("Batch 65: tool 12 (San Marcos zoning ban); Fermi card updated")
