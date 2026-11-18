# Maintenance: Inspections React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#inspections). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-maintenance-inspections-react-inertia`
**Matching domain module:** `maintenance-inspections`
**Application:** Maintenance
**Source feature:** [Inspections](../features/inspections.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/inspections.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Templates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Conditional checklists:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Readings:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Failures:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Signatures:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Certificates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Follow-up:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-maintenance-inspections-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `templates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `conditional-checklists`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `readings`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `failures`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `signatures`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `certificates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `follow-up`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `maintenance-inspections` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-maintenance-laravel-inertia-react`](https://github.com/liberusoftware/project-maintenance-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-maintenance-inspections-react-inertia`](https://github.com/liberusoftware/module-maintenance-inspections-react-inertia) (`@liberusoftware/module-maintenance-inspections-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/inspections.md) · [Core plan](../core/inspections.md) · [API plan](../api/inspections.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Templates** | Render `templates` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Conditional checklists** | Render `conditional checklists` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Readings** | Render `readings` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Failures** | Render `failures` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Signatures** | Render `signatures` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Certificates** | Render `certificates` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Follow-up** | Render `follow-up` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CompleteInspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Actions/CompleteInspection.php) | `public function handle(int $teamId, Inspection $inspection, string $outcome): Inspection` |
| [CreateInspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Actions/CreateInspection.php) | `public function handle(int $teamId, array $attributes): Inspection` |
| [DeleteInspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Actions/DeleteInspection.php) | `public function handle(int $teamId, Inspection $inspection): void` |
| [UpdateInspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Actions/UpdateInspection.php) | `public function handle(int $teamId, Inspection $inspection, array $attributes): Inspection` |
| [InspectionPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Policies/InspectionPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Inspection $inspection): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Inspection $inspection): bool`<br>`public function delete(object $user, Inspection $inspection): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Inspection.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections/src/Models/Inspection.php) | `team_id`, `title`, `template_key`, `status`, `outcome`, `inspected_at`, `inspector_id`, `readings`, `failures`, `signature`, `certificate`, `follow_up` |

| Observed API controller | Handler signatures |
| --- | --- |
| [InspectionController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections-api/src/Http/Controllers/InspectionController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateInspection $create): JsonResponse`<br>`public function show(Request $request, Inspection $inspection): JsonResponse`<br>`public function update(Request $request, Inspection $inspection, UpdateInspection $update): JsonResponse`<br>`public function complete(Request $request, Inspection $inspection, CompleteInspection $complete): JsonResponse`<br>`public function destroy(Request $request, Inspection $inspection, DeleteInspection $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-inspections-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inspections-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/inspections')->group(function (): void {
Route::get('/', [InspectionController::class, 'index']);
Route::post('/', [InspectionController::class, 'store']);
Route::get('/{inspection}', [InspectionController::class, 'show']);
Route::patch('/{inspection}', [InspectionController::class, 'update']);
Route::post('/{inspection}/complete', [InspectionController::class, 'complete']);
Route::delete('/{inspection}', [InspectionController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
