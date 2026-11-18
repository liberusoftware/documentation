# CRM: Email Marketing Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#email-marketing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-email-marketing-nuxt`
**Matching domain module:** `crm-email-marketing`
**Application:** CRM
**Source feature:** [Email Marketing](../features/email-marketing.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/email-marketing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-email-marketing` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Drag-and-drop and code templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Personalization:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dynamic content:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Test sends:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Inbox previews:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deliverability controls:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Scheduling:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Throttling:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Analytics:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-email-marketing-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `drag-and-drop-and-code-templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `personalization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dynamic-content`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `test-sends`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `inbox-previews`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deliverability-controls`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `scheduling`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `throttling`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `analytics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-email-marketing` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/email-marketing.md)) |
| Capability Nuxt module skeleton | [`module-crm-email-marketing-nuxt`](https://github.com/liberusoftware/module-crm-email-marketing-nuxt) (`@liberusoftware/module-crm-email-marketing-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Drag-and-drop and code templates** | Expose composable and Vue 3 component for `drag-and-drop and code templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/email-marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Personalization** | Expose composable and Vue 3 component for `personalization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/email-marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Dynamic content** | Expose composable and Vue 3 component for `dynamic content` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/email-marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Test sends** | Expose composable and Vue 3 component for `test sends` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/email-marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Inbox previews** | Expose composable and Vue 3 component for `inbox previews` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/email-marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Deliverability controls** | Expose composable and Vue 3 component for `deliverability controls` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/email-marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Scheduling** | Expose composable and Vue 3 component for `scheduling` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/email-marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Throttling** | Expose composable and Vue 3 component for `throttling` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/email-marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Analytics** | Expose composable and Vue 3 component for `analytics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/email-marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EmailMarketingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Queries/EmailMarketingQuery.php) | `public function campaigns(int $teamId)`<br>`public function analytics(int $teamId, int $campaignId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateEmailCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/CreateEmailCampaign.php) | `public function __construct(private readonly EmailMarketingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailCampaign` |
| [RecordMarketingEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/RecordMarketingEvent.php) | `public function execute(int $teamId, EmailCampaign $campaign, array $input): EmailMarketingEvent` |
| [ScheduleCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/ScheduleCampaign.php) | `public function __construct(private readonly EmailMarketingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, EmailCampaign $campaign, array $input): EmailCampaign` |
| [EmailMarketingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Services/EmailMarketingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EmailCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailCampaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailDelivery.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailMarketingEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailMarketingEvent.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [EmailMarketingController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing-api/src/Http/Controllers/EmailMarketingController.php) | `public function __construct(private readonly EmailMarketingQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateEmailCampaign $action): JsonResponse`<br>`public function schedule(EmailCampaign $campaign, ScheduleCampaign $action): JsonResponse`<br>`public function event(EmailCampaign $campaign, RecordMarketingEvent $action): JsonResponse`<br>`public function analytics(EmailCampaign $campaign): JsonResponse` |

**Observed route declarations:**

[modules/crm-email-marketing-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/email-marketing')->group(function (): void {
Route::get('campaigns', [EmailMarketingController::class, 'index']);
Route::post('campaigns', [EmailMarketingController::class, 'store']);
Route::post('campaigns/{campaign}/schedule', [EmailMarketingController::class, 'schedule']);
Route::post('campaigns/{campaign}/events', [EmailMarketingController::class, 'event']);
Route::get('campaigns/{campaign}/analytics', [EmailMarketingController::class, 'analytics']);
```
<!-- layer-implementation-plan:end -->
