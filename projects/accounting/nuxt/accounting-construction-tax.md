# Accounting: Accounting Construction Tax Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-construction-tax). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-construction-tax-nuxt`
**Matching domain module:** `accounting-construction-tax`
**Application:** Accounting
**Source feature:** [Accounting Construction Tax](../features/accounting-construction-tax.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-construction-tax.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-construction-tax` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **CIS-style subcontractor verification:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deduction rates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Statements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Monthly returns:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Corrections:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Filing adapters:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-construction-tax-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `cis-style-subcontractor-verification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deduction-rates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `statements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `monthly-returns`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `corrections`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `filing-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-construction-tax` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-construction-tax.md)) |
| Capability Nuxt module skeleton | [`module-accounting-construction-tax-nuxt`](https://github.com/liberusoftware/module-accounting-construction-tax-nuxt) (`@liberusoftware/module-accounting-construction-tax-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **CIS-style subcontractor verification** | Expose composable and Vue 3 component for `cis-style subcontractor verification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-construction-tax.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Deduction rates** | Expose composable and Vue 3 component for `deduction rates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-construction-tax.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Statements** | Expose composable and Vue 3 component for `statements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-construction-tax.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Monthly returns** | Expose composable and Vue 3 component for `monthly returns` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-construction-tax.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Corrections** | Expose composable and Vue 3 component for `corrections` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-construction-tax.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Filing adapters** | Expose composable and Vue 3 component for `filing adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-construction-tax.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ConstructionTaxQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Queries/ConstructionTaxQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CorrectConstructionTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/CorrectConstructionTaxReturn.php) | `public function handle(ConstructionTaxRecord $record, array $correction): ConstructionTaxRecord` |
| [CreateConstructionTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/CreateConstructionTaxRecord.php) | `public function handle(array $attributes): ConstructionTaxRecord` |
| [IssueConstructionTaxStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/IssueConstructionTaxStatement.php) | `public function handle(ConstructionTaxRecord $record, array $statement): ConstructionTaxRecord` |
| [SubmitConstructionTaxReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/SubmitConstructionTaxReturn.php) | `public function handle(ConstructionTaxRecord $record, string $adapter): ConstructionTaxRecord` |
| [VerifySubcontractor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Actions/VerifySubcontractor.php) | `public function handle(ConstructionTaxRecord $record, array $verification): ConstructionTaxRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConstructionTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax/src/Models/ConstructionTaxRecord.php) | `team_id`, `subcontractor_ref`, `verification_status`, `deduction_rate`, `tax_period`, `gross_amount`, `deduction_amount`, `return_status`, `filing_adapter`, `verification`, `statement`, `correction` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConstructionTaxController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax-api/src/Http/Controllers/ConstructionTaxController.php) | `public function index(ConstructionTaxQuery $query): JsonResponse`<br>`public function store(Request $request, CreateConstructionTaxRecord $action): JsonResponse`<br>`public function verify(Request $request, string $record, VerifySubcontractor $action): JsonResponse`<br>`public function submit(Request $request, string $record, SubmitConstructionTaxReturn $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-construction-tax-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-construction-tax-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/construction-tax')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.construction-tax.read')->get('/', [ConstructionTaxController::class, 'index']);
Route::middleware('ability:accounting.construction-tax.write')->group(function (): void {
Route::post('/', [ConstructionTaxController::class, 'store']);
Route::post('/{record}/verify', [ConstructionTaxController::class, 'verify']);
Route::post('/{record}/submit', [ConstructionTaxController::class, 'submit']);
```
<!-- layer-implementation-plan:end -->
