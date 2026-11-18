# Maintenance: Application Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#application). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-maintenance-application-nuxt`
**Matching domain module:** `application`
**Application:** Maintenance
**Source feature:** [Application](../features/application.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/application.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `application` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Environment validation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Application metadata:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Health/readiness:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Maintenance mode:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Identifiers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Clocks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Shared service contracts:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-application-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `environment-validation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `application-metadata`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `health-readiness`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `maintenance-mode`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `identifiers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `clocks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `shared-service-contracts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `application` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/application.md)) |
| Capability Nuxt module skeleton | [`module-application-nuxt`](https://github.com/liberusoftware/module-application-nuxt) (`@liberusoftware/module-application-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Environment validation** | Expose composable and Vue 3 component for `environment validation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/application.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Application metadata** | Expose composable and Vue 3 component for `application metadata` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/application.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Health/readiness** | Expose composable and Vue 3 component for `health/readiness` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/application.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Maintenance mode** | Expose composable and Vue 3 component for `maintenance mode` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/application.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Identifiers** | Expose composable and Vue 3 component for `identifiers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/application.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Clocks** | Expose composable and Vue 3 component for `clocks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/application.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Shared service contracts** | Expose composable and Vue 3 component for `shared service contracts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/application.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [Clock.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Contracts/Clock.php) | `public function now(): \DateTimeImmutable` |
| [IdentifierFactory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Contracts/IdentifierFactory.php) | `public function make(): string` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReadinessController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Http/Controllers/ReadinessController.php) | `public function __invoke(ReadinessRegistry $registry): JsonResponse` |

**Observed route declarations:**

[modules/application/routes/health.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/application/routes/health.php)

```php
Route::get('/ready', ReadinessController::class)->name('application.ready');
```
<!-- layer-implementation-plan:end -->
