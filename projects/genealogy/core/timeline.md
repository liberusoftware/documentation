# Genealogy: Timeline Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#timeline). Observed identity: [`liberusoftware/module-genealogy-timeline`](../../../modules/source/liberusoftware--module-genealogy-timeline.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-genealogy-timeline`
**Domain specification:** [Timeline](../features/timeline.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Timeline. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Personal/family timelines** | Model `personal/family timelines` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Historical context** | Model `historical context` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Conflicts** | Model `conflicts` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Chronological navigation** | Model `chronological navigation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_24_010000_create_timeline_events_table.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/database/migrations/2026_08_24_010000_create_timeline_events_table.php) · [2026_08_24_020000_add_timeline_semantics.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/database/migrations/2026_08_24_020000_add_timeline_semantics.php) · [2026_08_30_040000_create_genealogy_historical_events_table.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/database/migrations/2026_08_30_040000_create_genealogy_historical_events_table.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ChronologicalTimeline.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Queries/ChronologicalTimeline.php) | `public function execute(?string $subjectPersonId = null, ?string $familyKey = null, ?string $from = null, ?string $to = null, bool $includePrivate = false): array` |
| [ConflictingTimelineEvents.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Queries/ConflictingTimelineEvents.php) | `public function execute(?string $subjectPersonId = null, bool $includePrivate = false): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateTimelineEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Actions/CreateTimelineEvent.php) | `public function __construct(private readonly ?PersonReferenceResolver $personReference = null)`<br>`public function execute(array $attributes): TimelineEvent`<br>`public function validate(array $values): void` |
| [DeleteTimelineEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Actions/DeleteTimelineEvent.php) | `public function execute(TimelineEvent $event): void` |
| [UpdateTimelineEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Actions/UpdateTimelineEvent.php) | `public function __construct(private readonly ?PersonReferenceResolver $personReference = null)`<br>`public function execute(TimelineEvent $event, array $attributes): TimelineEvent` |
| [HistoricalEventService.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Services/HistoricalEventService.php) | `public function fetchForPeriod(string\|\DateTimeInterface $start, string\|\DateTimeInterface $end, ?string $country = null): Collection`<br>`public function fetchForPerson(Model $person, int $bufferYears = 5): Collection` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [HistoricalEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Models/HistoricalEvent.php) | `title`, `description`, `event_date`, `year`, `month`, `day`, `place`, `country`, `latitude`, `longitude`, `source_url` |
| [TimelineEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-timeline/src/Models/TimelineEvent.php) | `team_id`, `kind`, `name`, `subject_person_id`, `family_key`, `event_date`, `date_start`, `date_end`, `date_precision`, `place_id`, `description`, `historical_context`, `conflict_group`, `confidence`, `source_reference`, `is_private`, `status`, `metadata` |

### Consuming adapter specifications

- [HTTP API contract](../api/timeline.md) · [Filament 5](../filament/timeline.md) · [Livewire 4](../livewire/timeline.md) · [React + Inertia](../react/timeline.md) · [Vue + Inertia](../vue/timeline.md) · [Nuxt 4](../nuxt/timeline.md) · [Next.js](../nextjs/timeline.md) · [React Native](../react-native/timeline.md) · [Flutter & Dart](../flutter/timeline.md)
<!-- core-implementation-plan:end -->
