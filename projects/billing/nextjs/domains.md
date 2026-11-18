# Domains: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter over a published capability skeleton, not a certified npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-billing-domains`.<br>
**Matching domain module:** `domains`

**Proposed design identifier:** `module-billing-domains-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope, skeleton repositories, and backend ownership

The [domain specification](../features/domains.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-billing-next-react`](https://github.com/liberusoftware/project-billing-next-react) | Application App Router shell, session/BFF boundary, layout, and route composition ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Product HTTP composition root publishing versioned `/api/v1` contracts ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/domains.md)) |
| Capability Next.js module skeleton | [module-billing-domains-nextjs](https://github.com/liberusoftware/module-billing-domains-nextjs) (`@liberusoftware/module-billing-domains-nextjs`) | Reusable React Server/Client component and typed DTO adapter ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-billing-domains](../../../modules/source/liberusoftware--module-billing-domains.md) |
| API | [liberusoftware/module-billing-domains-api](../../../modules/source/liberusoftware--module-billing-domains-api.md) |

## Module surfaces and component contracts

| Capability / feature aspect | Next.js Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Search** | Server Component loads authorized `search` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Contacts** | Server Component loads authorized `contacts` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Registration** | Server Component loads authorized `registration` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Transfer** | Server Component loads authorized `transfer` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Renewal** | Server Component loads authorized `renewal` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Redemption** | Server Component loads authorized `redemption` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **EPP** | Server Component loads authorized `epp` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **DNS** | Server Component loads authorized `dns` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Registrar adapters** | Server Component loads authorized `registrar adapters` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-billing-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ListDomainsRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Queries/ListDomainsRecords.php) | `public function handle(int $teamId): Collection` |
| [SearchDomains.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Queries/SearchDomains.php) | `public function __construct(private RegistrarManager $registrars)`<br>`public function execute(string $domain, string $registrar, array $suggestionTlds = ['com', 'net', 'org']): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
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
| [UpsertDomainTld.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Actions/UpsertDomainTld.php) | `public function execute(array $attributes): DomainTld` |
| [RegistrarClient.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Contracts/RegistrarClient.php) | `public function registerDomain(string $domainName, mixed $customerId): ?array`<br>`public function renewDomain(string $domainName, int $period): ?array`<br>`public function transferDomain(string $domainName, string $authCode, mixed $customerId): ?array`<br>`public function checkAvailability(string $domainName): bool`<br>`public function getAvailableTlds(): array`<br>`public function getDomainPrice(string $tld): float`<br>`public function getDnsRecords(string $domainName): array`<br>`public function addDnsRecord(string $domainName, array $record): bool`<br>`public function deleteDnsRecord(string $domainName, string $recordId): bool`<br>`public function getWhoisContacts(string $domainName): array`<br>`public function updateWhoisContacts(string $domainName, array $contacts): bool` |
| [DomainPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Policies/DomainPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, Domain $record): bool`<br>`public function update(?Authenticatable $user, Domain $record): bool`<br>`public function delete(?Authenticatable $user, Domain $record): bool` |
| [DomainSupportPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Policies/DomainSupportPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function update(?object $user, object $record): bool` |
| [DomainPricingService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Services/DomainPricingService.php) | `public function __construct(private RegistrarManager $registrars)`<br>`public function priceForDomain(float $basePrice, bool $bundledWithHosting): float`<br>`public function calculateDomainPrice(string $domainName): float`<br>`public function syncTlds(string $registrar, float $markupValue = 10): int` |
| [RegistrarManager.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Services/RegistrarManager.php) | `public function register(string $name, RegistrarClient $client): void`<br>`public function client(string $name): RegistrarClient` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [DnsRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/DnsRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [Domain.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/Domain.php) | No literal fillable array detected; inspect the model and API schema. |
| [DomainContact.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/DomainContact.php) | No literal fillable array detected; inspect the model and API schema. |
| [DomainTld.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/DomainTld.php) | No literal fillable array detected; inspect the model and API schema. |
| [EppOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-domains/src/Models/EppOperation.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

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
