# Maintenance: Labor and Time React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#labor-and-time). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-maintenance-labor-and-time-react-inertia`
**Matching domain module:** `maintenance-labor-and-time`
**Application:** Maintenance
**Source feature:** [Labor and Time](../features/labor-and-time.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/labor-and-time.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Engineer skills:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Attendance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Time entries:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Expenses:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Approval:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-maintenance-labor-and-time-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `engineer-skills`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `attendance`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `time-entries`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `rates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `expenses`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `approval`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `maintenance-labor-and-time` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-maintenance-laravel-inertia-react`](https://github.com/liberusoftware/project-maintenance-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-maintenance-labor-and-time-react-inertia`](https://github.com/liberusoftware/module-maintenance-labor-and-time-react-inertia) (`@liberusoftware/module-maintenance-labor-and-time-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/labor-and-time.md) · [Core plan](../core/labor-and-time.md) · [API plan](../api/labor-and-time.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Engineer skills** | Render `engineer skills` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Attendance** | Render `attendance` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Time entries** | Render `time entries` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Rates** | Render `rates` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Expenses** | Render `expenses` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Approval** | Render `approval` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/ApproveTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry, int $approverId): TimeEntry` |
| [CreateTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/CreateTimeEntry.php) | `public function handle(int $teamId, array $attributes): TimeEntry` |
| [DeleteTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/DeleteTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry): void` |
| [RejectTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/RejectTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry, int $approverId, ?string $reason = null): TimeEntry` |
| [UpdateTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/UpdateTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry, array $attributes): TimeEntry` |
| [TimeEntryPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Policies/TimeEntryPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, TimeEntry $entry): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, TimeEntry $entry): bool`<br>`public function delete(object $user, TimeEntry $entry): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Models/TimeEntry.php) | `team_id`, `user_id`, `work_order_id`, `description`, `started_at`, `ended_at`, `minutes`, `rate`, `status`, `expense_amount`, `currency` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TimeEntryController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time-api/src/Http/Controllers/TimeEntryController.php) | `public function index(Request $r): JsonResponse`<br>`public function store(Request $r, CreateTimeEntry $create): JsonResponse`<br>`public function show(Request $r, TimeEntry $timeEntry): JsonResponse`<br>`public function approve(Request $r, TimeEntry $timeEntry, ApproveTimeEntry $approve): JsonResponse`<br>`public function reject(Request $r, TimeEntry $timeEntry, RejectTimeEntry $reject): JsonResponse`<br>`public function update(Request $r, TimeEntry $timeEntry, UpdateTimeEntry $update): JsonResponse`<br>`public function destroy(Request $r, TimeEntry $timeEntry, DeleteTimeEntry $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-labor-and-time-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/labor-and-time')->group(function (): void {
Route::get('/', [TimeEntryController::class, 'index']);
Route::post('/', [TimeEntryController::class, 'store']);
Route::get('/{timeEntry}', [TimeEntryController::class, 'show']);
Route::patch('/{timeEntry}', [TimeEntryController::class, 'update']);
Route::delete('/{timeEntry}', [TimeEntryController::class, 'destroy']);
Route::post('/{timeEntry}/approve', [TimeEntryController::class, 'approve']);
Route::post('/{timeEntry}/reject', [TimeEntryController::class, 'reject']);
```
<!-- layer-implementation-plan:end -->
