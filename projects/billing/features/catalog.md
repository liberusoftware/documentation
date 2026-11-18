# Billing: Catalog

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#catalog). Observed identity: [`liberusoftware/module-billing-catalog`](../../../modules/source/liberusoftware--module-billing-catalog.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-billing-catalog`
**Application:** Billing  
**Capability group:** Module plan  
**Source scope:** [BILLING.md](../BILLING.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Catalog module owns Products, plans, add-ons, bundles, configurable options, eligibility, channels, and lifecycle. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Products:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Plans:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Add-ons:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Bundles:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Configurable options:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Eligibility:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Channels:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Lifecycle:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-billing-catalog-filament`, `module-billing-catalog-livewire`, and `module-billing-catalog-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify products across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify plans across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify add-ons across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify bundles across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify configurable options across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify eligibility across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify channels across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify lifecycle across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
| **Products** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `products`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Plans** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `plans`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Add-ons** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `add-ons`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Bundles** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `bundles`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Configurable options** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `configurable options`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Eligibility** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `eligibility`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Channels** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `channels`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Lifecycle** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `lifecycle`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/catalog.md) | [Source map](../SOURCE-MAPPING.md#catalog) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/catalog.md) | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/catalog.md) | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) · [`module-billing-catalog-filament`](https://github.com/liberusoftware/module-billing-catalog-filament) (`liberusoftware/billing-catalog-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/catalog.md) | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/catalog.md) | [`project-billing-laravel-inertia-react`](https://github.com/liberusoftware/project-billing-laravel-inertia-react) · [`module-billing-catalog-react-inertia`](https://github.com/liberusoftware/module-billing-catalog-react-inertia) (`@liberusoftware/module-billing-catalog-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/catalog.md) | [`project-billing-laravel-inertia-vue`](https://github.com/liberusoftware/project-billing-laravel-inertia-vue) · [`module-billing-catalog-vue-inertia`](https://github.com/liberusoftware/module-billing-catalog-vue-inertia) (`@liberusoftware/module-billing-catalog-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/catalog.md) | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) · [`module-billing-catalog-nuxt`](https://github.com/liberusoftware/module-billing-catalog-nuxt) (`@liberusoftware/module-billing-catalog-nuxt`) | Standalone Vue SSR client consuming `project-billing-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/catalog.md) | [`project-billing-next-react`](https://github.com/liberusoftware/project-billing-next-react) · [`module-billing-catalog-nextjs`](https://github.com/liberusoftware/module-billing-catalog-nextjs) (`@liberusoftware/module-billing-catalog-nextjs`) | App Router Server/Client components consuming `project-billing-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/catalog.md) | [`project-billing-mobile-react`](https://github.com/liberusoftware/project-billing-mobile-react) · [`module-billing-catalog-react-native`](https://github.com/liberusoftware/module-billing-catalog-react-native) (`@liberusoftware/module-billing-catalog-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/catalog.md) | [`project-billing-mobile-flutter`](https://github.com/liberusoftware/project-billing-mobile-flutter) · [`module-billing-catalog-flutter`](https://github.com/liberusoftware/module-billing-catalog-flutter) (`module_billing_catalog_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/catalog.md) | [`project-billing-dart-mobile`](https://github.com/liberusoftware/project-billing-dart-mobile) · [`module-billing-catalog-dart-mobile`](https://github.com/liberusoftware/module-billing-catalog-dart-mobile) (`module_billing_catalog_dart_mobile`)<br>[`project-billing-dart-desktop`](https://github.com/liberusoftware/project-billing-dart-desktop) · [`module-billing-catalog-dart-desktop`](https://github.com/liberusoftware/module-billing-catalog-dart-desktop) (`module_billing_catalog_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
