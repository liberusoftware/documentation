# CRM: Crm Activities

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-activities). Observed identity: [`liberusoftware/module-crm-activities`](../../../modules/source/liberusoftware--module-crm-activities.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-crm-crm-activities`
**Application:** CRM  
**Capability group:** Crm Activities  
**Source scope:** [CRM.md](../CRM.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Crm Activities module owns crm activities domain behavior. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Tasks:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Calls:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Meetings:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Emails:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Deadlines:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Recurrence:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Queues:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Bulk completion:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Reminders:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Outcomes:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Goals:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Activity reporting:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-crm-crm-activities-filament`, `module-crm-crm-activities-livewire`, and `module-crm-crm-activities-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify crm activities across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
| **Tasks** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `tasks`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Calls** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `calls`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Meetings** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `meetings`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Emails** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `emails`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Deadlines** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `deadlines`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Recurrence** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `recurrence`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Queues** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `queues`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Bulk completion** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `bulk completion`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Reminders** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `reminders`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Outcomes** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `outcomes`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Goals** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `goals`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Activity reporting** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `activity reporting`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/crm-activities.md) | [Source map](../SOURCE-MAPPING.md#crm-activities) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/crm-activities.md) | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/crm-activities.md) | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) · [`module-crm-activities-filament`](https://github.com/liberusoftware/module-crm-activities-filament) (`liberusoftware/crm-activities-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/crm-activities.md) | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/crm-activities.md) | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) · [`module-crm-activities-react-inertia`](https://github.com/liberusoftware/module-crm-activities-react-inertia) (`@liberusoftware/module-crm-activities-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/crm-activities.md) | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) · [`module-crm-activities-vue-inertia`](https://github.com/liberusoftware/module-crm-activities-vue-inertia) (`@liberusoftware/module-crm-activities-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/crm-activities.md) | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) · [`module-crm-activities-nuxt`](https://github.com/liberusoftware/module-crm-activities-nuxt) (`@liberusoftware/module-crm-activities-nuxt`) | Standalone Vue SSR client consuming `project-crm-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/crm-activities.md) | [`project-crm-next-react`](https://github.com/liberusoftware/project-crm-next-react) · [`module-crm-activities-nextjs`](https://github.com/liberusoftware/module-crm-activities-nextjs) (`@liberusoftware/module-crm-activities-nextjs`) | App Router Server/Client components consuming `project-crm-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/crm-activities.md) | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) · [`module-crm-activities-react-native`](https://github.com/liberusoftware/module-crm-activities-react-native) (`@liberusoftware/module-crm-activities-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/crm-activities.md) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) · [`module-crm-activities-flutter`](https://github.com/liberusoftware/module-crm-activities-flutter) (`module_crm_activities_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/crm-activities.md) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) · [`module-crm-activities-dart-mobile`](https://github.com/liberusoftware/module-crm-activities-dart-mobile) (`module_crm_activities_dart_mobile`)<br>[`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) · [`module-crm-activities-dart-desktop`](https://github.com/liberusoftware/module-crm-activities-dart-desktop) (`module_crm_activities_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
