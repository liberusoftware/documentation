# CRM: Crm Conversation Intelligence Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-conversation-intelligence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-conversation-intelligence-nuxt`
**Matching domain module:** `crm-conversation-intelligence`
**Application:** CRM
**Source feature:** [Crm Conversation Intelligence](../features/crm-conversation-intelligence.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-conversation-intelligence.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-conversation-intelligence` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Call/meeting recording:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transcription:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Summaries:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Topics:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Questions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Objections:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Competitors:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sentiment policy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Action items:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Highlights:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Searchable evidence:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-conversation-intelligence-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `call-meeting-recording`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transcription`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `summaries`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `topics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `questions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `objections`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `competitors`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sentiment-policy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `action-items`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `highlights`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `searchable-evidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-conversation-intelligence` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-conversation-intelligence.md)) |
| Capability Nuxt module skeleton | [`module-crm-conversation-intelligence-nuxt`](https://github.com/liberusoftware/module-crm-conversation-intelligence-nuxt) (`@liberusoftware/module-crm-conversation-intelligence-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Call/meeting recording** | Expose composable and Vue 3 component for `call/meeting recording` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-conversation-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Transcription** | Expose composable and Vue 3 component for `transcription` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-conversation-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Summaries** | Expose composable and Vue 3 component for `summaries` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-conversation-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Topics** | Expose composable and Vue 3 component for `topics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-conversation-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Questions** | Expose composable and Vue 3 component for `questions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-conversation-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Objections** | Expose composable and Vue 3 component for `objections` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-conversation-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Competitors** | Expose composable and Vue 3 component for `competitors` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-conversation-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Sentiment policy** | Expose composable and Vue 3 component for `sentiment policy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-conversation-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Action items** | Expose composable and Vue 3 component for `action items` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-conversation-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Highlights** | Expose composable and Vue 3 component for `highlights` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-conversation-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Searchable evidence** | Expose composable and Vue 3 component for `searchable evidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-conversation-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ConversationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Queries/ConversationQuery.php) | `public function conversations(int $teamId): Builder`<br>`public function evidence(int $teamId, string $search): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddEvidence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Actions/AddEvidence.php) | `public function execute(int $teamId, Conversation $conversation, string $kind, string $label, string $content, array $metadata = []): ConversationEvidence` |
| [AnalyzeConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Actions/AnalyzeConversation.php) | `public function execute(int $teamId, Conversation $conversation, string $transcript, array $insights = []): Conversation` |
| [RecordConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Actions/RecordConversation.php) | `public function execute(int $teamId, int $userId, array $input): Conversation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Models/Conversation.php) | No literal fillable array detected; inspect the model and API schema. |
| [ConversationEvidence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence/src/Models/ConversationEvidence.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConversationIntelligenceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence-api/src/Http/Controllers/ConversationIntelligenceController.php) | `public function __construct(private readonly ConversationQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(RecordConversation $a): JsonResponse`<br>`public function analyze(Conversation $c, AnalyzeConversation $a): JsonResponse`<br>`public function evidence(Conversation $c, AddEvidence $a): JsonResponse`<br>`public function search(): JsonResponse` |

**Observed route declarations:**

[modules/crm-conversation-intelligence-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversation-intelligence-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/conversation-intelligence')->group(function (): void {
Route::get('conversations', [ConversationIntelligenceController::class, 'index']);
Route::post('conversations', [ConversationIntelligenceController::class, 'store']);
Route::post('conversations/{conversation}/analyze', [ConversationIntelligenceController::class, 'analyze']);
Route::post('conversations/{conversation}/evidence', [ConversationIntelligenceController::class, 'evidence']);
Route::get('evidence/search', [ConversationIntelligenceController::class, 'search']);
```
<!-- layer-implementation-plan:end -->
