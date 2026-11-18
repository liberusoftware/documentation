# Accounting: Transfers Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#transfers). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-transfers-nuxt`
**Matching domain module:** `accounting-transfers`
**Application:** Accounting
**Source feature:** [Transfers](../features/transfers.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/transfers.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-transfers` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Inter-account/entity transfers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Currency conversion:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fees:** page/component/composable/API-action behavior for this module's authorized workflow.
- **In-transit state:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Paired posting:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-transfers-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `inter-account-entity-transfers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `currency-conversion`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fees`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `in-transit-state`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `paired-posting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-transfers` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/transfers.md)) |
| Capability Nuxt module skeleton | [`module-accounting-transfers-nuxt`](https://github.com/liberusoftware/module-accounting-transfers-nuxt) (`@liberusoftware/module-accounting-transfers-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Inter-account/entity transfers** | Expose composable and Vue 3 component for `inter-account/entity transfers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/transfers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Currency conversion** | Expose composable and Vue 3 component for `currency conversion` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/transfers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Fees** | Expose composable and Vue 3 component for `fees` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/transfers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **In-transit state** | Expose composable and Vue 3 component for `in-transit state` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/transfers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Paired posting** | Expose composable and Vue 3 component for `paired posting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/transfers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/transfers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CompleteTransfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Actions/CompleteTransfer.php) | `public function handle(Transfer $transfer): Transfer` |
| [CreateTransfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Actions/CreateTransfer.php) | `public function handle(array $attributes): Transfer` |
| [ReconcileTransfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Actions/ReconcileTransfer.php) | `public function handle(Transfer $transfer, array $attributes): TransferReconciliation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Transfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Models/Transfer.php) | `team_id`, `source_account_ref`, `destination_account_ref`, `source_currency`, `destination_currency`, `source_amount`, `destination_amount`, `exchange_rate`, `fee_amount`, `status`, `reference`, `metadata` |
| [TransferReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Models/TransferReconciliation.php) | `team_id`, `transfer_id`, `external_ref`, `amount`, `reconciled_on`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TransfersController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers-api/src/Http/Controllers/TransfersController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateTransfer $action): mixed`<br>`public function complete(Request $request, string $transfer, CompleteTransfer $action): mixed`<br>`public function reconcile(Request $request, string $transfer, ReconcileTransfer $action): mixed` |

**Observed route declarations:**

[modules/accounting-transfers-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/transfers')->middleware(['auth:sanctum'])->group(function (): void {
Route::get('/', [TransfersController::class, 'index'])->middleware('ability:accounting.transfers.read');
Route::post('/', [TransfersController::class, 'store'])->middleware('ability:accounting.transfers.write');
Route::post('/{transfer}/complete', [TransfersController::class, 'complete'])->middleware('ability:accounting.transfers.write');
Route::post('/{transfer}/reconcile', [TransfersController::class, 'reconcile'])->middleware('ability:accounting.transfers.write');
```
<!-- layer-implementation-plan:end -->
