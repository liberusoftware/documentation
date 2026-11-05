# liberusoftware/module-liberu-platform-orchestration: shared adoption review

**Status:** source-backed consolidation design, not a completed migration or stability certification. This profile records differences at the pinned commits and a data-preserving adoption path. Active source projects are unchanged by this documentation review.

## Ownership and decision

The documentation owner is the [liberu capability scope](../../projects/liberu/README.md). Keep one authoritative capability/release boundary and product-specific behavior behind reviewed extensions. This is a documentation ownership decision; select the actual package maintainer/canonical release repository from verified package governance before changing consumers.

Runtime variants: **3**; selected metadata variants: **3** under this exact manifest identity. Equal names/constraints do not make different schemas or providers interchangeable. Keep the installed identity and its data until a compatible release or explicit migration is reviewed.

See the [implementation reference](../../modules/source/liberusoftware--module-liberu-platform-orchestration.md), [source comparison](../SHARED-MODULE-COMPARISON.md) and [consolidation procedure](../SHARED-MODULES.md).

## Consumer variants

| Consumer | Pinned module metadata | Variant | Test files |
| --- | --- | ---: | ---: |
| accounting | [liberu-platform-orchestration](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-platform-orchestration/composer.json) | 2 | 0 |
| billing | [liberu-platform-orchestration](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-platform-orchestration/composer.json) | 1 | 2 |
| billing | [module-liberu-platform-orchestration](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-liberu-platform-orchestration/composer.json) | 1 | 2 |
| genealogy | [liberu-platform-orchestration](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-platform-orchestration/composer.json) | 3 | 2 |

## Manifest and dependency differences

Each row below is one representative per runtime/metadata combination. Module defaults and providers are declarations, not proof of deployment enablement. Read the actual host resolver and registration path; changing defaults can change the selected graph without changing the application manifest.

| Variant | Module name / version | Default | Provider(s) | Composer runtime requirements |
| --- | --- | --- | --- | --- |
| 1 | `liberu-platform-orchestration` / `1.0.0` | `True` | `"Liberu\\Platform\\PlatformOrchestration\\PlatformOrchestrationServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "php": "^8.5"}` |
| 2 | `liberu-platform-orchestration` / `1.0.0` | `True` | `"Liberu\\PlatformOrchestration\\PlatformOrchestrationServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/support": "^13.0", "liberusoftware/module-manager": "^1.0", "php": "^8.5"}` |
| 3 | `liberu-platform-orchestration` / `1.1.1` | `True` | `"Liberu\\Platform\\PlatformOrchestration\\PlatformOrchestrationServiceProvider"` | `{"illuminate/database": "^13.0", "illuminate/events": "^13.0", "illuminate/support": "^13.0", "php": "^8.5"}` |

## Persistence and data transition

The following database paths differ or are missing in at least one consumer. A missing file does not prove its table/data never existed, and a matching filename does not prove matching contents. Inspect migration history and the deployed database before adoption.

| Differing database path | Variant source and declared table operation |
| --- | --- |
| `database/migrations/2026_08_24_000000_create_liberu_platform_compositions_table.php` | V1: absent<br>V2: [687ae4a6b4](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-platform-orchestration/database/migrations/2026_08_24_000000_create_liberu_platform_compositions_table.php); create liberu_platform_compositions, dropIfExists liberu_platform_compositions<br>V3: absent |
| `database/migrations/2026_08_24_010000_create_liberu_platform_workflows_table.php` | V1: [4e7f462ffa](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-platform-orchestration/database/migrations/2026_08_24_010000_create_liberu_platform_workflows_table.php); create liberu_platform_workflows, dropIfExists liberu_platform_workflows<br>V2: absent<br>V3: [c2c5dc6d6f](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-platform-orchestration/database/migrations/2026_08_24_010000_create_liberu_platform_workflows_table.php); create liberu_platform_workflows, dropIfExists liberu_platform_workflows |

Before a shared release, inventory affected tables/columns and tenant/source identifiers in every consumer, then map legacy/current record identities and callers. Use additive backfills or a separate migration with reconciliation and recovery; do not drop a historical table because the chosen package tree lacks its old migration. Reconcile counts, ownership and required evidence before moving callers or removing obsolete implementations.

## Public contract and extension review

Changed action/query/contract/service/context paths are indexed below. Signature differences identify compatibility work; equal signatures alone do not prove matching authorization, validation, side effects or event timing.

| Path | Variant entry points |
| --- | --- |
| `src/Actions/CreateComposition.php` | V1: absent<br>V2: [CreateComposition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-platform-orchestration/src/Actions/CreateComposition.php) — `public function __construct(private readonly Dispatcher $events)` ; `public function handle(array $attributes): PlatformComposition`<br>V3: absent |
| `src/Actions/CreatePlatformWorkflow.php` | V1: [CreatePlatformWorkflow.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-platform-orchestration/src/Actions/CreatePlatformWorkflow.php) — `public function execute(array $attributes): PlatformWorkflow`<br>V2: absent<br>V3: [CreatePlatformWorkflow.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-platform-orchestration/src/Actions/CreatePlatformWorkflow.php) — `public function execute(array $attributes): PlatformWorkflow` |
| `src/Actions/TransitionComposition.php` | V1: absent<br>V2: [TransitionComposition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-platform-orchestration/src/Actions/TransitionComposition.php) — `public function __construct(private readonly Dispatcher $events)` ; `public function handle(PlatformComposition $composition, CompositionState $state): PlatformComposition`<br>V3: absent |
| `src/Actions/TransitionPlatformWorkflow.php` | V1: absent<br>V2: absent<br>V3: [TransitionPlatformWorkflow.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-platform-orchestration/src/Actions/TransitionPlatformWorkflow.php) — `public function execute(PlatformWorkflow $record, LifecycleStatus $to): PlatformWorkflow` |

Resolve host-model lookups, actor/tenant policy, source-record references and provider dependencies through explicit public contracts/configuration. Keep product policy and presentation composition outside shared core. Consumer tests must cover the real call paths, including jobs/exports and private-data visibility; do not widen a contract solely to accommodate one host's internal model.

## Registration, route and presentation review

- `module.json`: V1 [source](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-platform-orchestration/module.json), V2 [source](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-platform-orchestration/module.json), V3 [source](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-platform-orchestration/module.json)
- `src/PlatformOrchestrationServiceProvider.php`: V1 [source](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-platform-orchestration/src/PlatformOrchestrationServiceProvider.php), V2 [source](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-platform-orchestration/src/PlatformOrchestrationServiceProvider.php), V3 [source](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/liberu-platform-orchestration/src/PlatformOrchestrationServiceProvider.php)

Validate discovery, manifest schema/version handling, dependency selection, provider boot order and route/plugin identifiers against the consuming host. For UI/API adapters, retain the authorized DTO and domain action semantics rather than exposing private models or bypassing transitions through generic record saves.

React/Inertia and Next.js can share framework-independent components, not page/session/redirect lifecycles. If a shared adapter is proposed, review all relevant variants and declared peers/exports first; a shared documentation home is not a completed code migration.

## Adoption sequence and acceptance

1. Confirm the canonical maintainer/release source and supported versions, then compare every source variant above with its actual host callers and schema. Keep the existing installed identities until that decision is reviewed.
2. Separate genuine shared behavior from product-specific legacy/adapters. Define the required extension points and map source-record IDs/data before removing or redirecting a caller.
3. Release compatible changes or an explicitly versioned migration. Test a clean consumer and upgrade/recovery path without local dependency overrides; package version strings and source tests are not release evidence.
4. Adopt one consumer through a targeted dependency/lockfile update, verify data reconciliation and meaningful permitted/denied/tenant/retry journeys, then expand to other consumers.
5. Record package/source versions, schema/data transition, retained extensions, checks run, remaining limitations and operational recovery. Preserve tracked installed trees and all documented product capabilities until callers/data have moved.

The current documentation supplies source comparisons and a consolidation design. Application refactoring, migration execution, package publication and certification of a stable common release remain separate owning-project work.
