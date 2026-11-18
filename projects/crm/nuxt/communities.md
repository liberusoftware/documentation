# CRM: Communities Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#communities). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-communities-nuxt`
**Matching domain module:** `crm-communities`
**Application:** CRM
**Source feature:** [Communities](../features/communities.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/communities.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-communities` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customer/partner groups:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Spaces:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Memberships:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Posts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Comments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Events:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Moderation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Gamification:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Knowledge links:** page/component/composable/API-action behavior for this module's authorized workflow.
- **CRM profile activity:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-communities-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `customer-partner-groups`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `spaces`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `memberships`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `posts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `comments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `events`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `moderation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `gamification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `knowledge-links`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `crm-profile-activity`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-communities` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/communities.md)) |
| Capability Nuxt module skeleton | [`module-crm-communities-nuxt`](https://github.com/liberusoftware/module-crm-communities-nuxt) (`@liberusoftware/module-crm-communities-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Customer/partner groups** | Expose composable and Vue 3 component for `customer/partner groups` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Spaces** | Expose composable and Vue 3 component for `spaces` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Memberships** | Expose composable and Vue 3 component for `memberships` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Posts** | Expose composable and Vue 3 component for `posts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Comments** | Expose composable and Vue 3 component for `comments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Events** | Expose composable and Vue 3 component for `events` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Moderation** | Expose composable and Vue 3 component for `moderation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Gamification** | Expose composable and Vue 3 component for `gamification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Knowledge links** | Expose composable and Vue 3 component for `knowledge links` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **CRM profile activity** | Expose composable and Vue 3 component for `crm profile activity` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CommunityQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Queries/CommunityQuery.php) | `public function spaces(int $teamId): Builder`<br>`public function feed(int $teamId, int $spaceId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCommunitySpace.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Actions/CreateCommunitySpace.php) | `public function execute(int $teamId, int $ownerId, string $name, string $kind = 'customer', array $settings = []): CommunitySpace` |
| [JoinCommunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Actions/JoinCommunity.php) | `public function execute(int $teamId, CommunitySpace $space, string $subjectKey, string $role = 'member'): CommunityMembership` |
| [PublishCommunityContent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Actions/PublishCommunityContent.php) | `public function execute(int $teamId, CommunitySpace $space, string $authorKey, string $body, string $kind = 'post', ?int $parentId = null, array $metadata = []): CommunityContent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommunityContent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Models/CommunityContent.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunityMembership.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Models/CommunityMembership.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunitySpace.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities/src/Models/CommunitySpace.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CommunitiesController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities-api/src/Http/Controllers/CommunitiesController.php) | `public function __construct(private readonly CommunityQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateCommunitySpace $a): JsonResponse`<br>`public function join(CommunitySpace $space, JoinCommunity $a): JsonResponse`<br>`public function content(CommunitySpace $space, PublishCommunityContent $a): JsonResponse`<br>`public function feed(CommunitySpace $space): JsonResponse` |

**Observed route declarations:**

[modules/crm-communities-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-communities-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/communities')->group(function (): void {
Route::get('spaces', [CommunitiesController::class, 'index']);
Route::post('spaces', [CommunitiesController::class, 'store']);
Route::post('spaces/{space}/join', [CommunitiesController::class, 'join']);
Route::post('spaces/{space}/content', [CommunitiesController::class, 'content']);
Route::get('spaces/{space}/feed', [CommunitiesController::class, 'feed']);
```
<!-- layer-implementation-plan:end -->
