# liberusoftware/module-liberu-business-workflow-reconciliation: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Cross-product workflow run registry and recovery-safe reconciliation.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [liberu-business-workflow-reconciliation](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-business-workflow-reconciliation/composer.json) | `39a49babafc0` | [Variant 3](#variant-3) | 0 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [liberu-business-workflow-reconciliation](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 2 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-liberu-business-workflow-reconciliation](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-business-workflow-reconciliation/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 2 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [liberu-business-workflow-reconciliation](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/composer.json) | `577e93db23cc` | [Variant 2](#variant-2) | 2 |

Physical source locations: **4**. Reference variants: **3**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: billing-laravel, `liberu-business-workflow-reconciliation`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-liberu-business-workflow-reconciliation` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `liberu-business-workflow-reconciliation` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Platform\\BusinessWorkflowReconciliation\\BusinessWorkflowReconciliationServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation/composer.json) · [module.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation/module.json).

**Declared capabilities:** liberu.business-workflow-reconciliation, liberu.business-workflow-reconciliation.lifecycle

**Declared features:** liberu business workflow reconciliation, liberu business workflow reconciliation lifecycle

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Platform\\BusinessWorkflowReconciliation\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateReconciliationCase.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation/src/Actions/CreateReconciliationCase.php) | `public function execute(array $attributes): ReconciliationCase` |

Other non-legacy PHP sources: [src/BusinessWorkflowReconciliationServiceProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation/src/BusinessWorkflowReconciliationServiceProvider.php) · [src/Capability.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation/src/Capability.php) · [src/Models/ReconciliationCase.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation/src/Models/ReconciliationCase.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_010000_create_liberu_reconciliation_cases_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation/database/migrations/2026_08_24_010000_create_liberu_reconciliation_cases_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/DomainTest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation/tests/Feature/DomainTest.php)
- [tests/Unit/CapabilityTest.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation/tests/Unit/CapabilityTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: genealogy-laravel, `liberu-business-workflow-reconciliation`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-liberu-business-workflow-reconciliation` |
| Composer version field | `1.1.1` |
| Package type | `liberu-module` |
| Module manifest name | `liberu-business-workflow-reconciliation` |
| Module version field | `1.1.1` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Platform\\BusinessWorkflowReconciliation\\BusinessWorkflowReconciliationServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/composer.json) · [module.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/module.json).

**Declared capabilities:** liberu.business-workflow-reconciliation, liberu.business-workflow-reconciliation.lifecycle

**Declared features:** liberu business workflow reconciliation, liberu business workflow reconciliation lifecycle

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Platform\\BusinessWorkflowReconciliation\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateReconciliationCase.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/src/Actions/CreateReconciliationCase.php) | `public function execute(array $attributes): ReconciliationCase` |
| [src/Actions/TransitionReconciliationCase.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/src/Actions/TransitionReconciliationCase.php) | `public function execute(ReconciliationCase $record, LifecycleStatus $to): ReconciliationCase` |

Other non-legacy PHP sources: [src/BusinessWorkflowReconciliationServiceProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/src/BusinessWorkflowReconciliationServiceProvider.php) · [src/Capability.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/src/Capability.php) · [src/Enums/LifecycleStatus.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/src/Enums/LifecycleStatus.php) · [src/Events/ReconciliationCaseTransitioned.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/src/Events/ReconciliationCaseTransitioned.php) · [src/Exceptions/InvalidLifecycleTransition.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/src/Exceptions/InvalidLifecycleTransition.php) · [src/Models/ReconciliationCase.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/src/Models/ReconciliationCase.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_010000_create_liberu_reconciliation_cases_table.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/database/migrations/2026_08_24_010000_create_liberu_reconciliation_cases_table.php)

[src/Enums/LifecycleStatus.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/src/Enums/LifecycleStatus.php): `Draft = 'draft'`, `Active = 'active'`, `Completed = 'completed'`, `Archived = 'archived'`.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/DomainTest.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/tests/Feature/DomainTest.php)
- [tests/Unit/CapabilityTest.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-business-workflow-reconciliation/tests/Unit/CapabilityTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 3

Representative: accounting-erp-laravel, `liberu-business-workflow-reconciliation`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-liberu-business-workflow-reconciliation` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `liberu-business-workflow-reconciliation` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\BusinessWorkflowReconciliation\\BusinessWorkflowReconciliationServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\BusinessWorkflowReconciliation\\BusinessWorkflowReconciliationServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-business-workflow-reconciliation/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-business-workflow-reconciliation/module.json).

**Declared capabilities:** liberu.business.workflow.reconciliation

**Declared features:** Workflow run registry, State mapping, Reconciliation rules, Recovery coordination, Audit timeline

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BusinessWorkflowReconciliation\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/StartWorkflowRun.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-business-workflow-reconciliation/src/Actions/StartWorkflowRun.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(array $attributes): WorkflowRun` |

Other non-legacy PHP sources: [src/BusinessWorkflowReconciliationServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-business-workflow-reconciliation/src/BusinessWorkflowReconciliationServiceProvider.php) · [src/Enums/WorkflowRunState.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-business-workflow-reconciliation/src/Enums/WorkflowRunState.php) · [src/Events/WorkflowRunStarted.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-business-workflow-reconciliation/src/Events/WorkflowRunStarted.php) · [src/Models/WorkflowRun.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-business-workflow-reconciliation/src/Models/WorkflowRun.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000000_create_liberu_workflow_runs_table.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-business-workflow-reconciliation/database/migrations/2026_08_24_000000_create_liberu_workflow_runs_table.php)

[src/Enums/WorkflowRunState.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-business-workflow-reconciliation/src/Enums/WorkflowRunState.php): `Running = 'running'`, `Reconciled = 'reconciled'`, `NeedsRecovery = 'needs_recovery'`, `Resolved = 'resolved'`.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
