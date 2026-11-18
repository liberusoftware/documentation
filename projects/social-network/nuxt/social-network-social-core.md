# Social Network: Social Network Social Core Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-social-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-social-network-social-network-social-core-nuxt`
**Matching domain module:** `social-network-social-core`
**Application:** Social Network
**Source feature:** [Social Network Social Core](../features/social-network-social-core.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/social-network-social-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `social-network-social-core` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Network settings:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deployment mode:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Terminology:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Feature policy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Shared IDs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Events:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-social-network-social-network-social-core-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `network-settings`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deployment-mode`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `terminology`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `feature-policy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `shared-ids`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `events`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `social-network-social-core` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-social-network-nuxt-vue`](https://github.com/liberusoftware/project-social-network-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-network-social-core.md)) |
| Capability Nuxt module skeleton | [`module-social-network-social-core-nuxt`](https://github.com/liberusoftware/module-social-network-social-core-nuxt) (`@liberusoftware/module-social-network-social-core-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Network settings** | Expose composable and Vue 3 component for `network settings` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-social-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Deployment mode** | Expose composable and Vue 3 component for `deployment mode` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-social-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Terminology** | Expose composable and Vue 3 component for `terminology` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-social-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Feature policy** | Expose composable and Vue 3 component for `feature policy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-social-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Shared IDs** | Expose composable and Vue 3 component for `shared ids` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-social-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Events** | Expose composable and Vue 3 component for `events` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-social-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GetSocialNetworkSettings.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Actions/GetSocialNetworkSettings.php) | `public function __construct(private SocialNetworkSettingsRepository $settings)`<br>`public function handle(int\|string $teamId): SocialNetworkSettings` |
| [UpdateSocialNetworkSettings.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Actions/UpdateSocialNetworkSettings.php) | `public function __construct( private SocialNetworkSettingsRepository $settings, private SocialNetworkSettingsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(int\|string $teamId, array $attributes, int\|string\|null $actorId = null): SocialNetworkSettings` |
| [SocialNetworkSettingsAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Contracts/SocialNetworkSettingsAuthorizer.php) | `public function authorize(int\|string $teamId): void` |
| [SocialNetworkSettingsRepository.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Contracts/SocialNetworkSettingsRepository.php) | `public function forTeam(int\|string $teamId): SocialNetworkSettings` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SocialNetworkSettings.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Models/SocialNetworkSettings.php) | `id`, `team_id`, `deployment_mode`, `network_settings`, `terminology`, `feature_policy`, `shared_ids` |

| Observed API controller | Handler signatures |
| --- | --- |
| [SocialCoreSettingsController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-api/src/Http/Controllers/SocialCoreSettingsController.php) | `public function show(Request $request, GetSocialNetworkSettings $get): JsonResponse`<br>`public function update(Request $request, UpdateSocialNetworkSettings $update): JsonResponse` |

**Observed route declarations:**

[modules/social-network-social-core-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/social-core')
Route::get('/', [SocialCoreSettingsController::class, 'show'])->name('show');
Route::patch('/', [SocialCoreSettingsController::class, 'update'])->name('update');
```
<!-- layer-implementation-plan:end -->
