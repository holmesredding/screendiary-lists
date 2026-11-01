# ScreenDiary curated lists

Validate every URL in the root `curated_lists*.json` manifests against the
checked-out repository with Python 3.9 or later (no dependencies or network needed):

```sh
python3 scripts/validate_manifests.py
```

The same check runs on pushes and pull requests through GitHub Actions. It rejects
malformed manifests, URLs outside this repository's `main/JSON/` directory, and
missing files. New root manifests matching the pattern are checked automatically.

`curated_lists_241.json` contains 95 entries. `curated_lists.json` and
`curated_lists_original.json` each contain 36 entries, including 19 historical
Academy Awards lists. Those 19 JSON files were restored unchanged from the parent
of commit `4ba1702ea1edf0dfe2e1ab67d05ed3f8e2f04950`, which deleted them.
Their 2024 filenames and historical contents are preserved.

These manifests alone do not establish which manifest the current app consumes.
