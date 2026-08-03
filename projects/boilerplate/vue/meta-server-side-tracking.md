# Boilerplate: Meta Server-Side Tracking Vue presentation packages

**Composer package:** `module-meta-server-side-tracking-vue`
**Matching core package:** [`module-meta-server-side-tracking`](../core/meta-server-side-tracking.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Meta server-side event mapping, deduplication, consent, hashing, delivery, and diagnostics.

## Adapter implementation plan

This package presents the Meta Server-Side Tracking core capability through Vue. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Consume the versioned API contract or approved server boundary; keep client state and views replaceable, typed, accessible, and resilient to partial failure.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Meta Server-Side Tracking core boundary.
