from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]

yaml_files = [
    ROOT / "_data" / "members.yml",
    ROOT / "_data" / "research.yml",
    ROOT / "_data" / "publications.yml",
]

for path in yaml_files:
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            yaml.safe_load(f)

print("YAML validation passed.")
