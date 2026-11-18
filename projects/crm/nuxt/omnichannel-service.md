# CRM: Omnichannel Service Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#omnichannel-service). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-omnichannel-service-nuxt`
**Matching domain module:** `crm-omnichannel-service`
**Application:** CRM
**Source feature:** [Omnichannel Service](../features/omnichannel-service.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/omnichannel-service.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-omnichannel-service` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Email/chat/social/phone intake:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Routing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Agent workspace:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Macros:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Suggested replies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Swarming:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Collision control:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Complete interaction history:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-omnichannel-service-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `email-chat-social-phone-intake`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `routing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `agent-workspace`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `macros`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `suggested-replies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `swarming`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `collision-control`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `complete-interaction-history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-omnichannel-service` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/omnichannel-service.md)) |
| Capability Nuxt module skeleton | [`module-crm-omnichannel-service-nuxt`](https://github.com/liberusoftware/module-crm-omnichannel-service-nuxt) (`@liberusoftware/module-crm-omnichannel-service-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Email/chat/social/phone intake** | Expose composable and Vue 3 component for `email/chat/social/phone intake` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/omnichannel-service.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Routing** | Expose composable and Vue 3 component for `routing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/omnichannel-service.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Agent workspace** | Expose composable and Vue 3 component for `agent workspace` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/omnichannel-service.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Macros** | Expose composable and Vue 3 component for `macros` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/omnichannel-service.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Suggested replies** | Expose composable and Vue 3 component for `suggested replies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/omnichannel-service.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Swarming** | Expose composable and Vue 3 component for `swarming` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/omnichannel-service.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Collision control** | Expose composable and Vue 3 component for `collision control` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/omnichannel-service.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Complete interaction history** | Expose composable and Vue 3 component for `complete interaction history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/omnichannel-service.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ConversationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Queries/ConversationQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AssignConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/AssignConversation.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Conversation $conversation, array $input): Conversation` |
| [RecordInteraction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/RecordInteraction.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Conversation $conversation, array $input): Interaction` |
| [RecordWorkspaceEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/RecordWorkspaceEvent.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Conversation $conversation, array $input): WorkspaceEvent` |
| [StartConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Actions/StartConversation.php) | `public function __construct(private readonly OmnichannelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Conversation` |
| [OmnichannelPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Services/OmnichannelPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/Conversation.php) | No literal fillable array detected; inspect the model and API schema. |
| [Interaction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/Interaction.php) | No literal fillable array detected; inspect the model and API schema. |
| [Macro.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/Macro.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkspaceEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service/src/Models/WorkspaceEvent.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [OmnichannelController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-omnichannel-service-api/src/Http/Controllers/OmnichannelController.php) | `public function index(Request $r, ConversationQuery $q): JsonResponse`<br>`public function store(Request $r, StartConversation $a): JsonResponse`<br>`public function interaction(Request $r, Conversation $c, RecordInteraction $a): JsonResponse`<br>`public function assign(Request $r, Conversation $c, AssignConversation $a): JsonResponse`<br>`public function workspaceEvent(Request $r, Conversation $c, RecordWorkspaceEvent $a): JsonResponse` |
<!-- layer-implementation-plan:end -->
