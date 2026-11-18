# Ecommerce: Categories and Navigation

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#categories-and-navigation). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-ecommerce-categories-and-navigation`
**Application:** Ecommerce  
**Capability group:** Product information and catalog modules  
**Source scope:** [ECOMMERCE.md](../ECOMMERCE.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Categories and Navigation module owns Hierarchies, menus, landing references, layered navigation, permissions, merchandising positions, and redirects. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Hierarchies:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Menus:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Landing references:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Layered navigation:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Permissions:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Merchandising positions:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Redirects:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-ecommerce-categories-and-navigation-filament`, `module-ecommerce-categories-and-navigation-livewire`, and `module-ecommerce-categories-and-navigation-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify hierarchies across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify menus across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify landing references across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify layered navigation across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify permissions across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify merchandising positions across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify redirects across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
| **Hierarchies** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `hierarchies`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Menus** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `menus`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Landing references** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `landing references`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Layered navigation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `layered navigation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Permissions** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `permissions`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Merchandising positions** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `merchandising positions`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Redirects** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `redirects`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/categories-and-navigation.md) | [Source map](../SOURCE-MAPPING.md#categories-and-navigation) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/categories-and-navigation.md) | [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/categories-and-navigation.md) | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) · [`module-ecommerce-categories-and-navigation-filament`](https://github.com/liberusoftware/module-ecommerce-categories-and-navigation-filament) (`liberusoftware/ecommerce-categories-and-navigation-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/categories-and-navigation.md) | [`project-ecommerce-laravel-filament`](https://github.com/liberusoftware/project-ecommerce-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/categories-and-navigation.md) | [`project-ecommerce-laravel-inertia-react`](https://github.com/liberusoftware/project-ecommerce-laravel-inertia-react) · [`module-ecommerce-categories-and-navigation-react-inertia`](https://github.com/liberusoftware/module-ecommerce-categories-and-navigation-react-inertia) (`@liberusoftware/module-ecommerce-categories-and-navigation-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/categories-and-navigation.md) | [`project-ecommerce-laravel-inertia-vue`](https://github.com/liberusoftware/project-ecommerce-laravel-inertia-vue) · [`module-ecommerce-categories-and-navigation-vue-inertia`](https://github.com/liberusoftware/module-ecommerce-categories-and-navigation-vue-inertia) (`@liberusoftware/module-ecommerce-categories-and-navigation-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/categories-and-navigation.md) | [`project-ecommerce-nuxt-vue`](https://github.com/liberusoftware/project-ecommerce-nuxt-vue) · [`module-ecommerce-categories-and-navigation-nuxt`](https://github.com/liberusoftware/module-ecommerce-categories-and-navigation-nuxt) (`@liberusoftware/module-ecommerce-categories-and-navigation-nuxt`) | Standalone Vue SSR client consuming `project-ecommerce-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/categories-and-navigation.md) | [`project-ecommerce-next-react`](https://github.com/liberusoftware/project-ecommerce-next-react) · [`module-ecommerce-categories-and-navigation-nextjs`](https://github.com/liberusoftware/module-ecommerce-categories-and-navigation-nextjs) (`@liberusoftware/module-ecommerce-categories-and-navigation-nextjs`) | App Router Server/Client components consuming `project-ecommerce-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/categories-and-navigation.md) | [`project-ecommerce-mobile-react`](https://github.com/liberusoftware/project-ecommerce-mobile-react) · [`module-ecommerce-categories-and-navigation-react-native`](https://github.com/liberusoftware/module-ecommerce-categories-and-navigation-react-native) (`@liberusoftware/module-ecommerce-categories-and-navigation-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/categories-and-navigation.md) | [`project-ecommerce-mobile-flutter`](https://github.com/liberusoftware/project-ecommerce-mobile-flutter) · [`module-ecommerce-categories-and-navigation-flutter`](https://github.com/liberusoftware/module-ecommerce-categories-and-navigation-flutter) (`module_ecommerce_categories_and_navigation_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/categories-and-navigation.md) | [`project-ecommerce-dart-mobile`](https://github.com/liberusoftware/project-ecommerce-dart-mobile) · [`module-ecommerce-categories-and-navigation-dart-mobile`](https://github.com/liberusoftware/module-ecommerce-categories-and-navigation-dart-mobile) (`module_ecommerce_categories_and_navigation_dart_mobile`)<br>[`project-ecommerce-dart-desktop`](https://github.com/liberusoftware/project-ecommerce-dart-desktop) · [`module-ecommerce-categories-and-navigation-dart-desktop`](https://github.com/liberusoftware/module-ecommerce-categories-and-navigation-dart-desktop) (`module_ecommerce_categories_and_navigation_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
