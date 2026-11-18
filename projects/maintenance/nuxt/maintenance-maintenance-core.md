# Maintenance: Maintenance Maintenance Core Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#maintenance-maintenance-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-maintenance-maintenance-maintenance-core-nuxt`
**Matching domain module:** `maintenance-maintenance-core`
**Application:** Maintenance
**Source feature:** [Maintenance Maintenance Core](../features/maintenance-maintenance-core.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/maintenance-maintenance-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `maintenance-maintenance-core` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Organizations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Service settings:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Statuses:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Numbering:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Priorities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Shared events:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-maintenance-maintenance-core-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `organizations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `service-settings`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `statuses`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `numbering`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `priorities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `shared-events`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `maintenance-maintenance-core` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/maintenance-maintenance-core.md)) |
| Capability Nuxt module skeleton | [`module-maintenance-maintenance-core-nuxt`](https://github.com/liberusoftware/module-maintenance-maintenance-core-nuxt) (`@liberusoftware/module-maintenance-maintenance-core-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Organizations** | Expose composable and Vue 3 component for `organizations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/maintenance-maintenance-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Service settings** | Expose composable and Vue 3 component for `service settings` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/maintenance-maintenance-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Statuses** | Expose composable and Vue 3 component for `statuses` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/maintenance-maintenance-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Numbering** | Expose composable and Vue 3 component for `numbering` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/maintenance-maintenance-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Priorities** | Expose composable and Vue 3 component for `priorities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/maintenance-maintenance-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Shared events** | Expose composable and Vue 3 component for `shared events` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/maintenance-maintenance-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |

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
