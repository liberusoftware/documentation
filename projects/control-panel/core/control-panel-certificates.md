# Control Panel: Control Panel Certificates Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-certificates). Observed identity: [`liberusoftware/module-control-panel-certificates`](../../../modules/source/liberusoftware--module-control-panel-certificates.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-control-panel-control-panel-certificates`
**Domain specification:** [Control Panel Certificates](../features/control-panel-certificates.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Control Panel Certificates. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **ACME accounts** | Model `acme accounts` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Issuance** | Model `issuance` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Deployment** | Model `deployment` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Renewal** | Model `renewal` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Revocation** | Model `revocation` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Expiry monitoring** | Model `expiry monitoring` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_24_020000_create_control_panel_certificates_table.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/database/migrations/2026_08_24_020000_create_control_panel_certificates_table.php) · [2026_08_24_120001_create_control_panel_certificate_operations.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/database/migrations/2026_08_24_120001_create_control_panel_certificate_operations.php) · [2026_08_24_140004_create_control_panel_certificate_lifecycle.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/database/migrations/2026_08_24_140004_create_control_panel_certificate_lifecycle.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListCertificates.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Queries/ListCertificates.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CheckCertificateExpiry.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/CheckCertificateExpiry.php) | `public function execute(Certificate $certificate, int $thresholdDays = 30): CertificateExpiryAlert` |
| [ExpireCertificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/ExpireCertificate.php) | `public function execute(Certificate $certificate): Certificate` |
| [IssueCertificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/IssueCertificate.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): Certificate` |
| [RecordCertificateOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RecordCertificateOperation.php) | `public function execute(array $attributes): CertificateOperation` |
| [RegisterAcmeAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RegisterAcmeAccount.php) | `public function execute(array $attributes): AcmeAccount` |
| [RegisterCertificateLifecycle.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RegisterCertificateLifecycle.php) | `public function execute(array $a): Model` |
| [RequestCertificateDeployment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RequestCertificateDeployment.php) | `public function execute(Certificate $certificate, array $attributes): CertificateDeployment` |
| [RequestCertificateRenewal.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RequestCertificateRenewal.php) | `public function execute(Certificate $certificate, ?\DateTimeInterface $scheduledAt = null): CertificateRenewal` |
| [RevokeCertificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/RevokeCertificate.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(Certificate $certificate): Certificate` |
| [UpdateCertificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Actions/UpdateCertificate.php) | `public function execute(Certificate $certificate, array $attributes): Certificate` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AcmeAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/AcmeAccount.php) | `id`, `team_id`, `email`, `directory`, `credentials`, `active` |
| [Certificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/Certificate.php) | `team_id`, `domains`, `status`, `issuer`, `certificate_pem`, `private_key`, `issued_at`, `expires_at`, `metadata` |
| [CertificateDeployment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/CertificateDeployment.php) | `id`, `team_id`, `certificate_id`, `target_type`, `target_id`, `status`, `deployed_at`, `error`, `metadata` |
| [CertificateExpiryAlert.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/CertificateExpiryAlert.php) | `id`, `team_id`, `certificate_id`, `threshold_days`, `status`, `notified_at`, `metadata` |
| [CertificateOperation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/CertificateOperation.php) | `id`, `team_id`, `certificate_id`, `operation`, `status`, `details`, `completed_at` |
| [CertificateRenewal.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates/src/Models/CertificateRenewal.php) | `id`, `team_id`, `certificate_id`, `scheduled_at`, `started_at`, `completed_at`, `status`, `attempts`, `error` |

### Consuming adapter specifications

- [HTTP API contract](../api/control-panel-certificates.md) · [Filament 5](../filament/control-panel-certificates.md) · [Livewire 4](../livewire/control-panel-certificates.md) · [React + Inertia](../react/control-panel-certificates.md) · [Vue + Inertia](../vue/control-panel-certificates.md) · [Nuxt 4](../nuxt/control-panel-certificates.md) · [Next.js](../nextjs/control-panel-certificates.md) · [React Native](../react-native/control-panel-certificates.md) · [Flutter & Dart](../flutter/control-panel-certificates.md)
<!-- core-implementation-plan:end -->
