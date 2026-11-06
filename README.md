# Kulp Lights Controller Manual

Source for the hardware manual for the Kulp Lights PocketBeagle 2 controllers
(K8-Pro, K8-Max, K16, K16-Pro, K16-Max, K32, K32-Pro, K32-Max, PocketScroller v3, PocketScroller-16).

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and published at
<https://kulplights.com/manuals/>. On every push to `main`, `.github/workflows/publish.yml` builds the
site and force-pushes the result to the `publish` branch; a webhook on the web server then pulls
that branch into place.

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve        # live preview on http://127.0.0.1:8000
.venv/bin/mkdocs build --strict
```

The pages are in `docs/`. Board renders are in `docs/assets/boards/` and come from the KiCad
files with `kicad-cli pcb render`.
