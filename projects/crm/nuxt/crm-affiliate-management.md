# CRM: Crm Affiliate Management Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-affiliate-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-affiliate-management-nuxt`
**Matching domain module:** `crm-affiliate-management`
**Application:** CRM
**Source feature:** [Crm Affiliate Management](../features/crm-affiliate-management.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-affiliate-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-affiliate-management` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Affiliates and partner profiles:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Applications and onboarding approval:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Links, campaigns, and clicks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Conversions and commission rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payout approvals/exports, disputes, assets, and portal:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-affiliate-management-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `affiliates-and-partner-profiles`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `applications-and-onboarding-approval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `links-campaigns-and-clicks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `conversions-and-commission-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payout-approvals-exports-disputes-assets-and-portal`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-affiliate-management` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-affiliate-management.md)) |
| Capability Nuxt module skeleton | [`module-crm-affiliate-management-nuxt`](https://github.com/liberusoftware/module-crm-affiliate-management-nuxt) (`@liberusoftware/module-crm-affiliate-management-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Affiliates and partner profiles** | Expose composable and Vue 3 component for `affiliates and partner profiles` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-affiliate-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Applications and onboarding approval** | Expose composable and Vue 3 component for `applications and onboarding approval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-affiliate-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Links, campaigns, and clicks** | Expose composable and Vue 3 component for `links, campaigns, and clicks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-affiliate-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Conversions and commission rules** | Expose composable and Vue 3 component for `conversions and commission rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-affiliate-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Payout approvals/exports, disputes, assets, and portal** | Expose composable and Vue 3 component for `payout approvals/exports, disputes, assets, and portal` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-affiliate-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AffiliateQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Queries/AffiliateQuery.php) | `public function affiliates(int $teamId): Builder`<br>`public function events(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplyAffiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApplyAffiliate.php) | `public function execute(int $teamId, array $input): Affiliate` |
| [ApproveAffiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApproveAffiliate.php) | `public function execute(int $teamId, Affiliate $affiliate): Affiliate` |
| [ApproveAffiliatePayout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/ApproveAffiliatePayout.php) | `public function execute(int $teamId, int $actorId, AffiliatePayout $payout): AffiliatePayout` |
| [CreateAffiliateLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/CreateAffiliateLink.php) | `public function execute(int $teamId, Affiliate $affiliate, array $input): AffiliateLink` |
| [RecordAffiliateEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Actions/RecordAffiliateEvent.php) | `public function execute(int $teamId, AffiliateLink $link, array $input): AffiliateEvent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Affiliate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/Affiliate.php) | No literal fillable array detected; inspect the model and API schema. |
| [AffiliateEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliateEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [AffiliateLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliateLink.php) | No literal fillable array detected; inspect the model and API schema. |
| [AffiliatePayout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management/src/Models/AffiliatePayout.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AffiliateController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management-api/src/Http/Controllers/AffiliateController.php) | `public function __construct(private readonly AffiliateQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(ApplyAffiliate $action): JsonResponse`<br>`public function approve(Affiliate $affiliate, ApproveAffiliate $action): JsonResponse`<br>`public function link(Affiliate $affiliate, CreateAffiliateLink $action): JsonResponse`<br>`public function event(AffiliateLink $link, RecordAffiliateEvent $action): JsonResponse`<br>`public function events(): JsonResponse` |

**Observed route declarations:**

[modules/crm-affiliate-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-affiliate-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/affiliate-management')->group(function (): void {
Route::get('affiliates', [AffiliateController::class, 'index']);
Route::post('affiliates', [AffiliateController::class, 'store']);
Route::post('affiliates/{affiliate}/approve', [AffiliateController::class, 'approve']);
Route::post('affiliates/{affiliate}/links', [AffiliateController::class, 'link']);
Route::post('links/{link}/events', [AffiliateController::class, 'event']);
Route::get('events', [AffiliateController::class, 'events']);
```
<!-- layer-implementation-plan:end -->
