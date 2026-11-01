p = "records.html"; s = open(p).read()
if "libTags" in s:
    print("already patched"); raise SystemExit
a = s.index('  const URL = "https://raw.githubusercontent.com/Grail-Systems/carrizo_wilcox_aquifer/main/frontend/library.json";')
b = s.index("})();", a) + len("})();\n")
s = s[:a] + open("/tmp/libjs.txt").read() + s[b:]
old = '<ul class="rows" id="libList">'
assert s.count(old) == 1; s = s.replace(old, '<div id="libTags"></div>\n  ' + old)
s = s.replace("Every record we've received and published, searchable by the words inside it.", "Every record we've received and published. Search every page, or tap a company, agency or topic to see everything tagged with it.", 1)
open(p, "w").write(s); print("records library: tags and full-page search")
