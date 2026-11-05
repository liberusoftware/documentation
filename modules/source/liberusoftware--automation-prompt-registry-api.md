# liberusoftware/automation-prompt-registry-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

HTTP API adapter for module-automation-prompt-registry.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [module-automation-prompt-registry-api](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-prompt-registry-api/composer.json) | `68e5f07a6704` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-automation-laravel-filament, `module-automation-prompt-registry-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/automation-prompt-registry-api` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `module-automation-prompt-registry-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Modules\\Automation\\PromptRegistry\\Api\\PromptRegistryApiServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-prompt-registry-api/composer.json) · [module.json](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-prompt-registry-api/module.json).

**Declared capabilities:** automation.prompt-registry.api

**Declared features:** Versioned JSON API, Team-scoped resources, Idempotent writes

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/support` | `^13.0` |
| `laravel/framework` | `^13.0` |
| `liberusoftware/automation-prompt-registry` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Modules\\Automation\\PromptRegistry\\Api\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/automation-prompt-registry": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/PromptRegistryResourceController.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-prompt-registry-api/src/Http/Controllers/PromptRegistryResourceController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreatePromptRegistryResource $create): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function update(Request $request, string $id): JsonResponse`<br>`public function destroy(Request $request, string $id): JsonResponse`<br>`public function transition(Request $request, string $id, TransitionPromptRegistryResource $transition): JsonResponse` |
| [src/Support/ResourcePayload.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-prompt-registry-api/src/Support/ResourcePayload.php) | `public static function one(Model $resource): array`<br>`public static function collection(LengthAwarePaginator $resources): array` |

Other non-legacy PHP sources: [src/PromptRegistryApiServiceProvider.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-prompt-registry-api/src/PromptRegistryApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/prompt-registry.yaml](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-prompt-registry-api/openapi/v1/prompt-registry.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-prompt-registry-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
