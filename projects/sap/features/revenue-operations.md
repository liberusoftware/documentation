# SAP: Revenue Operations

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-operations). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design status and ownership:** this is an enterprise capability group. Read the [detailed revenue operations design](../design/revenue-operations.md) for concrete records, transitions, permissions, proposed operations and recovery. Compose existing product owners under the [enterprise composition design](../COMPOSITION.md); package identifiers and endpoint examples here are proposals, not verified releases.

## Canonical independent module specification

**Domain module:** `module-sap-revenue-operations`
**Application:** SAP  
**Capability group:** Module plan  
**Source scope:** [SAP.md](../SAP.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Revenue Operations module owns Catalog, pricing, subscriptions, usage, licensing, billing, payments, collections, and revenue schedules. This enterprise scope composes the canonical product owners; only its own orchestration and genuine capability gaps require new independently versioned modules.

## 2. Full feature scope

- **Catalog:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Pricing:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Subscriptions:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Usage:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Licensing:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Billing:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Payments:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Collections:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Revenue schedules:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

## 3. Ownership and boundaries

- Own the capability's domain rules, policies, actions, queries, events, persistence, migrations, configuration, audit semantics, and failure recovery.
- Expose stable contracts, immutable DTOs/read models, commands, queries, and past-tense domain events where other modules have a legitimate integration need.
- Consume identity, organizations/teams, authorization, settings, files, notifications, queues, localization, currency, and observability from the shared foundation rather than duplicating them.
- Never depend on an application's `App\` classes, another module's private tables/models, a provider SDK in provider-neutral code, or an optional presentation framework.
- Keep Filament, Livewire, and HTTP API logic in matching one-to-one presentation packages when those surfaces are required.

## 4. Implementation strategy

### Domain model

- Define aggregates, entities, value objects, enums, invariants, lifecycle states, and transition rules using the terminology in this specification.
- Make invalid states unrepresentable where practical and enforce remaining invariants at every mutation boundary.
- Use opaque stable identifiers and explicit actor, tenant, locale, timezone, and currency context where relevant.

### Application layer

- Implement one application action per mutation/use case and purpose-built queries for reads.
- Authorize before accessing or mutating protected data; navigation or UI visibility never substitutes for a policy.
- Execute local invariant changes transactionally, dispatch events after commit, and make retryable commands idempotent.
- Model long-running or cross-module work through queued jobs, outbox/inbox delivery, sagas, compensation, and operator-visible recovery.

### Persistence and integrations

- Store only module-owned data in module-owned tables with documented indexes, constraints, retention, export, deletion, and migration behavior.
- Integrate other capabilities through contracts/events and external systems through independent provider adapters with timeouts, retries, rate limits, reconciliation, and sandbox support.
- Treat imports, webhooks, provider callbacks, files, and generated content as untrusted inputs with provenance and deduplication.

### Presentation

- Provide matching optional presentation packages only when required: `module-sap-revenue-operations-filament`, `module-sap-revenue-operations-livewire`, and `module-sap-revenue-operations-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify catalog across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify pricing across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify subscriptions across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify usage across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify licensing across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify billing across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify payments across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify collections across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify revenue schedules across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Add unit tests for pure rules/value objects and feature tests for actions, policies, validation, persistence, events, jobs, and module lifecycle.
- Add architecture tests for forbidden dependencies, `App\` coupling, provider leakage, private cross-module access, and presentation dependencies.
- Add migration/upgrade, contract, compatibility, security, performance, failure/recovery, and minimal-host installation tests as risk requires.
- Run the independent Pest 5 suite through repository-owned Composer scripts and the shared package testbench; meaningful owned PHP targets 100% line coverage without excluding difficult code.
- Run composition tests in representative host applications while keeping this repository's suite authoritative for module behavior.

## 7. Definition of done

- Every feature in scope has explicit acceptance criteria, permissions, tenant behavior, persistence ownership, events, failure handling, telemetry, and tests.
- Public contracts and presentation extension points are versioned and documented.
- Install, enable, disable, upgrade, retry/recovery, and uninstall/retention behavior is verified.
- Security, accessibility where presented, compatibility, architecture, and 100% meaningful-PHP coverage gates pass.
- README, changelog, migration guidance, runbook, CI evidence, and tagged release are available from the independent repository.

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Catalog** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `catalog`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Pricing** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `pricing`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Subscriptions** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `subscriptions`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Usage** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `usage`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Licensing** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `licensing`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Billing** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `billing`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Payments** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `payments`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Collections** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `collections`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Revenue schedules** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `revenue schedules`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/revenue-operations.md) | [Source map](../SOURCE-MAPPING.md#revenue-operations) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/revenue-operations.md) | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/revenue-operations.md) | [`project-enterprise-sap-laravel-filament`](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament) · [`module-sap-revenue-operations-filament`](https://github.com/liberusoftware/module-sap-revenue-operations-filament) (`liberusoftware/sap-revenue-operations-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/revenue-operations.md) | [`project-enterprise-sap-laravel-filament`](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/revenue-operations.md) | [`project-enterprise-sap-laravel-inertia-react`](https://github.com/liberusoftware/project-enterprise-sap-laravel-inertia-react) · [`module-sap-revenue-operations-react-inertia`](https://github.com/liberusoftware/module-sap-revenue-operations-react-inertia) (`@liberusoftware/module-sap-revenue-operations-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/revenue-operations.md) | [`project-enterprise-sap-laravel-inertia-vue`](https://github.com/liberusoftware/project-enterprise-sap-laravel-inertia-vue) · [`module-sap-revenue-operations-vue-inertia`](https://github.com/liberusoftware/module-sap-revenue-operations-vue-inertia) (`@liberusoftware/module-sap-revenue-operations-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/revenue-operations.md) | [`project-enterprise-sap-nuxt-vue`](https://github.com/liberusoftware/project-enterprise-sap-nuxt-vue) · [`module-sap-revenue-operations-nuxt`](https://github.com/liberusoftware/module-sap-revenue-operations-nuxt) (`@liberusoftware/module-sap-revenue-operations-nuxt`) | Standalone Vue SSR client consuming `project-enterprise-sap-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/revenue-operations.md) | [`project-enterprise-sap-next-react`](https://github.com/liberusoftware/project-enterprise-sap-next-react) · [`module-sap-revenue-operations-nextjs`](https://github.com/liberusoftware/module-sap-revenue-operations-nextjs) (`@liberusoftware/module-sap-revenue-operations-nextjs`) | App Router Server/Client components consuming `project-enterprise-sap-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/revenue-operations.md) | [`project-enterprise-sap-mobile-react`](https://github.com/liberusoftware/project-enterprise-sap-mobile-react) · [`module-sap-revenue-operations-react-native`](https://github.com/liberusoftware/module-sap-revenue-operations-react-native) (`@liberusoftware/module-sap-revenue-operations-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/revenue-operations.md) | [`project-enterprise-sap-mobile-flutter`](https://github.com/liberusoftware/project-enterprise-sap-mobile-flutter) · [`module-sap-revenue-operations-flutter`](https://github.com/liberusoftware/module-sap-revenue-operations-flutter) (`module_sap_revenue_operations_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/revenue-operations.md) | [`project-enterprise-sap-dart-mobile`](https://github.com/liberusoftware/project-enterprise-sap-dart-mobile) · [`module-sap-revenue-operations-dart-mobile`](https://github.com/liberusoftware/module-sap-revenue-operations-dart-mobile) (`module_sap_revenue_operations_dart_mobile`)<br>[`project-enterprise-sap-dart-desktop`](https://github.com/liberusoftware/project-enterprise-sap-dart-desktop) · [`module-sap-revenue-operations-dart-desktop`](https://github.com/liberusoftware/module-sap-revenue-operations-dart-desktop) (`module_sap_revenue_operations_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
