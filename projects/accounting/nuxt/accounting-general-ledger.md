# Accounting: Accounting General Ledger Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-general-ledger). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-general-ledger-nuxt`
**Matching domain module:** `accounting-general-ledger`
**Application:** Accounting
**Source feature:** [Accounting General Ledger](../features/accounting-general-ledger.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-general-ledger.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-general-ledger` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Journals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Balanced postings:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Recurring journals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reversals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Corrections:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Allocations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Accruals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Prepayments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Balances:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-general-ledger-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `journals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `balanced-postings`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `recurring-journals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reversals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `corrections`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `allocations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `accruals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `prepayments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `balances`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-general-ledger` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-general-ledger.md)) |
| Capability Nuxt module skeleton | [`module-accounting-general-ledger-nuxt`](https://github.com/liberusoftware/module-accounting-general-ledger-nuxt) (`@liberusoftware/module-accounting-general-ledger-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Journals** | Expose composable and Vue 3 component for `journals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-general-ledger.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Balanced postings** | Expose composable and Vue 3 component for `balanced postings` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-general-ledger.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Recurring journals** | Expose composable and Vue 3 component for `recurring journals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-general-ledger.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reversals** | Expose composable and Vue 3 component for `reversals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-general-ledger.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Corrections** | Expose composable and Vue 3 component for `corrections` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-general-ledger.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Allocations** | Expose composable and Vue 3 component for `allocations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-general-ledger.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Accruals** | Expose composable and Vue 3 component for `accruals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-general-ledger.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Prepayments** | Expose composable and Vue 3 component for `prepayments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-general-ledger.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Balances** | Expose composable and Vue 3 component for `balances` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-general-ledger.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AccountBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Queries/AccountBalances.php) | `public function handle(int $bookId, ?string $through = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAccrual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateAccrual.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreateAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateAllocation.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreateCorrection.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateCorrection.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreateJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateJournal.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreatePrepayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreatePrepayment.php) | `public function handle(array $attributes, array $lines): JournalEntry` |
| [CreateTypedJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/CreateTypedJournal.php) | `public function handle(JournalType $type, array $attributes, array $lines): JournalEntry` |
| [GenerateRecurringJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/GenerateRecurringJournal.php) | `public function handle(RecurringJournal $template, ?string $actor = null): JournalEntry` |
| [PostJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/PostJournal.php) | `public function handle(JournalEntry $journal, ?string $actor = null): JournalEntry` |
| [ReverseJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/ReverseJournal.php) | `public function handle(JournalEntry $journal, array $attributes = [], ?string $actor = null): JournalEntry` |
| [SaveRecurringJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Actions/SaveRecurringJournal.php) | `public function handle(array $attributes, ?RecurringJournal $template = null): RecurringJournal` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [JournalEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Models/JournalEntry.php) | `book_id`, `entry_number`, `entry_date`, `journal_type`, `status`, `description`, `source_type`, `source_id`, `reversal_of_id`, `posted_by`, `posted_at`, `metadata` |
| [JournalLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Models/JournalLine.php) | `journal_entry_id`, `account_id`, `debit`, `credit`, `description`, `dimensions` |
| [RecurringJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger/src/Models/RecurringJournal.php) | `book_id`, `name`, `frequency`, `next_run_on`, `end_on`, `is_active`, `description`, `lines`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [GeneralLedgerController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger-api/src/Http/Controllers/GeneralLedgerController.php) | `public function index(Request $request)`<br>`public function show(string $journal): JournalResource`<br>`public function store(Request $request, CreateJournal $create)`<br>`public function storeTyped(Request $request, string $type, CreateTypedJournal $create): JsonResource`<br>`public function post(Request $request, string $journal, PostJournal $post): JournalResource`<br>`public function reverse(Request $request, string $journal, ReverseJournal $reverse): JournalResource`<br>`public function balances(Request $request, AccountBalances $balances)`<br>`public function saveRecurring(Request $request, SaveRecurringJournal $save)`<br>`public function generateRecurring(Request $request, string $recurring, GenerateRecurringJournal $generate): JournalResource`<br>`public function destroy(string $journal): Response` |

**Observed route declarations:**

[modules/accounting-general-ledger-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-general-ledger-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/accounting/general-ledger')->group(function (): void {
Route::middleware('ability:accounting.general-ledger.read')->group(function (): void {
Route::get('/', [GeneralLedgerController::class, 'index']);
Route::get('/balances', [GeneralLedgerController::class, 'balances']);
Route::get('/{journal}', [GeneralLedgerController::class, 'show']);
Route::middleware('ability:accounting.general-ledger.write')->group(function (): void {
Route::post('/', [GeneralLedgerController::class, 'store']);
Route::post('/recurring', [GeneralLedgerController::class, 'saveRecurring']);
Route::post('/recurring/{recurring}/generate', [GeneralLedgerController::class, 'generateRecurring']);
Route::post('/'.$type, [GeneralLedgerController::class, 'storeTyped'])->defaults('type', $type);
}Route::post('/{journal}/post', [GeneralLedgerController::class, 'post']);
Route::post('/{journal}/reverse', [GeneralLedgerController::class, 'reverse']);
Route::delete('/{journal}', [GeneralLedgerController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
