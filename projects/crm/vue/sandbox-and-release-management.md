# CRM: Sandbox and Release Management Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sandbox-and-release-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-sandbox-and-release-management-vue-inertia`
**Matching domain module:** `crm-sandbox-and-release-management`
**Application:** CRM
**Source feature:** [Sandbox and Release Management](../features/sandbox-and-release-management.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/sandbox-and-release-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Configuration snapshots:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Test data policy:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Change sets:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Validation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Dependency analysis:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Promotion:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rollback:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Environment comparison:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-sandbox-and-release-management-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `configuration-snapshots`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `test-data-policy`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `change-sets`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `validation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `dependency-analysis`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `promotion`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `rollback`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `environment-comparison`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-sandbox-and-release-management` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-sandbox-and-release-management-vue-inertia`](https://github.com/liberusoftware/module-crm-sandbox-and-release-management-vue-inertia) (`@liberusoftware/module-crm-sandbox-and-release-management-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/sandbox-and-release-management.md) · [Core plan](../core/sandbox-and-release-management.md) · [API plan](../api/sandbox-and-release-management.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Configuration snapshots** | Render `configuration snapshots` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Test data policy** | Render `test data policy` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Change sets** | Render `change sets` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Validation** | Render `validation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Dependency analysis** | Render `dependency analysis` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Promotion** | Render `promotion` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Rollback** | Render `rollback` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Environment comparison** | Render `environment comparison` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ReleaseQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Queries/ReleaseQuery.php) | `public function snapshots(int $teamId)`<br>`public function changesets(int $teamId)`<br>`public function deployments(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/CreateChangeset.php) | `public function execute(int $teamId, int $actorId, array $data): ReleaseChangeset` |
| [CreateSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/CreateSnapshot.php) | `public function execute(int $teamId, int $actorId, array $data): ReleaseSnapshot` |
| [PromoteChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/PromoteChangeset.php) | `public function execute(int $teamId, int $actorId, int $id, array $data = []): ReleaseDeployment` |
| [RollbackChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/RollbackChangeset.php) | `public function execute(int $teamId, int $actorId, int $id, array $data = []): ReleaseDeployment` |
| [ValidateChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Actions/ValidateChangeset.php) | `public function execute(int $teamId, int $actorId, int $id): ReleaseChangeset` |
| [ReleaseAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Services/ReleaseAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [ReleasePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Services/ReleasePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReleaseChangeset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseChangeset.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReleaseDeployment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseDeployment.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReleaseSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management/src/Models/ReleaseSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReleaseController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management-api/src/Http/Controllers/ReleaseController.php) | `public function snapshots(Request $r, ReleaseQuery $q)`<br>`public function snapshot(Request $r, CreateSnapshot $a)`<br>`public function changesets(Request $r, ReleaseQuery $q)`<br>`public function changeset(Request $r, CreateChangeset $a)`<br>`public function validateSet(Request $r, int $set, ValidateChangeset $a)`<br>`public function promote(Request $r, int $set, PromoteChangeset $a)`<br>`public function rollback(Request $r, int $set, RollbackChangeset $a)` |

**Observed route declarations:**

[modules/crm-sandbox-and-release-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sandbox-and-release-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/sandbox-and-release-management')->group(function (): void {
Route::get('/snapshots', [ReleaseController::class, 'snapshots']);
Route::post('/snapshots', [ReleaseController::class, 'snapshot']);
Route::get('/changesets', [ReleaseController::class, 'changesets']);
Route::post('/changesets', [ReleaseController::class, 'changeset']);
Route::post('/changesets/{set}/validate', [ReleaseController::class, 'validateSet']);
Route::post('/changesets/{set}/promote', [ReleaseController::class, 'promote']);
Route::post('/changesets/{set}/rollback', [ReleaseController::class, 'rollback']);
```
<!-- layer-implementation-plan:end -->
