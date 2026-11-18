# Social Network: Social Network Profiles Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-profiles). Observed identity: [`liberusoftware/module-social-network-profiles`](../../../modules/source/liberusoftware--module-social-network-profiles.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-social-network-social-network-profiles`
**Domain specification:** [Social Network Profiles](../features/social-network-profiles.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Social Network Profiles. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Handles** | Model `handles` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Bios** | Model `bios` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Attributes** | Model `attributes` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Avatars** | Model `avatars` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Verification** | Model `verification` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Visibility** | Model `visibility` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Blocking** | Model `blocking` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Profile lifecycle** | Model `profile lifecycle` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_24_010000_create_social_profiles_table.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/database/migrations/2026_08_24_010000_create_social_profiles_table.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [BlockProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/BlockProfile.php) | `public function __construct(private ProfileAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $blocker, Profile $blocked): void` |
| [GetProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/GetProfile.php) | `public function __construct(private ProfileRepository $profiles, private ProfileAuthorizer $authorizer)`<br>`public function byId(string $id): Profile`<br>`public function forUser(int\|string $userId): Profile` |
| [UnblockProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/UnblockProfile.php) | `public function __construct(private ProfileAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $blocker, Profile $blocked): void` |
| [UpdateLifecycleState.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/UpdateLifecycleState.php) | `public function __construct(private Dispatcher $events)`<br>`public function handle(Profile $profile, string $state): Profile` |
| [UpdateProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/UpdateProfile.php) | `public function __construct(private ProfileRepository $profiles, private ProfileAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile, array $attributes): Profile` |
| [UpdateVerificationStatus.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/UpdateVerificationStatus.php) | `public function __construct(private Dispatcher $events)`<br>`public function handle(Profile $profile, string $status): Profile` |
| [ProfileAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Contracts/ProfileAuthorizer.php) | `public function view(Profile $profile): void`<br>`public function update(Profile $profile): void`<br>`public function block(Profile $profile, Profile $target): void` |
| [ProfileRepository.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Contracts/ProfileRepository.php) | `public function forUser(int\|string $userId): Profile`<br>`public function find(string $id): Profile` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Profile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Models/Profile.php) | `id`, `user_id`, `handle`, `bio`, `attributes`, `avatar_path`, `verification_status`, `visibility`, `lifecycle_state` |

### Consuming adapter specifications

- [HTTP API contract](../api/social-network-profiles.md) · [Filament 5](../filament/social-network-profiles.md) · [Livewire 4](../livewire/social-network-profiles.md) · [React + Inertia](../react/social-network-profiles.md) · [Vue + Inertia](../vue/social-network-profiles.md) · [Nuxt 4](../nuxt/social-network-profiles.md) · [Next.js](../nextjs/social-network-profiles.md) · [React Native](../react-native/social-network-profiles.md) · [Flutter & Dart](../flutter/social-network-profiles.md)
<!-- core-implementation-plan:end -->
