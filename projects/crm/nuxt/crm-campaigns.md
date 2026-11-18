# CRM: Crm Campaigns Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-campaigns). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-campaigns-nuxt`
**Matching domain module:** `crm-campaigns`
**Application:** CRM
**Source feature:** [Crm Campaigns](../features/crm-campaigns.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-campaigns.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-campaigns` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Campaign hierarchy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Briefs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Objectives:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Budget:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Assets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Channels:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Audience:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Owners:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Calendar:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tasks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Costs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Responses:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Influence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **ROI:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-campaigns-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `campaign-hierarchy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `briefs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `objectives`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `budget`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `assets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `channels`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `audience`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `owners`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `calendar`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tasks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `costs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `responses`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `influence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `roi`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-campaigns` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-campaigns.md)) |
| Capability Nuxt module skeleton | [`module-crm-campaigns-nuxt`](https://github.com/liberusoftware/module-crm-campaigns-nuxt) (`@liberusoftware/module-crm-campaigns-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Campaign hierarchy** | Expose composable and Vue 3 component for `campaign hierarchy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-campaigns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Briefs** | Expose composable and Vue 3 component for `briefs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-campaigns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Objectives** | Expose composable and Vue 3 component for `objectives` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-campaigns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Budget** | Expose composable and Vue 3 component for `budget` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-campaigns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Assets** | Expose composable and Vue 3 component for `assets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-campaigns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Channels** | Expose composable and Vue 3 component for `channels` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-campaigns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Audience** | Expose composable and Vue 3 component for `audience` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-campaigns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Owners** | Expose composable and Vue 3 component for `owners` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-campaigns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Calendar** | Expose composable and Vue 3 component for `calendar` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-campaigns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Tasks** | Expose composable and Vue 3 component for `tasks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-campaigns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Costs** | Expose composable and Vue 3 component for `costs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-campaigns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Responses** | Expose composable and Vue 3 component for `responses` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-campaigns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Influence** | Expose composable and Vue 3 component for `influence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-campaigns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **ROI** | Expose composable and Vue 3 component for `roi` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-campaigns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CampaignQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Queries/CampaignQuery.php) | `public function campaigns(int $teamId): Builder`<br>`public function roi(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Actions/CreateCampaign.php) | `public function execute(int $teamId, int $ownerId, array $input): Campaign` |
| [RecordCampaignEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Actions/RecordCampaignEvent.php) | `public function execute(int $teamId, int $actorId, Campaign $campaign, string $type, float $value = 0, array $payload = []): CampaignEvent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Campaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Models/Campaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [CampaignEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Models/CampaignEvent.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CampaignsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns-api/src/Http/Controllers/CampaignsController.php) | `public function __construct(private readonly CampaignQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateCampaign $a): JsonResponse`<br>`public function event(Campaign $campaign, RecordCampaignEvent $a): JsonResponse`<br>`public function roi(): JsonResponse` |

**Observed route declarations:**

[modules/crm-campaigns-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/campaigns')->group(function (): void {
Route::get('/', [CampaignsController::class, 'index']);
Route::post('/', [CampaignsController::class, 'store']);
Route::post('{campaign}/events', [CampaignsController::class, 'event']);
Route::get('roi', [CampaignsController::class, 'roi']);
```
<!-- layer-implementation-plan:end -->
