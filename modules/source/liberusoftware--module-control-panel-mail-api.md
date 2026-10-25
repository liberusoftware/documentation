# liberusoftware/module-control-panel-mail-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

API adapter for Control Panel Mail.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-mail-api](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-api/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: control-panel-laravel, `control-panel-mail-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-mail-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-mail-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\MailApi\\MailApiServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-api/composer.json) · [module.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-api/module.json).

**Declared capabilities:** control-panel.mail.api

**Declared features:** Mail domains, Mailboxes, Aliases, Routing, Quotas, Spam and virus controls, DKIM/SPF/DMARC authentication configuration, Delivery diagnostics

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/module-control-panel-mail` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\MailApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-control-panel-mail": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/MailAccountController.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-api/src/Http/Controllers/MailAccountController.php) | `public function index(Request $request, ListMailAccounts $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, CreateMailAccount $create): JsonResponse`<br>`public function update(Request $request, string $id, UpdateMailAccount $update): JsonResponse`<br>`public function delete(Request $request, string $id, DeleteMailAccount $delete): JsonResponse`<br>`public function operation(Request $request, RecordMailOperation $record): JsonResponse`<br>`public function alias(Request $request, CreateMailAlias $create): JsonResponse`<br>`public function updateAlias(Request $request, string $id, UpdateMailAlias $update): JsonResponse`<br>`public function deleteAlias(Request $request, string $id, DeleteMailAlias $delete): JsonResponse`<br>`public function updateRoute(Request $request, string $id, UpdateMailRoute $update): JsonResponse`<br>`public function deleteRoute(Request $request, string $id, DeleteMailRoute $delete): JsonResponse`<br>`public function route(Request $request, CreateMailRoute $create): JsonResponse`<br>`public function controls(Request $request, ConfigureMailControls $configure): JsonResponse`<br>`public function diagnostic(Request $request, RecordDeliveryDiagnostic $record): JsonResponse`<br>`public function rotateDkim(Request $request, RotateDkimKey $rotate): JsonResponse`<br>`public function authentication(Request $request, ConfigureMailAuthentication $configure): JsonResponse`<br>`public function domain(Request $request, RegisterMailDomain $register): JsonResponse` |

Other non-legacy PHP sources: [src/MailApiServiceProvider.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-api/src/MailApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/control-panel-mail.yaml](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-api/openapi/v1/control-panel-mail.yaml)
- [routes/api.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
