# Real Estate: Real Estate Lettings Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-lettings). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-real-estate-real-estate-lettings-vue-inertia`
**Matching domain module:** `real-estate-lettings`
**Application:** Real Estate
**Source feature:** [Real Estate Lettings](../features/real-estate-lettings.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/real-estate-lettings.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Applications:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Referencing:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Deposits:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Agreements:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Move-in/out:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Renewals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rent changes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Notices:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-real-estate-real-estate-lettings-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `applications`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `referencing`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `deposits`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `agreements`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `move-in-out`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `renewals`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `rent-changes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `notices`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-lettings` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-real-estate-laravel-inertia-vue`](https://github.com/liberusoftware/project-real-estate-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-real-estate-lettings-vue-inertia`](https://github.com/liberusoftware/module-real-estate-lettings-vue-inertia) (`@liberusoftware/module-real-estate-lettings-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/real-estate-lettings.md) · [Core plan](../core/real-estate-lettings.md) · [API plan](../api/real-estate-lettings.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Applications** | Render `applications` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Referencing** | Render `referencing` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Deposits** | Render `deposits` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Agreements** | Render `agreements` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Move-in/out** | Render `move-in/out` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Renewals** | Render `renewals` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Rent changes** | Render `rent changes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Notices** | Render `notices` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
