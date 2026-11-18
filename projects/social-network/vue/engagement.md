# Social Network: Engagement Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#engagement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-social-network-engagement-vue-inertia`
**Matching domain module:** `social-network-engagement`
**Application:** Social Network
**Source feature:** [Engagement](../features/engagement.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/engagement.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Reactions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Comments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Replies:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Sharing:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Bookmarks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Counters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Abuse limits:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-social-network-engagement-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `reactions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `comments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `replies`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `sharing`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `bookmarks`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `counters`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `abuse-limits`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `social-network-engagement` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-social-network-laravel-inertia-vue`](https://github.com/liberusoftware/project-social-network-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-social-network-engagement-vue-inertia`](https://github.com/liberusoftware/module-social-network-engagement-vue-inertia) (`@liberusoftware/module-social-network-engagement-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/engagement.md) · [Core plan](../core/engagement.md) · [API plan](../api/engagement.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Reactions** | Render `reactions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Comments** | Render `comments` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Replies** | Render `replies` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Sharing** | Render `sharing` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Bookmarks** | Render `bookmarks` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Counters** | Render `counters` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Abuse limits** | Render `abuse limits` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateEngagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/CreateEngagement.php) | `public function __construct(private EngagementAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $actor, array $attributes): Engagement` |
| [DeleteEngagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/DeleteEngagement.php) | `public function __construct(private EngagementAuthorizer $authorizer)`<br>`public function handle(Profile $actor, Engagement $engagement): void` |
| [ListEngagements.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/ListEngagements.php) | `public function handle(string $targetType, string $targetId, ?string $kind = null, int $limit = 50): Collection`<br>`public function count(string $targetType, string $targetId, ?string $kind = null): int` |
| [UpdateEngagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/UpdateEngagement.php) | `public function handle(Profile $actor, Engagement $engagement, string $body): Engagement` |
| [EngagementAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Contracts/EngagementAuthorizer.php) | `public function create(Profile $actor): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Engagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Models/Engagement.php) | `id`, `actor_profile_id`, `target_type`, `target_id`, `kind`, `reaction_type`, `body` |

| Observed API controller | Handler signatures |
| --- | --- |
| [EngagementController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement-api/src/Http/Controllers/EngagementController.php) | `public function store(Request $request, GetProfile $get, CreateEngagement $create): JsonResponse`<br>`public function destroy(string $engagement, Request $request, GetProfile $get, DeleteEngagement $delete): JsonResponse`<br>`public function index(string $targetType, string $targetId, Request $request, ListEngagements $list): JsonResponse`<br>`public function update(string $engagement, Request $request, GetProfile $get, UpdateEngagement $update): JsonResponse` |

**Observed route declarations:**

[modules/social-network-engagement-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/engagement')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.engagement.api.')->group(function (): void {
Route::post('/', [EngagementController::class, 'store'])->name('store');
Route::get('/target/{targetType}/{targetId}', [EngagementController::class, 'index'])->name('index');
Route::patch('/{engagement}', [EngagementController::class, 'update'])->name('update');
Route::delete('/{engagement}', [EngagementController::class, 'destroy'])->name('destroy');
```
<!-- layer-implementation-plan:end -->
