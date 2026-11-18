# Billing: Module Billing Domains Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-domains). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-billing-module-billing-domains-nuxt`
**Matching domain module:** `module-billing-domains`
**Application:** Billing
**Source feature:** [Module Billing Domains](../features/module-billing-domains.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-billing-domains.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-billing-domains` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Search:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Contacts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Registration:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transfer:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Renewal:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Redemption:** page/component/composable/API-action behavior for this module's authorized workflow.
- **EPP:** page/component/composable/API-action behavior for this module's authorized workflow.
- **DNS:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Registrar adapters:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-billing-module-billing-domains-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `search`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `contacts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `registration`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transfer`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `renewal`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `redemption`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `epp`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dns`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `registrar-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `module-billing-domains` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-domains.md)) |
| Capability Nuxt module skeleton | [`module-billing-domains-nuxt`](https://github.com/liberusoftware/module-billing-domains-nuxt) (`@liberusoftware/module-billing-domains-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Search** | Expose composable and Vue 3 component for `search` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-domains.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Contacts** | Expose composable and Vue 3 component for `contacts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-domains.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Registration** | Expose composable and Vue 3 component for `registration` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-domains.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Transfer** | Expose composable and Vue 3 component for `transfer` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-domains.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Renewal** | Expose composable and Vue 3 component for `renewal` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-domains.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Redemption** | Expose composable and Vue 3 component for `redemption` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-domains.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **EPP** | Expose composable and Vue 3 component for `epp` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-domains.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **DNS** | Expose composable and Vue 3 component for `dns` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-domains.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Registrar adapters** | Expose composable and Vue 3 component for `registrar adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-domains.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |

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
