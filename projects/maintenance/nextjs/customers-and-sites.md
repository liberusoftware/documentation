# Customers and Sites: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-maintenance-customers-and-sites`.

**Proposed design identifier:** `module-maintenance-customers-and-sites-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/customers-and-sites.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-maintenance-customers-and-sites](../../../modules/source/liberusoftware--module-maintenance-customers-and-sites.md) |
| API | [liberusoftware/module-maintenance-customers-and-sites-api](../../../modules/source/liberusoftware--module-maintenance-customers-and-sites-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Customers | A focused authorized view or workflow section for customers; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Contacts | A focused authorized view or workflow section for contacts; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Sites | A focused authorized view or workflow section for sites; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Locations | A focused authorized view or workflow section for locations; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Access details | A focused authorized view or workflow section for access details; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Hazards | A focused authorized view or workflow section for hazards; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Service windows | A focused authorized view or workflow section for service windows; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateCustomer.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/CreateCustomer.php) | `public function handle(int $teamId, array $attributes): Customer` |
| [CreateSite.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/CreateSite.php) | `public function handle(int $teamId, array $attributes): Site` |
| [DeleteCustomer.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/DeleteCustomer.php) | `public function handle(int $teamId, Customer $customer): void` |
| [DeleteSite.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/DeleteSite.php) | `public function handle(int $teamId, Site $site): void` |
| [UpdateCustomer.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/UpdateCustomer.php) | `public function handle(int $teamId, Customer $customer, array $attributes): Customer` |
| [UpdateSite.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/UpdateSite.php) | `public function handle(int $teamId, Site $site, array $attributes): Site` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Customer.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Models/Customer.php) | `team_id`, `name`, `code`, `email`, `phone`, `address`, `city`, `state`, `zip`, `website`, `industry`, `description`, `type`, `contact_person`, `payment_terms`, `notes`, `is_active` |
| [Site.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Models/Site.php) | `team_id`, `customer_id`, `name`, `code`, `address`, `access_details`, `hazards`, `is_active` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/module-maintenance-customers-and-sites-api/routes/api.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-api/routes/api.php)

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

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
