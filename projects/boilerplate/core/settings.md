# Boilerplate: Settings domain packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#settings). Observed identity: [`liberusoftware/settings`](../../../modules/source/liberusoftware--settings.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-settings`
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Typed application/organization/team/user settings, precedence, validation, secrets, audit, and cache invalidation.

## Ownership and implementation plan

This package is the authoritative, presentation-neutral implementation of Settings. It owns the domain language, invariants, application actions, read models, policies, persistence, events, jobs, contracts, lifecycle, recovery, data classification, and upgrade behavior for this capability.

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
| **Typed application/organization/team/user settings** | Model `typed application/organization/team/user settings` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Precedence** | Model `precedence` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Validation** | Model `validation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Secrets** | Model `secrets` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Audit** | Model `audit` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Cache invalidation** | Model `cache invalidation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2022_12_14_083707_create_settings_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/database/migrations/2022_12_14_083707_create_settings_table.php) · [2023_05_15_000000_create_site_settings_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/database/migrations/2023_05_15_000000_create_site_settings_table.php) · [2024_07_24_080000_create_menus_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/database/migrations/2024_07_24_080000_create_menus_table.php) · [2026_08_01_063100_create_scoped_settings_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/database/migrations/2026_08_01_063100_create_scoped_settings_table.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SettingDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/src/Contracts/SettingDefinition.php) | `public function key(): string`<br>`public function validate(mixed $value): bool`<br>`public function secret(): bool` |
| [ScopedSettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/src/Services/ScopedSettings.php) | `public function put(SettingDefinition $definition, string $scopeType, string $scopeId, mixed $value): void`<br>`public function resolve(string $key, array $scopes, mixed $fallback = null): mixed` |

### Consuming adapter specifications

- [HTTP API contract](../api/settings.md) · [Filament 5](../filament/settings.md) · [Livewire 4](../livewire/settings.md) · [React + Inertia](../react/settings.md) · [Vue + Inertia](../vue/settings.md) · [Nuxt 4](../nuxt/settings.md) · [Next.js](../nextjs/settings.md) · [React Native](../react-native/settings.md) · [Flutter & Dart](../flutter/settings.md)
<!-- core-implementation-plan:end -->
