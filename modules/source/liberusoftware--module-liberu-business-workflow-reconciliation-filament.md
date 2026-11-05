# liberusoftware/module-liberu-business-workflow-reconciliation-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Liberu liberu-business-workflow-reconciliation-filament module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [liberu-business-workflow-reconciliation-filament](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation-filament/composer.json) | `4743bdfebd1c` | [Variant 2](#variant-2) | 1 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-liberu-business-workflow-reconciliation-filament](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-business-workflow-reconciliation-filament/composer.json) | `4743bdfebd1c` | [Variant 2](#variant-2) | 1 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [liberu-business-workflow-reconciliation-filament](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation-filament/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 1 |

Physical source locations: **3**. Reference variants: **2**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-genealogy-laravel-filament, `liberu-business-workflow-reconciliation-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-liberu-business-workflow-reconciliation-filament` |
| Composer version field | `1.1.1` |
| Package type | `liberu-module` |
| Module manifest name | `liberu-business-workflow-reconciliation-filament` |
| Module version field | `1.1.1` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Platform\\BusinessWorkflowReconciliation\\Filament\\BusinessWorkflowReconciliationFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation-filament/composer.json) · [module.json](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation-filament/module.json).

**Declared capabilities:** liberu.business-workflow-reconciliation.filament

**Declared features:** filament presentation for business-workflow-reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-liberu-business-workflow-reconciliation` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Platform\\BusinessWorkflowReconciliation\\Filament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-liberu-business-workflow-reconciliation": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/BusinessWorkflowReconciliationFilamentServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation-filament/src/BusinessWorkflowReconciliationFilamentServiceProvider.php) · [src/Resources/ReconciliationCaseResource.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation-filament/src/Resources/ReconciliationCaseResource.php) · [src/Resources/ReconciliationCaseResource/Pages/CreateReconciliationCase.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation-filament/src/Resources/ReconciliationCaseResource/Pages/CreateReconciliationCase.php) · [src/Resources/ReconciliationCaseResource/Pages/EditReconciliationCase.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation-filament/src/Resources/ReconciliationCaseResource/Pages/EditReconciliationCase.php) · [src/Resources/ReconciliationCaseResource/Pages/ListReconciliationCases.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation-filament/src/Resources/ReconciliationCaseResource/Pages/ListReconciliationCases.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Unit/BoundaryTest.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation-filament/tests/Unit/BoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: project-billing-laravel-filament, `liberu-business-workflow-reconciliation-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-liberu-business-workflow-reconciliation-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `liberu-business-workflow-reconciliation-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Platform\\BusinessWorkflowReconciliation\\Filament\\BusinessWorkflowReconciliationFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation-filament/composer.json) · [module.json](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation-filament/module.json).

**Declared capabilities:** liberu.business-workflow-reconciliation.filament

**Declared features:** filament presentation for business-workflow-reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-liberu-business-workflow-reconciliation` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Platform\\BusinessWorkflowReconciliation\\Filament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-liberu-business-workflow-reconciliation": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/BusinessWorkflowReconciliationFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation-filament/src/BusinessWorkflowReconciliationFilamentServiceProvider.php) · [src/Resources/ReconciliationCaseResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation-filament/src/Resources/ReconciliationCaseResource.php) · [src/Resources/ReconciliationCaseResource/Pages/CreateReconciliationCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation-filament/src/Resources/ReconciliationCaseResource/Pages/CreateReconciliationCase.php) · [src/Resources/ReconciliationCaseResource/Pages/EditReconciliationCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation-filament/src/Resources/ReconciliationCaseResource/Pages/EditReconciliationCase.php) · [src/Resources/ReconciliationCaseResource/Pages/ListReconciliationCases.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation-filament/src/Resources/ReconciliationCaseResource/Pages/ListReconciliationCases.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Unit/BoundaryTest.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation-filament/tests/Unit/BoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
