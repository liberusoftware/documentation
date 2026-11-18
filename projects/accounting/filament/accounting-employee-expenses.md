# Accounting: Accounting Employee Expenses Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-employee-expenses). Observed identity: [`liberusoftware/module-accounting-employee-expenses-filament`](../../../modules/source/liberusoftware--module-accounting-employee-expenses-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-employee-expenses-filament`  
**Matching domain module:** `accounting-employee-expenses`  
**Application:** Accounting  
**Source feature:** [Accounting Employee Expenses](../features/accounting-employee-expenses.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-employee-expenses` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Claims:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Categories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Policy checks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Per diem:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attendees:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Projects/dimensions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reimbursement:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rejection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Posting:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-employee-expenses-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `claims`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `categories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `policy-checks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `per-diem`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attendees`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `projects-dimensions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reimbursement`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rejection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `posting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-employee-expenses` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-employee-expenses-filament`](https://github.com/liberusoftware/module-accounting-employee-expenses-filament) (`liberusoftware/accounting-employee-expenses-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-employee-expenses.md) · [API plan](../api/accounting-employee-expenses.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Claims** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `claims`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Categories** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `categories`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Policy checks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `policy checks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Per diem** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `per diem`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attendees** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attendees`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Projects/dimensions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `projects/dimensions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reimbursement** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reimbursement`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rejection** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rejection`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Posting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `posting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [EmployeeExpensesFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses-filament/src/EmployeeExpensesFilamentPlugin.php) · [EmployeeExpensesFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses-filament/src/EmployeeExpensesFilamentServiceProvider.php) · [ExpenseClaimResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses-filament/src/Resources/ExpenseClaimResource.php) · [ListExpenseClaims.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses-filament/src/Resources/Pages/ListExpenseClaims.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ExpenseClaimQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Queries/ExpenseClaimQuery.php) | `public function paginate(?int $teamId = null, ?ClaimStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function total(ExpenseClaim $c): float` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddExpenseItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Actions/AddExpenseItem.php) | `public function handle(ExpenseClaim $c, array $a): ExpenseItem` |
| [CreateExpenseClaim.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Actions/CreateExpenseClaim.php) | `public function handle(array $a): ExpenseClaim` |
| [DecideExpenseClaim.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Actions/DecideExpenseClaim.php) | `public function handle(ExpenseClaim $c, bool $approved, ?string $reason = null, ?string $actor = null): ExpenseClaim` |
| [PostExpenseClaim.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Actions/PostExpenseClaim.php) | `public function handle(ExpenseClaim $c, ?string $actor = null): ExpenseClaim` |
| [ReimburseExpenseClaim.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Actions/ReimburseExpenseClaim.php) | `public function handle(ExpenseClaim $c, ?string $actor = null): ExpenseClaim` |
| [SubmitExpenseClaim.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Actions/SubmitExpenseClaim.php) | `public function handle(ExpenseClaim $c, ?string $actor = null): ExpenseClaim` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ExpenseCategory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Models/ExpenseCategory.php) | `team_id`, `category_ref`, `name`, `daily_limit`, `requires_receipt`, `metadata` |
| [ExpenseClaim.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Models/ExpenseClaim.php) | `team_id`, `employee_ref`, `claim_ref`, `currency`, `status`, `submitted_on`, `approved_on`, `reimbursed_on`, `posted_on`, `rejection_reason`, `project_ref`, `dimension_ref`, `metadata` |
| [ExpenseHistory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Models/ExpenseHistory.php) | `claim_id`, `event`, `actor_ref`, `metadata` |
| [ExpenseItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses/src/Models/ExpenseItem.php) | `claim_id`, `category_ref`, `spent_on`, `description`, `amount`, `tax_amount`, `merchant`, `receipt_ref`, `per_diem_days`, `attendees`, `metadata` |
| [Employee.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses-api/src/Models/Employee.php) | `name`, `email`, `position`, `hire_date`, `tax_id`, `national_insurance_number`, `starter_declaration`, `p45_issue_date`, `has_student_loan`, `student_loan_plan` |
<!-- layer-implementation-plan:end -->
