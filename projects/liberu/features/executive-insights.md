# Liberu: Executive Insights

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#executive-insights). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent feature specification

**Domain module:** `module-liberu-executive-insights`
**Application:** Liberu Business Platform
**Status:** New cross-product capability; it does not replace Accounting, CRM, SAP Data and Intelligence, or product analytics modules
**Architecture:** [MODULES](../../../architecture/MODULES.md) · [LIBERU](../../LIBERU.md) · [Standards](../../../standards/README.md)

## Purpose and scope

Executive Insights provides governed cross-product metrics and read models for leadership and operations. Source systems remain authoritative; this module owns metric definitions, lineage, freshness, access, snapshots, and drill-through evidence.

## New capabilities

- **Metric registry:** define owner, formula, source contracts, dimensions, currency/timezone, freshness, and version.
- **Cross-product projections:** combine authorized events/read models for revenue, margin, cash, pipeline, service health, utilization, risk, and provider spend.
- **Evidence drill-through:** link each value to authorized source records, reconciliation status, and calculation version.
- **Decision snapshots:** capture period-closed metric packs with immutable lineage and approval status.
- **Data-quality operations:** surface freshness, missing dimensions, reconciliation failures, stale providers, and permission-filtered gaps.

## Boundaries and verification

The module never becomes the owner of invoices, customers, tickets, jobs, assets, or ledger records. Test formula/version changes, tenant and role filtering, stale data, missing sources, currency/timezone conversions, reconciliation, export redaction, and reproducible snapshots.

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Metric registry** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `metric registry`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Cross-product projections** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `cross-product projections`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Evidence drill-through** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `evidence drill-through`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Decision snapshots** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `decision snapshots`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Data-quality operations** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `data-quality operations`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/executive-insights.md) | [Source map](../SOURCE-MAPPING.md#executive-insights) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/executive-insights.md) | [`project-liberu-official-laravel-api`](https://github.com/liberusoftware/project-liberu-official-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/executive-insights.md) | [`project-liberu-official-laravel-filament`](https://github.com/liberusoftware/project-liberu-official-laravel-filament) · [`module-planned-liberu-executive-insights-0532ffee-filament`](https://github.com/liberusoftware/module-planned-liberu-executive-insights-0532ffee-filament) (`liberusoftware/planned-liberu-executive-insights-0532ffee-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/executive-insights.md) | [`project-liberu-official-laravel-filament`](https://github.com/liberusoftware/project-liberu-official-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/executive-insights.md) | [`project-liberu-official-laravel-inertia-react`](https://github.com/liberusoftware/project-liberu-official-laravel-inertia-react) · [`module-planned-liberu-executive-insights-0532ffee-react-inertia`](https://github.com/liberusoftware/module-planned-liberu-executive-insights-0532ffee-react-inertia) (`@liberusoftware/module-planned-liberu-executive-insights-0532ffee-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/executive-insights.md) | [`project-liberu-official-laravel-inertia-vue`](https://github.com/liberusoftware/project-liberu-official-laravel-inertia-vue) · [`module-planned-liberu-executive-insights-0532ffee-vue-inertia`](https://github.com/liberusoftware/module-planned-liberu-executive-insights-0532ffee-vue-inertia) (`@liberusoftware/module-planned-liberu-executive-insights-0532ffee-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/executive-insights.md) | [`project-liberu-official-nuxt-vue`](https://github.com/liberusoftware/project-liberu-official-nuxt-vue) · [`module-planned-liberu-executive-insights-0532ffee-nuxt`](https://github.com/liberusoftware/module-planned-liberu-executive-insights-0532ffee-nuxt) (`@liberusoftware/module-planned-liberu-executive-insights-0532ffee-nuxt`) | Standalone Vue SSR client consuming `project-liberu-official-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/executive-insights.md) | [`project-liberu-official-next-react`](https://github.com/liberusoftware/project-liberu-official-next-react) · [`module-planned-liberu-executive-insights-0532ffee-nextjs`](https://github.com/liberusoftware/module-planned-liberu-executive-insights-0532ffee-nextjs) (`@liberusoftware/module-planned-liberu-executive-insights-0532ffee-nextjs`) | App Router Server/Client components consuming `project-liberu-official-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/executive-insights.md) | [`project-liberu-official-mobile-react`](https://github.com/liberusoftware/project-liberu-official-mobile-react) · [`module-planned-liberu-executive-insights-0532ffee-react-native`](https://github.com/liberusoftware/module-planned-liberu-executive-insights-0532ffee-react-native) (`@liberusoftware/module-planned-liberu-executive-insights-0532ffee-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/executive-insights.md) | [`project-liberu-official-mobile-flutter`](https://github.com/liberusoftware/project-liberu-official-mobile-flutter) · [`module-planned-liberu-executive-insights-0532ffee-flutter`](https://github.com/liberusoftware/module-planned-liberu-executive-insights-0532ffee-flutter) (`module_planned_liberu_executive_insights_0532ffee_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/executive-insights.md) | [`project-liberu-official-dart-mobile`](https://github.com/liberusoftware/project-liberu-official-dart-mobile) · [`module-planned-liberu-executive-insights-0532ffee-dart-mobile`](https://github.com/liberusoftware/module-planned-liberu-executive-insights-0532ffee-dart-mobile) (`module_planned_liberu_executive_insights_0532ffee_dart_mobile`)<br>[`project-liberu-official-dart-desktop`](https://github.com/liberusoftware/project-liberu-official-dart-desktop) · [`module-planned-liberu-executive-insights-0532ffee-dart-desktop`](https://github.com/liberusoftware/module-planned-liberu-executive-insights-0532ffee-dart-desktop) (`module_planned_liberu_executive_insights_0532ffee_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
