# Boilerplate: Profiles domain packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#profiles). Observed identity: [`liberusoftware/profiles`](../../../modules/source/liberusoftware--profiles.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-profiles`
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Names, avatars, contact preferences, locale/timezone, completion, and controlled profile updates.

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Profiles. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability.

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
| **Names** | Model `names` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Avatars** | Model `avatars` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Contact preferences** | Model `contact preferences` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Locale/timezone** | Model `locale/timezone` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Completion** | Model `completion` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Controlled profile updates** | Model `controlled profile updates` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_02_16_000001_add_locale_to_users_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/profiles/database/migrations/2026_02_16_000001_add_locale_to_users_table.php) · [2026_02_16_215049_add_theme_preference_to_users_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/profiles/database/migrations/2026_02_16_215049_add_theme_preference_to_users_table.php) · [2026_08_01_000000_add_timezone_to_users_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/profiles/database/migrations/2026_08_01_000000_add_timezone_to_users_table.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [UpdateProfile.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/profiles/src/Actions/UpdateProfile.php) | `public function handle(Model $profile, ProfileUpdate $update): Model` |

### Consuming adapter specifications

- [HTTP API contract](../api/profiles.md) · [Filament 5](../filament/profiles.md) · [Livewire 4](../livewire/profiles.md) · [React + Inertia](../react/profiles.md) · [Vue + Inertia](../vue/profiles.md) · [Nuxt 4](../nuxt/profiles.md) · [Next.js](../nextjs/profiles.md) · [React Native](../react-native/profiles.md) · [Flutter & Dart](../flutter/profiles.md)
<!-- core-implementation-plan:end -->
