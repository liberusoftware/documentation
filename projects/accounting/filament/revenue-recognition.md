# Accounting: Revenue Recognition Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-recognition). Observed identity: [`liberusoftware/module-accounting-revenue-recognition-filament`](../../../modules/source/liberusoftware--module-accounting-revenue-recognition-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-revenue-recognition-filament`  
**Matching domain module:** `accounting-revenue-recognition`  
**Application:** Accounting  
**Source feature:** [Revenue Recognition](../features/revenue-recognition.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-revenue-recognition` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Obligations/schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Allocation references:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deferred/accrued revenue:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recognition runs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Modifications:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation (optional):** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-revenue-recognition-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `obligations-schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `allocation-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deferred-accrued-revenue`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recognition-runs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `modifications`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation-optional`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-revenue-recognition` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-revenue-recognition-filament`](https://github.com/liberusoftware/module-accounting-revenue-recognition-filament) (`liberusoftware/accounting-revenue-recognition-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/revenue-recognition.md) · [API plan](../api/revenue-recognition.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Obligations/schedules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `obligations/schedules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Allocation references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `allocation references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deferred/accrued revenue** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deferred/accrued revenue`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recognition runs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recognition runs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Modifications** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `modifications`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation (optional)** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation (optional)`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListRevenueSchedules.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition-filament/src/Resources/Pages/ListRevenueSchedules.php) · [RevenueScheduleResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition-filament/src/Resources/RevenueScheduleResource.php) · [RevenueRecognitionFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition-filament/src/RevenueRecognitionFilamentPlugin.php) · [RevenueRecognitionFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition-filament/src/RevenueRecognitionFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateRevenueSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/CreateRevenueSchedule.php) | `public function handle(array $attributes): RevenueSchedule` |
| [ModifyRevenueSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/ModifyRevenueSchedule.php) | `public function handle(RevenueSchedule $schedule, array $attributes): RevenueModification` |
| [RecognizeDueRevenue.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/RecognizeDueRevenue.php) | `public function handle(RevenueSchedule $schedule, string $asOfDate, ?int $teamId = null): RevenueRecognitionRun` |
| [ReconcileRevenueRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/ReconcileRevenueRun.php) | `public function handle(RevenueRecognitionRun $run, array $references = []): RevenueRecognitionRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RevenueAllocationReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueAllocationReference.php) | `team_id`, `reference_type`, `reference_id`, `allocation`, `status`, `metadata` |
| [RevenueModification.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueModification.php) | `schedule_id`, `effective_date`, `amount_delta`, `reason`, `status`, `metadata` |
| [RevenueObligation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueObligation.php) | `team_id`, `source_type`, `source_id`, `description`, `currency`, `total_amount`, `start_date`, `periods`, `status`, `metadata` |
| [RevenueRecognitionRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueRecognitionRun.php) | `team_id`, `as_of_date`, `status`, `processed_entries`, `failed_entries`, `errors`, `metadata`, `started_at`, `finished_at` |
| [RevenueReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueReconciliation.php) | `run_id`, `reference_type`, `reference_id`, `expected_amount`, `recognized_amount`, `variance`, `status`, `notes`, `metadata` |
| [RevenueSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueSchedule.php) | `obligation_id`, `allocation_reference_id`, `total_amount`, `start_date`, `periods`, `deferred_account_ref`, `revenue_account_ref`, `status`, `funded`, `metadata` |
| [RevenueScheduleEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueScheduleEntry.php) | `schedule_id`, `period_number`, `recognition_date`, `amount`, `status`, `recognized_at`, `ledger_reference`, `metadata` |
<!-- layer-implementation-plan:end -->
