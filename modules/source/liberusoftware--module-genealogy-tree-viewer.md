# liberusoftware/module-genealogy-tree-viewer: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Liberu genealogy-tree-viewer module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [genealogy-tree-viewer](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-genealogy-laravel-filament, `genealogy-tree-viewer`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-genealogy-tree-viewer` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `genealogy-tree-viewer` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Genealogy\\TreeViewer\\TreeViewerServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/composer.json) · [module.json](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/module.json).

**Declared capabilities:** genealogy.tree-viewer, genealogy.tree-viewer.pedigree, genealogy.tree-viewer.descendants, genealogy.tree-viewer.fan-chart, genealogy.tree-viewer.navigation, genealogy.tree-viewer.filters, genealogy.tree-viewer.large-tree-rendering, genealogy.tree-viewer.lifecycle

**Declared features:** genealogy tree viewer, genealogy tree viewer pedigree, genealogy tree viewer descendants, genealogy tree viewer fan-chart, genealogy tree viewer navigation, genealogy tree viewer filters, genealogy tree viewer large-tree-rendering, genealogy tree viewer lifecycle

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-genealogy-core` | `^1.0` |
| `liberusoftware/module-genealogy-people` | `^1.0` |
| `liberusoftware/module-genealogy-relationships` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Genealogy\\TreeViewer\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-genealogy-core": "^1.0", "liberusoftware/module-genealogy-people": "^1.0", "liberusoftware/module-genealogy-relationships": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateTreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Actions/CreateTreeView.php) | `public function execute(array $attributes): TreeView` |
| [src/Actions/DeleteTreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Actions/DeleteTreeView.php) | `public function execute(TreeView $tree): void` |
| [src/Actions/UpdateTreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Actions/UpdateTreeView.php) | `public function execute(TreeView $tree, array $attributes): TreeView` |
| [src/Queries/TreeGraph.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Queries/TreeGraph.php) | `public function for( Person $root, int $generations = 3, bool $includeLiving = true, string $view = 'chart', bool $includeSiblings = false, int $maxNodes = 2000, ): array` |

Other non-legacy PHP sources: [src/Capability.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Capability.php) · [src/Events/TreeViewDeleted.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Events/TreeViewDeleted.php) · [src/Listeners/ReconcilePersonMerge.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Listeners/ReconcilePersonMerge.php) · [src/Models/TreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Models/TreeView.php) · [src/TreeViewerServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/TreeViewerServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_010000_create_genealogy_trees_table.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/database/migrations/2026_08_24_010000_create_genealogy_trees_table.php)
- [database/migrations/2026_08_24_020000_add_root_and_visibility_to_genealogy_trees.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/database/migrations/2026_08_24_020000_add_root_and_visibility_to_genealogy_trees.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/DomainTest.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/tests/Feature/DomainTest.php)
- [tests/Unit/CapabilityTest.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/tests/Unit/CapabilityTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
