# CRM: Attribution Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#attribution). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-attribution-nuxt`
**Matching domain module:** `crm-attribution`
**Application:** CRM
**Source feature:** [Attribution](../features/attribution.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/attribution.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-attribution` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **First/last/multi-touch models:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Campaign members:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Source normalization:** page/component/composable/API-action behavior for this module's authorized workflow.
- **UTM/click IDs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Offline conversions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Influence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cost allocation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Model comparison:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-attribution-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `first-last-multi-touch-models`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `campaign-members`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `source-normalization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `utm-click-ids`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `offline-conversions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `influence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cost-allocation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `model-comparison`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-attribution` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/attribution.md)) |
| Capability Nuxt module skeleton | [`module-crm-attribution-nuxt`](https://github.com/liberusoftware/module-crm-attribution-nuxt) (`@liberusoftware/module-crm-attribution-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **First/last/multi-touch models** | Expose composable and Vue 3 component for `first/last/multi-touch models` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/attribution.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Campaign members** | Expose composable and Vue 3 component for `campaign members` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/attribution.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Source normalization** | Expose composable and Vue 3 component for `source normalization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/attribution.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **UTM/click IDs** | Expose composable and Vue 3 component for `utm/click ids` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/attribution.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Offline conversions** | Expose composable and Vue 3 component for `offline conversions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/attribution.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Influence** | Expose composable and Vue 3 component for `influence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/attribution.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Cost allocation** | Expose composable and Vue 3 component for `cost allocation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/attribution.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Model comparison** | Expose composable and Vue 3 component for `model comparison` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/attribution.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AttributionQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Queries/AttributionQuery.php) | `public function touchpoints(int $teamId): Builder`<br>`public function conversions(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordConversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Actions/RecordConversion.php) | `public function execute(int $teamId, array $input): Conversion` |
| [RecordTouchpoint.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Actions/RecordTouchpoint.php) | `public function execute(int $teamId, array $input): Touchpoint` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Models/Conversion.php) | No literal fillable array detected; inspect the model and API schema. |
| [Touchpoint.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Models/Touchpoint.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AttributionController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution-api/src/Http/Controllers/AttributionController.php) | `public function __construct(private readonly AttributionQuery $query)`<br>`public function touchpoints(Request $request): JsonResponse`<br>`public function recordTouchpoint(Request $request, RecordTouchpoint $action): JsonResponse`<br>`public function conversions(Request $request): JsonResponse`<br>`public function recordConversion(Request $request, RecordConversion $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-attribution-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/attribution')->group(function (): void {
Route::get('touchpoints', [AttributionController::class, 'touchpoints']);
Route::post('touchpoints', [AttributionController::class, 'recordTouchpoint']);
Route::get('conversions', [AttributionController::class, 'conversions']);
Route::post('conversions', [AttributionController::class, 'recordConversion']);
```
<!-- layer-implementation-plan:end -->
