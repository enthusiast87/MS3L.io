# MS<sup>3</sup>L.io

MS<sup>3</sup>L GitHub Pages website for the Membrane-based Sustainable Separation Solutions Laboratory.

Page content lives in `_data/*.yml`. `docs/content-guide.md` records what goes in which file and how entries are formatted, so a new member, paper or news item lands consistent with the ones already there.

## Local Preview

This repository can be previewed with Jekyll. On Windows, Docker is the simplest option because it avoids host Ruby setup and works better with GitHub Pages dependencies.

Recommended workflow:

1. Build and start the development container:
   `.\scripts\dev-up.ps1`
2. Open `http://localhost:4000/`
3. Edit files in the repo and let the browser reload automatically

Useful shortcuts:

- `.\scripts\dev-up.ps1`: start in the foreground with rebuild
- `.\scripts\dev-up.ps1 -Detached`: start in the background
- `.\scripts\dev-up.ps1 -Detached -Logs`: start in the background and immediately tail logs
- `.\scripts\dev-up.ps1 -NoBuild`: start without rebuilding the image
- `.\scripts\dev-logs.ps1`: tail dev server logs
- `.\scripts\dev-down.ps1`: stop and remove the dev container

Notes:

- The container publishes both `4000` and the live reload port `35729`.
- `--force_polling` is enabled in the container command because file watching over Docker bind mounts on Windows is often unreliable without polling.
- Gems are cached in the Docker volume `bundle_cache`, so after the first install subsequent starts are faster.
- If the `Gemfile` changes, rerun with `--build`.
- If your network injects a corporate SSL certificate, export the root certificate as a `.crt` file into `certs/` before starting Docker. The compose file mounts that directory into the container and runs `update-ca-certificates` on startup.
- Production deploy still uses `_config.yml`; the Docker dev flow adds `_config_dev.yml` so local preview works at the root path.

## Data Validation

Run structured data validation before publishing updates:

```bash
python scripts/validate_site.py
```

This invokes `scripts/validate_site.rb` to validate YAML syntax and required fields for members, publications, and patents.
If Ruby is not installed, the Python wrapper runs a fallback validation pass for the same core fields.

## Local Admin

Run the draft-only admin UI when Ruby is available:

```bash
ruby scripts/admin_server.rb
```

Open `http://localhost:4567/` to create draft updates for news, members, and research images. The tool writes `_data/*.yml.draft` files and does not publish changes automatically.
