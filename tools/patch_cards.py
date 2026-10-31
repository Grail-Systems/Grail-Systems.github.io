p = "texas.html"
s = open(p).read()
if "extraHTML" in s:
    print("already patched"); raise SystemExit
def rep(old, new):
    global s
    assert s.count(old) == 1, "not found once: " + old[:60]
    s = s.replace(old, new)
rep('    </select>\n  </div>\n  <ul class="rows" id="rows"></ul>',
    '    </select>\n    <label style="display:flex;align-items:center;gap:6px;font-weight:600"><input type="checkbox" id="soonFilter"> <span id="soonLabel">Hearing or deadline in the next 30 days</span></label>\n  </div>\n  <div id="upcoming"></div>\n  <ul class="rows" id="rows"></ul>')
a = s.index("  m.bindPopup(`"); b = s.index("`);\n  return m;", a) + len("`);")
s = s[:a] + "  m.bindPopup(popupHTML(p), {maxHeight: 340});" + s[b:]
helpers = r'''const soon = new Set();
const fmtD = d => new Date(d + "T12:00:00").toLocaleDateString("en-US", {month:"short", day:"numeric", year:"numeric"});
const pslug = n => n.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
const extraFields = p => [["Location", p.loc], ["Related companies and LLCs", p.llc], ["Land", p.land], ["Incentives", p.incent], ["Key dates", p.dates]].filter(x => x[1]);
const nextLine = e => `${esc(fmtD(e.date))}${e.time ? ", " + esc(e.time) : ""}: ${esc(e.what)}${e.where ? ", " + esc(e.where) : ""}`;
function extraHTML(p) {
  return (p.next || []).map(e => `<p><b style="color:var(--alarm)">Coming up:</b> ${nextLine(e)}</p>`).join("") +
    extraFields(p).map(([k, v]) => `<p><b>${k}:</b> ${esc(v)}</p>`).join("");
}
function popupHTML(p) {
  return `<strong>${esc(p.name)}</strong><br>${esc(p.county)} County · ${statusText[p.status]}<br><br>` +
    (p.next || []).map(e => `<b style="color:var(--alarm)">Coming up:</b> ${nextLine(e)}<br>`).join("") +
    `<b>Developer:</b> ${esc(p.dev)}<br><b>Power:</b> ${esc(p.power)}<br><b>Water:</b> ${esc(p.water)}<br>` +
    extraFields(p).map(([k, v]) => `<b>${k}:</b> ${esc(v)}<br>`).join("") +
    `<br>${esc(p.note)}<br><br>${p.src ? "<b>Sources:</b> " + esc(p.src) + "<br><br>" : ""}` +
    `<span class="tag">${esc(p.conf)}</span>${p.link ? `<a href="${p.link}">County page</a>` : ""} &nbsp;<a href="#${pslug(p.name)}">Link to this project</a>`;
}
'''
rep("const markers = projects.map(", helpers + "const markers = projects.map(")
rep('const hay = [p.name, p.county, p.dev, p.water, p.note].join(" ").toLowerCase();',
    'const hay = [p.name, p.county, p.dev, p.water, p.note, p.loc, p.llc, p.land, p.incent, p.dates].join(" ").toLowerCase();')
rep("const show = (!q || hay.includes(q)) && (!t || p.type === t) && (!s || p.status === s);",
    'const show = (!q || hay.includes(q)) && (!t || p.type === t) && (!s || p.status === s) && (!document.getElementById("soonFilter").checked || soon.has(p.name));')
rep("""'<p><b>Sources:</b> ' + esc(p.src) + '</p>' : ''}`;""",
    """'<p><b>Sources:</b> ' + esc(p.src) + '</p>' : ''}${extraHTML(p)}`;""")
rep('["search","typeFilter","statusFilter"].forEach(id => document.getElementById(id).addEventListener("input", render));',
    '["search","typeFilter","statusFilter"].forEach(id => document.getElementById(id).addEventListener("input", render));\ndocument.getElementById("soonFilter").addEventListener("change", render);')
rep('markers.forEach((m, i) => m.setPopupContent(m.getPopup().getContent() + ` &nbsp;<a href="#${slug(projects[i].name)}">Link to this project</a>`));\n', '')
rep('["name","county","type","status","dev","power","water","note","conf","src","lat","lng"]',
    '["name","county","type","status","dev","loc","llc","power","land","water","incent","dates","note","conf","src","lat","lng"]')
loader = r'''
Promise.all([fetch("/data/details.json").then(r => r.json()), fetch("/data/events.json").then(r => r.json())]).then(([D, E]) => {
  projects.forEach(p => Object.assign(p, D[p.name] || {}));
  const today = new Date(); today.setHours(0, 0, 0, 0);
  const in30 = new Date(today); in30.setDate(in30.getDate() + 30);
  const up = E.filter(e => new Date(e.date + "T12:00:00") >= today).sort((a, b) => a.date.localeCompare(b.date));
  up.forEach(e => {
    const d = new Date(e.date + "T12:00:00");
    e.projects.forEach(n => { const p = projects.find(x => x.name === n); if (!p) return; (p.next = p.next || []).push(e); if (d <= in30) soon.add(n); });
  });
  markers.forEach((m, i) => m.setPopupContent(popupHTML(projects[i])));
  document.getElementById("soonLabel").textContent = `Hearing or deadline in the next 30 days (${soon.size})`;
  if (up.length) document.getElementById("upcoming").innerHTML = `<h3 style="margin-top:18px">Coming up</h3><ul class="rows">` + up.map(e =>
    `<li><span class="tag">${esc(fmtD(e.date))}${e.time ? ", " + esc(e.time) : ""}</span>${e.expected ? '<span class="tag">Expected</span>' : ""}
     <h3>${esc(e.what)}</h3><p>${esc(e.where || "")}${e.projects.length ? " · Affects: " + e.projects.map(n => `<a href="#${pslug(n)}">${esc(n)}</a>`).join(", ") : ""}</p>
     ${e.src ? `<p><b>Source:</b> ${esc(e.src)}</p>` : ""}</li>`).join("") + `</ul>`;
  render();
}).catch(() => {});
'''
rep("goToHash();\n</script>", "goToHash();\n" + loader + "</script>")
open(p, "w").write(s)
print("Map cards upgraded")
