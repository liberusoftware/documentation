# Cms: Extension Marketplace Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#extension-marketplace). Observed identity: [`liberusoftware/module-cms-extension-marketplace`](../../../modules/source/liberusoftware--module-cms-extension-marketplace.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-cms-extension-marketplace`
**Domain specification:** [Extension Marketplace](../features/extension-marketplace.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Extension Marketplace. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Publishers** | Model `publishers` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Listings** | Model `listings` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Categories** | Model `categories` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Versions** | Model `versions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Signing** | Model `signing` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Reviews** | Model `reviews` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Licensing** | Model `licensing` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Trials** | Model `trials` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Security status** | Model `security status` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Support** | Model `support` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Distribution** | Model `distribution` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_29_000000_create_cms_extension_marketplace_tables.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/database/migrations/2026_08_29_000000_create_cms_extension_marketplace_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ExtensionMarketplaceQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Queries/ExtensionMarketplaceQuery.php) | `public function catalog(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function find(string $key): ?ExtensionListing` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ExtensionMarketplaceService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Services/ExtensionMarketplaceService.php) | `public function publisher(array $attributes, ?int $teamId = null): ExtensionPublisher`<br>`public function category(array $attributes): ExtensionCategory`<br>`public function listing(array $attributes, ?int $teamId = null): ExtensionListing`<br>`public function version(ExtensionListing $listing, array $attributes): ExtensionVersion`<br>`public function sign(ExtensionVersion $version, string $signature, string $key): ExtensionVersion`<br>`public function security(ExtensionListing $listing, string $status): ExtensionListing`<br>`public function review(ExtensionListing $listing, string $type, int\|string $subject, int $rating, ?string $body = null, ?int $teamId = null): ExtensionReview`<br>`public function license(ExtensionListing $listing, string $subjectType, int\|string $subject, ?int $days = null): ExtensionLicense`<br>`public function trial(ExtensionListing $listing, string $subjectType, int\|string $subject, int $days = 14): ExtensionTrial`<br>`public function support(ExtensionListing $listing, array $attributes): ExtensionSupport`<br>`public function distribute(ExtensionVersion $version, array $attributes): ExtensionDistribution`<br>`public function ratingSummary(ExtensionListing $listing): array`<br>`public function publish(ExtensionListing $listing): ExtensionListing` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ExtensionCategory.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionCategory.php) | `key`, `name`, `description` |
| [ExtensionDistribution.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionDistribution.php) | `version_id`, `channel`, `url`, `checksum`, `status` |
| [ExtensionLicense.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionLicense.php) | `listing_id`, `license_key`, `subject_type`, `subject_id`, `status`, `starts_at`, `ends_at` |
| [ExtensionListing.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionListing.php) | `publisher_id`, `category_id`, `key`, `name`, `description`, `license`, `status`, `security_status`, `metadata`, `team_id` |
| [ExtensionPublisher.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionPublisher.php) | `key`, `name`, `website`, `status`, `team_id` |
| [ExtensionReview.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionReview.php) | `listing_id`, `reviewer_type`, `reviewer_id`, `rating`, `review`, `status`, `team_id` |
| [ExtensionSupport.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionSupport.php) | `listing_id`, `channel`, `url`, `response_hours` |
| [ExtensionTrial.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionTrial.php) | `listing_id`, `subject_type`, `subject_id`, `status`, `starts_at`, `ends_at` |

### Consuming adapter specifications

- [HTTP API contract](../api/extension-marketplace.md) · [Filament 5](../filament/extension-marketplace.md) · [Livewire 4](../livewire/extension-marketplace.md) · [React + Inertia](../react/extension-marketplace.md) · [Vue + Inertia](../vue/extension-marketplace.md) · [Nuxt 4](../nuxt/extension-marketplace.md) · [Next.js](../nextjs/extension-marketplace.md) · [React Native](../react-native/extension-marketplace.md) · [Flutter & Dart](../flutter/extension-marketplace.md)
<!-- core-implementation-plan:end -->
