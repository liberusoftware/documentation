# Control Panel: Backups API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#backups). Observed identity: [`liberusoftware/module-control-panel-backups-api`](../../../modules/source/liberusoftware--module-control-panel-backups-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-control-panel-backups-api`
**Matching domain module:** `control-panel-backups`
**Application:** Control Panel
**Source feature:** [Backups](../features/backups.md)
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Backups domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Policies
- Snapshots
- Application-consistent backup
- Encryption
- Off-site storage
- Restore
- Verification

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Choose the route namespace through the host's reviewed API contract; observed source prefixes below take precedence over repository/design-name guesses.
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

## 3. Endpoint examples

**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.

### Product API backend and client integration

This module API adapter is composed into [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).

| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |
| --- | --- | --- | --- |
| Next.js React | [`project-control-panel-next-react`](https://github.com/liberusoftware/project-control-panel-next-react) | [Next.js plan](../nextjs/backups.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-control-panel-nuxt-vue`](https://github.com/liberusoftware/project-control-panel-nuxt-vue) | [Nuxt plan](../nuxt/backups.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-control-panel-mobile-react`](https://github.com/liberusoftware/project-control-panel-mobile-react) | [React Native plan](../react-native/backups.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-control-panel-mobile-flutter`](https://github.com/liberusoftware/project-control-panel-mobile-flutter) | [Flutter plan](../flutter/backups.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-control-panel-dart-mobile`](https://github.com/liberusoftware/project-control-panel-dart-mobile) · [`project-control-panel-dart-desktop`](https://github.com/liberusoftware/project-control-panel-dart-desktop) | [Flutter & Dart plan](../flutter/backups.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Policies** | Expose authorized query/read projection and explicit domain transition command for `policies` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Snapshots** | Expose authorized query/read projection and explicit domain transition command for `snapshots` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Application-consistent backup** | Expose authorized query/read projection and explicit domain transition command for `application-consistent backup` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Encryption** | Expose authorized query/read projection and explicit domain transition command for `encryption` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Off-site storage** | Expose authorized query/read projection and explicit domain transition command for `off-site storage` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Restore** | Expose authorized query/read projection and explicit domain transition command for `restore` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Verification** | Expose authorized query/read projection and explicit domain transition command for `verification` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-control-panel-backups-api](../../../modules/source/liberusoftware--module-control-panel-backups-api.md) |
| Source package | [liberusoftware/module-control-panel-backups](../../../modules/source/liberusoftware--module-control-panel-backups.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/control-panel-backups-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/backups')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/snapshots', [SnapshotController::class, 'index'])->name('control-panel.backups.snapshots.index');
Route::post('/snapshots', [SnapshotController::class, 'store'])->name('control-panel.backups.snapshots.store');
Route::patch('/policies/{policy}', [SnapshotController::class, 'updatePolicy'])->name('control-panel.backups.policies.update');
Route::delete('/policies/{policy}', [SnapshotController::class, 'deletePolicy'])->name('control-panel.backups.policies.delete');
Route::post('/snapshots/{snapshot}/verify', [SnapshotController::class, 'verify'])->name('control-panel.backups.snapshots.verify');
Route::post('/snapshots/{snapshot}/restore', [SnapshotController::class, 'restore'])->name('control-panel.backups.snapshots.restore');
Route::post('/destinations', [SnapshotController::class, 'destination'])->name('control-panel.backups.destinations.store');
Route::patch('/destinations/{destination}', [SnapshotController::class, 'updateDestination'])->name('control-panel.backups.destinations.update');
Route::post('/destinations/{destination}/health', [SnapshotController::class, 'destinationHealth'])->name('control-panel.backups.destinations.health');
Route::delete('/destinations/{destination}', [SnapshotController::class, 'deleteDestination'])->name('control-panel.backups.destinations.delete');
Route::post('/schedules', [SnapshotController::class, 'schedule'])->name('control-panel.backups.schedules.store');
Route::patch('/schedules/{schedule}', [SnapshotController::class, 'updateSchedule'])->name('control-panel.backups.schedules.update');
Route::delete('/schedules/{schedule}', [SnapshotController::class, 'deleteSchedule'])->name('control-panel.backups.schedules.delete');
Route::delete('/snapshots/{snapshot}', [SnapshotController::class, 'deleteSnapshot'])->name('control-panel.backups.snapshots.delete');
Route::post('/features', [SnapshotController::class, 'feature'])->name('control-panel.backups.features.store');
Route::get('snapshots/{snapshot}', [SnapshotController::class, 'show'])->name('control-panel.backups.show');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [SnapshotController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-api/src/Http/Controllers/SnapshotController.php) | `public function index(Request $request, ListSnapshots $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, CreateSnapshot $create): JsonResponse`<br>`public function destination(Request $request, CreateDestination $create): JsonResponse`<br>`public function updatePolicy(Request $request, string $id, UpdatePolicy $update): JsonResponse`<br>`public function updateDestination(Request $request, string $id, UpdateDestination $update): JsonResponse`<br>`public function destinationHealth(Request $request, string $id, RecordDestinationHealth $record): JsonResponse`<br>`public function deleteDestination(Request $request, string $id, DeleteDestination $delete): JsonResponse`<br>`public function updateSchedule(Request $request, string $id, UpdateSchedule $update): JsonResponse`<br>`public function deleteSchedule(Request $request, string $id, DeleteSchedule $delete): JsonResponse`<br>`public function deletePolicy(Request $request, string $id, DeletePolicy $delete): JsonResponse`<br>`public function deleteSnapshot(Request $request, string $id, DeleteSnapshot $delete): JsonResponse`<br>`public function schedule(Request $request, CreateSchedule $create): JsonResponse`<br>`public function restore(Request $request, string $snapshot, RequestRestore $restore): JsonResponse`<br>`public function verify(Request $request, string $snapshot, VerifySnapshot $verify): JsonResponse`<br>`public function feature(Request $request, RecordBackupFeature $record): JsonResponse` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core query source | Observed signatures |
| --- | --- |
| [ListSnapshots.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Queries/ListSnapshots.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Core action / service source | Observed signatures |
| --- | --- |
| [CreateDestination.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateDestination.php) | `public function execute(array $attributes): BackupDestination` |
| [CreatePolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreatePolicy.php) | `public function execute(array $attributes): BackupPolicy` |
| [CreateSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateSchedule.php) | `public function execute(BackupPolicy $policy, string $cron, string $timezone = 'UTC'): BackupSchedule` |
| [CreateSnapshot.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/CreateSnapshot.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(BackupPolicy $policy, array $attributes = []): BackupSnapshot` |
| [DeleteDestination.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteDestination.php) | `public function execute(BackupDestination $destination): void` |
| [DeletePolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeletePolicy.php) | `public function execute(BackupPolicy $policy): void` |
| [DeleteSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteSchedule.php) | `public function execute(BackupSchedule $schedule): void` |
| [DeleteSnapshot.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/DeleteSnapshot.php) | `public function execute(BackupSnapshot $snapshot): void` |
| [RecordBackupFeature.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/RecordBackupFeature.php) | `public function execute(array $a): Model` |
| [RecordDestinationHealth.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/RecordDestinationHealth.php) | `public function execute(BackupDestination $destination, bool $healthy, ?int $latencyMs = null, ?string $message = null, array $details = []): BackupDestination` |
| [RequestRestore.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/RequestRestore.php) | `public function execute(BackupSnapshot $snapshot, string $teamId, string $target, array $options = []): BackupRestore` |
| [UpdateDestination.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/UpdateDestination.php) | `public function execute(BackupDestination $destination, array $attributes): BackupDestination` |
| [UpdatePolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/UpdatePolicy.php) | `public function execute(BackupPolicy $policy, array $attributes): BackupPolicy` |
| [UpdateSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/UpdateSchedule.php) | `public function execute(BackupSchedule $schedule, array $attributes): BackupSchedule` |
| [VerifySnapshot.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Actions/VerifySnapshot.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(BackupSnapshot $snapshot, string $checksum): BackupSnapshot` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [BackupDestination.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupDestination.php) | `team_id`, `name`, `driver`, `config`, `retention_days`, `default`, `active`, `last_checked_at`, `health` |
| [BackupEncryption.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupEncryption.php) | `id`, `team_id`, `policy_id`, `algorithm`, `key_reference`, `active`, `rotated_at` |
| [BackupExecution.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupExecution.php) | `id`, `team_id`, `policy_id`, `type`, `consistency`, `status`, `started_at`, `completed_at`, `error`, `metadata` |
| [BackupPolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupPolicy.php) | `team_id`, `name`, `schedule`, `retention_days`, `storage_driver`, `storage_config`, `encrypted`, `active` |
| [BackupRestore.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupRestore.php) | `team_id`, `snapshot_id`, `target`, `status`, `options`, `error`, `started_at`, `finished_at` |
| [BackupSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupSchedule.php) | `team_id`, `policy_id`, `cron`, `timezone`, `active`, `next_run_at`, `last_run_at` |
| [BackupSnapshot.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/BackupSnapshot.php) | `team_id`, `policy_id`, `location`, `status`, `size_bytes`, `checksum`, `verified_at`, `metadata` |
| [OffsiteTransfer.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups/src/Models/OffsiteTransfer.php) | `id`, `team_id`, `snapshot_id`, `destination_id`, `status`, `attempts`, `transferred_at`, `error`, `metadata` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [openapi/v1/control-panel-backups.yaml](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-api/openapi/v1/control-panel-backups.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#backups), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

## 5. Audience and operation matrix

| Audience                       | Default exposure                    | Required controls                                                                      |
| ------------------------------ | ----------------------------------- | -------------------------------------------------------------------------------------- |
| Public/anonymous               | Disabled unless explicitly required | Enumeration resistance, strict rate limits, field minimization, abuse controls         |
| Authenticated customer/partner | Explicit allowlist                  | Tenant/resource ownership, purpose-specific scopes, field policy                       |
| Staff/administrator            | Explicit allowlist                  | Role/permission policy, tenant context, recent authentication for risky actions, audit |
| Service/integration client     | Explicit allowlist                  | Service identity, least-privilege scopes, expiry/rotation, idempotency, quotas         |

Every exposed operation must map to one audience, domain query/action, permission/scope, request/response schema, rate limit, idempotency/concurrency policy, audit event, and test set. Unmapped operations fail CI.

## 6. Implementation strategy

- Keep routes, controllers/handlers, requests, API resources, OpenAPI fragments, and transport tests in this API package.
- Validate shape at the request boundary and enforce authoritative invariants again in the domain action.
- Resolve tenant and actor context from trusted authentication/application routing; never grant context from a caller-supplied tenant identifier alone.
- Authorize field visibility as well as record/action access, and return concealment-safe errors where enumeration is a risk.
- Use idempotency keys for retryable writes, ETags/`If-Match` for relevant concurrent updates, and asynchronous operation resources for slow/bulk/provider-dependent work.
- Compose cross-module workflows in the application layer; do not query or mutate another module's private storage from this API package.

## 7. Security, resilience, and observability

- Threat-model authentication, authorization, tenant isolation, mass assignment, object references, abusive queries, uploads/downloads, webhooks, and sensitive data.
- Bound pagination, filters, includes, payloads, batch sizes, timeouts, and retry budgets.
- Redact credentials and protected data from logs and errors while recording request, correlation, API/module/version, tenant, principal, operation, status, latency, rate-limit, and idempotency outcomes.
- Define availability, latency, error-rate and queued-operation objectives plus alerts and recovery/reconciliation runbooks.

## 8. Verification strategy

- Lint OpenAPI, validate examples, detect implementation drift and breaking changes, and reject path/schema/operation-ID collisions during application aggregation.
- Test every operation for allowed, unauthenticated, wrong-tenant, insufficient-scope, insufficient-permission, hidden-field, invalid, missing, duplicate, stale, concurrent, throttled, and failure/recovery paths as applicable.
- Test pagination, filtering, sorting, includes, dates, money, identifiers, enums, idempotency, ETags, async operations, bulk partial failure, and stable Problem Details.
- Add one-to-one architecture tests proving this package depends on and presents only `control-panel-backups`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `control-panel-backups`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
