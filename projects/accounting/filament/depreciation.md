# Accounting: Depreciation Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#depreciation). Observed identity: [`liberusoftware/module-accounting-depreciation-filament`](../../../modules/source/liberusoftware--module-accounting-depreciation-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-depreciation-filament`  
**Matching domain module:** `accounting-depreciation`  
**Application:** Accounting  
**Source feature:** [Depreciation](../features/depreciation.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-depreciation` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Methods:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conventions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Useful life:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Residual value:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Runs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Journals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tax books:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Forecast:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-depreciation-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `methods`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conventions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `useful-life`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `residual-value`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `runs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `journals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tax-books`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `forecast`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-depreciation` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-depreciation-filament`](https://github.com/liberusoftware/module-accounting-depreciation-filament) (`liberusoftware/accounting-depreciation-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/depreciation.md) · [API plan](../api/depreciation.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Methods** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `methods`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Conventions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `conventions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Useful life** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `useful life`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Residual value** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `residual value`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schedules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schedules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Runs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `runs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Journals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `journals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tax books** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tax books`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Forecast** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `forecast`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DepreciationFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation-filament/src/DepreciationFilamentPlugin.php) · [DepreciationFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation-filament/src/DepreciationFilamentServiceProvider.php) · [DepreciationScheduleResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation-filament/src/Resources/DepreciationScheduleResource.php) · [ListDepreciationSchedules.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation-filament/src/Resources/DepreciationScheduleResource/Pages/ListDepreciationSchedules.php).

| Observed core query | Public method signatures |
| --- | --- |
| [DepreciationForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation/src/Queries/DepreciationForecast.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDepreciationSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation/src/Actions/CreateDepreciationSchedule.php) | `public function handle(array $attributes): DepreciationSchedule` |
| [PostDepreciationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation/src/Actions/PostDepreciationRun.php) | `public function handle(DepreciationRun $run, int $actorId, string $journalReference): DepreciationRun` |
| [RunDepreciation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation/src/Actions/RunDepreciation.php) | `public function handle(DepreciationSchedule $schedule, string $periodStart, string $periodEnd): DepreciationRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DepreciationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation/src/Models/DepreciationRun.php) | `schedule_id`, `team_id`, `period_start`, `period_end`, `amount`, `accumulated_amount`, `status`, `journal_ref`, `posted_by`, `posted_at`, `metadata` |
| [DepreciationSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation/src/Models/DepreciationSchedule.php) | `team_id`, `asset_ref`, `book_ref`, `method`, `convention`, `useful_life_months`, `cost`, `residual_value`, `start_date`, `end_date`, `currency`, `status`, `metadata` |
| [DepreciationTaxBook.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-depreciation/src/Models/DepreciationTaxBook.php) | `team_id`, `book_ref`, `name`, `jurisdiction`, `metadata` |
<!-- layer-implementation-plan:end -->
