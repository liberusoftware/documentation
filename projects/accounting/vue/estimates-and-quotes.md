# Accounting: Estimates and Quotes Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#estimates-and-quotes). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-estimates-and-quotes-vue-inertia`
**Matching domain module:** `accounting-estimates-and-quotes`
**Application:** Accounting
**Source feature:** [Estimates and Quotes](../features/estimates-and-quotes.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/estimates-and-quotes.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Branded estimates/quotes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Items:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Terms:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Versions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Delivery:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Acceptance/decline:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Expiry:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Conversion:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **History:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-estimates-and-quotes-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `branded-estimates-quotes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `items`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `terms`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `versions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `delivery`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `acceptance-decline`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `expiry`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `conversion`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
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

- Package identity, public exports, API dependency, and module dependency match `accounting-estimates-and-quotes` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-estimates-and-quotes-vue-inertia`](https://github.com/liberusoftware/module-accounting-estimates-and-quotes-vue-inertia) (`@liberusoftware/module-accounting-estimates-and-quotes-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/estimates-and-quotes.md) · [Core plan](../core/estimates-and-quotes.md) · [API plan](../api/estimates-and-quotes.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Branded estimates/quotes** | Render `branded estimates/quotes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Items** | Render `items` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Terms** | Render `terms` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Versions** | Render `versions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Delivery** | Render `delivery` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Acceptance/decline** | Render `acceptance/decline` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Expiry** | Render `expiry` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Conversion** | Render `conversion` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **History** | Render `history` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EstimateQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Queries/EstimateQuery.php) | `public function paginate(?int $legalEntityId = null, ?EstimateStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function total(Estimate $e): float` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddEstimateItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/AddEstimateItem.php) | `public function handle(Estimate $e, array $a): EstimateItem` |
| [ConvertEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/ConvertEstimate.php) | `public function handle(Estimate $e, string $convertedRef, ?string $actor = null): Estimate` |
| [CreateEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/CreateEstimate.php) | `public function handle(array $a): Estimate` |
| [DecideEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/DecideEstimate.php) | `public function handle(Estimate $e, bool $accepted, ?string $reason = null, ?string $actor = null): Estimate` |
| [ExpireEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/ExpireEstimate.php) | `public function handle(Estimate $e, ?string $actor = null): Estimate` |
| [SendEstimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Actions/SendEstimate.php) | `public function handle(Estimate $e, ?string $actor = null): Estimate` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Estimate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/Estimate.php) | `legal_entity_id`, `customer_ref`, `quote_ref`, `name`, `currency`, `status`, `issue_date`, `expires_on`, `version`, `terms`, `brand`, `accepted_at`, `declined_reason`, `converted_ref`, `metadata` |
| [EstimateHistory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateHistory.php) | `estimate_id`, `event`, `actor_ref`, `metadata` |
| [EstimateItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateItem.php) | `estimate_id`, `item_ref`, `description`, `quantity`, `unit_price`, `tax_rate`, `amount`, `metadata` |
| [EstimateVersion.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes/src/Models/EstimateVersion.php) | `estimate_id`, `version`, `snapshot`, `created_by` |

| Observed API controller | Handler signatures |
| --- | --- |
| [EstimatesController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes-api/src/Http/Controllers/EstimatesController.php) | `public function __construct(private readonly EstimateQuery $query)`<br>`public function index(Request $r): mixed`<br>`public function store(Request $r, CreateEstimate $a): EstimateResource`<br>`public function show(Estimate $e): EstimateResource`<br>`public function item(Request $r, Estimate $e, AddEstimateItem $a): EstimateResource`<br>`public function send(Request $r, Estimate $e, SendEstimate $a): EstimateResource`<br>`public function decide(Request $r, Estimate $e, DecideEstimate $a): EstimateResource`<br>`public function expire(Request $r, Estimate $e, ExpireEstimate $a): EstimateResource`<br>`public function convert(Request $r, Estimate $e, ConvertEstimate $a): EstimateResource` |

**Observed route declarations:**

[modules/accounting-estimates-and-quotes-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-estimates-and-quotes-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/estimates-and-quotes')->group(function (): void {
Route::middleware('ability:accounting.estimates-and-quotes.read')->group(function (): void {
Route::get('/', [EstimatesController::class, 'index']);
Route::get('/{estimate}', [EstimatesController::class, 'show']);
Route::middleware('ability:accounting.estimates-and-quotes.write')->group(function (): void {
Route::post('/', [EstimatesController::class, 'store']);
Route::post('/{estimate}/items', [EstimatesController::class, 'item']);
Route::post('/{estimate}/send', [EstimatesController::class, 'send']);
Route::post('/{estimate}/decide', [EstimatesController::class, 'decide']);
Route::post('/{estimate}/expire', [EstimatesController::class, 'expire']);
Route::post('/{estimate}/convert', [EstimatesController::class, 'convert']);
```
<!-- layer-implementation-plan:end -->
