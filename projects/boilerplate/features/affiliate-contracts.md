# Boilerplate: Affiliate Contracts

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#affiliate-contracts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-boilerplate-affiliate-contracts`
**Intended package identity:** `liberusoftware/affiliate-contracts`
**Extends / implements contracts:** `AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, FraudAndSelfReferralPolicyContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract, RewardFulfillmentContract`
**Application:** Boilerplate  
**Capability group:** Affiliate management and referral contracts  
**Source scope:** [BOILERPLATE.md](../BOILERPLATE.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Affiliate Contracts module owns product-neutral PHP interfaces, immutable attribution and conversion DTOs, commission calculator contracts, clawback/hold lifecycle states, fraud and self-referral policy contracts, and payout settlement boundaries that any repository (CRM, Billing, Ecommerce, Accounting) can implement or extend. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **AffiliateProgramContract and attribution window DTOs:** Define program terms, attribution windows, first/last/coupon-override models, hold periods, and recurring commission caps without product schema coupling.
- **ReferralAttributionContract and signed touch tokens:** Standardize referral link/code issuance, first-party click/touch recording, and winning advocate resolution for orders, invoices, subscriptions, or deals.
- **ConversionRecorderContract and idempotent clawbacks:** Provide product-neutral commands to record qualified conversions and process partial/full clawbacks when orders or invoices are refunded, voided, or disputed.
- **CommissionCalculatorContract and tiered rate rules:** Define flat, percentage, tiered-volume, product-category, and recurring-installment commission calculation contracts using exact minor-unit money DTOs.
- **FraudAndSelfReferralPolicyContract:** Define self-referral, shared payment fingerprint, velocity anomaly, and duplicate prospect checks executed before conversion qualification.
- **PayoutSettlementContract and RewardFulfillmentContract:** Define matured commission locking, minimum payout thresholds, tax/compliance holds, settlement batch handoff to Payment Core/Accounting, and two-sided referral rewards.

## 3. Ownership and contract boundaries

- **Contract alignment:** Implements and/or exposes `AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, FraudAndSelfReferralPolicyContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract, RewardFulfillmentContract` as defined in [AFFILIATES.md](../../../architecture/AFFILIATES.md). Consuming repositories depend on the contract boundary rather than coupling to internal models or vendor SDKs.
- Own the capability's domain rules, policies, actions, queries, events, persistence, migrations, configuration, audit semantics, and failure recovery.
- Expose stable contracts, immutable DTOs/read models, commands, queries, and past-tense domain events where other modules have a legitimate integration need.
- Consume identity, organizations/teams, authorization, settings, files, notifications, queues, localization, currency, and observability from the shared foundation rather than duplicating them.
- Never depend on an application's `App\` classes, another module's private tables/models, a provider SDK in provider-neutral code, or an optional presentation framework.
- Keep Filament, Livewire, Inertia, Next.js, Nuxt, Mobile, and HTTP API logic in matching one-to-one presentation packages when those surfaces are required.

## 4. Implementation strategy

### Domain model

- Define aggregates, entities, value objects, enums, invariants, lifecycle states, and transition rules using the terminology in this specification and [AFFILIATES.md](../../../architecture/AFFILIATES.md).
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

- Provide matching optional presentation packages only when required: `module-boilerplate-affiliate-contracts-filament`, `module-boilerplate-affiliate-contracts-livewire`, `module-boilerplate-affiliate-contracts-api`, `module-boilerplate-affiliate-contracts-react-inertia`, `module-boilerplate-affiliate-contracts-vue-inertia`, `module-boilerplate-affiliate-contracts-nuxt`, `module-boilerplate-affiliate-contracts-nextjs`, `module-boilerplate-affiliate-contracts-react-native`, and `module-boilerplate-affiliate-contracts-flutter`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify affiliateprogramcontract and attribution window dtos across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify referralattributioncontract and signed touch tokens across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify conversionrecordercontract and idempotent clawbacks across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify commissioncalculatorcontract and tiered rate rules across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify fraudandselfreferralpolicycontract across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify payoutsettlementcontract and rewardfulfillmentcontract across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Add unit tests for pure rules/value objects and feature tests for actions, policies, validation, persistence, events, jobs, and module lifecycle.
- Add architecture tests for forbidden dependencies, `App\` coupling, provider leakage, private cross-module access, and presentation dependencies.
- Add migration/upgrade, contract, compatibility, security, performance, failure/recovery, and minimal-host installation tests as risk requires.
- Run the independent Pest 5 suite through repository-owned Composer scripts and the shared package testbench; meaningful owned PHP targets 100% line coverage without excluding difficult code.
- Run composition tests in representative host applications while keeping this repository's suite authoritative for module behavior.

## 7. Definition of done

- Every feature in scope has explicit acceptance criteria, permissions, tenant behavior, persistence ownership, events, failure handling, telemetry, and tests.
- Public contracts (`AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, FraudAndSelfReferralPolicyContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract, RewardFulfillmentContract`) and presentation extension points are versioned and documented.
- Install, enable, disable, upgrade, retry/recovery, and uninstall/retention behavior is verified.
- Security, accessibility where presented, compatibility, architecture, and 100% meaningful-PHP coverage gates pass.
- README, changelog, migration guidance, runbook, CI evidence, and tagged release are available from the independent repository.

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **AffiliateProgramContract and attribution window DTOs** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `affiliateprogramcontract and attribution window dtos`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **ReferralAttributionContract and signed touch tokens** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `referralattributioncontract and signed touch tokens`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **ConversionRecorderContract and idempotent clawbacks** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `conversionrecordercontract and idempotent clawbacks`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **CommissionCalculatorContract and tiered rate rules** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `commissioncalculatorcontract and tiered rate rules`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **FraudAndSelfReferralPolicyContract** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `fraudandselfreferralpolicycontract`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **PayoutSettlementContract and RewardFulfillmentContract** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `payoutsettlementcontract and rewardfulfillmentcontract`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/affiliate-contracts.md) | [Source map](../SOURCE-MAPPING.md#affiliate-contracts) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/affiliate-contracts.md) | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/affiliate-contracts.md) | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) · `module-boilerplate-affiliate-contracts-filament` | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/affiliate-contracts.md) | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/affiliate-contracts.md) | [`project-boilerplate-laravel-inertia-react`](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · `module-boilerplate-affiliate-contracts-react-inertia` | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/affiliate-contracts.md) | [`project-boilerplate-laravel-inertia-vue`](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · `module-boilerplate-affiliate-contracts-vue-inertia` | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/affiliate-contracts.md) | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · `module-boilerplate-affiliate-contracts-nuxt` | Standalone Vue SSR client consuming `project-boilerplate-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/affiliate-contracts.md) | [`project-boilerplate-next-react`](https://github.com/liberusoftware/project-boilerplate-next-react) · `module-boilerplate-affiliate-contracts-nextjs` | App Router Server/Client components consuming `project-boilerplate-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/affiliate-contracts.md) | [`project-boilerplate-mobile-react`](https://github.com/liberusoftware/project-boilerplate-mobile-react) · `module-boilerplate-affiliate-contracts-react-native` | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/affiliate-contracts.md) | [`project-boilerplate-mobile-flutter`](https://github.com/liberusoftware/project-boilerplate-mobile-flutter) · `module-boilerplate-affiliate-contracts-flutter` | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/affiliate-contracts.md) | [`project-boilerplate-dart-mobile`](https://github.com/liberusoftware/project-boilerplate-dart-mobile) · `module-boilerplate-affiliate-contracts-dart-mobile`<br>[`project-boilerplate-dart-desktop`](https://github.com/liberusoftware/project-boilerplate-dart-desktop) · `module-boilerplate-affiliate-contracts-dart-desktop` | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
