# Real Estate: Lettings Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#lettings). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-real-estate-lettings-nuxt`
**Matching domain module:** `real-estate-lettings`
**Application:** Real Estate
**Source feature:** [Lettings](../features/lettings.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/lettings.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `real-estate-lettings` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Applications:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Referencing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deposits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Agreements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Move-in/out:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Renewals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rent changes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Notices:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-real-estate-lettings-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `applications`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `referencing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deposits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `agreements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `move-in-out`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `renewals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rent-changes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `notices`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-lettings` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-real-estate-nuxt-vue`](https://github.com/liberusoftware/project-real-estate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/lettings.md)) |
| Capability Nuxt module skeleton | [`module-real-estate-lettings-nuxt`](https://github.com/liberusoftware/module-real-estate-lettings-nuxt) (`@liberusoftware/module-real-estate-lettings-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Applications** | Expose composable and Vue 3 component for `applications` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/lettings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Referencing** | Expose composable and Vue 3 component for `referencing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/lettings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Deposits** | Expose composable and Vue 3 component for `deposits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/lettings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Agreements** | Expose composable and Vue 3 component for `agreements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/lettings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Move-in/out** | Expose composable and Vue 3 component for `move-in/out` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/lettings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Renewals** | Expose composable and Vue 3 component for `renewals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/lettings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Rent changes** | Expose composable and Vue 3 component for `rent changes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/lettings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Notices** | Expose composable and Vue 3 component for `notices` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/lettings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListLettings.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Queries/ListLettings.php) | `public function handle(int\|string $teamId, ?string $capability = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [LettingPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Policies/LettingPolicy.php) | `public function view($user, Letting $letting): bool`<br>`public function update($user, Letting $letting): bool`<br>`public function delete($user, Letting $letting): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [LeaseAgreement.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/LeaseAgreement.php) | No literal fillable array detected; inspect the model and API schema. |
| [Letting.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/Letting.php) | No literal fillable array detected; inspect the model and API schema. |
| [RentalApplication.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/RentalApplication.php) | No literal fillable array detected; inspect the model and API schema. |
| [RentalCharge.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/RentalCharge.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [LeaseAgreementController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-api/src/Http/Controllers/LeaseAgreementController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateLeaseAgreement $create): JsonResponse`<br>`public function show(Request $request, LeaseAgreement $tenancyAgreement): JsonResponse`<br>`public function update(Request $request, LeaseAgreement $tenancyAgreement): JsonResponse`<br>`public function renew(Request $request, LeaseAgreement $tenancyAgreement, RenewLeaseAgreement $renew): JsonResponse`<br>`public function notice(Request $request, LeaseAgreement $tenancyAgreement, ServeLeaseNotice $notice): JsonResponse` |
| [LettingController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-api/src/Http/Controllers/LettingController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateLetting $create): JsonResponse`<br>`public function show(Request $request, Letting $letting): JsonResponse`<br>`public function update(Request $request, Letting $letting, TransitionLetting $transition): JsonResponse`<br>`public function updateDetails(Request $request, Letting $letting, UpdateLettingDetails $update): JsonResponse`<br>`public function recordFailure(Request $request, Letting $letting, RecordLettingFailure $failure): JsonResponse` |
| [RentalApplicationController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-api/src/Http/Controllers/RentalApplicationController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateRentalApplication $create): JsonResponse`<br>`public function show(Request $request, RentalApplication $rentalApplication): JsonResponse`<br>`public function update(Request $request, RentalApplication $rentalApplication, UpdateRentalApplicationScreening $update): JsonResponse`<br>`public function screening(Request $request, RentalApplication $rentalApplication, UpdateRentalApplicationScreening $update): JsonResponse`<br>`public function decide(Request $request, RentalApplication $rentalApplication, DecideRentalApplication $decide): JsonResponse` |
| [RentalChargeController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-api/src/Http/Controllers/RentalChargeController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateRentalCharge $create): JsonResponse`<br>`public function show(Request $request, RentalCharge $rentalCharge): JsonResponse`<br>`public function update(Request $request, RentalCharge $rentalCharge, UpdateRentalCharge $update): JsonResponse`<br>`public function destroy(Request $request, RentalCharge $rentalCharge): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-lettings-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/lettings')->group(function (): void {
Route::get('/', [LettingController::class, 'index']);
Route::post('/', [LettingController::class, 'store']);
Route::get('/{letting}', [LettingController::class, 'show']);
Route::patch('/{letting}', [LettingController::class, 'update']);
Route::patch('/{letting}/details', [LettingController::class, 'updateDetails']);
Route::post('/{letting}/failure', [LettingController::class, 'recordFailure']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/rental-charges')->group(function (): void {
Route::get('/', [RentalChargeController::class, 'index']);
Route::post('/', [RentalChargeController::class, 'store']);
Route::get('/{rentalCharge}', [RentalChargeController::class, 'show']);
Route::patch('/{rentalCharge}', [RentalChargeController::class, 'update']);
Route::delete('/{rentalCharge}', [RentalChargeController::class, 'destroy']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/tenancy-agreements')->group(function (): void {
Route::get('/', [LeaseAgreementController::class, 'index']);
Route::post('/', [LeaseAgreementController::class, 'store']);
Route::get('/{tenancyAgreement}', [LeaseAgreementController::class, 'show']);
Route::patch('/{tenancyAgreement}', [LeaseAgreementController::class, 'update']);
Route::post('/{tenancyAgreement}/renew', [LeaseAgreementController::class, 'renew']);
Route::post('/{tenancyAgreement}/notice', [LeaseAgreementController::class, 'notice']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/rental-applications')->group(function (): void {
Route::get('/', [RentalApplicationController::class, 'index']);
Route::post('/', [RentalApplicationController::class, 'store']);
Route::get('/{rentalApplication}', [RentalApplicationController::class, 'show']);
Route::patch('/{rentalApplication}', [RentalApplicationController::class, 'update']);
Route::patch('/{rentalApplication}/screening', [RentalApplicationController::class, 'screening']);
Route::post('/{rentalApplication}/decision', [RentalApplicationController::class, 'decide']);
```
<!-- layer-implementation-plan:end -->
