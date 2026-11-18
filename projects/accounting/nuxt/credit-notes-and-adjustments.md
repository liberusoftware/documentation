# Accounting: Credit Notes and Adjustments Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#credit-notes-and-adjustments). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-credit-notes-and-adjustments-nuxt`
**Matching domain module:** `accounting-credit-notes-and-adjustments`
**Application:** Accounting
**Source feature:** [Credit Notes and Adjustments](../features/credit-notes-and-adjustments.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/credit-notes-and-adjustments.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-credit-notes-and-adjustments` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Full/partial credits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reasons:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approval:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Invoice allocation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Refund/store-credit references:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tax correction:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Audit:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-credit-notes-and-adjustments-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `full-partial-credits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reasons`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `invoice-allocation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `refund-store-credit-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tax-correction`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
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

- Package identity, public exports, API dependency, and module dependency match `accounting-credit-notes-and-adjustments` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/credit-notes-and-adjustments.md)) |
| Capability Nuxt module skeleton | [`module-accounting-credit-notes-and-adjustments-nuxt`](https://github.com/liberusoftware/module-accounting-credit-notes-and-adjustments-nuxt) (`@liberusoftware/module-accounting-credit-notes-and-adjustments-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Full/partial credits** | Expose composable and Vue 3 component for `full/partial credits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/credit-notes-and-adjustments.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reasons** | Expose composable and Vue 3 component for `reasons` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/credit-notes-and-adjustments.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approval** | Expose composable and Vue 3 component for `approval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/credit-notes-and-adjustments.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Invoice allocation** | Expose composable and Vue 3 component for `invoice allocation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/credit-notes-and-adjustments.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Refund/store-credit references** | Expose composable and Vue 3 component for `refund/store-credit references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/credit-notes-and-adjustments.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Tax correction** | Expose composable and Vue 3 component for `tax correction` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/credit-notes-and-adjustments.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Audit** | Expose composable and Vue 3 component for `audit` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/credit-notes-and-adjustments.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CreditNoteQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Queries/CreditNoteQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateCreditNote.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Actions/AllocateCreditNote.php) | `public function handle(CreditNote $note, string $invoiceRef, float $amount): CreditNoteAllocation` |
| [ApproveCreditNote.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Actions/ApproveCreditNote.php) | `public function handle(CreditNote $note, int $actor): CreditNote` |
| [CreateCreditNote.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Actions/CreateCreditNote.php) | `public function handle(array $attributes): CreditNote` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CreditNote.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Models/CreditNote.php) | `team_id`, `customer_id`, `credit_ref`, `status`, `reason`, `currency`, `amount`, `allocated_amount`, `tax_amount`, `refund_reference`, `store_credit_reference`, `approved_by`, `approved_at`, `evidence`, `metadata` |
| [CreditNoteAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Models/CreditNoteAllocation.php) | `credit_note_id`, `team_id`, `invoice_ref`, `amount` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CreditNotesController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments-api/src/Http/Controllers/CreditNotesController.php) | `public function index(CreditNoteQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCreditNote $action): JsonResponse`<br>`public function approve(Request $request, string $note, ApproveCreditNote $action): JsonResponse`<br>`public function allocate(Request $request, string $note, AllocateCreditNote $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-credit-notes-and-adjustments-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/credit-notes-and-adjustments')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.credit-notes-and-adjustments.read')->get('/', [CreditNotesController::class, 'index']);
Route::middleware('ability:accounting.credit-notes-and-adjustments.write')->group(function (): void {
Route::post('/', [CreditNotesController::class, 'store']);
Route::post('/{note}/approve', [CreditNotesController::class, 'approve']);
Route::post('/{note}/allocations', [CreditNotesController::class, 'allocate']);
```
<!-- layer-implementation-plan:end -->
