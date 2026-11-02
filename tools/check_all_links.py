"""Link check across both repos: runs check_links.py, then accepts links into /carrizo_wilcox_aquifer/ only if that file exists AND is committed in ~/carrizo_wilcox_aquifer."""
import subprocess, os, re, sys
OTHER = os.path.expanduser("~/carrizo_wilcox_aquifer/")
out = subprocess.run([sys.executable, "tools/check_links.py"], capture_output=True, text=True).stdout
real = []
for line in out.splitlines():
    m = re.match(r"BROKEN: (\S+) -> (\S+)", line)
    if not m: continue
    target = m.group(2).split("#")[0]
    if target.startswith("/carrizo_wilcox_aquifer/"):
        rel = target[len("/carrizo_wilcox_aquifer/"):]
        tracked = subprocess.run(["git", "-C", OTHER, "ls-files", "--error-unmatch", rel], capture_output=True).returncode == 0
        if os.path.exists(OTHER + rel) and tracked: continue
    real.append(line)
for line in real: print(line)
print(f"Checked both repos. Broken links: {len(real)}")
