# CRM: Crm Data Operations Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-data-operations). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-data-operations-nuxt`
**Matching domain module:** `crm-data-operations`
**Application:** CRM
**Source feature:** [Crm Data Operations](../features/crm-data-operations.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-data-operations.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-data-operations` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Imports/exports:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Field mapping:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Normalization:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Enrichment orchestration:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Duplicate detection/merge:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Formatting:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quality rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Schedules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exception queues:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-data-operations-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `imports-exports`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `field-mapping`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `normalization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `enrichment-orchestration`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `duplicate-detection-merge`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `formatting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quality-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `schedules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exception-queues`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-data-operations` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-data-operations.md)) |
| Capability Nuxt module skeleton | [`module-crm-data-operations-nuxt`](https://github.com/liberusoftware/module-crm-data-operations-nuxt) (`@liberusoftware/module-crm-data-operations-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Imports/exports** | Expose composable and Vue 3 component for `imports/exports` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-data-operations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Field mapping** | Expose composable and Vue 3 component for `field mapping` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-data-operations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Normalization** | Expose composable and Vue 3 component for `normalization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-data-operations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Enrichment orchestration** | Expose composable and Vue 3 component for `enrichment orchestration` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-data-operations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Duplicate detection/merge** | Expose composable and Vue 3 component for `duplicate detection/merge` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-data-operations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Formatting** | Expose composable and Vue 3 component for `formatting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-data-operations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Quality rules** | Expose composable and Vue 3 component for `quality rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-data-operations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Schedules** | Expose composable and Vue 3 component for `schedules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-data-operations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Exception queues** | Expose composable and Vue 3 component for `exception queues` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-data-operations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDataOperation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Actions/CreateDataOperation.php) | `public function execute(int $teamId, ?int $actorId, array $attributes, array $mappings = []): DataOperation` |
| [ResolveException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Actions/ResolveException.php) | `public function execute(OperationException $exception, int $actorId): OperationException` |
| [TransitionDataOperation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Actions/TransitionDataOperation.php) | `public function execute(DataOperation $operation, string $status, ?string $reason = null): DataOperation` |
| [DataOperationService.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Services/DataOperationService.php) | `public function mapAndNormalize(array $row, array $mapping): array`<br>`public function duplicateConfidence(array $left, array $right, array $fields): float` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DataOperation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/DataOperation.php) | `team_id`, `actor_id`, `kind`, `status`, `source`, `target`, `options`, `total_rows`, `processed_rows`, `failed_rows`, `failure_reason`, `started_at`, `completed_at` |
| [DuplicateMatch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/DuplicateMatch.php) | `team_id`, `operation_id`, `left_record_id`, `right_record_id`, `confidence`, `status` |
| [FieldMapping.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/FieldMapping.php) | `operation_id`, `source_field`, `target_field`, `transform`, `required` |
| [OperationException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/OperationException.php) | `team_id`, `operation_id`, `row_number`, `payload`, `reason`, `status`, `resolved_by`, `resolved_at` |
| [OperationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/OperationRule.php) | `team_id`, `name`, `kind`, `definition`, `active` |
| [OperationSchedule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/OperationSchedule.php) | `team_id`, `operation_id`, `cron`, `timezone`, `active`, `next_run_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [DataOperationController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations-api/src/Http/Controllers/DataOperationController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateDataOperation $create): JsonResponse`<br>`public function show(Request $request, int $operation): JsonResponse`<br>`public function update(Request $request, int $operation): JsonResponse`<br>`public function transition(Request $request, int $operation, TransitionDataOperation $transition): JsonResponse` |

**Observed route declarations:**

[modules/crm-data-operations-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/data-operations')->group(function (): void {
Route::get('/', [DataOperationController::class, 'index']);
Route::post('/', [DataOperationController::class, 'store']);
Route::get('/{operation}', [DataOperationController::class, 'show']);
Route::patch('/{operation}', [DataOperationController::class, 'update']);
Route::post('/{operation}/transition', [DataOperationController::class, 'transition'])->middleware('throttle:api');
```
<!-- layer-implementation-plan:end -->
