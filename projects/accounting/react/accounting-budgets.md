# Accounting: Accounting Budgets React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-budgets). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-accounting-budgets-react-inertia`
**Matching domain module:** `accounting-budgets`
**Application:** Accounting
**Source feature:** [Accounting Budgets](../features/accounting-budgets.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-budgets.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Annual/rolling budgets:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Accounts/dimensions/projects:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Imports:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Versions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Approvals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Phasing:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Actual comparison:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Revisions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-budgets-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `annual-rolling-budgets`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `accounts-dimensions-projects`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `imports`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `versions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `approvals`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `phasing`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `actual-comparison`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `revisions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-budgets` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-budgets-react-inertia`](https://github.com/liberusoftware/module-accounting-budgets-react-inertia) (`@liberusoftware/module-accounting-budgets-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/accounting-budgets.md) · [Core plan](../core/accounting-budgets.md) · [API plan](../api/accounting-budgets.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Annual/rolling budgets** | Render `annual/rolling budgets` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Accounts/dimensions/projects** | Render `accounts/dimensions/projects` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Imports** | Render `imports` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Versions** | Render `versions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Approvals** | Render `approvals` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Phasing** | Render `phasing` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Actual comparison** | Render `actual comparison` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Revisions** | Render `revisions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

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

| Observed API controller | Handler signatures |
| --- | --- |
| [BudgetsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-api/src/Http/Controllers/BudgetsController.php) | `public function index(Request $request, BudgetQuery $query): mixed`<br>`public function store(Request $request, CreateBudget $action): BudgetResource`<br>`public function show(Request $request, Budget $budget): BudgetResource`<br>`public function addLine(Request $request, Budget $budget, AddBudgetLine $action): BudgetResource`<br>`public function submit(Request $request, Budget $budget, SubmitBudget $action): BudgetResource`<br>`public function approve(Request $request, Budget $budget, ApproveBudget $action): BudgetResource`<br>`public function revise(Request $request, Budget $budget, ReviseBudget $action): BudgetResource` |

**Observed route declarations:**

[modules/accounting-budgets-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/budgets')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [BudgetsController::class, 'index'])->middleware('ability:accounting.budgets.read');
Route::post('/', [BudgetsController::class, 'store'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/submit', [BudgetsController::class, 'submit'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/lines', [BudgetsController::class, 'addLine'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/approve', [BudgetsController::class, 'approve'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/revise', [BudgetsController::class, 'revise'])->middleware('ability:accounting.budgets.write');
Route::get('/{budget}', [BudgetsController::class, 'show'])->middleware('ability:accounting.budgets.read');
```
<!-- layer-implementation-plan:end -->
