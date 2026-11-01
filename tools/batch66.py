"""Sign-up button: now says 'Get alerts for your county' (county email alerts went live Nov 1, 2026)."""
PAIRS = [
 ("Join the Texas Watch network &rarr;</a>", "Get alerts for your county &rarr;</a>"),
 ("Two minutes. Get records, meeting alerts and tools for your county.",
  "Two minutes. Get an email when something new shows up in your county, plus records, meeting alerts and tools."),
]
for f in ["network.html", "know-your-tools.html", "checklist.html"]:
    s = open(f).read(); n = 0
    for old, new in PAIRS:
        if new in s: continue
        assert s.count(old) == 1, f + " not found: " + old[:40]
        s = s.replace(old, new); n += 1
    open(f, "w").write(s)
    print(f, "updated" if n else "already done")
print("Batch 66: sign-up buttons now offer county alerts")
