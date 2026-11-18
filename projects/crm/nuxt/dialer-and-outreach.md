# CRM: Dialer and Outreach Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#dialer-and-outreach). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-dialer-and-outreach-nuxt`
**Matching domain module:** `crm-dialer-and-outreach`
**Application:** CRM
**Source feature:** [Dialer and Outreach](../features/dialer-and-outreach.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/dialer-and-outreach.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-dialer-and-outreach` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Power/preview/progressive dialing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Prioritized lists:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Scripts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Local-time policy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Retries:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Voicemail drop:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Answer detection adapters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Outcomes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Compliance controls:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-dialer-and-outreach-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `power-preview-progressive-dialing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `prioritized-lists`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `scripts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `local-time-policy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `retries`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `voicemail-drop`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `answer-detection-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `outcomes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `compliance-controls`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-dialer-and-outreach` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/dialer-and-outreach.md)) |
| Capability Nuxt module skeleton | [`module-crm-dialer-and-outreach-nuxt`](https://github.com/liberusoftware/module-crm-dialer-and-outreach-nuxt) (`@liberusoftware/module-crm-dialer-and-outreach-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Power/preview/progressive dialing** | Expose composable and Vue 3 component for `power/preview/progressive dialing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/dialer-and-outreach.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Prioritized lists** | Expose composable and Vue 3 component for `prioritized lists` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/dialer-and-outreach.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Scripts** | Expose composable and Vue 3 component for `scripts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/dialer-and-outreach.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Local-time policy** | Expose composable and Vue 3 component for `local-time policy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/dialer-and-outreach.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Retries** | Expose composable and Vue 3 component for `retries` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/dialer-and-outreach.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Voicemail drop** | Expose composable and Vue 3 component for `voicemail drop` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/dialer-and-outreach.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Answer detection adapters** | Expose composable and Vue 3 component for `answer detection adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/dialer-and-outreach.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Outcomes** | Expose composable and Vue 3 component for `outcomes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/dialer-and-outreach.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Compliance controls** | Expose composable and Vue 3 component for `compliance controls` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/dialer-and-outreach.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DialerQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Queries/DialerQuery.php) | `public function lists(int $teamId)`<br>`public function calls(int $teamId, int $listId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDialerList.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Actions/CreateDialerList.php) | `public function __construct(private readonly DialerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): DialerList` |
| [QueueDialerCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Actions/QueueDialerCall.php) | `public function __construct(private readonly DialerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, DialerList $list, array $input): DialerCall` |
| [RecordCallOutcome.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Actions/RecordCallOutcome.php) | `public function execute(int $teamId, int $userId, DialerCall $call, array $input): DialerEvent` |
| [RetryDialerCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Actions/RetryDialerCall.php) | `public function execute(int $teamId, DialerCall $call, int $maxAttempts = 3): DialerCall` |
| [DialerPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Services/DialerPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DialerCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Models/DialerCall.php) | No literal fillable array detected; inspect the model and API schema. |
| [DialerEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Models/DialerEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [DialerList.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Models/DialerList.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [DialerController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach-api/src/Http/Controllers/DialerController.php) | `public function __construct(private readonly DialerQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateDialerList $action): JsonResponse`<br>`public function queue(DialerList $list, QueueDialerCall $action): JsonResponse`<br>`public function outcome(DialerCall $call, RecordCallOutcome $action): JsonResponse`<br>`public function retry(DialerCall $call, RetryDialerCall $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-dialer-and-outreach-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/dialer-and-outreach')->group(function (): void {
Route::get('lists', [DialerController::class, 'index']);
Route::post('lists', [DialerController::class, 'store']);
Route::post('lists/{list}/calls', [DialerController::class, 'queue']);
Route::post('calls/{call}/outcome', [DialerController::class, 'outcome']);
Route::post('calls/{call}/retry', [DialerController::class, 'retry']);
```
<!-- layer-implementation-plan:end -->
