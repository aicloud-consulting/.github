#!/usr/bin/env python3
"""
Validates that all Markdown files in core-* repos have the required DaC frontmatter fields.
Required fields: title, version, status, owner, last_review, source_doc, lang
Skips files: README.md, CONTRIBUTING.md, adr-template.md.
Skips dirs: .github/, _archived/, .git/, node_modules/, dist/, .astro/, _content/.
"""

import os
import sys
import yaml

# Emoji output (✅ / ❌) must not crash on non-UTF-8 consoles (e.g. Windows cp1252).
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REQUIRED_FIELDS = ["title", "version", "status", "owner", "last_review", "source_doc", "lang"]
# Union of the content lifecycle (draft/approved/superseded/archived) and the
# ADR lifecycle (proposed/approved/superseded/deprecated). See the A&C ADR Standard in
# core-architecture-landscape/decision-records/README.md.
VALID_STATUSES = {"draft", "proposed", "approved", "superseded", "deprecated", "archived"}
VALID_LANGS = {"es-MX", "en-US"}

# README.md and CONTRIBUTING.md are org/process docs; adr-template.md is a template
# whose frontmatter is illustrative (placeholder dates), so it is exempt from validation.
SKIP_FILES = {"README.md", "CONTRIBUTING.md", "adr-template.md"}
# Skip infra/governance dirs, plus dependency/build output (node_modules, dist, .astro)
# so the validator never walks third-party or generated files.
SKIP_DIRS = {".github", "_archived", ".git", "node_modules", "dist", ".astro", "_content"}

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
