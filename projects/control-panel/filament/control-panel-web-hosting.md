# Control Panel: Control Panel Web Hosting Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-web-hosting). Observed identity: [`liberusoftware/module-control-panel-web-hosting-filament`](../../../modules/source/liberusoftware--module-control-panel-web-hosting-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-control-panel-control-panel-web-hosting-filament`  
**Matching domain module:** `control-panel-web-hosting`  
**Application:** Control Panel  
**Source feature:** [Control Panel Web Hosting](../features/control-panel-web-hosting.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `control-panel-web-hosting` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Domains:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Virtual hosts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **PHP/runtime versions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Web servers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **SSL:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Logs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Redirects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Applications:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-control-panel-control-panel-web-hosting-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `domains`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `virtual-hosts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `php-runtime-versions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `web-servers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ssl`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `logs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `redirects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `applications`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `control-panel-web-hosting` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-control-panel-laravel-filament`](https://github.com/liberusoftware/project-control-panel-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-control-panel-web-hosting-filament`](https://github.com/liberusoftware/module-control-panel-web-hosting-filament) (`liberusoftware/control-panel-web-hosting-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/control-panel-web-hosting.md) · [API plan](../api/control-panel-web-hosting.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Domains** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `domains`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Virtual hosts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `virtual hosts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **PHP/runtime versions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `php/runtime versions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Web servers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `web servers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **SSL** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ssl`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Logs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `logs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Redirects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `redirects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Applications** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `applications`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DomainResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-filament/src/Resources/DomainResource.php) · [CreateDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-filament/src/Resources/DomainResource/Pages/CreateDomain.php) · [EditDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-filament/src/Resources/DomainResource/Pages/EditDomain.php) · [ListDomains.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-filament/src/Resources/DomainResource/Pages/ListDomains.php) · [GitDeploymentResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-filament/src/Resources/GitDeploymentResource.php) · [CreateGitDeployment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-filament/src/Resources/GitDeploymentResource/Pages/CreateGitDeployment.php) · [EditGitDeployment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-filament/src/Resources/GitDeploymentResource/Pages/EditGitDeployment.php) · [ListGitDeployments.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-filament/src/Resources/GitDeploymentResource/Pages/ListGitDeployments.php) · [HostedApplicationResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-filament/src/Resources/HostedApplicationResource.php) · [CreateHostedApplication.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-filament/src/Resources/HostedApplicationResource/Pages/CreateHostedApplication.php) · [EditHostedApplication.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-filament/src/Resources/HostedApplicationResource/Pages/EditHostedApplication.php) · [ListHostedApplications.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-filament/src/Resources/HostedApplicationResource/Pages/ListHostedApplications.php) · [HostingLogResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-filament/src/Resources/HostingLogResource.php) · [CreateHostingLog.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-filament/src/Resources/HostingLogResource/Pages/CreateHostingLog.php).

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
<!-- layer-implementation-plan:end -->
