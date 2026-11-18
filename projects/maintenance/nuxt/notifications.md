# Maintenance: Notifications Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#notifications). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-maintenance-notifications-nuxt`
**Matching domain module:** `notifications`
**Application:** Maintenance
**Source feature:** [Notifications](../features/notifications.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/notifications.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `notifications` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Channels:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Preferences:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Inbox:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delivery status:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Retries:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quiet hours:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Localization:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-notifications-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `channels`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `preferences`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `inbox`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delivery-status`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `retries`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quiet-hours`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `localization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `notifications` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/notifications.md)) |
| Capability Nuxt module skeleton | [`module-notifications-nuxt`](https://github.com/liberusoftware/module-notifications-nuxt) (`@liberusoftware/module-notifications-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Templates** | Expose composable and Vue 3 component for `templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/notifications.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Channels** | Expose composable and Vue 3 component for `channels` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/notifications.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Preferences** | Expose composable and Vue 3 component for `preferences` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/notifications.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Inbox** | Expose composable and Vue 3 component for `inbox` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/notifications.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Delivery status** | Expose composable and Vue 3 component for `delivery status` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/notifications.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Retries** | Expose composable and Vue 3 component for `retries` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/notifications.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Quiet hours** | Expose composable and Vue 3 component for `quiet hours` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/notifications.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Localization** | Expose composable and Vue 3 component for `localization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/notifications.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |

### Observed domain and transport source evidence

**Observed route declarations:**

[modules/notifications-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/notifications-api/routes/api.php)

```php
Route::prefix('api/v1/notifications')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('notifications-api.status');
```

[modules/social-network-notifications-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/notifications')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.notifications.api.')->group(function (): void {
Route::get('/', [NotificationsController::class, 'index'])->name('index');
Route::get('/unread-count', [NotificationsController::class, 'unreadCount'])->name('unread-count');
Route::post('/read-all', [NotificationsController::class, 'readAll'])->name('read-all');
Route::patch('/preferences', [NotificationsController::class, 'preferences'])->name('preferences');
Route::post('/{notification}/read', [NotificationsController::class, 'read'])->name('read');
Route::post('/{notification}/dismiss', [NotificationsController::class, 'dismiss'])->name('dismiss');
```
<!-- layer-implementation-plan:end -->
