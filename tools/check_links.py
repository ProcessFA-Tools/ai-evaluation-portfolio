"""Verify relative Markdown links without network access or dependencies."""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]\n]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")


def main():
    failures = []
    count = 0
    for document in sorted(ROOT.rglob("*.md")):
        if ".git" in document.parts:
            continue
        for target in LINK.findall(document.read_text(encoding="utf-8")):
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            count += 1
            resolved = (document.parent / unquote(parts.path)).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                failures.append(f"{document.relative_to(ROOT)}: {target}")
    if failures:
        raise SystemExit("Broken or out-of-repository links:\n" + "\n".join(failures))
    print(f"Checked {count} relative Markdown links: all targets exist.")


if __name__ == "__main__":
    main()
