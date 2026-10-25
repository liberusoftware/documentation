# Boilerplate: Meta Server-Side Tracking Livewire presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#meta-server-side-tracking). No dedicated package name match was found for this layer in the scanned module manifests. This retained spelling maps to `analytics-meta`; it is not another independent module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-meta-server-side-tracking-livewire`
**Matching core package:** [`module-meta-server-side-tracking`](../core/meta-server-side-tracking.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Meta server-side event mapping, deduplication, consent, hashing, delivery, and diagnostics.

## Adapter implementation plan

This package presents the Meta Server-Side Tracking core capability through Livewire 4. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Provide responsive, keyboard-accessible, localized workflows with clear loading, validation, empty, denied, queued, failure, and recovery states.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Meta Server-Side Tracking core boundary.
