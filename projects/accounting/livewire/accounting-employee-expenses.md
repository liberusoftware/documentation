# Accounting: Accounting Employee Expenses Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-employee-expenses). Observed identity: [`liberusoftware/module-accounting-employee-expenses-livewire`](../../../modules/source/liberusoftware--module-accounting-employee-expenses-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-employee-expenses-livewire`  
**Matching domain module:** `accounting-employee-expenses`  
**Application:** Accounting  
**Source feature:** [Accounting Employee Expenses](../features/accounting-employee-expenses.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Claims:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Categories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Policy checks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Per diem:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Attendees:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Projects/dimensions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Approval:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reimbursement:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rejection:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Posting:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-employee-expenses-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingEmployeeExpenses::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `claims`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `categories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `policy-checks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `per-diem`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `attendees`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `projects-dimensions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `approval`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reimbursement`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rejection`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `posting`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-employee-expenses` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-employee-expenses.md) · [API plan](../api/accounting-employee-expenses.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Claims** | Expose a focused Livewire 4 component and namespaced Blade default view for `claims` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Categories** | Expose a focused Livewire 4 component and namespaced Blade default view for `categories` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Policy checks** | Expose a focused Livewire 4 component and namespaced Blade default view for `policy checks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Per diem** | Expose a focused Livewire 4 component and namespaced Blade default view for `per diem` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Attendees** | Expose a focused Livewire 4 component and namespaced Blade default view for `attendees` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Projects/dimensions** | Expose a focused Livewire 4 component and namespaced Blade default view for `projects/dimensions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Approval** | Expose a focused Livewire 4 component and namespaced Blade default view for `approval` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reimbursement** | Expose a focused Livewire 4 component and namespaced Blade default view for `reimbursement` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rejection** | Expose a focused Livewire 4 component and namespaced Blade default view for `rejection` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Posting** | Expose a focused Livewire 4 component and namespaced Blade default view for `posting` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Claims.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses-livewire/src/Livewire/Claims.php) · [EmployeeExpensesLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses-livewire/src/EmployeeExpensesLivewireServiceProvider.php).

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
