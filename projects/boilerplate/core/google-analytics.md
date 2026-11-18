# Boilerplate: Google Analytics domain packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#google-analytics). Observed identity: [`liberusoftware/analytics-google`](../../../modules/source/liberusoftware--analytics-google.md). This retained spelling maps to `analytics-google`; it is not another independent module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-google-analytics`
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Google Analytics event mapping, property/stream configuration, consent-aware delivery, and diagnostics.

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Google Analytics. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability.

- Model the bounded context with explicit aggregates, entities, value objects, enums, and lifecycle states; reject invalid transitions inside the domain boundary.
- Expose typed actions for mutations and purpose-built queries for reads. Keep Eloquent models as persistence mappings and never expose private tables to other modules.
- Enforce authorization, tenant/team context, ownership, consent, and field sensitivity consistently across HTTP, UI, console, queue, export, search, notification, and bulk paths.
- Own migrations, constraints, indexes, factories, seeders, retention, export, deletion, configuration, events, jobs, and safe enable/disable/upgrade behavior.
- Make asynchronous work idempotent, retryable, observable, and safe to replay; dispatch local events after commit and document compensation for distributed work.

## Verification and consumer contract

Test domain rules, actions, policies, validation, persistence, tenancy, events, jobs, commands, migrations, upgrades, security, failure recovery, and representative host composition. Add architecture tests for presentation coupling, provider leakage, private cross-module access, and dependency cycles.

API, Filament, Livewire, React, Vue, and Nuxt consumers use only this package's public contracts. See [DDD patterns](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md) and [testing](../../../standards/TESTING.md).

<!-- core-implementation-plan:start -->
## Module features, domain aspects, and source architecture

### Feature and domain aspect implementation matrix

| Feature / aspect | Domain model & invariant ownership | Application action, query, persistence & event contract |
| --- | --- | --- |
| **Google analytics event mapping** | Model `google analytics event mapping` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Property/stream configuration** | Model `property/stream configuration` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Consent-aware delivery** | Model `consent-aware delivery` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Diagnostics** | Model `diagnostics` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GoogleTransport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/analytics-google/src/Contracts/GoogleTransport.php) | `public function send(array $payload): array` |

### Consuming adapter specifications

- [HTTP API contract](../api/google-analytics.md) · [Filament 5](../filament/google-analytics.md) · [Livewire 4](../livewire/google-analytics.md) · [React + Inertia](../react/google-analytics.md) · [Vue + Inertia](../vue/google-analytics.md) · [Nuxt 4](../nuxt/google-analytics.md) · [Next.js](../nextjs/google-analytics.md) · [React Native](../react-native/google-analytics.md) · [Flutter & Dart](../flutter/google-analytics.md)
<!-- core-implementation-plan:end -->
