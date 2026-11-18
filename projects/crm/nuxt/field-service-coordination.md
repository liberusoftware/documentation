# CRM: Field Service Coordination Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#field-service-coordination). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-field-service-coordination-nuxt`
**Matching domain module:** `crm-field-service-coordination`
**Application:** CRM
**Source feature:** [Field Service Coordination](../features/field-service-coordination.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/field-service-coordination.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-field-service-coordination` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Work types:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Service appointments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dispatch references:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Technician/contractor visibility:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Asset/service history:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Maintenance module handoff:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-field-service-coordination-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `work-types`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `service-appointments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dispatch-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `technician-contractor-visibility`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `asset-service-history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `maintenance-module-handoff`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-field-service-coordination` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/field-service-coordination.md)) |
| Capability Nuxt module skeleton | [`module-crm-field-service-coordination-nuxt`](https://github.com/liberusoftware/module-crm-field-service-coordination-nuxt) (`@liberusoftware/module-crm-field-service-coordination-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Work types** | Expose composable and Vue 3 component for `work types` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/field-service-coordination.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Service appointments** | Expose composable and Vue 3 component for `service appointments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/field-service-coordination.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Dispatch references** | Expose composable and Vue 3 component for `dispatch references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/field-service-coordination.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Technician/contractor visibility** | Expose composable and Vue 3 component for `technician/contractor visibility` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/field-service-coordination.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Asset/service history** | Expose composable and Vue 3 component for `asset/service history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/field-service-coordination.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Maintenance module handoff** | Expose composable and Vue 3 component for `maintenance module handoff` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/field-service-coordination.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [FieldServiceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Queries/FieldServiceQuery.php) | `public function workTypes(int $teamId)`<br>`public function appointments(int $teamId)`<br>`public function assets(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateWorkType.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/CreateWorkType.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): WorkType` |
| [HandOffMaintenance.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/HandOffMaintenance.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, ServiceAppointment $appointment, array $input): MaintenanceHandoff` |
| [RecordServiceHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/RecordServiceHistory.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, ServiceAppointment $appointment, array $input): ServiceHistory` |
| [ScheduleAppointment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/ScheduleAppointment.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ServiceAppointment` |
| [FieldServicePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Services/FieldServicePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MaintenanceHandoff.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/MaintenanceHandoff.php) | No literal fillable array detected; inspect the model and API schema. |
| [ServiceAppointment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/ServiceAppointment.php) | No literal fillable array detected; inspect the model and API schema. |
| [ServiceAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/ServiceAsset.php) | No literal fillable array detected; inspect the model and API schema. |
| [ServiceHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/ServiceHistory.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkType.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/WorkType.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [FieldServiceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination-api/src/Http/Controllers/FieldServiceController.php) | `public function __construct(private readonly FieldServiceQuery $query)`<br>`public function workTypes(): JsonResponse`<br>`public function appointments(): JsonResponse`<br>`public function storeWorkType(CreateWorkType $action): JsonResponse`<br>`public function schedule(ScheduleAppointment $action): JsonResponse`<br>`public function history(ServiceAppointment $appointment, RecordServiceHistory $action): JsonResponse`<br>`public function handoff(ServiceAppointment $appointment, HandOffMaintenance $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-field-service-coordination-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/field-service-coordination')->group(function (): void {
Route::get('work-types', [FieldServiceController::class, 'workTypes']);
Route::get('appointments', [FieldServiceController::class, 'appointments']);
Route::post('work-types', [FieldServiceController::class, 'storeWorkType']);
Route::post('appointments', [FieldServiceController::class, 'schedule']);
Route::post('appointments/{appointment}/history', [FieldServiceController::class, 'history']);
Route::post('appointments/{appointment}/maintenance-handoff', [FieldServiceController::class, 'handoff']);
```
<!-- layer-implementation-plan:end -->
