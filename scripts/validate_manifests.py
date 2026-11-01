#!/usr/bin/env python3
"""Check every curated manifest URL against the local repository, offline."""

import json
from pathlib import Path, PurePosixPath
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
URL_PREFIX = "/holmesredding/screendiary-lists/main/"


def main():
    errors = []
    manifests = sorted(ROOT.glob("curated_lists*.json"))
    if not manifests:
        errors.append("No curated_lists*.json manifests found")
    for manifest in manifests:
        try:
            entries = json.loads(manifest.read_text(encoding="utf-8"))
            if not isinstance(entries, list) or not entries:
                raise ValueError("expected a non-empty array")
        except (ValueError, OSError) as error:
            errors.append(f"{manifest.name}: {error}")
            continue
        for index, entry in enumerate(entries, 1):
            label = f"{manifest.name}, entry {index}"
            url = entry.get("url") if isinstance(entry, dict) else None
            if not isinstance(url, str):
                errors.append(f"{label}: missing or invalid URL")
                continue
            try:
                parsed = urlsplit(url)
                if (parsed.scheme != "https"
                        or parsed.netloc != "raw.githubusercontent.com"
                        or not parsed.path.startswith(URL_PREFIX)
                        or parsed.query or parsed.fragment):
                    raise ValueError("expected a raw URL for this repository's main branch")
                relative = unquote(parsed.path[len(URL_PREFIX):])
                path = PurePosixPath(relative)
                if (not relative or path.is_absolute() or ".." in path.parts
                        or not path.parts or path.parts[0] != "JSON"):
                    raise ValueError("expected a file inside JSON/")
                target = ROOT / relative
                if not target.resolve().is_relative_to(ROOT) or not target.is_file():
                    raise ValueError(f"missing repository file: {relative}")
            except ValueError as error:
                errors.append(f"{label} ({entry.get('title', 'untitled')}): {error}")
        print(f"{manifest.name}: checked {len(entries)} URLs")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("All manifest URLs point to existing repository files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
