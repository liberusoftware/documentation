# Boilerplate: API Access domain packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#api-access). Observed identity: [`liberusoftware/api-access`](../../../modules/source/liberusoftware--api-access.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-api-access`
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Tokens, service identities, scopes, rate limits, versioning, idempotency, and revocation.

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of API Access. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability.

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
| **Tokens** | Model `tokens` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Service identities** | Model `service identities` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Scopes** | Model `scopes` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Rate limits** | Model `rate limits` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Versioning** | Model `versioning` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Idempotency** | Model `idempotency` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Revocation** | Model `revocation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_06_29_124225_create_personal_access_tokens_table.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/api-access/database/migrations/2026_06_29_124225_create_personal_access_tokens_table.php) · [2026_08_01_020100_create_api_idempotency_keys_table.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/api-access/database/migrations/2026_08_01_020100_create_api_idempotency_keys_table.php) · [2026_08_01_064200_create_api_service_identities.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/api-access/database/migrations/2026_08_01_064200_create_api_service_identities.php).

### Consuming adapter specifications

- [HTTP API contract](../api/api-access.md) · [Filament 5](../filament/api-access.md) · [Livewire 4](../livewire/api-access.md) · [React + Inertia](../react/api-access.md) · [Vue + Inertia](../vue/api-access.md) · [Nuxt 4](../nuxt/api-access.md) · [Next.js](../nextjs/api-access.md) · [React Native](../react-native/api-access.md) · [Flutter & Dart](../flutter/api-access.md)
<!-- core-implementation-plan:end -->
