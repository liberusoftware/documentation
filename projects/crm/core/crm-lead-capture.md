# CRM: Crm Lead Capture Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-lead-capture). Observed identity: [`liberusoftware/module-crm-lead-capture`](../../../modules/source/liberusoftware--module-crm-lead-capture.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-crm-crm-lead-capture`
**Domain specification:** [Crm Lead Capture](../features/crm-lead-capture.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Crm Lead Capture. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Leads inbox** | Model `leads inbox` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Manual/import/API capture** | Model `manual/import/api capture` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Forms** | Model `forms` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Surveys** | Model `surveys` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **QR codes** | Model `qr codes` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Chat** | Model `chat` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Calls** | Model `calls` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Advertisements** | Model `advertisements` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Events** | Model `events` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Referrals** | Model `referrals` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Source metadata** | Model `source metadata` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_24_110000_create_crm_lead_capture_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/database/migrations/2026_08_24_110000_create_crm_lead_capture_tables.php) · [2026_08_26_200000_create_crm_lead_capture_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/database/migrations/2026_08_26_200000_create_crm_lead_capture_tables.php) · [2026_08_30_130000_add_import_key_to_leads.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/database/migrations/2026_08_30_130000_add_import_key_to_leads.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CaptureQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Queries/CaptureQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CaptureLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CaptureLead.php) | `public function __construct(private readonly LeadCapturePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CapturedLead`<br>`public function executeLegacy(int $teamId, ?int $actorId, array $input): LeadCapture` |
| [CreateCaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CreateCaptureForm.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureForm` |
| [CreateCaptureQrCode.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CreateCaptureQrCode.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureQrCode` |
| [RecordCaptureEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/RecordCaptureEvent.php) | `public function __construct(private readonly LeadCapturePolicy $policy)`<br>`public function execute(int $teamId, int $userId, CapturedLead $lead, array $input): CaptureEvent` |
| [RecordReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/RecordReferral.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureReferral` |
| [SubmitCaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/SubmitCaptureForm.php) | `public function execute(CaptureForm $form, ?int $actorId, array $payload): LeadCapture` |
| [UpdateCaptureStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/UpdateCaptureStatus.php) | `public function execute(LeadCapture $capture, string $status, ?string $failureReason = null): LeadCapture` |
| [CaptureDeduplicator.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/CaptureDeduplicator.php) | `public function key(array $attributes): string`<br>`public function find(int $teamId, string $key): ?LeadCapture` |
| [CaptureReport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/CaptureReport.php) | `public function summarize(int $teamId, Carbon $from, Carbon $until): array` |
| [LeadCapturePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/LeadCapturePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CaptureEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [CaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureForm.php) | `team_id`, `actor_id`, `kind`, `name`, `slug`, `status`, `schema`, `settings`, `submissions_count` |
| [CaptureQrCode.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureQrCode.php) | `team_id`, `actor_id`, `name`, `code`, `destination`, `status`, `metadata`, `scan_count` |
| [CaptureReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureReferral.php) | `team_id`, `actor_id`, `code`, `referrer_type`, `referrer_id`, `referred_type`, `referred_id`, `status`, `metadata` |
| [CapturedLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CapturedLead.php) | No literal fillable array detected; inspect the model and API schema. |
| [LeadCapture.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/LeadCapture.php) | `team_id`, `actor_id`, `kind`, `status`, `name`, `email`, `phone`, `source`, `source_medium`, `source_campaign`, `external_id`, `dedupe_key`, `source_metadata`, `payload`, `provenance`, `captured_at`, `processed_at`, `failure_reason` |

### Consuming adapter specifications

- [HTTP API contract](../api/crm-lead-capture.md) · [Filament 5](../filament/crm-lead-capture.md) · [Livewire 4](../livewire/crm-lead-capture.md) · [React + Inertia](../react/crm-lead-capture.md) · [Vue + Inertia](../vue/crm-lead-capture.md) · [Nuxt 4](../nuxt/crm-lead-capture.md) · [Next.js](../nextjs/crm-lead-capture.md) · [React Native](../react-native/crm-lead-capture.md) · [Flutter & Dart](../flutter/crm-lead-capture.md)
<!-- core-implementation-plan:end -->
