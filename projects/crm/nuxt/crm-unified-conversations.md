# CRM: Crm Unified Conversations Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-unified-conversations). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-unified-conversations-nuxt`
**Matching domain module:** `crm-unified-conversations`
**Application:** CRM
**Source feature:** [Crm Unified Conversations](../features/crm-unified-conversations.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-unified-conversations.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-unified-conversations` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Omnichannel threads:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Participants:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Identity matching:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Assignments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Collision detection:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Drafts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Internal notes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attachments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delivery/read state:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Timeline:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-unified-conversations-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `omnichannel-threads`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `participants`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `identity-matching`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `assignments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `collision-detection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `drafts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `internal-notes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `attachments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delivery-read-state`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `timeline`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-unified-conversations` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-unified-conversations.md)) |
| Capability Nuxt module skeleton | [`module-crm-unified-conversations-nuxt`](https://github.com/liberusoftware/module-crm-unified-conversations-nuxt) (`@liberusoftware/module-crm-unified-conversations-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Omnichannel threads** | Expose composable and Vue 3 component for `omnichannel threads` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-unified-conversations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Participants** | Expose composable and Vue 3 component for `participants` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-unified-conversations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Identity matching** | Expose composable and Vue 3 component for `identity matching` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-unified-conversations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Assignments** | Expose composable and Vue 3 component for `assignments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-unified-conversations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Collision detection** | Expose composable and Vue 3 component for `collision detection` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-unified-conversations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Drafts** | Expose composable and Vue 3 component for `drafts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-unified-conversations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Internal notes** | Expose composable and Vue 3 component for `internal notes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-unified-conversations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Attachments** | Expose composable and Vue 3 component for `attachments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-unified-conversations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Delivery/read state** | Expose composable and Vue 3 component for `delivery/read state` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-unified-conversations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Timeline** | Expose composable and Vue 3 component for `timeline` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-unified-conversations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ConversationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Queries/ConversationQuery.php) | `public function list(int $teamId)`<br>`public function find(int $teamId, int $id): Conversation` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AssignConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/AssignConversation.php) | `public function execute(int $teamId, int $actorId, int $conversationId, ?int $assignee): Conversation` |
| [OpenConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/OpenConversation.php) | `public function execute(int $teamId, int $actorId, array $data): Conversation` |
| [SendMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/SendMessage.php) | `public function execute(int $teamId, int $actorId, int $conversationId, array $data): ConversationMessage` |
| [SyncExternalConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/SyncExternalConversation.php) | `public function execute(int $teamId, array $data): Conversation` |
| [ConversationAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Services/ConversationAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [ConversationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Services/ConversationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/Conversation.php) | `team_id`, `channel`, `external_id`, `subject`, `status`, `priority`, `assigned_to`, `last_message_at`, `metadata` |
| [ConversationAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/ConversationAudit.php) | `team_id`, `actor_id`, `event`, `details` |
| [ConversationMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/ConversationMessage.php) | `team_id`, `conversation_id`, `external_id`, `sender_id`, `body`, `direction`, `metadata`, `internal`, `delivery_status`, `read_at`, `idempotency_key` |
| [ConversationParticipant.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/ConversationParticipant.php) | `team_id`, `conversation_id`, `identity`, `name`, `role` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConversationController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations-api/src/Http/Controllers/ConversationController.php) | `public function index(Request $r, ConversationQuery $q): JsonResponse`<br>`public function store(Request $r, OpenConversation $a): JsonResponse`<br>`public function message(Request $r, int $conversation, SendMessage $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-unified-conversations-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/unified-conversations')->group(function () {
Route::get('/', [ConversationController::class, 'index']);
Route::post('/', [ConversationController::class, 'store']);
Route::post('/{conversation}/messages', [ConversationController::class, 'message']);
```
<!-- layer-implementation-plan:end -->
