# Automation: Evaluation

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#evaluation). Observed identity: [`liberusoftware/automation-evaluation`](../../../modules/source/liberusoftware--automation-evaluation.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-automation-evaluation`
**Application:** Automation
**Capability group:** Module plan
**Source scope:** [AUTOMATION.md](../AUTOMATION.md)
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Evaluation module owns Quality suites, regression comparison, latency/cost metrics, safety checks, and release gates. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Quality suites:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Regression comparison:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Latency/cost metrics:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Safety checks:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Release gates:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

## 3. Ownership and boundaries

- Own the capability's domain rules, policies, actions, queries, events, persistence, migrations, configuration, audit semantics, and failure recovery.
- Expose stable contracts, immutable DTOs/read models, commands, queries, and past-tense domain events where other modules have a legitimate integration need.
- Consume identity, organizations/teams, authorization, settings, files, notifications, queues, localization, currency, and observability from the shared foundation rather than duplicating them.
  -…34272 tokens truncated…to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Quality suites** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `quality suites`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Regression comparison** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `regression comparison`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Latency/cost metrics** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `latency/cost metrics`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Safety checks** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `safety checks`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Release gates** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `release gates`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/evaluation.md) | [Source map](../SOURCE-MAPPING.md#evaluation) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/evaluation.md) | [`project-automation-laravel-api`](https://github.com/liberusoftware/project-automation-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/evaluation.md) | [`project-automation-laravel-filament`](https://github.com/liberusoftware/project-automation-laravel-filament) · [`module-automation-evaluation-filament`](https://github.com/liberusoftware/module-automation-evaluation-filament) (`liberusoftware/automation-evaluation-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/evaluation.md) | [`project-automation-laravel-filament`](https://github.com/liberusoftware/project-automation-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/evaluation.md) | [`project-automation-laravel-inertia-react`](https://github.com/liberusoftware/project-automation-laravel-inertia-react) · [`module-automation-evaluation-react-inertia`](https://github.com/liberusoftware/module-automation-evaluation-react-inertia) (`@liberusoftware/module-automation-evaluation-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/evaluation.md) | [`project-automation-laravel-inertia-vue`](https://github.com/liberusoftware/project-automation-laravel-inertia-vue) · [`module-automation-evaluation-vue-inertia`](https://github.com/liberusoftware/module-automation-evaluation-vue-inertia) (`@liberusoftware/module-automation-evaluation-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/evaluation.md) | [`project-automation-nuxt-vue`](https://github.com/liberusoftware/project-automation-nuxt-vue) · [`module-automation-evaluation-nuxt`](https://github.com/liberusoftware/module-automation-evaluation-nuxt) (`@liberusoftware/module-automation-evaluation-nuxt`) | Standalone Vue SSR client consuming `project-automation-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/evaluation.md) | [`project-automation-next-react`](https://github.com/liberusoftware/project-automation-next-react) · [`module-automation-evaluation-nextjs`](https://github.com/liberusoftware/module-automation-evaluation-nextjs) (`@liberusoftware/module-automation-evaluation-nextjs`) | App Router Server/Client components consuming `project-automation-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/evaluation.md) | [`project-automation-mobile-react`](https://github.com/liberusoftware/project-automation-mobile-react) · [`module-automation-evaluation-react-native`](https://github.com/liberusoftware/module-automation-evaluation-react-native) (`@liberusoftware/module-automation-evaluation-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/evaluation.md) | [`project-automation-mobile-flutter`](https://github.com/liberusoftware/project-automation-mobile-flutter) · [`module-automation-evaluation-flutter`](https://github.com/liberusoftware/module-automation-evaluation-flutter) (`module_automation_evaluation_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/evaluation.md) | [`project-automation-dart-mobile`](https://github.com/liberusoftware/project-automation-dart-mobile) · [`module-automation-evaluation-dart-mobile`](https://github.com/liberusoftware/module-automation-evaluation-dart-mobile) (`module_automation_evaluation_dart_mobile`)<br>[`project-automation-dart-desktop`](https://github.com/liberusoftware/project-automation-dart-desktop) · [`module-automation-evaluation-dart-desktop`](https://github.com/liberusoftware/module-automation-evaluation-dart-desktop) (`module_automation_evaluation_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
