# SAP: Data and Intelligence

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#data-and-intelligence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design status and ownership:** this is an enterprise capability group. Read the [detailed data and intelligence design](../design/data-and-intelligence.md) for concrete records, transitions, permissions, proposed operations and recovery. Compose existing product owners under the [enterprise composition design](../COMPOSITION.md); package identifiers and endpoint examples here are proposals, not verified releases.

## Canonical independent module specification

**Domain module:** `module-sap-data-and-intelligence`
**Application:** SAP  
**Capability group:** Module plan  
**Source scope:** [SAP.md](../SAP.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Data and Intelligence module owns Governed metrics, semantic models, reports, planning, forecasts, data quality, lineage, exports, and AI assistance. This enterprise scope composes the canonical product owners; only its own orchestration and genuine capability gaps require new independently versioned modules.

## 2. Full feature scope

- **Governed metrics:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Semantic models:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Reports:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Planning:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Forecasts:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Data quality:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Lineage:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Exports:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **AI assistance:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-sap-data-and-intelligence-filament`, `module-sap-data-and-intelligence-livewire`, and `module-sap-data-and-intelligence-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify governed metrics across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify semantic models across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify reports across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify planning across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify forecasts across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify data quality across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify lineage across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify exports across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify aI assistance across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
| **Governed metrics** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `governed metrics`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Semantic models** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `semantic models`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Reports** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `reports`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Planning** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `planning`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Forecasts** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `forecasts`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Data quality** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `data quality`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Lineage** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `lineage`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Exports** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `exports`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **AI assistance** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `ai assistance`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/data-and-intelligence.md) | [Source map](../SOURCE-MAPPING.md#data-and-intelligence) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/data-and-intelligence.md) | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/data-and-intelligence.md) | [`project-enterprise-sap-laravel-filament`](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament) · [`module-sap-data-and-intelligence-filament`](https://github.com/liberusoftware/module-sap-data-and-intelligence-filament) (`liberusoftware/sap-data-and-intelligence-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/data-and-intelligence.md) | [`project-enterprise-sap-laravel-filament`](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/data-and-intelligence.md) | [`project-enterprise-sap-laravel-inertia-react`](https://github.com/liberusoftware/project-enterprise-sap-laravel-inertia-react) · [`module-sap-data-and-intelligence-react-inertia`](https://github.com/liberusoftware/module-sap-data-and-intelligence-react-inertia) (`@liberusoftware/module-sap-data-and-intelligence-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/data-and-intelligence.md) | [`project-enterprise-sap-laravel-inertia-vue`](https://github.com/liberusoftware/project-enterprise-sap-laravel-inertia-vue) · [`module-sap-data-and-intelligence-vue-inertia`](https://github.com/liberusoftware/module-sap-data-and-intelligence-vue-inertia) (`@liberusoftware/module-sap-data-and-intelligence-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/data-and-intelligence.md) | [`project-enterprise-sap-nuxt-vue`](https://github.com/liberusoftware/project-enterprise-sap-nuxt-vue) · [`module-sap-data-and-intelligence-nuxt`](https://github.com/liberusoftware/module-sap-data-and-intelligence-nuxt) (`@liberusoftware/module-sap-data-and-intelligence-nuxt`) | Standalone Vue SSR client consuming `project-enterprise-sap-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/data-and-intelligence.md) | [`project-enterprise-sap-next-react`](https://github.com/liberusoftware/project-enterprise-sap-next-react) · [`module-sap-data-and-intelligence-nextjs`](https://github.com/liberusoftware/module-sap-data-and-intelligence-nextjs) (`@liberusoftware/module-sap-data-and-intelligence-nextjs`) | App Router Server/Client components consuming `project-enterprise-sap-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/data-and-intelligence.md) | [`project-enterprise-sap-mobile-react`](https://github.com/liberusoftware/project-enterprise-sap-mobile-react) · [`module-sap-data-and-intelligence-react-native`](https://github.com/liberusoftware/module-sap-data-and-intelligence-react-native) (`@liberusoftware/module-sap-data-and-intelligence-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/data-and-intelligence.md) | [`project-enterprise-sap-mobile-flutter`](https://github.com/liberusoftware/project-enterprise-sap-mobile-flutter) · [`module-sap-data-and-intelligence-flutter`](https://github.com/liberusoftware/module-sap-data-and-intelligence-flutter) (`module_sap_data_and_intelligence_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/data-and-intelligence.md) | [`project-enterprise-sap-dart-mobile`](https://github.com/liberusoftware/project-enterprise-sap-dart-mobile) · [`module-sap-data-and-intelligence-dart-mobile`](https://github.com/liberusoftware/module-sap-data-and-intelligence-dart-mobile) (`module_sap_data_and_intelligence_dart_mobile`)<br>[`project-enterprise-sap-dart-desktop`](https://github.com/liberusoftware/project-enterprise-sap-dart-desktop) · [`module-sap-data-and-intelligence-dart-desktop`](https://github.com/liberusoftware/module-sap-data-and-intelligence-dart-desktop) (`module_sap_data_and_intelligence_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
