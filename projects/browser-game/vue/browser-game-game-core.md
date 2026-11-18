# Browser Game: Browser Game Game Core Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-game-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-browser-game-browser-game-game-core-vue-inertia`
**Matching domain module:** `browser-game-game-core`
**Application:** Browser Game
**Source feature:** [Browser Game Game Core](../features/browser-game-game-core.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/browser-game-game-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Worlds/shards:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Game clock:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rulesets:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Content versions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Feature flags:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Maintenance state:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-browser-game-browser-game-game-core-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `worlds-shards`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `game-clock`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `rulesets`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `content-versions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `feature-flags`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `maintenance-state`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-game-core` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-browser-game-laravel-inertia-vue`](https://github.com/liberusoftware/project-browser-game-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-browser-game-game-core-vue-inertia`](https://github.com/liberusoftware/module-browser-game-game-core-vue-inertia) (`@liberusoftware/module-browser-game-game-core-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/browser-game-game-core.md) · [Core plan](../core/browser-game-game-core.md) · [API plan](../api/browser-game-game-core.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Worlds/shards** | Render `worlds/shards` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Game clock** | Render `game clock` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Rulesets** | Render `rulesets` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Content versions** | Render `content versions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Feature flags** | Render `feature flags` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Maintenance state** | Render `maintenance state` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [GameCoreOverview.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Queries/GameCoreOverview.php) | `public function forWorld(GameCoreContext $context, string $worldId): array`<br>`public function enabledFlags(?string $worldId = null): Collection`<br>`public function isEnabled(GameCoreContext $context, ?GameWorld $world, string $key, array $attributes = []): bool`<br>`public function enabledFor(GameCoreContext $context, ?GameWorld $world, array $attributes = []): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GameCoreContext.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Contracts/GameCoreContext.php) | `public function actorId(): ?string`<br>`public function tenantId(): ?string`<br>`public function teamId(): ?string` |
| [GameCorePolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Policies/GameCorePolicy.php) | `public function view(GameCoreContext $context, GameWorld $world): bool`<br>`public function manage(GameCoreContext $context, GameWorld $world): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [GameClock.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameClock.php) | `world_id`, `current_at`, `speed`, `paused`, `updated_by` |
| [GameContentVersion.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameContentVersion.php) | `world_id`, `version`, `status`, `content_hash`, `manifest`, `published_at`, `published_by` |
| [GameFeatureFlag.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameFeatureFlag.php) | `world_id`, `key`, `enabled`, `rollout_percentage`, `constraints`, `changed_by` |
| [GameMaintenanceState.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameMaintenanceState.php) | `world_id`, `status`, `message`, `starts_at`, `ends_at`, `changed_by` |
| [GameRuleset.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameRuleset.php) | `world_id`, `version`, `status`, `rules`, `published_at`, `published_by` |
| [GameWorld.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameWorld.php) | `tenant_id`, `team_id`, `name`, `slug`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [GameCoreController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-api/src/Http/Controllers/GameCoreController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, string $world): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function update(Request $request, GameWorld $world): JsonResponse`<br>`public function clock(Request $request, GameWorld $world): JsonResponse`<br>`public function ruleset(Request $request, GameWorld $world): JsonResponse`<br>`public function content(Request $request, GameWorld $world): JsonResponse`<br>`public function flag(Request $request, GameWorld $world, string $key): JsonResponse`<br>`public function evaluateFlag(Request $request, GameWorld $world, string $key): JsonResponse`<br>`public function maintenance(Request $request, GameWorld $world): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-game-core-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/game-core')
Route::get('/', [GameCoreController::class, 'index'])->name('browser-game.game-core.index');
Route::post('/', [GameCoreController::class, 'store'])->name('browser-game.game-core.store');
Route::get('/{world}', [GameCoreController::class, 'show'])->name('browser-game.game-core.show');
Route::patch('/{world}', [GameCoreController::class, 'update'])->name('browser-game.game-core.update');
Route::put('/{world}/clock', [GameCoreController::class, 'clock'])->name('browser-game.game-core.clock');
Route::post('/{world}/rulesets', [GameCoreController::class, 'ruleset'])->name('browser-game.game-core.ruleset');
Route::post('/{world}/content-versions', [GameCoreController::class, 'content'])->name('browser-game.game-core.content');
Route::put('/{world}/feature-flags/{key}', [GameCoreController::class, 'flag'])->name('browser-game.game-core.flag');
Route::get('/{world}/feature-flags/{key}', [GameCoreController::class, 'evaluateFlag'])->name('browser-game.game-core.flag.evaluate');
Route::put('/{world}/maintenance', [GameCoreController::class, 'maintenance'])->name('browser-game.game-core.maintenance');
```
<!-- layer-implementation-plan:end -->
