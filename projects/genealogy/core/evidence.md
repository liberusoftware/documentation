# Genealogy: Evidence Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#evidence). Observed identity: [`liberusoftware/module-genealogy-evidence`](../../../modules/source/liberusoftware--module-genealogy-evidence.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-genealogy-evidence`
**Domain specification:** [Evidence](../features/evidence.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Evidence. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Sources** | Model `sources` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Repositories** | Model `repositories` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Citations** | Model `citations` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Extracts** | Model `extracts` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Assertions** | Model `assertions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Confidence** | Model `confidence` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Proof conclusions** | Model `proof conclusions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_24_010000_create_evidence_records_table.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/database/migrations/2026_08_24_010000_create_evidence_records_table.php) · [2026_08_24_020000_add_evidence_semantics.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/database/migrations/2026_08_24_020000_add_evidence_semantics.php) · [2026_08_25_040000_create_evidence_supporting_records.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/database/migrations/2026_08_25_040000_create_evidence_supporting_records.php) · [2026_08_25_050000_create_citation_links.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/database/migrations/2026_08_25_050000_create_citation_links.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveEvidenceRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/ArchiveEvidenceRecord.php) | `public function execute(EvidenceRecord $record): EvidenceRecord` |
| [CreateAssertion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateAssertion.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Assertion` |
| [CreateCitation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateCitation.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Citation` |
| [CreateCitationLink.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateCitationLink.php) | `public function execute(array $attributes): CitationLink` |
| [CreateEvidenceEntity.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateEvidenceEntity.php) | `public function execute(string $modelClass, array $attributes): Model`<br>`public function validate(array $values, string $modelClass): void` |
| [CreateEvidenceRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateEvidenceRecord.php) | `public function execute(array $attributes): EvidenceRecord`<br>`public function validate(array $values): void` |
| [CreateExtract.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateExtract.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Extract` |
| [CreateProofConclusion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateProofConclusion.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): ProofConclusion` |
| [CreateRepository.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateRepository.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Repository` |
| [CreateSource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Actions/CreateSource.php) | `public function __construct(private readonly CreateEvidenceEntity $create)`<br>`public function execute(array $attributes): Source` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Assertion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Assertion.php) | `subject_person_id`, `citation_id`, `extract_id`, `statement`, `confidence`, `status`, `metadata` |
| [Citation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Citation.php) | `source_id`, `repository_id`, `title`, `volume`, `page`, `text`, `confidence`, `event_date`, `metadata` |
| [CitationLink.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/CitationLink.php) | `team_id`, `citation_id`, `subject_person_id`, `group`, `page`, `quality`, `text`, `metadata` |
| [EvidenceRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/EvidenceRecord.php) | `team_id`, `name`, `kind`, `repository`, `citation`, `extract`, `assertion`, `proof_conclusion`, `confidence`, `source_url`, `event_date`, `subject_person_id`, `reviewed_at`, `status`, `metadata` |
| [Extract.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Extract.php) | `citation_id`, `content`, `transcription`, `page`, `metadata` |
| [ProofConclusion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/ProofConclusion.php) | `assertion_id`, `conclusion`, `confidence`, `status`, `metadata` |
| [Repository.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Repository.php) | `source_id`, `name`, `description`, `address`, `url`, `email`, `is_active`, `metadata` |
| [Source.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence/src/Models/Source.php) | `name`, `description`, `url`, `archive_metadata`, `record_type`, `is_active`, `metadata` |

### Consuming adapter specifications

- [HTTP API contract](../api/evidence.md) · [Filament 5](../filament/evidence.md) · [Livewire 4](../livewire/evidence.md) · [React + Inertia](../react/evidence.md) · [Vue + Inertia](../vue/evidence.md) · [Nuxt 4](../nuxt/evidence.md) · [Next.js](../nextjs/evidence.md) · [React Native](../react-native/evidence.md) · [Flutter & Dart](../flutter/evidence.md)
<!-- core-implementation-plan:end -->
