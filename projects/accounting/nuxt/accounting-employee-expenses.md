# Accounting: Accounting Employee Expenses Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-employee-expenses). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-employee-expenses-nuxt`
**Matching domain module:** `accounting-employee-expenses`
**Application:** Accounting
**Source feature:** [Accounting Employee Expenses](../features/accounting-employee-expenses.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-employee-expenses.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-employee-expenses` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Claims:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Categories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Policy checks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Per diem:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attendees:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Projects/dimensions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approval:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reimbursement:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rejection:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Posting:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-employee-expenses-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `claims`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `categories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `policy-checks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `per-diem`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `attendees`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `projects-dimensions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reimbursement`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rejection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `posting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-employee-expenses` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-employee-expenses.md)) |
| Capability Nuxt module skeleton | [`module-accounting-employee-expenses-nuxt`](https://github.com/liberusoftware/module-accounting-employee-expenses-nuxt) (`@liberusoftware/module-accounting-employee-expenses-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Claims** | Expose composable and Vue 3 component for `claims` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-employee-expenses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Categories** | Expose composable and Vue 3 component for `categories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-employee-expenses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Policy checks** | Expose composable and Vue 3 component for `policy checks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-employee-expenses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Per diem** | Expose composable and Vue 3 component for `per diem` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-employee-expenses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Attendees** | Expose composable and Vue 3 component for `attendees` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-employee-expenses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Projects/dimensions** | Expose composable and Vue 3 component for `projects/dimensions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-employee-expenses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approval** | Expose composable and Vue 3 component for `approval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-employee-expenses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reimbursement** | Expose composable and Vue 3 component for `reimbursement` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-employee-expenses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Rejection** | Expose composable and Vue 3 component for `rejection` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-employee-expenses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Posting** | Expose composable and Vue 3 component for `posting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-employee-expenses.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

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

| Observed API controller | Handler signatures |
| --- | --- |
| [ExpenseClaimsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses-api/src/Http/Controllers/ExpenseClaimsController.php) | `public function __construct(private readonly ExpenseClaimQuery $query)`<br>`public function index(Request $r): mixed`<br>`public function store(Request $r, CreateExpenseClaim $a): ExpenseClaimResource`<br>`public function show(ExpenseClaim $c): ExpenseClaimResource`<br>`public function item(Request $r, ExpenseClaim $c, AddExpenseItem $a): ExpenseClaimResource`<br>`public function submit(Request $r, ExpenseClaim $c, SubmitExpenseClaim $a): ExpenseClaimResource`<br>`public function decide(Request $r, ExpenseClaim $c, DecideExpenseClaim $a): ExpenseClaimResource`<br>`public function reimburse(Request $r, ExpenseClaim $c, ReimburseExpenseClaim $a): ExpenseClaimResource`<br>`public function post(Request $r, ExpenseClaim $c, PostExpenseClaim $a): ExpenseClaimResource` |

**Observed route declarations:**

[modules/accounting-employee-expenses-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-employee-expenses-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/employee-expenses')->group(function (): void {
Route::middleware('ability:accounting.employee-expenses.read')->group(function (): void {
Route::get('/', [ExpenseClaimsController::class, 'index']);
Route::get('/{c}', [ExpenseClaimsController::class, 'show']);
Route::middleware('ability:accounting.employee-expenses.write')->group(function (): void {
Route::post('/', [ExpenseClaimsController::class, 'store']);
Route::post('/{c}/items', [ExpenseClaimsController::class, 'item']);
Route::post('/{c}/submit', [ExpenseClaimsController::class, 'submit']);
Route::post('/{c}/decide', [ExpenseClaimsController::class, 'decide']);
Route::post('/{c}/reimburse', [ExpenseClaimsController::class, 'reimburse']);
Route::post('/{c}/post', [ExpenseClaimsController::class, 'post']);
```
<!-- layer-implementation-plan:end -->
