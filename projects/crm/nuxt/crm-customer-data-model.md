# CRM: Crm Customer Data Model Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-customer-data-model). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-customer-data-model-nuxt`
**Matching domain module:** `crm-customer-data-model`
**Application:** CRM
**Source feature:** [Crm Customer Data Model](../features/crm-customer-data-model.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-customer-data-model.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-customer-data-model` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Standard/custom objects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fields:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Relationships:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Layouts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Validation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Calculated fields:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Required-by-stage fields:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Schema versioning:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-customer-data-model-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `standard-custom-objects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fields`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `relationships`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `layouts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `validation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `calculated-fields`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `required-by-stage-fields`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `schema-versioning`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-customer-data-model` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-customer-data-model.md)) |
| Capability Nuxt module skeleton | [`module-crm-customer-data-model-nuxt`](https://github.com/liberusoftware/module-crm-customer-data-model-nuxt) (`@liberusoftware/module-crm-customer-data-model-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Standard/custom objects** | Expose composable and Vue 3 component for `standard/custom objects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-model.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Fields** | Expose composable and Vue 3 component for `fields` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-model.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Relationships** | Expose composable and Vue 3 component for `relationships` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-model.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Layouts** | Expose composable and Vue 3 component for `layouts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-model.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Validation** | Expose composable and Vue 3 component for `validation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-model.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Calculated fields** | Expose composable and Vue 3 component for `calculated fields` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-model.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Required-by-stage fields** | Expose composable and Vue 3 component for `required-by-stage fields` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-model.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Schema versioning** | Expose composable and Vue 3 component for `schema versioning` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-customer-data-model.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateObject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Actions/CreateObject.php) | `public function execute(int $teamId, array $attributes): ObjectDefinition` |
| [PublishSchema.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Actions/PublishSchema.php) | `public function execute(ObjectDefinition $object, ?int $actorId = null): SchemaVersion` |
| [SchemaValidator.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Contracts/SchemaValidator.php) | `public function validate(ObjectDefinition $object, array $values, ?string $stage = null): array` |
| [SchemaValidationService.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Services/SchemaValidationService.php) | `public function validate(ObjectDefinition $object, array $values, ?string $stage = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FieldDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/FieldDefinition.php) | `object_id`, `key`, `label`, `type`, `description`, `config`, `is_required`, `is_calculated`, `calculation`, `required_stages`, `position` |
| [LayoutDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/LayoutDefinition.php) | `object_id`, `key`, `label`, `sections`, `is_default` |
| [ObjectDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/ObjectDefinition.php) | `team_id`, `key`, `label`, `description`, `is_standard`, `status`, `current_version` |
| [RelationshipDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/RelationshipDefinition.php) | `team_id`, `from_object_id`, `to_object_id`, `key`, `label`, `cardinality`, `config` |
| [SchemaVersion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model/src/Models/SchemaVersion.php) | `object_id`, `version`, `status`, `snapshot`, `published_by`, `published_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ObjectDefinitionController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-api/src/Http/Controllers/ObjectDefinitionController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateObject $create): JsonResponse`<br>`public function show(Request $request, int $object): JsonResponse`<br>`public function update(Request $request, int $object): JsonResponse`<br>`public function publish(Request $request, int $object, PublishSchema $publish): JsonResponse` |

**Observed route declarations:**

[modules/crm-customer-data-model-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-model-api/routes/api.php)

```php
Route::prefix('api/v1/crm/customer-data-model')->middleware(['auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [ObjectDefinitionController::class, 'index'])->name('crm.customer.data.model.list');
Route::post('/', [ObjectDefinitionController::class, 'store'])->name('crm.customer.data.model.create');
Route::get('/{object}', [ObjectDefinitionController::class, 'show'])->name('crm.customer.data.model.get');
Route::patch('/{object}', [ObjectDefinitionController::class, 'update'])->name('crm.customer.data.model.update');
Route::post('/{object}/publish', [ObjectDefinitionController::class, 'publish'])->name('crm.customer.data.model.publish');
```
<!-- layer-implementation-plan:end -->
