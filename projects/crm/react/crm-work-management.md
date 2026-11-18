# CRM: Crm Work Management React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-work-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-crm-work-management-react-inertia`
**Matching domain module:** `crm-work-management`
**Application:** CRM
**Source feature:** [Crm Work Management](../features/crm-work-management.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-work-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Cross-record task boards:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Queues:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Recurring work:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Checklists:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Approvals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Workload:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Dependencies:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Personal/team views:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-crm-work-management-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `cross-record-task-boards`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `queues`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `recurring-work`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `checklists`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `approvals`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `workload`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `dependencies`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `personal-team-views`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-work-management` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-crm-work-management-react-inertia`](https://github.com/liberusoftware/module-crm-work-management-react-inertia) (`@liberusoftware/module-crm-work-management-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/crm-work-management.md) · [Core plan](../core/crm-work-management.md) · [API plan](../api/crm-work-management.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Cross-record task boards** | Render `cross-record task boards` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Queues** | Render `queues` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Recurring work** | Render `recurring work` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Checklists** | Render `checklists` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Approvals** | Render `approvals` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Workload** | Render `workload` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Dependencies** | Render `dependencies` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Personal/team views** | Render `personal/team views` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddChecklistItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/AddChecklistItem.php) | `public function execute(WorkItem $item, ?int $actorId, string $title): ChecklistItem` |
| [AddDependency.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/AddDependency.php) | `public function execute(WorkItem $item, WorkItem $dependsOn, ?int $actorId): Dependency` |
| [CompleteWorkItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/CompleteWorkItem.php) | `public function execute(WorkItem $item, ?int $actorId, ?int $expectedVersion = null): WorkItem` |
| [CreateWorkItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/CreateWorkItem.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): WorkItem` |
| [CreateWorkQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/CreateWorkQueue.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): WorkQueue` |
| [ReviewApproval.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/ReviewApproval.php) | `public function request(WorkItem $item, ?int $actorId, ?string $comment = null): Approval`<br>`public function review(Approval $approval, int $actorId, string $status, ?string $comment = null): Approval` |
| [UpdateWorkItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/UpdateWorkItem.php) | `public function execute(WorkItem $item, ?int $actorId, array $attributes, ?int $expectedVersion = null): WorkItem` |
| [UpdateWorkQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Actions/UpdateWorkQueue.php) | `public function execute(WorkQueue $queue, ?int $actorId, array $attributes): WorkQueue` |
| [WorkAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Services/WorkAudit.php) | `public function record(Model $item, ?int $actorId, string $event, array $details = []): void` |
| [WorkloadQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Services/WorkloadQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Approval.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/Approval.php) | `work_item_id`, `team_id`, `requested_by`, `reviewed_by`, `status`, `comment`, `reviewed_at` |
| [ChecklistItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/ChecklistItem.php) | `work_item_id`, `team_id`, `actor_id`, `title`, `completed`, `position` |
| [Dependency.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/Dependency.php) | `work_item_id`, `depends_on_id`, `team_id` |
| [WorkItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/WorkItem.php) | `team_id`, `actor_id`, `assigned_to`, `queue_id`, `title`, `description`, `status`, `priority`, `subject_type`, `subject_id`, `due_at`, `recurrence`, `next_run_at`, `version`, `metadata` |
| [WorkQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management/src/Models/WorkQueue.php) | `team_id`, `actor_id`, `name`, `description`, `status`, `rules` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WorkManagementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-api/src/Http/Controllers/WorkManagementController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateWorkItem $create, IdempotencyStore $idempotency): JsonResponse`<br>`public function show(Request $request, int $workItem): JsonResponse`<br>`public function update(Request $request, int $workItem, UpdateWorkItem $update): JsonResponse`<br>`public function complete(Request $request, int $workItem, CompleteWorkItem $complete, IdempotencyStore $idempotency): JsonResponse`<br>`public function checklist(Request $request, int $workItem, AddChecklistItem $add): JsonResponse`<br>`public function requestApproval(Request $request, int $workItem, ReviewApproval $approval, IdempotencyStore $idempotency): JsonResponse`<br>`public function dependency(Request $request, int $workItem, AddDependency $add): JsonResponse`<br>`public function queues(Request $request): JsonResponse`<br>`public function storeQueue(Request $request, CreateWorkQueue $create, IdempotencyStore $idempotency): JsonResponse`<br>`public function workload(Request $request, WorkloadQuery $workload): JsonResponse` |

**Observed route declarations:**

[modules/crm-work-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-work-management-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/work-management')->group(function (): void {
Route::get('/', [WorkManagementController::class, 'index']);
Route::post('/', [WorkManagementController::class, 'store']);
Route::get('/workload', [WorkManagementController::class, 'workload']);
Route::get('/queues', [WorkManagementController::class, 'queues']);
Route::post('/queues', [WorkManagementController::class, 'storeQueue']);
Route::get('/{workItem}', [WorkManagementController::class, 'show']);
Route::patch('/{workItem}', [WorkManagementController::class, 'update']);
Route::post('/{workItem}/complete', [WorkManagementController::class, 'complete']);
Route::post('/{workItem}/checklist', [WorkManagementController::class, 'checklist']);
Route::post('/{workItem}/approvals', [WorkManagementController::class, 'requestApproval']);
Route::post('/{workItem}/dependencies', [WorkManagementController::class, 'dependency']);
```
<!-- layer-implementation-plan:end -->
