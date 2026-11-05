# liberusoftware/scheduler-queues: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Queue idempotency, retry, failure, scheduling, locking, and deployment conventions.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/scheduler-queues/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 1 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/scheduler-queues/composer.json) | `68e5f07a6704` | [Variant 1](#variant-1) | 1 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/scheduler-queues/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 1 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/scheduler-queues/composer.json) | `3ade34046c3d` | [Variant 1](#variant-1) | 1 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/scheduler-queues/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 1 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/scheduler-queues/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 1 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/scheduler-queues/composer.json) | `63aad94e94c0` | [Variant 2](#variant-2) | 5 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/scheduler-queues/composer.json) | `b12a8c841c6a` | [Variant 1](#variant-1) | 1 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/scheduler-queues/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 1 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/scheduler-queues/composer.json) | `c267d625e264` | [Variant 1](#variant-1) | 1 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/scheduler-queues/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 1 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [scheduler-queues](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/scheduler-queues/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 1 |

Physical source locations: **12**. Reference variants: **2**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `scheduler-queues`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/scheduler-queues` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `scheduler-queues` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\SchedulerQueues\\SchedulerQueuesServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/scheduler-queues/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/scheduler-queues/module.json).

**Declared capabilities:** foundation.scheduler-queues

**Declared features:** Unique/idempotent job policy, Schedules, Locks, Retries, Failures, Monitoring, Graceful deployment conventions

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/console` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\SchedulerQueues\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Support/JobPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/scheduler-queues/src/Support/JobPolicy.php) | `public function backoff(int $attempt): int`<br>`public function assertIdempotencyKey(?string $key): string` |

Other non-legacy PHP sources: [src/SchedulerQueuesServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/scheduler-queues/src/SchedulerQueuesServiceProvider.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/scheduler-queues/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: project-crm-laravel-filament, `scheduler-queues`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/scheduler-queues` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `scheduler-queues` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\SchedulerQueues\\SchedulerQueuesServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/scheduler-queues/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/scheduler-queues/module.json).

**Declared capabilities:** foundation.scheduler-queues

**Declared features:** Unique/idempotent job policy, Schedules, Locks, Retries, Failures, Monitoring, Graceful deployment conventions

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/console` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\SchedulerQueues\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Support/JobPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/scheduler-queues/src/Support/JobPolicy.php) | `public function backoff(int $attempt): int`<br>`public function assertIdempotencyKey(?string $key): string` |

Other non-legacy PHP sources: [src/SchedulerQueuesServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/scheduler-queues/src/SchedulerQueuesServiceProvider.php).

**Legacy review:** 2 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **5**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/scheduler-queues/tests/.gitkeep)
- [tests/Feature/Console/CommandsTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/scheduler-queues/tests/Feature/Console/CommandsTest.php)
- [tests/Feature/Console/NotifyOverdueTasksTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/scheduler-queues/tests/Feature/Console/NotifyOverdueTasksTest.php)
- [tests/Feature/Jobs/JobsTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/scheduler-queues/tests/Feature/Jobs/JobsTest.php)
- [tests/Feature/Queue/TenantAwareJobTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/scheduler-queues/tests/Feature/Queue/TenantAwareJobTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
