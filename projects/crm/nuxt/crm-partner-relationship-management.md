# CRM: Crm Partner Relationship Management Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-partner-relationship-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-partner-relationship-management-nuxt`
**Matching domain module:** `crm-partner-relationship-management`
**Application:** CRM
**Source feature:** [Crm Partner Relationship Management](../features/crm-partner-relationship-management.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-partner-relationship-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-partner-relationship-management` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Partner accounts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Contacts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tiers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Recruitment:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Onboarding:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Competencies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Agreements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Enablement:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Certification:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Plans:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Performance:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-partner-relationship-management-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `partner-accounts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `contacts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tiers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `recruitment`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `onboarding`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `competencies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `agreements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `enablement`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `certification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `plans`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `performance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-partner-relationship-management` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-partner-relationship-management.md)) |
| Capability Nuxt module skeleton | [`module-crm-partner-relationship-management-nuxt`](https://github.com/liberusoftware/module-crm-partner-relationship-management-nuxt) (`@liberusoftware/module-crm-partner-relationship-management-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Partner accounts** | Expose composable and Vue 3 component for `partner accounts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-partner-relationship-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Contacts** | Expose composable and Vue 3 component for `contacts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-partner-relationship-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Tiers** | Expose composable and Vue 3 component for `tiers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-partner-relationship-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Recruitment** | Expose composable and Vue 3 component for `recruitment` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-partner-relationship-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Onboarding** | Expose composable and Vue 3 component for `onboarding` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-partner-relationship-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Competencies** | Expose composable and Vue 3 component for `competencies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-partner-relationship-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Agreements** | Expose composable and Vue 3 component for `agreements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-partner-relationship-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Enablement** | Expose composable and Vue 3 component for `enablement` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-partner-relationship-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Certification** | Expose composable and Vue 3 component for `certification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-partner-relationship-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Plans** | Expose composable and Vue 3 component for `plans` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-partner-relationship-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Performance** | Expose composable and Vue 3 component for `performance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-partner-relationship-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PartnerQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Queries/PartnerQuery.php) | `public function partners(int $teamId)`<br>`public function contacts(int $teamId)`<br>`public function activities(int $teamId)`<br>`public function performance(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddPartnerContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/AddPartnerContact.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PartnerContact` |
| [ChangePartnerStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/ChangePartnerStatus.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $partnerId, string $status): PartnerAccount` |
| [CreatePartner.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/CreatePartner.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PartnerAccount` |
| [RecordPartnerActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/RecordPartnerActivity.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PartnerActivity` |
| [RecordPartnerPerformance.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Actions/RecordPartnerPerformance.php) | `public function __construct(private readonly PartnerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PartnerPerformance` |
| [PartnerPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Services/PartnerPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PartnerAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Models/PartnerAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartnerActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Models/PartnerActivity.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartnerContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Models/PartnerContact.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartnerPerformance.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management/src/Models/PartnerPerformance.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PartnerRelationshipManagementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management-api/src/Http/Controllers/PartnerRelationshipManagementController.php) | `public function partners(Request $r, PartnerQuery $q)`<br>`public function partner(Request $r, CreatePartner $a)`<br>`public function contact(Request $r, AddPartnerContact $a)`<br>`public function status(Request $r, int $partner, string $status, ChangePartnerStatus $a)`<br>`public function activity(Request $r, RecordPartnerActivity $a)`<br>`public function performance(Request $r, RecordPartnerPerformance $a)` |

**Observed route declarations:**

[modules/crm-partner-relationship-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-partner-relationship-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/partner-relationship-management')->group(function (): void {
Route::get('/partners', [PartnerRelationshipManagementController::class, 'partners']);
Route::post('/partners', [PartnerRelationshipManagementController::class, 'partner']);
Route::post('/contacts', [PartnerRelationshipManagementController::class, 'contact']);
Route::post('/partners/{partner}/{status}', [PartnerRelationshipManagementController::class, 'status'])->whereIn('status', ['prospect', 'onboarding', 'active', 'suspended', 'inactive']);
Route::post('/activities', [PartnerRelationshipManagementController::class, 'activity']);
Route::post('/performance', [PartnerRelationshipManagementController::class, 'performance']);
```
<!-- layer-implementation-plan:end -->
