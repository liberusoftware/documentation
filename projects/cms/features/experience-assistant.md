# CMS: Experience Assistant

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#experience-assistant). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-cms-experience-assistant`
**Application:** CMS  
**Capability group:** Intelligence modules  
**Source scope:** [CMS.md](../CMS.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Experience Assistant module owns Layout/block suggestions, brand/design constraints, responsive/accessibility checks, preview, and approval. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Layout/block suggestions:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Brand/design constraints:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Responsive/accessibility checks:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Preview:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Approval:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-cms-experience-assistant-filament`, `module-cms-experience-assistant-livewire`, and `module-cms-experience-assistant-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify layout/block suggestions across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify brand/design constraints across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify responsive/accessibility checks across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify preview across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify approval across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
| **Layout/block suggestions** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `layout/block suggestions`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Brand/design constraints** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `brand/design constraints`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Responsive/accessibility checks** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `responsive/accessibility checks`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Preview** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `preview`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Approval** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `approval`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/experience-assistant.md) | [Source map](../SOURCE-MAPPING.md#experience-assistant) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/experience-assistant.md) | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/experience-assistant.md) | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) · [`module-cms-experience-assistant-filament`](https://github.com/liberusoftware/module-cms-experience-assistant-filament) (`liberusoftware/cms-experience-assistant-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/experience-assistant.md) | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/experience-assistant.md) | [`project-cms-laravel-inertia-react`](https://github.com/liberusoftware/project-cms-laravel-inertia-react) · [`module-cms-experience-assistant-react-inertia`](https://github.com/liberusoftware/module-cms-experience-assistant-react-inertia) (`@liberusoftware/module-cms-experience-assistant-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/experience-assistant.md) | [`project-cms-laravel-inertia-vue`](https://github.com/liberusoftware/project-cms-laravel-inertia-vue) · [`module-cms-experience-assistant-vue-inertia`](https://github.com/liberusoftware/module-cms-experience-assistant-vue-inertia) (`@liberusoftware/module-cms-experience-assistant-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/experience-assistant.md) | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) · [`module-cms-experience-assistant-nuxt`](https://github.com/liberusoftware/module-cms-experience-assistant-nuxt) (`@liberusoftware/module-cms-experience-assistant-nuxt`) | Standalone Vue SSR client consuming `project-cms-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/experience-assistant.md) | [`project-cms-next-react`](https://github.com/liberusoftware/project-cms-next-react) · [`module-cms-experience-assistant-nextjs`](https://github.com/liberusoftware/module-cms-experience-assistant-nextjs) (`@liberusoftware/module-cms-experience-assistant-nextjs`) | App Router Server/Client components consuming `project-cms-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/experience-assistant.md) | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) · [`module-cms-experience-assistant-react-native`](https://github.com/liberusoftware/module-cms-experience-assistant-react-native) (`@liberusoftware/module-cms-experience-assistant-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/experience-assistant.md) | [`project-cms-mobile-flutter`](https://github.com/liberusoftware/project-cms-mobile-flutter) · [`module-cms-experience-assistant-flutter`](https://github.com/liberusoftware/module-cms-experience-assistant-flutter) (`module_cms_experience_assistant_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/experience-assistant.md) | [`project-cms-dart-mobile`](https://github.com/liberusoftware/project-cms-dart-mobile) · [`module-cms-experience-assistant-dart-mobile`](https://github.com/liberusoftware/module-cms-experience-assistant-dart-mobile) (`module_cms_experience_assistant_dart_mobile`)<br>[`project-cms-dart-desktop`](https://github.com/liberusoftware/project-cms-dart-desktop) · [`module-cms-experience-assistant-dart-desktop`](https://github.com/liberusoftware/module-cms-experience-assistant-dart-desktop) (`module_cms_experience_assistant_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
