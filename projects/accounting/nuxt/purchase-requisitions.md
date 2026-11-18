# Accounting: Purchase Requisitions Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#purchase-requisitions). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-purchase-requisitions-nuxt`
**Matching domain module:** `accounting-purchase-requisitions`
**Application:** Accounting
**Source feature:** [Purchase Requisitions](../features/purchase-requisitions.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/purchase-requisitions.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-purchase-requisitions` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Requests:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Coding:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Budgets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attachments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approvals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sourcing handoff:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Conversion:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Status:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-purchase-requisitions-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `requests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `coding`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `budgets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `attachments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approvals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sourcing-handoff`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `conversion`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `status`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-purchase-requisitions` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/purchase-requisitions.md)) |
| Capability Nuxt module skeleton | [`module-accounting-purchase-requisitions-nuxt`](https://github.com/liberusoftware/module-accounting-purchase-requisitions-nuxt) (`@liberusoftware/module-accounting-purchase-requisitions-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Requests** | Expose composable and Vue 3 component for `requests` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/purchase-requisitions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Coding** | Expose composable and Vue 3 component for `coding` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/purchase-requisitions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Budgets** | Expose composable and Vue 3 component for `budgets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/purchase-requisitions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Attachments** | Expose composable and Vue 3 component for `attachments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/purchase-requisitions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approvals** | Expose composable and Vue 3 component for `approvals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/purchase-requisitions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Sourcing handoff** | Expose composable and Vue 3 component for `sourcing handoff` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/purchase-requisitions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Conversion** | Expose composable and Vue 3 component for `conversion` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/purchase-requisitions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Status** | Expose composable and Vue 3 component for `status` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/purchase-requisitions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateRequisition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions/src/Actions/CreateRequisition.php) | `public function handle(array $attributes): PurchaseRequisition` |
| [RecordApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions/src/Actions/RecordApproval.php) | `public function handle(PurchaseRequisition $requisition, array $attributes): RequisitionApproval` |
| [TransitionRequisition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions/src/Actions/TransitionRequisition.php) | `public function handle(PurchaseRequisition $requisition, RequisitionStatus $status, array $attributes = []): PurchaseRequisition` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PurchaseRequisition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions/src/Models/PurchaseRequisition.php) | `team_id`, `requester_ref`, `title`, `currency`, `total_amount`, `lines`, `coding`, `budget`, `attachments`, `status`, `submitted_at`, `approved_at`, `sourcing_ref`, `converted_ref`, `metadata` |
| [RequisitionApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions/src/Models/RequisitionApproval.php) | `requisition_id`, `approver_ref`, `decision`, `reason`, `decided_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PurchaseRequisitionsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions-api/src/Http/Controllers/PurchaseRequisitionsController.php) | `public function index(Request $request): AnonymousResourceCollection`<br>`public function store(Request $request, CreateRequisition $action): JsonResponse`<br>`public function show(Request $request, PurchaseRequisition $requisition): PurchaseRequisitionResource`<br>`public function transition(Request $request, PurchaseRequisition $requisition, TransitionRequisition $action): PurchaseRequisitionResource`<br>`public function approve(Request $request, PurchaseRequisition $requisition, RecordApproval $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-purchase-requisitions-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/purchase-requisitions')->group(function (): void {
Route::middleware('ability:accounting.purchase-requisitions.read')->group(function (): void {
Route::get('/', [PurchaseRequisitionsController::class, 'index']);
Route::get('/{requisition}', [PurchaseRequisitionsController::class, 'show']);
Route::middleware('ability:accounting.purchase-requisitions.write')->group(function (): void {
Route::post('/', [PurchaseRequisitionsController::class, 'store']);
Route::post('/{requisition}/transition', [PurchaseRequisitionsController::class, 'transition']);
Route::post('/{requisition}/approve', [PurchaseRequisitionsController::class, 'approve']);
```
<!-- layer-implementation-plan:end -->
