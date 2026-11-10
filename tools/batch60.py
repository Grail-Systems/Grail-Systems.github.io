"""Sign-up form: add a 'Join the network' button under the page heading on the Network, Know Your Tools and Checklist pages."""
import re
FORM = "https://forms.gle/XCe1hun4F9XBkCYdA"
BOX = ('\n<div class="joinbox noprint" style="margin:1rem 0 1.4rem;padding:1rem 1.2rem;border:2px solid var(--pine);border-radius:10px">'
       '<a href="' + FORM + '" target="_blank" rel="noopener" style="display:inline-block;background:var(--pine);color:#fff;'
       'font-weight:800;padding:.7rem 1.1rem;border-radius:8px;text-decoration:none">Join the Ground Truth Texas network &rarr;</a>'
       '<p style="margin:.6rem 0 0">Two minutes. Get records, meeting alerts and tools for your county. We never publish or share your information.</p></div>')
done = []
for page in ["network.html", "know-your-tools.html", "checklist.html"]:
    s = open(page).read()
    if FORM in s:
        done.append(page + " (already had it)"); continue
    m = re.search(r'<div class="hero">.*?</div>', s, re.S)
    assert m, page + ": page heading block not found; nothing changed"
    s = s[:m.end()] + BOX + s[m.end():]
    open(page, "w").write(s)
    done.append(page)
print("Batch 60: join button added to " + ", ".join(done))
