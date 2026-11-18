# CRM: Conversation Analytics Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#conversation-analytics). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-conversation-analytics-nuxt`
**Matching domain module:** `crm-conversation-analytics`
**Application:** CRM
**Source feature:** [Conversation Analytics](../features/conversation-analytics.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/conversation-analytics.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-conversation-analytics` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Topics:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Objections:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Competitors:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Talk ratios:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Questions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Outcomes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Coaching moments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quality scorecards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Trend comparison:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-conversation-analytics-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `topics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `objections`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `competitors`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `talk-ratios`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `questions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `outcomes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `coaching-moments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quality-scorecards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `trend-comparison`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-conversation-analytics` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/conversation-analytics.md)) |
| Capability Nuxt module skeleton | [`module-crm-conversation-analytics-nuxt`](https://github.com/liberusoftware/module-crm-conversation-analytics-nuxt) (`@liberusoftware/module-crm-conversation-analytics-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Topics** | Expose composable and Vue 3 component for `topics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversation-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Objections** | Expose composable and Vue 3 component for `objections` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversation-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Competitors** | Expose composable and Vue 3 component for `competitors` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversation-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Talk ratios** | Expose composable and Vue 3 component for `talk ratios` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversation-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Questions** | Expose composable and Vue 3 component for `questions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversation-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Outcomes** | Expose composable and Vue 3 component for `outcomes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversation-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Coaching moments** | Expose composable and Vue 3 component for `coaching moments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversation-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Quality scorecards** | Expose composable and Vue 3 component for `quality scorecards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversation-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Trend comparison** | Expose composable and Vue 3 component for `trend comparison` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/conversation-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ConversationAnalyticsQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics/src/Queries/ConversationAnalyticsQuery.php) | `public function analyses(int $teamId): Builder`<br>`public function trends(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordConversationAnalysis.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics/src/Actions/RecordConversationAnalysis.php) | `public function execute(int $teamId, int $analystId, string $conversationKey, array $input): ConversationAnalysis` |
| [ScoreConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics/src/Actions/ScoreConversation.php) | `public function execute(int $teamId, ConversationAnalysis $analysis, array $scores): ConversationAnalysis` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConversationAnalysis.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics/src/Models/ConversationAnalysis.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConversationAnalyticsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics-api/src/Http/Controllers/ConversationAnalyticsController.php) | `public function __construct(private readonly ConversationAnalyticsQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(string $conversationKey, RecordConversationAnalysis $a): JsonResponse`<br>`public function score(ConversationAnalysis $analysis, ScoreConversation $a): JsonResponse`<br>`public function trends(): JsonResponse` |

**Observed route declarations:**

[modules/crm-conversation-analytics-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-analytics-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/conversation-analytics')->group(function (): void {
Route::get('analyses', [ConversationAnalyticsController::class, 'index']);
Route::post('analyses/{conversationKey}', [ConversationAnalyticsController::class, 'store']);
Route::post('analyses/{analysis}/score', [ConversationAnalyticsController::class, 'score']);
Route::get('trends', [ConversationAnalyticsController::class, 'trends']);
```
<!-- layer-implementation-plan:end -->
