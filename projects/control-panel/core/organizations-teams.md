# Control Panel: Organizations Teams Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#organizations-teams). Observed identity: [`liberusoftware/organizations-teams`](../../../modules/source/liberusoftware--organizations-teams.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-control-panel-organizations-teams`
**Domain specification:** [Organizations Teams](../features/organizations-teams.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Organizations Teams. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Organizations** | Model `organizations` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Teams** | Model `teams` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Memberships** | Model `memberships` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Invitations** | Model `invitations` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Ownership** | Model `ownership` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Switching** | Model `switching` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Transfer** | Model `transfer` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Lifecycle** | Model `lifecycle` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2020_05_21_100000_create_teams_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2020_05_21_100000_create_teams_table.php) · [2020_05_21_200000_create_team_user_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2020_05_21_200000_create_team_user_table.php) · [2020_05_21_300000_create_team_invitations_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2020_05_21_300000_create_team_invitations_table.php) · [2024_01_10_000000_create_team_subscriptions_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2024_01_10_000000_create_team_subscriptions_table.php) · [2024_09_29_093707_add_team_to_resources.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2024_09_29_093707_add_team_to_resources.php) · [2024_11_17_000000_add_team_id_to-staff_resource_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2024_11_17_000000_add_team_id_to-staff_resource_tables.php) · [2026_07_06_000001_add_team_id_to_tenant_scoped_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_06_000001_add_team_id_to_tenant_scoped_tables.php) · [2026_07_06_000002_enable_spatie_teams_columns.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_06_000002_enable_spatie_teams_columns.php) · [2026_07_06_190000_add_archived_at_to_teams_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_06_190000_add_archived_at_to_teams_table.php) · [2026_07_06_200000_create_team_backups_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_06_200000_create_team_backups_table.php) · [2026_07_07_120000_add_team_id_to_tickets_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_07_120000_add_team_id_to_tickets_table.php) · [2026_07_08_030000_create_territories_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_08_030000_create_territories_table.php) · [2026_07_08_030001_create_territory_user_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_08_030001_create_territory_user_table.php) · [2026_07_08_080000_add_portal_branding_to_teams_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_08_080000_add_portal_branding_to_teams_table.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AcceptInvitation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/AcceptInvitation.php) | `public function handle(string $token, Authenticatable $actor, string $email): void` |
| [InviteMember.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/InviteMember.php) | `public function handle(int $teamId, string $email, string $role, int\|string $inviterId, ?\DateTimeImmutable $expiresAt = null): string` |
| [TransferOwnership.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/TransferOwnership.php) | `public function handle(Team $team, int\|string $currentOwner, int\|string $successor, bool $recentlyAuthenticated): void` |
| [OrganizationActor.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Contracts/OrganizationActor.php) | `public function belongsToTeam($team)`<br>`public function ownsTeam($team)` |
| [TeamPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Policies/TeamPolicy.php) | `public function viewAny(OrganizationActor $user): bool`<br>`public function view(OrganizationActor $user, Team $team): bool`<br>`public function create(OrganizationActor $user): bool`<br>`public function update(OrganizationActor $user, Team $team): bool`<br>`public function addTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function updateTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function removeTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function delete(OrganizationActor $user, Team $team): bool` |
| [CurrentTeamResolver.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Services/CurrentTeamResolver.php) | `public function resolve(Authenticatable $actor, int\|string\|null $requested): ?Team` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Membership.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/Membership.php) | No literal fillable array detected; inspect the model and API schema. |
| [Organization.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/Organization.php) | `name`, `slug`, `owner_id`, `status`, `archived_at` |
| [Team.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/Team.php) | `name`, `personal_team`, `organization_id`, `status` |
| [TeamInvitation.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/TeamInvitation.php) | `email`, `role`, `token_hash`, `invited_by`, `expires_at`, `accepted_at`, `revoked_at` |

### Consuming adapter specifications

- [HTTP API contract](../api/organizations-teams.md) · [Filament 5](../filament/organizations-teams.md) · [Livewire 4](../livewire/organizations-teams.md) · [React + Inertia](../react/organizations-teams.md) · [Vue + Inertia](../vue/organizations-teams.md) · [Nuxt 4](../nuxt/organizations-teams.md) · [Next.js](../nextjs/organizations-teams.md) · [React Native](../react-native/organizations-teams.md) · [Flutter & Dart](../flutter/organizations-teams.md)
<!-- core-implementation-plan:end -->
