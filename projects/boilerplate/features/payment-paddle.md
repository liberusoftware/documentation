# Boilerplate: Payment Paddle Adapter

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payment-paddle). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-boilerplate-payment-paddle`
**Intended package identity:** `liberusoftware/payment-paddle`
**Extends / implements contracts:** `liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)`
**Application:** Boilerplate  
**Capability group:** Unified merchant payment adapters  
**Source scope:** [BOILERPLATE.md](../BOILERPLATE.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Payment Paddle Adapter module owns Paddle Billing Merchant-of-Record provider adapter extending liberusoftware/payment-contracts and bridging liberusoftware/billing-paddle for global tax-inclusive/exclusive transactions, Paddle.js overlay/inline checkout, saved payment methods, subscription billing bridge, credit/refund adjustments, chargeback write-offs, payout fee/tax reconciliation, and Paddle-Signature webhook verification. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Paddle Billing transactions and Merchant-of-Record checkout:** Implement PaymentIntentServiceContract for Paddle transactions, localized tax calculation, and Paddle.js client transaction tokens.
- **Paddle adjustments for full/partial refunds and credits:** Implement PaymentCaptureAndRefundContract mapping Paddle transaction capture and refund/credit adjustment workflows.
- **Customer saved payment methods and subscription bridge:** Implement SavedPaymentMethodVaultContract for Paddle customer payment methods and recurring subscription renewal synchronization.
- **Paddle-Signature ts/h1 HMAC webhook verification:** Implement MerchantWebhookVerifierContract validating Paddle-Signature timestamp and HMAC-SHA256 digest over raw request bytes.
- **Tax, Merchant-of-Record fee, and payout reconciliation:** Implement PayoutAndSettlementReconcilerContract capturing Paddle MoR tax remittance, processing fees, chargebacks, and payout remittances.

## 3. Ownership and contract boundaries

- **Contract alignment:** Implements and/or exposes `liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)` as defined in [PAYMENTS.md](../../../architecture/PAYMENTS.md). Consuming repositories depend on the contract boundary rather than coupling to internal models or vendor SDKs.
- Own the capability's domain rules, policies, actions, queries, events, persistence, migrations, configuration, audit semantics, and failure recovery.
- Expose stable contracts, immutable DTOs/read models, commands, queries, and past-tense domain events where other modules have a legitimate integration need.
- Consume identity, organizations/teams, authorization, settings, files, notifications, queues, localization, currency, and observability from the shared foundation rather than duplicating them.
- Never depend on an application's `App\` classes, another module's private tables/models, a provider SDK in provider-neutral code, or an optional presentation framework.
- Keep Filament, Livewire, Inertia, Next.js, Nuxt, Mobile, and HTTP API logic in matching one-to-one presentation packages when those surfaces are required.

## 4. Implementation strategy

### Domain model

- Define aggregates, entities, value objects, enums, invariants, lifecycle states, and transition rules using the terminology in this specification and [PAYMENTS.md](../../../architecture/PAYMENTS.md).
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

- Provide matching optional presentation packages only when required: `module-boilerplate-payment-paddle-filament`, `module-boilerplate-payment-paddle-livewire`, `module-boilerplate-payment-paddle-api`, `module-boilerplate-payment-paddle-react-inertia`, `module-boilerplate-payment-paddle-vue-inertia`, `module-boilerplate-payment-paddle-nuxt`, `module-boilerplate-payment-paddle-nextjs`, `module-boilerplate-payment-paddle-react-native`, and `module-boilerplate-payment-paddle-flutter`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify paddle billing transactions and merchant-of-record checkout across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify paddle adjustments for full/partial refunds and credits across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify customer saved payment methods and subscription bridge across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify paddle-signature ts/h1 hmac webhook verification across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify tax, merchant-of-record fee, and payout reconciliation across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Add unit tests for pure rules/value objects and feature tests for actions, policies, validation, persistence, events, jobs, and module lifecycle.
- Add architecture tests for forbidden dependencies, `App\` coupling, provider leakage, private cross-module access, and presentation dependencies.
- Add migration/upgrade, contract, compatibility, security, performance, failure/recovery, and minimal-host installation tests as risk requires.
- Run the independent Pest 5 suite through repository-owned Composer scripts and the shared package testbench; meaningful owned PHP targets 100% line coverage without excluding difficult code.
- Run composition tests in representative host applications while keeping this repository's suite authoritative for module behavior.

## 7. Definition of done

- Every feature in scope has explicit acceptance criteria, permissions, tenant behavior, persistence ownership, events, failure handling, telemetry, and tests.
- Public contracts (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract)`) and presentation extension points are versioned and documented.
- Install, enable, disable, upgrade, retry/recovery, and uninstall/retention behavior is verified.
- Security, accessibility where presented, compatibility, architecture, and 100% meaningful-PHP coverage gates pass.
- README, changelog, migration guidance, runbook, CI evidence, and tagged release are available from the independent repository.

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Paddle Billing transactions and Merchant-of-Record checkout** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `paddle billing transactions and merchant-of-record checkout`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Paddle adjustments for full/partial refunds and credits** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `paddle adjustments for full/partial refunds and credits`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Customer saved payment methods and subscription bridge** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `customer saved payment methods and subscription bridge`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Paddle-Signature ts/h1 HMAC webhook verification** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `paddle-signature ts/h1 hmac webhook verification`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Tax, Merchant-of-Record fee, and payout reconciliation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `tax, merchant-of-record fee, and payout reconciliation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/payment-paddle.md) | [Source map](../SOURCE-MAPPING.md#payment-paddle) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/payment-paddle.md) | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/payment-paddle.md) | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) · `module-boilerplate-payment-paddle-filament` | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/payment-paddle.md) | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/payment-paddle.md) | [`project-boilerplate-laravel-inertia-react`](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · `module-boilerplate-payment-paddle-react-inertia` | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/payment-paddle.md) | [`project-boilerplate-laravel-inertia-vue`](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · `module-boilerplate-payment-paddle-vue-inertia` | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/payment-paddle.md) | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · `module-boilerplate-payment-paddle-nuxt` | Standalone Vue SSR client consuming `project-boilerplate-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/payment-paddle.md) | [`project-boilerplate-next-react`](https://github.com/liberusoftware/project-boilerplate-next-react) · `module-boilerplate-payment-paddle-nextjs` | App Router Server/Client components consuming `project-boilerplate-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/payment-paddle.md) | [`project-boilerplate-mobile-react`](https://github.com/liberusoftware/project-boilerplate-mobile-react) · `module-boilerplate-payment-paddle-react-native` | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/payment-paddle.md) | [`project-boilerplate-mobile-flutter`](https://github.com/liberusoftware/project-boilerplate-mobile-flutter) · `module-boilerplate-payment-paddle-flutter` | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/payment-paddle.md) | [`project-boilerplate-dart-mobile`](https://github.com/liberusoftware/project-boilerplate-dart-mobile) · `module-boilerplate-payment-paddle-dart-mobile`<br>[`project-boilerplate-dart-desktop`](https://github.com/liberusoftware/project-boilerplate-dart-desktop) · `module-boilerplate-payment-paddle-dart-desktop` | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
