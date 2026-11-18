# Billing: Module Billing Customer Portal

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-customer-portal). Observed identity: [`liberusoftware/module-billing-customer-portal`](../../../modules/source/liberusoftware--module-billing-customer-portal.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-billing-module-billing-customer-portal`
**Application:** Billing  
**Capability group:** Module Billing Customer Portal  
**Source scope:** [BILLING.md](../BILLING.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Module Billing Customer Portal module owns module billing customer portal domain behavior. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Profile:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Orders:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Services:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Usage:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Invoices:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Payments:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Tickets:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Changes:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Cancellation:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-billing-module-billing-customer-portal-filament`, `module-billing-module-billing-customer-portal-livewire`, and `module-billing-module-billing-customer-portal-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify module billing customer portal across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
| **Profile** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `profile`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Orders** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `orders`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Services** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `services`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Usage** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `usage`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Invoices** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `invoices`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Payments** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `payments`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Tickets** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `tickets`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Changes** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `changes`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Cancellation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `cancellation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/module-billing-customer-portal.md) | [Source map](../SOURCE-MAPPING.md#module-billing-customer-portal) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/module-billing-customer-portal.md) | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/module-billing-customer-portal.md) | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) · [`module-billing-customer-portal-filament`](https://github.com/liberusoftware/module-billing-customer-portal-filament) (`liberusoftware/billing-customer-portal-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/module-billing-customer-portal.md) | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/module-billing-customer-portal.md) | [`project-billing-laravel-inertia-react`](https://github.com/liberusoftware/project-billing-laravel-inertia-react) · [`module-billing-customer-portal-react-inertia`](https://github.com/liberusoftware/module-billing-customer-portal-react-inertia) (`@liberusoftware/module-billing-customer-portal-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/module-billing-customer-portal.md) | [`project-billing-laravel-inertia-vue`](https://github.com/liberusoftware/project-billing-laravel-inertia-vue) · [`module-billing-customer-portal-vue-inertia`](https://github.com/liberusoftware/module-billing-customer-portal-vue-inertia) (`@liberusoftware/module-billing-customer-portal-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/module-billing-customer-portal.md) | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) · [`module-billing-customer-portal-nuxt`](https://github.com/liberusoftware/module-billing-customer-portal-nuxt) (`@liberusoftware/module-billing-customer-portal-nuxt`) | Standalone Vue SSR client consuming `project-billing-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/module-billing-customer-portal.md) | [`project-billing-next-react`](https://github.com/liberusoftware/project-billing-next-react) · [`module-billing-customer-portal-nextjs`](https://github.com/liberusoftware/module-billing-customer-portal-nextjs) (`@liberusoftware/module-billing-customer-portal-nextjs`) | App Router Server/Client components consuming `project-billing-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/module-billing-customer-portal.md) | [`project-billing-mobile-react`](https://github.com/liberusoftware/project-billing-mobile-react) · [`module-billing-customer-portal-react-native`](https://github.com/liberusoftware/module-billing-customer-portal-react-native) (`@liberusoftware/module-billing-customer-portal-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/module-billing-customer-portal.md) | [`project-billing-mobile-flutter`](https://github.com/liberusoftware/project-billing-mobile-flutter) · [`module-billing-customer-portal-flutter`](https://github.com/liberusoftware/module-billing-customer-portal-flutter) (`module_billing_customer_portal_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/module-billing-customer-portal.md) | [`project-billing-dart-mobile`](https://github.com/liberusoftware/project-billing-dart-mobile) · [`module-billing-customer-portal-dart-mobile`](https://github.com/liberusoftware/module-billing-customer-portal-dart-mobile) (`module_billing_customer_portal_dart_mobile`)<br>[`project-billing-dart-desktop`](https://github.com/liberusoftware/project-billing-dart-desktop) · [`module-billing-customer-portal-dart-desktop`](https://github.com/liberusoftware/module-billing-customer-portal-dart-desktop) (`module_billing_customer_portal_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
