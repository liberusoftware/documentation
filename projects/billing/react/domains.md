# Billing: Domains React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#domains). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-billing-domains-react-inertia`
**Matching domain module:** `billing-domains`
**Application:** Billing
**Source feature:** [Domains](../features/domains.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/domains.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Search:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Contacts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Registration:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Transfer:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Renewal:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Redemption:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **EPP:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **DNS:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Registrar adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-billing-domains-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `search`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `contacts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `registration`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `transfer`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `renewal`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `redemption`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `epp`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `dns`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `registrar-adapters`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `billing-domains` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-billing-laravel-inertia-react`](https://github.com/liberusoftware/project-billing-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-billing-domains-react-inertia`](https://github.com/liberusoftware/module-billing-domains-react-inertia) (`@liberusoftware/module-billing-domains-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/domains.md) · [Core plan](../core/domains.md) · [API plan](../api/domains.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Search** | Render `search` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Contacts** | Render `contacts` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Registration** | Render `registration` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Transfer** | Render `transfer` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Renewal** | Render `renewal` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Redemption** | Render `redemption` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **EPP** | Render `epp` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **DNS** | Render `dns` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Registrar adapters** | Render `registrar adapters` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

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
