# CRM: Crm Proposals And Quotes Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-proposals-and-quotes). Observed identity: [`liberusoftware/module-crm-proposals-and-quotes`](../../../modules/source/liberusoftware--module-crm-proposals-and-quotes.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-crm-crm-proposals-and-quotes`
**Domain specification:** [Crm Proposals And Quotes](../features/crm-proposals-and-quotes.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Crm Proposals And Quotes. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Branded templates** | Model `branded templates` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Sections** | Model `sections` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Scope** | Model `scope` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Line items** | Model `line items` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Optional choices** | Model `optional choices` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Versions** | Model `versions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Comments** | Model `comments` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Approvals** | Model `approvals` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Delivery** | Model `delivery` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Engagement** | Model `engagement` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Acceptance** | Model `acceptance` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Expiry** | Model `expiry` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_26_040000_create_crm_proposals_and_quotes_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/database/migrations/2026_08_26_040000_create_crm_proposals_and_quotes_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ProposalQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Queries/ProposalQuery.php) | `public function templates(int $teamId)`<br>`public function proposals(int $teamId)`<br>`public function versions(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddProposalComment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/AddProposalComment.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalEvent` |
| [ChangeProposalStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/ChangeProposalStatus.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $proposalId, string $status): Proposal` |
| [CreateProposal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposal.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Proposal` |
| [CreateProposalTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposalTemplate.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalTemplate` |
| [CreateProposalVersion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposalVersion.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalVersion` |
| [UpdateProposal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/UpdateProposal.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $proposalId, array $input): Proposal` |
| [ProposalPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Services/ProposalPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Proposal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/Proposal.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalTemplate.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalVersion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalVersion.php) | No literal fillable array detected; inspect the model and API schema. |

### Consuming adapter specifications

- [HTTP API contract](../api/crm-proposals-and-quotes.md) · [Filament 5](../filament/crm-proposals-and-quotes.md) · [Livewire 4](../livewire/crm-proposals-and-quotes.md) · [React + Inertia](../react/crm-proposals-and-quotes.md) · [Vue + Inertia](../vue/crm-proposals-and-quotes.md) · [Nuxt 4](../nuxt/crm-proposals-and-quotes.md) · [Next.js](../nextjs/crm-proposals-and-quotes.md) · [React Native](../react-native/crm-proposals-and-quotes.md) · [Flutter & Dart](../flutter/crm-proposals-and-quotes.md)
<!-- core-implementation-plan:end -->
