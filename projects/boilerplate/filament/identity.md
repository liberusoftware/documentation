# Boilerplate: Identity Filament presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#identity). Observed identity: [`liberusoftware/identity-core-filament`](../../../modules/source/liberusoftware--identity-core-filament.md). This retained spelling maps to `identity-core`; it is not another independent module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-identity-filament`
**Matching core package:** [`module-identity`](../core/identity.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Registration, authentication, logout, password recovery, verification, identity linking, and security events.

## Adapter implementation plan

This package presents the Identity core capability through Filament 5. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Provide responsive, keyboard-accessible, localized workflows with clear loading, validation, empty, denied, queued, failure, and recovery states.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Identity core boundary.
