---
title: "A&C Docs-as-Code Standards"
status: "approved"
owner: "personal-abrahamchavez"
last_review: "2026-06-30"
source_doc: "Organization governance (born-digital)"
lang: "en-US"
---

# A&C Docs-as-Code Standards

The public, org-wide reference for how documentation is authored and validated across every
repository in `aicloud-consulting`. It defines three things: the **frontmatter contract**, the
**language policy**, and the **documentation quality gate**. Anyone contributing to a `core-*`
repo, `.github`, or `corporate-website` is expected to follow this document.

---

## 1. Frontmatter Contract

Every content `.md` document must begin with a YAML frontmatter block containing **all** of:

```yaml
---
title: ""
status: "approved"        # draft | proposed | approved | superseded | deprecated | archived
owner: ""                 # GitHub login of the responsible owner
last_review: "YYYY-MM-DD"
source_doc: ""            # origin (Drive path for migrations, or born-digital provenance)
lang: "en-US"             # es-MX | en-US
---
```

- **Status vocabulary** is the union of the content lifecycle (`draft → approved → superseded → archived`) and the ADR lifecycle (`proposed → approved → superseded → deprecated`). See the [ADR Standard](https://github.com/aicloud-consulting/core-architecture-landscape/blob/main/decision-records/README.md) for which states apply to which artifact.
- **No `version` field.** Change history is Git's job — frontmatter does not carry a document version number. `status` (lifecycle) and `last_review` (freshness) are the only state fields.
- **Exempt** (no frontmatter required): `README.md`, `CONTRIBUTING.md`, issue/PR templates, and `adr-template.md`.
- A machine-readable **JSON Schema is the single source of truth**: `.github/schemas/` holds `frontmatter.schema.json` (base) plus `case-study.schema.json` and `core-offer.schema.json` (path-selected extensions). `validate-frontmatter.py` validates against them with the `jsonschema` library. See [ADR-002](https://github.com/aicloud-consulting/corporate-website/blob/main/docs/adr/ADR-002-Build-Deploy-Pipeline.md).

---

## 2. Language Policy

Derived from A&C's verbal-identity manual (Strategic Bilingualism). **Mandatory**, not a preference.

| Repo / Section | Language | Rationale |
|---|---|---|
| `core-corporate-governance` — all | **es-MX only** | Mexican law, STPS contracts, local regulatory context |
| `core-architecture-landscape` — all | **en-US only** | Technical artifacts must be strictly in English |
| `core-design-system` — all | **en-US only** | Design System = technical engineering artifact |
| `core-developer-portal` — `engineering-standards`, `ways-of-working`, `getting-started`, `founders-credentials` | **en-US only** | Technical engineering documentation |
| `core-developer-portal` — `go-to-market`, `case-studies` | **Bilingual** (es-MX + en-US) | Commercial artifacts targeting Mexican and international/nearshoring markets |
| `.github` — all | **en-US** | Technical org-governance repository |
| `corporate-website` — all | **en-US** | Technical presentation layer (content is sourced bilingually at build time) |

> **Documented exceptions:** a repo's commercial/Procurement artifacts may be bilingual even inside an es-MX repo (e.g., `core-corporate-governance/procurement/narrativa-financiera-enterprise`). When in doubt: *technical → English; legal/Mexican-market → Spanish; commercial-for-both-markets → bilingual.*

---

## 3. Documentation Quality Gate

Three automated checks guard documentation quality. They run in CI (`docs-quality.yml`) and can be run locally before opening a PR.

| Check | Tool | What it validates |
|---|---|---|
| Markdown lint | `markdownlint-cli2` + `.markdownlint.yml` | Markdown structure (headings, lists, fenced-code languages, tables) |
| Link check | `lychee` | Internal and external links resolve |
| Frontmatter | `.github/scripts/validate-frontmatter.py` | The frontmatter contract (§1): required fields, valid `status`, valid `lang` |

### Run locally

```bash
# Frontmatter (run from a repo root; requires: pip install pyyaml)
python /path/to/.github/scripts/validate-frontmatter.py

# Markdown lint (uses the org .markdownlint.yml)
npx -y markdownlint-cli2 --config /path/to/.github/.markdownlint.yml "**/*.md"
```

The frontmatter validator skips `README.md`, `CONTRIBUTING.md`, `adr-template.md`, and the `.github/`, `_archived/`, `.git/`, `node_modules/`, `dist/`, `.astro/`, `_content/` directories (the latter four are dependency/build output). Repos with build output (e.g. `corporate-website`) also carry a `.markdownlint-cli2.jsonc` whose `ignores` array keeps markdownlint from scanning those directories — no negation globs needed on the command line.

### CI enforcement

The gate is a **reusable workflow** in this repo (`.github/workflows/docs-quality.yml`, `on: workflow_call`); every repo carries a thin caller (`.github/workflows/docs-quality.yml`) that invokes it, so the three checks run on every push/PR. The shared rules and validator are fetched from this public repo at run time — one source of truth. On GitHub Free the checks **run and are visible but are non-blocking** on private repos (branch protection is unavailable); this is a deliberate, cost-justified decision recorded in [ADR-001 — CI Quality-Gate Enforcement](https://github.com/aicloud-consulting/core-architecture-landscape/blob/main/decision-records/ADR-001-CI-Quality-Gate-Enforcement.md).

> **Bootstrap order:** the callers reference `aicloud-consulting/.github/.github/workflows/docs-quality.yml@main`, so the **`.github` repo must be pushed/merged to `main` first**; until then, caller workflows fail with "workflow not found."
