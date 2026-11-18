# Accounting: Employee Expenses Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#employee-expenses). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-employee-expenses-vue-inertia`
**Matching domain module:** `accounting-employee-expenses`
**Application:** Accounting
**Source feature:** [Employee Expenses](../features/employee-expenses.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/employee-expenses.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Claims:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Categories:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Policy checks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Per diem:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Attendees:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Projects/dimensions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Approval:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reimbursement:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rejection:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Posting:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-employee-expenses-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `claims`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `categories`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `policy-checks`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `per-diem`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `attendees`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `projects-dimensions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `approval`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `reimbursement`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `rejection`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `posting`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-employee-expenses` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-employee-expenses-vue-inertia`](https://github.com/liberusoftware/module-accounting-employee-expenses-vue-inertia) (`@liberusoftware/module-accounting-employee-expenses-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/employee-expenses.md) · [Core plan](../core/employee-expenses.md) · [API plan](../api/employee-expenses.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Claims** | Render `claims` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Categories** | Render `categories` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Policy checks** | Render `policy checks` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Per diem** | Render `per diem` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Attendees** | Render `attendees` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Projects/dimensions** | Render `projects/dimensions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Approval** | Render `approval` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Reimbursement** | Render `reimbursement` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Rejection** | Render `rejection` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Posting** | Render `posting` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
