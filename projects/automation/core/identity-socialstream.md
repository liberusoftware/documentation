# Automation: Identity Socialstream Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#identity-socialstream). Observed identity: [`liberusoftware/identity-socialstream`](../../../modules/source/liberusoftware--identity-socialstream.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-automation-identity-socialstream`
**Domain specification:** [Identity Socialstream](../features/identity-socialstream.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Identity Socialstream. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Social provider redirects** | Model `social provider redirects` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Callbacks** | Model `callbacks` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Identity linking** | Model `identity linking` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Protected credentials** | Model `protected credentials` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Account synchronization** | Model `account synchronization` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_06_29_123954_make_password_nullable_on_users_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/database/migrations/2026_06_29_123954_make_password_nullable_on_users_table.php) · [2026_06_29_123955_create_connected_accounts_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/database/migrations/2026_06_29_123955_create_connected_accounts_table.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateConnectedAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/CreateConnectedAccount.php) | `public function create(mixed $user, string $provider, ProviderUser $providerUser): ConnectedAccount` |
| [CreateUserFromProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/CreateUserFromProvider.php) | `public function __construct(CreatesConnectedAccounts $createsConnectedAccounts)`<br>`public function create(string $provider, ProviderUserContract $providerUser): User` |
| [GenerateRedirectForProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/GenerateRedirectForProvider.php) | `public function generate(string $provider): RedirectResponse` |
| [HandleInvalidState.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/HandleInvalidState.php) | `public function handle(InvalidStateException $exception): Response` |
| [ResolveSocialiteUser.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/ResolveSocialiteUser.php) | `public function resolve(string $provider): User` |
| [SetUserPassword.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/SetUserPassword.php) | `public function set(mixed $user, array $input): void` |
| [UpdateConnectedAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/UpdateConnectedAccount.php) | `public function update(mixed $user, ConnectedAccount $connectedAccount, string $provider, User $providerUser): ConnectedAccount`<br>`public function updateRefreshToken(ConnectedAccount $connectedAccount): ConnectedAccount` |
| [ConnectedAccountOwner.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Contracts/ConnectedAccountOwner.php) | `public function ownsConnectedAccount($account)` |
| [ConnectedAccountPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Policies/ConnectedAccountPolicy.php) | `public function viewAny(ConnectedAccountOwner $user): bool`<br>`public function view(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool`<br>`public function create(ConnectedAccountOwner $user): bool`<br>`public function update(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool`<br>`public function delete(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConnectedAccount.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/identity-socialstream/src/Models/ConnectedAccount.php) | `provider`, `provider_id`, `name`, `nickname`, `email`, `avatar_path`, `token`, `secret`, `refresh_token`, `expires_at` |

### Consuming adapter specifications

- [HTTP API contract](../api/identity-socialstream.md) · [Filament 5](../filament/identity-socialstream.md) · [Livewire 4](../livewire/identity-socialstream.md) · [React + Inertia](../react/identity-socialstream.md) · [Vue + Inertia](../vue/identity-socialstream.md) · [Nuxt 4](../nuxt/identity-socialstream.md) · [Next.js](../nextjs/identity-socialstream.md) · [React Native](../react-native/identity-socialstream.md) · [Flutter & Dart](../flutter/identity-socialstream.md)
<!-- core-implementation-plan:end -->
