from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
validator = ROOT / "scripts" / "validate_site.rb"

DATA_FILES = {
    "lab": ROOT / "_data" / "lab.yml",
    "members": ROOT / "_data" / "members.yml",
    "research": ROOT / "_data" / "research.yml",
    "publications": ROOT / "_data" / "publications.yml",
    "news": ROOT / "_data" / "news.yml",
    "patents": ROOT / "_data" / "patents.yml",
}


def clean_value(value):
    value = value.strip()
    if value in {"|-", ">-", "|", ">"}:
        return ""
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        value = value[1:-1]
    return value.strip()


def entries(path):
    items = []
    current = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if re.match(r"^- ", line):
            if current is not None:
                items.append(current)
            current = {}
            remainder = line[2:]
            if ":" in remainder:
                key, value = remainder.split(":", 1)
                current[key.strip()] = clean_value(value)
            continue
        if current is None:
            continue
        match = re.match(r"^\s{2,}([A-Za-z0-9_]+):\s*(.*)$", line)
        if match:
            current[match.group(1)] = clean_value(match.group(2))
    if current is not None:
        items.append(current)
    return items


def valid_url(value):
    return not value or value.startswith("http://") or value.startswith("https://")


def valid_asset_path(value):
    return (
        not value
        or (value.startswith("/assets/images/") and ".." not in value and "<" not in value and ">" not in value)
    )


def valid_url_or_asset(value):
    return valid_url(value) or valid_asset_path(value)


def valid_doi(value):
    return not value or re.match(r"^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$", value)


def fallback_validate():
    errors = []
    for name, path in DATA_FILES.items():
        if not path.exists():
            errors.append(f"Missing file: {path}")

    for index, member in enumerate(entries(DATA_FILES["members"])):
        for key in ("name", "role_group"):
            if not member.get(key):
                errors.append(f"members[{index}].{key} is required")
        if member.get("email") and "@" not in member["email"]:
            errors.append(f"members[{index}].email is invalid: {member['email']}")
        if member.get("image_url") and not valid_url_or_asset(member["image_url"]):
            errors.append(f"members[{index}].image_url must be an http(s) URL or /assets/images/ path")

    for index, item in enumerate(entries(DATA_FILES["research"])):
        if item.get("image") and not valid_url_or_asset(item["image"]):
            errors.append(f"research[{index}].image must be an http(s) URL or /assets/images/ path")

    for index, item in enumerate(entries(DATA_FILES["news"])):
        if item.get("image") and not valid_url_or_asset(item["image"]):
            errors.append(f"news[{index}].image must be an http(s) URL or /assets/images/ path")

    for index, publication in enumerate(entries(DATA_FILES["publications"])):
        for key in ("title", "venue", "year"):
            if not publication.get(key):
                errors.append(f"publications[{index}].{key} is required")
        if publication.get("year") and not re.match(r"^\d{4}$", publication["year"]):
            errors.append(f"publications[{index}].year must be 4 digits")
        if not valid_doi(publication.get("doi", "")):
            errors.append(f"publications[{index}].doi invalid format")
        if not valid_url(publication.get("url", "")):
            errors.append(f"publications[{index}].url invalid URL")

    for index, patent in enumerate(entries(DATA_FILES["patents"])):
        for key in ("title", "registration"):
            if not patent.get(key):
                errors.append(f"patents[{index}].{key} is required")

    for line_number, line in enumerate(DATA_FILES["lab"].read_text(encoding="utf-8").splitlines(), start=1):
        if re.match(r"^\s+image:\s+", line):
            value = clean_value(line.split(":", 1)[1])
            if value and not valid_url_or_asset(value):
                errors.append(f"lab.yml:{line_number} image must be an http(s) URL or /assets/images/ path")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed: data files satisfy fallback checks.")
    return 0


if shutil.which("ruby"):
    result = subprocess.run(["ruby", str(validator)], cwd=ROOT)
    sys.exit(result.returncode)

print("Ruby was not found; running Python fallback validation.")
sys.exit(fallback_validate())
