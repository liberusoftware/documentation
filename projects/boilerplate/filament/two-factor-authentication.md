# Boilerplate: Two-Factor Authentication Filament presentation packages

**Composer package:** `module-two-factor-authentication-filament`
**Matching core package:** [`module-two-factor-authentication`](../core/two-factor-authentication.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** TOTP enrollment, recovery codes, enforcement, trusted devices, recovery, and audit.

## Adapter implementation plan

This package presents the Two-Factor Authentication core capability through Filament 5. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Provide responsive, keyboard-accessible, localized workflows with clear loading, validation, empty, denied, queued, failure, and recovery states.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Two-Factor Authentication core boundary.
