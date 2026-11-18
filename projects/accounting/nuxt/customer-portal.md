# Accounting: Customer Portal Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customer-portal). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-customer-portal-nuxt`
**Matching domain module:** `accounting-customer-portal`
**Application:** Accounting
**Source feature:** [Customer Portal](../features/customer-portal.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/customer-portal.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-customer-portal` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Estimates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Invoices:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Credits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Statements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payment links:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payment history:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Disputes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Documents:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Communication preferences:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-customer-portal-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `estimates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `invoices`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `credits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `statements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payment-links`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payment-history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `disputes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `documents`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `communication-preferences`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-customer-portal` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/customer-portal.md)) |
| Capability Nuxt module skeleton | [`module-accounting-customer-portal-nuxt`](https://github.com/liberusoftware/module-accounting-customer-portal-nuxt) (`@liberusoftware/module-accounting-customer-portal-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Estimates** | Expose composable and Vue 3 component for `estimates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Invoices** | Expose composable and Vue 3 component for `invoices` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Credits** | Expose composable and Vue 3 component for `credits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Statements** | Expose composable and Vue 3 component for `statements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Payment links** | Expose composable and Vue 3 component for `payment links` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Payment history** | Expose composable and Vue 3 component for `payment history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Disputes** | Expose composable and Vue 3 component for `disputes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Documents** | Expose composable and Vue 3 component for `documents` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Communication preferences** | Expose composable and Vue 3 component for `communication preferences` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customer-portal.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CustomerPortalQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-portal/src/Queries/CustomerPortalQuery.php) | `public function forTeam(int $teamId): Collection`<br>`public function forCustomer(int $teamId, string $customerId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCustomerPortalRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-portal/src/Actions/CreateCustomerPortalRecord.php) | `public function handle(array $attributes): CustomerPortalRecord` |
| [PublishCustomerPortalRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-portal/src/Actions/PublishCustomerPortalRecord.php) | `public function handle(CustomerPortalRecord $record): CustomerPortalRecord` |
| [ResolveCustomerPortalDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-portal/src/Actions/ResolveCustomerPortalDispute.php) | `public function handle(CustomerPortalRecord $record, array $resolution): CustomerPortalRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CustomerPortalRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-portal/src/Models/CustomerPortalRecord.php) | `team_id`, `customer_id`, `type`, `reference`, `status`, `currency`, `amount`, `payload`, `metadata`, `published_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CustomerPortalController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-portal-api/src/Http/Controllers/CustomerPortalController.php) | `public function index(CustomerPortalQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCustomerPortalRecord $action): JsonResponse`<br>`public function publish(Request $request, string $record, PublishCustomerPortalRecord $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-customer-portal-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-portal-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/customer-portal')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.customer-portal.read')->get('/', [CustomerPortalController::class, 'index']);
Route::middleware('ability:accounting.customer-portal.write')->group(function (): void {
Route::post('/', [CustomerPortalController::class, 'store']);
Route::post('/{record}/publish', [CustomerPortalController::class, 'publish']);
```
<!-- layer-implementation-plan:end -->
