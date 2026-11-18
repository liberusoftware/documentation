# Control Panel: Databases API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#databases). Observed identity: [`liberusoftware/module-control-panel-databases-api`](../../../modules/source/liberusoftware--module-control-panel-databases-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-control-panel-databases-api`
**Matching domain module:** `control-panel-databases`
**Application:** Control Panel
**Source feature:** [Databases](../features/databases.md)
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Databases domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Engines
- Databases
- Users
- Privileges
- Backups
- Upgrades
- Health
- Remote access

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
| Next.js React | [`project-control-panel-next-react`](https://github.com/liberusoftware/project-control-panel-next-react) | [Next.js plan](../nextjs/databases.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-control-panel-nuxt-vue`](https://github.com/liberusoftware/project-control-panel-nuxt-vue) | [Nuxt plan](../nuxt/databases.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-control-panel-mobile-react`](https://github.com/liberusoftware/project-control-panel-mobile-react) | [React Native plan](../react-native/databases.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-control-panel-mobile-flutter`](https://github.com/liberusoftware/project-control-panel-mobile-flutter) | [Flutter plan](../flutter/databases.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-control-panel-dart-mobile`](https://github.com/liberusoftware/project-control-panel-dart-mobile) · [`project-control-panel-dart-desktop`](https://github.com/liberusoftware/project-control-panel-dart-desktop) | [Flutter & Dart plan](../flutter/databases.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Engines** | Expose authorized query/read projection and explicit domain transition command for `engines` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Databases** | Expose authorized query/read projection and explicit domain transition command for `databases` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Users** | Expose authorized query/read projection and explicit domain transition command for `users` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Privileges** | Expose authorized query/read projection and explicit domain transition command for `privileges` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Backups** | Expose authorized query/read projection and explicit domain transition command for `backups` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Upgrades** | Expose authorized query/read projection and explicit domain transition command for `upgrades` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Health** | Expose authorized query/read projection and explicit domain transition command for `health` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Remote access** | Expose authorized query/read projection and explicit domain transition command for `remote access` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-control-panel-databases-api](../../../modules/source/liberusoftware--module-control-panel-databases-api.md) |
| Source package | [liberusoftware/module-control-panel-databases](../../../modules/source/liberusoftware--module-control-panel-databases.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/control-panel-databases-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/databases')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [DatabaseController::class, 'index'])->name('control-panel.databases.index');
Route::post('/', [DatabaseController::class, 'store'])->name('control-panel.databases.store');
Route::patch('{database}', [DatabaseController::class, 'update'])->name('control-panel.databases.update');
Route::post('{database}/users', [DatabaseController::class, 'user'])->name('control-panel.databases.users.store');
Route::post('users/{user}/privileges', [DatabaseController::class, 'privilege'])->name('control-panel.databases.privileges.store');
Route::post('{database}/backups', [DatabaseController::class, 'backup'])->name('control-panel.databases.backups.store');
Route::post('{database}/health-checks', [DatabaseController::class, 'health'])->name('control-panel.databases.health.store');
Route::post('{database}/upgrades', [DatabaseController::class, 'upgrade'])->name('control-panel.databases.upgrades.store');
Route::post('{database}/remote-access', [DatabaseController::class, 'remoteAccess'])->name('control-panel.databases.remote-access.store');
Route::post('{database}/suspend', [DatabaseController::class, 'suspend'])->name('control-panel.databases.suspend');
Route::post('{database}/archive', [DatabaseController::class, 'archive'])->name('control-panel.databases.archive');
Route::delete('{database}', [DatabaseController::class, 'delete'])->name('control-panel.databases.delete');
Route::get('{database}', [DatabaseController::class, 'show'])->name('control-panel.databases.show');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [DatabaseController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases-api/src/Http/Controllers/DatabaseController.php) | `public function index(Request $request, ListDatabases $list): JsonResponse`<br>`public function user(Request $request, Database $database, CreateDatabaseUser $create): JsonResponse`<br>`public function privilege(Request $request, DatabaseUser $user, GrantDatabasePrivilege $grant): JsonResponse`<br>`public function backup(Request $request, Database $database, CreateDatabaseBackup $create): JsonResponse`<br>`public function health(Request $request, Database $database, RecordDatabaseHealth $record): JsonResponse`<br>`public function upgrade(Request $request, Database $database, RequestDatabaseUpgrade $requestUpgrade): JsonResponse`<br>`public function remoteAccess(Request $request, Database $database, ConfigureRemoteAccess $configure): JsonResponse`<br>`public function suspend(Request $request, Database $database, SuspendDatabase $suspend): JsonResponse`<br>`public function archive(Request $request, Database $database, ArchiveDatabase $archive): JsonResponse`<br>`public function delete(Request $request, Database $database, DeleteDatabase $delete): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, CreateDatabase $create): JsonResponse`<br>`public function update(Request $request, string $id, UpdateDatabase $update): JsonResponse` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core query source | Observed signatures |
| --- | --- |
| [ListDatabaseBackups.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Queries/ListDatabaseBackups.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |
| [ListDatabases.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Queries/ListDatabases.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Core action / service source | Observed signatures |
| --- | --- |
| [ActivateDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/ActivateDatabase.php) | `public function execute(Database $database): Database` |
| [ArchiveDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/ArchiveDatabase.php) | `public function execute(Database $database): Database` |
| [ConfigureRemoteAccess.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/ConfigureRemoteAccess.php) | `public function execute(Database $database, array $attributes): DatabaseRemoteAccess` |
| [CreateDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/CreateDatabase.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): Database` |
| [CreateDatabaseBackup.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/CreateDatabaseBackup.php) | `public function execute(Database $database, array $attributes): DatabaseBackup` |
| [CreateDatabaseUser.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/CreateDatabaseUser.php) | `public function execute(Database $database, array $attributes): DatabaseUser` |
| [DeleteDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/DeleteDatabase.php) | `public function execute(Database $database): void` |
| [GrantDatabasePrivilege.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/GrantDatabasePrivilege.php) | `public function execute(DatabaseUser $user, string $privilege, string $objectName = '*'): DatabasePrivilege` |
| [RecordDatabaseHealth.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/RecordDatabaseHealth.php) | `public function execute(Database $database, bool $healthy, ?int $latencyMs = null, ?string $message = null, array $details = []): DatabaseHealthCheck` |
| [RequestDatabaseUpgrade.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/RequestDatabaseUpgrade.php) | `public function execute(Database $database, string $toVersion): DatabaseUpgrade` |
| [SuspendDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/SuspendDatabase.php) | `public function execute(Database $database): Database` |
| [UpdateDatabase.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Actions/UpdateDatabase.php) | `public function execute(Database $database, array $attributes): Database` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [Database.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/Database.php) | `team_id`, `engine_id`, `account_id`, `name`, `status`, `charset`, `collation`, `metadata` |
| [DatabaseBackup.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseBackup.php) | `team_id`, `database_id`, `destination`, `type`, `path`, `size`, `status`, `error`, `started_at`, `completed_at`, `automated` |
| [DatabaseEngine.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseEngine.php) | `team_id`, `name`, `driver`, `version`, `host`, `port`, `active`, `metadata` |
| [DatabaseHealthCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseHealthCheck.php) | `team_id`, `database_id`, `healthy`, `latency_ms`, `message`, `details`, `checked_at` |
| [DatabasePrivilege.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabasePrivilege.php) | `team_id`, `database_id`, `database_user_id`, `privilege`, `object_name` |
| [DatabaseRemoteAccess.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseRemoteAccess.php) | `team_id`, `database_id`, `source_cidr`, `port`, `tls_required`, `active`, `expires_at`, `metadata` |
| [DatabaseUpgrade.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseUpgrade.php) | `team_id`, `database_id`, `from_version`, `to_version`, `status`, `error`, `started_at`, `finished_at`, `metadata` |
| [DatabaseUser.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases/src/Models/DatabaseUser.php) | `team_id`, `database_id`, `username`, `host`, `password`, `active` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [openapi/v1/control-panel-databases.yaml](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-databases-api/openapi/v1/control-panel-databases.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#databases), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `control-panel-databases`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `control-panel-databases`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
