# Accounting: Accounting Review Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-review). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-review-nuxt`
**Matching domain module:** `accounting-review`
**Application:** Accounting
**Source feature:** [Accounting Review](../features/accounting-review.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-review.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-review` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Uncategorized/unreconciled items:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exceptions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Unusual balances:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Changes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Overdue transactions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Queries:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Resolution:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sign-off:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-review-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `uncategorized-unreconciled-items`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exceptions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `unusual-balances`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `changes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `overdue-transactions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `queries`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `resolution`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sign-off`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-review` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-review.md)) |
| Capability Nuxt module skeleton | [`module-accounting-review-nuxt`](https://github.com/liberusoftware/module-accounting-review-nuxt) (`@liberusoftware/module-accounting-review-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Uncategorized/unreconciled items** | Expose composable and Vue 3 component for `uncategorized/unreconciled items` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-review.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Exceptions** | Expose composable and Vue 3 component for `exceptions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-review.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Unusual balances** | Expose composable and Vue 3 component for `unusual balances` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-review.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Changes** | Expose composable and Vue 3 component for `changes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-review.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Overdue transactions** | Expose composable and Vue 3 component for `overdue transactions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-review.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Queries** | Expose composable and Vue 3 component for `queries` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-review.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Resolution** | Expose composable and Vue 3 component for `resolution` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-review.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Sign-off** | Expose composable and Vue 3 component for `sign-off` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-review.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ReviewItemQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-review/src/Queries/ReviewItemQuery.php) | `public function paginate(int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateReviewItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-review/src/Actions/CreateReviewItem.php) | `public function handle(array $attributes): ReviewItem` |
| [ResolveReviewItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-review/src/Actions/ResolveReviewItem.php) | `public function handle(ReviewItem $item, int $actorId, array $resolution): ReviewItem` |
| [SignOffReviewItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-review/src/Actions/SignOffReviewItem.php) | `public function handle(ReviewItem $item, int $actorId, string $attestation): ReviewItem` |
| [ReviewPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-review-api/src/Policies/ReviewPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function update(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReviewItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-review/src/Models/ReviewItem.php) | `team_id`, `item_type`, `source_type`, `source_id`, `severity`, `status`, `title`, `details`, `resolution`, `resolved_by`, `resolved_at`, `signoff`, `signed_off_by`, `signed_off_at`, `due_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReviewController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-review-api/src/Http/Controllers/ReviewController.php) | `public function index(Request $request, ReviewItemQuery $query): mixed`<br>`public function store(Request $request, CreateReviewItem $action): ReviewItemResource`<br>`public function resolve(Request $request, ReviewItem $item, ResolveReviewItem $action): ReviewItemResource`<br>`public function signOff(Request $request, ReviewItem $item, SignOffReviewItem $action): ReviewItemResource` |

**Observed route declarations:**

[modules/accounting-review-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-review-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/review')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [ReviewController::class, 'index'])->middleware('ability:accounting.review.read');
Route::post('/', [ReviewController::class, 'store'])->middleware('ability:accounting.review.write');
Route::post('/{item}/resolve', [ReviewController::class, 'resolve'])->middleware('ability:accounting.review.write');
Route::post('/{item}/sign-off', [ReviewController::class, 'signOff'])->middleware('ability:accounting.review.write');
```
<!-- layer-implementation-plan:end -->
