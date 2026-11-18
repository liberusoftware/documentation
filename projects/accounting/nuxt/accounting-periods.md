# Accounting: Accounting Periods Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-periods). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-periods-nuxt`
**Matching domain module:** `accounting-periods`
**Application:** Accounting
**Source feature:** [Accounting Periods](../features/accounting-periods.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-periods.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-periods` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Open/soft-close/hard-close states:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transaction-date controls:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Module dependencies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Locks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reopen approval:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Evidence:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-periods-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `open-soft-close-hard-close-states`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transaction-date-controls`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `module-dependencies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `locks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reopen-approval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `evidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-periods` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-periods.md)) |
| Capability Nuxt module skeleton | [`module-accounting-periods-nuxt`](https://github.com/liberusoftware/module-accounting-periods-nuxt) (`@liberusoftware/module-accounting-periods-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Open/soft-close/hard-close states** | Expose composable and Vue 3 component for `open/soft-close/hard-close states` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-periods.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Transaction-date controls** | Expose composable and Vue 3 component for `transaction-date controls` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-periods.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Module dependencies** | Expose composable and Vue 3 component for `module dependencies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-periods.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Locks** | Expose composable and Vue 3 component for `locks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-periods.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reopen approval** | Expose composable and Vue 3 component for `reopen approval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-periods.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Evidence** | Expose composable and Vue 3 component for `evidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-periods.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Actions/CreatePeriod.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(array $attributes): AccountingPeriod` |
| [LockPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Actions/LockPeriod.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(AccountingPeriod $period, ?string $actor): AccountingPeriod` |
| [TransitionPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Actions/TransitionPeriod.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(AccountingPeriod $period, PeriodState $to, ?string $actor = null, ?string $reason = null): AccountingPeriod` |
| [UnlockPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Actions/UnlockPeriod.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(AccountingPeriod $period, ?string $actor, ?string $reason): AccountingPeriod` |
| [AccountingPeriodsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods-api/src/Policies/AccountingPeriodsPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountingPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods/src/Models/AccountingPeriod.php) | `book_id`, `starts_on`, `ends_on`, `state`, `posting_ends_on`, `locked_by`, `locked_at`, `reopened_by`, `reopen_reason`, `evidence` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AccountingPeriodController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods-api/src/Http/Controllers/AccountingPeriodController.php) | `public function index(Request $request)`<br>`public function show(string $period): AccountingPeriodResource`<br>`public function store(Request $request, CreatePeriod $create)`<br>`public function transition(Request $request, string $period, TransitionPeriod $transition): AccountingPeriodResource`<br>`public function lock(Request $request, string $period, LockPeriod $lock): AccountingPeriodResource`<br>`public function unlock(Request $request, string $period, UnlockPeriod $unlock): AccountingPeriodResource`<br>`public function postingAllowed(Request $request, string $period): JsonResponse`<br>`public function destroy(string $period): Response` |

**Observed route declarations:**

[modules/accounting-periods-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-periods-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/accounting-periods')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('periods', [AccountingPeriodController::class, 'index'])->middleware('ability:accounting.periods.read');
Route::get('periods/{period}', [AccountingPeriodController::class, 'show'])->middleware('ability:accounting.periods.read');
Route::post('periods', [AccountingPeriodController::class, 'store'])->middleware('ability:accounting.periods.write');
Route::post('periods/{period}/transition', [AccountingPeriodController::class, 'transition'])->middleware('ability:accounting.periods.write');
Route::post('periods/{period}/lock', [AccountingPeriodController::class, 'lock'])->middleware('ability:accounting.periods.write');
Route::post('periods/{period}/unlock', [AccountingPeriodController::class, 'unlock'])->middleware('ability:accounting.periods.write');
Route::get('periods/{period}/posting-allowed', [AccountingPeriodController::class, 'postingAllowed'])->middleware('ability:accounting.periods.read');
Route::delete('periods/{period}', [AccountingPeriodController::class, 'destroy'])->middleware('ability:accounting.periods.write');
```
<!-- layer-implementation-plan:end -->
