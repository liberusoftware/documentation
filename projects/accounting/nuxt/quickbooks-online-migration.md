# Accounting: QuickBooks Online Migration Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#quickbooks-online-migration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-quickbooks-online-migration-nuxt`
**Matching domain module:** `accounting-quickbooks-online-migration`
**Application:** Accounting
**Source feature:** [QuickBooks Online Migration](../features/quickbooks-online-migration.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/quickbooks-online-migration.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-quickbooks-online-migration` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Chart:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Classes/locations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Contacts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Items:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Invoices/bills/credits/payments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Journals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Bank data:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Projects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tax:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attachments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Source IDs:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-quickbooks-online-migration-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `chart`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `classes-locations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `contacts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `items`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `invoices-bills-credits-payments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `journals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `bank-data`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `projects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tax`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `attachments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `source-ids`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-quickbooks-online-migration` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/quickbooks-online-migration.md)) |
| Capability Nuxt module skeleton | [`module-accounting-quickbooks-online-migration-nuxt`](https://github.com/liberusoftware/module-accounting-quickbooks-online-migration-nuxt) (`@liberusoftware/module-accounting-quickbooks-online-migration-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Chart** | Expose composable and Vue 3 component for `chart` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/quickbooks-online-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Classes/locations** | Expose composable and Vue 3 component for `classes/locations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/quickbooks-online-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Contacts** | Expose composable and Vue 3 component for `contacts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/quickbooks-online-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Items** | Expose composable and Vue 3 component for `items` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/quickbooks-online-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Invoices/bills/credits/payments** | Expose composable and Vue 3 component for `invoices/bills/credits/payments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/quickbooks-online-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Journals** | Expose composable and Vue 3 component for `journals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/quickbooks-online-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Bank data** | Expose composable and Vue 3 component for `bank data` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/quickbooks-online-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Projects** | Expose composable and Vue 3 component for `projects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/quickbooks-online-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Tax** | Expose composable and Vue 3 component for `tax` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/quickbooks-online-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Attachments** | Expose composable and Vue 3 component for `attachments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/quickbooks-online-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Source IDs** | Expose composable and Vue 3 component for `source ids` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/quickbooks-online-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateMigrationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Actions/CreateMigrationRun.php) | `public function handle(?int $connectionId, array $metadata = []): QboMigrationRun` |
| [ImportMigrationRecords.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Actions/ImportMigrationRecords.php) | `public function handle(QboMigrationRun $run, array $records): QboMigrationRun` |
| [ReconcileMigration.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Actions/ReconcileMigration.php) | `public function handle(QboMigrationRun $run): QboMigrationRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [QboMigrationConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Models/QboMigrationConnection.php) | `team_id`, `realm_id`, `access_token`, `refresh_token`, `token_expires_at`, `status`, `last_synced_at` |
| [QboMigrationRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Models/QboMigrationRecord.php) | `run_id`, `entity_type`, `source_id`, `status`, `payload`, `payload_hash`, `error_message`, `metadata` |
| [QboMigrationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Models/QboMigrationRun.php) | `connection_id`, `status`, `total_records`, `imported_records`, `failed_records`, `errors`, `metadata`, `started_at`, `finished_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [QboMigrationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration-api/src/Http/Controllers/QboMigrationController.php) | `public function index(): mixed`<br>`public function store(Request $request, CreateMigrationRun $create, ImportMigrationRecords $import): QboMigrationRun`<br>`public function show(QboMigrationRun $run): QboMigrationRun`<br>`public function reconcile(QboMigrationRun $run, ReconcileMigration $action): QboMigrationRun` |

**Observed route declarations:**

[modules/accounting-quickbooks-online-migration-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/quickbooks-online-migration')->group(function (): void {
Route::get('/', [QboMigrationController::class, 'index']);
Route::post('/', [QboMigrationController::class, 'store']);
Route::get('/{run}', [QboMigrationController::class, 'show']);
Route::post('/{run}/reconcile', [QboMigrationController::class, 'reconcile']);
```
<!-- layer-implementation-plan:end -->
