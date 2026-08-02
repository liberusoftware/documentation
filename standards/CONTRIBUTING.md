# Contributing

Liberu documentation and code changes should be small, reviewable, evidence-based, and safe to operate. Read [DOCUMENTATION.md](DOCUMENTATION.md), [MODULES.md](../architecture/MODULES.md), [TESTING.md](TESTING.md), and [SECURITY.md](../architecture/SECURITY.md) before starting.

## Before you change anything

- Search for the existing source of truth and link to it instead of duplicating it.
- Identify the intended reader, outcome, owner, compatibility impact, and security/privacy implications.
- Check the current branch, worktree, and related issues. Preserve unrelated user changes.
- For dependency or framework claims, verify the repository lock/manifest and current upstream documentation.

## Engineering standards

- Target PHP 8.5 and Laravel 13 unless a document explicitly defines another compatibility range.
- Follow PSR-12 and PSR-4, Laravel conventions, strict typing where compatible, typed signatures, dependency injection, small actions, and explicit contracts.
- Keep domain modules independent, presentation packages one-to-one, and cross-module integration contract/event based.
- Authorize every boundary server-side; validate untrusted input; use least privilege; redact sensitive data.
- Make writes transactional, queued work idempotent, events observable, and migrations reversible or accompanied by a documented recovery path.
- Keep examples minimal, runnable, current, and free of real credentials or personal data.

## Documentation standards

- Use one H1, sentence-case headings, descriptive links, fenced code labels, relative internal links, and stable external URLs.
- State requirements with **must**, recommendations with **should**, and options with **may**.
- Document prerequisites, verification, failure recovery, limitations, security, compatibility, and upgrade impact where relevant.
- Add a new document to the nearest index and update inbound links when renaming or replacing a page.
- Do not claim support, coverage, security, or deployment capability without current evidence.

## Workflow

1. Create a focused branch from `main`.
2. Make the smallest complete change and update the owning documentation/index.
3. Run Markdown link checks, formatting/linting, tests, static analysis, architecture checks, and security checks appropriate to the change.
4. Review the rendered Markdown, code examples, anchors, tables, and sensitive-data handling.
5. Open a pull request describing the outcome, compatibility, verification, migration/rollback, and security impact.
6. Respond to review with amended commits; do not rewrite shared history without agreement.

## Commit and review expectations

Use clear imperative commit subjects, keep each commit coherent, and do not mix generated output or unrelated formatting. A pull request must identify changed public contracts and include tests or explain why tests are not applicable. Maintainers may request an ADR for architecture, dependency, security, or deployment decisions.

## Reporting problems

Use a public issue for ordinary bugs, documentation errors, and feature proposals. Follow [SECURITY.md](../architecture/SECURITY.md) for vulnerabilities; do not publish exploitable details publicly.
