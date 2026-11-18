# Accounting: Accounting Tax Core Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-tax-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-tax-core-nuxt`
**Matching domain module:** `accounting-tax-core`
**Application:** Accounting
**Source feature:** [Accounting Tax Core](../features/accounting-tax-core.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-tax-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-tax-core` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Tax types/codes/rates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Inclusive/exclusive treatment:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Jurisdictions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Effective dates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exemptions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rounding:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Evidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Control accounts:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-tax-core-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `tax-types-codes-rates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `inclusive-exclusive-treatment`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `jurisdictions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `effective-dates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exemptions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rounding`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `evidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `control-accounts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-tax-core` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-tax-core.md)) |
| Capability Nuxt module skeleton | [`module-accounting-tax-core-nuxt`](https://github.com/liberusoftware/module-accounting-tax-core-nuxt) (`@liberusoftware/module-accounting-tax-core-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Tax types/codes/rates** | Expose composable and Vue 3 component for `tax types/codes/rates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-tax-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Inclusive/exclusive treatment** | Expose composable and Vue 3 component for `inclusive/exclusive treatment` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-tax-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Jurisdictions** | Expose composable and Vue 3 component for `jurisdictions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-tax-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Effective dates** | Expose composable and Vue 3 component for `effective dates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-tax-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Exemptions** | Expose composable and Vue 3 component for `exemptions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-tax-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Rounding** | Expose composable and Vue 3 component for `rounding` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-tax-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Evidence** | Expose composable and Vue 3 component for `evidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-tax-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Control accounts** | Expose composable and Vue 3 component for `control accounts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-tax-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ActiveTaxRuleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Queries/ActiveTaxRuleQuery.php) | `public function handle(string $code, ?string $jurisdiction = null, ?string $on = null): ?TaxRule` |
| [TaxRuleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Queries/TaxRuleQuery.php) | `public function paginate(?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/ActivateTaxRule.php) | `public function handle(TaxRule $rule): TaxRule` |
| [ArchiveTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/ArchiveTaxRule.php) | `public function handle(TaxRule $rule): TaxRule` |
| [CalculateTax.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/CalculateTax.php) | `public function handle(TaxRule $rule, float $amount): array` |
| [CaptureTaxEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/CaptureTaxEvidence.php) | `public function handle(TaxRule $rule, string $sourceType, string $sourceId, array $snapshot, ?int $actorId = null): TaxEvidence` |
| [CreateTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/CreateTaxRule.php) | `public function handle(array $attributes): TaxRule` |
| [UpdateTaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Actions/UpdateTaxRule.php) | `public function handle(TaxRule $rule, array $attributes): TaxRule` |
| [TaxCorePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core-api/src/Policies/TaxCorePolicy.php) | `public function viewAny($user): bool`<br>`public function view($user, TaxRule $rule): bool`<br>`public function create($user): bool`<br>`public function update($user, TaxRule $rule): bool`<br>`public function delete($user, TaxRule $rule): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TaxEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Models/TaxEvidence.php) | `tax_rule_id`, `source_type`, `source_id`, `snapshot_hash`, `snapshot`, `captured_by`, `metadata` |
| [TaxRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core/src/Models/TaxRule.php) | `code`, `name`, `tax_type`, `jurisdiction_code`, `rate`, `treatment`, `effective_from`, `effective_until`, `status`, `exemption_code`, `control_account_code`, `rounding_method`, `rounding_scale`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TaxRuleController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core-api/src/Http/Controllers/TaxRuleController.php) | `public function index(Request $request): mixed`<br>`public function show(TaxRule $taxRule): TaxRuleResource`<br>`public function store(Request $request, CreateTaxRule $action): mixed`<br>`public function update(Request $request, TaxRule $taxRule, UpdateTaxRule $action): TaxRuleResource`<br>`public function activate(TaxRule $taxRule, ActivateTaxRule $action): TaxRuleResource`<br>`public function archive(TaxRule $taxRule, ArchiveTaxRule $action): TaxRuleResource` |

**Observed route declarations:**

[modules/accounting-tax-core-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-tax-core-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/tax-core')->group(function (): void {
Route::middleware('ability:accounting.tax-core.read')->group(function (): void {
Route::get('/', [TaxRuleController::class, 'index']);
Route::get('/{taxRule}', [TaxRuleController::class, 'show']);
Route::middleware('ability:accounting.tax-core.write')->group(function (): void {
Route::post('/', [TaxRuleController::class, 'store']);
Route::patch('/{taxRule}', [TaxRuleController::class, 'update']);
Route::post('/{taxRule}/activate', [TaxRuleController::class, 'activate']);
Route::post('/{taxRule}/archive', [TaxRuleController::class, 'archive']);
```
<!-- layer-implementation-plan:end -->
