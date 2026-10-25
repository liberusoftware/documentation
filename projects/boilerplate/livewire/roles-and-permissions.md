# Boilerplate: Roles and Permissions Livewire presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#roles-and-permissions). No dedicated package name match was found for this layer in the scanned module manifests. This retained spelling maps to `roles-permissions`; it is not another independent module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-roles-and-permissions-livewire`
**Matching core package:** [`module-roles-and-permissions`](../core/roles-and-permissions.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Permission definitions, assignments, contextual scope, policies, caches, safeguards, and audit.

## Adapter implementation plan

This package presents the Roles and Permissions core capability through Livewire 4. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Provide responsive, keyboard-accessible, localized workflows with clear loading, validation, empty, denied, queued, failure, and recovery states.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Roles and Permissions core boundary.
