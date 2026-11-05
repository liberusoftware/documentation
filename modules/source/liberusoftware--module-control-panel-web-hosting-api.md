# liberusoftware/module-control-panel-web-hosting-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Authenticated API adapter for Control Panel Web Hosting.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-web-hosting-api](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-api/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-control-panel-laravel-filament, `control-panel-web-hosting-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-web-hosting-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-web-hosting-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\WebHostingApi\\WebHostingApiServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-api/composer.json) · [module.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-api/module.json).

**Declared capabilities:** control-panel.web-hosting.api

**Declared features:** Domains, Virtual hosts, Runtime versions, Web servers, SSL certificates, Logs, Redirects, MIME types, Applications, Git deployments, Hotlink protection, Directory protection, Custom error pages, Cron jobs and execution history, Subdomains

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/module-control-panel-web-hosting` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\WebHostingApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-control-panel-web-hosting": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/DomainController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-api/src/Http/Controllers/DomainController.php) | `public function index(Request $request, ListDomains $list): JsonResponse`<br>`public function usage(Request $request, ListResourceUsage $list): JsonResponse`<br>`public function recordUsage(Request $request, Domain $domain, RecordResourceUsage $record): JsonResponse`<br>`public function domainUsage(Request $request, Domain $domain, ListResourceUsage $list): JsonResponse`<br>`public function subdomains(Request $request, Domain $domain): JsonResponse`<br>`public function createSubdomain(Request $request, Domain $domain, CreateSubdomain $create): JsonResponse`<br>`public function updateSubdomain(Request $request, string $subdomain, UpdateSubdomain $update): JsonResponse`<br>`public function deleteSubdomain(Request $request, string $subdomain, DeleteSubdomain $delete): JsonResponse`<br>`public function cronJobs(Request $request, Domain $domain): JsonResponse`<br>`public function createCronJob(Request $request, Domain $domain, CreateCronJob $create): JsonResponse`<br>`public function updateCronJob(Request $request, string $job, UpdateCronJob $update): JsonResponse`<br>`public function deleteCronJob(Request $request, string $job, DeleteCronJob $delete): JsonResponse`<br>`public function cronExecutions(Request $request, string $job): JsonResponse`<br>`public function recordCronExecution(Request $request, string $job, RecordCronExecution $record): JsonResponse`<br>`public function store(Request $request, CreateDomain $create): JsonResponse`<br>`public function update(Request $request, Domain $domain, UpdateDomain $update): JsonResponse`<br>`public function activate(Request $request, Domain $domain, ActivateDomain $activate): JsonResponse`<br>`public function suspend(Request $request, Domain $domain, SuspendDomain $suspend): JsonResponse`<br>`public function archive(Request $request, Domain $domain, ArchiveDomain $archive): JsonResponse`<br>`public function virtualHost(Request $request, Domain $domain, CreateVirtualHost $create): JsonResponse`<br>`public function updateVirtualHost(Request $request, string $id, UpdateVirtualHost $update): JsonResponse`<br>`public function deleteVirtualHost(Request $request, string $id, DeleteVirtualHost $delete): JsonResponse`<br>`public function redirect(Request $request, Domain $domain, CreateRedirect $create): JsonResponse`<br>`public function updateRedirect(Request $request, string $id, UpdateRedirect $update): JsonResponse`<br>`public function deleteRedirect(Request $request, string $id, DeleteRedirect $delete): JsonResponse`<br>`public function mimeType(Request $request, Domain $domain, CreateMimeType $create): JsonResponse`<br>`public function certificate(Request $request, Domain $domain, RequestCertificate $requestCertificate): JsonResponse`<br>`public function resourceRecord(Request $request, RegisterHostingResource $register): JsonResponse`<br>`public function resources(Request $request, string $kind): JsonResponse`<br>`public function applications(Request $request): JsonResponse`<br>`public function applicationStatistics(Request $request, ApplicationStatistics $statistics): JsonResponse`<br>`public function application(Request $request, RegisterHostingResource $register): JsonResponse`<br>`public function updateApplication(Request $request, string $id, UpdateHostedApplication $update): JsonResponse`<br>`public function deleteApplication(Request $request, string $id, DeleteHostedApplication $delete): JsonResponse`<br>`public function applicationPerformance(Request $request, HostedApplication $application): JsonResponse`<br>`public function applicationHealth(Request $request, HostedApplication $application, CheckApplicationHealth $check): JsonResponse`<br>`public function wordpressUpdate(Request $request, HostedApplication $application, CheckWordPressUpdates $check): JsonResponse`<br>`public function deployments(Request $request, ListGitDeployments $list): JsonResponse`<br>`public function deployment(Request $request, Domain $domain, RegisterGitDeployment $register): JsonResponse`<br>`public function deploy(Request $request, string $deployment, RequestGitDeployment $requestDeployment): JsonResponse`<br>`public function githubWebhook(Request $request, string $deployment, RequestGitDeployment $requestDeployment): JsonResponse`<br>`public function gitlabWebhook(Request $request, string $deployment, RequestGitDeployment $requestDeployment): JsonResponse`<br>`public function genericWebhook(Request $request, string $deployment, RequestGitDeployment $requestDeployment): JsonResponse`<br>`public function phpConfiguration(Request $request, Domain $domain, SavePhpConfiguration $save): JsonResponse` |
| [src/Http/Controllers/WebProtectionController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-api/src/Http/Controllers/WebProtectionController.php) | `public function hotlink(Request $request, string $domain, ConfigureHotlinkProtection $configure): JsonResponse`<br>`public function directory(Request $request, string $domain, CreateDirectoryProtection $create): JsonResponse`<br>`public function deleteDirectory(Request $request, string $protection, DeleteDirectoryProtection $delete): JsonResponse`<br>`public function directoryUser(Request $request, string $protection, AddDirectoryProtectionUser $add): JsonResponse`<br>`public function deleteDirectoryUser(Request $request, string $user, RemoveDirectoryProtectionUser $remove): JsonResponse`<br>`public function errorPage(Request $request, string $domain, SaveCustomErrorPage $save): JsonResponse`<br>`public function deleteErrorPage(Request $request, string $page, DeleteCustomErrorPage $delete): JsonResponse` |

Other non-legacy PHP sources: [src/WebHostingApiServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-api/src/WebHostingApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/control-panel-web-hosting.yaml](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-api/openapi/v1/control-panel-web-hosting.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-web-hosting-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
