# Social Network: Moderation Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#moderation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-social-network-moderation-nuxt`
**Matching domain module:** `social-network-moderation`
**Application:** Social Network
**Source feature:** [Moderation](../features/moderation.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/moderation.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `social-network-moderation` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Reports:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Queues:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Policy/rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Evidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Actions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Appeals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sanctions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transparency:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-social-network-moderation-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `reports`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `queues`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `policy-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `evidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `actions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `appeals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sanctions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transparency`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `social-network-moderation` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-social-network-nuxt-vue`](https://github.com/liberusoftware/project-social-network-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/moderation.md)) |
| Capability Nuxt module skeleton | [`module-social-network-moderation-nuxt`](https://github.com/liberusoftware/module-social-network-moderation-nuxt) (`@liberusoftware/module-social-network-moderation-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Reports** | Expose composable and Vue 3 component for `reports` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Queues** | Expose composable and Vue 3 component for `queues` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Policy/rules** | Expose composable and Vue 3 component for `policy/rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Evidence** | Expose composable and Vue 3 component for `evidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Actions** | Expose composable and Vue 3 component for `actions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Appeals** | Expose composable and Vue 3 component for `appeals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Sanctions** | Expose composable and Vue 3 component for `sanctions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Transparency** | Expose composable and Vue 3 component for `transparency` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateReport.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Actions/CreateReport.php) | `public function __construct(private ModerationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $reporter, string $targetType, string $targetId, string $reason, ?string $details = null): ModerationReport` |
| [DecideReport.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Actions/DecideReport.php) | `public function __construct(private ModerationAuthorizer $authorizer)`<br>`public function handle(Profile $actor, ModerationReport $report, string $action, ?string $reason = null, array $evidence = []): ModerationDecision` |
| [ModerationAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Contracts/ModerationAuthorizer.php) | `public function report(Profile $reporter): void`<br>`public function decide(Profile $actor): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ModerationDecision.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Models/ModerationDecision.php) | `report_id`, `actor_profile_id`, `action`, `reason`, `evidence` |
| [ModerationReport.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Models/ModerationReport.php) | `id`, `reporter_profile_id`, `target_type`, `target_id`, `reason`, `details`, `state`, `assigned_to` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ModerationController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation-api/src/Http/Controllers/ModerationController.php) | `public function report(Request $request, GetProfile $get, CreateReport $create): JsonResponse`<br>`public function decide(string $report, Request $request, GetProfile $get, DecideReport $decide): JsonResponse` |

**Observed route declarations:**

[modules/social-network-moderation-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/moderation')->middleware(['auth:sanctum', 'throttle:30,1'])->name('social-network.moderation.api.')->group(function (): void {
Route::post('/reports', [ModerationController::class, 'report'])->name('report');
Route::post('/reports/{report}/decide', [ModerationController::class, 'decide'])->name('decide');
```
<!-- layer-implementation-plan:end -->
