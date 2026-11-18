# Social Network: Social Network Notifications Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-notifications). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-social-network-social-network-notifications-vue-inertia`
**Matching domain module:** `social-network-notifications`
**Application:** Social Network
**Source feature:** [Social Network Notifications](../features/social-network-notifications.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/social-network-notifications.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Preferences:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **In-app/email/push delivery:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Grouping:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Digests:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Quiet hours:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Read state:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-social-network-social-network-notifications-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `preferences`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `in-app-email-push-delivery`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `grouping`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `digests`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `quiet-hours`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `read-state`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `social-network-notifications` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-social-network-laravel-inertia-vue`](https://github.com/liberusoftware/project-social-network-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-social-network-notifications-vue-inertia`](https://github.com/liberusoftware/module-social-network-notifications-vue-inertia) (`@liberusoftware/module-social-network-notifications-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/social-network-notifications.md) · [Core plan](../core/social-network-notifications.md) · [API plan](../api/social-network-notifications.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Preferences** | Render `preferences` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **In-app/email/push delivery** | Render `in-app/email/push delivery` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Grouping** | Render `grouping` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Digests** | Render `digests` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Quiet hours** | Render `quiet hours` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Read state** | Render `read state` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateNotification.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/CreateNotification.php) | `public function __construct(private Dispatcher $events)`<br>`public function handle(string $profileId, string $kind, array $payload = [], string $channel = 'in_app', ?string $groupKey = null): SocialNotification` |
| [DismissNotification.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/DismissNotification.php) | `public function __construct(private NotificationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile, string $id): SocialNotification` |
| [MarkAllRead.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/MarkAllRead.php) | `public function __construct(private NotificationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile): int` |
| [MarkRead.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/MarkRead.php) | `public function __construct(private NotificationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile, string $id): SocialNotification` |
| [UnreadCount.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/UnreadCount.php) | `public function __construct(private NotificationAuthorizer $authorizer)`<br>`public function handle(Profile $profile): int` |
| [UpdatePreferences.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/UpdatePreferences.php) | `public function __construct(private NotificationAuthorizer $authorizer)`<br>`public function handle(Profile $profile, array $data): NotificationPreference` |
| [NotificationAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Contracts/NotificationAuthorizer.php) | `public function manage(Profile $profile): void`<br>`public function view(Profile $profile): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [NotificationPreference.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Models/NotificationPreference.php) | `profile_id`, `channels`, `quiet_hours`, `digest` |
| [SocialNotification.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Models/SocialNotification.php) | `id`, `profile_id`, `kind`, `group_key`, `state`, `channel`, `payload`, `read_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [NotificationsController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications-api/src/Http/Controllers/NotificationsController.php) | `public function index(Request $request, GetProfile $get): JsonResponse`<br>`public function preferences(Request $request, GetProfile $get, UpdatePreferences $update): JsonResponse`<br>`public function unreadCount(Request $request, GetProfile $get, UnreadCount $count): JsonResponse`<br>`public function readAll(Request $request, GetProfile $get, MarkAllRead $read): JsonResponse`<br>`public function read(string $notification, Request $request, GetProfile $get, MarkRead $read): JsonResponse`<br>`public function dismiss(string $notification, Request $request, GetProfile $get, DismissNotification $dismiss): JsonResponse` |

**Observed route declarations:**

[modules/social-network-notifications-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/notifications')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.notifications.api.')->group(function (): void {
Route::get('/', [NotificationsController::class, 'index'])->name('index');
Route::get('/unread-count', [NotificationsController::class, 'unreadCount'])->name('unread-count');
Route::post('/read-all', [NotificationsController::class, 'readAll'])->name('read-all');
Route::patch('/preferences', [NotificationsController::class, 'preferences'])->name('preferences');
Route::post('/{notification}/read', [NotificationsController::class, 'read'])->name('read');
Route::post('/{notification}/dismiss', [NotificationsController::class, 'dismiss'])->name('dismiss');
```
<!-- layer-implementation-plan:end -->
