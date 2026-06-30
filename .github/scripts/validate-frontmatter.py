#!/usr/bin/env python3
"""
Validate the frontmatter of every Markdown file in an A&C repo against the shared JSON Schema
contract — the single source of truth in `.github/schemas/`. See `.github/schemas/README.md`
and ADR-002 (corporate-website, decision D4).

The schema is selected by path so the same tool validates both generic docs and the publishable
content types:

    .../case-studies/...  -> case-study.schema.json   (base + display metadata)
    .../go-to-market/...  -> core-offer.schema.json    (base + display metadata)
    everything else       -> frontmatter.schema.json   (the universal 6-field base)

Skips files: README.md, CONTRIBUTING.md, adr-template.md.
Skips dirs:  .github, _archived, .git, node_modules, dist, .astro, _content.

Schema directory resolution (first match wins):
    1. --schema-dir CLI argument          (CI passes this explicitly)
    2. $AC_SCHEMA_DIR environment variable
    3. <.github repo>/schemas, derived from this script's location (local/in-repo runs)

Requires: pyyaml, jsonschema.
"""

import argparse
import json
import os
import sys
from pathlib import Path

import yaml

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    sys.stderr.write("ERROR: the 'jsonschema' package is required (pip install jsonschema).\n")
    sys.exit(2)

# Emoji output (✅ / ❌) must not crash on non-UTF-8 consoles (e.g. Windows cp1252).
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SKIP_FILES = {"README.md", "CONTRIBUTING.md", "adr-template.md"}
SKIP_DIRS = {".github", "_archived", ".git", "node_modules", "dist", ".astro", "_content"}

BASE_SCHEMA = "frontmatter.schema.json"
CASE_STUDY_SCHEMA = "case-study.schema.json"
CORE_OFFER_SCHEMA = "core-offer.schema.json"


def resolve_schema_dir(cli_dir):
    if cli_dir:
        return Path(cli_dir)
    env = os.environ.get("AC_SCHEMA_DIR")
    if env:
        return Path(env)
    # .github/.github/scripts/validate-frontmatter.py -> .github/schemas
    return Path(__file__).resolve().parents[2] / "schemas"


def load_validators(schema_dir):
    validators = {}
    for key, fname in (("base", BASE_SCHEMA), ("case", CASE_STUDY_SCHEMA), ("offer", CORE_OFFER_SCHEMA)):
        path = schema_dir / fname
        if not path.exists():
            sys.stderr.write(f"ERROR: schema not found: {path}\n")
            sys.exit(2)
        with open(path, encoding="utf-8") as fh:
            validators[key] = Draft202012Validator(json.load(fh), format_checker=FormatChecker())
    return validators


def schema_key_for(filepath):
    parts = Path(filepath).parts
    if "case-studies" in parts:
        return "case"
    if "go-to-market" in parts:
        return "offer"
    return "base"


def check_file(filepath, validators, errors):
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

    validator = validators[schema_key_for(filepath)]
    for verr in sorted(validator.iter_errors(fm), key=lambda e: list(e.path)):
        loc = ".".join(str(p) for p in verr.path) or "(root)"
        errors.append(f"[SCHEMA] {filepath} :: {loc}: {verr.message}")


def main():
    parser = argparse.ArgumentParser(
        description="Validate A&C Markdown frontmatter against the shared JSON Schema contract."
    )
    parser.add_argument("--schema-dir", help="Directory containing the frontmatter JSON Schemas.")
    parser.add_argument("root", nargs="?", default=".", help="Root directory to scan (default: cwd).")
    args = parser.parse_args()

    schema_dir = resolve_schema_dir(args.schema_dir)
    validators = load_validators(schema_dir)

    errors = []
    for root, dirs, files in os.walk(args.root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for filename in files:
            if filename in SKIP_FILES or not filename.endswith(".md"):
                continue
            check_file(os.path.join(root, filename), validators, errors)

    if errors:
        print(f"\n❌ Frontmatter validation failed with {len(errors)} error(s):\n")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)
    print(f"✅ All frontmatter validated against the schema contract in {schema_dir}.")


if __name__ == "__main__":
    main()
