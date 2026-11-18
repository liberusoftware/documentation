# Accounting: Client Collaboration Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#client-collaboration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-client-collaboration-nuxt`
**Matching domain module:** `accounting-client-collaboration`
**Application:** Accounting
**Source feature:** [Client Collaboration](../features/client-collaboration.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/client-collaboration.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-client-collaboration` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Secure document requests:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Questions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tasks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Discussions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approvals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Status:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reminders:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Evidence:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-client-collaboration-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `secure-document-requests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `questions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tasks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `discussions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approvals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `status`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reminders`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `evidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-client-collaboration` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/client-collaboration.md)) |
| Capability Nuxt module skeleton | [`module-accounting-client-collaboration-nuxt`](https://github.com/liberusoftware/module-accounting-client-collaboration-nuxt) (`@liberusoftware/module-accounting-client-collaboration-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Secure document requests** | Expose composable and Vue 3 component for `secure document requests` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-collaboration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Questions** | Expose composable and Vue 3 component for `questions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-collaboration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Tasks** | Expose composable and Vue 3 component for `tasks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-collaboration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Discussions** | Expose composable and Vue 3 component for `discussions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-collaboration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approvals** | Expose composable and Vue 3 component for `approvals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-collaboration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Status** | Expose composable and Vue 3 component for `status` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-collaboration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reminders** | Expose composable and Vue 3 component for `reminders` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-collaboration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Evidence** | Expose composable and Vue 3 component for `evidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/client-collaboration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CollaborationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-client-collaboration/src/Queries/CollaborationQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCollaborationThread.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-client-collaboration/src/Actions/CreateCollaborationThread.php) | `public function handle(array $attributes): CollaborationThread` |
| [RecordCollaborationActivity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-client-collaboration/src/Actions/RecordCollaborationActivity.php) | `public function message(CollaborationThread $thread, array $message): CollaborationThread`<br>`public function approval(CollaborationThread $thread, array $approval): CollaborationThread`<br>`public function reminder(CollaborationThread $thread, array $reminder): CollaborationThread`<br>`public function evidence(CollaborationThread $thread, array $evidence): CollaborationThread` |
| [ResolveCollaboration.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-client-collaboration/src/Actions/ResolveCollaboration.php) | `public function approve(CollaborationThread $thread, string $approver): CollaborationThread`<br>`public function close(CollaborationThread $thread): CollaborationThread` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CollaborationThread.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-client-collaboration/src/Models/CollaborationThread.php) | `team_id`, `thread_ref`, `kind`, `subject`, `status`, `participants`, `messages`, `approvals`, `reminders`, `evidence` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CollaborationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-client-collaboration-api/src/Http/Controllers/CollaborationController.php) | `public function index(CollaborationQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCollaborationThread $action): JsonResponse`<br>`public function message(Request $request, string $thread, RecordCollaborationActivity $action): JsonResponse`<br>`public function approval(Request $request, string $thread, RecordCollaborationActivity $action): JsonResponse`<br>`public function evidence(Request $request, string $thread, RecordCollaborationActivity $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-client-collaboration-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-client-collaboration-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/client-collaboration')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.client-collaboration.read')->get('/', [CollaborationController::class, 'index']);
Route::middleware('ability:accounting.client-collaboration.write')->group(function (): void {
Route::post('/', [CollaborationController::class, 'store']);
Route::post('/{thread}/messages', [CollaborationController::class, 'message']);
Route::post('/{thread}/approvals', [CollaborationController::class, 'approval']);
Route::post('/{thread}/evidence', [CollaborationController::class, 'evidence']);
```
<!-- layer-implementation-plan:end -->
