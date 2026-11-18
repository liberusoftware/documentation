# CRM: Territories and Ownership Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#territories-and-ownership). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-territories-and-ownership-nuxt`
**Matching domain module:** `crm-territories-and-ownership`
**Application:** CRM
**Source feature:** [Territories and Ownership](../features/territories-and-ownership.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/territories-and-ownership.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-territories-and-ownership` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Territories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Books of business:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Teams:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Queues:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Assignment rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Round-robin/capacity routing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Temporary coverage:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Ownership history:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-territories-and-ownership-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `territories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `books-of-business`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `teams`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `queues`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `assignment-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `round-robin-capacity-routing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `temporary-coverage`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ownership-history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-territories-and-ownership` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/territories-and-ownership.md)) |
| Capability Nuxt module skeleton | [`module-crm-territories-and-ownership-nuxt`](https://github.com/liberusoftware/module-crm-territories-and-ownership-nuxt) (`@liberusoftware/module-crm-territories-and-ownership-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Territories** | Expose composable and Vue 3 component for `territories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/territories-and-ownership.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Books of business** | Expose composable and Vue 3 component for `books of business` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/territories-and-ownership.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Teams** | Expose composable and Vue 3 component for `teams` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/territories-and-ownership.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Queues** | Expose composable and Vue 3 component for `queues` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/territories-and-ownership.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Assignment rules** | Expose composable and Vue 3 component for `assignment rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/territories-and-ownership.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Round-robin/capacity routing** | Expose composable and Vue 3 component for `round-robin/capacity routing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/territories-and-ownership.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Temporary coverage** | Expose composable and Vue 3 component for `temporary coverage` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/territories-and-ownership.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Ownership history** | Expose composable and Vue 3 component for `ownership history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/territories-and-ownership.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TerritoryQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Queries/TerritoryQuery.php) | `public function rules(int $teamId): LengthAwarePaginator`<br>`public function history(int $teamId): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AssignOwner.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Actions/AssignOwner.php) | `public function execute(int $teamId, int $actorId, string $subjectType, int $subjectId, ?int $previousOwnerId, int $ownerId, string $reason): OwnershipHistory` |
| [CreateCoverage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Actions/CreateCoverage.php) | `public function execute(int $teamId, int $actorId, array $data): TerritoryCoverage` |
| [UpsertTerritoryRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Actions/UpsertTerritoryRule.php) | `public function execute(int $teamId, int $actorId, array $data): TerritoryRule` |
| [TerritoryPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Services/TerritoryPolicy.php) | `public function canManage(int $teamId, int $userId): bool`<br>`public function isTeamMember(int $teamId, int $userId, array $roles = [], bool $includeOwner = false): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [OwnershipHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Models/OwnershipHistory.php) | `team_id`, `subject_type`, `subject_id`, `previous_owner_id`, `owner_id`, `reason`, `actor_id` |
| [TerritoryCoverage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Models/TerritoryCoverage.php) | `team_id`, `rule_id`, `covered_user_id`, `substitute_user_id`, `starts_at`, `ends_at` |
| [TerritoryRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership/src/Models/TerritoryRule.php) | `team_id`, `name`, `book_of_business`, `criteria`, `members`, `capacity`, `round_robin_cursor`, `active` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TerritoryController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership-api/src/Http/Controllers/TerritoryController.php) | `public function index(Request $r, TerritoryQuery $q): JsonResponse`<br>`public function history(Request $r, TerritoryQuery $q): JsonResponse`<br>`public function store(Request $r, UpsertTerritoryRule $a): JsonResponse`<br>`public function assign(Request $r, AssignOwner $a): JsonResponse`<br>`public function coverage(Request $r, CreateCoverage $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-territories-and-ownership-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-territories-and-ownership-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/territories-and-ownership')->group(function () {
Route::get('/rules', [TerritoryController::class, 'index']);
Route::post('/rules', [TerritoryController::class, 'store']);
Route::post('/ownership', [TerritoryController::class, 'assign']);
Route::post('/coverage', [TerritoryController::class, 'coverage']);
Route::get('/history', [TerritoryController::class, 'history']);
```
<!-- layer-implementation-plan:end -->
