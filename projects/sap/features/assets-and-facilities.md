# SAP: Assets and Facilities

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#assets-and-facilities). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design status and ownership:** this is an enterprise capability group. Read the [detailed assets and facilities design](../design/assets-and-facilities.md) for concrete records, transitions, permissions, proposed operations and recovery. Compose existing product owners under the [enterprise composition design](../COMPOSITION.md); package identifiers and endpoint examples here are proposals, not verified releases.

## Canonical independent module specification

**Domain module:** `module-sap-assets-and-facilities`
**Application:** SAP  
**Capability group:** Module plan  
**Source scope:** [SAP.md](../SAP.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Assets and Facilities module owns Asset lifecycle, maintenance, leases, locations, facilities, energy, safety, and disposal. This enterprise scope composes the canonical product owners; only its own orchestration and genuine capability gaps require new independently versioned modules.

## 2. Full feature scope

- **Asset lifecycle:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Maintenance:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Leases:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Locations:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Facilities:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Energy:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Safety:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Disposal:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-sap-assets-and-facilities-filament`, `module-sap-assets-and-facilities-livewire`, and `module-sap-assets-and-facilities-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify asset lifecycle across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify maintenance across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify leases across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify locations across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify facilities across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify energy across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify safety across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify disposal across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
| **Asset lifecycle** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `asset lifecycle`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Maintenance** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `maintenance`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Leases** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `leases`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Locations** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `locations`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Facilities** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `facilities`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Energy** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `energy`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Safety** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `safety`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Disposal** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `disposal`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/assets-and-facilities.md) | [Source map](../SOURCE-MAPPING.md#assets-and-facilities) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/assets-and-facilities.md) | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/assets-and-facilities.md) | [`project-enterprise-sap-laravel-filament`](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament) · [`module-sap-assets-and-facilities-filament`](https://github.com/liberusoftware/module-sap-assets-and-facilities-filament) (`liberusoftware/sap-assets-and-facilities-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/assets-and-facilities.md) | [`project-enterprise-sap-laravel-filament`](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/assets-and-facilities.md) | [`project-enterprise-sap-laravel-inertia-react`](https://github.com/liberusoftware/project-enterprise-sap-laravel-inertia-react) · [`module-sap-assets-and-facilities-react-inertia`](https://github.com/liberusoftware/module-sap-assets-and-facilities-react-inertia) (`@liberusoftware/module-sap-assets-and-facilities-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/assets-and-facilities.md) | [`project-enterprise-sap-laravel-inertia-vue`](https://github.com/liberusoftware/project-enterprise-sap-laravel-inertia-vue) · [`module-sap-assets-and-facilities-vue-inertia`](https://github.com/liberusoftware/module-sap-assets-and-facilities-vue-inertia) (`@liberusoftware/module-sap-assets-and-facilities-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/assets-and-facilities.md) | [`project-enterprise-sap-nuxt-vue`](https://github.com/liberusoftware/project-enterprise-sap-nuxt-vue) · [`module-sap-assets-and-facilities-nuxt`](https://github.com/liberusoftware/module-sap-assets-and-facilities-nuxt) (`@liberusoftware/module-sap-assets-and-facilities-nuxt`) | Standalone Vue SSR client consuming `project-enterprise-sap-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/assets-and-facilities.md) | [`project-enterprise-sap-next-react`](https://github.com/liberusoftware/project-enterprise-sap-next-react) · [`module-sap-assets-and-facilities-nextjs`](https://github.com/liberusoftware/module-sap-assets-and-facilities-nextjs) (`@liberusoftware/module-sap-assets-and-facilities-nextjs`) | App Router Server/Client components consuming `project-enterprise-sap-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/assets-and-facilities.md) | [`project-enterprise-sap-mobile-react`](https://github.com/liberusoftware/project-enterprise-sap-mobile-react) · [`module-sap-assets-and-facilities-react-native`](https://github.com/liberusoftware/module-sap-assets-and-facilities-react-native) (`@liberusoftware/module-sap-assets-and-facilities-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/assets-and-facilities.md) | [`project-enterprise-sap-mobile-flutter`](https://github.com/liberusoftware/project-enterprise-sap-mobile-flutter) · [`module-sap-assets-and-facilities-flutter`](https://github.com/liberusoftware/module-sap-assets-and-facilities-flutter) (`module_sap_assets_and_facilities_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/assets-and-facilities.md) | [`project-enterprise-sap-dart-mobile`](https://github.com/liberusoftware/project-enterprise-sap-dart-mobile) · [`module-sap-assets-and-facilities-dart-mobile`](https://github.com/liberusoftware/module-sap-assets-and-facilities-dart-mobile) (`module_sap_assets_and_facilities_dart_mobile`)<br>[`project-enterprise-sap-dart-desktop`](https://github.com/liberusoftware/project-enterprise-sap-dart-desktop) · [`module-sap-assets-and-facilities-dart-desktop`](https://github.com/liberusoftware/module-sap-assets-and-facilities-dart-desktop) (`module_sap_assets_and_facilities_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
