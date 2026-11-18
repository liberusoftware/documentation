# CRM: Field Service Coordination React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#field-service-coordination). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-field-service-coordination-react-inertia`
**Matching domain module:** `crm-field-service-coordination`
**Application:** CRM
**Source feature:** [Field Service Coordination](../features/field-service-coordination.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/field-service-coordination.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Work types:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Service appointments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Dispatch references:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Technician/contractor visibility:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Asset/service history:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Maintenance module handoff:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-field-service-coordination-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `work-types`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `service-appointments`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `dispatch-references`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `technician-contractor-visibility`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `asset-service-history`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `maintenance-module-handoff`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-field-service-coordination` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-crm-field-service-coordination-react-inertia`](https://github.com/liberusoftware/module-crm-field-service-coordination-react-inertia) (`@liberusoftware/module-crm-field-service-coordination-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/field-service-coordination.md) · [Core plan](../core/field-service-coordination.md) · [API plan](../api/field-service-coordination.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Work types** | Render `work types` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Service appointments** | Render `service appointments` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Dispatch references** | Render `dispatch references` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Technician/contractor visibility** | Render `technician/contractor visibility` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Asset/service history** | Render `asset/service history` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Maintenance module handoff** | Render `maintenance module handoff` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [FieldServiceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Queries/FieldServiceQuery.php) | `public function workTypes(int $teamId)`<br>`public function appointments(int $teamId)`<br>`public function assets(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateWorkType.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/CreateWorkType.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): WorkType` |
| [HandOffMaintenance.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/HandOffMaintenance.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, ServiceAppointment $appointment, array $input): MaintenanceHandoff` |
| [RecordServiceHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/RecordServiceHistory.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, ServiceAppointment $appointment, array $input): ServiceHistory` |
| [ScheduleAppointment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Actions/ScheduleAppointment.php) | `public function __construct(private readonly FieldServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ServiceAppointment` |
| [FieldServicePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Services/FieldServicePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MaintenanceHandoff.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/MaintenanceHandoff.php) | No literal fillable array detected; inspect the model and API schema. |
| [ServiceAppointment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/ServiceAppointment.php) | No literal fillable array detected; inspect the model and API schema. |
| [ServiceAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/ServiceAsset.php) | No literal fillable array detected; inspect the model and API schema. |
| [ServiceHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/ServiceHistory.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkType.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination/src/Models/WorkType.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [FieldServiceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination-api/src/Http/Controllers/FieldServiceController.php) | `public function __construct(private readonly FieldServiceQuery $query)`<br>`public function workTypes(): JsonResponse`<br>`public function appointments(): JsonResponse`<br>`public function storeWorkType(CreateWorkType $action): JsonResponse`<br>`public function schedule(ScheduleAppointment $action): JsonResponse`<br>`public function history(ServiceAppointment $appointment, RecordServiceHistory $action): JsonResponse`<br>`public function handoff(ServiceAppointment $appointment, HandOffMaintenance $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-field-service-coordination-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-field-service-coordination-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/field-service-coordination')->group(function (): void {
Route::get('work-types', [FieldServiceController::class, 'workTypes']);
Route::get('appointments', [FieldServiceController::class, 'appointments']);
Route::post('work-types', [FieldServiceController::class, 'storeWorkType']);
Route::post('appointments', [FieldServiceController::class, 'schedule']);
Route::post('appointments/{appointment}/history', [FieldServiceController::class, 'history']);
Route::post('appointments/{appointment}/maintenance-handoff', [FieldServiceController::class, 'handoff']);
```
<!-- layer-implementation-plan:end -->
