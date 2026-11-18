# Social Network: Currency Context

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#currency-context). Observed identity: [`liberusoftware/currency-context`](../../../modules/source/liberusoftware--currency-context.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-social-network-currency-context`
**Application:** Social Network  
**Capability group:** Currency Context  
**Source scope:** [SOCIAL-NETWORK.md](../SOCIAL-NETWORK.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Currency Context module owns currency context domain behavior. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Currency metadata:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Preferences:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Precision:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Formatting:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Exchange-rate contracts:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Context:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-social-network-currency-context-filament`, `module-social-network-currency-context-livewire`, and `module-social-network-currency-context-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify currency context across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
| **Currency metadata** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `currency metadata`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Preferences** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `preferences`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Precision** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `precision`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Formatting** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `formatting`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Exchange-rate contracts** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `exchange-rate contracts`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Context** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `context`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/currency-context.md) | [Source map](../SOURCE-MAPPING.md#currency-context) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/currency-context.md) | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/currency-context.md) | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) · [`module-currency-context-filament`](https://github.com/liberusoftware/module-currency-context-filament) (`liberusoftware/currency-context-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/currency-context.md) | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/currency-context.md) | [`project-social-network-laravel-inertia-react`](https://github.com/liberusoftware/project-social-network-laravel-inertia-react) · [`module-currency-context-react-inertia`](https://github.com/liberusoftware/module-currency-context-react-inertia) (`@liberusoftware/module-currency-context-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/currency-context.md) | [`project-social-network-laravel-inertia-vue`](https://github.com/liberusoftware/project-social-network-laravel-inertia-vue) · [`module-currency-context-vue-inertia`](https://github.com/liberusoftware/module-currency-context-vue-inertia) (`@liberusoftware/module-currency-context-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/currency-context.md) | [`project-social-network-nuxt-vue`](https://github.com/liberusoftware/project-social-network-nuxt-vue) · [`module-currency-context-nuxt`](https://github.com/liberusoftware/module-currency-context-nuxt) (`@liberusoftware/module-currency-context-nuxt`) | Standalone Vue SSR client consuming `project-social-network-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/currency-context.md) | [`project-social-network-next-react`](https://github.com/liberusoftware/project-social-network-next-react) · [`module-currency-context-nextjs`](https://github.com/liberusoftware/module-currency-context-nextjs) (`@liberusoftware/module-currency-context-nextjs`) | App Router Server/Client components consuming `project-social-network-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/currency-context.md) | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) · [`module-currency-context-react-native`](https://github.com/liberusoftware/module-currency-context-react-native) (`@liberusoftware/module-currency-context-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/currency-context.md) | [`project-social-network-mobile-flutter`](https://github.com/liberusoftware/project-social-network-mobile-flutter) · [`module-currency-context-flutter`](https://github.com/liberusoftware/module-currency-context-flutter) (`module_currency_context_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/currency-context.md) | [`project-social-network-dart-mobile`](https://github.com/liberusoftware/project-social-network-dart-mobile) · [`module-currency-context-dart-mobile`](https://github.com/liberusoftware/module-currency-context-dart-mobile) (`module_currency_context_dart_mobile`)<br>[`project-social-network-dart-desktop`](https://github.com/liberusoftware/project-social-network-dart-desktop) · [`module-currency-context-dart-desktop`](https://github.com/liberusoftware/module-currency-context-dart-desktop) (`module_currency_context_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
