# Control Panel: Control Panel Accounts API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-accounts). Observed identity: [`liberusoftware/module-control-panel-accounts-api`](../../../modules/source/liberusoftware--module-control-panel-accounts-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-control-panel-control-panel-accounts-api`<br>
**Matching domain module:** `control-panel-accounts`  
**Application:** Control Panel  
**Source feature:** [Control Panel Accounts](../features/control-panel-accounts.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Control Panel Accounts domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Admin/reseller/customer hierarchy
- Packages
- Quotas
- Delegation
- Branding
- Suspension

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
| Next.js React | [`project-control-panel-next-react`](https://github.com/liberusoftware/project-control-panel-next-react) | [Next.js plan](../nextjs/control-panel-accounts.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-control-panel-nuxt-vue`](https://github.com/liberusoftware/project-control-panel-nuxt-vue) | [Nuxt plan](../nuxt/control-panel-accounts.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-control-panel-mobile-react`](https://github.com/liberusoftware/project-control-panel-mobile-react) | [React Native plan](../react-native/control-panel-accounts.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-control-panel-mobile-flutter`](https://github.com/liberusoftware/project-control-panel-mobile-flutter) | [Flutter plan](../flutter/control-panel-accounts.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-control-panel-dart-mobile`](https://github.com/liberusoftware/project-control-panel-dart-mobile) · [`project-control-panel-dart-desktop`](https://github.com/liberusoftware/project-control-panel-dart-desktop) | [Flutter & Dart plan](../flutter/control-panel-accounts.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Admin/reseller/customer hierarchy** | Expose authorized query/read projection and explicit domain transition command for `admin/reseller/customer hierarchy` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Packages** | Expose authorized query/read projection and explicit domain transition command for `packages` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Quotas** | Expose authorized query/read projection and explicit domain transition command for `quotas` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Delegation** | Expose authorized query/read projection and explicit domain transition command for `delegation` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Branding** | Expose authorized query/read projection and explicit domain transition command for `branding` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Suspension** | Expose authorized query/read projection and explicit domain transition command for `suspension` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-control-panel-accounts-api](../../../modules/source/liberusoftware--module-control-panel-accounts-api.md) |
| Source package | [liberusoftware/module-control-panel-accounts](../../../modules/source/liberusoftware--module-control-panel-accounts.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/control-panel-accounts-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/accounts')
Route::get('/', [AccountController::class, 'index'])->name('control-panel.accounts.index');
Route::post('/', [AccountController::class, 'store'])->name('control-panel.accounts.store');
Route::post('{account}/suspend', [AccountController::class, 'suspend'])->name('control-panel.accounts.suspend');
Route::post('{account}/activate', [AccountController::class, 'activate'])->name('control-panel.accounts.activate');
Route::post('{account}/archive', [AccountController::class, 'archive'])->name('control-panel.accounts.archive');
Route::post('{account}/delegations', [AccountController::class, 'delegate'])->name('control-panel.accounts.delegate');
Route::patch('{account}/branding', [AccountController::class, 'branding'])->name('control-panel.accounts.branding');
Route::post('{account}/quota-check', [AccountController::class, 'quotaCheck'])->name('control-panel.accounts.quota-check');
Route::post('packages', [AccountController::class, 'package'])->name('control-panel.accounts.packages.store');
Route::get('packages', [AccountController::class, 'packages'])->name('control-panel.accounts.packages.index');
Route::patch('packages/{package}', [AccountController::class, 'updatePackage'])->name('control-panel.accounts.packages.update');
Route::get('{account}/hosting-packages', [AccountController::class, 'assignments'])->name('control-panel.accounts.hosting-packages.index');
Route::post('{account}/hosting-packages', [AccountController::class, 'assignPackage'])->name('control-panel.accounts.hosting-packages.store');
Route::patch('hosting-package-assignments/{assignment}', [AccountController::class, 'updateAssignment'])->name('control-panel.accounts.hosting-packages.update');
Route::delete('hosting-package-assignments/{assignment}', [AccountController::class, 'removeAssignment'])->name('control-panel.accounts.hosting-packages.destroy');
Route::get('{account}/delegations', [AccountController::class, 'delegations'])->name('control-panel.accounts.delegations.index');
Route::post('delegations/{delegation}/revoke', [AccountController::class, 'revokeDelegation'])->name('control-panel.accounts.delegations.revoke');
Route::patch('delegations/{delegation}', [AccountController::class, 'updateDelegation'])->name('control-panel.accounts.delegations.update');
Route::patch('{account}', [AccountController::class, 'update'])->name('control-panel.accounts.update');
Route::get('{account}', [AccountController::class, 'show'])->name('control-panel.accounts.show');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [AccountController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts-api/src/Http/Controllers/AccountController.php) | `public function index(Request $request, ListAccounts $list): JsonResponse`<br>`public function suspend(Request $request, Account $account, SuspendAccount $suspend): JsonResponse`<br>`public function activate(Request $request, Account $account, ActivateAccount $activate): JsonResponse`<br>`public function archive(Request $request, Account $account, ArchiveAccount $archive): JsonResponse`<br>`public function package(Request $request, CreateHostingPackage $create): JsonResponse`<br>`public function packages(Request $request): JsonResponse`<br>`public function assignments(Request $request, Account $account): JsonResponse`<br>`public function assignPackage(Request $request, Account $account, AssignHostingPackage $assign): JsonResponse`<br>`public function updateAssignment(Request $request, string $assignment, UpdateHostingPackageAssignment $update): JsonResponse`<br>`public function removeAssignment(Request $request, string $assignment, RemoveHostingPackageAssignment $remove): JsonResponse`<br>`public function updatePackage(Request $request, string $package, UpdateHostingPackage $update): JsonResponse`<br>`public function delegate(Request $request, Account $account, DelegateAccount $delegate): JsonResponse`<br>`public function delegations(Request $request, Account $account): JsonResponse`<br>`public function revokeDelegation(Request $request, string $delegation, RevokeDelegation $revoke): JsonResponse`<br>`public function updateDelegation(Request $request, string $delegation, UpdateDelegation $update): JsonResponse`<br>`public function branding(Request $request, Account $account, UpdateBranding $update): JsonResponse`<br>`public function quotaCheck(Request $request, Account $account, QuotaGuard $quotas): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function update(Request $request, Account $account, UpdateAccount $update): JsonResponse`<br>`public function store(Request $request, CreateAccount $create): JsonResponse` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core query source | Observed signatures |
| --- | --- |
| [ListAccounts.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Queries/ListAccounts.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |

| Core action / service source | Observed signatures |
| --- | --- |
| [ActivateAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/ActivateAccount.php) | `public function execute(Account $account): Account` |
| [ArchiveAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/ArchiveAccount.php) | `public function execute(Account $account): Account` |
| [AssignHostingPackage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/AssignHostingPackage.php) | `public function execute(Account $account, HostingPackage $package, array $attributes = []): HostingPackageAssignment` |
| [CreateAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/CreateAccount.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): Account` |
| [CreateHostingPackage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/CreateHostingPackage.php) | `public function execute(array $attributes): HostingPackage` |
| [DelegateAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/DelegateAccount.php) | `public function execute(Account $account, array $attributes): AccountDelegation` |
| [RemoveHostingPackageAssignment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/RemoveHostingPackageAssignment.php) | `public function execute(HostingPackageAssignment $assignment): void` |
| [RevokeDelegation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/RevokeDelegation.php) | `public function execute(AccountDelegation $delegation): AccountDelegation` |
| [SuspendAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/SuspendAccount.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(Account $account, string $reason): Account` |
| [UpdateAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/UpdateAccount.php) | `public function execute(Account $account, array $attributes): Account` |
| [UpdateBranding.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/UpdateBranding.php) | `public function execute(Account $account, array $branding): Account` |
| [UpdateDelegation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/UpdateDelegation.php) | `public function execute(AccountDelegation $delegation, array $attributes): AccountDelegation` |
| [UpdateHostingPackage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/UpdateHostingPackage.php) | `public function execute(HostingPackage $package, array $attributes): HostingPackage` |
| [UpdateHostingPackageAssignment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/UpdateHostingPackageAssignment.php) | `public function execute(HostingPackageAssignment $assignment, array $attributes): HostingPackageAssignment` |
| [QuotaGuard.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Services/QuotaGuard.php) | `public function assertWithinQuota(Account $account, array $usage): void` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [Account.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Models/Account.php) | `team_id`, `parent_id`, `owner_id`, `type`, `status`, `name`, `brand`, `quota_overrides`, `suspended_reason`, `suspended_at` |
| [AccountDelegation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Models/AccountDelegation.php) | `team_id`, `account_id`, `delegate_id`, `permissions`, `expires_at`, `active` |
| [HostingPackage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Models/HostingPackage.php) | `team_id`, `name`, `limits`, `features`, `active` |
| [HostingPackageAssignment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Models/HostingPackageAssignment.php) | `team_id`, `account_id`, `hosting_package_id`, `start_date`, `end_date`, `active` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [openapi/v1/control-panel-accounts.yaml](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts-api/openapi/v1/control-panel-accounts.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#control-panel-accounts), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `control-panel-accounts`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `control-panel-accounts`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
