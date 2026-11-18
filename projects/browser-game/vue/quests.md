# Browser Game: Quests Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#quests). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-browser-game-quests-vue-inertia`
**Matching domain module:** `browser-game-quests`
**Application:** Browser Game
**Source feature:** [Quests](../features/quests.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/quests.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Storylines:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Objectives:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Prerequisites:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Branching:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Dialogue:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rewards:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Repeatability:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Progress:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-browser-game-quests-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `storylines`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `objectives`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `prerequisites`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `branching`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `dialogue`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `rewards`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `repeatability`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `progress`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-quests` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-browser-game-laravel-inertia-vue`](https://github.com/liberusoftware/project-browser-game-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-browser-game-quests-vue-inertia`](https://github.com/liberusoftware/module-browser-game-quests-vue-inertia) (`@liberusoftware/module-browser-game-quests-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/quests.md) · [Core plan](../core/quests.md) · [API plan](../api/quests.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Storylines** | Render `storylines` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Objectives** | Render `objectives` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Prerequisites** | Render `prerequisites` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Branching** | Render `branching` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Dialogue** | Render `dialogue` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Rewards** | Render `rewards` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Repeatability** | Render `repeatability` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Progress** | Render `progress` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [QuestQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests/src/Queries/QuestQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder`<br>`public function availableFor(string $actorId, ?string $tenantId, ?string $teamId): Builder`<br>`public function activeFor(string $actorId, ?string $tenantId, ?string $teamId): Builder`<br>`public function completedFor(string $actorId, ?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Quest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests/src/Models/Quest.php) | No literal fillable array detected; inspect the model and API schema. |
| [QuestProgress.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests/src/Models/QuestProgress.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [QuestsController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests-api/src/Http/Controllers/QuestsController.php) | `public function index(Request $request): JsonResponse`<br>`public function available(Request $request): JsonResponse`<br>`public function active(Request $request): JsonResponse`<br>`public function completed(Request $request): JsonResponse`<br>`public function show(Request $request, Quest $quest): JsonResponse`<br>`public function progress(Request $request, Quest $quest): JsonResponse`<br>`public function accept(Request $request, Quest $quest): JsonResponse`<br>`public function complete(Request $request, Quest $quest): JsonResponse`<br>`public function abandon(Request $request, Quest $quest): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-quests-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/quests')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [QuestsController::class, 'index'])->name('browser-game.quests.index');
Route::get('/available', [QuestsController::class, 'available'])->name('browser-game.quests.available');
Route::get('/active', [QuestsController::class, 'active'])->name('browser-game.quests.active');
Route::get('/completed', [QuestsController::class, 'completed'])->name('browser-game.quests.completed');
Route::post('/{quest}/accept', [QuestsController::class, 'accept'])->name('browser-game.quests.accept');
Route::post('/{quest}/complete', [QuestsController::class, 'complete'])->name('browser-game.quests.complete');
Route::post('/{quest}/abandon', [QuestsController::class, 'abandon'])->name('browser-game.quests.abandon');
Route::get('/{quest}', [QuestsController::class, 'show'])->name('browser-game.quests.show');
Route::post('/{quest}/progress', [QuestsController::class, 'progress'])->name('browser-game.quests.progress');
```
<!-- layer-implementation-plan:end -->
