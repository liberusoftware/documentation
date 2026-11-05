# liberusoftware/module-cms-taxonomy: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

CMS vocabularies, hierarchical terms, synonyms, localization, and assignments.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [cms](../../projects/cms/SOURCE-MODULES.md) | [cms-taxonomy](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/composer.json) | `5d91aa9c0a3d` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-cms-laravel-filament, `cms-taxonomy`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-cms-taxonomy` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-cms-taxonomy` |
| Module version field | `0.1.0` |
| Category / layers | `"not declared"` |
| Manifest provider(s) | `"not declared"` |
| Composer Laravel provider registration | `["Liberu\\Cms\\Taxonomy\\TaxonomyServiceProvider"]` |
| default_enabled field | `"not declared"` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/composer.json) · [module.json](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/module.json).

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `laravel/framework` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Cms\\Taxonomy\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Queries/TaxonomyQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/src/Queries/TaxonomyQuery.php) | `public function taxonomies(?string $key = null, ?string $search = null, int $perPage = 15): LengthAwarePaginator`<br>`public function taxonomy(int $id): ?Taxonomy`<br>`public function term(int $id): ?Term`<br>`public function terms(int $taxonomyId, ?string $search = null): array` |
| [src/Services/TaxonomyService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/src/Services/TaxonomyService.php) | `public function create(string $key, string $name, bool $hierarchical = true, bool $exclusive = false, ?int $teamId = null, ?string $description = null): Taxonomy`<br>`public function update(Taxonomy $taxonomy, array $attributes): Taxonomy`<br>`public function delete(Taxonomy $taxonomy): void`<br>`public function addTerm(Taxonomy $taxonomy, string $name, ?string $slug = null, ?int $parentId = null, array $synonyms = [], array $translations = [], ?int $position = null): Term`<br>`public function move(Term $term, ?int $parentId, ?int $position = null): Term`<br>`public function assign(Term $term, string $subjectType, int\|string $subjectId): TermAssignment`<br>`public function unassign(Term $term, string $subjectType, int\|string $subjectId): int`<br>`public function merge(Term $from, Term $into): Term`<br>`public function terms(Taxonomy $taxonomy, ?string $search = null): array` |

Other non-legacy PHP sources: [src/Models/Taxonomy.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/src/Models/Taxonomy.php) · [src/Models/Term.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/src/Models/Term.php) · [src/Models/TermAssignment.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/src/Models/TermAssignment.php) · [src/TaxonomyModule.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/src/TaxonomyModule.php) · [src/TaxonomyServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/src/TaxonomyServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_200000_create_cms_taxonomy_tables.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-taxonomy/database/migrations/2026_08_24_200000_create_cms_taxonomy_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
