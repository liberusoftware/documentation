# Boilerplate: Affiliates and Partner Programs

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#affiliates). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-boilerplate-affiliates`
**Intended package identity:** `liberusoftware/affiliate-core`
**Extends / implements contracts:** `liberusoftware/affiliate-contracts (AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract)`
**Application:** Boilerplate  
**Capability group:** Affiliate management and referral capabilities  
**Source scope:** [BOILERPLATE.md](../BOILERPLATE.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [AFFILIATES.md](../../../architecture/AFFILIATES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Affiliates and Partner Programs module owns reusable affiliate program administration, partner enrollment and approval, referral links and promotional codes, first-party click and conversion attribution, tiered and recurring commission ledger, refund/dispute clawback hold windows, fraud prevention, partner portal read models, and payout settlement batching extending liberusoftware/affiliate-contracts. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Affiliate program and commission tier rules:** Configure attribution windows, hold periods, flat/percentage/tiered/recurring commission schedules, and product eligibility extending AffiliateProgramContract.
- **Partner applications, KYC/tax readiness, and approval:** Manage partner enrollment applications, review workflows, tier assignment, and custom partner rate overrides via AffiliatePartnerEnrollmentContract.
- **Tracking links, campaign parameters, and promo codes:** Issue signed referral links, vanity codes, and campaign creative assets with first-party consent-aware click tracking.
- **Authoritative conversion ingestion and hold ledger:** Record idempotent conversions from orders, subscriptions, and invoices via ConversionRecorderContract with immutable pending/held/matured ledger states.
- **Automated refund, cancellation, and dispute clawbacks:** Reverse or adjust pending and matured commissions automatically when upstream payments are refunded, voided, or charged back.
- **Self-referral, velocity, and fraud screening:** Enforce FraudAndSelfReferralPolicyContract across account, email domain, IP/device velocity, and payment-fingerprint signals with operator review queues.
- **Payout approval batches and settlement handoff:** Group matured commissions above payout thresholds, enforce tax/compliance holds, and export or disburse via PayoutSettlementContract.

## 3. Ownership and contract boundaries

- **Contract alignment:** Implements and/or exposes `liberusoftware/affiliate-contracts (AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract)` as defined in [AFFILIATES.md](../../../architecture/AFFILIATES.md). Consuming repositories depend on the contract boundary rather than coupling to internal models or vendor SDKs.
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

- Provide matching optional presentation packages only when required: `module-boilerplate-affiliates-filament`, `module-boilerplate-affiliates-livewire`, `module-boilerplate-affiliates-api`, `module-boilerplate-affiliates-react-inertia`, `module-boilerplate-affiliates-vue-inertia`, `module-boilerplate-affiliates-nuxt`, `module-boilerplate-affiliates-nextjs`, `module-boilerplate-affiliates-react-native`, and `module-boilerplate-affiliates-flutter`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify affiliate program and commission tier rules across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify partner applications, kyc/tax readiness, and approval across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify tracking links, campaign parameters, and promo codes across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify authoritative conversion ingestion and hold ledger across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify automated refund, cancellation, and dispute clawbacks across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify self-referral, velocity, and fraud screening across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify payout approval batches and settlement handoff across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Add unit tests for pure rules/value objects and feature tests for actions, policies, validation, persistence, events, jobs, and module lifecycle.
- Add architecture tests for forbidden dependencies, `App\` coupling, provider leakage, private cross-module access, and presentation dependencies.
- Add migration/upgrade, contract, compatibility, security, performance, failure/recovery, and minimal-host installation tests as risk requires.
- Run the independent Pest 5 suite through repository-owned Composer scripts and the shared package testbench; meaningful owned PHP targets 100% line coverage without excluding difficult code.
- Run composition tests in representative host applications while keeping this repository's suite authoritative for module behavior.

## 7. Definition of done

- Every feature in scope has explicit acceptance criteria, permissions, tenant behavior, persistence ownership, events, failure handling, telemetry, and tests.
- Public contracts (`liberusoftware/affiliate-contracts (AffiliateProgramContract, AffiliatePartnerEnrollmentContract, ReferralAttributionContract, ConversionRecorderContract, CommissionCalculatorContract, PayoutSettlementContract)`) and presentation extension points are versioned and documented.
- Install, enable, disable, upgrade, retry/recovery, and uninstall/retention behavior is verified.
- Security, accessibility where presented, compatibility, architecture, and 100% meaningful-PHP coverage gates pass.
- README, changelog, migration guidance, runbook, CI evidence, and tagged release are available from the independent repository.

<!-- feature-technology-matrix:start -->
## Cross-technology implementation plan and feature matrix

Every aspect of this capability is implemented once in the authoritative core domain module and exposed through optional one-to-one presentation and API adapters. Clients never duplicate business invariants or write directly to another module's persistence.

### Feature and domain aspect breakdown

| Feature / aspect | Domain aggregate & invariant focus | Application action, query & audit contract |
| --- | --- | --- |
| **Affiliate program and commission tier rules** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `affiliate program and commission tier rules`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Partner applications, KYC/tax readiness, and approval** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `partner applications, kyc/tax readiness, and approval`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Tracking links, campaign parameters, and promo codes** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `tracking links, campaign parameters, and promo codes`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Authoritative conversion ingestion and hold ledger** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `authoritative conversion ingestion and hold ledger`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Automated refund, cancellation, and dispute clawbacks** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `automated refund, cancellation, and dispute clawbacks`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Self-referral, velocity, and fraud screening** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `self-referral, velocity, and fraud screening`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Payout approval batches and settlement handoff** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `payout approval batches and settlement handoff`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/affiliates.md) | [Source map](../SOURCE-MAPPING.md#affiliates) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/affiliates.md) | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/affiliates.md) | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) · `module-boilerplate-affiliates-filament` | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/affiliates.md) | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/affiliates.md) | [`project-boilerplate-laravel-inertia-react`](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · `module-boilerplate-affiliates-react-inertia` | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/affiliates.md) | [`project-boilerplate-laravel-inertia-vue`](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · `module-boilerplate-affiliates-vue-inertia` | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/affiliates.md) | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · `module-boilerplate-affiliates-nuxt` | Standalone Vue SSR client consuming `project-boilerplate-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/affiliates.md) | [`project-boilerplate-next-react`](https://github.com/liberusoftware/project-boilerplate-next-react) · `module-boilerplate-affiliates-nextjs` | App Router Server/Client components consuming `project-boilerplate-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/affiliates.md) | [`project-boilerplate-mobile-react`](https://github.com/liberusoftware/project-boilerplate-mobile-react) · `module-boilerplate-affiliates-react-native` | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/affiliates.md) | [`project-boilerplate-mobile-flutter`](https://github.com/liberusoftware/project-boilerplate-mobile-flutter) · `module-boilerplate-affiliates-flutter` | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/affiliates.md) | [`project-boilerplate-dart-mobile`](https://github.com/liberusoftware/project-boilerplate-dart-mobile) · `module-boilerplate-affiliates-dart-mobile`<br>[`project-boilerplate-dart-desktop`](https://github.com/liberusoftware/project-boilerplate-dart-desktop) · `module-boilerplate-affiliates-dart-desktop` | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
