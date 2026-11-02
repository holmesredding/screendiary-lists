# ScreenDiary curated lists

Validate every URL in the root `curated_lists*.json` manifests against the
checked-out repository with Python 3.9 or later (no dependencies or network needed):

```sh
python3 scripts/validate_manifests.py
```

The same check runs on pushes and pull requests through GitHub Actions. It rejects
malformed manifests, URLs outside this repository's `main/JSON/` directory, and
missing files. New root manifests matching the pattern are checked automatically.

## Application manifest

`curated_lists_241.json` is the active manifest used by the current ScreenDiary
application source and contains 95 entries. The app's
[`fetchGitHubLists()` in `CuratedListsView.swift`](https://github.com/holmesredding/screendiary/blob/main/ScreenDiary/Recommendations/CuratedListsView.swift#L464)
explicitly fetches this manifest from this repository's `main` branch. Target
`curated_lists_241.json` when updating the lists available in the current app.

## Historical manifests

`curated_lists.json` and `curated_lists_original.json` are retained as historical
manifests. Each contains 36 entries, including 19 historical Academy Awards lists.
They preserve earlier list selections and are not the manifest fetched by the
current application source.

Those 19 JSON files were restored unchanged from the parent of commit
`4ba1702ea1edf0dfe2e1ab67d05ed3f8e2f04950`, which deleted them.
Their 2024 filenames and historical contents are preserved.
