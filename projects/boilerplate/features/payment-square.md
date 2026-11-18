# Boilerplate: Payment Square Adapter

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payment-square). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-boilerplate-payment-square`
**Intended package identity:** `liberusoftware/payment-square`
**Extends / implements contracts:** `liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)`
**Application:** Boilerplate  
**Capability group:** Unified merchant payment adapters  
**Source scope:** [BOILERPLATE.md](../BOILERPLATE.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Payment Square Adapter module owns Square commerce and POS payment provider adapter extending liberusoftware/payment-contracts for Square Web Payments SDK, In-App Payments, Cards on File, Cash App Pay, Afterpay, delayed-capture authorizations, refunds, Square Terminal hardware checkouts, disputes API, payout entries reconciliation, and x-square-hmacsha256-signature webhook verification. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Square Payments API and Web Payments SDK tokenization:** Implement PaymentIntentServiceContract for tokenized card/wallet/Cash App Pay nonces, buyer verification (3DS/SCA), and location-scoped payments.
- **Delayed capture, CompletePayment, CancelPayment, and Refunds:** Implement PaymentCaptureAndRefundContract with Square idempotency_key enforcement for partial/full captures, voids, and PaymentRefunds.
- **Square Cards on File and customer vaulting:** Implement SavedPaymentMethodVaultContract for storing, disabling, and charging customer Cards on File across web, mobile, and POS.
- **Square Terminal API and in-person POS hardware bridge:** Implement POSHardwareTerminalContract for TerminalCheckout creation, device pairing status, and card-present receipt correlation.
- **HMAC-SHA256 webhook verification, Disputes API, and Payouts:** Implement MerchantWebhookVerifierContract (`x-square-hmacsha256-signature`), DisputeAndChargebackHandlerContract, and PayoutAndSettlementReconcilerContract.

## 3. Ownership and contract boundaries

- **Contract alignment:** Implements and/or exposes `liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)` as defined in [PAYMENTS.md](../../../architecture/PAYMENTS.md). Consuming repositories depend on the contract boundary rather than coupling to internal models or vendor SDKs.
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

- Provide matching optional presentation packages only when required: `module-boilerplate-payment-square-filament`, `module-boilerplate-payment-square-livewire`, `module-boilerplate-payment-square-api`, `module-boilerplate-payment-square-react-inertia`, `module-boilerplate-payment-square-vue-inertia`, `module-boilerplate-payment-square-nuxt`, `module-boilerplate-payment-square-nextjs`, `module-boilerplate-payment-square-react-native`, and `module-boilerplate-payment-square-flutter`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify square payments api and web payments sdk tokenization across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify delayed capture, completepayment, cancelpayment, and refunds across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify square cards on file and customer vaulting across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify square terminal api and in-person pos hardware bridge across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify hmac-sha256 webhook verification, disputes api, and payouts across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Add unit tests for pure rules/value objects and feature tests for actions, policies, validation, persistence, events, jobs, and module lifecycle.
- Add architecture tests for forbidden dependencies, `App\` coupling, provider leakage, private cross-module access, and presentation dependencies.
- Add migration/upgrade, contract, compatibility, security, performance, failure/recovery, and minimal-host installation tests as risk requires.
- Run the independent Pest 5 suite through repository-owned Composer scripts and the shared package testbench; meaningful owned PHP targets 100% line coverage without excluding difficult code.
- Run composition tests in representative host applications while keeping this repository's suite authoritative for module behavior.

## 7. Definition of done

- Every feature in scope has explicit acceptance criteria, permissions, tenant behavior, persistence ownership, events, failure handling, telemetry, and tests.
- Public contracts (`liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)`) and presentation extension points are versioned and documented.
- Install, enable, disable, upgrade, retry/recovery, and uninstall/retention behavior is verified.
- Security, accessibility where presented, compatibility, architecture, and 100% meaningful-PHP coverage gates pass.
- README, changelog, migration guidance, runbook, CI evidence, and tagged release are available from the independent repository.

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Square Payments API and Web Payments SDK tokenization** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `square payments api and web payments sdk tokenization`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Delayed capture, CompletePayment, CancelPayment, and Refunds** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `delayed capture, completepayment, cancelpayment, and refunds`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Square Cards on File and customer vaulting** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `square cards on file and customer vaulting`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Square Terminal API and in-person POS hardware bridge** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `square terminal api and in-person pos hardware bridge`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **HMAC-SHA256 webhook verification, Disputes API, and Payouts** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `hmac-sha256 webhook verification, disputes api, and payouts`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/payment-square.md) | [Source map](../SOURCE-MAPPING.md#payment-square) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/payment-square.md) | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/payment-square.md) | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) · `module-boilerplate-payment-square-filament` | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/payment-square.md) | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/payment-square.md) | [`project-boilerplate-laravel-inertia-react`](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · `module-boilerplate-payment-square-react-inertia` | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/payment-square.md) | [`project-boilerplate-laravel-inertia-vue`](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · `module-boilerplate-payment-square-vue-inertia` | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/payment-square.md) | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · `module-boilerplate-payment-square-nuxt` | Standalone Vue SSR client consuming `project-boilerplate-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/payment-square.md) | [`project-boilerplate-next-react`](https://github.com/liberusoftware/project-boilerplate-next-react) · `module-boilerplate-payment-square-nextjs` | App Router Server/Client components consuming `project-boilerplate-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/payment-square.md) | [`project-boilerplate-mobile-react`](https://github.com/liberusoftware/project-boilerplate-mobile-react) · `module-boilerplate-payment-square-react-native` | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/payment-square.md) | [`project-boilerplate-mobile-flutter`](https://github.com/liberusoftware/project-boilerplate-mobile-flutter) · `module-boilerplate-payment-square-flutter` | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/payment-square.md) | [`project-boilerplate-dart-mobile`](https://github.com/liberusoftware/project-boilerplate-dart-mobile) · `module-boilerplate-payment-square-dart-mobile`<br>[`project-boilerplate-dart-desktop`](https://github.com/liberusoftware/project-boilerplate-dart-desktop) · `module-boilerplate-payment-square-dart-desktop` | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
