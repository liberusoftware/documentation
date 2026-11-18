# Accounting: Accounting Corporate Cards Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-corporate-cards). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-corporate-cards-nuxt`
**Matching domain module:** `accounting-corporate-cards`
**Application:** Accounting
**Source feature:** [Accounting Corporate Cards](../features/accounting-corporate-cards.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-corporate-cards.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-corporate-cards` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Card accounts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Holders:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Feeds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Controls references:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transaction assignment:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Receipt collection:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Coding:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approval:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-corporate-cards-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `card-accounts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `holders`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `feeds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `controls-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transaction-assignment`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `receipt-collection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `coding`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-corporate-cards` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-corporate-cards.md)) |
| Capability Nuxt module skeleton | [`module-accounting-corporate-cards-nuxt`](https://github.com/liberusoftware/module-accounting-corporate-cards-nuxt) (`@liberusoftware/module-accounting-corporate-cards-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Card accounts** | Expose composable and Vue 3 component for `card accounts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-corporate-cards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Holders** | Expose composable and Vue 3 component for `holders` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-corporate-cards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Feeds** | Expose composable and Vue 3 component for `feeds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-corporate-cards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Controls references** | Expose composable and Vue 3 component for `controls references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-corporate-cards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Transaction assignment** | Expose composable and Vue 3 component for `transaction assignment` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-corporate-cards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Receipt collection** | Expose composable and Vue 3 component for `receipt collection` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-corporate-cards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Coding** | Expose composable and Vue 3 component for `coding` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-corporate-cards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approval** | Expose composable and Vue 3 component for `approval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-corporate-cards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-corporate-cards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CorporateCardQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-corporate-cards/src/Queries/CorporateCardQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveCardTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-corporate-cards/src/Actions/ApproveCardTransaction.php) | `public function handle(CardTransaction $transaction, int $actor): CardTransaction` |
| [CodeCardTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-corporate-cards/src/Actions/CodeCardTransaction.php) | `public function handle(CardTransaction $transaction, string $category, ?string $receipt = null): CardTransaction` |
| [CreateCardAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-corporate-cards/src/Actions/CreateCardAccount.php) | `public function handle(array $attributes): CardAccount` |
| [ReconcileCardTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-corporate-cards/src/Actions/ReconcileCardTransaction.php) | `public function handle(CardTransaction $transaction, string $reference): CardTransaction` |
| [RecordCardTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-corporate-cards/src/Actions/RecordCardTransaction.php) | `public function handle(CardAccount $account, array $attributes): CardTransaction` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CardAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-corporate-cards/src/Models/CardAccount.php) | `team_id`, `card_ref`, `holder_ref`, `provider_ref`, `currency`, `limit_amount`, `spent_amount`, `status`, `controls` |
| [CardTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-corporate-cards/src/Models/CardTransaction.php) | `card_account_id`, `team_id`, `transaction_ref`, `transaction_date`, `amount`, `currency`, `merchant_ref`, `status`, `category_ref`, `receipt_ref`, `feed_ref`, `approved_by`, `approved_at`, `reconciliation_ref`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CorporateCardsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-corporate-cards-api/src/Http/Controllers/CorporateCardsController.php) | `public function index(CorporateCardQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCardAccount $action): JsonResponse`<br>`public function transaction(Request $request, string $account, RecordCardTransaction $action): JsonResponse`<br>`public function code(Request $request, string $transaction, CodeCardTransaction $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-corporate-cards-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-corporate-cards-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/corporate-cards')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.corporate-cards.read')->get('/', [CorporateCardsController::class, 'index']);
Route::middleware('ability:accounting.corporate-cards.write')->group(function (): void {
Route::post('/', [CorporateCardsController::class, 'store']);
Route::post('/{account}/transactions', [CorporateCardsController::class, 'transaction']);
Route::post('/transactions/{transaction}/code', [CorporateCardsController::class, 'code']);
```
<!-- layer-implementation-plan:end -->
