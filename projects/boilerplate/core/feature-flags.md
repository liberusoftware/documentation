# Boilerplate: Feature Flags domain packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#feature-flags). Observed identity: [`liberusoftware/feature-flags`](../../../modules/source/liberusoftware--feature-flags.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-feature-flags`
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Typed flags, environment/tenant/user targeting, rollout, telemetry, ownership, and cleanup.

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Feature Flags. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability.

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
| **Typed flags** | Model `typed flags` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Environment/tenant/user targeting** | Model `environment/tenant/user targeting` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Rollout** | Model `rollout` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Telemetry** | Model `telemetry` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Ownership** | Model `ownership` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Cleanup** | Model `cleanup` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_01_020000_create_feature_flags_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/feature-flags/database/migrations/2026_08_01_020000_create_feature_flags_table.php).

### Consuming adapter specifications

- [HTTP API contract](../api/feature-flags.md) · [Filament 5](../filament/feature-flags.md) · [Livewire 4](../livewire/feature-flags.md) · [React + Inertia](../react/feature-flags.md) · [Vue + Inertia](../vue/feature-flags.md) · [Nuxt 4](../nuxt/feature-flags.md) · [Next.js](../nextjs/feature-flags.md) · [React Native](../react-native/feature-flags.md) · [Flutter & Dart](../flutter/feature-flags.md)
<!-- core-implementation-plan:end -->
