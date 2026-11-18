# Billing: Module Billing Core Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-billing-module-billing-core-vue-inertia`
**Matching domain module:** `module-billing-core`
**Application:** Billing
**Source feature:** [Module Billing Core](../features/module-billing-core.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-billing-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Accounts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Contacts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Currencies:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tax profiles:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Sequences:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Terms:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Billing settings:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-billing-module-billing-core-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `accounts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `contacts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `currencies`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `tax-profiles`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `sequences`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `terms`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `billing-settings`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `module-billing-core` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-billing-laravel-inertia-vue`](https://github.com/liberusoftware/project-billing-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-billing-module-billing-core-vue-inertia`](https://github.com/liberusoftware/module-billing-module-billing-core-vue-inertia) (`@liberusoftware/module-billing-module-billing-core-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/module-billing-core.md) · [Core plan](../core/module-billing-core.md) · [API plan](../api/module-billing-core.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Accounts** | Render `accounts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Contacts** | Render `contacts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Currencies** | Render `currencies` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Tax profiles** | Render `tax profiles` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Sequences** | Render `sequences` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Terms** | Render `terms` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Billing settings** | Render `billing settings` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListBillingAccounts.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Queries/ListBillingAccounts.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListBillingRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Queries/ListBillingRecords.php) | `public function execute(string $modelClass, ?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CalculateTax.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CalculateTax.php) | `public function execute(int $teamId, float $amount, ?string $jurisdiction = null, ?int $customerId = null): array` |
| [ConvertCurrency.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/ConvertCurrency.php) | `public function execute(int $teamId, float $amount, string $from, string $to): array` |
| [CreateBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CreateBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): BillingAccount` |
| [CreateBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CreateBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(string $modelClass, array $attributes): Model` |
| [DeleteBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/DeleteBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account): void` |
| [DeleteBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/DeleteBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Model $record, string $recordType): void` |
| [TransitionBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/TransitionBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account, BillingAccountStatus $status): BillingAccount` |
| [UpdateBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/UpdateBillingAccount.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(BillingAccount $account, array $attributes): BillingAccount` |
| [UpdateBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/UpdateBillingRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Model $record, array $attributes): Model` |
| [BillingAccountPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Policies/BillingAccountPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, BillingAccount $account): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, BillingAccount $account): bool`<br>`public function delete(object $user, BillingAccount $account): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingContact.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingContact.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingCurrency.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingCurrency.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingSequence.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingSetting.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingSetting.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTaxExemption.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTaxExemption.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTaxProfile.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTaxProfile.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTerm.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTerm.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [BillingAccountController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-api/src/Http/Controllers/BillingAccountController.php) | `public function index(Request $request, ListBillingAccounts $query): JsonResponse`<br>`public function store(Request $request, CreateBillingAccount $create): JsonResponse`<br>`public function update(Request $request, int $account, UpdateBillingAccount $update): JsonResponse`<br>`public function transition(Request $request, int $account, TransitionBillingAccount $transition): JsonResponse`<br>`public function destroy(Request $request, int $account, DeleteBillingAccount $delete): JsonResponse` |
| [BillingCoreRecordController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-api/src/Http/Controllers/BillingCoreRecordController.php) | `public function index(Request $request, string $type, ListBillingRecords $list): JsonResponse`<br>`public function store(Request $request, string $type, CreateBillingRecord $create): JsonResponse`<br>`public function convertCurrency(Request $request, ConvertCurrency $convert): JsonResponse`<br>`public function calculateTax(Request $request, CalculateTax $calculate): JsonResponse`<br>`public function update(Request $request, string $type, int $record, UpdateBillingRecord $update): JsonResponse`<br>`public function destroy(Request $request, string $type, int $record, DeleteBillingRecord $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-core-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.billing-core.read'])
Route::get('/', [BillingAccountController::class, 'index'])->name('accounts.index');
Route::post('/currencies/convert', [BillingCoreRecordController::class, 'convertCurrency'])->name('currencies.convert');
Route::post('/tax/calculate', [BillingCoreRecordController::class, 'calculateTax'])->name('tax.calculate');
Route::get('/{type}', [BillingCoreRecordController::class, 'index'])->whereIn('type', ['contacts', 'currencies', 'tax-profiles', 'tax-exemptions', 'sequences', 'terms', 'settings'])->name('records.index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.billing-core.write', 'idempotency'])
Route::post('/', [BillingAccountController::class, 'store'])->name('accounts.store');
Route::patch('/{account}', [BillingAccountController::class, 'update'])->whereNumber('account')->name('accounts.update');
Route::delete('/{account}', [BillingAccountController::class, 'destroy'])->whereNumber('account')->name('accounts.destroy');
Route::patch('/{account}/status', [BillingAccountController::class, 'transition'])->whereNumber('account')->name('accounts.status');
Route::post('/{type}', [BillingCoreRecordController::class, 'store'])->whereIn('type', ['contacts', 'currencies', 'tax-profiles', 'tax-exemptions', 'sequences', 'terms', 'settings'])->name('records.store');
Route::patch('/{type}/{record}', [BillingCoreRecordController::class, 'update'])->whereIn('type', ['contacts', 'currencies', 'tax-profiles', 'tax-exemptions', 'sequences', 'terms', 'settings'])->name('records.update');
Route::delete('/{type}/{record}', [BillingCoreRecordController::class, 'destroy'])->whereIn('type', ['contacts', 'currencies', 'tax-profiles', 'tax-exemptions', 'sequences', 'terms', 'settings'])->name('records.destroy');
```
<!-- layer-implementation-plan:end -->
