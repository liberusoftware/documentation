# Accounting: Accounting Workforce Costing React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-workforce-costing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-accounting-workforce-costing-react-inertia`
**Matching domain module:** `accounting-workforce-costing`
**Application:** Accounting
**Source feature:** [Accounting Workforce Costing](../features/accounting-workforce-costing.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-workforce-costing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Time/payroll cost allocation to project:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Department:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Class/location:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Capitalization rules:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Profitability reporting:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-workforce-costing-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `time-payroll-cost-allocation-to-project`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `department`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `class-location`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `capitalization-rules`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `profitability-reporting`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-workforce-costing` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-workforce-costing-react-inertia`](https://github.com/liberusoftware/module-accounting-workforce-costing-react-inertia) (`@liberusoftware/module-accounting-workforce-costing-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/accounting-workforce-costing.md) · [Core plan](../core/accounting-workforce-costing.md) · [API plan](../api/accounting-workforce-costing.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Time/payroll cost allocation to project** | Render `time/payroll cost allocation to project` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Department** | Render `department` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Class/location** | Render `class/location` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Capitalization rules** | Render `capitalization rules` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Profitability reporting** | Render `profitability reporting` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

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

| Observed API controller | Handler signatures |
| --- | --- |
| [WorkforceCostingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing-api/src/Http/Controllers/WorkforceCostingController.php) | `public function costs(Request $request): mixed`<br>`public function record(Request $request, RecordWorkforceCost $action): mixed`<br>`public function allocate(Request $request, string $cost, AllocateWorkforceCost $action): mixed`<br>`public function capitalize(Request $request, string $cost, CapitalizeWorkforceCost $action): mixed`<br>`public function rules(Request $request): mixed`<br>`public function createRule(Request $request, CreateWorkforceCostingRule $action): mixed`<br>`public function profitability(Request $request, WorkforceProfitability $query): mixed` |

**Observed route declarations:**

[modules/accounting-workforce-costing-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workforce-costing-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/workforce-costing')->middleware('auth:sanctum')->group(function (): void {
Route::get('/costs', [WorkforceCostingController::class, 'costs'])->middleware('ability:accounting.workforce-costing.read');
Route::post('/costs', [WorkforceCostingController::class, 'record'])->middleware('ability:accounting.workforce-costing.write');
Route::post('/costs/{cost}/allocate', [WorkforceCostingController::class, 'allocate'])->middleware('ability:accounting.workforce-costing.write');
Route::post('/costs/{cost}/capitalize', [WorkforceCostingController::class, 'capitalize'])->middleware('ability:accounting.workforce-costing.write');
Route::get('/rules', [WorkforceCostingController::class, 'rules'])->middleware('ability:accounting.workforce-costing.read');
Route::post('/rules', [WorkforceCostingController::class, 'createRule'])->middleware('ability:accounting.workforce-costing.write');
Route::get('/profitability', [WorkforceCostingController::class, 'profitability'])->middleware('ability:accounting.workforce-costing.read');
```
<!-- layer-implementation-plan:end -->
