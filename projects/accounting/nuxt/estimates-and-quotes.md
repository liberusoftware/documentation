# Accounting: Estimates and Quotes Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#estimates-and-quotes). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-estimates-and-quotes-nuxt`
**Matching domain module:** `accounting-estimates-and-quotes`
**Application:** Accounting
**Source feature:** [Estimates and Quotes](../features/estimates-and-quotes.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/estimates-and-quotes.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-estimates-and-quotes` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Branded estimates/quotes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Items:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Terms:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Versions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delivery:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Acceptance/decline:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Expiry:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Conversion:** page/component/composable/API-action behavior for this module's authorized workflow.
- **History:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-estimates-and-quotes-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `branded-estimates-quotes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `items`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `terms`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `versions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delivery`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `acceptance-decline`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `expiry`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `conversion`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-estimates-and-quotes` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/estimates-and-quotes.md)) |
| Capability Nuxt module skeleton | [`module-accounting-estimates-and-quotes-nuxt`](https://github.com/liberusoftware/module-accounting-estimates-and-quotes-nuxt) (`@liberusoftware/module-accounting-estimates-and-quotes-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Branded estimates/quotes** | Expose composable and Vue 3 component for `branded estimates/quotes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/estimates-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Items** | Expose composable and Vue 3 component for `items` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/estimates-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Terms** | Expose composable and Vue 3 component for `terms` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/estimates-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Versions** | Expose composable and Vue 3 component for `versions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/estimates-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Delivery** | Expose composable and Vue 3 component for `delivery` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/estimates-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Acceptance/decline** | Expose composable and Vue 3 component for `acceptance/decline` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/estimates-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Expiry** | Expose composable and Vue 3 component for `expiry` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/estimates-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Conversion** | Expose composable and Vue 3 component for `conversion` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/estimates-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **History** | Expose composable and Vue 3 component for `history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/estimates-and-quotes.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EstimateQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Queries/EstimateQuery.php) | `public function paginate(?int $legalEntityId = null, ?EstimateStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function total(Estimate $e): float` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddEstimateItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/AddEstimateItem.php) | `public function handle(Estimate $e, array $a): EstimateItem` |
| [ConvertEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/ConvertEstimate.php) | `public function handle(Estimate $e, string $convertedRef, ?string $actor = null): Estimate` |
| [CreateEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/CreateEstimate.php) | `public function handle(array $a): Estimate` |
| [DecideEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/DecideEstimate.php) | `public function handle(Estimate $e, bool $accepted, ?string $reason = null, ?string $actor = null): Estimate` |
| [ExpireEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/ExpireEstimate.php) | `public function handle(Estimate $e, ?string $actor = null): Estimate` |
| [SendEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/SendEstimate.php) | `public function handle(Estimate $e, ?string $actor = null): Estimate` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Estimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/Estimate.php) | `legal_entity_id`, `customer_ref`, `quote_ref`, `name`, `currency`, `status`, `issue_date`, `expires_on`, `version`, `terms`, `brand`, `accepted_at`, `declined_reason`, `converted_ref`, `metadata` |
| [EstimateHistory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateHistory.php) | `estimate_id`, `event`, `actor_ref`, `metadata` |
| [EstimateItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateItem.php) | `estimate_id`, `item_ref`, `description`, `quantity`, `unit_price`, `tax_rate`, `amount`, `metadata` |
| [EstimateVersion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateVersion.php) | `estimate_id`, `version`, `snapshot`, `created_by` |

| Observed API controller | Handler signatures |
| --- | --- |
| [EstimatesController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes-api/src/Http/Controllers/EstimatesController.php) | `public function __construct(private readonly EstimateQuery $query)`<br>`public function index(Request $r): mixed`<br>`public function store(Request $r, CreateEstimate $a): EstimateResource`<br>`public function show(Estimate $e): EstimateResource`<br>`public function item(Request $r, Estimate $e, AddEstimateItem $a): EstimateResource`<br>`public function send(Request $r, Estimate $e, SendEstimate $a): EstimateResource`<br>`public function decide(Request $r, Estimate $e, DecideEstimate $a): EstimateResource`<br>`public function expire(Request $r, Estimate $e, ExpireEstimate $a): EstimateResource`<br>`public function convert(Request $r, Estimate $e, ConvertEstimate $a): EstimateResource` |

**Observed route declarations:**

[modules/accounting-estimates-and-quotes-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/estimates-and-quotes')->group(function (): void {
Route::middleware('ability:accounting.estimates-and-quotes.read')->group(function (): void {
Route::get('/', [EstimatesController::class, 'index']);
Route::get('/{estimate}', [EstimatesController::class, 'show']);
Route::middleware('ability:accounting.estimates-and-quotes.write')->group(function (): void {
Route::post('/', [EstimatesController::class, 'store']);
Route::post('/{estimate}/items', [EstimatesController::class, 'item']);
Route::post('/{estimate}/send', [EstimatesController::class, 'send']);
Route::post('/{estimate}/decide', [EstimatesController::class, 'decide']);
Route::post('/{estimate}/expire', [EstimatesController::class, 'expire']);
Route::post('/{estimate}/convert', [EstimatesController::class, 'convert']);
```
<!-- layer-implementation-plan:end -->
