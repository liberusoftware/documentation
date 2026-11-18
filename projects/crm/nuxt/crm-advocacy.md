# CRM: Crm Advocacy Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-advocacy). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-advocacy-nuxt`
**Matching domain module:** `crm-advocacy`
**Application:** CRM
**Source feature:** [Crm Advocacy](../features/crm-advocacy.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-advocacy.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-advocacy` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **References:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Testimonials:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reviews:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Case-study consent:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Speakers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Advisory boards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Nominations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Requests:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Recognition history:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-advocacy-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `testimonials`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reviews`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `case-study-consent`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `speakers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `advisory-boards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `nominations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `requests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `recognition-history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-advocacy` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-advocacy.md)) |
| Capability Nuxt module skeleton | [`module-crm-advocacy-nuxt`](https://github.com/liberusoftware/module-crm-advocacy-nuxt) (`@liberusoftware/module-crm-advocacy-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **References** | Expose composable and Vue 3 component for `references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-advocacy.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Testimonials** | Expose composable and Vue 3 component for `testimonials` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-advocacy.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Reviews** | Expose composable and Vue 3 component for `reviews` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-advocacy.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Case-study consent** | Expose composable and Vue 3 component for `case-study consent` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-advocacy.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Speakers** | Expose composable and Vue 3 component for `speakers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-advocacy.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Advisory boards** | Expose composable and Vue 3 component for `advisory boards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-advocacy.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Nominations** | Expose composable and Vue 3 component for `nominations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-advocacy.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Requests** | Expose composable and Vue 3 component for `requests` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-advocacy.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Recognition history** | Expose composable and Vue 3 component for `recognition history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-advocacy.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AdvocacyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy/src/Queries/AdvocacyQuery.php) | `public function records(int $teamId, ?string $kind = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TransitionRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy/src/Actions/TransitionRecord.php) | `public function execute(int $teamId, int $id, string $status): AdvocacyRecord` |
| [UpsertRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy/src/Actions/UpsertRecord.php) | `public function execute(int $teamId, array $attributes, ?int $id = null): AdvocacyRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AdvocacyRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy/src/Models/AdvocacyRecord.php) | `team_id`, `kind`, `name`, `status`, `contact_id`, `owner_id`, `payload`, `requested_at`, `approved_at`, `completed_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AdvocacyController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy-api/src/Http/Controllers/AdvocacyController.php) | `public function __construct(private readonly AdvocacyQuery $query)`<br>`public function index(Request $request): JsonResponse`<br>`public function store(Request $request, UpsertRecord $upsert): JsonResponse`<br>`public function update(Request $request, int $record, UpsertRecord $upsert): JsonResponse`<br>`public function transition(Request $request, int $record, TransitionRecord $transition): JsonResponse` |

**Observed route declarations:**

[modules/crm-advocacy-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/advocacy')->group(function (): void {
Route::get('records', [AdvocacyController::class, 'index']);
Route::post('records', [AdvocacyController::class, 'store']);
Route::patch('records/{record}', [AdvocacyController::class, 'update']);
Route::post('records/{record}/transition', [AdvocacyController::class, 'transition']);
```
<!-- layer-implementation-plan:end -->
