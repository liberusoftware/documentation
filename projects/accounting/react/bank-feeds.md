# Accounting: Bank Feeds React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#bank-feeds). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-bank-feeds-react-inertia`
**Matching domain module:** `accounting-bank-feeds`
**Application:** Accounting
**Source feature:** [Bank Feeds](../features/bank-feeds.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/bank-feeds.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Consent/connections:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Institutions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Account mapping:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Cursors:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Imports:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Duplicates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Pending/posted state:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Health:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Provider adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-bank-feeds-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `consent-connections`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `institutions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `account-mapping`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `cursors`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `imports`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `duplicates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `pending-posted-state`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `health`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `provider-adapters`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-bank-feeds` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-bank-feeds-react-inertia`](https://github.com/liberusoftware/module-accounting-bank-feeds-react-inertia) (`@liberusoftware/module-accounting-bank-feeds-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/bank-feeds.md) · [Core plan](../core/bank-feeds.md) · [API plan](../api/bank-feeds.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Consent/connections** | Render `consent/connections` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Institutions** | Render `institutions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Account mapping** | Render `account mapping` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Cursors** | Render `cursors` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Imports** | Render `imports` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Duplicates** | Render `duplicates` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Pending/posted state** | Render `pending/posted state` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Health** | Render `health` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Provider adapters** | Render `provider adapters` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [BankFeedQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Queries/BankFeedQuery.php) | `public function connections(?int $teamId = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateBankFeedConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/CreateBankFeedConnection.php) | `public function handle(array $attributes): BankFeedConnection` |
| [ImportBankFeedTransactions.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/ImportBankFeedTransactions.php) | `public function handle(BankFeedConnection $connection, array $batch): array` |
| [MapBankFeedAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/MapBankFeedAccount.php) | `public function handle(BankFeedConnection $connection, array $attributes): BankFeedAccountMapping` |
| [SetBankFeedTransactionStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/SetBankFeedTransactionStatus.php) | `public function handle(BankFeedTransaction $transaction, FeedTransactionStatus $status): BankFeedTransaction` |
| [UpdateBankFeedHealth.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/UpdateBankFeedHealth.php) | `public function handle(BankFeedConnection $connection, ?string $error = null): BankFeedConnection` |
| [UpsertBankFeedInstitution.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Actions/UpsertBankFeedInstitution.php) | `public function handle(array $attributes): BankFeedInstitution` |
| [BankFeedAdapter.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Contracts/BankFeedAdapter.php) | `public function fetch(BankFeedConnection $connection): array` |
| [BankFeedsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds-api/src/Policies/BankFeedsPolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $connection): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $connection): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BankFeedAccountMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedAccountMapping.php) | `team_id`, `connection_id`, `bank_account_id`, `external_account_id`, `name`, `currency`, `metadata` |
| [BankFeedConnection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedConnection.php) | `team_id`, `user_id`, `institution_id`, `provider`, `name`, `external_reference`, `access_token`, `credentials`, `cursor`, `status`, `last_synced_at`, `last_error`, `last_error_at`, `metadata` |
| [BankFeedInstitution.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedInstitution.php) | `provider`, `external_id`, `name`, `country`, `logo_url`, `metadata` |
| [BankFeedTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds/src/Models/BankFeedTransaction.php) | `team_id`, `connection_id`, `mapping_id`, `external_id`, `transaction_date`, `posted_date`, `description`, `amount`, `currency`, `status`, `category`, `raw_data`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [BankFeedController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds-api/src/Http/Controllers/BankFeedController.php) | `public function index(Request $request): mixed`<br>`public function show(string $connection): BankFeedResource`<br>`public function institution(Request $request, UpsertBankFeedInstitution $action): mixed`<br>`public function store(Request $request, CreateBankFeedConnection $action): BankFeedResource`<br>`public function map(Request $request, string $connection, MapBankFeedAccount $action): mixed`<br>`public function import(Request $request, string $connection, ImportBankFeedTransactions $action): mixed` |

**Observed route declarations:**

[modules/accounting-bank-feeds-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-feeds-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/bank-feeds')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [BankFeedController::class, 'index'])->middleware('ability:accounting.bank-feeds.read');
Route::post('/institutions', [BankFeedController::class, 'institution'])->middleware('ability:accounting.bank-feeds.write');
Route::post('/', [BankFeedController::class, 'store'])->middleware('ability:accounting.bank-feeds.write');
Route::get('/{connection}', [BankFeedController::class, 'show'])->middleware('ability:accounting.bank-feeds.read');
Route::post('/{connection}/mapping', [BankFeedController::class, 'map'])->middleware('ability:accounting.bank-feeds.write');
Route::post('/{connection}/imports', [BankFeedController::class, 'import'])->middleware('ability:accounting.bank-feeds.write');
```
<!-- layer-implementation-plan:end -->
