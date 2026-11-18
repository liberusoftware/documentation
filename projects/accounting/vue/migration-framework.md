# Accounting: Migration Framework Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#migration-framework). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-migration-framework-vue-inertia`
**Matching domain module:** `accounting-migration-framework`
**Application:** Accounting
**Source feature:** [Migration Framework](../features/migration-framework.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/migration-framework.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Source inventory:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Mapping:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Dry run:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Transforms:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Validation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Batches:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Resume:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Attachments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Errors:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Counts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-migration-framework-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `source-inventory`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `mapping`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `dry-run`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `transforms`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `validation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `batches`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `resume`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `attachments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `errors`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `counts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `reconciliation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-migration-framework` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-migration-framework-vue-inertia`](https://github.com/liberusoftware/module-accounting-migration-framework-vue-inertia) (`@liberusoftware/module-accounting-migration-framework-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/migration-framework.md) · [Core plan](../core/migration-framework.md) · [API plan](../api/migration-framework.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Source inventory** | Render `source inventory` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Mapping** | Render `mapping` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Dry run** | Render `dry run` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Transforms** | Render `transforms` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Validation** | Render `validation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Batches** | Render `batches` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Resume** | Render `resume` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Attachments** | Render `attachments` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Errors** | Render `errors` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Counts** | Render `counts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Reconciliation** | Render `reconciliation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [MigrationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Queries/MigrationQuery.php) | `public function sources(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function batches(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function counts(MigrationBatch $batch): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/CreateBatch.php) | `public function handle(MigrationSource $source, MigrationMapping $mapping, array $attributes, array $rows = []): MigrationBatch` |
| [CreateMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/CreateMapping.php) | `public function handle(MigrationSource $source, array $attributes): MigrationMapping` |
| [ReconcileBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/ReconcileBatch.php) | `public function handle(MigrationBatch $batch, array $attributes = []): MigrationReconciliation` |
| [RegisterSource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/RegisterSource.php) | `public function handle(array $attributes): MigrationSource` |
| [RunBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/RunBatch.php) | `public function handle(MigrationBatch $batch, bool $dryRun = false, int $limit = 100): MigrationBatch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MigrationAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationAttachment.php) | `batch_id`, `file_ref`, `name`, `mime_type`, `size_bytes`, `checksum`, `metadata` |
| [MigrationBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationBatch.php) | `team_id`, `batch_ref`, `source_id`, `mapping_id`, `status`, `dry_run`, `resume_token`, `total_count`, `processed_count`, `success_count`, `error_count`, `skipped_count`, `started_at`, `completed_at`, `paused_at`, `failure_message`, `metadata` |
| [MigrationMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationMapping.php) | `source_id`, `mapping_ref`, `entity_type`, `field_map`, `transforms`, `validation_rules`, `version`, `active`, `metadata` |
| [MigrationReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationReconciliation.php) | `batch_id`, `source_count`, `imported_count`, `failed_count`, `source_total`, `destination_total`, `variance`, `status`, `notes`, `metadata` |
| [MigrationRow.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationRow.php) | `batch_id`, `row_ref`, `source_key`, `destination_key`, `payload`, `transformed_payload`, `status`, `error_code`, `error_message`, `attempts`, `processed_at`, `metadata` |
| [MigrationSource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationSource.php) | `team_id`, `source_ref`, `provider`, `source_type`, `name`, `record_count`, `checksum`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MigrationFrameworkController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework-api/src/Http/Controllers/MigrationFrameworkController.php) | `public function sources(Request $request, MigrationQuery $query): mixed`<br>`public function source(Request $request, RegisterSource $action): JsonResponse`<br>`public function mapping(Request $request, MigrationSource $source, CreateMapping $action): JsonResponse`<br>`public function batches(Request $request, MigrationQuery $query): mixed`<br>`public function batch(Request $request, MigrationSource $source, CreateBatch $action): MigrationBatchResource`<br>`public function dryRun(MigrationBatch $batch, RunBatch $action): MigrationBatchResource`<br>`public function resume(MigrationBatch $batch, RunBatch $action): MigrationBatchResource`<br>`public function reconcile(Request $request, MigrationBatch $batch, ReconcileBatch $action): JsonResponse`<br>`public function counts(MigrationBatch $batch, MigrationQuery $query): array` |

**Observed route declarations:**

[modules/accounting-migration-framework-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/migration-framework')->group(function (): void {
Route::get('/sources', [MigrationFrameworkController::class, 'sources'])->name('accounting.migration-framework.sources');
Route::post('/sources', [MigrationFrameworkController::class, 'source'])->name('accounting.migration-framework.source');
Route::post('/sources/{source}/mappings', [MigrationFrameworkController::class, 'mapping'])->name('accounting.migration-framework.mapping');
Route::get('/batches', [MigrationFrameworkController::class, 'batches'])->name('accounting.migration-framework.batches');
Route::post('/sources/{source}/batches', [MigrationFrameworkController::class, 'batch'])->name('accounting.migration-framework.batch');
Route::post('/batches/{batch}/dry-run', [MigrationFrameworkController::class, 'dryRun'])->name('accounting.migration-framework.dry-run');
Route::post('/batches/{batch}/resume', [MigrationFrameworkController::class, 'resume'])->name('accounting.migration-framework.resume');
Route::post('/batches/{batch}/reconcile', [MigrationFrameworkController::class, 'reconcile'])->name('accounting.migration-framework.reconcile');
Route::get('/batches/{batch}/counts', [MigrationFrameworkController::class, 'counts'])->name('accounting.migration-framework.counts');
```
<!-- layer-implementation-plan:end -->
