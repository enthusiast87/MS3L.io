#!/usr/bin/env python3
"""Import public Google Sites images into local Jekyll assets.

The script has three modes:

- dry run: inspect data files and optional Google Sites pages.
- draft: download images and write *.asset-import-draft files.
- apply: download images and update the source YAML files in place.

It intentionally uses only Python's standard library so it can run on a
fresh Windows machine before Ruby/Jekyll dependencies are installed.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import mimetypes
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SITE_URL = "https://sites.google.com/view/kim-jihoon/home"
SITE_PREFIX = "https://sites.google.com/view/kim-jihoon"
DATA_FILES = [
    ROOT / "_data" / "lab.yml",
    ROOT / "_data" / "members.yml",
    ROOT / "_data" / "news.yml",
    ROOT / "_data" / "research.yml",
]
IMAGE_URL_RE = re.compile(r"https://lh3\.googleusercontent\.com/[^\s\"'<>\\)]+")
HREF_RE = re.compile(r"href=[\"']([^\"']+)[\"']", re.IGNORECASE)
LOCAL_RESEARCH_RE = re.compile(r"^\s*image:\s*(/assets/images/research/[^\s#]+)\s*$")
HTTP_TIMEOUT = 45


@dataclass
class DataImage:
    source_url: str
    normalized_url: str
    data_file: Path
    line_number: int
    label: str
    category: str


def normalize_text(value: str) -> str:
    value = html.unescape(value)
    value = value.replace("\\/", "/")
    value = value.replace("\\u003d", "=").replace("\\u003D", "=")
    value = value.replace("%3D", "=").replace("%3d", "=")
    return value


def normalize_url(value: str) -> str:
    value = normalize_text(value).strip()
    return value.rstrip(".,;]")


def extract_image_urls(text: str) -> list[str]:
    normalized = normalize_text(text)
    urls: list[str] = []
    seen: set[str] = set()
    for match in IMAGE_URL_RE.finditer(normalized):
        url = normalize_url(match.group(0))
        if url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def slugify(value: str, fallback: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"<[^>]+>", "", value)
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    value = re.sub(r"-{2,}", "-", value)
    if not value:
        value = fallback
    return value[:70].strip("-") or fallback


def yaml_value(line: str) -> str:
    value = line.split(":", 1)[1].strip()
    if value in {"|-", ">-", "|", ">"}:
        return ""
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        value = value[1:-1]
    return value.strip()


def nearest_label(lines: list[str], index: int) -> str:
    for cursor in range(index, max(-1, index - 35), -1):
        line = lines[cursor]
        match = re.match(r"^\s*-\s*(name|title):\s*(.+?)\s*$", line)
        if match:
            return yaml_value(line.replace(f"- {match.group(1)}:", f"{match.group(1)}:", 1))
        match = re.match(r"^\s*(name|title):\s*(.+?)\s*$", line)
        if match:
            return yaml_value(line)
    return "google-sites-image"


def category_for(path: Path) -> str:
    if path.name == "members.yml":
        return "members"
    if path.name == "news.yml":
        return "news"
    if path.name == "research.yml":
        return "research"
    if path.name == "lab.yml":
        return "logos"
    return "imported/google-sites"


def discover_data_images() -> list[DataImage]:
    images: list[DataImage] = []
    seen: set[tuple[Path, str]] = set()
    for path in DATA_FILES:
        if not path.exists():
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        for index, line in enumerate(lines):
            for source_url in extract_image_urls(line):
                key = (path, source_url)
                if key in seen:
                    continue
                seen.add(key)
                images.append(
                    DataImage(
                        source_url=source_url,
                        normalized_url=normalize_url(source_url),
                        data_file=path,
                        line_number=index + 1,
                        label=nearest_label(lines, index),
                        category=category_for(path),
                    )
                )
    return images


def fetch_bytes(url: str) -> tuple[bytes, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "MS3L asset importer/1.0 (+https://github.com/enthusiast87/MS3L.io)",
            "Accept": "image/avif,image/webp,image/png,image/jpeg,image/*,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(request, timeout=HTTP_TIMEOUT) as response:
        return response.read(), response.headers.get("Content-Type", "").split(";", 1)[0]


def extension_for(content_type: str, url: str, fallback: str = ".jpg") -> str:
    suffix = Path(urllib.parse.urlparse(url).path).suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"}:
        return ".jpg" if suffix == ".jpeg" else suffix
    guessed = mimetypes.guess_extension(content_type or "")
    if guessed == ".jpe":
        return ".jpg"
    if guessed in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"}:
        return ".jpg" if guessed == ".jpeg" else guessed
    return fallback


def local_rel(path: Path) -> str:
    return "/" + path.relative_to(ROOT).as_posix()


def unique_path(base: Path, ext: str, force: bool) -> Path:
    return base.with_suffix(ext)


def download_image(url: str, base_path: Path, force: bool = False) -> dict[str, str]:
    payload, content_type = fetch_bytes(url)
    ext = extension_for(content_type, url)
    target = unique_path(base_path, ext, force)
    target.parent.mkdir(parents=True, exist_ok=True)
    if force or not target.exists():
        target.write_bytes(payload)
        status = "downloaded"
    else:
        status = "existing"
    return {
        "source_url": url,
        "local_path": local_rel(target),
        "content_type": content_type,
        "bytes": str(len(payload)),
        "status": status,
    }


def download_image_to(url: str, target: Path, force: bool = False) -> dict[str, str]:
    payload, content_type = fetch_bytes(url)
    target.parent.mkdir(parents=True, exist_ok=True)
    if force or not target.exists():
        target.write_bytes(payload)
        status = "downloaded"
    else:
        status = "existing"
    return {
        "source_url": url,
        "local_path": local_rel(target),
        "content_type": content_type,
        "bytes": str(len(payload)),
        "status": status,
    }


def crawl_site(start_url: str, max_pages: int) -> tuple[list[str], list[str]]:
    queue = [start_url]
    seen_pages: set[str] = set()
    images: list[str] = []
    seen_images: set[str] = set()

    while queue and len(seen_pages) < max_pages:
        url = queue.pop(0)
        if url in seen_pages:
            continue
        seen_pages.add(url)
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "MS3L asset importer/1.0"})
            with urllib.request.urlopen(request, timeout=HTTP_TIMEOUT) as response:
                raw = response.read()
        except Exception as exc:  # noqa: BLE001 - network crawls should be best effort.
            print(f"Warning: could not fetch {url}: {exc}", file=sys.stderr)
            continue

        text = raw.decode("utf-8", errors="replace")
        for image_url in extract_image_urls(text):
            if image_url not in seen_images:
                seen_images.add(image_url)
                images.append(image_url)

        normalized = normalize_text(text)
        for href in HREF_RE.findall(normalized):
            absolute = urllib.parse.urljoin(url, href).split("#", 1)[0]
            absolute = absolute.split("?", 1)[0]
            if absolute.startswith(SITE_PREFIX) and absolute not in seen_pages and absolute not in queue:
                queue.append(absolute)

    return list(seen_pages), images


def missing_research_assets() -> list[str]:
    path = ROOT / "_data" / "research.yml"
    if not path.exists():
        return []
    missing: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = LOCAL_RESEARCH_RE.match(line)
        if not match:
            continue
        rel = match.group(1)
        target = ROOT / rel.lstrip("/")
        if not target.exists():
            missing.append(rel)
    return missing


def write_manifest(manifest: dict[str, object]) -> Path:
    target = ROOT / "assets" / "images" / "imported" / "google-sites" / "manifest.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return target


def replace_data_urls(
    replacements: dict[Path, dict[str, str]], mode: str
) -> list[dict[str, str]]:
    writes: list[dict[str, str]] = []
    for path, path_replacements in replacements.items():
        original = path.read_text(encoding="utf-8")
        updated = original
        for source, local in path_replacements.items():
            variants = {
                source,
                normalize_url(source),
                source.replace("=", "%3D"),
                source.replace("=", "%3d"),
                normalize_url(source).replace("=", "%3D"),
                normalize_url(source).replace("=", "%3d"),
            }
            for variant in variants:
                updated = updated.replace(variant, local)
        if updated == original:
            continue
        if mode == "apply":
            target = path
        elif mode == "draft":
            target = path.with_name(path.name + ".asset-import-draft")
        else:
            target = path.with_name(path.name + ".dry-run")
        if mode in {"apply", "draft"}:
            target.write_text(updated, encoding="utf-8")
        writes.append({"source": str(path.relative_to(ROOT)), "target": str(target.relative_to(ROOT))})
    return writes


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-url", default=DEFAULT_SITE_URL, help="Google Sites page to crawl.")
    parser.add_argument("--max-pages", type=int, default=40, help="Maximum Google Sites pages to crawl.")
    parser.add_argument("--no-crawl", action="store_true", help="Only migrate URLs already in _data.")
    parser.add_argument("--draft", action="store_true", help="Write draft YAML files instead of editing source data.")
    parser.add_argument("--apply", action="store_true", help="Update source data files in place.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing local image files.")
    parser.add_argument(
        "--save-unassigned",
        action="store_true",
        help="Download crawled images that are not mapped to current data fields.",
    )
    return parser


def main() -> int:
    args = build_arg_parser().parse_args()
    if args.apply and args.draft:
        print("Choose either --apply or --draft, not both.", file=sys.stderr)
        return 2

    mode = "apply" if args.apply else "draft" if args.draft else "dry-run"
    should_download = mode in {"apply", "draft"}

    data_images = discover_data_images()
    data_normalized = {item.normalized_url for item in data_images}
    pages: list[str] = []
    crawled_images: list[str] = []
    if not args.no_crawl:
        pages, crawled_images = crawl_site(args.site_url, args.max_pages)

    manifest: dict[str, object] = {
        "site_url": args.site_url,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "mode": mode,
        "pages": pages,
        "data_images": [],
        "research_images": [],
        "unassigned_site_images": [],
        "data_writes": [],
    }

    replacements: dict[Path, dict[str, str]] = {}
    failures: list[dict[str, str]] = []

    for item in data_images:
        digest = hashlib.sha1(item.normalized_url.encode("utf-8")).hexdigest()[:8]
        slug = slugify(item.label, f"image-{digest}")
        base_path = ROOT / "assets" / "images" / item.category / slug
        try:
            if should_download:
                record = download_image(item.normalized_url, base_path, args.force)
            else:
                record = {
                    "source_url": item.normalized_url,
                    "local_path": f"/assets/images/{item.category}/{slug}.jpg",
                    "status": "planned",
                }
            replacements.setdefault(item.data_file, {})[item.source_url] = record["local_path"]
            manifest["data_images"].append(
                {
                    **record,
                    "data_file": str(item.data_file.relative_to(ROOT)),
                    "line": str(item.line_number),
                    "label": item.label,
                }
            )
        except Exception as exc:  # noqa: BLE001 - script should report and continue.
            failures.append({"source_url": item.normalized_url, "error": str(exc)})

    missing_research = missing_research_assets()
    research_candidates = [url for url in crawled_images if normalize_url(url) not in data_normalized]
    for rel, image_url in zip(missing_research, research_candidates):
        try:
            target = ROOT / rel.lstrip("/")
            if should_download:
                record = download_image_to(normalize_url(image_url), target, args.force)
            else:
                record = {
                    "source_url": normalize_url(image_url),
                    "local_path": rel,
                    "status": "planned",
                }
            manifest["research_images"].append(record)
        except Exception as exc:  # noqa: BLE001
            failures.append({"source_url": normalize_url(image_url), "error": str(exc), "target": rel})

    assigned_research = {entry["source_url"] for entry in manifest["research_images"]}
    unassigned_images = [
        normalize_url(url)
        for url in research_candidates[len(missing_research) :]
        if normalize_url(url) not in assigned_research
    ]
    manifest["unassigned_site_image_count"] = len(unassigned_images)
    if args.save_unassigned:
        for index, image_url in enumerate(unassigned_images, start=1):
            digest = hashlib.sha1(image_url.encode("utf-8")).hexdigest()[:8]
            base_path = ROOT / "assets" / "images" / "imported" / "google-sites" / f"unassigned-{index:03d}-{digest}"
            try:
                if should_download:
                    record = download_image(image_url, base_path, args.force)
                else:
                    record = {
                        "source_url": image_url,
                        "local_path": f"/assets/images/imported/google-sites/{base_path.name}",
                        "status": "planned",
                    }
                manifest["unassigned_site_images"].append(record)
            except Exception as exc:  # noqa: BLE001
                failures.append({"source_url": image_url, "error": str(exc)})

    manifest["data_writes"] = replace_data_urls(replacements, mode)
    if failures:
        manifest["failures"] = failures

    if should_download:
        manifest_path = write_manifest(manifest)
        print(f"Wrote manifest: {manifest_path.relative_to(ROOT)}")

    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
