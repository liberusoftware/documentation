# Control Panel: Web Hosting Core Module

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#web-hosting). Observed identity: [`liberusoftware/module-control-panel-web-hosting`](../../../modules/source/liberusoftware--module-control-panel-web-hosting.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Package contract

**Design package identifier:** `module-control-panel-web-hosting`
**Domain specification:** [Web Hosting](../features/web-hosting.md)
**Target:** Laravel 13, PHP 8.5, Composer 2, Pest 5

This package is the authoritative, provider-neutral implementation of Web Hosting. It owns domain behavior and data; optional API, Filament, Livewire, React, Vue, and Nuxt packages translate its public contracts for their surfaces.

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
| **Domains** | Model `domains` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Virtual hosts** | Model `virtual hosts` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **PHP/runtime versions** | Model `php/runtime versions` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Web servers** | Model `web servers` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **SSL** | Model `ssl` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Logs** | Model `logs` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Redirects** | Model `redirects` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |
| **Applications** | Model `applications` with explicit value objects, state transitions, and invariant guards inside the domain boundary. | Provide a dedicated application action/query, enforce policy and tenant context, persist inside module-owned tables, and publish post-commit events. |

### Observed domain and transport source evidence

**Observed migration files:** [2026_08_23_020000_create_control_panel_web_hosting_tables.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/database/migrations/2026_08_23_020000_create_control_panel_web_hosting_tables.php) · [2026_08_24_000001_create_control_panel_web_hosting_operations.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/database/migrations/2026_08_24_000001_create_control_panel_web_hosting_operations.php) · [2026_08_24_160000_create_control_panel_git_deployments.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/database/migrations/2026_08_24_160000_create_control_panel_git_deployments.php) · [2026_08_24_170000_create_control_panel_php_configurations.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/database/migrations/2026_08_24_170000_create_control_panel_php_configurations.php) · [2026_08_25_000001_create_control_panel_application_metrics.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/database/migrations/2026_08_25_000001_create_control_panel_application_metrics.php) · [2026_08_30_000001_create_control_panel_resource_usage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/database/migrations/2026_08_30_000001_create_control_panel_resource_usage.php) · [2026_08_30_000003_create_control_panel_web_protection.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/database/migrations/2026_08_30_000003_create_control_panel_web_protection.php) · [2026_08_30_000004_add_redirect_policies_and_mime_types.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/database/migrations/2026_08_30_000004_add_redirect_policies_and_mime_types.php) · [2026_08_30_000006_create_control_panel_cron_tables.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/database/migrations/2026_08_30_000006_create_control_panel_cron_tables.php) · [2026_08_30_000007_create_control_panel_subdomains.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/database/migrations/2026_08_30_000007_create_control_panel_subdomains.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ApplicationStatistics.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Queries/ApplicationStatistics.php) | `public function execute(string\|int $teamId, int $days = 30): array` |
| [ListDomains.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Queries/ListDomains.php) | `public function execute(?string $teamId = null, int $perPage = 25): LengthAwarePaginator` |
| [ListGitDeployments.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Queries/ListGitDeployments.php) | `public function execute(string\|int $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |
| [ListResourceUsage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Queries/ListResourceUsage.php) | `public function execute(string\|int $teamId, ?string $domainId = null, int $months = 12): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/ActivateDomain.php) | `public function execute(Domain $domain): Domain` |
| [AddDirectoryProtectionUser.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/AddDirectoryProtectionUser.php) | `public function execute(DirectoryProtection $protection, string $username, string $password): DirectoryProtectionUser` |
| [ArchiveDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/ArchiveDomain.php) | `public function execute(Domain $domain): Domain` |
| [CheckApplicationHealth.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CheckApplicationHealth.php) | `public function __construct(private readonly RecordApplicationMetric $record)`<br>`public function execute(HostedApplication $application): array` |
| [CheckWordPressUpdates.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CheckWordPressUpdates.php) | `public function execute(HostedApplication $application): array` |
| [ConfigureHotlinkProtection.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/ConfigureHotlinkProtection.php) | `public function execute(Domain $domain, array $attributes): HotlinkProtection` |
| [CreateCronJob.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CreateCronJob.php) | `public function execute(Domain $domain, array $attributes): CronJob`<br>`public function assertSchedule(string $schedule): void` |
| [CreateDirectoryProtection.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CreateDirectoryProtection.php) | `public function execute(Domain $domain, array $attributes): DirectoryProtection` |
| [CreateDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CreateDomain.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): Domain` |
| [CreateMimeType.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CreateMimeType.php) | `public function execute(Domain $domain, array $attributes): MimeType` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ApplicationMetric.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/ApplicationMetric.php) | `id`, `team_id`, `application_id`, `response_time_ms`, `status_code`, `healthy`, `checked_at`, `details` |
| [CronExecution.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/CronExecution.php) | `cron_job_id`, `started_at`, `finished_at`, `exit_code`, `output`, `error_output`, `duration` |
| [CronJob.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/CronJob.php) | `team_id`, `domain_id`, `name`, `command`, `schedule`, `active`, `last_run_at`, `next_run_at`, `output`, `error_output` |
| [CustomErrorPage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/CustomErrorPage.php) | `team_id`, `domain_id`, `error_code`, `custom_content`, `custom_file_path`, `active` |
| [DirectoryProtection.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/DirectoryProtection.php) | `team_id`, `domain_id`, `directory_path`, `auth_name`, `htpasswd_file_path`, `active` |
| [DirectoryProtectionUser.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/DirectoryProtectionUser.php) | `team_id`, `directory_protection_id`, `username`, `password` |
| [Domain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/Domain.php) | `team_id`, `account_id`, `hostname`, `status`, `metadata` |
| [GitDeployment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/GitDeployment.php) | `domain_id`, `team_id`, `connected_account_id`, `use_oauth`, `container_id`, `kubernetes_pod_name`, `kubernetes_namespace`, `repository_url`, `repository_type`, `branch`, `deploy_path`, `deploy_key`, `webhook_secret`, `status`, `deployment_log`, `build_command`, `deploy_command`, `auto_deploy`, `last_deployed_at`, `last_commit_hash` |

### Consuming adapter specifications

- [HTTP API contract](../api/web-hosting.md) · [Filament 5](../filament/web-hosting.md) · [Livewire 4](../livewire/web-hosting.md) · [React + Inertia](../react/web-hosting.md) · [Vue + Inertia](../vue/web-hosting.md) · [Nuxt 4](../nuxt/web-hosting.md) · [Next.js](../nextjs/web-hosting.md) · [React Native](../react-native/web-hosting.md) · [Flutter & Dart](../flutter/web-hosting.md)
<!-- core-implementation-plan:end -->
