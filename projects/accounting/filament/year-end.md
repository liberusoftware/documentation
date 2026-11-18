# Accounting: Year End Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#year-end). Observed identity: [`liberusoftware/module-accounting-year-end-filament`](../../../modules/source/liberusoftware--module-accounting-year-end-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-year-end-filament`  
**Matching domain module:** `accounting-year-end`  
**Application:** Accounting  
**Source feature:** [Year End](../features/year-end.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-year-end` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Final adjustments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Retained earnings/roll-forward:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Opening balances:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Statutory/tax handoff:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lock:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Archive:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Evidence:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-year-end-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `final-adjustments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `retained-earnings-roll-forward`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `opening-balances`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `statutory-tax-handoff`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lock`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `archive`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-year-end` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-year-end-filament`](https://github.com/liberusoftware/module-accounting-year-end-filament) (`liberusoftware/accounting-year-end-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/year-end.md) · [API plan](../api/year-end.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Final adjustments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `final adjustments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Retained earnings/roll-forward** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `retained earnings/roll-forward`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Opening balances** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `opening balances`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Statutory/tax handoff** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `statutory/tax handoff`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lock** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lock`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Archive** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `archive`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListYearEndCloses.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end-filament/src/Resources/Pages/ListYearEndCloses.php) · [YearEndCloseResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end-filament/src/Resources/YearEndCloseResource.php) · [YearEndFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end-filament/src/YearEndFilamentPlugin.php) · [YearEndFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end-filament/src/YearEndFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [YearEndQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Queries/YearEndQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddYearEndAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/AddYearEndAdjustment.php) | `public function handle(YearEndPeriod $period, array $attributes): YearEndAdjustment` |
| [ArchiveYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/ArchiveYearEnd.php) | `public function handle(YearEndPeriod $period): YearEndPeriod` |
| [CloseYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CloseYearEnd.php) | `public function handle(YearEndClose $close, string $closingEntryRef): YearEndClose` |
| [CreateYearEndClose.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CreateYearEndClose.php) | `public function handle(array $attributes): YearEndClose` |
| [CreateYearEndPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CreateYearEndPeriod.php) | `public function handle(array $attributes): YearEndPeriod` |
| [LockYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/LockYearEnd.php) | `public function handle(YearEndPeriod $period, int $actor): YearEndPeriod` |
| [ReopenYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/ReopenYearEnd.php) | `public function handle(YearEndClose $close): YearEndClose` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [YearEndAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndAdjustment.php) | `period_id`, `team_id`, `adjustment_ref`, `amount`, `description`, `journal_ref`, `status`, `evidence` |
| [YearEndClose.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndClose.php) | `team_id`, `fiscal_year`, `period_end`, `retained_earnings_account_ref`, `net_income`, `status`, `closed_at`, `locked_at`, `closing_entry_ref`, `metadata` |
| [YearEndPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndPeriod.php) | `team_id`, `period_ref`, `period_end`, `status`, `retained_earnings`, `opening_balances`, `statutory_handoff`, `evidence`, `locked_by`, `locked_at`, `archived_at` |
<!-- layer-implementation-plan:end -->
