# Accounting: Bank Accounts Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#bank-accounts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-bank-accounts-vue-inertia`
**Matching domain module:** `accounting-bank-accounts`
**Application:** Accounting
**Source feature:** [Bank Accounts](../features/bank-accounts.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/bank-accounts.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Bank/current/savings/credit/loan/cash accounts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Ownership:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Currency:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Opening data:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Feeds:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Lifecycle:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Restricted details:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-bank-accounts-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `bank-current-savings-credit-loan-cash-accounts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `ownership`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `currency`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `opening-data`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `feeds`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `lifecycle`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `restricted-details`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-bank-accounts` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-bank-accounts-vue-inertia`](https://github.com/liberusoftware/module-accounting-bank-accounts-vue-inertia) (`@liberusoftware/module-accounting-bank-accounts-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/bank-accounts.md) · [Core plan](../core/bank-accounts.md) · [API plan](../api/bank-accounts.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Bank/current/savings/credit/loan/cash accounts** | Render `bank/current/savings/credit/loan/cash accounts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Ownership** | Render `ownership` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Currency** | Render `currency` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Opening data** | Render `opening data` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Feeds** | Render `feeds` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Lifecycle** | Render `lifecycle` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Restricted details** | Render `restricted details` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [BankAccountBalanceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Queries/BankAccountBalanceQuery.php) | `public function handle(?int $legalEntityId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateBankAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Actions/CreateBankAccount.php) | `public function handle(array $attributes): BankAccount` |
| [SetBankAccountStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Actions/SetBankAccountStatus.php) | `public function handle(BankAccount $account, BankAccountStatus $status): BankAccount` |
| [UpdateBankAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Actions/UpdateBankAccount.php) | `public function handle(BankAccount $account, array $attributes): BankAccount` |
| [BankAccountsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts-api/src/Policies/BankAccountsPolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $account): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $account): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BankAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Models/BankAccount.php) | `legal_entity_id`, `owner_type`, `owner_id`, `name`, `institution_name`, `account_type`, `currency`, `opening_balance`, `opening_date`, `current_balance`, `account_number`, `routing_number`, `feed_reference`, `status`, `closed_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [BankAccountController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts-api/src/Http/Controllers/BankAccountController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateBankAccount $action): BankAccountResource`<br>`public function show(string $bankAccount): BankAccountResource`<br>`public function update(Request $request, string $bankAccount, UpdateBankAccount $action): BankAccountResource`<br>`public function status(Request $request, string $bankAccount, SetBankAccountStatus $action): BankAccountResource`<br>`public function balances(Request $request, BankAccountBalanceQuery $query): JsonResponse` |

**Observed route declarations:**

[modules/accounting-bank-accounts-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/bank-accounts')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [BankAccountController::class, 'index'])->middleware('ability:accounting.bank-accounts.read');
Route::get('/balances', [BankAccountController::class, 'balances'])->middleware('ability:accounting.bank-accounts.read');
Route::get('/{bankAccount}', [BankAccountController::class, 'show'])->middleware('ability:accounting.bank-accounts.read');
Route::post('/', [BankAccountController::class, 'store'])->middleware('ability:accounting.bank-accounts.write');
Route::patch('/{bankAccount}', [BankAccountController::class, 'update'])->middleware('ability:accounting.bank-accounts.write');
Route::post('/{bankAccount}/status', [BankAccountController::class, 'status'])->middleware('ability:accounting.bank-accounts.write');
```
<!-- layer-implementation-plan:end -->
