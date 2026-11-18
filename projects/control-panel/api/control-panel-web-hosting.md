# Control Panel: Control Panel Web Hosting API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-web-hosting). Observed identity: [`liberusoftware/module-control-panel-web-hosting-api`](../../../modules/source/liberusoftware--module-control-panel-web-hosting-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-control-panel-control-panel-web-hosting-api`<br>
**Matching domain module:** `control-panel-web-hosting`  
**Application:** Control Panel  
**Source feature:** [Control Panel Web Hosting](../features/control-panel-web-hosting.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Control Panel Web Hosting domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Domains
- Virtual hosts
- PHP/runtime versions
- Web servers
- SSL
- Logs
- Redirects
- Applications

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Choose the route namespace through the host's reviewed API contract; observed source prefixes below take precedence over repository/design-name guesses.
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

## 3. Endpoint examples

**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.

### Product API backend and client integration

This module API adapter is composed into [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).

| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |
| --- | --- | --- | --- |
| Next.js React | [`project-control-panel-next-react`](https://github.com/liberusoftware/project-control-panel-next-react) | [Next.js plan](../nextjs/control-panel-web-hosting.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-control-panel-nuxt-vue`](https://github.com/liberusoftware/project-control-panel-nuxt-vue) | [Nuxt plan](../nuxt/control-panel-web-hosting.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-control-panel-mobile-react`](https://github.com/liberusoftware/project-control-panel-mobile-react) | [React Native plan](../react-native/control-panel-web-hosting.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-control-panel-mobile-flutter`](https://github.com/liberusoftware/project-control-panel-mobile-flutter) | [Flutter plan](../flutter/control-panel-web-hosting.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-control-panel-dart-mobile`](https://github.com/liberusoftware/project-control-panel-dart-mobile) · [`project-control-panel-dart-desktop`](https://github.com/liberusoftware/project-control-panel-dart-desktop) | [Flutter & Dart plan](../flutter/control-panel-web-hosting.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Domains** | Expose authorized query/read projection and explicit domain transition command for `domains` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Virtual hosts** | Expose authorized query/read projection and explicit domain transition command for `virtual hosts` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **PHP/runtime versions** | Expose authorized query/read projection and explicit domain transition command for `php/runtime versions` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Web servers** | Expose authorized query/read projection and explicit domain transition command for `web servers` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **SSL** | Expose authorized query/read projection and explicit domain transition command for `ssl` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Logs** | Expose authorized query/read projection and explicit domain transition command for `logs` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Redirects** | Expose authorized query/read projection and explicit domain transition command for `redirects` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Applications** | Expose authorized query/read projection and explicit domain transition command for `applications` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-control-panel-web-hosting-api](../../../modules/source/liberusoftware--module-control-panel-web-hosting-api.md) |
| Source package | [liberusoftware/module-control-panel-web-hosting](../../../modules/source/liberusoftware--module-control-panel-web-hosting.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

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

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [DomainController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-api/src/Http/Controllers/DomainController.php) | `public function index(Request $request, ListDomains $list): JsonResponse`<br>`public function usage(Request $request, ListResourceUsage $list): JsonResponse`<br>`public function recordUsage(Request $request, Domain $domain, RecordResourceUsage $record): JsonResponse`<br>`public function domainUsage(Request $request, Domain $domain, ListResourceUsage $list): JsonResponse`<br>`public function subdomains(Request $request, Domain $domain): JsonResponse`<br>`public function createSubdomain(Request $request, Domain $domain, CreateSubdomain $create): JsonResponse`<br>`public function updateSubdomain(Request $request, string $subdomain, UpdateSubdomain $update): JsonResponse`<br>`public function deleteSubdomain(Request $request, string $subdomain, DeleteSubdomain $delete): JsonResponse`<br>`public function cronJobs(Request $request, Domain $domain): JsonResponse`<br>`public function createCronJob(Request $request, Domain $domain, CreateCronJob $create): JsonResponse`<br>`public function updateCronJob(Request $request, string $job, UpdateCronJob $update): JsonResponse`<br>`public function deleteCronJob(Request $request, string $job, DeleteCronJob $delete): JsonResponse`<br>`public function cronExecutions(Request $request, string $job): JsonResponse`<br>`public function recordCronExecution(Request $request, string $job, RecordCronExecution $record): JsonResponse`<br>`public function store(Request $request, CreateDomain $create): JsonResponse`<br>`public function update(Request $request, Domain $domain, UpdateDomain $update): JsonResponse`<br>`public function activate(Request $request, Domain $domain, ActivateDomain $activate): JsonResponse`<br>`public function suspend(Request $request, Domain $domain, SuspendDomain $suspend): JsonResponse`<br>`public function archive(Request $request, Domain $domain, ArchiveDomain $archive): JsonResponse`<br>`public function virtualHost(Request $request, Domain $domain, CreateVirtualHost $create): JsonResponse`<br>`public function updateVirtualHost(Request $request, string $id, UpdateVirtualHost $update): JsonResponse`<br>`public function deleteVirtualHost(Request $request, string $id, DeleteVirtualHost $delete): JsonResponse`<br>`public function redirect(Request $request, Domain $domain, CreateRedirect $create): JsonResponse`<br>`public function updateRedirect(Request $request, string $id, UpdateRedirect $update): JsonResponse`<br>`public function deleteRedirect(Request $request, string $id, DeleteRedirect $delete): JsonResponse`<br>`public function mimeType(Request $request, Domain $domain, CreateMimeType $create): JsonResponse`<br>`public function certificate(Request $request, Domain $domain, RequestCertificate $requestCertificate): JsonResponse`<br>`public function resourceRecord(Request $request, RegisterHostingResource $register): JsonResponse`<br>`public function resources(Request $request, string $kind): JsonResponse`<br>`public function applications(Request $request): JsonResponse`<br>`public function applicationStatistics(Request $request, ApplicationStatistics $statistics): JsonResponse`<br>`public function application(Request $request, RegisterHostingResource $register): JsonResponse`<br>`public function updateApplication(Request $request, string $id, UpdateHostedApplication $update): JsonResponse`<br>`public function deleteApplication(Request $request, string $id, DeleteHostedApplication $delete): JsonResponse`<br>`public function applicationPerformance(Request $request, HostedApplication $application): JsonResponse`<br>`public function applicationHealth(Request $request, HostedApplication $application, CheckApplicationHealth $check): JsonResponse`<br>`public function wordpressUpdate(Request $request, HostedApplication $application, CheckWordPressUpdates $check): JsonResponse`<br>`public function deployments(Request $request, ListGitDeployments $list): JsonResponse`<br>`public function deployment(Request $request, Domain $domain, RegisterGitDeployment $register): JsonResponse`<br>`public function deploy(Request $request, string $deployment, RequestGitDeployment $requestDeployment): JsonResponse`<br>`public function githubWebhook(Request $request, string $deployment, RequestGitDeployment $requestDeployment): JsonResponse`<br>`public function gitlabWebhook(Request $request, string $deployment, RequestGitDeployment $requestDeployment): JsonResponse`<br>`public function genericWebhook(Request $request, string $deployment, RequestGitDeployment $requestDeployment): JsonResponse`<br>`public function phpConfiguration(Request $request, Domain $domain, SavePhpConfiguration $save): JsonResponse` |
| [WebProtectionController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-api/src/Http/Controllers/WebProtectionController.php) | `public function hotlink(Request $request, string $domain, ConfigureHotlinkProtection $configure): JsonResponse`<br>`public function directory(Request $request, string $domain, CreateDirectoryProtection $create): JsonResponse`<br>`public function deleteDirectory(Request $request, string $protection, DeleteDirectoryProtection $delete): JsonResponse`<br>`public function directoryUser(Request $request, string $protection, AddDirectoryProtectionUser $add): JsonResponse`<br>`public function deleteDirectoryUser(Request $request, string $user, RemoveDirectoryProtectionUser $remove): JsonResponse`<br>`public function errorPage(Request $request, string $domain, SaveCustomErrorPage $save): JsonResponse`<br>`public function deleteErrorPage(Request $request, string $page, DeleteCustomErrorPage $delete): JsonResponse` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core query source | Observed signatures |
| --- | --- |
| [ApplicationStatistics.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Queries/ApplicationStatistics.php) | `public function execute(string\|int $teamId, int $days = 30): array` |
| [ListDomains.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Queries/ListDomains.php) | `public function execute(?string $teamId = null, int $perPage = 25): LengthAwarePaginator` |
| [ListGitDeployments.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Queries/ListGitDeployments.php) | `public function execute(string\|int $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |
| [ListResourceUsage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting/src/Queries/ListResourceUsage.php) | `public function execute(string\|int $teamId, ?string $domainId = null, int $months = 12): Collection` |

| Core action / service source | Observed signatures |
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

| Core storage model | Observed fillable fields (review for DTO allowlist) |
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

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [openapi/v1/control-panel-web-hosting.yaml](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-api/openapi/v1/control-panel-web-hosting.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#control-panel-web-hosting), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

## 5. Audience and operation matrix

| Audience                       | Default exposure                    | Required controls                                                                      |
| ------------------------------ | ----------------------------------- | -------------------------------------------------------------------------------------- |
| Public/anonymous               | Disabled unless explicitly required | Enumeration resistance, strict rate limits, field minimization, abuse controls         |
| Authenticated customer/partner | Explicit allowlist                  | Tenant/resource ownership, purpose-specific scopes, field policy                       |
| Staff/administrator            | Explicit allowlist                  | Role/permission policy, tenant context, recent authentication for risky actions, audit |
| Service/integration client     | Explicit allowlist                  | Service identity, least-privilege scopes, expiry/rotation, idempotency, quotas         |

Every exposed operation must map to one audience, domain query/action, permission/scope, request/response schema, rate limit, idempotency/concurrency policy, audit event, and test set. Unmapped operations fail CI.

## 6. Implementation strategy

- Keep routes, controllers/handlers, requests, API resources, OpenAPI fragments, and transport tests in this API package.
- Validate shape at the request boundary and enforce authoritative invariants again in the domain action.
- Resolve tenant and actor context from trusted authentication/application routing; never grant context from a caller-supplied tenant identifier alone.
- Authorize field visibility as well as record/action access, and return concealment-safe errors where enumeration is a risk.
- Use idempotency keys for retryable writes, ETags/`If-Match` for relevant concurrent updates, and asynchronous operation resources for slow/bulk/provider-dependent work.
- Compose cross-module workflows in the application layer; do not query or mutate another module's private storage from this API package.

## 7. Security, resilience, and observability

- Threat-model authentication, authorization, tenant isolation, mass assignment, object references, abusive queries, uploads/downloads, webhooks, and sensitive data.
- Bound pagination, filters, includes, payloads, batch sizes, timeouts, and retry budgets.
- Redact credentials and protected data from logs and errors while recording request, correlation, API/module/version, tenant, principal, operation, status, latency, rate-limit, and idempotency outcomes.
- Define availability, latency, error-rate and queued-operation objectives plus alerts and recovery/reconciliation runbooks.

## 8. Verification strategy

- Lint OpenAPI, validate examples, detect implementation drift and breaking changes, and reject path/schema/operation-ID collisions during application aggregation.
- Test every operation for allowed, unauthenticated, wrong-tenant, insufficient-scope, insufficient-permission, hidden-field, invalid, missing, duplicate, stale, concurrent, throttled, and failure/recovery paths as applicable.
- Test pagination, filtering, sorting, includes, dates, money, identifiers, enums, idempotency, ETags, async operations, bulk partial failure, and stable Problem Details.
- Add one-to-one architecture tests proving this package depends on and presents only `control-panel-web-hosting`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `control-panel-web-hosting`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
