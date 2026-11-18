# Accounting: Bill Payments

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#bill-payments). Observed identity: [`liberusoftware/module-accounting-bill-payments`](../../../modules/source/liberusoftware--module-accounting-bill-payments.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-accounting-bill-payments`
**Application:** Accounting  
**Capability group:** Purchasing and payables modules  
**Source scope:** [ACCOUNTING.md](../ACCOUNTING.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Bill Payments module owns Payment proposals, due-date/discount optimization, bank details validation, maker-checker approval, files/APIs, remittances, and status. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Payment proposals:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Due-date/discount optimization:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Bank details validation:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Maker-checker approval:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Files/APIs:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Remittances:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Status:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

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

- Provide matching optional presentation packages only when required: `module-accounting-bill-payments-filament`, `module-accounting-bill-payments-livewire`, and `module-accounting-bill-payments-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify payment proposals across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify due-date/discount optimization across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify bank details validation across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify maker-checker approval across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify files/APIs across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify remittances across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify status across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
| **Payment proposals** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `payment proposals`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Due-date/discount optimization** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `due-date/discount optimization`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Bank details validation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `bank details validation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Maker-checker approval** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `maker-checker approval`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Files/APIs** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `files/apis`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Remittances** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `remittances`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Status** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `status`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/bill-payments.md) | [Source map](../SOURCE-MAPPING.md#bill-payments) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/bill-payments.md) | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/bill-payments.md) | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) · [`module-accounting-bill-payments-filament`](https://github.com/liberusoftware/module-accounting-bill-payments-filament) (`liberusoftware/accounting-bill-payments-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/bill-payments.md) | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/bill-payments.md) | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) · [`module-accounting-bill-payments-react-inertia`](https://github.com/liberusoftware/module-accounting-bill-payments-react-inertia) (`@liberusoftware/module-accounting-bill-payments-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/bill-payments.md) | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) · [`module-accounting-bill-payments-vue-inertia`](https://github.com/liberusoftware/module-accounting-bill-payments-vue-inertia) (`@liberusoftware/module-accounting-bill-payments-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/bill-payments.md) | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) · [`module-accounting-bill-payments-nuxt`](https://github.com/liberusoftware/module-accounting-bill-payments-nuxt) (`@liberusoftware/module-accounting-bill-payments-nuxt`) | Standalone Vue SSR client consuming `project-accounting-erp-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/bill-payments.md) | [`project-accounting-erp-next-react`](https://github.com/liberusoftware/project-accounting-erp-next-react) · [`module-accounting-bill-payments-nextjs`](https://github.com/liberusoftware/module-accounting-bill-payments-nextjs) (`@liberusoftware/module-accounting-bill-payments-nextjs`) | App Router Server/Client components consuming `project-accounting-erp-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/bill-payments.md) | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) · [`module-accounting-bill-payments-react-native`](https://github.com/liberusoftware/module-accounting-bill-payments-react-native) (`@liberusoftware/module-accounting-bill-payments-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/bill-payments.md) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) · [`module-accounting-bill-payments-flutter`](https://github.com/liberusoftware/module-accounting-bill-payments-flutter) (`module_accounting_bill_payments_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/bill-payments.md) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) · `module-accounting-bill-payments-dart-mobile` (`module_accounting_bill_payments_dart_mobile`)<br>[`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) · `module-accounting-bill-payments-dart-desktop` (`module_accounting_bill_payments_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
