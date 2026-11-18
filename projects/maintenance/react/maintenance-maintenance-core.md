# Maintenance: Maintenance Maintenance Core React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#maintenance-maintenance-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-maintenance-maintenance-maintenance-core-react-inertia`
**Matching domain module:** `maintenance-maintenance-core`
**Application:** Maintenance
**Source feature:** [Maintenance Maintenance Core](../features/maintenance-maintenance-core.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/maintenance-maintenance-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Organizations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Service settings:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Statuses:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Numbering:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Priorities:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Shared events:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-maintenance-maintenance-maintenance-core-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `organizations`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `service-settings`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `statuses`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `numbering`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `priorities`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `shared-events`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `maintenance-maintenance-core` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-maintenance-laravel-inertia-react`](https://github.com/liberusoftware/project-maintenance-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-maintenance-maintenance-core-react-inertia`](https://github.com/liberusoftware/module-maintenance-maintenance-core-react-inertia) (`@liberusoftware/module-maintenance-maintenance-core-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/maintenance-maintenance-core.md) · [Core plan](../core/maintenance-maintenance-core.md) · [API plan](../api/maintenance-maintenance-core.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Organizations** | Render `organizations` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Service settings** | Render `service settings` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Statuses** | Render `statuses` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Numbering** | Render `numbering` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Priorities** | Render `priorities` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Shared events** | Render `shared events` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureNumbering.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/ConfigureNumbering.php) | `public function execute(int $teamId, string $documentType, string $prefix, int $padding = 6): NumberingSequence` |
| [CreateOrganization.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/CreateOrganization.php) | `public function execute(int $teamId, string $name, string $code, ?string $description = null): Organization` |
| [CreatePriority.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/CreatePriority.php) | `public function execute(int $teamId, array $attributes): Priority` |
| [CreateStatus.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/CreateStatus.php) | `public function execute(int $teamId, array $attributes): Status` |
| [DeleteOrganization.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/DeleteOrganization.php) | `public function execute(Organization $organization): void` |
| [DeletePriority.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/DeletePriority.php) | `public function execute(Priority $priority): void` |
| [DeleteServiceSetting.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/DeleteServiceSetting.php) | `public function execute(ServiceSetting $setting): void` |
| [DeleteStatus.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/DeleteStatus.php) | `public function execute(Status $status): void` |
| [IssueNumber.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/IssueNumber.php) | `public function execute(int $teamId, string $documentType): string` |
| [SetServiceSetting.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Actions/SetServiceSetting.php) | `public function execute(int $teamId, string $key, ?string $value, bool $encrypted = false): ServiceSetting` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [NumberingSequence.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/NumberingSequence.php) | `team_id`, `document_type`, `prefix`, `next_number`, `padding` |
| [Organization.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/Organization.php) | `team_id`, `name`, `code`, `description`, `state` |
| [Priority.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/Priority.php) | `team_id`, `name`, `code`, `color`, `sort_order`, `is_default`, `is_active` |
| [ServiceSetting.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/ServiceSetting.php) | `team_id`, `key`, `value`, `is_encrypted` |
| [Status.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/maintenance-maintenance-core/src/Models/Status.php) | `team_id`, `name`, `code`, `color`, `sort_order`, `is_default`, `is_active` |

| Observed API controller | Handler signatures |
| --- | --- |
| [NumberingController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-api/src/Http/Controllers/NumberingController.php) | `public function configure(Request $request, ConfigureNumbering $configure): JsonResponse`<br>`public function issue(Request $request, IssueNumber $issue): JsonResponse` |
| [OrganizationController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-api/src/Http/Controllers/OrganizationController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateOrganization $create): JsonResponse`<br>`public function show(Request $request, Organization $organization): JsonResponse`<br>`public function update(Request $request, Organization $organization, UpdateOrganization $update): JsonResponse`<br>`public function destroy(Request $request, Organization $organization, DeleteOrganization $delete): Response` |
| [PriorityController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-api/src/Http/Controllers/PriorityController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreatePriority $create): JsonResponse`<br>`public function update(Request $request, Priority $priority, UpdatePriority $update): JsonResponse`<br>`public function destroy(Request $request, Priority $priority, DeletePriority $delete): Response` |
| [ServiceSettingController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-api/src/Http/Controllers/ServiceSettingController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, SetServiceSetting $set): JsonResponse` |
| [StatusController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-api/src/Http/Controllers/StatusController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateStatus $create): JsonResponse`<br>`public function update(Request $request, Status $status, UpdateStatus $update): JsonResponse`<br>`public function destroy(Request $request, Status $status, DeleteStatus $delete): Response` |

**Observed route declarations:**

[modules/module-maintenance-core-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-api/routes/api.php)

```php
Route::middleware('api')
Route::middleware('auth:sanctum')->group(function (): void {
Route::get('organizations', [OrganizationController::class, 'index'])->name('organizations.index');
Route::post('organizations', [OrganizationController::class, 'store'])->name('organizations.store');
Route::get('organizations/{organization}', [OrganizationController::class, 'show'])->name('organizations.show');
Route::patch('organizations/{organization}', [OrganizationController::class, 'update'])->name('organizations.update');
Route::delete('organizations/{organization}', [OrganizationController::class, 'destroy'])->name('organizations.destroy');
Route::get('statuses', [StatusController::class, 'index'])->name('statuses.index');
Route::post('statuses', [StatusController::class, 'store'])->name('statuses.store');
Route::patch('statuses/{status}', [StatusController::class, 'update'])->name('statuses.update');
Route::delete('statuses/{status}', [StatusController::class, 'destroy'])->name('statuses.destroy');
Route::get('priorities', [PriorityController::class, 'index'])->name('priorities.index');
Route::post('priorities', [PriorityController::class, 'store'])->name('priorities.store');
Route::patch('priorities/{priority}', [PriorityController::class, 'update'])->name('priorities.update');
Route::delete('priorities/{priority}', [PriorityController::class, 'destroy'])->name('priorities.destroy');
Route::get('settings', [ServiceSettingController::class, 'index'])->name('settings.index');
Route::post('settings', [ServiceSettingController::class, 'store'])->name('settings.store');
Route::post('numbering/configure', [NumberingController::class, 'configure'])->name('numbering.configure');
Route::post('numbering/issue', [NumberingController::class, 'issue'])->name('numbering.issue');
```
<!-- layer-implementation-plan:end -->
