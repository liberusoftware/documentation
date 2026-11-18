# CRM: Crm Feedback And Voice Of Customer Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-feedback-and-voice-of-customer). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-feedback-and-voice-of-customer-nuxt`
**Matching domain module:** `crm-feedback-and-voice-of-customer`
**Application:** CRM
**Source feature:** [Crm Feedback And Voice Of Customer](../features/crm-feedback-and-voice-of-customer.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-feedback-and-voice-of-customer.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-feedback-and-voice-of-customer` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **CSAT:** page/component/composable/API-action behavior for this module's authorized workflow.
- **NPS:** page/component/composable/API-action behavior for this module's authorized workflow.
- **CES:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Custom surveys:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sampling:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delivery:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Responses:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Text analysis:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Alerts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Close-the-loop cases:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Trend reporting:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-feedback-and-voice-of-customer-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `csat`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `nps`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ces`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `custom-surveys`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sampling`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delivery`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `responses`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `text-analysis`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `alerts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `close-the-loop-cases`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `trend-reporting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-feedback-and-voice-of-customer` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-feedback-and-voice-of-customer.md)) |
| Capability Nuxt module skeleton | [`module-crm-feedback-and-voice-of-customer-nuxt`](https://github.com/liberusoftware/module-crm-feedback-and-voice-of-customer-nuxt) (`@liberusoftware/module-crm-feedback-and-voice-of-customer-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **CSAT** | Expose composable and Vue 3 component for `csat` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-feedback-and-voice-of-customer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **NPS** | Expose composable and Vue 3 component for `nps` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-feedback-and-voice-of-customer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **CES** | Expose composable and Vue 3 component for `ces` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-feedback-and-voice-of-customer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Custom surveys** | Expose composable and Vue 3 component for `custom surveys` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-feedback-and-voice-of-customer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Sampling** | Expose composable and Vue 3 component for `sampling` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-feedback-and-voice-of-customer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Delivery** | Expose composable and Vue 3 component for `delivery` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-feedback-and-voice-of-customer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Responses** | Expose composable and Vue 3 component for `responses` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-feedback-and-voice-of-customer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Text analysis** | Expose composable and Vue 3 component for `text analysis` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-feedback-and-voice-of-customer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Alerts** | Expose composable and Vue 3 component for `alerts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-feedback-and-voice-of-customer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Close-the-loop cases** | Expose composable and Vue 3 component for `close-the-loop cases` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-feedback-and-voice-of-customer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Trend reporting** | Expose composable and Vue 3 component for `trend reporting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-feedback-and-voice-of-customer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [FeedbackQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Queries/FeedbackQuery.php) | `public function surveys(int $teamId)`<br>`public function responses(int $teamId, int $surveyId)`<br>`public function trend(int $teamId, int $surveyId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateFeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/CreateFeedbackSurvey.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): FeedbackSurvey` |
| [DeliverFeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/DeliverFeedbackSurvey.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackSurvey $survey, ?int $recipientId, string $channel = 'email'): FeedbackDelivery` |
| [OpenFeedbackCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/OpenFeedbackCase.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackResponse $response, ?int $ownerId = null): FeedbackCase` |
| [RecordFeedbackResponse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/RecordFeedbackResponse.php) | `public function execute(int $teamId, FeedbackDelivery $delivery, array $input): FeedbackResponse` |
| [ResolveFeedbackAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/ResolveFeedbackAlert.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackAlert $alert): FeedbackAlert` |
| [FeedbackPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Services/FeedbackPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FeedbackAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackAlert.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackCase.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackDelivery.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackResponse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackResponse.php) | No literal fillable array detected; inspect the model and API schema. |
| [FeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackSurvey.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [FeedbackController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer-api/src/Http/Controllers/FeedbackController.php) | `public function __construct(private readonly FeedbackQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateFeedbackSurvey $action): JsonResponse`<br>`public function deliver(FeedbackSurvey $survey, DeliverFeedbackSurvey $action): JsonResponse`<br>`public function respond(FeedbackDelivery $delivery, RecordFeedbackResponse $action): JsonResponse`<br>`public function trend(FeedbackSurvey $survey): JsonResponse`<br>`public function openCase(FeedbackResponse $response, OpenFeedbackCase $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-feedback-and-voice-of-customer-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/feedback-and-voice-of-customer')->group(function (): void {
Route::get('surveys', [FeedbackController::class, 'index']);
Route::post('surveys', [FeedbackController::class, 'store']);
Route::post('surveys/{survey}/deliver', [FeedbackController::class, 'deliver']);
Route::post('deliveries/{delivery}/responses', [FeedbackController::class, 'respond']);
Route::get('surveys/{survey}/trend', [FeedbackController::class, 'trend']);
Route::post('responses/{response}/cases', [FeedbackController::class, 'openCase']);
```
<!-- layer-implementation-plan:end -->
