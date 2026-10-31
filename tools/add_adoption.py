p = "standards.html"; s = open(p).read()
if 'id="adopted"' in s:
    print("already added"); raise SystemExit
rows = [
 ("Adopted", "Angelina County", "Resolution 010-26 asks the Legislature for county authority over setbacks, noise, lighting and water impact.", "E", "July 14, 2026", "Angelina County records"),
 ("Drafted", "Angelina County", "Draft abatement terms for Amp Z include closed-loop cooling, setbacks, and yearly fire ($150,000) and road ($500,000) funds.", "6, 10, 11, 12", "Mar 2026", "Angelina County records"),
 ("Adopted", "Caldwell County", "Resolution 29-2026 opposes open-loop evaporative cooling and high-volume drinking-water use, and asks the Legislature for county authority.", "6, E", "May 14, 2026", "Caldwell County news release"),
 ("Adopted", "Hood County", "Paid for a professional sound study near the MARA bitcoin mine to set a noise baseline.", "F", "2024 to 2026", "Texas Tribune; KERA"),
 ("Adopted", "Hood County", "Stricter development rules for large industrial projects, including data centers. The county rejected one plan over missing water information.", "6, A", "March 2026", "Texas Tribune (June 2, 2026)"),
 ("Adopted", "Somervell County", "Unanimous resolution opposing new data centers until the Legislature addresses water and energy.", "E", "May 11, 2026", "KERA"),
 ("Adopted", "Henderson County", "Resolution asking the Legislature for authority to regulate data centers.", "E", "2026", "Texas Tribune; KSAT"),
 ("Adopted", "Hill County", "Replaced its rescinded moratorium with a review checklist for developers.", "A", "June 2026", "KWTX; Texas Tribune"),
 ("Adopted", "Hays County", "Commissioned its first full county water study since 2011, covering all proposals together.", "B", "Jan 20, 2026", "Community Impact; Texas Tribune"),
 ("Adopted", "State of Texas (TWDB)", "Mandatory water-use reporting for data centers, at the Governor's direction.", "6", "Sept 14, 2026", "Texas Tribune; KBTX"),
 ("Called for", "Gov. Greg Abbott", "Closed-loop cooling, annual water and power reporting, grid connections that lower household bills, and repeal of sales tax breaks.", "6, 9, 13", "July 23, 2026", "Office of the Governor; Texas Tribune"),
 ("Proposed", "City of Fort Worth", "Draft zoning: 250-foot setbacks from homes, generators at least 300 feet away and screened, closed-loop cooling, stricter noise limits, and no crypto mining.", "3, 6, 8, 9, 10", "June 2, 2026", "City of Fort Worth presentation; NBC DFW"),
 ("Proposed", "Pineywoods GCD", "Rule changes requiring monitoring wells with real-time readings for power plants and data centers. Public hearing Nov. 9.", "6, 7", "Nov 9, 2026 hearing", "Pineywoods proposed rule amendments"),
 ("In progress", "City of El Paso", "Council directed staff to draft a community benefits agreement for the Meta data center.", "13", "2026", "KFOX14"),
]
n = len({g for st, g, *_ in rows if st == "Adopted"})
items = "\n".join(
  f'    <li><span class="tag">{st}</span><span class="tag">Matches {("items " if "," in m else "item ") + m}</span><span class="tag">{d}</span>'
  f'<h3>{g}</h3><p>{w}</p><span class="src">Source: {src}</span></li>' for st, g, w, m, d, src in rows)
section = f'''<section id="adopted">
  <h2>Who has adopted part of it</h2>
  <p>{n} Texas governments have already adopted at least one piece of this Standard, and others have proposed more. Numbers match the 16 conditions above; letters match the 8 county actions. A resolution asking the Legislature for authority is a start, not a protection on its own.</p>
  <ul class="rows">
{items}
  </ul>
  <p>Know of another? <a href="mailto:contact@grailsystems.io?subject=Standard%20adopted">Tell us</a> and send the record. We add it after we check it.</p>
</section>

'''
import re
m = re.search(r"<section[^>]*>\s*<h2[^>]*>Use it</h2>", s); assert m, "anchor not found"
s = s[:m.start()] + section + s[m.start():]
open(p, "w").write(s); print(f"Adoption list added: {len(rows)} entries, {n} governments adopted")
