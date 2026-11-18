# Accounting: Workpapers Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#workpapers). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-workpapers-nuxt`
**Matching domain module:** `accounting-workpapers`
**Application:** Accounting
**Source feature:** [Workpapers](../features/workpapers.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/workpapers.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-workpapers` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Lead schedules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **References:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attachments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Procedures:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Conclusions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Preparer/reviewer:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rollover:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Export:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-workpapers-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `lead-schedules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `attachments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `procedures`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `conclusions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `preparer-reviewer`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rollover`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `export`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-workpapers` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/workpapers.md)) |
| Capability Nuxt module skeleton | [`module-accounting-workpapers-nuxt`](https://github.com/liberusoftware/module-accounting-workpapers-nuxt) (`@liberusoftware/module-accounting-workpapers-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Lead schedules** | Expose composable and Vue 3 component for `lead schedules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/workpapers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **References** | Expose composable and Vue 3 component for `references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/workpapers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Attachments** | Expose composable and Vue 3 component for `attachments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/workpapers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Procedures** | Expose composable and Vue 3 component for `procedures` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/workpapers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Conclusions** | Expose composable and Vue 3 component for `conclusions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/workpapers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Preparer/reviewer** | Expose composable and Vue 3 component for `preparer/reviewer` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/workpapers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Rollover** | Expose composable and Vue 3 component for `rollover` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/workpapers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Export** | Expose composable and Vue 3 component for `export` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/workpapers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddWorkpaperAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperAttachment.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperAttachment` |
| [AddWorkpaperProcedure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperProcedure.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperProcedure` |
| [AddWorkpaperReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AddWorkpaperReference.php) | `public function handle(Workpaper $workpaper, array $attributes): WorkpaperReference` |
| [AssignWorkpaperReviewer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/AssignWorkpaperReviewer.php) | `public function handle(Workpaper $workpaper, int $reviewerId): Workpaper` |
| [ConcludeWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/ConcludeWorkpaper.php) | `public function handle(Workpaper $workpaper, string $conclusion): Workpaper` |
| [CreateWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/CreateWorkpaper.php) | `public function handle(array $attributes): Workpaper` |
| [RequestWorkpaperExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/RequestWorkpaperExport.php) | `public function handle(Workpaper $workpaper, string $format): WorkpaperExport` |
| [RolloverWorkpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Actions/RolloverWorkpaper.php) | `public function handle(Workpaper $source, array $attributes = []): Workpaper` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Workpaper.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/Workpaper.php) | `team_id`, `title`, `reference`, `status`, `period_start`, `period_end`, `preparer_id`, `reviewer_id`, `conclusion`, `metadata` |
| [WorkpaperAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperAttachment.php) | `workpaper_id`, `name`, `disk`, `path`, `mime_type`, `size` |
| [WorkpaperExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperExport.php) | `workpaper_id`, `format`, `status`, `path`, `error` |
| [WorkpaperProcedure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperProcedure.php) | `workpaper_id`, `description`, `status`, `performed_by`, `performed_at`, `evidence` |
| [WorkpaperReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers/src/Models/WorkpaperReference.php) | `workpaper_id`, `label`, `target_type`, `target_id`, `notes` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WorkpapersController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers-api/src/Http/Controllers/WorkpapersController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateWorkpaper $action): mixed`<br>`public function procedure(Request $request, string $workpaper, AddWorkpaperProcedure $action): mixed`<br>`public function reference(Request $request, string $workpaper, AddWorkpaperReference $action): mixed`<br>`public function attachment(Request $request, string $workpaper, AddWorkpaperAttachment $action): mixed`<br>`public function reviewer(Request $request, string $workpaper, AssignWorkpaperReviewer $action): mixed`<br>`public function conclude(Request $request, string $workpaper, ConcludeWorkpaper $action): mixed`<br>`public function rollover(Request $request, string $workpaper, RolloverWorkpaper $action): mixed`<br>`public function export(Request $request, string $workpaper, RequestWorkpaperExport $action): mixed` |

**Observed route declarations:**

[modules/accounting-workpapers-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-workpapers-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/workpapers')->middleware('auth:sanctum')->group(function (): void {
Route::get('/', [WorkpapersController::class, 'index'])->middleware('ability:accounting.workpapers.read');
Route::post('/', [WorkpapersController::class, 'store'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/references', [WorkpapersController::class, 'reference'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/attachments', [WorkpapersController::class, 'attachment'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/procedures', [WorkpapersController::class, 'procedure'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/reviewer', [WorkpapersController::class, 'reviewer'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/conclude', [WorkpapersController::class, 'conclude'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/rollover', [WorkpapersController::class, 'rollover'])->middleware('ability:accounting.workpapers.write');
Route::post('/{workpaper}/exports', [WorkpapersController::class, 'export'])->middleware('ability:accounting.workpapers.write');
```
<!-- layer-implementation-plan:end -->
