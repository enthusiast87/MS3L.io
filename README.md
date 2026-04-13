# MS<sup>3</sup>L.io

MS<sup>3</sup>L GitHub Pages website for the Membrane-based Sustainable Separation Solutions Laboratory.

## Local Preview

This repository can be previewed with Jekyll. On Windows, Docker is the simplest option because it avoids host Ruby setup and works better with GitHub Pages dependencies.

Recommended workflow:

1. Build and start the development container:
   `docker compose -f compose.dev.yaml up --build`
2. Open `http://localhost:4000/`
3. Edit files in the repo and let the browser reload automatically

Notes:

- The container publishes both `4000` and the live reload port `35729`.
- `--force_polling` is enabled in the container command because file watching over Docker bind mounts on Windows is often unreliable without polling.
- Gems are cached in the Docker volume `bundle_cache`, so after the first install subsequent starts are faster.
- If the `Gemfile` changes, rerun with `--build`.
- If your network injects a corporate SSL certificate, export the root certificate as a `.crt` file into `certs/` before starting Docker. The compose file mounts that directory into the container and runs `update-ca-certificates` on startup.
- Production deploy still uses `_config.yml`; the Docker dev flow adds `_config_dev.yml` so local preview works at the root path.

The current project also includes a reusable sub-agent workflow guide in `docs/subagent-playbook.md`.

## Data Validation

Run structured data validation before publishing updates:

```bash
python scripts/validate_site.py
```

This invokes `scripts/validate_site.rb` to validate YAML syntax and required fields for members, publications, and patents.
