# Real Estate: Viewings API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#viewings). Observed identity: [`liberusoftware/real-estate-viewings-api`](../../../modules/source/liberusoftware--real-estate-viewings-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-real-estate-viewings-api`
**Matching domain module:** `real-estate-viewings`
**Application:** Real Estate
**Source feature:** [Viewings](../features/viewings.md)
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Viewings domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Availability
- Booking
- Confirmation
- Access
- Accompaniment
- Reminders
- Feedback
- No-shows

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

This module API adapter is composed into [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).

| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |
| --- | --- | --- | --- |
| Next.js React | [`project-real-estate-next-react`](https://github.com/liberusoftware/project-real-estate-next-react) | [Next.js plan](../nextjs/viewings.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-real-estate-nuxt-vue`](https://github.com/liberusoftware/project-real-estate-nuxt-vue) | [Nuxt plan](../nuxt/viewings.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-real-estate-mobile-react`](https://github.com/liberusoftware/project-real-estate-mobile-react) | [React Native plan](../react-native/viewings.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-real-estate-mobile-flutter`](https://github.com/liberusoftware/project-real-estate-mobile-flutter) | [Flutter plan](../flutter/viewings.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-real-estate-dart-mobile`](https://github.com/liberusoftware/project-real-estate-dart-mobile) · [`project-real-estate-dart-desktop`](https://github.com/liberusoftware/project-real-estate-dart-desktop) | [Flutter & Dart plan](../flutter/viewings.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Availability** | Expose authorized query/read projection and explicit domain transition command for `availability` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Booking** | Expose authorized query/read projection and explicit domain transition command for `booking` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Confirmation** | Expose authorized query/read projection and explicit domain transition command for `confirmation` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Access** | Expose authorized query/read projection and explicit domain transition command for `access` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Accompaniment** | Expose authorized query/read projection and explicit domain transition command for `accompaniment` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Reminders** | Expose authorized query/read projection and explicit domain transition command for `reminders` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Feedback** | Expose authorized query/read projection and explicit domain transition command for `feedback` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **No-shows** | Expose authorized query/read projection and explicit domain transition command for `no-shows` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/real-estate-viewings-api](../../../modules/source/liberusoftware--real-estate-viewings-api.md) |
| Source package | [liberusoftware/real-estate-viewings](../../../modules/source/liberusoftware--real-estate-viewings.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/real-estate-viewings-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/viewings')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [ViewingController::class, 'index'])->name('real-estate.viewings.index');
Route::post('/', [ViewingController::class, 'store'])->name('real-estate.viewings.store');
Route::get('/availability', [ViewingController::class, 'availability'])->name('real-estate.viewings.availability');
Route::get('/{viewing}', [ViewingController::class, 'show'])->name('real-estate.viewings.show');
Route::delete('/{viewing}', [ViewingController::class, 'destroy'])->name('real-estate.viewings.destroy');
Route::post('/{viewing}/confirm', [ViewingController::class, 'confirm'])->name('real-estate.viewings.confirm');
Route::post('/{viewing}/complete', [ViewingController::class, 'complete'])->name('real-estate.viewings.complete');
Route::post('/{viewing}/cancel', [ViewingController::class, 'cancel'])->name('real-estate.viewings.cancel');
Route::post('/{viewing}/no-show', [ViewingController::class, 'noShow'])->name('real-estate.viewings.no-show');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [ViewingController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings-api/src/Http/Controllers/ViewingController.php) | `public function index(Request $request): JsonResponse`<br>`public function availability(Request $request, AvailableViewingSlots $slots): JsonResponse`<br>`public function store(Request $request, CreateViewing $create): JsonResponse`<br>`public function show(Request $request, Viewing $viewing): JsonResponse`<br>`public function update(Request $request, Viewing $viewing, UpdateViewing $update): JsonResponse`<br>`public function destroy(Request $request, Viewing $viewing, DeleteViewing $delete): Response`<br>`public function confirm(Request $request, Viewing $viewing, ConfirmViewing $confirm): JsonResponse`<br>`public function complete(Request $request, Viewing $viewing, CompleteViewing $complete): JsonResponse`<br>`public function cancel(Request $request, Viewing $viewing, CancelViewing $cancel): JsonResponse`<br>`public function noShow(Request $request, Viewing $viewing, MarkViewingNoShow $noShow): JsonResponse` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core query source | Observed signatures |
| --- | --- |
| [AvailableViewingSlots.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Queries/AvailableViewingSlots.php) | `public function handle( int\|string $teamId, int\|string\|null $propertyId, CarbonImmutable $date, int $durationMinutes = 60, ): array` |
| [ViewingCalendarExport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Queries/ViewingCalendarExport.php) | `public function handle(Viewing\|int\|string $viewing): string` |

| Core action / service source | Observed signatures |
| --- | --- |
| [ViewingPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Policies/ViewingPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Viewing $viewing): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Viewing $viewing): bool`<br>`public function delete(AuthUser $authUser, Viewing $viewing): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Viewing $viewing): bool`<br>`public function forceDelete(AuthUser $authUser, Viewing $viewing): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Viewing $viewing): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [Viewing.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Models/Viewing.php) | No literal fillable array detected; inspect the model and API schema. |
| [ViewingFeedback.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Models/ViewingFeedback.php) | No literal fillable array detected; inspect the model and API schema. |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [openapi/v1/real-estate-viewings.yaml](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings-api/openapi/v1/real-estate-viewings.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#viewings), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

## 5. Audience and operation matrix

Expose only explicitly selected operations. Anonymous access is disabled unless the owning capability requires it; customer/partner reads and commands use record/tenant scope, staff actions use the relevant policy, and integrations use a narrow service identity. UI visibility and authentication alone do not establish authorization.

## 6. Implementation strategy

Resolve trusted actor/tenant context, validate the reviewed request and delegate to the public owning action/query. Serialize explicit authorized DTOs; preserve documented operation identity, concurrency and error semantics. Reuse existing owner APIs instead of copying their records or private model access.

## 7. Security, resilience, and observability

Apply record/field policy to lists, relationships, commands, bulk work, jobs and downloads. Use bounded retries/timeouts, durable operation/source references and explicit partial-failure recovery. Redact credentials/protected data while retaining safe request/correlation diagnostics.

## 8. Verification strategy

Verify actual route/schema parity, required input, allowed/denied/wrong-tenant requests, stale/duplicate commands, uncertain outcomes, pagination/field policy and affected owner integrations. Check the declared package/host scripts and supported versions; source/test presence is not a passing-run claim.

## 9. Definition of done

Release only after the complete reviewed request/response/error contract, version compatibility, security and owner invariants, consumer integration, migrations where owned, and operational recovery are verified. Document the actual package identity and source/release evidence in its README and changelog.
