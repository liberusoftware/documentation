# Social Network: Federation Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#federation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-social-network-federation-nuxt`
**Matching domain module:** `social-network-federation`
**Application:** Social Network
**Source feature:** [Federation](../features/federation.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/federation.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `social-network-federation` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **ActivityPub identities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Inbox/outbox:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Signatures:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delivery:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Mapping:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Moderation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-social-network-federation-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `activitypub-identities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `inbox-outbox`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `signatures`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delivery`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `mapping`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `moderation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `social-network-federation` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-social-network-nuxt-vue`](https://github.com/liberusoftware/project-social-network-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/federation.md)) |
| Capability Nuxt module skeleton | [`module-social-network-federation-nuxt`](https://github.com/liberusoftware/module-social-network-federation-nuxt) (`@liberusoftware/module-social-network-federation-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **ActivityPub identities** | Expose composable and Vue 3 component for `activitypub identities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/federation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Inbox/outbox** | Expose composable and Vue 3 component for `inbox/outbox` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/federation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Signatures** | Expose composable and Vue 3 component for `signatures` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/federation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Delivery** | Expose composable and Vue 3 component for `delivery` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/federation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Mapping** | Expose composable and Vue 3 component for `mapping` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/federation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Moderation** | Expose composable and Vue 3 component for `moderation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/federation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/federation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PublishActivity.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Actions/PublishActivity.php) | `public function handle(string $type, array $payload): FederationMessage` |
| [QueueDelivery.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Actions/QueueDelivery.php) | `public function handle(FederationMessage $message, string $inboxUrl): FederationDelivery` |
| [ReceiveActivity.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Actions/ReceiveActivity.php) | `public function handle(array $payload, ?string $signature = null): FederationMessage` |
| [ReconcileMapping.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Actions/ReconcileMapping.php) | `public function handle(string $remoteType, string $remoteId, string $localType, string $localId, array $metadata = []): FederationMapping` |
| [RegisterActor.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Actions/RegisterActor.php) | `public function handle(Profile $profile, array $data): FederationActor` |
| [VerifyActivitySignature.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Actions/VerifyActivitySignature.php) | `public function handle(string $payload, string $signature, string $publicKey): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FederationActor.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Models/FederationActor.php) | No literal fillable array detected; inspect the model and API schema. |
| [FederationDelivery.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Models/FederationDelivery.php) | No literal fillable array detected; inspect the model and API schema. |
| [FederationMapping.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Models/FederationMapping.php) | No literal fillable array detected; inspect the model and API schema. |
| [FederationMessage.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation/src/Models/FederationMessage.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [FederationController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation-api/src/Http/Controllers/FederationController.php) | `public function inbox(Request $request, ReceiveActivity $receive): JsonResponse`<br>`public function outbox(Request $request): JsonResponse`<br>`public function actor(Request $request, GetProfile $get, RegisterActor $register): JsonResponse` |

**Observed route declarations:**

[modules/social-network-federation-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-federation-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/federation')->middleware('api')->group(function (): void {
Route::post('/inbox', [FederationController::class, 'inbox'])->name('social-network.federation.inbox');
Route::get('/outbox', [FederationController::class, 'outbox'])->name('social-network.federation.outbox');
Route::middleware(['auth:sanctum', 'throttle:60,1'])->post('/actors', [FederationController::class, 'actor'])->name('social-network.federation.actors');
```
<!-- layer-implementation-plan:end -->
