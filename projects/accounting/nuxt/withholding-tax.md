# Accounting: Withholding Tax Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#withholding-tax). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-withholding-tax-nuxt`
**Matching domain module:** `accounting-withholding-tax`
**Application:** Accounting
**Source feature:** [Withholding Tax](../features/withholding-tax.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/withholding-tax.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-withholding-tax` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Certificates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Supplier/customer deductions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Liabilities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Remittance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Statements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Regional filing adapters:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-withholding-tax-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `certificates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `supplier-customer-deductions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `liabilities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `remittance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `statements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `regional-filing-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-withholding-tax` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/withholding-tax.md)) |
| Capability Nuxt module skeleton | [`module-accounting-withholding-tax-nuxt`](https://github.com/liberusoftware/module-accounting-withholding-tax-nuxt) (`@liberusoftware/module-accounting-withholding-tax-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Rules** | Expose composable and Vue 3 component for `rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/withholding-tax.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Certificates** | Expose composable and Vue 3 component for `certificates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/withholding-tax.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Supplier/customer deductions** | Expose composable and Vue 3 component for `supplier/customer deductions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/withholding-tax.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Liabilities** | Expose composable and Vue 3 component for `liabilities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/withholding-tax.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Remittance** | Expose composable and Vue 3 component for `remittance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/withholding-tax.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Statements** | Expose composable and Vue 3 component for `statements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/withholding-tax.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Regional filing adapters** | Expose composable and Vue 3 component for `regional filing adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/withholding-tax.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CalculateWithholdingTax.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/CalculateWithholdingTax.php) | `public function handle(WithholdingTaxRule $rule, array $attributes): WithholdingTaxDeduction` |
| [CreateWithholdingTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/CreateWithholdingTaxRule.php) | `public function handle(array $attributes): WithholdingTaxRule` |
| [RemitWithholdingTax.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/RemitWithholdingTax.php) | `public function handle(WithholdingTaxLiability $liability, array $attributes): WithholdingTaxRemittance` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WithholdingTaxCertificate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxCertificate.php) | `team_id`, `rule_id`, `party_type`, `party_id`, `certificate_ref`, `valid_from`, `valid_until`, `status`, `metadata` |
| [WithholdingTaxDeduction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxDeduction.php) | `team_id`, `rule_id`, `party_type`, `party_id`, `source_ref`, `currency`, `gross_amount`, `withheld_amount`, `status`, `metadata` |
| [WithholdingTaxFilingAdapter.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxFilingAdapter.php) | `team_id`, `jurisdiction`, `provider`, `status`, `configuration` |
| [WithholdingTaxLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxLiability.php) | `team_id`, `deduction_id`, `amount`, `due_on`, `status`, `metadata` |
| [WithholdingTaxRemittance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxRemittance.php) | `team_id`, `liability_id`, `amount`, `remitted_on`, `reference`, `status`, `metadata` |
| [WithholdingTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxRule.php) | `team_id`, `code`, `name`, `jurisdiction`, `rate`, `threshold`, `effective_from`, `effective_until`, `status`, `metadata` |
| [WithholdingTaxStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxStatement.php) | `team_id`, `jurisdiction`, `period_start`, `period_end`, `total_amount`, `status`, `payload` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WithholdingTaxController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax-api/src/Http/Controllers/WithholdingTaxController.php) | `public function rules(Request $request): mixed`<br>`public function deductions(Request $request): mixed`<br>`public function createRule(Request $request, CreateWithholdingTaxRule $action): mixed`<br>`public function calculate(Request $request, WithholdingTaxRule $rule, CalculateWithholdingTax $action): mixed`<br>`public function remit(Request $request, WithholdingTaxLiability $liability, RemitWithholdingTax $action): mixed` |

**Observed route declarations:**

[modules/accounting-withholding-tax-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/withholding-tax')->group(function (): void {
Route::middleware('ability:accounting.withholding-tax.read')->group(function (): void {
Route::get('/rules', [WithholdingTaxController::class, 'rules']);
Route::get('/deductions', [WithholdingTaxController::class, 'deductions']);
Route::middleware('ability:accounting.withholding-tax.write')->group(function (): void {
Route::post('/rules', [WithholdingTaxController::class, 'createRule']);
Route::post('/rules/{rule}/deductions', [WithholdingTaxController::class, 'calculate']);
Route::post('/liabilities/{liability}/remit', [WithholdingTaxController::class, 'remit']);
```
<!-- layer-implementation-plan:end -->
