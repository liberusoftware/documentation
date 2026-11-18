# Genealogy: Genealogy Tree Viewer

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-tree-viewer). Observed identity: [`liberusoftware/module-genealogy-tree-viewer`](../../../modules/source/liberusoftware--module-genealogy-tree-viewer.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-genealogy-genealogy-tree-viewer`
**Application:** Genealogy  
**Capability group:** Genealogy Tree Viewer  
**Source scope:** [GENEALOGY.md](../GENEALOGY.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Genealogy Tree Viewer module owns genealogy tree viewer domain behavior. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Pedigree:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Descendants:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Fan/chart views:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Navigation:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Filters:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Large-tree rendering:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-genealogy-genealogy-tree-viewer-filament`, `module-genealogy-genealogy-tree-viewer-livewire`, and `module-genealogy-genealogy-tree-viewer-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify genealogy tree viewer across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
| **Pedigree** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `pedigree`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Descendants** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `descendants`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Fan/chart views** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `fan/chart views`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Navigation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `navigation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Filters** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `filters`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Large-tree rendering** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `large-tree rendering`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/genealogy-tree-viewer.md) | [Source map](../SOURCE-MAPPING.md#genealogy-tree-viewer) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/genealogy-tree-viewer.md) | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/genealogy-tree-viewer.md) | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) · [`module-genealogy-tree-viewer-filament`](https://github.com/liberusoftware/module-genealogy-tree-viewer-filament) (`liberusoftware/genealogy-tree-viewer-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/genealogy-tree-viewer.md) | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/genealogy-tree-viewer.md) | [`project-genealogy-laravel-inertia-react`](https://github.com/liberusoftware/project-genealogy-laravel-inertia-react) · [`module-genealogy-tree-viewer-react-inertia`](https://github.com/liberusoftware/module-genealogy-tree-viewer-react-inertia) (`@liberusoftware/module-genealogy-tree-viewer-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/genealogy-tree-viewer.md) | [`project-genealogy-laravel-inertia-vue`](https://github.com/liberusoftware/project-genealogy-laravel-inertia-vue) · [`module-genealogy-tree-viewer-vue-inertia`](https://github.com/liberusoftware/module-genealogy-tree-viewer-vue-inertia) (`@liberusoftware/module-genealogy-tree-viewer-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/genealogy-tree-viewer.md) | [`project-genealogy-nuxt-vue`](https://github.com/liberusoftware/project-genealogy-nuxt-vue) · [`module-genealogy-tree-viewer-nuxt`](https://github.com/liberusoftware/module-genealogy-tree-viewer-nuxt) (`@liberusoftware/module-genealogy-tree-viewer-nuxt`) | Standalone Vue SSR client consuming `project-genealogy-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/genealogy-tree-viewer.md) | [`project-genealogy-next-react`](https://github.com/liberusoftware/project-genealogy-next-react) · [`module-genealogy-tree-viewer-nextjs`](https://github.com/liberusoftware/module-genealogy-tree-viewer-nextjs) (`@liberusoftware/module-genealogy-tree-viewer-nextjs`) | App Router Server/Client components consuming `project-genealogy-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/genealogy-tree-viewer.md) | [`project-genealogy-mobile-react`](https://github.com/liberusoftware/project-genealogy-mobile-react) · [`module-genealogy-tree-viewer-react-native`](https://github.com/liberusoftware/module-genealogy-tree-viewer-react-native) (`@liberusoftware/module-genealogy-tree-viewer-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/genealogy-tree-viewer.md) | [`project-genealogy-mobile-flutter`](https://github.com/liberusoftware/project-genealogy-mobile-flutter) · [`module-genealogy-tree-viewer-flutter`](https://github.com/liberusoftware/module-genealogy-tree-viewer-flutter) (`module_genealogy_tree_viewer_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/genealogy-tree-viewer.md) | [`project-genealogy-dart-mobile`](https://github.com/liberusoftware/project-genealogy-dart-mobile) · [`module-genealogy-tree-viewer-dart-mobile`](https://github.com/liberusoftware/module-genealogy-tree-viewer-dart-mobile) (`module_genealogy_tree_viewer_dart_mobile`)<br>[`project-genealogy-dart-desktop`](https://github.com/liberusoftware/project-genealogy-dart-desktop) · [`module-genealogy-tree-viewer-dart-desktop`](https://github.com/liberusoftware/module-genealogy-tree-viewer-dart-desktop) (`module_genealogy_tree_viewer_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
