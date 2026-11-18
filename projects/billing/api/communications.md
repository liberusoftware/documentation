# Billing: Communications API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#communications). Observed identity: [`liberusoftware/module-billing-communications-api`](../../../modules/source/liberusoftware--module-billing-communications-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-billing-communications-api`
**Matching domain module:** `billing-communications`
**Application:** Billing
**Source feature:** [Communications](../features/communications.md)
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Communications domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- VoIP/SMS service inventory
- Number lifecycle
- Usage/rating imports
- Provider adapters

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

This module API adapter is composed into [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).

| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |
| --- | --- | --- | --- |
| Next.js React | [`project-billing-next-react`](https://github.com/liberusoftware/project-billing-next-react) | [Next.js plan](../nextjs/communications.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | [Nuxt plan](../nuxt/communications.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-billing-mobile-react`](https://github.com/liberusoftware/project-billing-mobile-react) | [React Native plan](../react-native/communications.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-billing-mobile-flutter`](https://github.com/liberusoftware/project-billing-mobile-flutter) | [Flutter plan](../flutter/communications.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-billing-dart-mobile`](https://github.com/liberusoftware/project-billing-dart-mobile) · [`project-billing-dart-desktop`](https://github.com/liberusoftware/project-billing-dart-desktop) | [Flutter & Dart plan](../flutter/communications.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **VoIP/SMS service inventory** | Expose authorized query/read projection and explicit domain transition command for `voip/sms service inventory` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Number lifecycle** | Expose authorized query/read projection and explicit domain transition command for `number lifecycle` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Usage/rating imports** | Expose authorized query/read projection and explicit domain transition command for `usage/rating imports` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Provider adapters** | Expose authorized query/read projection and explicit domain transition command for `provider adapters` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-billing-communications-api](../../../modules/source/liberusoftware--module-billing-communications-api.md) |
| Source package | [liberusoftware/module-billing-communications](../../../modules/source/liberusoftware--module-billing-communications.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/module-billing-communications-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.communications.read'])->prefix('api/v1/billing/communications')->group(function (): void {
Route::get('/voice/accounts', [CommunicationsController::class, 'voiceAccounts'])->name('billing.communications.voice.accounts.index');
Route::get('/voice/accounts/{account}/cdrs', [CommunicationsController::class, 'callRecords'])->whereNumber('account')->name('billing.communications.voice.cdrs.index');
Route::get('/voice/rates', [CommunicationsController::class, 'rates'])->name('billing.communications.voice.rates.index');
Route::get('/', [CommunicationsController::class, 'index'])->name('billing.communications.index');
Route::get('/numbers', [CommunicationsController::class, 'numbers'])->name('numbers');
Route::get('/providers', [CommunicationsController::class, 'providers'])->name('providers');
Route::get('/usage-imports', [CommunicationsController::class, 'usageImports'])->name('usage-imports');
Route::get('/{record}', [CommunicationsController::class, 'show'])->whereNumber('record')->name('billing.communications.show');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.communications.write', 'idempotency'])->prefix('api/v1/billing/communications')->group(function (): void {
Route::post('/voice/accounts', [CommunicationsController::class, 'createVoiceAccount'])->name('billing.communications.voice.accounts.store');
Route::post('/voice/accounts/{account}/provision', [CommunicationsController::class, 'provisionVoiceAccount'])->whereNumber('account')->name('billing.communications.voice.accounts.provision');
Route::post('/voice/accounts/{account}/cdrs', [CommunicationsController::class, 'ingestCallRecord'])->whereNumber('account')->name('billing.communications.voice.cdrs.store');
Route::post('/voice/rates', [CommunicationsController::class, 'createRate'])->name('billing.communications.voice.rates.store');
Route::post('/', [CommunicationsController::class, 'createService'])->name('billing.communications.store');
Route::patch('/{service}/lifecycle', [CommunicationsController::class, 'transitionService'])->whereNumber('service')->name('billing.communications.services.lifecycle');
Route::post('/numbers', [CommunicationsController::class, 'provisionNumber'])->name('billing.communications.numbers.store');
Route::patch('/numbers/{number}/status', [CommunicationsController::class, 'transitionNumber'])->whereNumber('number')->name('billing.communications.numbers.status');
Route::post('/providers', [CommunicationsController::class, 'createProvider'])->name('billing.communications.providers.store');
Route::post('/usage-imports', [CommunicationsController::class, 'importUsage'])->name('billing.communications.usage-imports.store');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [CommunicationsController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-api/src/Http/Controllers/CommunicationsController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, int $record): JsonResponse`<br>`public function createService(Request $request, CreateCommunicationService $create): JsonResponse`<br>`public function numbers(Request $request): JsonResponse`<br>`public function providers(Request $request): JsonResponse`<br>`public function usageImports(Request $request): JsonResponse`<br>`public function provisionNumber(Request $request, ProvisionCommunicationNumber $provision): JsonResponse`<br>`public function importUsage(Request $request, ImportCommunicationUsage $import): JsonResponse`<br>`public function transitionNumber(Request $request, int $number, TransitionCommunicationNumber $transition): JsonResponse`<br>`public function transitionService(Request $request, int $service, TransitionCommunicationService $transition): JsonResponse`<br>`public function createProvider(Request $request, CreateCommunicationProvider $create): JsonResponse`<br>`public function voiceAccounts(Request $request): JsonResponse`<br>`public function createVoiceAccount(Request $request, CreateVoipAccount $create): JsonResponse`<br>`public function provisionVoiceAccount(Request $request, int $account, ProvisionVoipAccount $provision): JsonResponse`<br>`public function rates(Request $request): JsonResponse`<br>`public function createRate(Request $request, CreateCallRateRule $create): JsonResponse`<br>`public function callRecords(Request $request, int $account): JsonResponse`<br>`public function ingestCallRecord(Request $request, int $account, IngestCallDetailRecord $ingest): JsonResponse` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core query source | Observed signatures |
| --- | --- |
| [ListCommunicationRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Queries/ListCommunicationRecords.php) | `public function handle(string $model, int $teamId): Collection` |
| [ListCommunicationsRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Queries/ListCommunicationsRecords.php) | `public function handle(int $teamId): Collection` |

| Core action / service source | Observed signatures |
| --- | --- |
| [CreateCallRateRule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/CreateCallRateRule.php) | `public function handle(int $teamId, array $attributes): CallRateRule` |
| [CreateCommunicationProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/CreateCommunicationProvider.php) | `public function handle(int $teamId, array $attributes): CommunicationProvider` |
| [CreateCommunicationService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/CreateCommunicationService.php) | `public function handle(int $teamId, array $attributes): CommunicationService` |
| [CreateVoipAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/CreateVoipAccount.php) | `public function handle(int $teamId, array $attributes): VoipAccount` |
| [ImportCommunicationUsage.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/ImportCommunicationUsage.php) | `public function handle(int $teamId, array $attributes): CommunicationUsageImport` |
| [IngestCallDetailRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/IngestCallDetailRecord.php) | `public function handle(VoipAccount $account, array $attributes): CallDetailRecord` |
| [ProvisionCommunicationNumber.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/ProvisionCommunicationNumber.php) | `public function handle(int $teamId, array $attributes): CommunicationNumber` |
| [ProvisionVoipAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/ProvisionVoipAccount.php) | `public function __construct(private VoiceProviderRegistry $providers)`<br>`public function handle(VoipAccount $account): VoipAccount` |
| [TransitionCommunicationNumber.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/TransitionCommunicationNumber.php) | `public function handle(CommunicationNumber $number, string $status): CommunicationNumber` |
| [TransitionCommunicationService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Actions/TransitionCommunicationService.php) | `public function handle(CommunicationService $service, string $status): CommunicationService` |
| [CommunicationProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Contracts/CommunicationProvider.php) | `public function provisionNumber(string $number, string $type = 'phone'): array`<br>`public function importUsage(iterable $rows): int` |
| [VoiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Contracts/VoiceProvider.php) | `public function key(): string`<br>`public function provision(array $attributes): array` |
| [CommunicationRecordPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Policies/CommunicationRecordPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function update(?object $user, object $record): bool` |
| [CommunicationServicePolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Policies/CommunicationServicePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, CommunicationService $record): bool`<br>`public function update(?Authenticatable $user, CommunicationService $record): bool` |
| [VoiceProviderRegistry.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Services/VoiceProviderRegistry.php) | `public function register(VoiceProvider $provider): void`<br>`public function resolve(string $key): VoiceProvider` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [CallDetailRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CallDetailRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [CallRateRule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CallRateRule.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunicationNumber.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CommunicationNumber.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunicationProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CommunicationProvider.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunicationService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CommunicationService.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommunicationUsageImport.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/CommunicationUsageImport.php) | No literal fillable array detected; inspect the model and API schema. |
| [VoipAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/VoipAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [VoipFraudAlert.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications/src/Models/VoipFraudAlert.php) | No literal fillable array detected; inspect the model and API schema. |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [openapi/v1/billing-communications.yaml](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-api/openapi/v1/billing-communications.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#communications), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `billing-communications`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `billing-communications`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
