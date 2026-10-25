# Mileage: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-mileage`.

**Proposed design identifier:** `module-accounting-mileage-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/mileage.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-mileage](../../../modules/source/liberusoftware--module-accounting-mileage.md) |
| API | [liberusoftware/module-accounting-mileage-api](../../../modules/source/liberusoftware--module-accounting-mileage-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Vehicles/rates | A focused authorized view or workflow section for vehicles/rates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Trip capture/import | A focused authorized view or workflow section for trip capture/import; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Distance | A focused authorized view or workflow section for distance; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Business purpose | A focused authorized view or workflow section for business purpose; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Projects | A focused authorized view or workflow section for projects; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Policy | A focused authorized view or workflow section for policy; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Approval | A focused authorized view or workflow section for approval; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Reimbursement | A focused authorized view or workflow section for reimbursement; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Regional reporting | A focused authorized view or workflow section for regional reporting; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [MileageQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Queries/MileageQuery.php) | `public function trips(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function rates(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function regionalReport(?int $teamId = null, ?string $region = null): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ApproveTrip.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/ApproveTrip.php) | `public function handle(MileageTrip $trip, string $actor, bool $approved = true, ?string $reason = null): MileageTrip` |
| [CaptureTrip.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/CaptureTrip.php) | `public function handle(array $attributes): MileageTrip` |
| [CreateVehicle.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/CreateVehicle.php) | `public function handle(array $attributes): Vehicle` |
| [RecordMileageRate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/RecordMileageRate.php) | `public function handle(array $attributes): MileageRate` |
| [ReimburseTrip.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/ReimburseTrip.php) | `public function handle(MileageTrip $trip, string $payee, ?string $externalRef = null): MileageReimbursement` |
| [SubmitTrip.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/SubmitTrip.php) | `public function handle(MileageTrip $trip): MileageTrip` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [MileageApproval.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageApproval.php) | `trip_id`, `actor_ref`, `decision`, `reason`, `decided_at`, `metadata` |
| [MileagePolicy.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileagePolicy.php) | `team_id`, `name`, `region`, `max_distance_per_trip`, `max_distance_per_day`, `requires_purpose`, `requires_project`, `approval_threshold`, `currency`, `active`, `metadata` |
| [MileageRate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageRate.php) | `team_id`, `region`, `vehicle_type`, `currency`, `rate_per_distance`, `effective_from`, `effective_until`, `active`, `metadata` |
| [MileageReimbursement.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageReimbursement.php) | `trip_id`, `payee_ref`, `currency`, `amount`, `status`, `external_ref`, `failure_message`, `paid_at`, `metadata` |
| [MileageTrip.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageTrip.php) | `team_id`, `trip_ref`, `employee_ref`, `vehicle_id`, `rate_id`, `policy_id`, `project_ref`, `origin`, `destination`, `trip_date`, `distance`, `distance_unit`, `business_purpose`, `region`, `currency`, `reimbursement_amount`, `status`, `source`, `source_hash`, `submitted_at`, `approved_at`, `reimbursed_at`, `metadata` |
| [Vehicle.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/Vehicle.php) | `team_id`, `owner_ref`, `registration`, `make`, `model`, `fuel_type`, `co2_g_per_km`, `active`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-mileage-api/routes/api.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/mileage')->group(function (): void {
Route::get('/', [MileageController::class, 'index'])->name('accounting.mileage.list');
Route::post('/', [MileageController::class, 'store'])->name('accounting.mileage.create');
Route::get('/vehicles', [MileageController::class, 'vehicles'])->name('accounting.mileage.vehicles');
Route::post('/vehicles', [MileageController::class, 'vehicle'])->name('accounting.mileage.vehicle');
Route::post('/rates', [MileageController::class, 'rate'])->name('accounting.mileage.rate');
Route::get('/report/regional', [MileageController::class, 'report'])->name('accounting.mileage.report');
Route::get('/{trip}', [MileageController::class, 'show'])->name('accounting.mileage.get');
Route::post('/{trip}/submit', [MileageController::class, 'submit'])->name('accounting.mileage.submit');
Route::post('/{trip}/approve', [MileageController::class, 'approve'])->name('accounting.mileage.approve');
Route::post('/{trip}/reimburse', [MileageController::class, 'reimburse'])->name('accounting.mileage.reimburse');
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
