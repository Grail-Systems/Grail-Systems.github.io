"""Batch 31: HyperDataGrid card names the former Northern Chip Mill (same site as 3641 Ben Dunn Rd, off Highway 103 West)."""
old = 'note:"3641 Ben Dunn Rd, about 187 acres.'
new = 'note:"3641 Ben Dunn Rd, off State Highway 103 West, at the former Northern Chip Mill property; about 187 acres.'
s = open("texas.html").read()
if new not in s:
    assert s.count(old) == 1, "HyperDataGrid note not found"; s = s.replace(old, new)
open("texas.html", "w").write(s)
print("Batch 31: HyperDataGrid card now names the old chip mill site")
