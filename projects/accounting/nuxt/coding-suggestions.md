# Accounting: Coding Suggestions Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#coding-suggestions). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-coding-suggestions-nuxt`
**Matching domain module:** `accounting-coding-suggestions`
**Application:** Accounting
**Source feature:** [Coding Suggestions](../features/coding-suggestions.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/coding-suggestions.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-coding-suggestions` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Account/tax/dimension/payee suggestions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Confidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Explanations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **User feedback:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Policy thresholds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Review:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-coding-suggestions-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `account-tax-dimension-payee-suggestions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `confidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `explanations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `user-feedback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `policy-thresholds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `review`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-coding-suggestions` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/coding-suggestions.md)) |
| Capability Nuxt module skeleton | [`module-accounting-coding-suggestions-nuxt`](https://github.com/liberusoftware/module-accounting-coding-suggestions-nuxt) (`@liberusoftware/module-accounting-coding-suggestions-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Account/tax/dimension/payee suggestions** | Expose composable and Vue 3 component for `account/tax/dimension/payee suggestions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/coding-suggestions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Confidence** | Expose composable and Vue 3 component for `confidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/coding-suggestions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Explanations** | Expose composable and Vue 3 component for `explanations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/coding-suggestions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **User feedback** | Expose composable and Vue 3 component for `user feedback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/coding-suggestions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Policy thresholds** | Expose composable and Vue 3 component for `policy thresholds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/coding-suggestions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Review** | Expose composable and Vue 3 component for `review` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/coding-suggestions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CodingSuggestionQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Queries/CodingSuggestionQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplySuggestionFeedback.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/ApplySuggestionFeedback.php) | `public function handle(CodingSuggestion $suggestion, array $feedback): CodingSuggestion` |
| [CreateCodingSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/CreateCodingSuggestion.php) | `public function handle(array $attributes): CodingSuggestion` |
| [ReviewCodingSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/ReviewCodingSuggestion.php) | `public function handle(CodingSuggestion $suggestion, array $review): CodingSuggestion` |
| [SetSuggestionPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/SetSuggestionPolicy.php) | `public function handle(CodingSuggestion $suggestion, array $policy): CodingSuggestion` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CodingSuggestion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Models/CodingSuggestion.php) | `team_id`, `source_ref`, `target_type`, `target_ref`, `confidence`, `explanation`, `status`, `feedback`, `policy`, `review` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CodingSuggestionsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions-api/src/Http/Controllers/CodingSuggestionsController.php) | `public function index(CodingSuggestionQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCodingSuggestion $action): JsonResponse`<br>`public function feedback(Request $request, string $suggestion, ApplySuggestionFeedback $action): JsonResponse`<br>`public function review(Request $request, string $suggestion, ReviewCodingSuggestion $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-coding-suggestions-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/coding-suggestions')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.coding-suggestions.read')->get('/', [CodingSuggestionsController::class, 'index']);
Route::middleware('ability:accounting.coding-suggestions.write')->group(function (): void {
Route::post('/', [CodingSuggestionsController::class, 'store']);
Route::post('/{suggestion}/feedback', [CodingSuggestionsController::class, 'feedback']);
Route::post('/{suggestion}/review', [CodingSuggestionsController::class, 'review']);
```
<!-- layer-implementation-plan:end -->
