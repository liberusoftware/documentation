# Accounting: Accounting Bank Rules Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-bank-rules). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-bank-rules-nuxt`
**Matching domain module:** `accounting-bank-rules`
**Application:** Accounting
**Source feature:** [Accounting Bank Rules](../features/accounting-bank-rules.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-bank-rules.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-bank-rules` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Payee/text/amount/account conditions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Split/category/tax/dimension actions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Priority:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Suggestions/automation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Testing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **History:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-bank-rules-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `payee-text-amount-account-conditions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `split-category-tax-dimension-actions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `priority`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `suggestions-automation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `testing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-bank-rules` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-bank-rules.md)) |
| Capability Nuxt module skeleton | [`module-accounting-bank-rules-nuxt`](https://github.com/liberusoftware/module-accounting-bank-rules-nuxt) (`@liberusoftware/module-accounting-bank-rules-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Payee/text/amount/account conditions** | Expose composable and Vue 3 component for `payee/text/amount/account conditions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-bank-rules.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Split/category/tax/dimension actions** | Expose composable and Vue 3 component for `split/category/tax/dimension actions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-bank-rules.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Priority** | Expose composable and Vue 3 component for `priority` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-bank-rules.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Suggestions/automation** | Expose composable and Vue 3 component for `suggestions/automation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-bank-rules.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Testing** | Expose composable and Vue 3 component for `testing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-bank-rules.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **History** | Expose composable and Vue 3 component for `history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-bank-rules.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [BankRuleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Queries/BankRuleQuery.php) | `public function forTeam(int $teamId): Builder`<br>`public function matching(int $teamId, array $transaction): array`<br>`public function matches(array $conditions, array $transaction): bool` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordBankRuleDecision.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Actions/RecordBankRuleDecision.php) | `public function handle(BankRule $rule, string $transactionReference, bool $matched, string $outcome, array $actionsApplied = [], ?string $actorReference = null): BankRuleHistory` |
| [SaveBankRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Actions/SaveBankRule.php) | `public function handle(array $attributes, ?BankRule $rule = null): BankRule` |
| [TestBankRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Actions/TestBankRule.php) | `public function __construct(private readonly BankRuleQuery $query)`<br>`public function handle(BankRule $rule, array $transaction): array` |
| [BankRulesPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules-api/src/Policies/BankRulesPolicy.php) | `public function viewAny($user): bool`<br>`public function view($user, BankRule $rule): bool`<br>`public function create($user): bool`<br>`public function update($user, BankRule $rule): bool`<br>`public function delete($user, BankRule $rule): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BankRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Models/BankRule.php) | `team_id`, `name`, `priority`, `enabled`, `conditions`, `actions`, `automation_mode`, `metadata` |
| [BankRuleHistory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Models/BankRuleHistory.php) | `team_id`, `rule_id`, `transaction_reference`, `outcome`, `matched`, `actions_applied`, `actor_reference`, `created_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [BankRuleController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules-api/src/Http/Controllers/BankRuleController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, SaveBankRule $action): BankRuleResource`<br>`public function show(string $rule): BankRuleResource`<br>`public function update(Request $request, string $rule, SaveBankRule $action): BankRuleResource`<br>`public function destroy(string $rule): mixed`<br>`public function test(Request $request, string $rule, TestBankRule $action): mixed`<br>`public function history(string $rule): mixed` |

**Observed route declarations:**

[modules/accounting-bank-rules-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/bank-rules')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [BankRuleController::class, 'index'])->middleware('ability:accounting.bank-rules.read');
Route::post('/', [BankRuleController::class, 'store'])->middleware('ability:accounting.bank-rules.write');
Route::get('/{rule}', [BankRuleController::class, 'show'])->middleware('ability:accounting.bank-rules.read');
Route::patch('/{rule}', [BankRuleController::class, 'update'])->middleware('ability:accounting.bank-rules.write');
Route::delete('/{rule}', [BankRuleController::class, 'destroy'])->middleware('ability:accounting.bank-rules.write');
Route::post('/{rule}/test', [BankRuleController::class, 'test'])->middleware('ability:accounting.bank-rules.read');
Route::get('/{rule}/history', [BankRuleController::class, 'history'])->middleware('ability:accounting.bank-rules.read');
```
<!-- layer-implementation-plan:end -->
