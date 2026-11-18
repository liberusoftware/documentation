# Maintenance: Developer Experience Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#developer-experience). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-maintenance-developer-experience-nuxt`
**Matching domain module:** `developer-experience`
**Application:** Maintenance
**Source feature:** [Developer Experience](../features/developer-experience.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/developer-experience.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `developer-experience` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Local setup:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fixtures:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Factories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quality scripts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **CI:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Architecture tests:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Docs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Upgrade automation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-developer-experience-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `local-setup`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fixtures`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `factories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quality-scripts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ci`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `architecture-tests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `docs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `upgrade-automation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `developer-experience` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/developer-experience.md)) |
| Capability Nuxt module skeleton | [`module-developer-experience-nuxt`](https://github.com/liberusoftware/module-developer-experience-nuxt) (`@liberusoftware/module-developer-experience-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Local setup** | Expose composable and Vue 3 component for `local setup` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/developer-experience.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Fixtures** | Expose composable and Vue 3 component for `fixtures` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/developer-experience.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Factories** | Expose composable and Vue 3 component for `factories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/developer-experience.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Quality scripts** | Expose composable and Vue 3 component for `quality scripts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/developer-experience.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **CI** | Expose composable and Vue 3 component for `ci` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/developer-experience.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Architecture tests** | Expose composable and Vue 3 component for `architecture tests` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/developer-experience.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Docs** | Expose composable and Vue 3 component for `docs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/developer-experience.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Upgrade automation** | Expose composable and Vue 3 component for `upgrade automation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/developer-experience.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |

### Observed domain and transport source evidence

**Observed route declarations:**

[modules/developer-experience-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/developer-experience-api/routes/api.php)

```php
Route::prefix('api/v1/developer-experience')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('developer-experience-api.status');
```
<!-- layer-implementation-plan:end -->
