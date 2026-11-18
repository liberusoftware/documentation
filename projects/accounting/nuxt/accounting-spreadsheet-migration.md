# Accounting: Accounting Spreadsheet Migration Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-spreadsheet-migration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-spreadsheet-migration-nuxt`
**Matching domain module:** `accounting-spreadsheet-migration`
**Application:** Accounting
**Source feature:** [Accounting Spreadsheet Migration](../features/accounting-spreadsheet-migration.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-spreadsheet-migration.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-spreadsheet-migration` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Guided mapping:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Opening/outstanding/detail modes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Balancing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Duplicate controls:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Validation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-spreadsheet-migration-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `guided-mapping`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `opening-outstanding-detail-modes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `balancing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `duplicate-controls`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `validation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
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

- Package identity, public exports, API dependency, and module dependency match `accounting-spreadsheet-migration` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-spreadsheet-migration.md)) |
| Capability Nuxt module skeleton | [`module-accounting-spreadsheet-migration-nuxt`](https://github.com/liberusoftware/module-accounting-spreadsheet-migration-nuxt) (`@liberusoftware/module-accounting-spreadsheet-migration-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Templates** | Expose composable and Vue 3 component for `templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-spreadsheet-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Guided mapping** | Expose composable and Vue 3 component for `guided mapping` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-spreadsheet-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Opening/outstanding/detail modes** | Expose composable and Vue 3 component for `opening/outstanding/detail modes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-spreadsheet-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Balancing** | Expose composable and Vue 3 component for `balancing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-spreadsheet-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Duplicate controls** | Expose composable and Vue 3 component for `duplicate controls` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-spreadsheet-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Validation** | Expose composable and Vue 3 component for `validation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-spreadsheet-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-spreadsheet-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateMigrationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-spreadsheet-migration/src/Actions/CreateMigrationRun.php) | `public function handle(MigrationTemplate $template, array $attributes): MigrationRun` |
| [CreateMigrationTemplate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-spreadsheet-migration/src/Actions/CreateMigrationTemplate.php) | `public function handle(array $attributes): MigrationTemplate` |
| [ValidateMigration.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-spreadsheet-migration/src/Actions/ValidateMigration.php) | `public function handle(MigrationRun $run): MigrationRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MigrationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-spreadsheet-migration/src/Models/MigrationRun.php) | `template_id`, `mode`, `status`, `source_hash`, `row_count`, `source_total`, `target_total`, `errors`, `metadata` |
| [MigrationTemplate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-spreadsheet-migration/src/Models/MigrationTemplate.php) | `name`, `entity`, `mapping`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MigrationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-spreadsheet-migration-api/src/Http/Controllers/MigrationController.php) | `public function templates(): mixed`<br>`public function storeTemplate(Request $request, CreateMigrationTemplate $action): MigrationTemplate`<br>`public function storeRun(Request $request, MigrationTemplate $template, CreateMigrationRun $action): MigrationRunResource`<br>`public function validateRun(MigrationRun $run, ValidateMigration $action): MigrationRunResource` |

**Observed route declarations:**

[modules/accounting-spreadsheet-migration-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-spreadsheet-migration-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/spreadsheet-migration')->group(function (): void {
Route::get('/templates', [MigrationController::class, 'templates']);
Route::post('/templates', [MigrationController::class, 'storeTemplate']);
Route::post('/templates/{template}/runs', [MigrationController::class, 'storeRun']);
Route::post('/runs/{run}/validate', [MigrationController::class, 'validateRun']);
```
<!-- layer-implementation-plan:end -->
