# Browser Game: Browser Game Moderation And Analytics React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-moderation-and-analytics). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-browser-game-browser-game-moderation-and-analytics-react-inertia`
**Matching domain module:** `browser-game-moderation-and-analytics`
**Application:** Browser Game
**Source feature:** [Browser Game Moderation And Analytics](../features/browser-game-moderation-and-analytics.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/browser-game-moderation-and-analytics.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Reports:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Sanctions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Appeals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Telemetry:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Funnels:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Balance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Economy:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Fraud:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Health:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-browser-game-browser-game-moderation-and-analytics-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `reports`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `sanctions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `appeals`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `telemetry`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `funnels`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `balance`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `economy`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `fraud`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `health`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `browser-game-moderation-and-analytics` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-browser-game-laravel-inertia-react`](https://github.com/liberusoftware/project-browser-game-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-browser-game-moderation-and-analytics-react-inertia`](https://github.com/liberusoftware/module-browser-game-moderation-and-analytics-react-inertia) (`@liberusoftware/module-browser-game-moderation-and-analytics-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/browser-game-moderation-and-analytics.md) · [Core plan](../core/browser-game-moderation-and-analytics.md) · [API plan](../api/browser-game-moderation-and-analytics.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Reports** | Render `reports` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Sanctions** | Render `sanctions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Appeals** | Render `appeals` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Telemetry** | Render `telemetry` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Funnels** | Render `funnels` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Balance** | Render `balance` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Economy** | Render `economy` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Fraud** | Render `fraud` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Health** | Render `health` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ModerationAndAnalyticsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Queries/ModerationAndAnalyticsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ModerationAndAnalyticsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Models/ModerationAndAnalyticsRecord.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ModerationAndAnalyticsController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics-api/src/Http/Controllers/ModerationAndAnalyticsController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function report(Request $request): JsonResponse`<br>`public function sanction(Request $request): JsonResponse`<br>`public function appeal(Request $request): JsonResponse`<br>`public function telemetry(Request $request): JsonResponse`<br>`public function funnel(Request $request): JsonResponse`<br>`public function balance(Request $request): JsonResponse`<br>`public function economy(Request $request): JsonResponse`<br>`public function fraud(Request $request): JsonResponse`<br>`public function health(Request $request): JsonResponse`<br>`public function resolve(Request $request, ModerationAndAnalyticsRecord $moderationAndAnalytics): JsonResponse`<br>`public function show(Request $request, ModerationAndAnalyticsRecord $moderationAndAnalytics): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-moderation-and-analytics-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/moderation-and-analytics')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [ModerationAndAnalyticsController::class, 'index'])->name('browser-game.moderation-and-analytics.index');
Route::post('/', [ModerationAndAnalyticsController::class, 'store'])->name('browser-game.moderation-and-analytics.store');
Route::post('/reports', [ModerationAndAnalyticsController::class, 'report'])->name('browser-game.moderation-and-analytics.reports');
Route::post('/sanctions', [ModerationAndAnalyticsController::class, 'sanction'])->name('browser-game.moderation-and-analytics.sanctions');
Route::post('/appeals', [ModerationAndAnalyticsController::class, 'appeal'])->name('browser-game.moderation-and-analytics.appeals');
Route::post('/telemetry', [ModerationAndAnalyticsController::class, 'telemetry'])->name('browser-game.moderation-and-analytics.telemetry');
Route::post('/funnels', [ModerationAndAnalyticsController::class, 'funnel'])->name('browser-game.moderation-and-analytics.funnels');
Route::post('/balance', [ModerationAndAnalyticsController::class, 'balance'])->name('browser-game.moderation-and-analytics.balance');
Route::post('/economy', [ModerationAndAnalyticsController::class, 'economy'])->name('browser-game.moderation-and-analytics.economy');
Route::post('/fraud', [ModerationAndAnalyticsController::class, 'fraud'])->name('browser-game.moderation-and-analytics.fraud');
Route::post('/health', [ModerationAndAnalyticsController::class, 'health'])->name('browser-game.moderation-and-analytics.health');
Route::post('/{moderationAndAnalytics}/resolve', [ModerationAndAnalyticsController::class, 'resolve'])->name('browser-game.moderation-and-analytics.resolve');
Route::get('/{moderationAndAnalytics}', [ModerationAndAnalyticsController::class, 'show'])->name('browser-game.moderation-and-analytics.show');
```
<!-- layer-implementation-plan:end -->
