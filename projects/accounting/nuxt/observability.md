# Accounting: Observability Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#observability). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-observability-nuxt`
**Matching domain module:** `observability`
**Application:** Accounting
**Source feature:** [Observability](../features/observability.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/observability.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `observability` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Structured logs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Correlation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Metrics:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Traces:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exception reporting:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Health checks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Redaction:** page/component/composable/API-action behavior for this module's authorized workflow.
- **SLO hooks:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-observability-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `structured-logs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `correlation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `metrics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `traces`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exception-reporting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `health-checks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `redaction`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `slo-hooks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `observability` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/observability.md)) |
| Capability Nuxt module skeleton | [`module-observability-nuxt`](https://github.com/liberusoftware/module-observability-nuxt) (`@liberusoftware/module-observability-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Structured logs** | Expose composable and Vue 3 component for `structured logs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Correlation** | Expose composable and Vue 3 component for `correlation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Metrics** | Expose composable and Vue 3 component for `metrics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Traces** | Expose composable and Vue 3 component for `traces` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Exception reporting** | Expose composable and Vue 3 component for `exception reporting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Health checks** | Expose composable and Vue 3 component for `health checks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Redaction** | Expose composable and Vue 3 component for `redaction` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **SLO hooks** | Expose composable and Vue 3 component for `slo hooks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [Metrics.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/observability/src/Contracts/Metrics.php) | `public function increment(string $name, int $value = 1, array $labels = []): void`<br>`public function observe(string $name, float $value, array $labels = []): void` |
| [ObservabilityActor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/observability/src/Contracts/ObservabilityActor.php) | `public function isAdmin(): bool` |

**Observed route declarations:**

[modules/observability-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/observability-api/routes/api.php)

```php
Route::prefix('api/v1/observability')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('observability-api.status');
```
<!-- layer-implementation-plan:end -->
