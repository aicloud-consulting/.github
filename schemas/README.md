---
title: "Frontmatter Schemas — The Content Contract"
status: "approved"
owner: "personal-abrahamchavez"
last_review: "2026-06-30"
source_doc: "Implements ADR-001/ADR-002 (corporate-website) D4"
lang: "en-US"
---

# Frontmatter Schemas — The Content Contract

This directory holds the **single source of truth** for the frontmatter contract that binds
A&C's content (in `core-*` repos) to its consumers (the org CI validator and the
`corporate-website` build). It is the concrete realization of ADR-002, decision **D4**.

> **Principle:** the contract is defined **once**, here, and **mechanically consumed** by every
> party. Nobody re-types field rules. A breaking change is a single, versioned edit (bump the
> `$id` minor/major), never a divergent copy.

## Schemas

| File | `$id` | Applies to |
| :--- | :--- | :--- |
| `frontmatter.schema.json` | `…/frontmatter/1.0` | **Every** A&C Markdown document (the universal base — the required fields). |
| `case-study.schema.json` | `…/case-study/1.0` | Documents under `core-developer-portal/case-studies/`. Base + display metadata. |
| `core-offer.schema.json` | `…/core-offer/1.0` | Documents under `core-developer-portal/go-to-market/`. Base + display metadata. |

The specialized schemas are **self-contained** (they restate the base properties rather
than `$ref`-compose them). This is deliberate: `additionalProperties: false` does not compose
cleanly through `allOf`, and the self-contained form is what both the Python `jsonschema`
validator and the JSON-Schema→Zod generator handle without edge cases. The base field *rules*
(enums, patterns) are identical across files by contract; the **base schema is authoritative**
if they ever appear to differ.

## Per-path schema selection

The org validator (`.github/scripts/validate-frontmatter.py`) picks the schema by path:

```text
core-developer-portal/case-studies/**   -> case-study.schema.json
core-developer-portal/go-to-market/**   -> core-offer.schema.json
everything else                          -> frontmatter.schema.json (base)
```

## Consumers

1. **Org CI — `validate-frontmatter.py`** (runs in `docs-quality.yml` on every PR):
   validates each document against its path-selected schema using the `jsonschema` library.
   Invalid frontmatter fails the PR **before** merge.
2. **Website build — `corporate-website`** (after ADR-002 ratification): a `schema:gen` step
   derives Zod schemas from `case-study.schema.json` / `core-offer.schema.json` so Astro
   Content Collections validate the same contract at build time (fail-fast). A staleness check
   keeps the generated Zod and these JSON Schemas in lock-step.

## Status vocabulary

`status` is the **union** of the content lifecycle (`draft → approved → superseded → archived`)
and the ADR lifecycle (`proposed → approved → superseded → deprecated`), so one contract
validates both. See the
[A&C ADR Standard](https://github.com/aicloud-consulting/core-architecture-landscape/blob/main/decision-records/README.md)
for which states apply to which artifact, and `dac-standards.md` for the full frontmatter and
language policy.

## Versioning

The `$id` carries the version. Additive, backward-compatible changes (new **optional** field)
bump the **minor** (`/1.0` → `/1.1`). Any change that could invalidate existing content (new
required field, tighter rule, removed field) bumps the **major** (`/1.0` → `/2.0`) and is an
announced, coordinated change to this ADR and to all consumers.
