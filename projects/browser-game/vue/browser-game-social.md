# Browser Game: Browser Game Social Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-social). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-browser-game-browser-game-social-vue-inertia`
**Matching domain module:** `browser-game-social`
**Application:** Browser Game
**Source feature:** [Browser Game Social](../features/browser-game-social.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/browser-game-social.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Friends:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Parties:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Chat:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Mail:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Guilds:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Alliances:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Permissions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Activity:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reporting:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-browser-game-browser-game-social-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `friends`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `parties`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `chat`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `mail`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `guilds`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `alliances`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `permissions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `activity`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `reporting`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-social` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-browser-game-laravel-inertia-vue`](https://github.com/liberusoftware/project-browser-game-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-browser-game-social-vue-inertia`](https://github.com/liberusoftware/module-browser-game-social-vue-inertia) (`@liberusoftware/module-browser-game-social-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/browser-game-social.md) · [Core plan](../core/browser-game-social.md) · [API plan](../api/browser-game-social.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Friends** | Render `friends` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Parties** | Render `parties` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Chat** | Render `chat` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Mail** | Render `mail` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Guilds** | Render `guilds` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Alliances** | Render `alliances` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Permissions** | Render `permissions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Activity** | Render `activity` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Reporting** | Render `reporting` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SocialQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Queries/SocialQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SocialActivity.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialActivity.php) | No literal fillable array detected; inspect the model and API schema. |
| [SocialMembership.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialMembership.php) | No literal fillable array detected; inspect the model and API schema. |
| [SocialRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialRecord.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [SocialController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social-api/src/Http/Controllers/SocialController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function friendRequest(Request $request): JsonResponse`<br>`public function respondToFriendRequest(Request $request, SocialRecord $social): JsonResponse`<br>`public function createGroup(Request $request, string $kind): JsonResponse`<br>`public function mail(Request $request): JsonResponse`<br>`public function member(Request $request, SocialRecord $social): JsonResponse`<br>`public function message(Request $request, SocialRecord $social): JsonResponse`<br>`public function report(Request $request): JsonResponse`<br>`public function permissions(Request $request, SocialRecord $social): JsonResponse`<br>`public function activity(Request $request): JsonResponse`<br>`public function show(Request $request, SocialRecord $social): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-social-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/social')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [SocialController::class, 'index'])->name('browser-game.social.index');
Route::post('/', [SocialController::class, 'store'])->name('browser-game.social.store');
Route::post('/friends', [SocialController::class, 'friendRequest'])->name('browser-game.social.friends.create');
Route::post('/groups/{kind}', [SocialController::class, 'createGroup'])->whereIn('kind', ['party', 'chat', 'guild', 'alliance'])->name('browser-game.social.groups.create');
Route::post('/mail', [SocialController::class, 'mail'])->name('browser-game.social.mail.create');
Route::get('/activity', [SocialController::class, 'activity'])->name('browser-game.social.activity');
Route::post('/{social}/members', [SocialController::class, 'member'])->name('browser-game.social.member');
Route::patch('/{social}/permissions', [SocialController::class, 'permissions'])->name('browser-game.social.permissions');
Route::patch('/{social}/friend-response', [SocialController::class, 'respondToFriendRequest'])->name('browser-game.social.friends.respond');
Route::post('/{social}/messages', [SocialController::class, 'message'])->name('browser-game.social.message');
Route::post('/reports', [SocialController::class, 'report'])->name('browser-game.social.report');
Route::get('/{social}', [SocialController::class, 'show'])->name('browser-game.social.show');
```
<!-- layer-implementation-plan:end -->
