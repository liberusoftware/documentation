# CRM: Crm Activities Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-activities). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-crm-activities-vue-inertia`
**Matching domain module:** `crm-activities`
**Application:** CRM
**Source feature:** [Crm Activities](../features/crm-activities.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-activities.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

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

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-crm-activities-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `tasks`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `calls`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `meetings`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `emails`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `deadlines`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `recurrence`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `queues`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `bulk-completion`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `reminders`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `outcomes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `goals`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `activity-reporting`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-activities` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-activities-vue-inertia`](https://github.com/liberusoftware/module-crm-activities-vue-inertia) (`@liberusoftware/module-crm-activities-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/crm-activities.md) · [Core plan](../core/crm-activities.md) · [API plan](../api/crm-activities.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Tasks** | Render `tasks` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Calls** | Render `calls` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Meetings** | Render `meetings` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Emails** | Render `emails` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Deadlines** | Render `deadlines` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Recurrence** | Render `recurrence` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Queues** | Render `queues` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Bulk completion** | Render `bulk completion` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Reminders** | Render `reminders` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Outcomes** | Render `outcomes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Goals** | Render `goals` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Activity reporting** | Render `activity reporting` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
