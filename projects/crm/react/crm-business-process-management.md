# CRM: Crm Business Process Management React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-business-process-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-crm-business-process-management-react-inertia`
**Matching domain module:** `crm-business-process-management`
**Application:** CRM
**Source feature:** [Crm Business Process Management](../features/crm-business-process-management.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-business-process-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Guided stages:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Required steps/data:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Approvals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Validations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Service processes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Exception routing:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Process versioning:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-crm-business-process-management-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `guided-stages`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `required-steps-data`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `approvals`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `validations`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `service-processes`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `exception-routing`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `process-versioning`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-business-process-management` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-crm-business-process-management-react-inertia`](https://github.com/liberusoftware/module-crm-business-process-management-react-inertia) (`@liberusoftware/module-crm-business-process-management-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/crm-business-process-management.md) · [Core plan](../core/crm-business-process-management.md) · [API plan](../api/crm-business-process-management.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Guided stages** | Render `guided stages` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Required steps/data** | Render `required steps/data` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Approvals** | Render `approvals` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Validations** | Render `validations` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Service processes** | Render `service processes` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Exception routing** | Render `exception routing` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Process versioning** | Render `process versioning` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProcessQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Queries/ProcessQuery.php) | `public function processes(int $teamId): Builder`<br>`public function runs(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AdvanceProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/AdvanceProcess.php) | `public function execute(int $teamId, int $actorId, ProcessRun $run, array $context = []): ProcessRun` |
| [CreateProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/CreateProcess.php) | `public function execute(int $teamId, int $ownerId, array $input): Process` |
| [PublishProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/PublishProcess.php) | `public function execute(int $teamId, int $actorId, Process $process): Process` |
| [StartProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/StartProcess.php) | `public function execute(int $teamId, int $actorId, Process $process, array $context = []): ProcessRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Process.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/Process.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProcessEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/ProcessEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProcessRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/ProcessRun.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [BusinessProcessesController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management-api/src/Http/Controllers/BusinessProcessesController.php) | `public function __construct(private readonly ProcessQuery $query)`<br>`public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateProcess $action): JsonResponse`<br>`public function publish(Request $request, Process $process, PublishProcess $action): JsonResponse`<br>`public function start(Request $request, Process $process, StartProcess $action): JsonResponse`<br>`public function advance(Request $request, ProcessRun $run, AdvanceProcess $action): JsonResponse`<br>`public function runs(Request $request): JsonResponse` |

**Observed route declarations:**

[modules/crm-business-process-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/business-process-management')->group(function (): void {
Route::get('/', [BusinessProcessesController::class, 'index']);
Route::post('/', [BusinessProcessesController::class, 'store']);
Route::post('{process}/publish', [BusinessProcessesController::class, 'publish']);
Route::post('{process}/runs', [BusinessProcessesController::class, 'start']);
Route::post('runs/{run}/advance', [BusinessProcessesController::class, 'advance']);
Route::get('runs', [BusinessProcessesController::class, 'runs']);
```
<!-- layer-implementation-plan:end -->
