# CRM: Crm Enrichment Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-enrichment). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-enrichment-nuxt`
**Matching domain module:** `crm-enrichment`
**Application:** CRM
**Source feature:** [Crm Enrichment](../features/crm-enrichment.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-enrichment.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-enrichment` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Company/contact firmographic:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Demographic:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Technographic:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Social:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Verification:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Change monitoring:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Confidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Field-level provenance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provider adapters:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-enrichment-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `company-contact-firmographic`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `demographic`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `technographic`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `social`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `verification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `change-monitoring`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `confidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `field-level-provenance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provider-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-enrichment` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-enrichment.md)) |
| Capability Nuxt module skeleton | [`module-crm-enrichment-nuxt`](https://github.com/liberusoftware/module-crm-enrichment-nuxt) (`@liberusoftware/module-crm-enrichment-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Company/contact firmographic** | Expose composable and Vue 3 component for `company/contact firmographic` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-enrichment.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Demographic** | Expose composable and Vue 3 component for `demographic` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-enrichment.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Technographic** | Expose composable and Vue 3 component for `technographic` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-enrichment.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Social** | Expose composable and Vue 3 component for `social` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-enrichment.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Verification** | Expose composable and Vue 3 component for `verification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-enrichment.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Change monitoring** | Expose composable and Vue 3 component for `change monitoring` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-enrichment.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Confidence** | Expose composable and Vue 3 component for `confidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-enrichment.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Field-level provenance** | Expose composable and Vue 3 component for `field-level provenance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-enrichment.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Provider adapters** | Expose composable and Vue 3 component for `provider adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-enrichment.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EnrichmentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Queries/EnrichmentQuery.php) | `public function profiles(int $teamId)`<br>`public function changes(int $teamId, int $profileId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordChange.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Actions/RecordChange.php) | `public function __construct(private readonly EnrichmentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, EnrichmentProfile $profile, array $input): EnrichmentChange` |
| [RecordProvenance.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Actions/RecordProvenance.php) | `public function __construct(private readonly EnrichmentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, EnrichmentProfile $profile, array $input): EnrichmentField` |
| [UpsertEnrichment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Actions/UpsertEnrichment.php) | `public function __construct(private readonly EnrichmentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EnrichmentProfile` |
| [VerifyProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Actions/VerifyProfile.php) | `public function __construct(private readonly EnrichmentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, EnrichmentProfile $profile, bool $verified): EnrichmentProfile` |
| [EnrichmentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Services/EnrichmentPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EnrichmentChange.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Models/EnrichmentChange.php) | No literal fillable array detected; inspect the model and API schema. |
| [EnrichmentField.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Models/EnrichmentField.php) | No literal fillable array detected; inspect the model and API schema. |
| [EnrichmentProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Models/EnrichmentProfile.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [EnrichmentController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment-api/src/Http/Controllers/EnrichmentController.php) | `public function __construct(private readonly EnrichmentQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(UpsertEnrichment $action): JsonResponse`<br>`public function provenance(EnrichmentProfile $profile, RecordProvenance $action): JsonResponse`<br>`public function change(EnrichmentProfile $profile, RecordChange $action): JsonResponse`<br>`public function verify(EnrichmentProfile $profile, VerifyProfile $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-enrichment-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/enrichment')->group(function (): void {
Route::get('profiles', [EnrichmentController::class, 'index']);
Route::post('profiles', [EnrichmentController::class, 'store']);
Route::post('profiles/{profile}/provenance', [EnrichmentController::class, 'provenance']);
Route::post('profiles/{profile}/changes', [EnrichmentController::class, 'change']);
Route::post('profiles/{profile}/verify', [EnrichmentController::class, 'verify']);
```
<!-- layer-implementation-plan:end -->
