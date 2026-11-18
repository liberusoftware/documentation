# Billing: Module Billing Subscriptions React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-subscriptions). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-billing-module-billing-subscriptions-react-inertia`
**Matching domain module:** `module-billing-subscriptions`
**Application:** Billing
**Source feature:** [Module Billing Subscriptions](../features/module-billing-subscriptions.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-billing-subscriptions.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Activation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Renewal:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Trial:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Upgrade/downgrade:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Pause:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Cancellation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Entitlement state:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-billing-module-billing-subscriptions-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `activation`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `renewal`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `trial`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `upgrade-downgrade`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `pause`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `cancellation`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `entitlement-state`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `module-billing-subscriptions` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-billing-laravel-inertia-react`](https://github.com/liberusoftware/project-billing-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-billing-subscriptions-react-inertia`](https://github.com/liberusoftware/module-billing-subscriptions-react-inertia) (`@liberusoftware/module-billing-subscriptions-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/module-billing-subscriptions.md) · [Core plan](../core/module-billing-subscriptions.md) · [API plan](../api/module-billing-subscriptions.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Activation** | Render `activation` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Renewal** | Render `renewal` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Trial** | Render `trial` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Upgrade/downgrade** | Render `upgrade/downgrade` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Pause** | Render `pause` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Cancellation** | Render `cancellation` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Entitlement state** | Render `entitlement state` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListSubscriptions.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Queries/ListSubscriptions.php) | `public function execute(?int $teamId, int $perPage = 25, ?int $customerId = null, ?SubscriptionStatus $status = null): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ActivateSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Subscription` |
| [CancelSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/CancelSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription): Subscription` |
| [ChangeSubscriptionPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ChangeSubscriptionPlan.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription, ?int $pricingPlanId): Subscription` |
| [ExpireSubscriptions.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ExpireSubscriptions.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(?int $teamId = null, ?CarbonInterface $asOf = null): int` |
| [PauseSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/PauseSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription): Subscription` |
| [RenewSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/RenewSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription, ?int $periodDays = null): Subscription` |
| [ResumeSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ResumeSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription): Subscription` |
| [UpdateEntitlementState.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/UpdateEntitlementState.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription, array $entitlements): Subscription` |
| [SubscriptionPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Policies/SubscriptionPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Subscription $subscription): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Subscription $subscription): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Subscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Models/Subscription.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [SubscriptionController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions-api/src/Http/Controllers/SubscriptionController.php) | `public function index(Request $request, ListSubscriptions $query): JsonResponse`<br>`public function show(Request $request, Subscription $subscription): JsonResponse`<br>`public function store(Request $request, ActivateSubscription $activate): JsonResponse`<br>`public function renew(Request $request, Subscription $subscription, RenewSubscription $renew): JsonResponse`<br>`public function pause(Request $request, Subscription $subscription, PauseSubscription $pause): JsonResponse`<br>`public function cancel(Request $request, Subscription $subscription, CancelSubscription $cancel): JsonResponse`<br>`public function resume(Request $request, Subscription $subscription, ResumeSubscription $resume): JsonResponse`<br>`public function changePlan(Request $request, Subscription $subscription, ChangeSubscriptionPlan $change): JsonResponse`<br>`public function entitlements(Request $request, Subscription $subscription, UpdateEntitlementState $update): JsonResponse`<br>`public function expire(Request $request, ExpireSubscriptions $expire): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-subscriptions-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.subscriptions.read'])
Route::get('/', [SubscriptionController::class, 'index'])->name('index');
Route::get('/{subscription}', [SubscriptionController::class, 'show'])->whereNumber('subscription')->name('show');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.subscriptions.write', 'idempotency'])
Route::post('/', [SubscriptionController::class, 'store'])->name('store');
Route::post('/{subscription}/renew', [SubscriptionController::class, 'renew'])->name('renew');
Route::post('/{subscription}/pause', [SubscriptionController::class, 'pause'])->name('pause');
Route::post('/{subscription}/resume', [SubscriptionController::class, 'resume'])->name('resume');
Route::post('/{subscription}/cancel', [SubscriptionController::class, 'cancel'])->name('cancel');
Route::patch('/{subscription}/plan', [SubscriptionController::class, 'changePlan'])->name('plan');
Route::patch('/{subscription}/entitlements', [SubscriptionController::class, 'entitlements'])->name('entitlements');
Route::post('/expire', [SubscriptionController::class, 'expire'])->name('expire');
```
<!-- layer-implementation-plan:end -->
