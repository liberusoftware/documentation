# Web Hosting: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-control-panel-web-hosting`.

**Proposed design identifier:** `module-control-panel-web-hosting-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/web-hosting.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-control-panel-web-hosting](../../../modules/source/liberusoftware--module-control-panel-web-hosting.md) |
| API | [liberusoftware/module-control-panel-web-hosting-api](../../../modules/source/liberusoftware--module-control-panel-web-hosting-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Domains | A focused authorized view or workflow section for domains; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Virtual hosts | A focused authorized view or workflow section for virtual hosts; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| PHP/runtime versions | A focused authorized view or workflow section for php/runtime versions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Web servers | A focused authorized view or workflow section for web servers; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| SSL | A focused authorized view or workflow section for ssl; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Logs | A focused authorized view or workflow section for logs; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Redirects | A focused authorized view or workflow section for redirects; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Applications | A focused authorized view or workflow section for applications; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ApplicationStatistics.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Queries/ApplicationStatistics.php) | `public function execute(string\|int $teamId, int $days = 30): array` |
| [ListDomains.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Queries/ListDomains.php) | `public function execute(?string $teamId = null, int $perPage = 25): LengthAwarePaginator` |
| [ListGitDeployments.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Queries/ListGitDeployments.php) | `public function execute(string\|int $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |
| [ListResourceUsage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Queries/ListResourceUsage.php) | `public function execute(string\|int $teamId, ?string $domainId = null, int $months = 12): Collection` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ActivateDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/ActivateDomain.php) | `public function execute(Domain $domain): Domain` |
| [AddDirectoryProtectionUser.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/AddDirectoryProtectionUser.php) | `public function execute(DirectoryProtection $protection, string $username, string $password): DirectoryProtectionUser` |
| [ArchiveDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/ArchiveDomain.php) | `public function execute(Domain $domain): Domain` |
| [CheckApplicationHealth.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CheckApplicationHealth.php) | `public function execute(HostedApplication $application): array` |
| [CheckWordPressUpdates.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CheckWordPressUpdates.php) | `public function execute(HostedApplication $application): array` |
| [ConfigureHotlinkProtection.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/ConfigureHotlinkProtection.php) | `public function execute(Domain $domain, array $attributes): HotlinkProtection` |
| [CreateCronJob.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CreateCronJob.php) | `public function execute(Domain $domain, array $attributes): CronJob`<br>`public function assertSchedule(string $schedule): void` |
| [CreateDirectoryProtection.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CreateDirectoryProtection.php) | `public function execute(Domain $domain, array $attributes): DirectoryProtection` |
| [CreateDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CreateDomain.php) | `public function execute(array $attributes): Domain` |
| [CreateMimeType.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CreateMimeType.php) | `public function execute(Domain $domain, array $attributes): MimeType` |
| [CreateRedirect.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CreateRedirect.php) | `public function execute(Domain $domain, array $attributes): Redirect` |
| [CreateSubdomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CreateSubdomain.php) | `public function execute(Domain $domain, array $attributes): Subdomain` |
| [CreateVirtualHost.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/CreateVirtualHost.php) | `public function execute(Domain $domain, array $attributes): VirtualHost` |
| [DeleteCronJob.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/DeleteCronJob.php) | `public function execute(CronJob $job): void` |
| [DeleteCustomErrorPage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/DeleteCustomErrorPage.php) | `public function execute(CustomErrorPage $page): void` |
| [DeleteDirectoryProtection.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/DeleteDirectoryProtection.php) | `public function execute(DirectoryProtection $protection): void` |
| [DeleteHostedApplication.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/DeleteHostedApplication.php) | `public function execute(HostedApplication $application): void` |
| [DeleteRedirect.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/DeleteRedirect.php) | `public function execute(Redirect $redirect): void` |
| [DeleteSubdomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/DeleteSubdomain.php) | `public function execute(Subdomain $subdomain): void` |
| [DeleteVirtualHost.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/DeleteVirtualHost.php) | `public function execute(VirtualHost $virtualHost): void` |
| [RecordApplicationMetric.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/RecordApplicationMetric.php) | `public function execute(HostedApplication $application, array $attributes): ApplicationMetric` |
| [RecordCronExecution.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/RecordCronExecution.php) | `public function execute(CronJob $job, array $attributes): CronExecution` |
| [RecordResourceUsage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/RecordResourceUsage.php) | `public function execute(Domain $domain, array $attributes): ResourceUsage` |
| [RegisterGitDeployment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/RegisterGitDeployment.php) | `public function execute(Domain $domain, array $attributes): GitDeployment` |
| [RegisterHostingResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/RegisterHostingResource.php) | `public function execute(array $attributes): Model` |
| [RemoveDirectoryProtectionUser.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/RemoveDirectoryProtectionUser.php) | `public function execute(DirectoryProtectionUser $user): void` |
| [RequestCertificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/RequestCertificate.php) | `public function execute(Domain $domain, array $attributes = []): SslCertificate` |
| [RequestGitDeployment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/RequestGitDeployment.php) | `public function execute(GitDeployment $deployment): GitDeployment` |
| [SaveCustomErrorPage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/SaveCustomErrorPage.php) | `public function execute(Domain $domain, array $attributes): CustomErrorPage` |
| [SavePhpConfiguration.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/SavePhpConfiguration.php) | `public function execute(Domain $domain, array $attributes): PhpConfiguration` |
| [SuspendDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/SuspendDomain.php) | `public function execute(Domain $domain, string $reason): Domain` |
| [UpdateCronJob.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/UpdateCronJob.php) | `public function execute(CronJob $job, array $attributes): CronJob` |
| [UpdateDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/UpdateDomain.php) | `public function execute(Domain $domain, array $attributes): Domain` |
| [UpdateHostedApplication.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/UpdateHostedApplication.php) | `public function execute(HostedApplication $application, array $attributes): HostedApplication` |
| [UpdateRedirect.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/UpdateRedirect.php) | `public function execute(Redirect $redirect, array $attributes): Redirect` |
| [UpdateSubdomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/UpdateSubdomain.php) | `public function execute(Subdomain $subdomain, array $attributes): Subdomain` |
| [UpdateVirtualHost.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Actions/UpdateVirtualHost.php) | `public function execute(VirtualHost $virtualHost, array $attributes): VirtualHost` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [ApplicationMetric.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/ApplicationMetric.php) | `id`, `team_id`, `application_id`, `response_time_ms`, `status_code`, `healthy`, `checked_at`, `details` |
| [CronExecution.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/CronExecution.php) | `cron_job_id`, `started_at`, `finished_at`, `exit_code`, `output`, `error_output`, `duration` |
| [CronJob.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/CronJob.php) | `team_id`, `domain_id`, `name`, `command`, `schedule`, `active`, `last_run_at`, `next_run_at`, `output`, `error_output` |
| [CustomErrorPage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/CustomErrorPage.php) | `team_id`, `domain_id`, `error_code`, `custom_content`, `custom_file_path`, `active` |
| [DirectoryProtection.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/DirectoryProtection.php) | `team_id`, `domain_id`, `directory_path`, `auth_name`, `htpasswd_file_path`, `active` |
| [DirectoryProtectionUser.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/DirectoryProtectionUser.php) | `team_id`, `directory_protection_id`, `username`, `password` |
| [Domain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/Domain.php) | `team_id`, `account_id`, `hostname`, `status`, `metadata` |
| [GitDeployment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/GitDeployment.php) | `domain_id`, `team_id`, `connected_account_id`, `use_oauth`, `container_id`, `kubernetes_pod_name`, `kubernetes_namespace`, `repository_url`, `repository_type`, `branch`, `deploy_path`, `deploy_key`, `webhook_secret`, `status`, `deployment_log`, `build_command`, `deploy_command`, `auto_deploy`, `last_deployed_at`, `last_commit_hash` |
| [HostedApplication.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/HostedApplication.php) | `team_id`, `domain_id`, `name`, `type`, `version`, `document_root`, `status`, `config` |
| [HostingLog.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/HostingLog.php) | `team_id`, `domain_id`, `kind`, `level`, `message`, `context`, `occurred_at` |
| [HotlinkProtection.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/HotlinkProtection.php) | `team_id`, `domain_id`, `enabled`, `allowed_domains`, `protected_extensions`, `redirect_url`, `allow_blank_referrer` |
| [MimeType.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/MimeType.php) | `team_id`, `domain_id`, `extension`, `mime_type`, `active` |
| [PhpConfiguration.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/PhpConfiguration.php) | `domain_id`, `team_id`, `php_version`, `memory_limit`, `upload_max_filesize`, `post_max_size`, `max_execution_time`, `max_input_time`, `max_input_vars`, `display_errors`, `short_open_tag`, `error_reporting`, `session_save_path`, `custom_settings` |
| [Redirect.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/Redirect.php) | `team_id`, `domain_id`, `source`, `destination`, `status_code`, `active`, `source_path`, `destination_url`, `redirect_type`, `match_query_string`, `is_regex`, `priority` |
| [ResourceUsage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/ResourceUsage.php) | `id`, `team_id`, `domain_id`, `month`, `year`, `disk_usage_mb`, `bandwidth_usage_mb` |
| [RuntimeVersion.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/RuntimeVersion.php) | `team_id`, `runtime`, `version`, `available`, `default`, `metadata` |
| [SslCertificate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/SslCertificate.php) | `team_id`, `domain_id`, `issuer`, `serial`, `status`, `issued_at`, `expires_at`, `auto_renew`, `metadata` |
| [Subdomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/Subdomain.php) | `id`, `domain_id`, `subdomain`, `document_root`, `php_version`, `active`, `redirect_url`, `redirect_type` |
| [VirtualHost.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/VirtualHost.php) | `domain_id`, `node_id`, `server`, `runtime`, `document_root`, `desired_state`, `active` |
| [WebServer.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Models/WebServer.php) | `team_id`, `node_id`, `server`, `version`, `status`, `config`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/control-panel-web-hosting-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/web-hosting')
Route::get('/domains', [DomainController::class, 'index'])->name('control-panel.web-hosting.domains.index');
Route::get('/usage', [DomainController::class, 'usage'])->name('control-panel.web-hosting.usage.index');
Route::post('/domains', [DomainController::class, 'store'])->name('control-panel.web-hosting.domains.store');
Route::patch('/domains/{domain}', [DomainController::class, 'update'])->name('control-panel.web-hosting.domains.update');
Route::post('/domains/{domain}/activate', [DomainController::class, 'activate'])->name('control-panel.web-hosting.domains.activate');
Route::post('/domains/{domain}/suspend', [DomainController::class, 'suspend'])->name('control-panel.web-hosting.domains.suspend');
Route::post('/domains/{domain}/archive', [DomainController::class, 'archive'])->name('control-panel.web-hosting.domains.archive');
Route::get('/domains/{domain}/usage', [DomainController::class, 'domainUsage'])->name('control-panel.web-hosting.domains.usage.index');
Route::post('/domains/{domain}/usage', [DomainController::class, 'recordUsage'])->name('control-panel.web-hosting.domains.usage.store');
Route::get('/domains/{domain}/cron-jobs', [DomainController::class, 'cronJobs'])->name('control-panel.web-hosting.domains.cron-jobs.index');
Route::post('/domains/{domain}/cron-jobs', [DomainController::class, 'createCronJob'])->name('control-panel.web-hosting.domains.cron-jobs.store');
Route::get('/domains/{domain}/subdomains', [DomainController::class, 'subdomains'])->name('control-panel.web-hosting.domains.subdomains.index');
Route::post('/domains/{domain}/subdomains', [DomainController::class, 'createSubdomain'])->name('control-panel.web-hosting.domains.subdomains.store');
Route::patch('/subdomains/{subdomain}', [DomainController::class, 'updateSubdomain'])->name('control-panel.web-hosting.subdomains.update');
Route::delete('/subdomains/{subdomain}', [DomainController::class, 'deleteSubdomain'])->name('control-panel.web-hosting.subdomains.delete');
Route::patch('/cron-jobs/{job}', [DomainController::class, 'updateCronJob'])->name('control-panel.web-hosting.cron-jobs.update');
Route::delete('/cron-jobs/{job}', [DomainController::class, 'deleteCronJob'])->name('control-panel.web-hosting.cron-jobs.delete');
Route::get('/cron-jobs/{job}/executions', [DomainController::class, 'cronExecutions'])->name('control-panel.web-hosting.cron-jobs.executions.index');
Route::post('/cron-jobs/{job}/executions', [DomainController::class, 'recordCronExecution'])->name('control-panel.web-hosting.cron-jobs.executions.store');
Route::post('/domains/{domain}/virtual-hosts', [DomainController::class, 'virtualHost'])->name('control-panel.web-hosting.virtual-hosts.store');
Route::patch('/virtual-hosts/{virtualHost}', [DomainController::class, 'updateVirtualHost'])->name('control-panel.web-hosting.virtual-hosts.update');
Route::delete('/virtual-hosts/{virtualHost}', [DomainController::class, 'deleteVirtualHost'])->name('control-panel.web-hosting.virtual-hosts.delete');
Route::post('/domains/{domain}/redirects', [DomainController::class, 'redirect'])->name('control-panel.web-hosting.redirects.store');
Route::patch('/redirects/{redirect}', [DomainController::class, 'updateRedirect'])->name('control-panel.web-hosting.redirects.update');
Route::delete('/redirects/{redirect}', [DomainController::class, 'deleteRedirect'])->name('control-panel.web-hosting.redirects.delete');
Route::post('/domains/{domain}/mime-types', [DomainController::class, 'mimeType'])->name('control-panel.web-hosting.mime-types.store');
Route::post('/domains/{domain}/certificates', [DomainController::class, 'certificate'])->name('control-panel.web-hosting.certificates.store');
Route::get('/deployments', [DomainController::class, 'deployments'])->name('control-panel.web-hosting.deployments.index');
Route::post('/deployments/{deployment}/deploy', [DomainController::class, 'deploy'])->name('control-panel.web-hosting.deployments.deploy');
Route::post('/domains/{domain}/deployments', [DomainController::class, 'deployment'])->name('control-panel.web-hosting.deployments.store');
Route::put('/domains/{domain}/php-configuration', [DomainController::class, 'phpConfiguration'])->name('control-panel.web-hosting.php-configuration.update');
Route::post('/resources', [DomainController::class, 'resourceRecord'])->name('control-panel.web-hosting.resources.store');
Route::get('/resources/{kind}', [DomainController::class, 'resources'])->name('control-panel.web-hosting.resources.index');
Route::get('/applications', [DomainController::class, 'applications'])->name('control-panel.web-hosting.applications.index');
Route::get('/applications/statistics', [DomainController::class, 'applicationStatistics'])->name('control-panel.web-hosting.applications.statistics');
Route::post('/applications', [DomainController::class, 'application'])->name('control-panel.web-hosting.applications.store');
Route::patch('/applications/{application}', [DomainController::class, 'updateApplication'])->name('control-panel.web-hosting.applications.update');
Route::delete('/applications/{application}', [DomainController::class, 'deleteApplication'])->name('control-panel.web-hosting.applications.delete');
Route::get('/applications/{application}/performance', [DomainController::class, 'applicationPerformance'])->name('control-panel.web-hosting.applications.performance');
Route::post('/applications/{application}/health-checks', [DomainController::class, 'applicationHealth'])->name('control-panel.web-hosting.applications.health');
Route::post('/applications/{application}/wordpress-update-checks', [DomainController::class, 'wordpressUpdate'])->name('control-panel.web-hosting.applications.wordpress-update-check');
Route::post('/domains/{domain}/hotlink-protection', [WebProtectionController::class, 'hotlink'])->name('control-panel.web-hosting.hotlink-protection.store');
Route::post('/domains/{domain}/directory-protections', [WebProtectionController::class, 'directory'])->name('control-panel.web-hosting.directory-protections.store');
Route::post('/directory-protections/{protection}/users', [WebProtectionController::class, 'directoryUser'])->name('control-panel.web-hosting.directory-protections.users.store');
Route::delete('/directory-protections/{protection}', [WebProtectionController::class, 'deleteDirectory'])->name('control-panel.web-hosting.directory-protections.delete');
Route::delete('/directory-protection-users/{user}', [WebProtectionController::class, 'deleteDirectoryUser'])->name('control-panel.web-hosting.directory-protection-users.delete');
Route::post('/domains/{domain}/custom-error-pages', [WebProtectionController::class, 'errorPage'])->name('control-panel.web-hosting.custom-error-pages.store');
Route::delete('/custom-error-pages/{page}', [WebProtectionController::class, 'deleteErrorPage'])->name('control-panel.web-hosting.custom-error-pages.delete');
Route::prefix('webhooks')->group(function (): void {
Route::post('github/{deployment}', [DomainController::class, 'githubWebhook'])->name('control-panel.web-hosting.webhooks.github');
Route::post('gitlab/{deployment}', [DomainController::class, 'gitlabWebhook'])->name('control-panel.web-hosting.webhooks.gitlab');
Route::post('generic/{deployment}', [DomainController::class, 'genericWebhook'])->name('control-panel.web-hosting.webhooks.generic');
```

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
