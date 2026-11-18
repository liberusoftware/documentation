# CRM: Crm Cpq Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-cpq). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-cpq-nuxt`
**Matching domain module:** `crm-cpq`
**Application:** CRM
**Source feature:** [Crm Cpq](../features/crm-cpq.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-cpq.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-cpq` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Guided configuration:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Compatibility rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Price books:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tiers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Discounts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approvals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Margin guardrails:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Amendments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Renewals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Authoritative pricing adapters:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-cpq-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `guided-configuration`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `compatibility-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `price-books`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tiers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `discounts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approvals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `margin-guardrails`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `amendments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `renewals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `authoritative-pricing-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-cpq` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-cpq.md)) |
| Capability Nuxt module skeleton | [`module-crm-cpq-nuxt`](https://github.com/liberusoftware/module-crm-cpq-nuxt) (`@liberusoftware/module-crm-cpq-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Guided configuration** | Expose composable and Vue 3 component for `guided configuration` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-cpq.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Compatibility rules** | Expose composable and Vue 3 component for `compatibility rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-cpq.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Price books** | Expose composable and Vue 3 component for `price books` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-cpq.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Tiers** | Expose composable and Vue 3 component for `tiers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-cpq.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Discounts** | Expose composable and Vue 3 component for `discounts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-cpq.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Approvals** | Expose composable and Vue 3 component for `approvals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-cpq.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Margin guardrails** | Expose composable and Vue 3 component for `margin guardrails` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-cpq.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Amendments** | Expose composable and Vue 3 component for `amendments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-cpq.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Renewals** | Expose composable and Vue 3 component for `renewals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-cpq.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Authoritative pricing adapters** | Expose composable and Vue 3 component for `authoritative pricing adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-cpq.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CpqQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-cpq/src/Queries/CpqQuery.php) | `public function quotes(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PriceQuote.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-cpq/src/Actions/PriceQuote.php) | `public function execute(int $teamId, int $userId, array $input): CpqQuote` |
| [SubmitQuote.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-cpq/src/Actions/SubmitQuote.php) | `public function execute(int $teamId, int $userId, CpqQuote $quote): CpqApproval` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CpqApproval.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-cpq/src/Models/CpqApproval.php) | No literal fillable array detected; inspect the model and API schema. |
| [CpqQuote.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-cpq/src/Models/CpqQuote.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CpqController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-cpq-api/src/Http/Controllers/CpqController.php) | `public function __construct(private readonly CpqQuery $query)`<br>`public function index(Request $request): JsonResponse`<br>`public function show(int $quote): CpqQuoteResource`<br>`public function store(PriceQuote $action): JsonResponse`<br>`public function submit(int $quote, SubmitQuote $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-cpq-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-cpq-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/cpq')->group(function (): void {
Route::get('quotes', [CpqController::class, 'index']);
Route::post('quotes', [CpqController::class, 'store']);
Route::get('quotes/{quote}', [CpqController::class, 'show']);
Route::post('quotes/{quote}/submit', [CpqController::class, 'submit']);
```
<!-- layer-implementation-plan:end -->
