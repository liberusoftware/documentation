# Control Panel: Control Panel Web Hosting Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-web-hosting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-control-panel-control-panel-web-hosting-nuxt`
**Matching domain module:** `control-panel-web-hosting`
**Application:** Control Panel
**Source feature:** [Control Panel Web Hosting](../features/control-panel-web-hosting.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/control-panel-web-hosting.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `control-panel-web-hosting` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Domains:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Virtual hosts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **PHP/runtime versions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Web servers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **SSL:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Logs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Redirects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Applications:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-control-panel-control-panel-web-hosting-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `domains`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `virtual-hosts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `php-runtime-versions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `web-servers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ssl`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `logs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `redirects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `applications`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `control-panel-web-hosting` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-control-panel-nuxt-vue`](https://github.com/liberusoftware/project-control-panel-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/control-panel-web-hosting.md)) |
| Capability Nuxt module skeleton | [`module-control-panel-web-hosting-nuxt`](https://github.com/liberusoftware/module-control-panel-web-hosting-nuxt) (`@liberusoftware/module-control-panel-web-hosting-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Domains** | Expose composable and Vue 3 component for `domains` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-web-hosting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Virtual hosts** | Expose composable and Vue 3 component for `virtual hosts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-web-hosting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **PHP/runtime versions** | Expose composable and Vue 3 component for `php/runtime versions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-web-hosting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Web servers** | Expose composable and Vue 3 component for `web servers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-web-hosting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **SSL** | Expose composable and Vue 3 component for `ssl` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-web-hosting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Logs** | Expose composable and Vue 3 component for `logs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-web-hosting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Redirects** | Expose composable and Vue 3 component for `redirects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-web-hosting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Applications** | Expose composable and Vue 3 component for `applications` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-web-hosting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |

### Observed domain and transport source evidence

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

| Observed API controller | Handler signatures |
| --- | --- |
| [DomainController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-api/src/Http/Controllers/DomainController.php) | `public function index(Request $request, ListDomains $list): JsonResponse`<br>`public function usage(Request $request, ListResourceUsage $list): JsonResponse`<br>`public function recordUsage(Request $request, Domain $domain, RecordResourceUsage $record): JsonResponse`<br>`public function domainUsage(Request $request, Domain $domain, ListResourceUsage $list): JsonResponse`<br>`public function subdomains(Request $request, Domain $domain): JsonResponse`<br>`public function createSubdomain(Request $request, Domain $domain, CreateSubdomain $create): JsonResponse`<br>`public function updateSubdomain(Request $request, string $subdomain, UpdateSubdomain $update): JsonResponse`<br>`public function deleteSubdomain(Request $request, string $subdomain, DeleteSubdomain $delete): JsonResponse`<br>`public function cronJobs(Request $request, Domain $domain): JsonResponse`<br>`public function createCronJob(Request $request, Domain $domain, CreateCronJob $create): JsonResponse`<br>`public function updateCronJob(Request $request, string $job, UpdateCronJob $update): JsonResponse`<br>`public function deleteCronJob(Request $request, string $job, DeleteCronJob $delete): JsonResponse`<br>`public function cronExecutions(Request $request, string $job): JsonResponse`<br>`public function recordCronExecution(Request $request, string $job, RecordCronExecution $record): JsonResponse`<br>`public function store(Request $request, CreateDomain $create): JsonResponse`<br>`public function update(Request $request, Domain $domain, UpdateDomain $update): JsonResponse`<br>`public function activate(Request $request, Domain $domain, ActivateDomain $activate): JsonResponse`<br>`public function suspend(Request $request, Domain $domain, SuspendDomain $suspend): JsonResponse`<br>`public function archive(Request $request, Domain $domain, ArchiveDomain $archive): JsonResponse`<br>`public function virtualHost(Request $request, Domain $domain, CreateVirtualHost $create): JsonResponse`<br>`public function updateVirtualHost(Request $request, string $id, UpdateVirtualHost $update): JsonResponse`<br>`public function deleteVirtualHost(Request $request, string $id, DeleteVirtualHost $delete): JsonResponse`<br>`public function redirect(Request $request, Domain $domain, CreateRedirect $create): JsonResponse`<br>`public function updateRedirect(Request $request, string $id, UpdateRedirect $update): JsonResponse`<br>`public function deleteRedirect(Request $request, string $id, DeleteRedirect $delete): JsonResponse`<br>`public function mimeType(Request $request, Domain $domain, CreateMimeType $create): JsonResponse`<br>`public function certificate(Request $request, Domain $domain, RequestCertificate $requestCertificate): JsonResponse`<br>`public function resourceRecord(Request $request, RegisterHostingResource $register): JsonResponse`<br>`public function resources(Request $request, string $kind): JsonResponse`<br>`public function applications(Request $request): JsonResponse`<br>`public function applicationStatistics(Request $request, ApplicationStatistics $statistics): JsonResponse`<br>`public function application(Request $request, RegisterHostingResource $register): JsonResponse`<br>`public function updateApplication(Request $request, string $id, UpdateHostedApplication $update): JsonResponse`<br>`public function deleteApplication(Request $request, string $id, DeleteHostedApplication $delete): JsonResponse`<br>`public function applicationPerformance(Request $request, HostedApplication $application): JsonResponse`<br>`public function applicationHealth(Request $request, HostedApplication $application, CheckApplicationHealth $check): JsonResponse`<br>`public function wordpressUpdate(Request $request, HostedApplication $application, CheckWordPressUpdates $check): JsonResponse`<br>`public function deployments(Request $request, ListGitDeployments $list): JsonResponse`<br>`public function deployment(Request $request, Domain $domain, RegisterGitDeployment $register): JsonResponse`<br>`public function deploy(Request $request, string $deployment, RequestGitDeployment $requestDeployment): JsonResponse`<br>`public function githubWebhook(Request $request, string $deployment, RequestGitDeployment $requestDeployment): JsonResponse`<br>`public function gitlabWebhook(Request $request, string $deployment, RequestGitDeployment $requestDeployment): JsonResponse`<br>`public function genericWebhook(Request $request, string $deployment, RequestGitDeployment $requestDeployment): JsonResponse`<br>`public function phpConfiguration(Request $request, Domain $domain, SavePhpConfiguration $save): JsonResponse` |
| [WebProtectionController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-api/src/Http/Controllers/WebProtectionController.php) | `public function hotlink(Request $request, string $domain, ConfigureHotlinkProtection $configure): JsonResponse`<br>`public function directory(Request $request, string $domain, CreateDirectoryProtection $create): JsonResponse`<br>`public function deleteDirectory(Request $request, string $protection, DeleteDirectoryProtection $delete): JsonResponse`<br>`public function directoryUser(Request $request, string $protection, AddDirectoryProtectionUser $add): JsonResponse`<br>`public function deleteDirectoryUser(Request $request, string $user, RemoveDirectoryProtectionUser $remove): JsonResponse`<br>`public function errorPage(Request $request, string $domain, SaveCustomErrorPage $save): JsonResponse`<br>`public function deleteErrorPage(Request $request, string $page, DeleteCustomErrorPage $delete): JsonResponse` |

**Observed route declarations:**

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
<!-- layer-implementation-plan:end -->
