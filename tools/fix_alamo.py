"""Correct Alamo Mission LLC on the Ellis page and the Google company card: Midlothian is Sharka LLC; Alamo Mission is Red Oak."""
F = {
 "ellis/index.html": [
  ("built starting in 2019 through a shell company, Alamo Mission LLC, under the project name Sharka.", "built starting in 2019 through a shell company, Sharka LLC."),
  ("Google&#x27;s first Midlothian building was filed under Alamo Mission LLC.", "Google&#x27;s Midlothian buildings were filed under Sharka LLC. Its Red Oak campus is registered to another shell, Alamo Mission LLC."),
  ("Google built here as Alamo Mission LLC.", "Google built here as Sharka LLC and Alamo Mission LLC.")],
 "companies.html": [
  ('entities:"Built Midlothian through shell company Alamo Mission LLC (project Sharka)"', 'entities:"Midlothian is registered to Sharka LLC and Red Oak to Alamo Mission LLC; the occupant on both is Design LLC (Texas Comptroller)"')],
}
for p, pairs in F.items():
    s = open(p).read()
    for old, new in pairs:
        if new in s: continue
        assert s.count(old) == 1, f"not found in {p}: {old[:60]}"; s = s.replace(old, new)
    open(p, "w").write(s)
print("Alamo Mission fixed on the Ellis page and the Google company card")
