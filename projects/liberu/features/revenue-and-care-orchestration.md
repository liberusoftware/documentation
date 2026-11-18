# Liberu: Revenue and Care Orchestration

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-and-care-orchestration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Domain module:** `module-liberu-revenue-and-care-orchestration`
**Status:** Liberu-specific cross-product capability
**Architecture:** [LIBERU](../../LIBERU.md) · [CRM](../../crm/CRM.md) · [Modules](../../../architecture/MODULES.md)

## Purpose

This module turns authoritative CRM, CMS, Billing, Control Panel, Ecommerce, Maintenance, Projects, and Automation events into explainable customer-health projections and safe next actions. It coordinates the Liberu hosting and professional-services journey without duplicating customer, case, invoice, subscription, infrastructure, project, or AI records.

## Business capabilities

- **Customer health constellation:** source, confidence, owner, expiry, and drill-through evidence across authoritative product modules.
- **Revenue-aware service recovery:** coordinated recovery for incidents, provisioning failures, entitlement gaps, renewal risk, and overdue commercial actions.
- **Contact-protection ledger:** blocks automated outreach until `next_contact_at`, conversion, explicit reply/request, or approved exception.
- **Cross-brand consent and quiet-hour evaluation:** unified evaluation for Liberu websites, campaigns, sales, support, and success.
- **Approval-gated AI recommendations:** triage, summaries, drafts, next-best action, and recovery plays requiring explicit operator approval.
- **Mobile-ready daily queues:** prioritized queues for sales, support, on-call, and managers across web and mobile surfaces.

## Invariants and events

Health signals are immutable observations and can expire; projections never overwrite source records. An outreach decision must cite the policy version and reason. Service recovery must retain the source incident/job ID and owning module. AI output is advisory until an authorized action accepts it. Publish `HealthSignalObserved`, `CareRiskDetected`, `OutreachDeferred`, `RecoveryCaseRequested`, and `AiRecommendationAccepted` after commit through the outbox.

## Non-goals

CRM remains authoritative for people, relationships, cases, activities, consent, and dialer behavior. Billing/Ecommerce remain authoritative for money and orders. Control Panel remains authoritative for infrastructure. Automation remains authoritative for the generic workflow and AI runtime.

## Acceptance

Test cross-module correlation, stale signals, duplicate/replayed events, consent withdrawal, outreach cooling-off, incident-to-case handoff, tenant/brand isolation, AI approval, provider outage, offline mobile recovery, and explainable audit trails.

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Customer health constellation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `customer health constellation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Revenue-aware service recovery** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `revenue-aware service recovery`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Contact-protection ledger** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `contact-protection ledger`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Cross-brand consent and quiet-hour evaluation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `cross-brand consent and quiet-hour evaluation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Approval-gated AI recommendations** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `approval-gated ai recommendations`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Mobile-ready daily queues** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `mobile-ready daily queues`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/revenue-and-care-orchestration.md) | [Source map](../SOURCE-MAPPING.md#revenue-and-care-orchestration) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/revenue-and-care-orchestration.md) | [`project-liberu-official-laravel-api`](https://github.com/liberusoftware/project-liberu-official-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/revenue-and-care-orchestration.md) | [`project-liberu-official-laravel-filament`](https://github.com/liberusoftware/project-liberu-official-laravel-filament) · [`module-planned-liberu-revenue-and-care-orchestration-40451d50-filament`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-filament) (`liberusoftware/planned-liberu-revenue-and-care-orchestration-40451d50-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/revenue-and-care-orchestration.md) | [`project-liberu-official-laravel-filament`](https://github.com/liberusoftware/project-liberu-official-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/revenue-and-care-orchestration.md) | [`project-liberu-official-laravel-inertia-react`](https://github.com/liberusoftware/project-liberu-official-laravel-inertia-react) · [`module-planned-liberu-revenue-and-care-orchestration-40451d50-react-inertia`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-react-inertia) (`@liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/revenue-and-care-orchestration.md) | [`project-liberu-official-laravel-inertia-vue`](https://github.com/liberusoftware/project-liberu-official-laravel-inertia-vue) · [`module-planned-liberu-revenue-and-care-orchestration-40451d50-vue-inertia`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-vue-inertia) (`@liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/revenue-and-care-orchestration.md) | [`project-liberu-official-nuxt-vue`](https://github.com/liberusoftware/project-liberu-official-nuxt-vue) · [`module-planned-liberu-revenue-and-care-orchestration-40451d50-nuxt`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-nuxt) (`@liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-nuxt`) | Standalone Vue SSR client consuming `project-liberu-official-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/revenue-and-care-orchestration.md) | [`project-liberu-official-next-react`](https://github.com/liberusoftware/project-liberu-official-next-react) · [`module-planned-liberu-revenue-and-care-orchestration-40451d50-nextjs`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-nextjs) (`@liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-nextjs`) | App Router Server/Client components consuming `project-liberu-official-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/revenue-and-care-orchestration.md) | [`project-liberu-official-mobile-react`](https://github.com/liberusoftware/project-liberu-official-mobile-react) · [`module-planned-liberu-revenue-and-care-orchestration-40451d50-react-native`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-react-native) (`@liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/revenue-and-care-orchestration.md) | [`project-liberu-official-mobile-flutter`](https://github.com/liberusoftware/project-liberu-official-mobile-flutter) · [`module-planned-liberu-revenue-and-care-orchestration-40451d50-flutter`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-flutter) (`module_planned_liberu_revenue_and_care_orchestration_40451d50_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/revenue-and-care-orchestration.md) | [`project-liberu-official-dart-mobile`](https://github.com/liberusoftware/project-liberu-official-dart-mobile) · [`module-planned-liberu-revenue-and-care-orchestration-40451d50-dart-mobile`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-dart-mobile) (`module_planned_liberu_revenue_and_care_orchestration_40451d50_dart_mobile`)<br>[`project-liberu-official-dart-desktop`](https://github.com/liberusoftware/project-liberu-official-dart-desktop) · [`module-planned-liberu-revenue-and-care-orchestration-40451d50-dart-desktop`](https://github.com/liberusoftware/module-planned-liberu-revenue-and-care-orchestration-40451d50-dart-desktop) (`module_planned_liberu_revenue_and_care_orchestration_40451d50_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
