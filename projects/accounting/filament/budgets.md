# Accounting: Budgets Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#budgets). Observed identity: [`liberusoftware/module-accounting-budgets-filament`](../../../modules/source/liberusoftware--module-accounting-budgets-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-budgets-filament`  
**Matching domain module:** `accounting-budgets`  
**Application:** Accounting  
**Source feature:** [Budgets](../features/budgets.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-budgets` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Annual/rolling budgets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Accounts/dimensions/projects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Imports:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Versions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Phasing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Actual comparison:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Revisions:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-budgets-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `annual-rolling-budgets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `accounts-dimensions-projects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `imports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `versions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `phasing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `actual-comparison`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `revisions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-budgets` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-budgets-filament`](https://github.com/liberusoftware/module-accounting-budgets-filament) (`liberusoftware/accounting-budgets-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/budgets.md) · [API plan](../api/budgets.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Annual/rolling budgets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `annual/rolling budgets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Accounts/dimensions/projects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `accounts/dimensions/projects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Imports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `imports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Versions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `versions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approvals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approvals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Phasing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `phasing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Actual comparison** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `actual comparison`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Revisions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `revisions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [BudgetsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-filament/src/BudgetsFilamentPlugin.php) · [BudgetsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-filament/src/BudgetsFilamentServiceProvider.php) · [BudgetResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-filament/src/Resources/BudgetResource.php) · [CreateBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-filament/src/Resources/Pages/CreateBudget.php) · [ListBudgets.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-filament/src/Resources/Pages/ListBudgets.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BudgetQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Queries/BudgetQuery.php) | `public function paginate(int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddBudgetLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/AddBudgetLine.php) | `public function handle(Budget $budget, array $attributes): BudgetLine` |
| [ApproveBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/ApproveBudget.php) | `public function handle(Budget $budget, int $actorId): Budget` |
| [CreateBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/CreateBudget.php) | `public function handle(array $attributes): Budget` |
| [ReviseBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/ReviseBudget.php) | `public function handle(Budget $budget, array $attributes): Budget` |
| [SubmitBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/SubmitBudget.php) | `public function handle(Budget $budget, int $actorId): Budget` |
| [BudgetsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-api/src/Policies/BudgetsPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function create(?object $user): bool`<br>`public function update(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Budget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Models/Budget.php) | `team_id`, `name`, `period_start`, `period_end`, `currency`, `status`, `version`, `notes`, `metadata`, `submitted_by`, `approved_by`, `approved_at`, `rejected_at` |
| [BudgetLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Models/BudgetLine.php) | `budget_id`, `account_id`, `project_id`, `dimensions`, `planned_amount`, `phases`, `actual_amount`, `notes` |
<!-- layer-implementation-plan:end -->
