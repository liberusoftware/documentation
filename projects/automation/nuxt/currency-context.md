# Automation: Currency Context Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#currency-context). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-automation-currency-context-nuxt`
**Matching domain module:** `currency-context`
**Application:** Automation
**Source feature:** [Currency Context](../features/currency-context.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/currency-context.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `currency-context` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Currency metadata:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Preferences:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Precision:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Formatting:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exchange-rate contracts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Context:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-automation-currency-context-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `currency-metadata`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `preferences`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `precision`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `formatting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exchange-rate-contracts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `context`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `currency-context` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-automation-nuxt-vue`](https://github.com/liberusoftware/project-automation-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-automation-laravel-api`](https://github.com/liberusoftware/project-automation-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/currency-context.md)) |
| Capability Nuxt module skeleton | [`module-currency-context-nuxt`](https://github.com/liberusoftware/module-currency-context-nuxt) (`@liberusoftware/module-currency-context-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Currency metadata** | Expose composable and Vue 3 component for `currency metadata` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/currency-context.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Preferences** | Expose composable and Vue 3 component for `preferences` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/currency-context.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Precision** | Expose composable and Vue 3 component for `precision` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/currency-context.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Formatting** | Expose composable and Vue 3 component for `formatting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/currency-context.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Exchange-rate contracts** | Expose composable and Vue 3 component for `exchange-rate contracts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/currency-context.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Context** | Expose composable and Vue 3 component for `context` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/currency-context.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ExchangeRateProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/currency-context/src/Contracts/ExchangeRateProvider.php) | `public function rate(Currency $base, Currency $quote, DateTimeImmutable $effectiveAt): ?ExchangeRate` |
| [CurrencyContext.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/currency-context/src/Services/CurrencyContext.php) | `public function __construct(private array $currencies)`<br>`public function for(CurrencyRole $role): Currency` |
| [CurrencyPreferenceResolver.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/currency-context/src/Services/CurrencyPreferenceResolver.php) | `public function resolve(array $scopes, string $fallback): string` |
| [CurrencyRegistry.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/currency-context/src/Services/CurrencyRegistry.php) | `public function __construct(private array $definitions)`<br>`public function get(string $code): Currency` |
| [MoneyFormatter.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/currency-context/src/Services/MoneyFormatter.php) | `public function __construct(private readonly ?Closure $formatterFactory = null)`<br>`public function format(Money $money, string $locale): string` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Currency.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/currency-context/src/Models/Currency.php) | No literal fillable array detected; inspect the model and API schema. |

**Observed route declarations:**

[modules/currency-context-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/currency-context-api/routes/api.php)

```php
Route::prefix('api/v1/currency-context')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('currency-context-api.status');
```
<!-- layer-implementation-plan:end -->
