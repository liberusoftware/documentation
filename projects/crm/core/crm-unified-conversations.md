# CRM: Crm Unified Conversations Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-unified-conversations). Observed identity: [`liberusoftware/module-crm-unified-conversations`](../../../modules/source/liberusoftware--module-crm-unified-conversations.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-crm-crm-unified-conversations`
**Domain specification:** [Crm Unified Conversations](../features/crm-unified-conversations.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Crm Unified Conversations. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Omnichannel threads** | Model `omnichannel threads` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Participants** | Model `participants` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Identity matching** | Model `identity matching` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Assignments** | Model `assignments` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Collision detection** | Model `collision detection` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Drafts** | Model `drafts` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Internal notes** | Model `internal notes` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Attachments** | Model `attachments` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Delivery/read state** | Model `delivery/read state` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Timeline** | Model `timeline` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_25_050000_create_crm_unified_conversations_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/database/migrations/2026_08_25_050000_create_crm_unified_conversations_tables.php) · [2026_08_30_120000_add_inbox_metadata.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/database/migrations/2026_08_30_120000_add_inbox_metadata.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ConversationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Queries/ConversationQuery.php) | `public function list(int $teamId)`<br>`public function find(int $teamId, int $id): Conversation` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AssignConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/AssignConversation.php) | `public function execute(int $teamId, int $actorId, int $conversationId, ?int $assignee): Conversation` |
| [OpenConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/OpenConversation.php) | `public function execute(int $teamId, int $actorId, array $data): Conversation` |
| [SendMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/SendMessage.php) | `public function execute(int $teamId, int $actorId, int $conversationId, array $data): ConversationMessage` |
| [SyncExternalConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/SyncExternalConversation.php) | `public function execute(int $teamId, array $data): Conversation` |
| [ConversationAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Services/ConversationAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [ConversationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Services/ConversationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/Conversation.php) | `team_id`, `channel`, `external_id`, `subject`, `status`, `priority`, `assigned_to`, `last_message_at`, `metadata` |
| [ConversationAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/ConversationAudit.php) | `team_id`, `actor_id`, `event`, `details` |
| [ConversationMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/ConversationMessage.php) | `team_id`, `conversation_id`, `external_id`, `sender_id`, `body`, `direction`, `metadata`, `internal`, `delivery_status`, `read_at`, `idempotency_key` |
| [ConversationParticipant.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/ConversationParticipant.php) | `team_id`, `conversation_id`, `identity`, `name`, `role` |

### Consuming adapter specifications

- [HTTP API contract](../api/crm-unified-conversations.md) · [Filament 5](../filament/crm-unified-conversations.md) · [Livewire 4](../livewire/crm-unified-conversations.md) · [React + Inertia](../react/crm-unified-conversations.md) · [Vue + Inertia](../vue/crm-unified-conversations.md) · [Nuxt 4](../nuxt/crm-unified-conversations.md) · [Next.js](../nextjs/crm-unified-conversations.md) · [React Native](../react-native/crm-unified-conversations.md) · [Flutter & Dart](../flutter/crm-unified-conversations.md)
<!-- core-implementation-plan:end -->
