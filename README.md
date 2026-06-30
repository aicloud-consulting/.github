# A&C Consulting Services — Organizational Governance Repository

This repository contains the policies, templates, and standards that apply to **all repositories** within the `aicloud-consulting` organization.

## Contents

| Artefact | Description |
|---|---|
| `CODEOWNERS` | Code ownership: all changes require review by a repository Owner |
| `CONTRIBUTING.md` | Contribution guide: philosophy, branching model, DevSecOps, and Rule of 3 |
| `profile/README.md` | Public profile of the GitHub organization |
| `.github/ISSUE_TEMPLATE/` | Issue templates: new doc, update, deprecation, evidence |
| `.github/pull_request_template.md` | Mandatory checklist for all Pull Requests |
| `.github/workflows/docs-quality.yml` | CI: markdownlint + link-check + frontmatter validation |
| `.github/scripts/validate-frontmatter.py` | Frontmatter validator invoked by the CI workflow |
| `docs/dac-standards.md` | DaC standards: frontmatter contract, language policy, and quality gate |
| `.markdownlint.yml` | Markdownlint rules configuration for the entire org |

## Organization Repositories

A&C Consulting Services maintains strict access controls. The `core-*` repositories are private and restricted to authorized personnel only.

| Repo | Visibility | Purpose |
|---|---|---|
| [`.github`](https://github.com/aicloud-consulting/.github) | Public | Organizational governance (this repository) |
| [`core-corporate-governance`](https://github.com/aicloud-consulting/core-corporate-governance) | Private | Legal, governance, policies, and contracts |
| [`core-architecture-landscape`](https://github.com/aicloud-consulting/core-architecture-landscape) | Private | Reference architectures, integration patterns, and runbooks |
| [`core-design-system`](https://github.com/aicloud-consulting/core-design-system) | Private | Brand identity, design tokens, and verbal identity |
| [`core-developer-portal`](https://github.com/aicloud-consulting/core-developer-portal) | Private | ADF methodology, Core Offers, case studies, and onboarding |

## Project Context

Docs-as-Code conventions (frontmatter contract, language policy) and the documentation quality gate are defined in [`docs/dac-standards.md`](./docs/dac-standards.md).
