# Automation: Module Automation Voice Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-automation-voice). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-automation-module-automation-voice-nuxt`
**Matching domain module:** `module-automation-voice`
**Application:** Automation
**Source feature:** [Module Automation Voice](../features/module-automation-voice.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-automation-voice.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-automation-voice` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Speech-to-text:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Text-to-speech:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Streaming sessions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Interruption:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transcripts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Consent controls:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-automation-module-automation-voice-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `speech-to-text`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `text-to-speech`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `streaming-sessions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `interruption`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transcripts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `consent-controls`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-automation-voice` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-automation-nuxt-vue`](https://github.com/liberusoftware/project-automation-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-automation-laravel-api`](https://github.com/liberusoftware/project-automation-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-automation-voice.md)) |
| Capability Nuxt module skeleton | [`module-automation-voice-nuxt`](https://github.com/liberusoftware/module-automation-voice-nuxt) (`@liberusoftware/module-automation-voice-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Speech-to-text** | Expose composable and Vue 3 component for `speech-to-text` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-automation-voice.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Text-to-speech** | Expose composable and Vue 3 component for `text-to-speech` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-automation-voice.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Streaming sessions** | Expose composable and Vue 3 component for `streaming sessions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-automation-voice.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Interruption** | Expose composable and Vue 3 component for `interruption` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-automation-voice.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Transcripts** | Expose composable and Vue 3 component for `transcripts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-automation-voice.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Consent controls** | Expose composable and Vue 3 component for `consent controls` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-automation-voice.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateVoiceResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-voice/src/Actions/CreateVoiceResource.php) | `public function execute(string $teamId, string $name, array $payload = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): VoiceResource` |
| [TransitionVoiceResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-voice/src/Actions/TransitionVoiceResource.php) | `public function execute(VoiceResource $resource, string $teamId, string $status, array $allowedStatuses = ['draft', 'active', 'paused', 'completed', 'failed', 'cancelled'], ?string $actorId = null, ?string $correlationId = null): VoiceResource` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [VoiceResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-voice/src/Models/VoiceResource.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [VoiceResourceController.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-voice-api/src/Http/Controllers/VoiceResourceController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateVoiceResource $create): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function update(Request $request, string $id): JsonResponse`<br>`public function destroy(Request $request, string $id): JsonResponse`<br>`public function transition(Request $request, string $id, TransitionVoiceResource $transition): JsonResponse` |

**Observed route declarations:**

[modules/module-automation-voice-api/routes/api.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-voice-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:60,1'])->prefix('api/v1/automation/voice')->group(function (): void {
Route::get('/', [VoiceResourceController::class, 'index']);
Route::post('/', [VoiceResourceController::class, 'store']);
Route::get('/{id}', [VoiceResourceController::class, 'show']);
Route::patch('/{id}', [VoiceResourceController::class, 'update']);
Route::delete('/{id}', [VoiceResourceController::class, 'destroy']);
Route::post('/{id}/transition', [VoiceResourceController::class, 'transition']);
```
<!-- layer-implementation-plan:end -->
