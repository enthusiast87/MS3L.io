"""Report class selectors in style.css that no template can produce.

    python scripts/find_dead_css.py

Reports only. Deleting is a separate, deliberate act - see the note in
docs/content-guide.md for why, and for the check to run afterwards.

A rule survives a redesign that removed its markup without complaining, so the
stylesheet accumulates selectors that cannot match anything. This walks the
stylesheet with a real parser rather than regex over the text, because comments
in this file contain braces and selector-like fragments and a hand-rolled
scanner reads them as rules.
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

try:
    import tinycss2
except ImportError:
    sys.exit("needs tinycss2:  pip install tinycss2")


def names_templates_can_emit():
    """Every class a template, an include, a data file or the layout's JS sets."""
    sources = (glob.glob("*.md") + glob.glob("_layouts/*.html")
               + glob.glob("_includes/*.html") + glob.glob("_data/*.yml"))
    text = "\n".join(io.open(f, encoding="utf-8").read() for f in sources)
    names = set()
    for attr in re.findall(r'class\s*=\s*"([^"]*)"', text):
        names.update(re.findall(r"[a-zA-Z][\w-]*", attr))
    # classes the layout adds at runtime never appear in a class attribute
    for call in re.findall(r"classList\.(?:add|remove|contains|toggle)\(([^)]*)\)", text):
        names.update(re.findall(r"['\"]([\w-]+)['\"]", call))
    for call in re.findall(r"querySelector(?:All)?\(([^)]*)\)", text):
        names.update(re.findall(r"\.([\w-]+)", call))
    return names


def selector_can_match(selector, live):
    # a class inside :not() does not decide whether the selector matches
    outside = re.sub(r":not\([^)]*\)", "", selector)
    classes = re.findall(r"\.([\w-]+)", outside)
    return not classes or all(name in live for name in classes)


def walk(nodes, live, dead, depth=0):
    for node in nodes:
        if node.type == "qualified-rule":
            selectors, current = [], []
            for token in node.prelude:
                if token.type == "literal" and token.value == ",":
                    selectors.append(current); current = []
                else:
                    current.append(token)
            selectors.append(current)
            for sel in selectors:
                text = tinycss2.serialize(sel).strip()
                if text and not selector_can_match(text, live):
                    dead.append(text)
        elif node.type == "at-rule" and node.content is not None:
            walk(tinycss2.parse_rule_list(node.content, skip_comments=False,
                                          skip_whitespace=False), live, dead, depth + 1)


def main():
    css = io.open("assets/css/style.css", encoding="utf-8").read()
    live = names_templates_can_emit()
    dead = []
    walk(tinycss2.parse_stylesheet(css, skip_comments=False, skip_whitespace=False), live, dead)
    if not dead:
        print("No unreachable class selectors.")
        return
    print("%d selectors no template can produce:\n" % len(dead))
    for sel in sorted(set(dead)):
        print("   ", sel)
    print("\nBefore deleting any of these, read the warning in docs/content-guide.md.")


if __name__ == "__main__":
    main()
