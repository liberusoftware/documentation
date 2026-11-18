# Control Panel: Security Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#security). Observed identity: [`liberusoftware/module-control-panel-security`](../../../modules/source/liberusoftware--module-control-panel-security.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-control-panel-security`
**Domain specification:** [Security](../features/security.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Security. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Hardening** | Model `hardening` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Patching** | Model `patching` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **MFA/RBAC** | Model `mfa/rbac` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Secrets** | Model `secrets` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Malware** | Model `malware` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Intrusion controls** | Model `intrusion controls` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Vulnerability and compliance status** | Model `vulnerability and compliance status` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_24_110002_create_control_panel_security_findings.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/database/migrations/2026_08_24_110002_create_control_panel_security_findings.php) · [2026_08_24_110003_create_control_panel_security_controls.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/database/migrations/2026_08_24_110003_create_control_panel_security_controls.php) · [2026_08_30_000004_create_control_panel_fail2ban_tables.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/database/migrations/2026_08_30_000004_create_control_panel_fail2ban_tables.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListFindings.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Queries/ListFindings.php) | `public function execute(string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureFail2ban.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/ConfigureFail2ban.php) | `public function execute(array $attributes): Fail2banSetting` |
| [RecordFail2banBan.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/RecordFail2banBan.php) | `public function execute(Fail2banSetting $setting, array $attributes): Fail2banBan` |
| [RecordFinding.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/RecordFinding.php) | `public function execute(array $attributes): SecurityFinding` |
| [RecordSecurityResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/RecordSecurityResource.php) | `public function execute(string $modelClass, array $attributes): Model` |
| [ResolveSecurityFinding.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/ResolveSecurityFinding.php) | `public function execute(SecurityFinding $finding): SecurityFinding` |
| [StoreSecret.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/StoreSecret.php) | `public function execute(array $attributes): SecretRecord` |
| [UnbanFail2banBan.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/UnbanFail2banBan.php) | `public function execute(Fail2banBan $ban): Fail2banBan` |
| [UpdateSecurityFinding.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Actions/UpdateSecurityFinding.php) | `public function execute(SecurityFinding $finding, array $attributes): SecurityFinding` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ComplianceStatus.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/ComplianceStatus.php) | `team_id`, `framework`, `control`, `status`, `score`, `evidence`, `assessed_at`, `expires_at` |
| [Fail2banBan.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/Fail2banBan.php) | `team_id`, `jail_name`, `ip_address`, `banned_at`, `unbanned_at`, `ban_count`, `reason` |
| [Fail2banSetting.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/Fail2banSetting.php) | `team_id`, `jail_name`, `enabled`, `max_retry`, `find_time`, `ban_time`, `whitelist_ips` |
| [HardeningControl.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/HardeningControl.php) | `team_id`, `subject_type`, `subject_id`, `control`, `desired`, `observed`, `status`, `evidence`, `checked_at` |
| [IntrusionControl.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/IntrusionControl.php) | `team_id`, `subject_type`, `subject_id`, `kind`, `action`, `threshold`, `window_seconds`, `enabled`, `metadata` |
| [MalwareScan.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/MalwareScan.php) | `team_id`, `subject_type`, `subject_id`, `status`, `scanner`, `findings`, `started_at`, `finished_at` |
| [MfaRbacPolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/MfaRbacPolicy.php) | `team_id`, `subject_type`, `subject_id`, `mfa_required`, `roles`, `permissions`, `status`, `metadata` |
| [PatchRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security/src/Models/PatchRecord.php) | `team_id`, `subject_type`, `subject_id`, `package`, `current_version`, `target_version`, `severity`, `status`, `published_at`, `installed_at`, `metadata` |

### Consuming adapter specifications

- [HTTP API contract](../api/security.md) · [Filament 5](../filament/security.md) · [Livewire 4](../livewire/security.md) · [React + Inertia](../react/security.md) · [Vue + Inertia](../vue/security.md) · [Nuxt 4](../nuxt/security.md) · [Next.js](../nextjs/security.md) · [React Native](../react-native/security.md) · [Flutter & Dart](../flutter/security.md)
<!-- core-implementation-plan:end -->
