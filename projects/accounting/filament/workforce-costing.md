# Accounting: Workforce Costing Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#workforce-costing). Observed identity: [`liberusoftware/module-accounting-workforce-costing-filament`](../../../modules/source/liberusoftware--module-accounting-workforce-costing-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-workforce-costing-filament`  
**Matching domain module:** `accounting-workforce-costing`  
**Application:** Accounting  
**Source feature:** [Workforce Costing](../features/workforce-costing.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-workforce-costing` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Time/payroll cost allocation to project:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Department:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Class/location:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Capitalization rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Profitability reporting:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-workforce-costing-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `time-payroll-cost-allocation-to-project`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `department`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `class-location`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `capitalization-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `profitability-reporting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-workforce-costing` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-workforce-costing-filament`](https://github.com/liberusoftware/module-accounting-workforce-costing-filament) (`liberusoftware/accounting-workforce-costing-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/workforce-costing.md) · [API plan](../api/workforce-costing.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Time/payroll cost allocation to project** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `time/payroll cost allocation to project`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Department** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `department`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Class/location** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `class/location`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Capitalization rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `capitalization rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Profitability reporting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `profitability reporting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListWorkforceCostingRules.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing-filament/src/Resources/Pages/ListWorkforceCostingRules.php) · [ListWorkforceCosts.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing-filament/src/Resources/Pages/ListWorkforceCosts.php) · [WorkforceCostResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing-filament/src/Resources/WorkforceCostResource.php) · [WorkforceCostingRuleResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing-filament/src/Resources/WorkforceCostingRuleResource.php) · [WorkforceCostingFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing-filament/src/WorkforceCostingFilamentPlugin.php) · [WorkforceCostingFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing-filament/src/WorkforceCostingFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [WorkforceProfitability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Queries/WorkforceProfitability.php) | `public function handle(int $teamId, ?string $from = null, ?string $to = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateWorkforceCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/AllocateWorkforceCost.php) | `public function handle(WorkforceCost $cost, string\|WorkforceAllocationType $allocationType, string $allocationRef): WorkforceCost` |
| [CapitalizeWorkforceCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/CapitalizeWorkforceCost.php) | `public function handle(WorkforceCost $cost): WorkforceCost` |
| [CreateWorkforceCostingRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/CreateWorkforceCostingRule.php) | `public function handle(array $attributes): WorkforceCostingRule` |
| [RecordWorkforceCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Actions/RecordWorkforceCost.php) | `public function handle(array $attributes): WorkforceCost` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorkforceCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Models/WorkforceCost.php) | `team_id`, `worker_ref`, `source_type`, `source_id`, `cost_date`, `hours`, `hourly_rate`, `amount`, `allocation_type`, `allocation_ref`, `capitalized`, `status`, `metadata` |
| [WorkforceCostingRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing/src/Models/WorkforceCostingRule.php) | `team_id`, `name`, `allocation_type`, `allocation_ref`, `hourly_rate`, `capitalize`, `active`, `metadata` |
<!-- layer-implementation-plan:end -->
