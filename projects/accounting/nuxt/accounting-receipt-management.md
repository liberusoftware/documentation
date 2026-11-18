# Accounting: Accounting Receipt Management Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-receipt-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-receipt-management-nuxt`
**Matching domain module:** `accounting-receipt-management`
**Application:** Accounting
**Source feature:** [Accounting Receipt Management](../features/accounting-receipt-management.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-receipt-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-receipt-management` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Receipt inbox:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Matching to bank/card/expense/bill:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Missing-receipt requests:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Annotations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Retention:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Audit:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-receipt-management-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `receipt-inbox`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `matching-to-bank-card-expense-bill`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `missing-receipt-requests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `annotations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `retention`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `audit`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-receipt-management` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-receipt-management.md)) |
| Capability Nuxt module skeleton | [`module-accounting-receipt-management-nuxt`](https://github.com/liberusoftware/module-accounting-receipt-management-nuxt) (`@liberusoftware/module-accounting-receipt-management-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Receipt inbox** | Expose composable and Vue 3 component for `receipt inbox` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-receipt-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Matching to bank/card/expense/bill** | Expose composable and Vue 3 component for `matching to bank/card/expense/bill` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-receipt-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Missing-receipt requests** | Expose composable and Vue 3 component for `missing-receipt requests` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-receipt-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Annotations** | Expose composable and Vue 3 component for `annotations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-receipt-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Retention** | Expose composable and Vue 3 component for `retention` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-receipt-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Audit** | Expose composable and Vue 3 component for `audit` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-receipt-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [IngestReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Actions/IngestReceipt.php) | `public function handle(array $attributes): Receipt` |
| [MatchReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Actions/MatchReceipt.php) | `public function handle(Receipt $receipt, array $attributes): ReceiptMatch` |
| [RequestMissingReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Actions/RequestMissingReceipt.php) | `public function handle(array $attributes): MissingReceiptRequest` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MissingReceiptRequest.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Models/MissingReceiptRequest.php) | `team_id`, `receipt_id`, `requestee_ref`, `target_type`, `target_id`, `reason`, `status`, `due_on`, `fulfilled_at`, `metadata` |
| [Receipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Models/Receipt.php) | `team_id`, `file_ref`, `source_type`, `source_id`, `merchant`, `amount`, `currency`, `receipt_date`, `status`, `retention_until`, `metadata` |
| [ReceiptAnnotation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Models/ReceiptAnnotation.php) | `receipt_id`, `author_ref`, `body`, `visibility`, `metadata` |
| [ReceiptAudit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Models/ReceiptAudit.php) | `receipt_id`, `action`, `actor_ref`, `evidence`, `created_at` |
| [ReceiptMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management/src/Models/ReceiptMatch.php) | `receipt_id`, `target_type`, `target_id`, `matched_amount`, `status`, `confidence`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReceiptManagementController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management-api/src/Http/Controllers/ReceiptManagementController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, IngestReceipt $action): mixed`<br>`public function show(Request $request, Receipt $receipt): Receipt`<br>`public function match(Request $request, Receipt $receipt, MatchReceipt $action): mixed`<br>`public function requestMissing(Request $request, RequestMissingReceipt $action): mixed` |

**Observed route declarations:**

[modules/accounting-receipt-management-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-receipt-management-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/receipt-management')->group(function (): void {
Route::middleware('ability:accounting.receipt-management.read')->group(function (): void {
Route::get('/', [ReceiptManagementController::class, 'index']);
Route::get('/{receipt}', [ReceiptManagementController::class, 'show']);
Route::middleware('ability:accounting.receipt-management.write')->group(function (): void {
Route::post('/', [ReceiptManagementController::class, 'store']);
Route::post('/{receipt}/match', [ReceiptManagementController::class, 'match']);
Route::post('/missing-requests', [ReceiptManagementController::class, 'requestMissing']);
```
<!-- layer-implementation-plan:end -->
