import os, html
E = html.escape
T = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{name} County Watch | Grail Systems</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{name} County Watch">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://grailsystems.io/{slug}/">
<meta property="og:image" content="https://grailsystems.io/img/grail_share.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;600;800&family=Young+Serif&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/watch.css">
<style>.counts{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:1px;background:var(--rule);border:1px solid var(--rule);margin:18px 0 6px}}.counts div{{background:var(--card);padding:16px}}.counts b{{display:block;font-family:'Young Serif',Georgia,serif;font-weight:400;font-size:2.1rem;line-height:1.1;color:var(--pine)}}.counts span{{font-size:.92rem;color:var(--muted)}}</style>
</head>
<body>
<div class="wrap">
<nav class="top"><a class="brand" href="/">Grail <span>Systems</span></a><a href="/texas">Texas Watch</a><a href="/standards">The Standard</a><a href="/companies">Companies</a><a href="/records">Records</a><a href="/network">Join the network</a></nav>
<div class="hero">
  <h1>{title}</h1>
  <p>{intro}</p>
  <p class="by">Compiled by Grail Systems from news reports and public records. Checked {checked}. Corrections welcome.</p>
</div>
<section><h2>At a glance</h2><div class="counts">{counts}</div></section>
<section><h2>The projects</h2><ul class="rows">{projects}</ul>
<span class="src">Know something we're missing? <a href="mailto:contact@grailsystems.io?subject={name}%20County%20tip">Tell us</a>.</span></section>
<section><h2>What has happened</h2><ul class="rows">{timeline}</ul></section>
<section><h2>Lessons for other counties</h2><ul class="rows">{lessons}</ul></section>
<section><h2>Sources</h2><p>{sources}</p></section>
<footer>
  <span>{name} County Watch · Grail Systems</span>
  <a href="/texas">Texas Watch</a>
  <a href="/standards">The Deep East Texas Standard</a>
  <a href="/angelina/">Angelina County Watch</a>
  <a href="mailto:contact@grailsystems.io">contact@grailsystems.io</a>
</footer>
</div>
</body>
</html>
"""
def li(tags, title, text):
    t = "".join('<span class="tag">%s</span>' % E(x) for x in tags)
    return '\n<li>%s<h3>%s</h3><p>%s</p></li>' % (t, E(title), E(text))
def build(c):
    os.makedirs(c["slug"], exist_ok=True)
    out = T.format(
        name=E(c["name"]), slug=c["slug"], desc=E(c["desc"]), title=E(c["title"]), intro=E(c["intro"]),
        checked=E(c["checked"]), sources=E(c["sources"]),
        counts="".join('<div><b>%s</b><span>%s</span></div>' % (E(n), E(t)) for n, t in c["counts"]),
        projects="".join(li(*p) for p in c["projects"]),
        timeline="".join(li([d], h, x) for d, h, x in c["timeline"]),
        lessons="".join(li([], h, x) for h, x in c["lessons"]))
    open(os.path.join(c["slug"], "index.html"), "w").write(out)
    print("built /%s/" % c["slug"])
