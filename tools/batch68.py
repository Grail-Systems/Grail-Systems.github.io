"""County records (v2, fixed document paths): show Angelina County's public records requests, their status and every document we got back, on the Angelina page.
Rerunnable: rebuilds the block between its markers from data/records.json, so rerun it whenever records.json changes."""
import json, html, os
PREFIX = "/carrizo_wilcox_aquifer/"   # the records files live in the carrizo_wilcox_aquifer repo, served under this path
SRC = os.path.expanduser("~/carrizo_wilcox_aquifer/")
E = html.escape
d = json.load(open("data/records.json")); reqs = d["requests"]
COUNTY_AGENCIES = {"angelina": ["City of Lufkin", "Lufkin Economic Development Corporation", "Pineywoods Groundwater Conservation District", "Angelina County"]}
def fmt(day):
    y, m, dd = day.split("-"); M = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][int(m)-1]
    return f"{M} {int(dd)}, {y}"
def block(rs):
    rows = []
    for r in sorted(rs, key=lambda r: r.get("filed", ""), reverse=True):
        num = f" {E(r['number'])}" if r.get("number") else ""
        docs = r.get("documents") or []
        seen, dl = set(), []
        for x in docs:
            if x["href"] in seen: continue
            seen.add(x["href"])
            assert os.path.exists(SRC + x["href"]), "document file not found: " + SRC + x["href"]
            pg = f" ({x['pages']} pages)" if x.get("pages") else ""
            dl.append(f'<li><a href="{PREFIX}{E(x["href"])}">{E(x["title"])}</a>{pg}</li>')
        docs_html = (f'<ul style="margin:8px 0 0;padding-left:20px;line-height:1.6">{"".join(dl)}</ul>' if dl
                     else '<p style="margin:8px 0 0;color:#555">No documents released yet.</p>')
        rows.append(f'<li style="border-top:1px solid #d4d9d3;padding:14px 0">'
                    f'<b>{E(r["agency"])}{num}</b> <span style="color:#555">filed {fmt(r["filed"])}</span><br>'
                    f'<span style="font-weight:600;color:var(--pine,#1f4a36)">{E(r["status"])}</span>'
                    f'<details style="margin-top:6px"><summary style="cursor:pointer">What we asked for</summary><p style="margin:6px 0 0;line-height:1.55">{E(r["asked"])}</p></details>'
                    f'{docs_html}' + ''.join(f'<p style="margin:6px 0 0;color:#555">{E(n)}</p>' for n in (r.get("privacy_notes") or [])) + '</li>')
    n_docs = sum(len({x["href"] for x in (r.get("documents") or [])}) for r in rs)
    return ('<!--records:start-->\n<section id="records" style="margin:1.6rem 0">'
            '<h2>Records we asked for</h2>'
            f'<p>{len(rs)} public information requests, {n_docs} documents released so far. '
            'Every deadline is tracked on the <a href="/records.html#list-section">records page</a>.</p>'
            f'<ul style="list-style:none;margin:0;padding:0">{"".join(rows)}</ul></section>\n<!--records:end-->')
for county, agencies in COUNTY_AGENCIES.items():
    f = f"{county}/index.html"; s = open(f).read()
    rs = [r for r in reqs if r["agency"] in agencies]
    unmatched = sorted({r["agency"] for r in reqs if not any(r["agency"] in a for a in COUNTY_AGENCIES.values())})
    new = block(rs)
    if "<!--records:start-->" in s:
        a = s.index("<!--records:start-->"); b = s.index("<!--records:end-->") + len("<!--records:end-->")
        s = s[:a] + new + s[b:]
    else:
        i = s.find('<div class="joinbox'); assert i >= 0, "alert box not found on " + f
        s = s[:i] + new + "\n" + s[i:]
    open(f, "w").write(s)
    print(f, "requests:", len(rs), "| unmatched agencies:", unmatched or "none")
print("Batch 68: Angelina County page now lists its records requests and documents")
