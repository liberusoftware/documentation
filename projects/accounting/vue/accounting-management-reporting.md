# Accounting: Accounting Management Reporting Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-management-reporting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-accounting-management-reporting-vue-inertia`
**Matching domain module:** `accounting-management-reporting`
**Application:** Accounting
**Source feature:** [Accounting Management Reporting](../features/accounting-management-reporting.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-management-reporting.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Report packs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Narratives:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Charts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Schedules:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Review:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Approval:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **PDF/spreadsheet delivery:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Archive:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-management-reporting-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `report-packs`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `narratives`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `charts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `schedules`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `review`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `approval`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `pdf-spreadsheet-delivery`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `archive`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-management-reporting` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-management-reporting-vue-inertia`](https://github.com/liberusoftware/module-accounting-management-reporting-vue-inertia) (`@liberusoftware/module-accounting-management-reporting-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/accounting-management-reporting.md) · [Core plan](../core/accounting-management-reporting.md) · [API plan](../api/accounting-management-reporting.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Report packs** | Render `report packs` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Narratives** | Render `narratives` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Charts** | Render `charts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Schedules** | Render `schedules` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Review** | Render `review` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Approval** | Render `approval` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **PDF/spreadsheet delivery** | Render `pdf/spreadsheet delivery` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Archive** | Render `archive` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ReportQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Queries/ReportQuery.php) | `public function packs(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function summary(ReportPack $report): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddReportContent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/AddReportContent.php) | `public function narrative(ReportPack $report, array $attributes): ReportNarrative`<br>`public function chart(ReportPack $report, array $attributes): ReportChart` |
| [ArchiveReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/ArchiveReport.php) | `public function handle(ReportPack $report): ReportPack` |
| [CreateReportPack.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/CreateReportPack.php) | `public function handle(array $attributes): ReportPack` |
| [DeliverReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/DeliverReport.php) | `public function handle(ReportPack $report, string $format, array $attributes = []): ReportDelivery` |
| [ReviewReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/ReviewReport.php) | `public function handle(ReportPack $report, string $actor, string $decision, ?string $comment = null): ReportPack` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReportChart.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportChart.php) | `report_pack_id`, `chart_ref`, `title`, `chart_type`, `data_source`, `series`, `options`, `metadata` |
| [ReportDelivery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportDelivery.php) | `report_pack_id`, `format`, `file_ref`, `status`, `recipients`, `checksum`, `delivered_at`, `failure_message`, `metadata` |
| [ReportNarrative.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportNarrative.php) | `report_pack_id`, `section_ref`, `title`, `body`, `author_ref`, `version`, `metadata` |
| [ReportPack.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportPack.php) | `team_id`, `report_ref`, `name`, `period_start`, `period_end`, `currency`, `status`, `version`, `owner_ref`, `approved_by`, `approved_at`, `delivered_at`, `archived_at`, `metadata` |
| [ReportReview.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportReview.php) | `report_pack_id`, `actor_ref`, `decision`, `comment`, `reviewed_at`, `metadata` |
| [ReportSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportSchedule.php) | `report_pack_id`, `frequency`, `timezone`, `recipients`, `next_run_at`, `active`, `last_run_at`, `failure_message`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ManagementReportingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting-api/src/Http/Controllers/ManagementReportingController.php) | `public function index(Request $request, ReportQuery $query): mixed`<br>`public function store(Request $request, CreateReportPack $action): ReportPackResource`<br>`public function show(ReportPack $reportPack): ReportPackResource`<br>`public function review(Request $request, ReportPack $reportPack, ReviewReport $action): ReportPackResource`<br>`public function deliver(Request $request, ReportPack $reportPack, DeliverReport $action): JsonResponse`<br>`public function archive(ReportPack $reportPack, ArchiveReport $action): ReportPackResource` |

**Observed route declarations:**

[modules/accounting-management-reporting-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/management-reporting')->group(function (): void {
Route::get('/packs', [ManagementReportingController::class, 'index'])->name('accounting.management-reporting.list');
Route::post('/packs', [ManagementReportingController::class, 'store'])->name('accounting.management-reporting.create');
Route::get('/packs/{reportPack}', [ManagementReportingController::class, 'show'])->name('accounting.management-reporting.show');
Route::post('/packs/{reportPack}/review', [ManagementReportingController::class, 'review'])->name('accounting.management-reporting.review');
Route::post('/packs/{reportPack}/deliver', [ManagementReportingController::class, 'deliver'])->name('accounting.management-reporting.deliver');
Route::post('/packs/{reportPack}/archive', [ManagementReportingController::class, 'archive'])->name('accounting.management-reporting.archive');
```
<!-- layer-implementation-plan:end -->
