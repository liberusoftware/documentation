# CRM: Crm Telephony Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-telephony). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-telephony-nuxt`
**Matching domain module:** `crm-telephony`
**Application:** CRM
**Source feature:** [Crm Telephony](../features/crm-telephony.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-telephony.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-telephony` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Numbers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Caller ID:** page/component/composable/API-action behavior for this module's authorized workflow.
- **IVR:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Queues:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Business hours:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Skills:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Recording:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Voicemail:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transfers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dispositions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Click-to-call:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Call logging:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provider adapters:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-telephony-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `numbers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `caller-id`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ivr`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `queues`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `business-hours`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `skills`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `recording`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `voicemail`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transfers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dispositions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `click-to-call`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `call-logging`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provider-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-telephony` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-telephony.md)) |
| Capability Nuxt module skeleton | [`module-crm-telephony-nuxt`](https://github.com/liberusoftware/module-crm-telephony-nuxt) (`@liberusoftware/module-crm-telephony-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Numbers** | Expose composable and Vue 3 component for `numbers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-telephony.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Caller ID** | Expose composable and Vue 3 component for `caller id` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-telephony.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **IVR** | Expose composable and Vue 3 component for `ivr` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-telephony.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Queues** | Expose composable and Vue 3 component for `queues` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-telephony.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Business hours** | Expose composable and Vue 3 component for `business hours` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-telephony.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Skills** | Expose composable and Vue 3 component for `skills` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-telephony.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Recording** | Expose composable and Vue 3 component for `recording` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-telephony.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Voicemail** | Expose composable and Vue 3 component for `voicemail` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-telephony.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Transfers** | Expose composable and Vue 3 component for `transfers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-telephony.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Dispositions** | Expose composable and Vue 3 component for `dispositions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-telephony.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Click-to-call** | Expose composable and Vue 3 component for `click-to-call` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-telephony.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Call logging** | Expose composable and Vue 3 component for `call logging` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-telephony.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Provider adapters** | Expose composable and Vue 3 component for `provider adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-telephony.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TelephonyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Queries/TelephonyQuery.php) | `public function numbers(int $teamId)`<br>`public function queues(int $teamId)`<br>`public function calls(int $teamId)`<br>`public function settings(int $teamId): ?TelephonySettings` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureTelephony.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/ConfigureTelephony.php) | `public function execute(int $teamId, int $actorId, array $data): TelephonySettings` |
| [CreateTelephonyQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/CreateTelephonyQueue.php) | `public function execute(int $teamId, int $actorId, array $data): TelephonyQueue` |
| [LogTelephonyCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/LogTelephonyCall.php) | `public function execute(int $teamId, int $actorId, array $data): TelephonyCall` |
| [UpdateCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/UpdateCall.php) | `public function execute(int $teamId, int $actorId, int $callId, array $data): TelephonyCall` |
| [UpsertTelephonyNumber.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/UpsertTelephonyNumber.php) | `public function execute(int $teamId, int $actorId, array $data, ?int $id = null): TelephonyNumber` |
| [TelephonyAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Services/TelephonyAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): Audit` |
| [TelephonyPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Services/TelephonyPolicy.php) | `public function canManage(int $teamId, int $userId): bool`<br>`public function isTeamMember(int $teamId, int $userId, array $roles = [], bool $includeOwner = false): bool` |
| [TenantTwilioService.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Services/TenantTwilioService.php) | `public function client(int $teamId): Client`<br>`public function sendMessage(int $teamId, string $to, string $body): object`<br>`public function usage(int $teamId, array $filters = []): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TelephonyAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonyCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyCall.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonyNumber.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyNumber.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonyQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyQueue.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonySettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonySettings.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [TelephonyController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-api/src/Http/Controllers/TelephonyController.php) | `public function numbers(Request $r, TelephonyQuery $q): JsonResponse`<br>`public function queues(Request $r, TelephonyQuery $q): JsonResponse`<br>`public function settings(Request $r, TelephonyQuery $q): JsonResponse`<br>`public function configure(Request $r, ConfigureTelephony $a): JsonResponse`<br>`public function number(Request $r, UpsertTelephonyNumber $a): JsonResponse`<br>`public function queue(Request $r, CreateTelephonyQueue $a): JsonResponse`<br>`public function calls(Request $r, TelephonyQuery $q): JsonResponse`<br>`public function logCall(Request $r, LogTelephonyCall $a): JsonResponse`<br>`public function updateCall(Request $r, int $call, UpdateCall $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-telephony-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/telephony')->group(function (): void {
Route::get('/numbers', [TelephonyController::class, 'numbers']);
Route::post('/numbers', [TelephonyController::class, 'number']);
Route::get('/queues', [TelephonyController::class, 'queues']);
Route::post('/queues', [TelephonyController::class, 'queue']);
Route::get('/settings', [TelephonyController::class, 'settings']);
Route::put('/settings', [TelephonyController::class, 'configure']);
Route::get('/calls', [TelephonyController::class, 'calls']);
Route::post('/calls', [TelephonyController::class, 'logCall']);
Route::patch('/calls/{call}', [TelephonyController::class, 'updateCall']);
```
<!-- layer-implementation-plan:end -->
