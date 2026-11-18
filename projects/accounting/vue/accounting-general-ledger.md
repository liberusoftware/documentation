# Accounting: Accounting General Ledger Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-general-ledger). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-accounting-general-ledger-vue-inertia`
**Matching domain module:** `accounting-general-ledger`
**Application:** Accounting
**Source feature:** [Accounting General Ledger](../features/accounting-general-ledger.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-general-ledger.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Journals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Balanced postings:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Recurring journals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reversals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Corrections:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Allocations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Accruals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Prepayments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Balances:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-general-ledger-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `journals`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `balanced-postings`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `recurring-journals`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `reversals`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `corrections`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `allocations`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `accruals`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `prepayments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `balances`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-general-ledger` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-general-ledger-vue-inertia`](https://github.com/liberusoftware/module-accounting-general-ledger-vue-inertia) (`@liberusoftware/module-accounting-general-ledger-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/accounting-general-ledger.md) · [Core plan](../core/accounting-general-ledger.md) · [API plan](../api/accounting-general-ledger.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Journals** | Render `journals` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Balanced postings** | Render `balanced postings` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Recurring journals** | Render `recurring journals` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Reversals** | Render `reversals` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Corrections** | Render `corrections` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Allocations** | Render `allocations` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Accruals** | Render `accruals` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Prepayments** | Render `prepayments` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Balances** | Render `balances` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
