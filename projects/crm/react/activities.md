# CRM: Activities React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#activities). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-activities-react-inertia`
**Matching domain module:** `crm-activities`
**Application:** CRM
**Source feature:** [Activities](../features/activities.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/activities.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Tasks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Calls:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Meetings:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Emails:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Deadlines:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Recurrence:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Queues:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Bulk completion:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reminders:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Outcomes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Goals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Activity reporting:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-activities-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `tasks`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `calls`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `meetings`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `emails`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `deadlines`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `recurrence`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `queues`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `bulk-completion`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `reminders`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `outcomes`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `goals`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `activity-reporting`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-activities` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-crm-activities-react-inertia`](https://github.com/liberusoftware/module-crm-activities-react-inertia) (`@liberusoftware/module-crm-activities-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/activities.md) · [Core plan](../core/activities.md) · [API plan](../api/activities.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Tasks** | Render `tasks` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Calls** | Render `calls` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Meetings** | Render `meetings` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Emails** | Render `emails` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Deadlines** | Render `deadlines` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Recurrence** | Render `recurrence` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Queues** | Render `queues` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Bulk completion** | Render `bulk completion` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Reminders** | Render `reminders` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Outcomes** | Render `outcomes` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Goals** | Render `goals` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Activity reporting** | Render `activity reporting` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CancelActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CancelActivity.php) | `public function execute(Activity $activity): Activity` |
| [CompleteActivities.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CompleteActivities.php) | `public function execute(int $teamId, array $activityIds, ?string $outcome = null, ?string $notes = null): int` |
| [CreateActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CreateActivity.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): Activity` |
| [CreateActivityGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CreateActivityGoal.php) | `public function execute(int $teamId, array $attributes): ActivityGoal` |
| [ActivityReport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Services/ActivityReport.php) | `public function summarize(int $teamId, Carbon $from, Carbon $until): array` |
| [ActivityScheduler.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Services/ActivityScheduler.php) | `public function nextOccurrence(Activity $activity): ?Activity`<br>`public function dueReminders(int $teamId, ?Carbon $at = null): Collection` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Activity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Models/Activity.php) | `team_id`, `actor_id`, `assigned_to`, `kind`, `status`, `title`, `description`, `subject_type`, `subject_id`, `starts_at`, `due_at`, `ends_at`, `recurrence`, `recurrence_until`, `reminder_at`, `queue`, `outcome`, `outcome_notes`, `metadata`, `completed_at` |
| [ActivityEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Models/ActivityEvent.php) | `team_id`, `activity_id`, `actor_id`, `event`, `details` |
| [ActivityGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Models/ActivityGoal.php) | `team_id`, `owner_id`, `name`, `kind`, `target`, `progress`, `starts_at`, `ends_at`, `status`, `criteria` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ActivityController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-api/src/Http/Controllers/ActivityController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateActivity $create): JsonResponse`<br>`public function show(Request $request, int $activity): JsonResponse`<br>`public function update(Request $request, int $activity): JsonResponse`<br>`public function complete(Request $request, CompleteActivities $complete): JsonResponse`<br>`public function cancel(Request $request, int $activity, CancelActivity $cancel): JsonResponse`<br>`public function report(Request $request, ActivityReport $report): JsonResponse` |

**Observed route declarations:**

[modules/crm-activities-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/activities')->group(function (): void {
Route::get('/', [ActivityController::class, 'index']);
Route::post('/', [ActivityController::class, 'store']);
Route::get('/report', [ActivityController::class, 'report']);
Route::post('/complete', [ActivityController::class, 'complete']);
Route::get('/{activity}', [ActivityController::class, 'show']);
Route::patch('/{activity}', [ActivityController::class, 'update']);
Route::post('/{activity}/cancel', [ActivityController::class, 'cancel']);
```
<!-- layer-implementation-plan:end -->
