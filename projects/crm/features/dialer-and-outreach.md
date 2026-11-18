# CRM: Dialer and Outreach

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#dialer-and-outreach). Observed identity: [`liberusoftware/module-crm-dialer-and-outreach`](../../../modules/source/liberusoftware--module-crm-dialer-and-outreach.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical independent module specification

**Domain module:** `module-crm-dialer-and-outreach`
**Application:** CRM  
**Capability group:** Communications and contact-center modules  
**Source scope:** [CRM.md](../CRM.md)  
**Architecture:** [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md) · [API.md](../../../architecture/API.md) · [FILAMENT.md](../../../standards/FILAMENT.md) · [LIVEWIRE.md](../../../standards/LIVEWIRE.md)

## 1. Purpose

The Dialer and Outreach module owns Power/preview/progressive dialing, prioritized lists, scripts, local-time policy, retries, voicemail drop, answer detection adapters, outcomes, and compliance controls. It is the authoritative boundary for this capability and must remain independently installable, testable, versioned, enabled, and reusable across compatible Liberu applications.

## 2. Full feature scope

- **Power/preview/progressive dialing:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Prioritized lists:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Scripts:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Local-time policy:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Retries:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Voicemail drop:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Answer detection adapters:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Outcomes:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.
- **Compliance controls:** implement the complete lifecycle, validation, permissions, failure handling, audit evidence, and operator/user feedback required by this capability.

## 3. Ownership and boundaries

- Own the capability's domain rules, policies, actions, queries, events, persistence, migrations, configuration, audit semantics, and failure recovery.
- Expose stable contracts, immutable DTOs/read models, commands, queries, and past-tense domain events where other modules have a legitimate integration need.
- Consume identity, organizations/teams, authorization, settings, files, notifications, queues, localization, currency, and observability from the shared foundation rather than duplicating them.
- Never depend on an application's `App\` classes, another module's private tables/models, a provider SDK in provider-neutral code, or an optional presentation framework.
- Keep Filament, Livewire, and HTTP API logic in matching one-to-one presentation packages when those surfaces are required.

## 3a. Liberu contact-protection profile

Liberu installations use this module's standard dialer with a mandatory contact-protection policy. The policy is part of eligibility, not a UI hint:

- After an initial call attempt, persist `next_contact_at`, the attempt outcome, and the policy reason before the lead can return to an automated queue.
- Do not dial or send another automated outreach step while `now < next_contact_at`; the scheduler must filter it out and the domain action must reject a bypass.
- Clear cooling-off only for an explicit inbound reply, booked meeting, conversion, contact request, or separately authorized staff exception. A failed provider retry does not clear it.
- Apply opt-out, complaint, suppression, legal restriction, per-channel consent, local-time windows, and frequency caps before every attempt. The strictest rule wins.
- Keep the decision explainable in the activity timeline and expose the next eligible time to sales staff without exposing protected consent evidence to unauthorized users.

This profile works with [Sales Engagement](sales-engagement.md), [Consent and Preferences](consent-and-preferences.md), and Liberu's [Revenue and Care Orchestration](../../liberu/features/revenue-and-care-orchestration.md); it does not duplicate those modules.

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

- Provide matching optional presentation packages only when required: `module-crm-dialer-and-outreach-filament`, `module-crm-dialer-and-outreach-livewire`, and `module-crm-dialer-and-outreach-api`.
- Each presentation package depends on this module's public boundary and presents no other independent module.
- Themes may style supported extension points but cannot replace validation, authorization, routes, or domain actions.

## 5. Security, privacy, and operations

- Apply least privilege, tenant isolation, field-level sensitivity, recent authentication/approval for risky actions, and immutable audit evidence proportionate to the capability.
- Classify personal, financial, credential, document, and regulated data; define purpose, consent, minimization, retention, export, deletion, legal hold, and residency rules.
- Redact secrets and sensitive payloads from logs, exceptions, events, metrics, snapshots, and test artifacts.
- Emit structured logs, metrics, traces, health checks, queue/provider diagnostics, and correlation identifiers with actionable runbooks and alerts.

## 6. Verification strategy

- Verify power/preview/progressive dialing across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify prioritized lists across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify scripts across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify local-time policy across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify retries across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify voicemail drop across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify answer detection adapters across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify outcomes across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
- Verify compliance controls across allowed, denied, invalid, duplicate, concurrent, partial-failure, recovery, and tenant-isolation paths where applicable.
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
| **Power/preview/progressive dialing** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `power/preview/progressive dialing`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Prioritized lists** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `prioritized lists`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Scripts** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `scripts`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Local-time policy** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `local-time policy`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Retries** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `retries`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Voicemail drop** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `voicemail drop`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Answer detection adapters** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `answer detection adapters`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Outcomes** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `outcomes`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |
| **Compliance controls** | Enforce lifecycle state transitions, value-object invariants, and tenant/workspace ownership for `compliance controls`. | Expose a typed command/query DTO, recheck policy at the application boundary, and emit post-commit domain/audit events. |

### Technology delivery matrix

| Technology layer | Specification | Host & skeleton repositories | Delivery boundary |
| --- | --- | --- | --- |
| Core domain (`PHP 8.5 / Laravel 13`) | [Core plan](../core/dialer-and-outreach.md) | [Source map](../SOURCE-MAPPING.md#dialer-and-outreach) | Authoritative domain model, actions, queries, policies, migrations, and events |
| HTTP API (`OpenAPI 3.1 / Sanctum`) | [API plan](../api/dialer-and-outreach.md) | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Versioned `/api/v1` REST/OpenAPI contract for independent web, mobile, and desktop clients |
| Filament 5 (`Laravel Admin`) | [Filament plan](../filament/dialer-and-outreach.md) | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) · [`module-crm-dialer-and-outreach-filament`](https://github.com/liberusoftware/module-crm-dialer-and-outreach-filament) (`liberusoftware/crm-dialer-and-outreach-filament`) | Resources, schemas, tables, infolists, widgets, and panel actions |
| Livewire 4 (`Server UI`) | [Livewire plan](../livewire/dialer-and-outreach.md) | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Server-driven reactive components and namespaced default Blade views |
| React 19.2 + Inertia 3 | [React Inertia plan](../react/dialer-and-outreach.md) | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) · [`module-crm-dialer-and-outreach-react-inertia`](https://github.com/liberusoftware/module-crm-dialer-and-outreach-react-inertia) (`@liberusoftware/module-crm-dialer-and-outreach-react-inertia`) | Laravel session/CSRF routes with typed Inertia page props and shared React primitives |
| Vue 3 + Inertia 3 | [Vue Inertia plan](../vue/dialer-and-outreach.md) | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) · [`module-crm-dialer-and-outreach-vue-inertia`](https://github.com/liberusoftware/module-crm-dialer-and-outreach-vue-inertia) (`@liberusoftware/module-crm-dialer-and-outreach-vue-inertia`) | Laravel session/CSRF routes with Vue SFC pages and shared composables |
| Nuxt 4 + Vue 3 | [Nuxt plan](../nuxt/dialer-and-outreach.md) | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) · [`module-crm-dialer-and-outreach-nuxt`](https://github.com/liberusoftware/module-crm-dialer-and-outreach-nuxt) (`@liberusoftware/module-crm-dialer-and-outreach-nuxt`) | Standalone Vue SSR client consuming `project-crm-laravel-api` with isolated caches |
| Next.js + React 19.2 | [Next.js plan](../nextjs/dialer-and-outreach.md) | [`project-crm-next-react`](https://github.com/liberusoftware/project-crm-next-react) · [`module-crm-dialer-and-outreach-nextjs`](https://github.com/liberusoftware/module-crm-dialer-and-outreach-nextjs) (`@liberusoftware/module-crm-dialer-and-outreach-nextjs`) | App Router Server/Client components consuming `project-crm-laravel-api` |
| React Native + Expo | [React Native plan](../react-native/dialer-and-outreach.md) | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) · [`module-crm-dialer-and-outreach-react-native`](https://github.com/liberusoftware/module-crm-dialer-and-outreach-react-native) (`@liberusoftware/module-crm-dialer-and-outreach-react-native`) | Native iOS/Android mobile screens with SecureStore credentials and offline recovery |
| Flutter mobile | [Flutter plan](../flutter/dialer-and-outreach.md) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) · [`module-crm-dialer-and-outreach-flutter`](https://github.com/liberusoftware/module-crm-dialer-and-outreach-flutter) (`module_crm_dialer_and_outreach_flutter`) | Native iOS/Android Dart/Flutter widgets and typed repository client |
| Dart mobile & desktop | [Flutter & Dart plan](../flutter/dialer-and-outreach.md) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) · [`module-crm-dialer-and-outreach-dart-mobile`](https://github.com/liberusoftware/module-crm-dialer-and-outreach-dart-mobile) (`module_crm_dialer_and_outreach_dart_mobile`)<br>[`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) · [`module-crm-dialer-and-outreach-dart-desktop`](https://github.com/liberusoftware/module-crm-dialer-and-outreach-dart-desktop) (`module_crm_dialer_and_outreach_dart_desktop`) | Dedicated mobile (`iOS`/`Android`) and desktop (`Linux`/`macOS`/`Windows`) Flutter hosts |
<!-- feature-technology-matrix:end -->
