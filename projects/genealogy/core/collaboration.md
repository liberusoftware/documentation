# Genealogy: Collaboration Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#collaboration). Observed identity: [`liberusoftware/module-genealogy-collaboration`](../../../modules/source/liberusoftware--module-genealogy-collaboration.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-genealogy-collaboration`
**Domain specification:** [Collaboration](../features/collaboration.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Collaboration. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Invitations** | Model `invitations` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Roles** | Model `roles` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Branch/change proposals** | Model `branch/change proposals` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Review** | Model `review` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Discussions** | Model `discussions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Watch lists** | Model `watch lists` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Attribution** | Model `attribution` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_24_010000_create_genealogy_collaboration_spaces_table.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/database/migrations/2026_08_24_010000_create_genealogy_collaboration_spaces_table.php) · [2026_08_25_060000_create_genealogy_collaboration_proposals_table.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/database/migrations/2026_08_25_060000_create_genealogy_collaboration_proposals_table.php) · [2026_08_25_070000_create_genealogy_collaboration_workflows_tables.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/database/migrations/2026_08_25_070000_create_genealogy_collaboration_workflows_tables.php) · [2026_08_30_030000_create_genealogy_virtual_events_tables.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/database/migrations/2026_08_30_030000_create_genealogy_virtual_events_tables.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AcceptCollaborationInvitation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/AcceptCollaborationInvitation.php) | `public function execute(CollaborationInvitation $invitation, Authenticatable $actor): CollaborationMembership` |
| [CreateCollaborationDiscussion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/CreateCollaborationDiscussion.php) | `public function execute(array $attributes): CollaborationDiscussion` |
| [CreateCollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/CreateCollaborationProposal.php) | `public function execute(array $attributes): CollaborationProposal` |
| [CreateCollaborationSpace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/CreateCollaborationSpace.php) | `public function execute(array $attributes): CollaborationSpace` |
| [DeleteCollaborationDiscussion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/DeleteCollaborationDiscussion.php) | `public function execute(CollaborationDiscussion $discussion): void` |
| [DeleteCollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/DeleteCollaborationProposal.php) | `public function execute(CollaborationProposal $proposal): void` |
| [DeleteCollaborationSpace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/DeleteCollaborationSpace.php) | `public function execute(CollaborationSpace $space): void` |
| [InviteCollaborationMember.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/InviteCollaborationMember.php) | `public function execute(array $attributes): CollaborationInvitation` |
| [RecordCollaborationAttribution.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/RecordCollaborationAttribution.php) | `public function execute(string $type, string $id, string $action, array $metadata = [], string\|int\|null $actorId = null): CollaborationAttribution` |
| [ReviewCollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/ReviewCollaborationProposal.php) | `public function execute(CollaborationProposal $proposal, string $status, string\|int\|null $reviewerId = null): CollaborationProposal` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CollaborationAttribution.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationAttribution.php) | `team_id`, `actor_id`, `attributable_type`, `attributable_id`, `action`, `metadata`, `created_at` |
| [CollaborationDiscussion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationDiscussion.php) | `team_id`, `space_id`, `proposal_id`, `author_id`, `body`, `status`, `metadata` |
| [CollaborationInvitation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationInvitation.php) | `team_id`, `space_id`, `email`, `role`, `status`, `invited_by`, `expires_at`, `accepted_at`, `revoked_at` |
| [CollaborationMembership.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationMembership.php) | `team_id`, `space_id`, `user_id`, `role`, `status`, `joined_at` |
| [CollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationProposal.php) | `team_id`, `proposer_id`, `reviewer_id`, `title`, `description`, `status`, `reviewed_at`, `metadata` |
| [CollaborationSpace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationSpace.php) | `team_id`, `name`, `status`, `metadata` |
| [CollaborationWatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationWatch.php) | `team_id`, `user_id`, `watchable_type`, `watchable_id` |
| [VirtualEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/VirtualEvent.php) | `team_id`, `created_by`, `title`, `description`, `start_time`, `end_time`, `timezone`, `status`, `platform`, `meeting_id`, `meeting_password`, `meeting_url`, `join_url`, `platform_data`, `max_attendees`, `require_rsvp`, `allow_guests`, `instructions`, `host_email` |

### Consuming adapter specifications

- [HTTP API contract](../api/collaboration.md) · [Filament 5](../filament/collaboration.md) · [Livewire 4](../livewire/collaboration.md) · [React + Inertia](../react/collaboration.md) · [Vue + Inertia](../vue/collaboration.md) · [Nuxt 4](../nuxt/collaboration.md) · [Next.js](../nextjs/collaboration.md) · [React Native](../react-native/collaboration.md) · [Flutter & Dart](../flutter/collaboration.md)
<!-- core-implementation-plan:end -->
