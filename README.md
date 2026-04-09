# MS<sup>3</sup>L.io

MS<sup>3</sup>L GitHub Pages website for the Membrane-based Sustainable Separation Solutions Laboratory.

## Local Preview

This repository can be previewed with Jekyll. On Windows, Ruby native gems may fail when the repo is located in a non-ASCII path.

Recommended workflow:

1. Edit the source repo normally.
2. Copy it to an ASCII-only preview path if needed.
3. Run `bundle install`.
4. Run `bundle exec jekyll serve`.

The current project also includes a reusable sub-agent workflow guide in `docs/subagent-playbook.md`.

## Data Validation

Run structured data validation before publishing updates:

```bash
python scripts/validate_site.py
```

This invokes `scripts/validate_site.rb` to validate YAML syntax and required fields for members, publications, and patents.
