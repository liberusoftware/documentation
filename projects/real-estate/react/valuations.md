# Real Estate: Valuations React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#valuations). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-real-estate-valuations-react-inertia`
**Matching domain module:** `real-estate-valuations`
**Application:** Real Estate
**Source feature:** [Valuations](../features/valuations.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/valuations.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Appraisals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Comparables:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Pricing:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Fees:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Recommendations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Follow-up:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Conversion:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-real-estate-valuations-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `appraisals`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `comparables`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `pricing`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `fees`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `recommendations`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `follow-up`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `conversion`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-valuations` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-real-estate-laravel-inertia-react`](https://github.com/liberusoftware/project-real-estate-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-real-estate-valuations-react-inertia`](https://github.com/liberusoftware/module-real-estate-valuations-react-inertia) (`@liberusoftware/module-real-estate-valuations-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/valuations.md) · [Core plan](../core/valuations.md) · [API plan](../api/valuations.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Appraisals** | Render `appraisals` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Comparables** | Render `comparables` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Pricing** | Render `pricing` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Fees** | Render `fees` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Recommendations** | Render `recommendations` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Follow-up** | Render `follow-up` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Conversion** | Render `conversion` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ValuationPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Policies/ValuationPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Valuation $valuation): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Valuation $valuation): bool`<br>`public function delete(AuthUser $authUser, Valuation $valuation): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Valuation $valuation): bool`<br>`public function forceDelete(AuthUser $authUser, Valuation $valuation): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Valuation $valuation): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Valuation.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Models/Valuation.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ValuationController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations-api/src/Http/Controllers/ValuationController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateValuation $create): JsonResponse`<br>`public function calculateNeuralProperty(Request $request, GenerateNeuralPropertyValuation $generate): JsonResponse`<br>`public function show(Request $request, Valuation $valuation): JsonResponse`<br>`public function update(Request $request, Valuation $valuation, UpdateValuation $update): JsonResponse`<br>`public function destroy(Request $request, Valuation $valuation, DeleteValuation $delete): Response`<br>`public function schedule(Request $request, Valuation $valuation, ScheduleValuation $schedule): JsonResponse`<br>`public function complete(Request $request, Valuation $valuation, CompleteValuation $complete): JsonResponse`<br>`public function convert(Request $request, Valuation $valuation, ConvertValuation $convert): JsonResponse`<br>`public function comparables(Request $request, Valuation $valuation, CalculateComparables $calculate): JsonResponse`<br>`public function calculateHome(Request $request, CalculateHomeValuation $calculate): JsonResponse`<br>`public function calculateProperty(Request $request, GeneratePropertyValuation $calculate): JsonResponse`<br>`public function calculateMortgage(Request $request, CalculateMortgage $calculate): JsonResponse`<br>`public function calculateRentalYield(Request $request, CalculateRentalYield $calculate): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-valuations-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/valuations')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [ValuationController::class, 'index'])->name('real-estate.valuations.index');
Route::post('/', [ValuationController::class, 'store'])->name('real-estate.valuations.store');
Route::post('/calculate-home', [ValuationController::class, 'calculateHome'])->name('real-estate.valuations.calculate-home');
Route::post('/calculate-property', [ValuationController::class, 'calculateProperty'])->name('real-estate.valuations.calculate-property');
Route::post('/calculate-neural-property', [ValuationController::class, 'calculateNeuralProperty'])->name('real-estate.valuations.calculate-neural-property');
Route::post('/calculate-mortgage', [ValuationController::class, 'calculateMortgage'])->name('real-estate.valuations.calculate-mortgage');
Route::post('/calculate-rental-yield', [ValuationController::class, 'calculateRentalYield'])->name('real-estate.valuations.calculate-rental-yield');
Route::get('/{valuation}', [ValuationController::class, 'show'])->name('real-estate.valuations.show');
Route::delete('/{valuation}', [ValuationController::class, 'destroy'])->name('real-estate.valuations.destroy');
Route::post('/{valuation}/schedule', [ValuationController::class, 'schedule'])->name('real-estate.valuations.schedule');
Route::post('/{valuation}/complete', [ValuationController::class, 'complete'])->name('real-estate.valuations.complete');
Route::post('/{valuation}/convert', [ValuationController::class, 'convert'])->name('real-estate.valuations.convert');
Route::post('/{valuation}/comparables', [ValuationController::class, 'comparables'])->name('real-estate.valuations.comparables');
```
<!-- layer-implementation-plan:end -->
