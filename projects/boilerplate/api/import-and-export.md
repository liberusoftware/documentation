# Boilerplate: Import and Export API presentation packages

**Composer package:** `module-import-and-export-api`
**Matching core package:** [`module-import-and-export`](../core/import-and-export.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Schemas, mapping, dry runs, validation, queued execution, progress, errors, authorization, and retention.

## Adapter implementation plan

This package presents the Import and Export core capability through API. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Publish versioned OpenAPI 3.1 schemas, operation IDs, scopes, pagination, rate limits, idempotency, concurrency, and RFC 9457 Problem Details.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Import and Export core boundary.
