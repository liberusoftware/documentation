# Accounting: Accounting Custom Report Builder Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-custom-report-builder). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-custom-report-builder-nuxt`
**Matching domain module:** `accounting-custom-report-builder`
**Application:** Accounting
**Source feature:** [Accounting Custom Report Builder](../features/accounting-custom-report-builder.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-custom-report-builder.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-custom-report-builder` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Governed measures/dimensions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Filters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Grouping:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Formulas:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Comparisons:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Layouts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Permissions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Saved variants:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exports:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-custom-report-builder-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `governed-measures-dimensions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `filters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `grouping`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `formulas`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `comparisons`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `layouts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `permissions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `saved-variants`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exports`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-custom-report-builder` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-custom-report-builder.md)) |
| Capability Nuxt module skeleton | [`module-accounting-custom-report-builder-nuxt`](https://github.com/liberusoftware/module-accounting-custom-report-builder-nuxt) (`@liberusoftware/module-accounting-custom-report-builder-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Governed measures/dimensions** | Expose composable and Vue 3 component for `governed measures/dimensions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-custom-report-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Filters** | Expose composable and Vue 3 component for `filters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-custom-report-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Grouping** | Expose composable and Vue 3 component for `grouping` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-custom-report-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Formulas** | Expose composable and Vue 3 component for `formulas` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-custom-report-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Comparisons** | Expose composable and Vue 3 component for `comparisons` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-custom-report-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Layouts** | Expose composable and Vue 3 component for `layouts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-custom-report-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Permissions** | Expose composable and Vue 3 component for `permissions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-custom-report-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Saved variants** | Expose composable and Vue 3 component for `saved variants` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-custom-report-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Exports** | Expose composable and Vue 3 component for `exports` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-custom-report-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CustomReportQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Queries/CustomReportQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCustomReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Actions/CreateCustomReport.php) | `public function handle(array $attributes): CustomReport` |
| [RequestReportExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Actions/RequestReportExport.php) | `public function handle(CustomReport $report, string $format, array $parameters = []): CustomReportExport` |
| [SaveReportVariant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Actions/SaveReportVariant.php) | `public function handle(CustomReport $report, string $variantRef, array $configuration): CustomReportVariant` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CustomReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Models/CustomReport.php) | `team_id`, `report_ref`, `name`, `measures`, `dimensions`, `filters`, `grouping`, `formulas`, `comparisons`, `layout`, `permissions` |
| [CustomReportExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Models/CustomReportExport.php) | `report_id`, `team_id`, `format`, `status`, `parameters`, `completed_at` |
| [CustomReportVariant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Models/CustomReportVariant.php) | `report_id`, `team_id`, `variant_ref`, `configuration` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CustomReportsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder-api/src/Http/Controllers/CustomReportsController.php) | `public function index(CustomReportQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCustomReport $action): JsonResponse`<br>`public function variant(Request $request, string $report, SaveReportVariant $action): JsonResponse`<br>`public function export(Request $request, string $report, RequestReportExport $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-custom-report-builder-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/custom-report-builder')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.custom-report-builder.read')->get('/', [CustomReportsController::class, 'index']);
Route::middleware('ability:accounting.custom-report-builder.write')->group(function (): void {
Route::post('/', [CustomReportsController::class, 'store']);
Route::post('/{report}/variants', [CustomReportsController::class, 'variant']);
Route::post('/{report}/exports', [CustomReportsController::class, 'export']);
```
<!-- layer-implementation-plan:end -->
