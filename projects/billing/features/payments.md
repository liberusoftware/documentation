# Billing: Payments

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payments). Observed identity: [`liberusoftware/module-billing-payments`](../../../modules/source/liberusoftware--module-billing-payments.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-billing-payments`
**Extends / implements contracts:** `liberusoftware/payment-contracts, liberusoftware/payment-core`
**Application:** Billing  
**Capability group:** Module plan  
**Source scope:** [BILLING.md](../BILLING.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)

## 1. Purpose

The Payments module owns Methods, mandates, gateway drivers, capture, allocation, refunds, disputes, and reconciliation. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Unified payment-contracts and payment-core integration:** Delegate gateway driver resolution to liberusoftware/payment-core and provider adapters (payment-stripe, payment-paypal, payment-paddle, payment-adyen, payment-mollie, payment-square, payment-gocardless) implementing liberusoftware/payment-contracts.
- **Methods and vaulted payment instruments:** Manage customer cards, wallets, and payment tokens through SavedPaymentMethodVaultContract without storing raw cardholder data.
- **Mandates and Direct Debit lifecycles:** Manage SEPA, Bacs, ACH, and recurring billing mandates across GoCardless, Stripe, Mollie, and Adyen adapters.
- **Gateway drivers and capability discovery:** Bridge GatewayManager with PaymentGatewayAdapterContract capability descriptors, credential health checks, and tenant/currency routing.
- **Capture, partial invoice payments, and allocation:** Execute authorized captures via PaymentCaptureAndRefundContract and allocate funds across invoices and account balances.
- **Refunds and credit reversals:** Execute full and partial refunds with deterministic idempotency keys and approval policies.
- **Disputes and chargeback evidence:** Track provider disputes via DisputeAndChargebackHandlerContract, evidence deadlines, and win/loss accounting adjustments.
- **Reconciliation and settlement batches:** Reconcile local payment records against provider balance transactions, fees, and payout batches via PayoutAndSettlementReconcilerContract.

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

- Provide matching optional presentation packages only when required: `module-billing-payments-filament`, `module-billing-payments-livewire`, and `module-billing-payments-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify methods across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify mandates across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify gateway drivers across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify capture across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify allocation across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify refunds across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify disputes across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify reconciliation across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
| **Unified payment-contracts and payment-core integration** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `unified payment-contracts and payment-core integration`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Methods and vaulted payment instruments** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `methods and vaulted payment instruments`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Mandates and Direct Debit lifecycles** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `mandates and direct debit lifecycles`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Gateway drivers and capability discovery** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `gateway drivers and capability discovery`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Capture, partial invoice payments, and allocation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `capture, partial invoice payments, and allocation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Refunds and credit reversals** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `refunds and credit reversals`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Disputes and chargeback evidence** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `disputes and chargeback evidence`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Reconciliation and settlement batches** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `reconciliation and settlement batches`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/payments.md) | [Source map](../SOURCE-MAPPING.md#payments) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/payments.md) | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/payments.md) | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) · [`module-billing-payments-filament`](https://github.com/liberusoftware/module-billing-payments-filament) (`liberusoftware/billing-payments-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/payments.md) | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/payments.md) | [`project-billing-laravel-inertia-react`](https://github.com/liberusoftware/project-billing-laravel-inertia-react) · [`module-billing-payments-react-inertia`](https://github.com/liberusoftware/module-billing-payments-react-inertia) (`@liberusoftware/module-billing-payments-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/payments.md) | [`project-billing-laravel-inertia-vue`](https://github.com/liberusoftware/project-billing-laravel-inertia-vue) · [`module-billing-payments-vue-inertia`](https://github.com/liberusoftware/module-billing-payments-vue-inertia) (`@liberusoftware/module-billing-payments-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/payments.md) | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) · [`module-billing-payments-nuxt`](https://github.com/liberusoftware/module-billing-payments-nuxt) (`@liberusoftware/module-billing-payments-nuxt`) | Standalone Vue SSR client consuming `project-billing-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/payments.md) | [`project-billing-next-react`](https://github.com/liberusoftware/project-billing-next-react) · [`module-billing-payments-nextjs`](https://github.com/liberusoftware/module-billing-payments-nextjs) (`@liberusoftware/module-billing-payments-nextjs`) | App Router Server/Client components consuming `project-billing-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/payments.md) | [`project-billing-mobile-react`](https://github.com/liberusoftware/project-billing-mobile-react) · [`module-billing-payments-react-native`](https://github.com/liberusoftware/module-billing-payments-react-native) (`@liberusoftware/module-billing-payments-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/payments.md) | [`project-billing-mobile-flutter`](https://github.com/liberusoftware/project-billing-mobile-flutter) · [`module-billing-payments-flutter`](https://github.com/liberusoftware/module-billing-payments-flutter) (`module_billing_payments_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/payments.md) | [`project-billing-dart-mobile`](https://github.com/liberusoftware/project-billing-dart-mobile) · [`module-billing-payments-dart-mobile`](https://github.com/liberusoftware/module-billing-payments-dart-mobile) (`module_billing_payments_dart_mobile`)<br>[`project-billing-dart-desktop`](https://github.com/liberusoftware/project-billing-dart-desktop) · [`module-billing-payments-dart-desktop`](https://github.com/liberusoftware/module-billing-payments-dart-desktop) (`module_billing_payments_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
