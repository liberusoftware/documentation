# Accounting: Accounting Copilot Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-copilot). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-copilot-nuxt`
**Matching domain module:** `accounting-copilot`
**Application:** Accounting
**Source feature:** [Accounting Copilot](../features/accounting-copilot.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-copilot.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-copilot` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Permission-bounded search:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Explanations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Summaries:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Report narratives:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Draft transactions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Explicit action confirmation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-copilot-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `permission-bounded-search`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `explanations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `summaries`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `report-narratives`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `draft-transactions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `explicit-action-confirmation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-copilot` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-copilot.md)) |
| Capability Nuxt module skeleton | [`module-accounting-copilot-nuxt`](https://github.com/liberusoftware/module-accounting-copilot-nuxt) (`@liberusoftware/module-accounting-copilot-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Permission-bounded search** | Expose composable and Vue 3 component for `permission-bounded search` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-copilot.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Explanations** | Expose composable and Vue 3 component for `explanations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-copilot.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Summaries** | Expose composable and Vue 3 component for `summaries` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-copilot.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Report narratives** | Expose composable and Vue 3 component for `report narratives` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-copilot.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Draft transactions** | Expose composable and Vue 3 component for `draft transactions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-copilot.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Explicit action confirmation** | Expose composable and Vue 3 component for `explicit action confirmation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-copilot.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CopilotRequestQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-copilot/src/Queries/CopilotRequestQuery.php) | `public function forTeam(int $teamId, ?string $kind = null): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfirmCopilotRequest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-copilot/src/Actions/ConfirmCopilotRequest.php) | `public function handle(CopilotRequest $request, string $confirmationKey): CopilotRequest` |
| [CreateCopilotRequest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-copilot/src/Actions/CreateCopilotRequest.php) | `public function handle(array $attributes): CopilotRequest` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CopilotRequest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-copilot/src/Models/CopilotRequest.php) | `team_id`, `actor_id`, `kind`, `prompt`, `result`, `status`, `confirmation_key`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CopilotRequestController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-copilot-api/src/Http/Controllers/CopilotRequestController.php) | `public function index(Request $request, CopilotRequestQuery $query): mixed`<br>`public function store(Request $request, CreateCopilotRequest $action): mixed`<br>`public function confirm(Request $request, string $requestId, ConfirmCopilotRequest $action): mixed` |

**Observed route declarations:**

[modules/accounting-copilot-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-copilot-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/copilot')->middleware(['auth:sanctum', 'throttle:30,1'])->group(function (): void {
Route::get('/requests', [CopilotRequestController::class, 'index'])->middleware('ability:accounting.copilot.read');
Route::post('/requests', [CopilotRequestController::class, 'store'])->middleware('ability:accounting.copilot.write');
Route::post('/requests/{request}/confirm', [CopilotRequestController::class, 'confirm'])->middleware('ability:accounting.copilot.write');
```
<!-- layer-implementation-plan:end -->
