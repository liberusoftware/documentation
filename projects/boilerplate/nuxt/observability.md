# Boilerplate: Observability Nuxt presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#observability). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-observability-nuxt`
**Matching core package:** [`module-observability`](../core/observability.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Structured logs, correlation, metrics, traces, exception reporting, health checks, redaction, and SLO hooks.

## Adapter implementation plan

This package presents the Observability core capability through Nuxt 4. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Consume the versioned API contract or approved server boundary; keep client state and views replaceable, typed, accessible, and resilient to partial failure.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Observability core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/observability.md)) |
| Capability Nuxt module skeleton | [`module-observability-nuxt`](https://github.com/liberusoftware/module-observability-nuxt) (`@liberusoftware/module-observability-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Structured logs** | Expose composable and Vue 3 component for `structured logs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Correlation** | Expose composable and Vue 3 component for `correlation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Metrics** | Expose composable and Vue 3 component for `metrics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Traces** | Expose composable and Vue 3 component for `traces` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Exception reporting** | Expose composable and Vue 3 component for `exception reporting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Health checks** | Expose composable and Vue 3 component for `health checks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Redaction** | Expose composable and Vue 3 component for `redaction` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **SLO hooks** | Expose composable and Vue 3 component for `slo hooks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/observability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

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
