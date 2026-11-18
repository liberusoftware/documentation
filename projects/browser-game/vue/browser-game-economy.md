# Browser Game: Browser Game Economy Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-economy). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-browser-game-browser-game-economy-vue-inertia`
**Matching domain module:** `browser-game-economy`
**Application:** Browser Game
**Source feature:** [Browser Game Economy](../features/browser-game-economy.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/browser-game-economy.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Currencies:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Faucets/sinks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Vendors:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Pricing:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Trading:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Auction house:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Fees:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Anti-abuse controls:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-browser-game-browser-game-economy-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `currencies`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `faucets-sinks`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `vendors`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `pricing`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `trading`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `auction-house`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `fees`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `anti-abuse-controls`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-economy` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-browser-game-laravel-inertia-vue`](https://github.com/liberusoftware/project-browser-game-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-browser-game-economy-vue-inertia`](https://github.com/liberusoftware/module-browser-game-economy-vue-inertia) (`@liberusoftware/module-browser-game-economy-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/browser-game-economy.md) · [Core plan](../core/browser-game-economy.md) · [API plan](../api/browser-game-economy.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Currencies** | Render `currencies` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Faucets/sinks** | Render `faucets/sinks` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Vendors** | Render `vendors` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Pricing** | Render `pricing` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Trading** | Render `trading` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Auction house** | Render `auction house` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Fees** | Render `fees` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Anti-abuse controls** | Render `anti-abuse controls` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EconomyQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Queries/EconomyQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EconomyLedgerEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyLedgerEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyListing.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyListing.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyVendor.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyVendor.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyVendorOffer.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyVendorOffer.php) | No literal fillable array detected; inspect the model and API schema. |
| [EconomyWallet.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyWallet.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [EconomyController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-api/src/Http/Controllers/EconomyController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, EconomyRecord $economy): JsonResponse`<br>`public function wallet(Request $request): JsonResponse`<br>`public function transfer(Request $request): JsonResponse`<br>`public function credit(Request $request): JsonResponse`<br>`public function debit(Request $request): JsonResponse`<br>`public function vendors(Request $request): JsonResponse`<br>`public function createVendor(Request $request): JsonResponse`<br>`public function addOffer(Request $request, EconomyVendor $vendor): JsonResponse`<br>`public function purchaseOffer(Request $request, EconomyVendorOffer $offer): JsonResponse`<br>`public function listings(Request $request): JsonResponse`<br>`public function createListing(Request $request): JsonResponse`<br>`public function purchaseListing(Request $request, EconomyListing $listing): JsonResponse`<br>`public function cancelListing(Request $request, EconomyListing $listing): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-economy-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/economy')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [EconomyController::class, 'index'])->name('browser-game.economy.index');
Route::get('/wallet', [EconomyController::class, 'wallet'])->name('browser-game.economy.wallet');
Route::post('/transfer', [EconomyController::class, 'transfer'])->name('browser-game.economy.transfer');
Route::post('/wallet/credit', [EconomyController::class, 'credit'])->name('browser-game.economy.wallet.credit');
Route::post('/wallet/debit', [EconomyController::class, 'debit'])->name('browser-game.economy.wallet.debit');
Route::get('/vendors', [EconomyController::class, 'vendors'])->name('browser-game.economy.vendors');
Route::post('/vendors', [EconomyController::class, 'createVendor'])->name('browser-game.economy.vendors.create');
Route::post('/vendors/{vendor}/offers', [EconomyController::class, 'addOffer'])->name('browser-game.economy.vendors.offers.create');
Route::post('/offers/{offer}/purchase', [EconomyController::class, 'purchaseOffer'])->name('browser-game.economy.offers.purchase');
Route::get('/listings', [EconomyController::class, 'listings'])->name('browser-game.economy.listings');
Route::post('/listings', [EconomyController::class, 'createListing'])->name('browser-game.economy.listings.create');
Route::post('/listings/{listing}/purchase', [EconomyController::class, 'purchaseListing'])->name('browser-game.economy.listings.purchase');
Route::post('/listings/{listing}/cancel', [EconomyController::class, 'cancelListing'])->name('browser-game.economy.listings.cancel');
Route::get('/{economy}', [EconomyController::class, 'show'])->name('browser-game.economy.show');
```
<!-- layer-implementation-plan:end -->
