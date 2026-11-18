# Accounting: Xero Migration Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#xero-migration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-xero-migration-nuxt`
**Matching domain module:** `accounting-xero-migration`
**Application:** Accounting
**Source feature:** [Xero Migration](../features/xero-migration.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/xero-migration.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-xero-migration` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Chart/tracking categories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Contacts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Items:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Invoices/bills/credits/payments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Bank:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tax:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Assets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Projects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Expense claims:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attachments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Source IDs:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-xero-migration-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `chart-tracking-categories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `contacts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `items`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `invoices-bills-credits-payments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `bank`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tax`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `assets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `projects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `expense-claims`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
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

- Package identity, public exports, API dependency, and module dependency match `accounting-xero-migration` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/xero-migration.md)) |
| Capability Nuxt module skeleton | [`module-accounting-xero-migration-nuxt`](https://github.com/liberusoftware/module-accounting-xero-migration-nuxt) (`@liberusoftware/module-accounting-xero-migration-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Chart/tracking categories** | Expose composable and Vue 3 component for `chart/tracking categories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/xero-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Contacts** | Expose composable and Vue 3 component for `contacts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/xero-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Items** | Expose composable and Vue 3 component for `items` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/xero-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Invoices/bills/credits/payments** | Expose composable and Vue 3 component for `invoices/bills/credits/payments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/xero-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Bank** | Expose composable and Vue 3 component for `bank` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/xero-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Tax** | Expose composable and Vue 3 component for `tax` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/xero-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Assets** | Expose composable and Vue 3 component for `assets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/xero-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Projects** | Expose composable and Vue 3 component for `projects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/xero-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Expense claims** | Expose composable and Vue 3 component for `expense claims` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/xero-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Attachments** | Expose composable and Vue 3 component for `attachments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/xero-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Source IDs** | Expose composable and Vue 3 component for `source ids` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/xero-migration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConnectXeroTenant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Actions/ConnectXeroTenant.php) | `public function handle(array $attributes): XeroConnection` |
| [RecordMigration.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Actions/RecordMigration.php) | `public function handle(XeroConnection $connection, array $attributes): XeroMigrationRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [XeroConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Models/XeroConnection.php) | `team_id`, `tenant_ref`, `access_token`, `refresh_token`, `token_expires_at`, `status`, `last_synced_at`, `metadata` |
| [XeroMigrationRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration/src/Models/XeroMigrationRecord.php) | `team_id`, `connection_id`, `source_type`, `source_id`, `target_type`, `target_id`, `status`, `error`, `payload` |

| Observed API controller | Handler signatures |
| --- | --- |
| [XeroMigrationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration-api/src/Http/Controllers/XeroMigrationController.php) | `public function connections(Request $request): mixed`<br>`public function connect(Request $request, ConnectXeroTenant $action): mixed`<br>`public function record(Request $request, string $connection, RecordMigration $action): mixed` |

**Observed route declarations:**

[modules/accounting-xero-migration-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-xero-migration-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/xero-migration')->middleware(['auth:sanctum'])->group(function (): void {
Route::get('/connections', [XeroMigrationController::class, 'connections'])->middleware('ability:accounting.xero-migration.read');
Route::post('/connections', [XeroMigrationController::class, 'connect'])->middleware('ability:accounting.xero-migration.write');
Route::post('/connections/{connection}/records', [XeroMigrationController::class, 'record'])->middleware('ability:accounting.xero-migration.write');
```
<!-- layer-implementation-plan:end -->
