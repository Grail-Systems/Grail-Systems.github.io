"""Verified tonight: Cipher McLennan quote (KXXV, DCD) named and sharpened; Mikeska site road added from tracker listing."""
fixes = {
 "companies.html": [(
  ' In McLennan County, a commissioner said Texas law gives the county little authority over the project.',
  ' In McLennan County, near Riesel, Precinct 2 Commissioner D.L. Wilson said he opposes data centers in the county but that Texas law gives commissioners little authority to stop them (KXXV; Data Center Dynamics).')],
 "texas.html": [(
  'Power was promised for 2027; trackers now say 2028 to 2030. Pin is approximate."',
  'Power was promised for 2027; trackers now say 2028 to 2030. One tracker lists the site on East County Road 368. Pin is approximate."')],
}
for f, pairs in fixes.items():
    s = open(f).read()
    for old, new in pairs:
        if new in s: continue
        assert s.count(old) == 1, f + " not found: " + old[:50]; s = s.replace(old, new)
    open(f, "w").write(s)
print("Batch 63: Cipher McLennan quote verified and named; Mikeska road added")
