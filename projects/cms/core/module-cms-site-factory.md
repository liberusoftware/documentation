# CMS: Module Cms Site Factory Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-site-factory). Observed identity: [`liberusoftware/module-cms-site-factory`](../../../modules/source/liberusoftware--module-cms-site-factory.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-cms-module-cms-site-factory`
**Domain specification:** [Module Cms Site Factory](../features/module-cms-site-factory.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Module Cms Site Factory. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Site templates/recipes** | Model `site templates/recipes` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Provisioning** | Model `provisioning` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Domain verification** | Model `domain verification` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Initial content/configuration** | Model `initial content/configuration` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Cloning** | Model `cloning` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Suspension** | Model `suspension` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Archival** | Model `archival` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Teardown** | Model `teardown` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_24_150000_create_cms_site_factory_tables.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-factory/database/migrations/2026_08_24_150000_create_cms_site_factory_tables.php) · [2026_08_25_010000_add_site_factory_tenancy_and_operations.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-factory/database/migrations/2026_08_25_010000_add_site_factory_tenancy_and_operations.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SiteFactoryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-factory/src/Services/SiteFactoryService.php) | `public function templates(): Collection`<br>`public function template(string $key, string $name, array $configuration = [], array $initialContent = [], ?int $teamId = null): SiteTemplate`<br>`public function updateTemplate(SiteTemplate $template, string $name, array $configuration, array $initialContent): SiteTemplate`<br>`public function activateTemplate(SiteTemplate $template): SiteTemplate`<br>`public function deactivateTemplate(SiteTemplate $template): SiteTemplate`<br>`public function provision(string $key, string $name, ?string $templateKey = null, ?string $domain = null, ?int $teamId = null): Site`<br>`public function addDomain(Site $site, string $domain): SiteDomain`<br>`public function verifyDomain(SiteDomain $domain, string $token): SiteDomain`<br>`public function clone(Site $source, string $key, string $name): Site`<br>`public function suspend(Site $site): Site`<br>`public function archive(Site $site): Site`<br>`public function transition(Site $site, string $status): Site`<br>`public function teardown(Site $site, bool $confirm = false): void`<br>`public function operations(?Site $site = null): Collection` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SiteDomain.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-factory/src/Models/SiteDomain.php) | `site_id`, `domain`, `verification_token`, `verified_at`, `team_id` |
| [SiteFactoryOperation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-factory/src/Models/SiteFactoryOperation.php) | `site_id`, `team_id`, `operation`, `status`, `payload`, `error`, `completed_at` |
| [SiteTemplate.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-factory/src/Models/SiteTemplate.php) | `key`, `name`, `configuration`, `initial_content`, `active`, `team_id` |

### Consuming adapter specifications

- [HTTP API contract](../api/module-cms-site-factory.md) · [Filament 5](../filament/module-cms-site-factory.md) · [Livewire 4](../livewire/module-cms-site-factory.md) · [React + Inertia](../react/module-cms-site-factory.md) · [Vue + Inertia](../vue/module-cms-site-factory.md) · [Nuxt 4](../nuxt/module-cms-site-factory.md) · [Next.js](../nextjs/module-cms-site-factory.md) · [React Native](../react-native/module-cms-site-factory.md) · [Flutter & Dart](../flutter/module-cms-site-factory.md)
<!-- core-implementation-plan:end -->
