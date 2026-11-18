# Boilerplate: Payment Stripe Adapter

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payment-stripe). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-boilerplate-payment-stripe`
**Intended package identity:** `liberusoftware/payment-stripe`
**Extends / implements contracts:** `liberusoftware/payment-contracts (PaymentGatewayAdapterContract, PaymentIntentServiceContract, PaymentCaptureAndRefundContract, SavedPaymentMethodVaultContract, MerchantWebhookVerifierContract, DisputeAndChargebackHandlerContract, PayoutAndSettlementReconcilerContract, POSHardwareTerminalContract)`
**Application:** Boilerplate  
**Capability group:** Unified merchant payment adapters  
**Source scope:** [BOILERPLATE.md](../BOILERPLATE.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [PAYMENTS.md](../../../architecture/PAYMENTS.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Payment Stripe Adapter module owns the single shared Stripe merchant payment provider adapter built on the latest stripe/stripe-php SDK (^20.3+) and pinned StripeClient API version, extending liberusoftware/payment-contracts and consolidating liberusoftware/billing-stripe for PaymentIntents, SetupIntents, CustomerSession, Checkout\Session, ConfirmationToken, Stripe Payment Element, Apple Pay / Google Pay / Link / SEPA / ACH / Klarna, manual and automatic capture, full/partial refunds, Radar disputes, Stripe Terminal POS readers, BalanceTransaction settlement reconciliation, and Webhook::constructEvent signature verification. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Latest Stripe SDK client and pinned API version:** Instantiate \Stripe\StripeClient (stripe/stripe-php ^20.3+) per tenant credential with explicit pinned stripe_version, max_network_retries, and per-request idempotency_key options.
- **PaymentIntents, Checkout Sessions, and 3DS2/SCA confirmation:** Implement PaymentIntentServiceContract using automatic_payment_methods, ConfirmationToken, CustomerSession, and next_action 3DS/redirect handling.
- **SetupIntents and PaymentMethod vaulting:** Implement SavedPaymentMethodVaultContract for off-session recurring cards, wallets, SEPA Direct Debit, and US Bank Account mandates.
- **Full/partial capture, cancellation, and idempotent refunds:** Implement PaymentCaptureAndRefundContract with deterministic Stripe idempotency_key options and provider reference tracking.
- **Stripe-Signature webhook verification and normalization:** Implement MerchantWebhookVerifierContract using \Stripe\Webhook::constructEvent() with timestamp tolerance and raw-body verification into MerchantWebhookEventDto.
- **Stripe disputes, Terminal POS, and BalanceTransaction reconciliation:** Implement DisputeAndChargebackHandlerContract, POSHardwareTerminalContract, and PayoutAndSettlementReconcilerContract for disputes, Terminal readers, and payout fee/FX reconciliation.

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

- Provide matching optional presentation packages only when required: `module-boilerplate-payment-stripe-filament`, `module-boilerplate-payment-stripe-livewire`, `module-boilerplate-payment-stripe-api`, `module-boilerplate-payment-stripe-react-inertia`, `module-boilerplate-payment-stripe-vue-inertia`, `module-boilerplate-payment-stripe-nuxt`, `module-boilerplate-payment-stripe-nextjs`, `module-boilerplate-payment-stripe-react-native`, and `module-boilerplate-payment-stripe-flutter`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify latest stripe sdk client and pinned api version across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify paymentintents, checkout sessions, and 3ds2/sca confirmation across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify setupintents and paymentmethod vaulting across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify full/partial capture, cancellation, and idempotent refunds across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify stripe-signature webhook verification and normalization across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify stripe disputes, terminal pos, and balancetransaction reconciliation across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
| **Latest Stripe SDK client and pinned API version** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `latest stripe sdk client and pinned api version`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **PaymentIntents, Checkout Sessions, and 3DS2/SCA confirmation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `paymentintents, checkout sessions, and 3ds2/sca confirmation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **SetupIntents and PaymentMethod vaulting** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `setupintents and paymentmethod vaulting`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Full/partial capture, cancellation, and idempotent refunds** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `full/partial capture, cancellation, and idempotent refunds`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Stripe-Signature webhook verification and normalization** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `stripe-signature webhook verification and normalization`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Stripe disputes, Terminal POS, and BalanceTransaction reconciliation** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `stripe disputes, terminal pos, and balancetransaction reconciliation`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/payment-stripe.md) | [Source map](../SOURCE-MAPPING.md#payment-stripe) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/payment-stripe.md) | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/payment-stripe.md) | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) · `module-boilerplate-payment-stripe-filament` | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/payment-stripe.md) | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/payment-stripe.md) | [`project-boilerplate-laravel-inertia-react`](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · `module-boilerplate-payment-stripe-react-inertia` | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/payment-stripe.md) | [`project-boilerplate-laravel-inertia-vue`](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · `module-boilerplate-payment-stripe-vue-inertia` | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/payment-stripe.md) | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · `module-boilerplate-payment-stripe-nuxt` | Standalone Vue SSR client consuming `project-boilerplate-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/payment-stripe.md) | [`project-boilerplate-next-react`](https://github.com/liberusoftware/project-boilerplate-next-react) · `module-boilerplate-payment-stripe-nextjs` | App Router Server/Client components consuming `project-boilerplate-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/payment-stripe.md) | [`project-boilerplate-mobile-react`](https://github.com/liberusoftware/project-boilerplate-mobile-react) · `module-boilerplate-payment-stripe-react-native` | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/payment-stripe.md) | [`project-boilerplate-mobile-flutter`](https://github.com/liberusoftware/project-boilerplate-mobile-flutter) · `module-boilerplate-payment-stripe-flutter` | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/payment-stripe.md) | [`project-boilerplate-dart-mobile`](https://github.com/liberusoftware/project-boilerplate-dart-mobile) · `module-boilerplate-payment-stripe-dart-mobile`<br>[`project-boilerplate-dart-desktop`](https://github.com/liberusoftware/project-boilerplate-dart-desktop) · `module-boilerplate-payment-stripe-dart-desktop` | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
