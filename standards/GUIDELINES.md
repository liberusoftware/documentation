# Liberu coding guidelines

These guidelines are the default for every application, module, package, theme, and presentation adapter. A local exception requires a documented reason, owner, tests, and an upgrade or removal condition.

Apply the [progressive delivery standard](ADOPTION.md): simplify infrastructure for personal or SME installations only when the same security, authorization, data ownership, recovery, and public-contract baseline remains intact.

## Before coding

- Identify the owning application, domain module, public contract, tenant boundary, and presentation adapter.
- Read the relevant [architecture decision](../architecture/README.md) or architecture document and the matching standard in this folder.
- Prefer an existing shared contract or service over introducing a parallel abstraction.

## During implementation

- Keep dependencies pointed inward toward stable contracts; domain code must not depend on UI frameworks.
- Use strict types, explicit names, constructor injection, immutable value objects where useful, and small focused classes.
- Validate and authorize at the server boundary. Client-side visibility and validation improve usability but never grant access.
- Make retries, idempotency, transactions, tenancy, audit events, and failure recovery explicit for mutations.
- Keep public APIs, events, jobs, component aliases, routes, tokens, and view extension points versioned and documented.
- Prefer semantic HTML, keyboard access, visible focus, localization, RTL support, reduced motion, and WCAG 2.2 AA behavior.
- Do not commit secrets, private data, generated credentials, unexplained snapshots, or unrelated formatting changes.

## Review and verification

- Test allowed, denied, invalid, wrong-tenant/team, duplicate, concurrent, timeout, and recovery paths where applicable.
- Run formatting, linting, static analysis, architecture checks, type checks, accessibility checks, and the smallest relevant test suite.
- Check internal links, examples, manifests, migrations, compatibility claims, and release notes before merging.
- Document deliberate exclusions and follow-up work instead of leaving implicit behavior.

## Naming and structure

Use descriptive nouns for domain concepts, verbs for actions, singular class names, plural collection names, and stable kebab-case package/route identifiers. Keep framework-specific code at the edge and use the directory conventions defined by [MODULES.md](../architecture/MODULES.md), [LARAVEL.md](LARAVEL.md), and the relevant frontend standard.
