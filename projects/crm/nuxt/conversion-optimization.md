# CRM: Conversion Optimization Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#conversion-optimization). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-conversion-optimization-nuxt`
**Matching domain module:** `crm-conversion-optimization`
**Application:** CRM
**Source feature:** [Conversion Optimization](../features/conversion-optimization.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/conversion-optimization.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-conversion-optimization` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **A/B and multivariate tests:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Traffic allocation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Goals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Statistical policy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Popups:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Banners:** page/component/composable/API-action behavior for this module's authorized workflow.
- **CTAs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Personalization rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Experiment reporting:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-conversion-optimization-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `a-b-and-multivariate-tests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `traffic-allocation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `goals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `statistical-policy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `popups`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `banners`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ctas`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `personalization-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `experiment-reporting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-conversion-optimization` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/conversion-optimization.md)) |
| Capability Nuxt module skeleton | [`module-crm-conversion-optimization-nuxt`](https://github.com/liberusoftware/module-crm-conversion-optimization-nuxt) (`@liberusoftware/module-crm-conversion-optimization-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **A/B and multivariate tests** | Expose composable and Vue 3 component for `a/b and multivariate tests` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversion-optimization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Traffic allocation** | Expose composable and Vue 3 component for `traffic allocation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversion-optimization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Goals** | Expose composable and Vue 3 component for `goals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversion-optimization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Statistical policy** | Expose composable and Vue 3 component for `statistical policy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversion-optimization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Popups** | Expose composable and Vue 3 component for `popups` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversion-optimization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Banners** | Expose composable and Vue 3 component for `banners` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversion-optimization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **CTAs** | Expose composable and Vue 3 component for `ctas` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversion-optimization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Personalization rules** | Expose composable and Vue 3 component for `personalization rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversion-optimization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Experiment reporting** | Expose composable and Vue 3 component for `experiment reporting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversion-optimization.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ConversionReportQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Queries/ConversionReportQuery.php) | `public function experiments(int $teamId): Builder`<br>`public function report(int $teamId, ConversionExperiment $experiment): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateExperiment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Actions/ActivateExperiment.php) | `public function execute(int $teamId, int $userId, ConversionExperiment $experiment): ConversionExperiment` |
| [CreateConversionExperiment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Actions/CreateConversionExperiment.php) | `public function execute(int $teamId, int $userId, array $input): ConversionExperiment` |
| [RecordConversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Actions/RecordConversion.php) | `public function execute(int $teamId, ConversionExperiment $experiment, string $subjectKey, string $variant, string $event, float $value = 1): ConversionObservation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConversionExperiment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Models/ConversionExperiment.php) | No literal fillable array detected; inspect the model and API schema. |
| [ConversionObservation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Models/ConversionObservation.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConversionOptimizationController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization-api/src/Http/Controllers/ConversionOptimizationController.php) | `public function __construct(private readonly ConversionReportQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateConversionExperiment $a): JsonResponse`<br>`public function activate(ConversionExperiment $e, ActivateExperiment $a): JsonResponse`<br>`public function convert(ConversionExperiment $e, RecordConversion $a): JsonResponse`<br>`public function report(ConversionExperiment $e): JsonResponse` |

**Observed route declarations:**

[modules/crm-conversion-optimization-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/conversion-optimization')->group(function (): void {
Route::get('experiments', [ConversionOptimizationController::class, 'index']);
Route::post('experiments', [ConversionOptimizationController::class, 'store']);
Route::post('experiments/{experiment}/activate', [ConversionOptimizationController::class, 'activate']);
Route::post('experiments/{experiment}/conversions', [ConversionOptimizationController::class, 'convert']);
Route::get('experiments/{experiment}/report', [ConversionOptimizationController::class, 'report']);
```
<!-- layer-implementation-plan:end -->
