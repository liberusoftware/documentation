# Accounting: Multi-Entity React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#multi-entity). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-multi-entity-react-inertia`
**Matching domain module:** `accounting-multi-entity`
**Application:** Accounting
**Source feature:** [Multi-Entity](../features/multi-entity.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/multi-entity.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Entity books:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Shared master-data policy:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Access:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Entity switching:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Separate periods/tax:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Standardized mappings:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reporting:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-multi-entity-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `entity-books`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `shared-master-data-policy`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `access`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `entity-switching`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `separate-periods-tax`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `standardized-mappings`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `reporting`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-multi-entity` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-multi-entity-react-inertia`](https://github.com/liberusoftware/module-accounting-multi-entity-react-inertia) (`@liberusoftware/module-accounting-multi-entity-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/multi-entity.md) · [Core plan](../core/multi-entity.md) · [API plan](../api/multi-entity.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Entity books** | Render `entity books` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Shared master-data policy** | Render `shared master-data policy` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Access** | Render `access` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Entity switching** | Render `entity switching` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Separate periods/tax** | Render `separate periods/tax` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Standardized mappings** | Render `standardized mappings` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Reporting** | Render `reporting` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EntityQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Queries/EntityQuery.php) | `public function paginate(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function report(EntityBook $entity): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateEntityBook.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/CreateEntityBook.php) | `public function handle(array $attributes): EntityBook` |
| [CreateEntityMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/CreateEntityMapping.php) | `public function handle(EntityBook $entity, string $type, string $source, string $target): EntityMapping` |
| [CreateEntityPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/CreateEntityPeriod.php) | `public function handle(EntityBook $entity, array $attributes): EntityPeriod` |
| [GrantEntityAccess.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/GrantEntityAccess.php) | `public function handle(EntityBook $entity, string $userRef, string $role, array $permissions = [], bool $default = false): EntityAccess` |
| [SetMasterDataPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/SetMasterDataPolicy.php) | `public function handle(EntityBook $entity, string $key, string $mode, array $configuration = []): MasterDataPolicy` |
| [SwitchEntity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/SwitchEntity.php) | `public function handle(EntityBook $entity, string $userRef, string $sessionRef): EntitySwitch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EntityAccess.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntityAccess.php) | `entity_id`, `user_ref`, `role`, `permissions`, `is_default`, `metadata` |
| [EntityBook.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntityBook.php) | `team_id`, `entity_ref`, `code`, `name`, `base_currency`, `timezone`, `tax_registration`, `status`, `metadata` |
| [EntityMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntityMapping.php) | `entity_id`, `mapping_type`, `source_ref`, `target_ref`, `description`, `is_active`, `metadata` |
| [EntityPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntityPeriod.php) | `entity_id`, `period_ref`, `starts_on`, `ends_on`, `tax_configuration`, `status`, `closed_by`, `closed_at`, `metadata` |
| [EntitySwitch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntitySwitch.php) | `entity_id`, `user_ref`, `session_ref`, `switched_at`, `metadata` |
| [MasterDataPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/MasterDataPolicy.php) | `entity_id`, `policy_key`, `mode`, `configuration`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MultiEntityController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity-api/src/Http/Controllers/MultiEntityController.php) | `public function index(Request $request, EntityQuery $query): mixed`<br>`public function store(Request $request, CreateEntityBook $action): JsonResponse`<br>`public function show(EntityBook $entityBook): EntityResource`<br>`public function access(Request $request, EntityBook $entityBook, GrantEntityAccess $action): JsonResponse`<br>`public function switch(Request $request, EntityBook $entityBook, SwitchEntity $action): JsonResponse`<br>`public function period(Request $request, EntityBook $entityBook, CreateEntityPeriod $action): JsonResponse`<br>`public function policy(Request $request, EntityBook $entityBook, SetMasterDataPolicy $action): JsonResponse`<br>`public function mapping(Request $request, EntityBook $entityBook, CreateEntityMapping $action): JsonResponse`<br>`public function report(EntityBook $entityBook, EntityQuery $query): array` |

**Observed route declarations:**

[modules/accounting-multi-entity-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/multi-entity')->group(function (): void {
Route::get('/', [MultiEntityController::class, 'index'])->name('accounting.multi-entity.list');
Route::post('/', [MultiEntityController::class, 'store'])->name('accounting.multi-entity.create');
Route::get('/{entityBook}', [MultiEntityController::class, 'show'])->name('accounting.multi-entity.show');
Route::post('/{entityBook}/access', [MultiEntityController::class, 'access'])->name('accounting.multi-entity.access');
Route::post('/{entityBook}/switch', [MultiEntityController::class, 'switch'])->name('accounting.multi-entity.switch');
Route::post('/{entityBook}/periods', [MultiEntityController::class, 'period'])->name('accounting.multi-entity.period');
Route::post('/{entityBook}/policy', [MultiEntityController::class, 'policy'])->name('accounting.multi-entity.policy');
Route::post('/{entityBook}/mappings', [MultiEntityController::class, 'mapping'])->name('accounting.multi-entity.mapping');
Route::get('/{entityBook}/report', [MultiEntityController::class, 'report'])->name('accounting.multi-entity.report');
```
<!-- layer-implementation-plan:end -->
