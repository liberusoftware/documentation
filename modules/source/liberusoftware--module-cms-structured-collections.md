# liberusoftware/module-cms-structured-collections: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Canonical compatibility package for CMS structured collections.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [cms](../../projects/cms/SOURCE-MODULES.md) | [cms-structured-collections](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-structured-collections/composer.json) | `5d91aa9c0a3d` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-cms-laravel-filament, `cms-structured-collections`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-cms-structured-collections` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-cms-structured-collections` |
| Module version field | `0.1.0` |
| Category / layers | `"not declared"` |
| Manifest provider(s) | `"not declared"` |
| Composer Laravel provider registration | `["Liberu\\Cms\\StructuredCollections\\StructuredCollectionsServiceProvider"]` |
| default_enabled field | `"not declared"` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-structured-collections/composer.json) · [module.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-structured-collections/module.json).

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `liberusoftware/module-cms-collections` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Cms\\StructuredCollections\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/StructuredCollectionMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-structured-collections/src/Actions/StructuredCollectionMutationService.php) | `public function __construct(private CollectionMutationService $legacy)`<br>`public function create(array $attributes): Collection`<br>`public function update(Collection $collection, array $attributes): Collection`<br>`public function delete(Collection $collection): void`<br>`public function createRecord(Collection $collection, array $attributes): CollectionItem`<br>`public function updateRecord(CollectionItem $record, array $attributes): CollectionItem`<br>`public function deleteRecord(CollectionItem $record): void` |
| [src/Queries/StructuredCollectionQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-structured-collections/src/Queries/StructuredCollectionQuery.php) | `public function __construct(private CollectionQuery $legacy)`<br>`public function paginate(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function collection(string $slug): ?Collection`<br>`public function records(string $slug, int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function record(string $collection, string $slug): ?CollectionItem`<br>`public function recordForMutation(string $collection, string $slug): ?CollectionItem` |

Other non-legacy PHP sources: [src/StructuredCollectionsServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-structured-collections/src/StructuredCollectionsServiceProvider.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
