import re, json
s = open("texas.html").read()
a = s.index("const projects = [") + len("const projects = ")
b = s.index("];\n\nconst actions") + 1
js = s[a:b]
keys = "name|county|type|status|lat|lng|dev|power|water|conf|note|link|src"
js = re.sub(r'([{,]\s*)(' + keys + r'):', r'\1"\2":', js)
data = json.loads(js)
json.dump(data, open("data/projects.json", "w"), indent=1, ensure_ascii=False)
print("Exported", len(data), "projects to data/projects.json")
