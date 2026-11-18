# CMS: Cms Theme Marketplace Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-theme-marketplace). Observed identity: [`liberusoftware/module-cms-theme-marketplace`](../../../modules/source/liberusoftware--module-cms-theme-marketplace.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-cms-cms-theme-marketplace`
**Domain specification:** [Cms Theme Marketplace](../features/cms-theme-marketplace.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Cms Theme Marketplace. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

## Domain-driven implementation plan

- Model the capability with small aggregates, entities, value objects, enums, domain services, and explicit lifecycle states. Enforce invariants inside the domain boundary and keep invalid transitions impossible or rejected with typed exceptions.
- Implement one application action per meaningful mutation/use case and purpose-built query/read-model classes for reads. Use typed immutable DTOs and stable identifiers at public boundaries; use repositories only where persistence abstraction adds value.
- Publish past-tense domain events after a successful local transaction. Use an outbox/inbox, idempotent handlers, sagas, or compensating actions for cross-module and distributed work; never mutate another module's private tables.

## Laravel and persistence plan

- Use PHP 8.5 strict types, PSR-compatible names, constructor injection, Laravel contracts, service providers, configuration, policies, validation, and route-independent application services. Format with the repository's Pint rules and keep static analysis clean.
- Keep Eloquent models as persistence mappings, not domain aggregates or API resources. The module owns migrations, constraints, indexes, casts, factories, seeders, retention, export, deletion, and upgrade behavior. Released migrations are immutable; production-safe follow-up migrations document locks, backfills, deployment order, and rollback limits.
- Queue work that exceeds the request budget or depends on external systems. Jobs carry authorized tenant/actor context, have explicit retry/backoff/timeout/idempotency rules, and emit structured logs, metrics, traces, correlation IDs, and operator-visible failure state.

## Security and user outcomes

- Apply policies consistently to HTTP, UI, console, queue, export, search, notification, and bulk paths. Enforce tenant/team/resource ownership, field sensitivity, consent, entitlement, and break-glass auditing; scopes never override domain authorization.
- Treat imports, files, webhooks, provider responses, and user input as untrusted. Redact credentials and protected data from logs, exceptions, events, snapshots, metrics, and test artifacts.
- Make normal workflows understandable for SMEs and personal users: actionable validation, safe defaults, reversible or previewable operations, clear status and recovery guidance, localization/timezone/currency support where relevant, accessibility in adapters, low operational overhead, and export/retention controls.

## Public boundary and adapters

Expose only stable contracts, actions, queries, events, resource data, and capability metadata needed by consumers. Keep provider SDKs, credentials, webhook mappings, and provider identifiers in separate adapter packages. Presentation packages may add validation at their boundary, but the core revalidates invariants and authorization and remains free of presentation dependencies.

## Verification and delivery plan

- Use unit tests for value objects, entities, aggregates, policies, and pure rules; feature/integration tests for actions, persistence, validation, tenancy, events, jobs, commands, migrations, upgrades, and recovery; and shared contract tests for adapters.
- Add architecture tests for forbidden App classes, private cross-module access, provider leakage, presentation dependencies, and dependency cycles. Test empty installs, supported upgrades, rollback policy, representative host composition, and compatibility across the declared Laravel/PHP/database matrix.
- Run the independent repository's Pest 5 suite through Composer scripts and the shared package testbench. Generate meaningful coverage, static-analysis, security, documentation/link, and performance evidence; coverage complements risk-based assertions and never replaces them.
- Release with Composer metadata, module manifest, service provider, changelog, migration notes, README, compatibility matrix, runbook, and safe install/enable/disable/upgrade/uninstall behavior. Disabling or removal never silently deletes user data.

<!-- core-implementation-plan:start -->
## Module features, domain aspects, and source architecture

### Feature and domain aspect implementation matrix

| Feature / aspect | Domain model & invariant ownership | Application action, query, persistence & event contract |
| --- | --- | --- |
| **Theme manifests** | Model `theme manifests` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Compatibility** | Model `compatibility` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Previews** | Model `previews` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Licenses** | Model `licenses` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Child themes** | Model `child themes` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Installation** | Model `installation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Updates** | Model `updates` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Security review** | Model `security review` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Ratings** | Model `ratings` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_25_000000_create_cms_theme_marketplace_tables.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/database/migrations/2026_08_25_000000_create_cms_theme_marketplace_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ThemeMarketplaceQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Queries/ThemeMarketplaceQuery.php) | `public function catalog(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function find(string $key, ?string $version = null): ?MarketplaceTheme`<br>`public function installation(string $siteKey, string $themeKey): ?ThemeInstallation` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ThemeMarketplaceService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Services/ThemeMarketplaceService.php) | `public function publish(array $manifest, ?int $teamId = null): MarketplaceTheme`<br>`public function reviewSecurity(MarketplaceTheme $theme, string $status): MarketplaceTheme`<br>`public function compatible(MarketplaceTheme $theme, string $cmsVersion, array $features = []): bool`<br>`public function install(MarketplaceTheme $theme, string $siteKey, string $cmsVersion, array $features = [], ?int $teamId = null): ThemeInstallation`<br>`public function update(ThemeInstallation $installation, MarketplaceTheme $theme, string $cmsVersion, array $features = []): ThemeInstallation`<br>`public function rate(MarketplaceTheme $theme, string $reviewerType, int\|string $reviewerId, int $rating, ?string $review = null, ?int $teamId = null): ThemeRating`<br>`public function ratingSummary(MarketplaceTheme $theme): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MarketplaceTheme.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Models/MarketplaceTheme.php) | `key`, `name`, `version`, `author`, `description`, `manifest`, `compatibility`, `preview_url`, `license`, `parent_key`, `status`, `security_status`, `team_id` |
| [ThemeInstallation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Models/ThemeInstallation.php) | `theme_id`, `site_key`, `installed_version`, `status`, `installed_at`, `updated_at_version`, `team_id` |
| [ThemeRating.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-marketplace/src/Models/ThemeRating.php) | `theme_id`, `reviewer_type`, `reviewer_id`, `rating`, `review`, `team_id` |

### Consuming adapter specifications

- [HTTP API contract](../api/cms-theme-marketplace.md) · [Filament 5](../filament/cms-theme-marketplace.md) · [Livewire 4](../livewire/cms-theme-marketplace.md) · [React + Inertia](../react/cms-theme-marketplace.md) · [Vue + Inertia](../vue/cms-theme-marketplace.md) · [Nuxt 4](../nuxt/cms-theme-marketplace.md) · [Next.js](../nextjs/cms-theme-marketplace.md) · [React Native](../react-native/cms-theme-marketplace.md) · [Flutter & Dart](../flutter/cms-theme-marketplace.md)
<!-- core-implementation-plan:end -->
