# Accounting: Cash Collection Assistant Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cash-collection-assistant). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-cash-collection-assistant-nuxt`
**Matching domain module:** `accounting-cash-collection-assistant`
**Application:** Accounting
**Source feature:** [Cash Collection Assistant](../features/cash-collection-assistant.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/cash-collection-assistant.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-cash-collection-assistant` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Invoice-risk prioritization:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reminder drafts/timing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Promise tracking:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Policy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approval:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Outcome feedback:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-cash-collection-assistant-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `invoice-risk-prioritization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reminder-drafts-timing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `promise-tracking`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `policy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `outcome-feedback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-cash-collection-assistant` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cash-collection-assistant.md)) |
| Capability Nuxt module skeleton | [`module-accounting-cash-collection-assistant-nuxt`](https://github.com/liberusoftware/module-accounting-cash-collection-assistant-nuxt) (`@liberusoftware/module-accounting-cash-collection-assistant-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Invoice-risk prioritization** | Expose composable and Vue 3 component for `invoice-risk prioritization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cash-collection-assistant.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reminder drafts/timing** | Expose composable and Vue 3 component for `reminder drafts/timing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cash-collection-assistant.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Promise tracking** | Expose composable and Vue 3 component for `promise tracking` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cash-collection-assistant.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Policy** | Expose composable and Vue 3 component for `policy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cash-collection-assistant.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approval** | Expose composable and Vue 3 component for `approval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cash-collection-assistant.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Outcome feedback** | Expose composable and Vue 3 component for `outcome feedback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cash-collection-assistant.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CashCollectionAssistantQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Queries/CashCollectionAssistantQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCashCollectionAssistant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/CreateCashCollectionAssistant.php) | `public function handle(array $attributes): CashCollectionAssistant` |
| [RecordCollectionPromise.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/RecordCollectionPromise.php) | `public function handle(CashCollectionAssistant $assistant, string $date, string\|float $amount): CashCollectionAssistant` |
| [ScheduleCollectionReminder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/ScheduleCollectionReminder.php) | `public function handle(CashCollectionAssistant $assistant, string $at, ?string $draft = null): CashCollectionAssistant` |
| [SetCollectionDecision.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/SetCollectionDecision.php) | `public function handle(CashCollectionAssistant $assistant, string $field, string $value): CashCollectionAssistant` |
| [UpdateCashCollectionAssistant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/UpdateCashCollectionAssistant.php) | `public function handle(CashCollectionAssistant $assistant, array $attributes): CashCollectionAssistant` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CashCollectionAssistant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Models/CashCollectionAssistant.php) | `team_id`, `invoice_ref`, `customer_ref`, `risk_score`, `risk_level`, `reminder_status`, `reminder_at`, `promised_amount`, `promised_date`, `promise_status`, `policy_ref`, `approval_status`, `outcome`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CashCollectionAssistantsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant-api/src/Http/Controllers/CashCollectionAssistantsController.php) | `public function index(CashCollectionAssistantQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCashCollectionAssistant $action): JsonResponse`<br>`public function update(Request $request, string $assistant, UpdateCashCollectionAssistant $action): JsonResponse`<br>`public function reminder(Request $request, string $assistant, ScheduleCollectionReminder $action): JsonResponse`<br>`public function promise(Request $request, string $assistant, RecordCollectionPromise $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-cash-collection-assistant-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/cash-collection-assistant')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.cash-collection-assistant.read')->get('/', [CashCollectionAssistantsController::class, 'index']);
Route::middleware('ability:accounting.cash-collection-assistant.write')->group(function (): void {
Route::post('/', [CashCollectionAssistantsController::class, 'store']);
Route::post('/{assistant}/reminder', [CashCollectionAssistantsController::class, 'reminder']);
Route::post('/{assistant}/promise', [CashCollectionAssistantsController::class, 'promise']);
Route::patch('/{assistant}', [CashCollectionAssistantsController::class, 'update']);
```
<!-- layer-implementation-plan:end -->
