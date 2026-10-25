# liberusoftware/module-cms-experimentation: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Tenant-aware A/B and multivariate content experimentation with allocation and promotion history.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [cms](../../projects/cms/SOURCE-MODULES.md) | [cms-experimentation](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/composer.json) | `5d91aa9c0a3d` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: cms-laravel, `cms-experimentation`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-cms-experimentation` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-cms-experimentation` |
| Module version field | `0.1.0` |
| Category / layers | `"not declared"` |
| Manifest provider(s) | `"not declared"` |
| Composer Laravel provider registration | `["Liberu\\Cms\\Experimentation\\ExperimentationServiceProvider"]` |
| default_enabled field | `"not declared"` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/composer.json) · [module.json](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/module.json).

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `laravel/framework` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Cms\\Experimentation\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Queries/ExperimentationQuery.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Queries/ExperimentationQuery.php) | `public function list(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function find(string $key): ?Experiment`<br>`public function active(string $key): ?Experiment` |
| [src/Services/ExperimentationService.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Services/ExperimentationService.php) | `public function create(array $attributes, ?int $teamId = null): Experiment`<br>`public function start(Experiment $experiment): Experiment`<br>`public function stop(Experiment $experiment): Experiment`<br>`public function allocate(Experiment $experiment, string $subjectKey): ?ExperimentVariant`<br>`public function observe(Experiment $experiment, ExperimentVariant $variant, string $subjectKey, ?string $goalKey, float $value = 1): ExperimentObservation`<br>`public function promote(Experiment $experiment, ExperimentVariant $variant, ?string $reason = null, ?string $actorType = null, int\|string\|null $actorId = null): Experiment` |

Other non-legacy PHP sources: [src/ExperimentationModule.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/ExperimentationModule.php) · [src/ExperimentationServiceProvider.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/ExperimentationServiceProvider.php) · [src/Models/Experiment.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Models/Experiment.php) · [src/Models/ExperimentObservation.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Models/ExperimentObservation.php) · [src/Models/ExperimentPromotion.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Models/ExperimentPromotion.php) · [src/Models/ExperimentVariant.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Models/ExperimentVariant.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_29_010000_create_cms_experimentation_tables.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/database/migrations/2026_08_29_010000_create_cms_experimentation_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
