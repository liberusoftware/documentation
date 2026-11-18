# Accounting: Accounting Policies Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-policies). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-policies-nuxt`
**Matching domain module:** `accounting-policies`
**Application:** Accounting
**Source feature:** [Accounting Policies](../features/accounting-policies.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-policies.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-policies` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Effective-dated recognition:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Capitalization:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Depreciation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **FX:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tax:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rounding:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Write-off:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Materiality:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approval rules:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-policies-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `effective-dated-recognition`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `capitalization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `depreciation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fx`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tax`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rounding`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `write-off`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `materiality`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approval-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-policies` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-policies.md)) |
| Capability Nuxt module skeleton | [`module-accounting-policies-nuxt`](https://github.com/liberusoftware/module-accounting-policies-nuxt) (`@liberusoftware/module-accounting-policies-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Effective-dated recognition** | Expose composable and Vue 3 component for `effective-dated recognition` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-policies.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Capitalization** | Expose composable and Vue 3 component for `capitalization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-policies.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Depreciation** | Expose composable and Vue 3 component for `depreciation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-policies.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **FX** | Expose composable and Vue 3 component for `fx` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-policies.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Tax** | Expose composable and Vue 3 component for `tax` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-policies.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Rounding** | Expose composable and Vue 3 component for `rounding` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-policies.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Write-off** | Expose composable and Vue 3 component for `write-off` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-policies.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Materiality** | Expose composable and Vue 3 component for `materiality` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-policies.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approval rules** | Expose composable and Vue 3 component for `approval rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-policies.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PolicyRuleForDate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies/src/Queries/PolicyRuleForDate.php) | `public function handle(int\|string $bookId, PolicyCategory\|string $category, string $key, \DateTimeInterface\|string $date): ?PolicyRule` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SavePolicyRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies/src/Actions/SavePolicyRule.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(?PolicyRule $rule, array $attributes): PolicyRule` |
| [AccountingPoliciesPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies-api/src/Policies/AccountingPoliciesPolicy.php) | `public function viewAny(?Authenticatable $u): bool`<br>`public function view(?Authenticatable $u, PolicyRule $rule): bool`<br>`public function create(?Authenticatable $u): bool`<br>`public function update(?Authenticatable $u, PolicyRule $rule): bool`<br>`public function delete(?Authenticatable $u, PolicyRule $rule): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PolicyRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies/src/Models/PolicyRule.php) | `book_id`, `category`, `key`, `value`, `effective_from`, `effective_until`, `is_active`, `approved_by`, `approved_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PolicyRuleController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies-api/src/Http/Controllers/PolicyRuleController.php) | `public function index(Request $request)`<br>`public function show(string $rule): PolicyRuleResource`<br>`public function store(Request $request, SavePolicyRule $save)`<br>`public function update(Request $request, string $rule, SavePolicyRule $save): PolicyRuleResource`<br>`public function resolve(Request $request, PolicyRuleForDate $resolve)`<br>`public function destroy(string $rule): Response` |

**Observed route declarations:**

[modules/accounting-policies-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/accounting-policies')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('policies', [PolicyRuleController::class, 'index'])->middleware('ability:accounting.policies.read');
Route::get('policies/{rule}', [PolicyRuleController::class, 'show'])->middleware('ability:accounting.policies.read');
Route::post('policies', [PolicyRuleController::class, 'store'])->middleware('ability:accounting.policies.write');
Route::get('resolve', [PolicyRuleController::class, 'resolve'])->middleware('ability:accounting.policies.read');
Route::delete('policies/{rule}', [PolicyRuleController::class, 'destroy'])->middleware('ability:accounting.policies.write');
```
<!-- layer-implementation-plan:end -->
