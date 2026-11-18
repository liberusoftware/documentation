# CRM: Account Planning Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#account-planning). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-account-planning-nuxt`
**Matching domain module:** `crm-account-planning`
**Application:** CRM
**Source feature:** [Account Planning](../features/account-planning.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/account-planning.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-account-planning` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Account hierarchies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Stakeholders:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Influence maps:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Whitespace:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Account plans:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Objectives:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Risks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Mutual action plans:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Account-based coordination:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-account-planning-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `account-hierarchies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `stakeholders`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `influence-maps`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `whitespace`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `account-plans`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `objectives`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `risks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `mutual-action-plans`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `account-based-coordination`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-account-planning` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/account-planning.md)) |
| Capability Nuxt module skeleton | [`module-crm-account-planning-nuxt`](https://github.com/liberusoftware/module-crm-account-planning-nuxt) (`@liberusoftware/module-crm-account-planning-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Account hierarchies** | Expose composable and Vue 3 component for `account hierarchies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-planning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Stakeholders** | Expose composable and Vue 3 component for `stakeholders` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-planning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Influence maps** | Expose composable and Vue 3 component for `influence maps` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-planning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Whitespace** | Expose composable and Vue 3 component for `whitespace` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-planning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Account plans** | Expose composable and Vue 3 component for `account plans` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-planning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Objectives** | Expose composable and Vue 3 component for `objectives` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-planning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Risks** | Expose composable and Vue 3 component for `risks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-planning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Mutual action plans** | Expose composable and Vue 3 component for `mutual action plans` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-planning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Account-based coordination** | Expose composable and Vue 3 component for `account-based coordination` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-planning.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AccountPlanningQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning/src/Queries/AccountPlanningQuery.php) | `public function records(int $teamId, ?string $kind = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TransitionRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning/src/Actions/TransitionRecord.php) | `public function execute(int $teamId, int $id, string $status): AccountPlanningRecord` |
| [UpsertRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning/src/Actions/UpsertRecord.php) | `public function execute(int $teamId, array $attributes, ?int $id = null): AccountPlanningRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountPlanningRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning/src/Models/AccountPlanningRecord.php) | `team_id`, `kind`, `name`, `status`, `account_id`, `owner_id`, `payload`, `starts_at`, `ends_at`, `completed_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AccountPlanningController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning-api/src/Http/Controllers/AccountPlanningController.php) | `public function __construct(private readonly AccountPlanningQuery $query)`<br>`public function index(Request $request): JsonResponse`<br>`public function show(int $record): AccountPlanningResource`<br>`public function store(Request $request, UpsertRecord $upsert): JsonResponse`<br>`public function update(Request $request, int $record, UpsertRecord $upsert): JsonResponse`<br>`public function transition(Request $request, int $record, TransitionRecord $transition): JsonResponse`<br>`public function destroy(int $record, TransitionRecord $transition): JsonResponse` |

**Observed route declarations:**

[modules/crm-account-planning-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-account-planning-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/account-planning')->group(function (): void {
Route::get('records', [AccountPlanningController::class, 'index']);
Route::post('records', [AccountPlanningController::class, 'store']);
Route::get('records/{record}', [AccountPlanningController::class, 'show']);
Route::patch('records/{record}', [AccountPlanningController::class, 'update']);
Route::post('records/{record}/transition', [AccountPlanningController::class, 'transition']);
Route::delete('records/{record}', [AccountPlanningController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
