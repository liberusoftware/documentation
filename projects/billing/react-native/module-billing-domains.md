# Module Billing Domains React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-domains). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-billing-module-billing-domains-react-native
**Matching core package:** module-billing-module-billing-domains ([implementation](../core/module-billing-domains.md))
**Matching API package:** module-billing-module-billing-domains-api ([contract](../api/module-billing-domains.md))

## Implementation plan

This adapter presents Module Billing Domains for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Billing Domains API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/module-billing-domains.md), and [API module](../api/module-billing-domains.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `module-billing-domains`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-billing-mobile-react`](https://github.com/liberusoftware/project-billing-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-domains.md)) |
| Capability React Native module skeleton | [`module-billing-domains-react-native`](https://github.com/liberusoftware/module-billing-domains-react-native) (`@liberusoftware/module-billing-domains-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Search** | Progressive mobile list/detail/sheet flow for `search` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Contacts** | Progressive mobile list/detail/sheet flow for `contacts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Registration** | Progressive mobile list/detail/sheet flow for `registration` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Transfer** | Progressive mobile list/detail/sheet flow for `transfer` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Renewal** | Progressive mobile list/detail/sheet flow for `renewal` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Redemption** | Progressive mobile list/detail/sheet flow for `redemption` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **EPP** | Progressive mobile list/detail/sheet flow for `epp` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **DNS** | Progressive mobile list/detail/sheet flow for `dns` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Registrar adapters** | Progressive mobile list/detail/sheet flow for `registrar adapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListDomainsRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Queries/ListDomainsRecords.php) | `public function handle(int $teamId): Collection` |
| [SearchDomains.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Queries/SearchDomains.php) | `public function __construct(private RegistrarManager $registrars)`<br>`public function execute(string $domain, string $registrar, array $suggestionTlds = ['com', 'net', 'org']): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/CreateDomain.php) | `public function handle(int $teamId, array $attributes): Domain` |
| [CreateDomainContact.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/CreateDomainContact.php) | `public function execute(int $teamId, array $attributes): DomainContact` |
| [DeleteDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/DeleteDomain.php) | `public function execute(Domain $domain): void` |
| [RecordEppOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/RecordEppOperation.php) | `public function execute(Domain $domain, string $operation, string $status, array $payload = [], ?string $eppCode = null): EppOperation` |
| [RedeemDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/RedeemDomain.php) | `public function execute(Domain $domain): Domain` |
| [RegisterDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/RegisterDomain.php) | `public function __construct(private DatabaseManager $database, private RegistrarManager $registrars)`<br>`public function execute(Domain $domain, mixed $customerId): Domain` |
| [RenewDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/RenewDomain.php) | `public function __construct(private DatabaseManager $database, private RegistrarManager $registrars)`<br>`public function execute(Domain $domain, int $period = 1): Domain` |
| [TransferDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/TransferDomain.php) | `public function __construct(private DatabaseManager $database, private RegistrarManager $registrars)`<br>`public function execute(Domain $domain, string $authCode, mixed $customerId, ?string $registrar = null): Domain` |
| [UpdateDomain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/UpdateDomain.php) | `public function handle(Domain $domain, array $attributes): Domain` |
| [UpsertDnsRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/UpsertDnsRecord.php) | `public function execute(int $teamId, array $attributes): DnsRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DnsRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/DnsRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [Domain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/Domain.php) | No literal fillable array detected; inspect the model and API schema. |
| [DomainContact.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/DomainContact.php) | No literal fillable array detected; inspect the model and API schema. |
| [DomainTld.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/DomainTld.php) | No literal fillable array detected; inspect the model and API schema. |
| [EppOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/EppOperation.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [DomainController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-api/src/Http/Controllers/DomainController.php) | `public function tlds(Request $request): JsonResponse`<br>`public function syncTlds(Request $request, DomainPricingService $pricing): JsonResponse`<br>`public function storeTld(Request $request, UpsertDomainTld $upsert): JsonResponse`<br>`public function index(Request $request): JsonResponse`<br>`public function show(Request $request, Domain $domain): JsonResponse`<br>`public function store(Request $request, CreateDomain $create): JsonResponse`<br>`public function update(Request $request, Domain $domain, UpdateDomain $update): JsonResponse`<br>`public function destroy(Request $request, Domain $domain, DeleteDomain $delete): JsonResponse`<br>`public function search(Request $request, SearchDomains $search): JsonResponse`<br>`public function register(Request $request, Domain $domain, RegisterDomain $register): JsonResponse`<br>`public function renew(Request $request, Domain $domain, RenewDomain $renew): JsonResponse`<br>`public function transfer(Request $request, Domain $domain, TransferDomain $transfer): JsonResponse`<br>`public function contacts(Request $request): JsonResponse`<br>`public function eppOperations(Request $request): JsonResponse`<br>`public function storeContact(Request $request, CreateDomainContact $create): JsonResponse`<br>`public function dns(Request $request, Domain $domain): JsonResponse`<br>`public function storeDns(Request $request, Domain $domain, UpsertDnsRecord $upsert): JsonResponse`<br>`public function redeem(Request $request, Domain $domain, RedeemDomain $redeem): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-domains-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.domains.read'])->prefix('api/v1/billing/domains')->group(function (): void {
Route::get('/search', [DomainController::class, 'search']);
Route::get('/tlds', [DomainController::class, 'tlds']);
Route::get('/contacts', [DomainController::class, 'contacts']);
Route::get('/epp-operations', [DomainController::class, 'eppOperations']);
Route::get('/{domain}/dns', [DomainController::class, 'dns']);
Route::get('/', [DomainController::class, 'index']);
Route::get('/{domain}', [DomainController::class, 'show']);
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.domains.write', 'idempotency'])->prefix('api/v1/billing/domains')->group(function (): void {
Route::post('/', [DomainController::class, 'store']);
Route::post('/tlds', [DomainController::class, 'storeTld']);
Route::post('/tlds/sync', [DomainController::class, 'syncTlds']);
Route::patch('/{domain}', [DomainController::class, 'update']);
Route::delete('/{domain}', [DomainController::class, 'destroy']);
Route::post('/{domain}/register', [DomainController::class, 'register']);
Route::post('/{domain}/renew', [DomainController::class, 'renew']);
Route::post('/{domain}/transfer', [DomainController::class, 'transfer']);
Route::post('/contacts', [DomainController::class, 'storeContact']);
Route::post('/{domain}/dns', [DomainController::class, 'storeDns']);
Route::post('/{domain}/redeem', [DomainController::class, 'redeem']);
```
<!-- layer-implementation-plan:end -->
