# CMS: Cms Hello Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-hello). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-cms-hello-nuxt`
**Matching domain module:** `cms-hello`
**Application:** CMS
**Source feature:** [Cms Hello](../features/cms-hello.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/cms-hello.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-hello` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Starter module manifest verification:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Service provider and route registration check:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sample authorized query and action boundary:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Theme default view resolution smoke check:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Package testbench verification:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-cms-hello-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `starter-module-manifest-verification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `service-provider-and-route-registration-check`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sample-authorized-query-and-action-boundary`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `theme-default-view-resolution-smoke-check`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `package-testbench-verification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-hello` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-hello.md)) |
| Capability Nuxt module skeleton | [`module-cms-hello-nuxt`](https://github.com/liberusoftware/module-cms-hello-nuxt) (`@liberusoftware/module-cms-hello-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Starter module manifest verification** | Expose composable and Vue 3 component for `starter module manifest verification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-hello.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Service provider and route registration check** | Expose composable and Vue 3 component for `service provider and route registration check` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-hello.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Sample authorized query and action boundary** | Expose composable and Vue 3 component for `sample authorized query and action boundary` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-hello.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Theme default view resolution smoke check** | Expose composable and Vue 3 component for `theme default view resolution smoke check` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-hello.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Package testbench verification** | Expose composable and Vue 3 component for `package testbench verification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-hello.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GreeterInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-hello/src/Contracts/GreeterInterface.php) | `public function greet(string $name): string` |
| [Greeter.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-hello/src/Services/Greeter.php) | `public function __construct(private string $template)`<br>`public function greet(string $name): string` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Greeting.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-hello/src/Models/Greeting.php) | `name`, `message` |

| Observed API controller | Handler signatures |
| --- | --- |
| [GreetingApiController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-hello/src/Http/Controllers/GreetingApiController.php) | `public function index(): AnonymousResourceCollection` |
| [HelloController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-hello/src/Http/Controllers/HelloController.php) | `public function __construct( private GreeterInterface $greeter, private EventBusInterface $events, )`<br>`public function __invoke(string $name = 'world'): JsonResponse` |

**Observed route declarations:**

[modules/cms-hello/routes/api.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-hello/routes/api.php)

```php
Route::get('api/v1/hello/{name?}', HelloController::class)->name('cms.hello.greet');
```
<!-- layer-implementation-plan:end -->
