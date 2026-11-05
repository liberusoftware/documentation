# liberusoftware/module-control-panel-security-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

API adapter for Control Panel Security.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-security-api](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-control-panel-laravel-filament, `control-panel-security-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-security-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-security-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\SecurityApi\\SecurityApiServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/composer.json) · [module.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/module.json).

**Declared capabilities:** control-panel.security.api

**Declared features:** Hardening, Patching, MFA and RBAC, Secrets, Malware, Intrusion controls, Fail2ban jail and ban management, Vulnerability and compliance status

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/module-control-panel-security` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\SecurityApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-control-panel-security": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/SecurityFindingController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/src/Http/Controllers/SecurityFindingController.php) | `public function index(Request $request, ListFindings $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, RecordFinding $record): JsonResponse`<br>`public function resolve(Request $request, string $id, ResolveSecurityFinding $resolve): JsonResponse`<br>`public function update(Request $request, string $id, UpdateSecurityFinding $update): JsonResponse`<br>`public function hardening(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function patch(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function patches(Request $request): JsonResponse`<br>`public function policy(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function policies(Request $request): JsonResponse`<br>`public function secret(Request $request, StoreSecret $store): JsonResponse`<br>`public function secrets(Request $request): JsonResponse`<br>`public function malware(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function malwareScans(Request $request): JsonResponse`<br>`public function intrusion(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function intrusionControls(Request $request): JsonResponse`<br>`public function fail2ban(Request $request, ConfigureFail2ban $configure): JsonResponse`<br>`public function fail2banBans(Request $request, string $jail, RecordFail2banBan $record): JsonResponse`<br>`public function listFail2banBans(Request $request, string $jail): JsonResponse`<br>`public function unbanFail2ban(Request $request, string $ban, UnbanFail2banBan $unban): JsonResponse`<br>`public function compliance(Request $request, RecordSecurityResource $record): JsonResponse` |

Other non-legacy PHP sources: [src/SecurityApiServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/src/SecurityApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/control-panel-security.yaml](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/openapi/v1/control-panel-security.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
