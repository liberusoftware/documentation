# Accounting: Accounting Bank Rules Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-bank-rules). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-accounting-bank-rules-vue-inertia`
**Matching domain module:** `accounting-bank-rules`
**Application:** Accounting
**Source feature:** [Accounting Bank Rules](../features/accounting-bank-rules.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-bank-rules.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Payee/text/amount/account conditions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Split/category/tax/dimension actions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Priority:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Suggestions/automation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Testing:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **History:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-bank-rules-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `payee-text-amount-account-conditions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `split-category-tax-dimension-actions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `priority`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `suggestions-automation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `testing`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `history`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-bank-rules` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-bank-rules-vue-inertia`](https://github.com/liberusoftware/module-accounting-bank-rules-vue-inertia) (`@liberusoftware/module-accounting-bank-rules-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/accounting-bank-rules.md) · [Core plan](../core/accounting-bank-rules.md) · [API plan](../api/accounting-bank-rules.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Payee/text/amount/account conditions** | Render `payee/text/amount/account conditions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Split/category/tax/dimension actions** | Render `split/category/tax/dimension actions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Priority** | Render `priority` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Suggestions/automation** | Render `suggestions/automation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Testing** | Render `testing` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **History** | Render `history` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
