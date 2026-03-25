import json
import sys
from pathlib import Path
import requests
import difflib

ROOT = Path(__file__).resolve().parents[1]
OLLAMA_URL = "http://localhost:11434/api/chat"

ALLOWED_FILES = [
    "index.md",
    "introduction.md",
    "research.md",
    "members.md",
    "projects.md",
    "publications.md",
    "patents.md",
    "news.md",
    "contacts.md",
    "_data/lab.yml",
    "_data/research.yml",
    "_data/members.yml",
    "_data/publications.yml",
    "_data/news.yml",
    "_data/patents.yml",
]

PLANNER_MODEL = "qwen3:4b"
WRITER_MODEL = "qwen2.5-coder:3b"


def read_text(path_str):
    path = ROOT / path_str
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def ollama_chat(model, messages, schema):
    payload = {
        "model": model,
        "messages": messages,
        "format": schema,
        "stream": False,
        "options": {
            "temperature": 0.2
        }
    }
    r = requests.post(OLLAMA_URL, json=payload, timeout=300)
    r.raise_for_status()
    data = r.json()
    return json.loads(data["message"]["content"])


def plan_task(task):
    planner_schema = {
        "type": "object",
        "properties": {
            "target_files": {
                "type": "array",
                "items": {"type": "string"}
            },
            "reason": {"type": "string"}
        },
        "required": ["target_files", "reason"]
    }

    messages = [
        {
            "role": "system",
            "content": (
                "You are the planner for a lab website update workflow. "
                "Choose the minimum editable files needed. "
                "Only use allowed files."
            )
        },
        {
            "role": "user",
            "content": (
                f"Task:\n{task}\n\n"
                f"Allowed files:\n" + "\n".join(ALLOWED_FILES)
            )
        }
    ]
    result = ollama_chat(PLANNER_MODEL, messages, planner_schema)
    return [f for f in result["target_files"] if f in ALLOWED_FILES]


def write_file(task, relpath):
    old_content = read_text(relpath)

    writer_schema = {
        "type": "object",
        "properties": {
            "content": {"type": "string"}
        },
        "required": ["content"]
    }

    messages = [
        {
            "role": "system",
            "content": (
                "You edit exactly one website source file. "
                "Return the full updated file content. "
                "Keep syntax valid. Do not invent facts."
            )
        },
        {
            "role": "user",
            "content": (
                f"Task:\n{task}\n\n"
                f"Target file:\n{relpath}\n\n"
                f"Current content:\n```text\n{old_content}\n```"
            )
        }
    ]

    result = ollama_chat(WRITER_MODEL, messages, writer_schema)
    new_content = result["content"]

    draft_path = ROOT / (relpath + ".draft")
    draft_path.parent.mkdir(parents=True, exist_ok=True)
    draft_path.write_text(new_content, encoding="utf-8")

    diff = difflib.unified_diff(
        old_content.splitlines(),
        new_content.splitlines(),
        fromfile=relpath,
        tofile=relpath + ".draft",
        lineterm=""
    )
    print("\n".join(diff))


def main():
    if len(sys.argv) < 2:
        print('Usage: python scripts/update_site.py "your task"')
        sys.exit(1)

    task = sys.argv[1]
    targets = plan_task(task)

    if not targets:
        print("No safe target files selected.")
        sys.exit(1)

    print("Planned files:")
    for t in targets:
        print("-", t)

    for t in targets:
        print(f"\n=== Writing draft for {t} ===")
        write_file(task, t)

    print("\nDraft files created. Review *.draft before applying.")


if __name__ == "__main__":
    main()
