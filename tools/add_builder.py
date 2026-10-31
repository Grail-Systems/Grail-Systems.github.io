"""Add the records-request builder to county pages. Safe to run again; skips pages that have it."""
import os, html
B = {
 "anderson": ("Anderson", "City of Palestine", "Palestine Economic Development Corporation", "Neches & Trinity Valleys Groundwater Conservation District", "NextEra Energy, Comstock Resources"),
 "navarro": ("Navarro", "City of Corsicana", "", "", "Riot Platforms, Hedgehog USA"),
 "henderson": ("Henderson", "City of Athens", "Athens Economic Development Corporation", "Neches & Trinity Valleys Groundwater Conservation District", "Diode Ventures, Data Factory"),
 "milam": ("Milam", "City of Rockdale", "Rockdale Municipal Development District", "Post Oak Savannah Groundwater Conservation District", "Riot Platforms, Bitdeer, SB Energy"),
 "hood": ("Hood", "City of Granbury", "", "Upper Trinity Groundwater Conservation District", "MARA Holdings, Sailfish Development, Bilateral Energy"),
 "ellis": ("Ellis", "City of Midlothian", "Midlothian Economic Development", "Prairielands Groundwater Conservation District", "Google, DataBank, Compass Datacenters"),
 "hays": ("Hays", "City of San Marcos", "", "", "CloudBurst, Sabey Data Centers, Highlander SM One LLC"),
 "young": ("Young", "City of Graham", "", "", "Stream Data Centers"),
 "somervell": ("Somervell", "City of Glen Rose", "", "Prairielands Groundwater Conservation District", "Amazon, Black Mountain Power"),
 "elpaso": ("El Paso", "City of El Paso", "", "", "Meta, Wurldwide LLC, EdgeCore"),
 "newton": ("Newton", "City of Newton", "", "Southeast Texas Groundwater Conservation District", "Clean Holding Company, USA BioEnergy"),
}
E = lambda s: html.escape(s, quote=True)
for slug, (county, city, edc, gcd, co) in B.items():
    p = os.path.join(slug, "index.html")
    if not os.path.exists(p): print("no page:", p); continue
    s = open(p).read()
    if 'id="ask"' in s: print("already has builder:", slug); continue
    block = f'<section id="ask" data-county="{E(county)}" data-city="{E(city)}" data-edc="{E(edc)}" data-gcd="{E(gcd)}" data-companies="{E(co)}"></section>\n<script src="/assets/requestbuilder.js" defer></script>\n'
    anchor = '<script src="/assets/livewatch.js" defer></script>\n'
    s = s.replace(anchor, anchor + block, 1) if anchor in s else s.replace("<footer>", block + "<footer>", 1)
    open(p, "w").write(s); print("request builder added:", slug)
