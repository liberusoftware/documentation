# CRM: Crm Resource Planning React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-resource-planning). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-crm-resource-planning-react-inertia`
**Matching domain module:** `crm-resource-planning`
**Application:** CRM
**Source feature:** [Crm Resource Planning](../features/crm-resource-planning.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-resource-planning.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Skills:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Capacity:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Allocation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Utilization:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tentative/confirmed bookings:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Conflicts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Staffing forecasts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-crm-resource-planning-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `skills`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `capacity`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `allocation`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `utilization`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `tentative-confirmed-bookings`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `conflicts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `rates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `staffing-forecasts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-resource-planning` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-crm-resource-planning-react-inertia`](https://github.com/liberusoftware/module-crm-resource-planning-react-inertia) (`@liberusoftware/module-crm-resource-planning-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/crm-resource-planning.md) · [Core plan](../core/crm-resource-planning.md) · [API plan](../api/crm-resource-planning.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Skills** | Render `skills` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Capacity** | Render `capacity` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Allocation** | Render `allocation` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Utilization** | Render `utilization` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Tentative/confirmed bookings** | Render `tentative/confirmed bookings` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Conflicts** | Render `conflicts` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Rates** | Render `rates` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Staffing forecasts** | Render `staffing forecasts` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ResourcePlanningQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Queries/ResourcePlanningQuery.php) | `public function skills(int $teamId)`<br>`public function capacity(int $teamId)`<br>`public function bookings(int $teamId)`<br>`public function forecasts(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateBooking.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/CreateBooking.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceBooking` |
| [RecordForecast.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/RecordForecast.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceForecast` |
| [SetCapacity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/SetCapacity.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceCapacity` |
| [SetRate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/SetRate.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceRate` |
| [UpsertSkill.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Actions/UpsertSkill.php) | `public function __construct(private readonly ResourcePlanningPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ResourceSkill` |
| [ResourcePlanningPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Services/ResourcePlanningPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ResourceBooking.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceBooking.php) | No literal fillable array detected; inspect the model and API schema. |
| [ResourceCapacity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceCapacity.php) | No literal fillable array detected; inspect the model and API schema. |
| [ResourceForecast.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceForecast.php) | No literal fillable array detected; inspect the model and API schema. |
| [ResourceRate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceRate.php) | No literal fillable array detected; inspect the model and API schema. |
| [ResourceSkill.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning/src/Models/ResourceSkill.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ResourcePlanningController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning-api/src/Http/Controllers/ResourcePlanningController.php) | `public function skills(Request $r, ResourcePlanningQuery $q)`<br>`public function skill(Request $r, UpsertSkill $a)`<br>`public function capacity(Request $r, ResourcePlanningQuery $q)`<br>`public function setCapacity(Request $r, SetCapacity $a)`<br>`public function bookings(Request $r, ResourcePlanningQuery $q)`<br>`public function booking(Request $r, CreateBooking $a)`<br>`public function rate(Request $r, SetRate $a)`<br>`public function forecast(Request $r, RecordForecast $a)` |

**Observed route declarations:**

[modules/crm-resource-planning-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-resource-planning-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/resource-planning')->group(function (): void {
Route::get('/skills', [ResourcePlanningController::class, 'skills']);
Route::post('/skills', [ResourcePlanningController::class, 'skill']);
Route::get('/capacity', [ResourcePlanningController::class, 'capacity']);
Route::post('/capacity', [ResourcePlanningController::class, 'setCapacity']);
Route::get('/bookings', [ResourcePlanningController::class, 'bookings']);
Route::post('/bookings', [ResourcePlanningController::class, 'booking']);
Route::post('/rates', [ResourcePlanningController::class, 'rate']);
Route::post('/forecasts', [ResourcePlanningController::class, 'forecast']);
```
<!-- layer-implementation-plan:end -->
