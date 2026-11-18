# Accounting: Tax Returns Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#tax-returns). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-tax-returns-nuxt`
**Matching domain module:** `accounting-tax-returns`
**Application:** Accounting
**Source feature:** [Tax Returns](../features/tax-returns.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/tax-returns.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-tax-returns` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Return preparation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Source reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Diagnostics:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Review:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approval:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Submission adapter:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Receipt/status:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payment:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Amendments:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-tax-returns-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `return-preparation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `source-reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `diagnostics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `review`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `submission-adapter`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `receipt-status`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payment`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `amendments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-tax-returns` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/tax-returns.md)) |
| Capability Nuxt module skeleton | [`module-accounting-tax-returns-nuxt`](https://github.com/liberusoftware/module-accounting-tax-returns-nuxt) (`@liberusoftware/module-accounting-tax-returns-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Return preparation** | Expose composable and Vue 3 component for `return preparation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/tax-returns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Source reconciliation** | Expose composable and Vue 3 component for `source reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/tax-returns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Diagnostics** | Expose composable and Vue 3 component for `diagnostics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/tax-returns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Review** | Expose composable and Vue 3 component for `review` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/tax-returns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approval** | Expose composable and Vue 3 component for `approval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/tax-returns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Submission adapter** | Expose composable and Vue 3 component for `submission adapter` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/tax-returns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Receipt/status** | Expose composable and Vue 3 component for `receipt/status` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/tax-returns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Payment** | Expose composable and Vue 3 component for `payment` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/tax-returns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Amendments** | Expose composable and Vue 3 component for `amendments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/tax-returns.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AmendTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Actions/AmendTaxReturn.php) | `public function handle(TaxReturn $taxReturn): TaxReturn` |
| [CreateTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Actions/CreateTaxReturn.php) | `public function handle(array $attributes): TaxReturn` |
| [SubmitTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Actions/SubmitTaxReturn.php) | `public function handle(TaxReturn $taxReturn, string $externalReference): TaxReturn` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Models/TaxReturn.php) | `team_id`, `tax_type`, `jurisdiction`, `period_start`, `period_end`, `due_on`, `status`, `external_reference`, `submitted_at`, `metadata` |
| [TaxReturnLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns/src/Models/TaxReturnLine.php) | `team_id`, `tax_return_id`, `code`, `amount`, `currency`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TaxReturnsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns-api/src/Http/Controllers/TaxReturnsController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateTaxReturn $action): mixed`<br>`public function submit(Request $request, string $taxReturn, SubmitTaxReturn $action): mixed`<br>`public function amend(Request $request, string $taxReturn, AmendTaxReturn $action): mixed` |

**Observed route declarations:**

[modules/accounting-tax-returns-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-returns-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/tax-returns')->middleware(['auth:sanctum'])->group(function (): void {
Route::get('/', [TaxReturnsController::class, 'index'])->middleware('ability:accounting.tax-returns.read');
Route::post('/', [TaxReturnsController::class, 'store'])->middleware('ability:accounting.tax-returns.write');
Route::post('/{taxReturn}/submit', [TaxReturnsController::class, 'submit'])->middleware('ability:accounting.tax-returns.write');
Route::post('/{taxReturn}/amend', [TaxReturnsController::class, 'amend'])->middleware('ability:accounting.tax-returns.write');
```
<!-- layer-implementation-plan:end -->
