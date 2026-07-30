from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
changed = []

for path in (ROOT / "content").rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3:
        continue

    match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', parts[1], re.MULTILINE)
    if not match:
        continue

    title = match.group(1).strip().strip("\"'")
    body = parts[2]
    updated = re.sub(
        rf"\A(\s*)#\s+{re.escape(title)}\s*\n+",
        r"\1",
        body,
        count=1,
    )
    if updated != body:
        path.write_text("---".join((parts[0], parts[1], updated)), encoding="utf-8")
        changed.append(path.relative_to(ROOT))

print(f"Removed {len(changed)} duplicate body titles.")
