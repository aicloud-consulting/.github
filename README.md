# A&C Consulting Services — Organizational Governance

The org-wide source of truth for Docs-as-Code: the policies, templates, schemas, and CI that apply to **every repository** in `aicloud-consulting`.

> **Visibility:** Public · **Language:** en-US · **Owner:** @personal-abrahamchavez
>
> **Brand architecture — Group / Member.** **A&C Consulting Services** is the **group** (legal entity / holding); its public-facing commercial brand is **Ficentia** (ficentia.com) under an endorsed model (*"Ficentia, a brand of A&C Consulting Services"*). Brand specs live in [`core-design-system`](https://github.com/aicloud-consulting/core-design-system).

## What's here

| Item | Description |
|---|---|
| `CODEOWNERS` | Code ownership: every change requires review by a repository Owner |
| `CONTRIBUTING.md` | Contribution guide: zero-improvisation philosophy, branching model, DevSecOps, and the Rule of 3 |
| `.markdownlint.yml` | Org-wide markdownlint rule configuration (the single linter ruleset) |
| `profile/README.md` | Public GitHub organization profile (mission, vision, approach, contact) |
| `docs/dac-standards.md` | The Docs-as-Code standards: frontmatter contract, language policy, and quality gate |
| `schemas/frontmatter.schema.json` | Universal base frontmatter contract — applies to every A&C Markdown document |
| `schemas/case-study.schema.json` | Path-selected extension for `core-developer-portal/case-studies/` |
| `schemas/core-offer.schema.json` | Path-selected extension for `core-developer-portal/go-to-market/` |
| `schemas/README.md` | How the schemas compose, per-path selection, and their consumers |
| `.github/ISSUE_TEMPLATE/` | Issue templates: new doc, update doc, deprecation, case-study/evidence request |
| `.github/pull_request_template.md` | Mandatory PR checklist (change type + Context / Solution / Impact) |
| `.github/workflows/docs-quality.yml` | Reusable CI quality gate: markdownlint + link-check + frontmatter validation |
| `.github/scripts/validate-frontmatter.py` | Frontmatter validator invoked by the CI workflow |

## Where else to look

A&C Consulting Services maintains strict access controls. The `core-*` repositories are private and restricted to authorized personnel only. This repo defines the rules; the content lives elsewhere — check the right repo before reinventing it.

| Repo | Visibility | What it holds |
|---|---|---|
| [`core-design-system`](https://github.com/aicloud-consulting/core-design-system) | Private | Brand: mission, vision, tagline, story, tone of voice + vocabulary, design tokens, logo assets |
| [`core-developer-portal`](https://github.com/aicloud-consulting/core-developer-portal) | Private | Services (7 Core Offers), 14 case studies, ADF delivery methodology, engineering standards, onboarding |
| [`core-corporate-governance`](https://github.com/aicloud-consulting/core-corporate-governance) | Private | Legal/corporate: bylaws, term-sheet/governance, pricing & engagement models, SLAs, PMSI, BCP/DRP, MNDA/SOW, risk register |
| [`core-architecture-landscape`](https://github.com/aicloud-consulting/core-architecture-landscape) | Private | Architecture: technical principles, reference architectures, integration patterns, runbooks, ADR standard + org register |
| [`corporate-website`](https://github.com/aicloud-consulting/corporate-website) | Private | The public website (Astro presentation layer) |

## Conventions

This repo defines the org Docs-as-Code standards in [`docs/dac-standards.md`](./docs/dac-standards.md):

- **Frontmatter contract.** Every content `.md` carries `title`, `status`, `owner`, `last_review`, `source_doc`, and `lang`. There is **no `version` field — Git history is the version record**, and `_vN` filename suffixes are not used. READMEs, `CONTRIBUTING.md`, issue/PR templates, and `adr-template.md` are exempt.
- **Language policy.** Language is assigned per repo/section (technical → en-US; Mexican-legal → es-MX; commercial-for-both-markets → bilingual). This repo is en-US.
- **Quality gate.** A single reusable workflow (`.github/workflows/docs-quality.yml`) runs markdownlint, link-check, and frontmatter validation; every repo carries a thin caller that invokes it.

The three JSON Schemas in [`schemas/`](./schemas/) are the **single source of truth** for frontmatter validation — consumed mechanically by the CI validator and by the `corporate-website` build. Nobody re-types the field rules.
