# Genealogy: Genealogy People Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-people). Observed identity: [`liberusoftware/module-genealogy-people`](../../../modules/source/liberusoftware--module-genealogy-people.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-genealogy-genealogy-people`
**Domain specification:** [Genealogy People](../features/genealogy-people.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Genealogy People. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Names** | Model `names` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Identities** | Model `identities` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Attributes** | Model `attributes` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Life events** | Model `life events` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Living/deceased status** | Model `living/deceased status` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Merge candidates** | Model `merge candidates` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_24_000000_create_genealogy_people_table.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/database/migrations/2026_08_24_000000_create_genealogy_people_table.php) · [2026_08_24_020000_add_people_lifecycle_indexes.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/database/migrations/2026_08_24_020000_add_people_lifecycle_indexes.php) · [2026_08_25_010000_add_public_visibility_to_genealogy_people.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/database/migrations/2026_08_25_010000_add_public_visibility_to_genealogy_people.php) · [2026_08_25_020000_create_people_supporting_records.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/database/migrations/2026_08_25_020000_create_people_supporting_records.php) · [2026_08_25_030000_create_person_associations.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/database/migrations/2026_08_25_030000_create_person_associations.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateMergeCandidate.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreateMergeCandidate.php) | `public function execute(array $attributes): MergeCandidate` |
| [CreatePerson.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePerson.php) | `public function execute(array $attributes): Person` |
| [CreatePersonAssociation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonAssociation.php) | `public function execute(array $attributes): PersonAssociation` |
| [CreatePersonIdentity.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonIdentity.php) | `public function execute(array $attributes): PersonIdentity` |
| [CreatePersonLifeEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonLifeEvent.php) | `public function execute(array $attributes): PersonLifeEvent` |
| [CreatePersonName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonName.php) | `public function execute(array $attributes): PersonName` |
| [DeletePerson.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/DeletePerson.php) | `public function execute(Person $person): void` |
| [DeletePersonAssociation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/DeletePersonAssociation.php) | `public function execute(PersonAssociation $association): void` |
| [DeletePersonSupportingRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/DeletePersonSupportingRecord.php) | `public function execute(Model $record): void` |
| [MergePersons.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/MergePersons.php) | `public function execute(Person $primary, Person $duplicate): Person` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MergeCandidate.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/MergeCandidate.php) | `team_id`, `person_id`, `candidate_person_id`, `status`, `score`, `reason`, `metadata`, `reviewed_at` |
| [Person.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/Person.php) | `team_id`, `given_name`, `family_name`, `display_name`, `sex`, `aliases`, `attributes`, `birth_date`, `death_date`, `birth_place`, `death_place`, `is_public`, `metadata` |
| [PersonAssociation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonAssociation.php) | `team_id`, `person_id`, `associated_person_id`, `associated_external_id`, `relationship`, `description`, `metadata` |
| [PersonIdentity.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonIdentity.php) | `team_id`, `person_id`, `type`, `value`, `label`, `is_verified`, `metadata` |
| [PersonLifeEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonLifeEvent.php) | `team_id`, `person_id`, `type`, `date`, `place`, `description`, `metadata` |
| [PersonName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonName.php) | `team_id`, `person_id`, `type`, `given_name`, `family_name`, `prefix`, `suffix`, `is_preferred`, `metadata` |

### Consuming adapter specifications

- [HTTP API contract](../api/genealogy-people.md) · [Filament 5](../filament/genealogy-people.md) · [Livewire 4](../livewire/genealogy-people.md) · [React + Inertia](../react/genealogy-people.md) · [Vue + Inertia](../vue/genealogy-people.md) · [Nuxt 4](../nuxt/genealogy-people.md) · [Next.js](../nextjs/genealogy-people.md) · [React Native](../react-native/genealogy-people.md) · [Flutter & Dart](../flutter/genealogy-people.md)
<!-- core-implementation-plan:end -->
