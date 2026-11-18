# CRM: Crm Customer Data Platform Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-customer-data-platform). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-customer-data-platform-nuxt`
**Matching domain module:** `crm-customer-data-platform`
**Application:** CRM
**Source feature:** [Crm Customer Data Platform](../features/crm-customer-data-platform.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-customer-data-platform.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-customer-data-platform` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Source profiles:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Identity resolution:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Unified profiles:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Audience activation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Event ingestion:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Consent-aware calculated attributes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Profile lineage:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-customer-data-platform-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `source-profiles`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `identity-resolution`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `unified-profiles`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `audience-activation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `event-ingestion`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `consent-aware-calculated-attributes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `profile-lineage`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-customer-data-platform` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-customer-data-platform.md)) |
| Capability Nuxt module skeleton | [`module-crm-customer-data-platform-nuxt`](https://github.com/liberusoftware/module-crm-customer-data-platform-nuxt) (`@liberusoftware/module-crm-customer-data-platform-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Source profiles** | Expose composable and Vue 3 component for `source profiles` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-platform.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Identity resolution** | Expose composable and Vue 3 component for `identity resolution` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-platform.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Unified profiles** | Expose composable and Vue 3 component for `unified profiles` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-platform.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Audience activation** | Expose composable and Vue 3 component for `audience activation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-platform.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Event ingestion** | Expose composable and Vue 3 component for `event ingestion` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-platform.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Consent-aware calculated attributes** | Expose composable and Vue 3 component for `consent-aware calculated attributes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-platform.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Profile lineage** | Expose composable and Vue 3 component for `profile lineage` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-platform.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CdpQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Queries/CdpQuery.php) | `public function profiles(int $teamId)`<br>`public function audiences(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateCdpAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/ActivateCdpAudience.php) | `public function __construct(private readonly CdpPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CdpAudience $audience, string $destination): CdpAudience` |
| [CreateCdpAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/CreateCdpAudience.php) | `public function __construct(private readonly CdpPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CdpAudience` |
| [IngestCdpEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/IngestCdpEvent.php) | `public function execute(int $teamId, CdpProfile $profile, array $input): CdpEvent` |
| [UpsertCdpProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/UpsertCdpProfile.php) | `public function __construct(private readonly CdpPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CdpProfile` |
| [CdpPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Services/CdpPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CdpAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpAudience.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpIdentity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpIdentity.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpProfile.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CdpController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform-api/src/Http/Controllers/CdpController.php) | `public function __construct(private readonly CdpQuery $query)`<br>`public function profiles(): JsonResponse`<br>`public function storeProfile(UpsertCdpProfile $action): JsonResponse`<br>`public function event(CdpProfile $profile, IngestCdpEvent $action): JsonResponse`<br>`public function audiences(): JsonResponse`<br>`public function storeAudience(CreateCdpAudience $action): JsonResponse`<br>`public function activate(CdpAudience $audience, ActivateCdpAudience $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-customer-data-platform-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/customer-data-platform')->group(function (): void {
Route::get('profiles', [CdpController::class, 'profiles']);
Route::post('profiles', [CdpController::class, 'storeProfile']);
Route::post('profiles/{profile}/events', [CdpController::class, 'event']);
Route::get('audiences', [CdpController::class, 'audiences']);
Route::post('audiences', [CdpController::class, 'storeAudience']);
Route::post('audiences/{audience}/activate', [CdpController::class, 'activate']);
```
<!-- layer-implementation-plan:end -->
