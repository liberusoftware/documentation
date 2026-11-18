# Social Network: Social Network Events API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-events). Observed identity: [`liberusoftware/module-social-network-events-api`](../../../modules/source/liberusoftware--module-social-network-events-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-social-network-social-network-events-api`<br>
**Matching domain module:** `social-network-events`  
**Application:** Social Network  
**Source feature:** [Social Network Events](../features/social-network-events.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Social Network Events domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Events
- Invitations
- Attendance
- Capacity
- Schedules
- Locations
- Reminders
- Updates

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

This module API adapter is composed into [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).

| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |
| --- | --- | --- | --- |
| Next.js React | [`project-social-network-next-react`](https://github.com/liberusoftware/project-social-network-next-react) | [Next.js plan](../nextjs/social-network-events.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-social-network-nuxt-vue`](https://github.com/liberusoftware/project-social-network-nuxt-vue) | [Nuxt plan](../nuxt/social-network-events.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) | [React Native plan](../react-native/social-network-events.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-social-network-mobile-flutter`](https://github.com/liberusoftware/project-social-network-mobile-flutter) | [Flutter plan](../flutter/social-network-events.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-social-network-dart-mobile`](https://github.com/liberusoftware/project-social-network-dart-mobile) · [`project-social-network-dart-desktop`](https://github.com/liberusoftware/project-social-network-dart-desktop) | [Flutter & Dart plan](../flutter/social-network-events.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Events** | Expose authorized query/read projection and explicit domain transition command for `events` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Invitations** | Expose authorized query/read projection and explicit domain transition command for `invitations` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Attendance** | Expose authorized query/read projection and explicit domain transition command for `attendance` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Capacity** | Expose authorized query/read projection and explicit domain transition command for `capacity` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Schedules** | Expose authorized query/read projection and explicit domain transition command for `schedules` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Locations** | Expose authorized query/read projection and explicit domain transition command for `locations` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Reminders** | Expose authorized query/read projection and explicit domain transition command for `reminders` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Updates** | Expose authorized query/read projection and explicit domain transition command for `updates` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-social-network-events-api](../../../modules/source/liberusoftware--module-social-network-events-api.md) |
| Source package | [liberusoftware/module-social-network-events](../../../modules/source/liberusoftware--module-social-network-events.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/social-network-events-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/events')
Route::get('/', [EventsController::class, 'index'])->name('index');
Route::post('/', [EventsController::class, 'store'])->name('store');
Route::patch('/{event}', [EventsController::class, 'update'])->name('update');
Route::post('/{event}/publish', [EventsController::class, 'publish'])->name('publish');
Route::post('/{event}/invitations', [EventsController::class, 'invite'])->name('invite');
Route::post('/{event}/attendance', [EventsController::class, 'attendance'])->name('attendance');
Route::post('/{event}/updates', [EventsController::class, 'updateLog'])->name('updates.store');
Route::post('/{event}/reminders', [EventsController::class, 'reminder'])->name('reminders.store');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [EventsController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events-api/src/Http/Controllers/EventsController.php) | `public function index(Request $request, GetProfile $get, ListEvents $list): JsonResponse`<br>`public function store(Request $request, GetProfile $get, CreateEvent $create): JsonResponse`<br>`public function update(Event $event, Request $request, GetProfile $get, UpdateEvent $update): JsonResponse`<br>`public function publish(Event $event, Request $request, GetProfile $get, PublishEvent $publish): JsonResponse`<br>`public function invite(Event $event, Request $request, GetProfile $get, InviteProfile $invite): JsonResponse`<br>`public function attendance(Event $event, Request $request, GetProfile $get, SetAttendance $set): JsonResponse`<br>`public function updateLog(Event $event, Request $request, GetProfile $get, AddEventUpdate $add): JsonResponse`<br>`public function reminder(Event $event, Request $request, GetProfile $get, ScheduleReminder $schedule): JsonResponse` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core action / service source | Observed signatures |
| --- | --- |
| [AddEventUpdate.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/AddEventUpdate.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, Event $event, string $body): EventUpdate` |
| [CreateEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/CreateEvent.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, array $data): Event` |
| [InviteProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/InviteProfile.php) | `public function __construct(private EventsAuthorizer $authorizer)`<br>`public function handle(Profile $owner, Event $event, Profile $invitee): Invitation` |
| [ListEvents.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/ListEvents.php) | `public function handle(Profile $viewer, int $limit = 25): Collection` |
| [PublishEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/PublishEvent.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, Event $event): Event` |
| [ScheduleReminder.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/ScheduleReminder.php) | `public function __construct(private EventsAuthorizer $authorizer)`<br>`public function handle(Profile $profile, Event $event, string $sendAt): EventReminder` |
| [SetAttendance.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/SetAttendance.php) | `public function __construct(private EventsAuthorizer $authorizer)`<br>`public function handle(Profile $profile, Event $event, string $state): void` |
| [UpdateEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Actions/UpdateEvent.php) | `public function __construct( private EventsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $owner, Event $event, array $data): Event` |
| [EventsAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Contracts/EventsAuthorizer.php) | `public function create(Profile $owner): void`<br>`public function manage(Profile $owner, Event $event): void`<br>`public function attend(Profile $profile, Event $event): void` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [Event.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/Event.php) | `id`, `owner_profile_id`, `state`, `visibility`, `timezone`, `title`, `description`, `starts_at`, `ends_at`, `capacity`, `location`, `metadata` |
| [EventReminder.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/EventReminder.php) | `event_id`, `profile_id`, `send_at`, `sent_at` |
| [EventUpdate.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/EventUpdate.php) | `event_id`, `author_profile_id`, `body` |
| [Invitation.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events/src/Models/Invitation.php) | `event_id`, `profile_id`, `state` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [openapi/v1/social-network-events.yaml](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-events-api/openapi/v1/social-network-events.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#social-network-events), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `social-network-events`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `social-network-events`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
