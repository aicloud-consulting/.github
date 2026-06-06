# Contributing to A&C Projects

Thank you for your interest in contributing to **A&C** repositories!

Our working philosophy is built on **zero improvisation** and flawless technical execution. To maintain our high standards of architectural quality (MACH, API-first, Cloud-native) and security (DevSecOps), please follow these guidelines when contributing to any project in the organization.

## 1. Architecture Philosophy (Zero Technical Debt)

All contributed code must align with our **Enterprise Standards** principles:
- **Agnostic and Modular**: We prioritize microservices-based architecture and scalable solutions.
- **Predictable Quality**: Every change must be backed by automated unit/integration tests. We do not consider work "Done" (Definition of Done) until it passes validation and security thresholds.
- **Efficiency**: At A&C we treat time as a critical variable. Avoid "temporary" solutions that increase technical debt.

## 2. Contribution Process (A&C Agile Delivery Framework)

1. **Issues First**: Before creating a large Pull Request (PR), open an Issue to discuss the architecture and approach of the change.
2. **Branching Model**: We use a standardized strategy.
   - `feature/feature-name` for new development.
   - `bugfix/bug-description` for bug fixes.
   - `hotfix/critical-incident` for urgent production patches.
3. **Semantic Commits**: Commit messages must be descriptive (e.g. `feat: add AI governance module`, `fix: resolve auth race condition`).
4. **Peer Review**: Every PR must be reviewed and approved by at least one architect or technical lead of the repository before being merged.

## 3. Security by Design (DevSecOps)

- **Zero Credentials**: NEVER commit passwords, secrets, tokens, or API keys to source code.
- **AI Governance**: If your contribution involves the use of Artificial Intelligence models or automated prompts, ensure compliance with A&C's *Master Information Security Policy (PMSI)*.
- **Vulnerability Analysis**: Code will be evaluated by our automated CI/CD tools. Ensure you fix any security findings (SAST/DAST) before requesting review.

## 4. Deliverable Structure (The Rule of 3)

Our technical communication is direct, free of visual noise, and highly executive. When documenting PRs or Issues:
1. **The Context**: What problem is being solved?
2. **The Solution**: How was it technically addressed?
3. **The Impact/Action**: What dependencies does it affect and how to validate it?

We deeply appreciate your hyper-specialized talent and your commitment to excellence!