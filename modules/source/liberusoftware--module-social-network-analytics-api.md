# liberusoftware/module-social-network-analytics-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

API adapter for social network analytics.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [social-network-analytics-api](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics-api/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-social-network-laravel-filament, `social-network-analytics-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-social-network-analytics-api` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `social-network-analytics-api` |
| Module version field | `0.1.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\SocialNetwork\\Analytics\\Api\\AnalyticsApiServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics-api/composer.json) · [module.json](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics-api/module.json).

**Declared capabilities:** social-network.analytics.api

**Declared features:** authenticated metric reads, bounded queries, explicit resource serialization, OpenAPI contract

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `laravel/framework` | `^13.0` |
| `liberusoftware/module-social-network-analytics` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\SocialNetwork\\Analytics\\Api\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-social-network-analytics": "^0.1"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/AnalyticsController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics-api/src/Http/Controllers/AnalyticsController.php) | `public function show(Request $request, string $metric, GetMetrics $metrics): JsonResponse` |

Other non-legacy PHP sources: [src/AnalyticsApiServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics-api/src/AnalyticsApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/social-network-analytics.yaml](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics-api/openapi/v1/social-network-analytics.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
