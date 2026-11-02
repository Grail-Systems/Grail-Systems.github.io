"""Black Mountain profile: add the May 2026 donation by its vice president of land to PACs tied to Paxton's campaign (KERA, Aug 11, 2026)."""
import re
f = "companies.html"; s = open(f).read()
ADD = (" Its vice president of land gave $17,000 in May 2026 to PACs associated with Attorney General Ken Paxton\u2019s campaign, "
       "according to FEC filings reported by KERA, while Hood County awaited a ruling from Paxton\u2019s office on its proposed data center moratorium.")
if "vice president of land gave $17,000" not in s:
    s, n = re.subn(r'(\{name:"Black Mountain[^"]*".*?know:"[^"]*?)(", conf:)', lambda m: m.group(1) + ADD + m.group(2), s, count=1)
    assert n == 1, "Black Mountain profile not found"
    open(f, "w").write(s)
print("Batch 69: Black Mountain profile updated (KERA, Aug 11, 2026)")
