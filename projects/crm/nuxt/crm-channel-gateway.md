# CRM: Crm Channel Gateway Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-channel-gateway). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-channel-gateway-nuxt`
**Matching domain module:** `crm-channel-gateway`
**Application:** CRM
**Source feature:** [Crm Channel Gateway](../features/crm-channel-gateway.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-channel-gateway.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-channel-gateway` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Provider-neutral email:** page/component/composable/API-action behavior for this module's authorized workflow.
- **SMS/MMS:** page/component/composable/API-action behavior for this module's authorized workflow.
- **WhatsApp:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Web chat:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Social messaging:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Push contracts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Routing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Health:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provider selection:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-channel-gateway-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `provider-neutral-email`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sms-mms`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `whatsapp`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `web-chat`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `social-messaging`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `push-contracts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `routing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `health`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provider-selection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-channel-gateway` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-channel-gateway.md)) |
| Capability Nuxt module skeleton | [`module-crm-channel-gateway-nuxt`](https://github.com/liberusoftware/module-crm-channel-gateway-nuxt) (`@liberusoftware/module-crm-channel-gateway-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Provider-neutral email** | Expose composable and Vue 3 component for `provider-neutral email` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-gateway.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **SMS/MMS** | Expose composable and Vue 3 component for `sms/mms` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-gateway.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **WhatsApp** | Expose composable and Vue 3 component for `whatsapp` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-gateway.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Web chat** | Expose composable and Vue 3 component for `web chat` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-gateway.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Social messaging** | Expose composable and Vue 3 component for `social messaging` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-gateway.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Push contracts** | Expose composable and Vue 3 component for `push contracts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-gateway.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Routing** | Expose composable and Vue 3 component for `routing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-gateway.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Templates** | Expose composable and Vue 3 component for `templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-gateway.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Health** | Expose composable and Vue 3 component for `health` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-gateway.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Provider selection** | Expose composable and Vue 3 component for `provider selection` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-gateway.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [GatewayQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Queries/GatewayQuery.php) | `public function channels(int $teamId): Builder`<br>`public function deliveries(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [QueueGatewayDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Actions/QueueGatewayDelivery.php) | `public function execute(int $teamId, GatewayChannel $channel, string $idempotencyKey, string $address, string $body, array $metadata = []): GatewayDelivery` |
| [RegisterGatewayChannel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Actions/RegisterGatewayChannel.php) | `public function execute(int $teamId, string $key, string $kind, string $provider, array $configuration = []): GatewayChannel` |
| [UpdateGatewayHealth.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Actions/UpdateGatewayHealth.php) | `public function execute(int $teamId, GatewayChannel $channel, bool $healthy, ?string $failure = null): GatewayChannel` |
| [ChannelAdapter.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Contracts/ChannelAdapter.php) | `public function send(string $address, string $body, array $metadata = []): string`<br>`public function health(): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [GatewayChannel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Models/GatewayChannel.php) | No literal fillable array detected; inspect the model and API schema. |
| [GatewayDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway/src/Models/GatewayDelivery.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ChannelGatewayController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway-api/src/Http/Controllers/ChannelGatewayController.php) | `public function __construct(private readonly GatewayQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(RegisterGatewayChannel $a): JsonResponse`<br>`public function delivery(GatewayChannel $channel, QueueGatewayDelivery $a): JsonResponse`<br>`public function health(GatewayChannel $channel, UpdateGatewayHealth $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-channel-gateway-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-gateway-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/channel-gateway')->group(function (): void {
Route::get('channels', [ChannelGatewayController::class, 'index']);
Route::post('channels', [ChannelGatewayController::class, 'store']);
Route::post('channels/{channel}/deliveries', [ChannelGatewayController::class, 'delivery']);
Route::post('channels/{channel}/health', [ChannelGatewayController::class, 'health']);
```
<!-- layer-implementation-plan:end -->
