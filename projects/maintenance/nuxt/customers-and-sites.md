# Maintenance: Customers and Sites Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customers-and-sites). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-maintenance-customers-and-sites-nuxt`
**Matching domain module:** `maintenance-customers-and-sites`
**Application:** Maintenance
**Source feature:** [Customers and Sites](../features/customers-and-sites.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/customers-and-sites.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `maintenance-customers-and-sites` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Contacts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sites:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Locations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Access details:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Hazards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Service windows:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-customers-and-sites-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `customers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `contacts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sites`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `locations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `access-details`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `hazards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `service-windows`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `maintenance-customers-and-sites` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/customers-and-sites.md)) |
| Capability Nuxt module skeleton | [`module-maintenance-customers-and-sites-nuxt`](https://github.com/liberusoftware/module-maintenance-customers-and-sites-nuxt) (`@liberusoftware/module-maintenance-customers-and-sites-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Customers** | Expose composable and Vue 3 component for `customers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customers-and-sites.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Contacts** | Expose composable and Vue 3 component for `contacts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customers-and-sites.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Sites** | Expose composable and Vue 3 component for `sites` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customers-and-sites.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Locations** | Expose composable and Vue 3 component for `locations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customers-and-sites.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Access details** | Expose composable and Vue 3 component for `access details` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customers-and-sites.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Hazards** | Expose composable and Vue 3 component for `hazards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customers-and-sites.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Service windows** | Expose composable and Vue 3 component for `service windows` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/customers-and-sites.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCustomer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/CreateCustomer.php) | `public function handle(int $teamId, array $attributes): Customer` |
| [CreateSite.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/CreateSite.php) | `public function handle(int $teamId, array $attributes): Site` |
| [DeleteCustomer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/DeleteCustomer.php) | `public function handle(int $teamId, Customer $customer): void` |
| [DeleteSite.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/DeleteSite.php) | `public function handle(int $teamId, Site $site): void` |
| [UpdateCustomer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/UpdateCustomer.php) | `public function handle(int $teamId, Customer $customer, array $attributes): Customer` |
| [UpdateSite.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/UpdateSite.php) | `public function handle(int $teamId, Site $site, array $attributes): Site` |
| [CustomerPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Policies/CustomerPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Customer $customer): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Customer $customer): bool`<br>`public function delete(object $user, Customer $customer): bool` |
| [SitePolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Policies/SitePolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Site $site): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Site $site): bool`<br>`public function delete(object $user, Site $site): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Customer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Models/Customer.php) | `team_id`, `name`, `code`, `email`, `phone`, `address`, `city`, `state`, `zip`, `website`, `industry`, `description`, `type`, `contact_person`, `payment_terms`, `notes`, `is_active` |
| [Site.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Models/Site.php) | `team_id`, `customer_id`, `name`, `code`, `address`, `access_details`, `hazards`, `is_active` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CustomersAndSitesController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-api/src/Http/Controllers/CustomersAndSitesController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateCustomer $create): JsonResponse`<br>`public function show(Request $request, Customer $customer): JsonResponse`<br>`public function update(Request $request, Customer $customer, UpdateCustomer $update): JsonResponse`<br>`public function destroy(Request $request, Customer $customer, DeleteCustomer $delete): JsonResponse`<br>`public function sites(Request $request): JsonResponse`<br>`public function storeSite(Request $request, CreateSite $create): JsonResponse`<br>`public function updateSite(Request $request, Site $site, UpdateSite $update): JsonResponse`<br>`public function destroySite(Request $request, Site $site, DeleteSite $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-customers-and-sites-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/customers-and-sites')->group(function (): void {
Route::get('/', [CustomersAndSitesController::class, 'index']);
Route::post('/', [CustomersAndSitesController::class, 'store']);
Route::get('/sites', [CustomersAndSitesController::class, 'sites']);
Route::post('/sites', [CustomersAndSitesController::class, 'storeSite']);
Route::patch('/sites/{site}', [CustomersAndSitesController::class, 'updateSite']);
Route::delete('/sites/{site}', [CustomersAndSitesController::class, 'destroySite']);
Route::get('/{customer}', [CustomersAndSitesController::class, 'show']);
Route::patch('/{customer}', [CustomersAndSitesController::class, 'update']);
Route::delete('/{customer}', [CustomersAndSitesController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
