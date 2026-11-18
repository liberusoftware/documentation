# Liberu: Business Workflow Reconciliation

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#business-workflow-reconciliation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent feature specification

**Domain module:** `module-liberu-business-workflow-reconciliation`
**Application:** Liberu Business Platform
**Status:** New cross-product capability; it does not replace Billing, Control Panel, CRM, Ecommerce, Accounting, Automation, or Maintenance workflows
**Architecture:** [MODULES](../../../architecture/MODULES.md) · [LIBERU](../../LIBERU.md) · [Standards](../../../standards/README.md)

## Purpose and scope

Business Workflow Reconciliation tracks the shared state of composed workflows such as hosting order-to-provisioning, lead-to-revenue, procure-to-pay, and incident-to-resolution. Owning products remain authoritative for each local state and action.

## New capabilities

- **Workflow run registry:** correlate cross-product steps, contracts, events, approvals, actors, and tenant context.
- **State mapping:** declare the expected relationship between source states without copying source records.
- **Reconciliation rules:** detect missing, duplicate, out-of-order, stale, unauthorized, or contradictory transitions.
- **Recovery coordination:** expose retry, replay, compensation, escalation, and manual resolution with idempotency protection.
- **Audit timeline:** provide a permission-filtered evidence trail with correlation IDs, timestamps, contract versions, and responsible owners.

## Boundaries and verification

This module coordinates and reports; it does not mutate another module's private data or bypass its actions. Test duplicate/out-of-order events, partial failure, provider outage, timeout, replay, compensation, wrong-tenant access, manual resolution, and audit redaction.

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Workflow run registry** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `workflow run registry`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **State mapping** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `state mapping`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Reconciliation rules** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `reconciliation rules`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Recovery coordination** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `recovery coordination`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Audit timeline** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `audit timeline`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/business-workflow-reconciliation.md) | [Source map](../SOURCE-MAPPING.md#business-workflow-reconciliation) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/business-workflow-reconciliation.md) | [`project-liberu-official-laravel-api`](https://github.com/liberusoftware/project-liberu-official-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/business-workflow-reconciliation.md) | [`project-liberu-official-laravel-filament`](https://github.com/liberusoftware/project-liberu-official-laravel-filament) · [`module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-filament`](https://github.com/liberusoftware/module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-filament) (`liberusoftware/planned-liberu-business-workflow-reconciliation-c7cb9c4f-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/business-workflow-reconciliation.md) | [`project-liberu-official-laravel-filament`](https://github.com/liberusoftware/project-liberu-official-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/business-workflow-reconciliation.md) | [`project-liberu-official-laravel-inertia-react`](https://github.com/liberusoftware/project-liberu-official-laravel-inertia-react) · [`module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-react-inertia`](https://github.com/liberusoftware/module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-react-inertia) (`@liberusoftware/module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/business-workflow-reconciliation.md) | [`project-liberu-official-laravel-inertia-vue`](https://github.com/liberusoftware/project-liberu-official-laravel-inertia-vue) · [`module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-vue-inertia`](https://github.com/liberusoftware/module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-vue-inertia) (`@liberusoftware/module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/business-workflow-reconciliation.md) | [`project-liberu-official-nuxt-vue`](https://github.com/liberusoftware/project-liberu-official-nuxt-vue) · [`module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-nuxt`](https://github.com/liberusoftware/module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-nuxt) (`@liberusoftware/module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-nuxt`) | Standalone Vue SSR client consuming `project-liberu-official-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/business-workflow-reconciliation.md) | [`project-liberu-official-next-react`](https://github.com/liberusoftware/project-liberu-official-next-react) · [`module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-nextjs`](https://github.com/liberusoftware/module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-nextjs) (`@liberusoftware/module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-nextjs`) | App Router Server/Client components consuming `project-liberu-official-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/business-workflow-reconciliation.md) | [`project-liberu-official-mobile-react`](https://github.com/liberusoftware/project-liberu-official-mobile-react) · [`module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-react-native`](https://github.com/liberusoftware/module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-react-native) (`@liberusoftware/module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/business-workflow-reconciliation.md) | [`project-liberu-official-mobile-flutter`](https://github.com/liberusoftware/project-liberu-official-mobile-flutter) · [`module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-flutter`](https://github.com/liberusoftware/module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-flutter) (`module_planned_liberu_business_workflow_reconciliation_c7cb9c4f_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/business-workflow-reconciliation.md) | [`project-liberu-official-dart-mobile`](https://github.com/liberusoftware/project-liberu-official-dart-mobile) · [`module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-dart-mobile`](https://github.com/liberusoftware/module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-dart-mobile) (`module_planned_liberu_business_workflow_reconciliation_c7cb9c4f_dart_mobile`)<br>[`project-liberu-official-dart-desktop`](https://github.com/liberusoftware/project-liberu-official-dart-desktop) · [`module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-dart-desktop`](https://github.com/liberusoftware/module-planned-liberu-business-workflow-reconciliation-c7cb9c4f-dart-desktop) (`module_planned_liberu_business_workflow_reconciliation_c7cb9c4f_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
