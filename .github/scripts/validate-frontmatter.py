#!/usr/bin/env python3
"""
Validates that all Markdown files in core-* repos have the required DaC frontmatter fields.
Required fields: title, version, status, owner, last_review, source_doc, lang
Skips: README.md, files in .github/, _archived/
"""

import os
import sys
import yaml

REQUIRED_FIELDS = ["title", "version", "status", "owner", "last_review", "source_doc", "lang"]
VALID_STATUSES = {"draft", "approved", "superseded", "archived"}
VALID_LANGS = {"es-MX", "en-US"}

SKIP_FILES = {"README.md", "CONTRIBUTING.md"}
SKIP_DIRS = {".github", "_archived", ".git"}

errors = []

def check_file(filepath):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        errors.append(f"[MISSING FRONTMATTER] {filepath}")
        return

    try:
        end = content.index("---", 3)
        fm = yaml.safe_load(content[3:end])
    except Exception as e:
        errors.append(f"[INVALID FRONTMATTER YAML] {filepath}: {e}")
        return

    if not isinstance(fm, dict):
        errors.append(f"[EMPTY FRONTMATTER] {filepath}")
        return

    for field in REQUIRED_FIELDS:
        if field not in fm or fm[field] in (None, ""):
            errors.append(f"[MISSING FIELD '{field}'] {filepath}")

    if "status" in fm and fm["status"] not in VALID_STATUSES:
        errors.append(f"[INVALID STATUS '{fm['status']}'] {filepath} — must be one of {VALID_STATUSES}")

    if "lang" in fm and fm["lang"] not in VALID_LANGS:
        errors.append(f"[INVALID LANG '{fm['lang']}'] {filepath} — must be one of {VALID_LANGS}")

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for filename in files:
        if filename in SKIP_FILES:
            continue
        if not filename.endswith(".md"):
            continue
        filepath = os.path.join(root, filename)
        check_file(filepath)

if errors:
    print(f"\n❌ Frontmatter validation failed with {len(errors)} error(s):\n")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)
else:
    print("✅ All frontmatter fields validated successfully.")
