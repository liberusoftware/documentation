# Accounting: Custom Report Builder React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#custom-report-builder). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-custom-report-builder-react-inertia`
**Matching domain module:** `accounting-custom-report-builder`
**Application:** Accounting
**Source feature:** [Custom Report Builder](../features/custom-report-builder.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/custom-report-builder.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Governed measures/dimensions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Filters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Grouping:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Formulas:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Comparisons:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Layouts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Permissions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Saved variants:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Exports:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-custom-report-builder-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `governed-measures-dimensions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `filters`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `grouping`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `formulas`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `comparisons`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `layouts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `permissions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `saved-variants`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `exports`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-custom-report-builder` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-custom-report-builder-react-inertia`](https://github.com/liberusoftware/module-accounting-custom-report-builder-react-inertia) (`@liberusoftware/module-accounting-custom-report-builder-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/custom-report-builder.md) · [Core plan](../core/custom-report-builder.md) · [API plan](../api/custom-report-builder.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Governed measures/dimensions** | Render `governed measures/dimensions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Filters** | Render `filters` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Grouping** | Render `grouping` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Formulas** | Render `formulas` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Comparisons** | Render `comparisons` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Layouts** | Render `layouts` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Permissions** | Render `permissions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Saved variants** | Render `saved variants` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Exports** | Render `exports` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CustomReportQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Queries/CustomReportQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCustomReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Actions/CreateCustomReport.php) | `public function handle(array $attributes): CustomReport` |
| [RequestReportExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Actions/RequestReportExport.php) | `public function handle(CustomReport $report, string $format, array $parameters = []): CustomReportExport` |
| [SaveReportVariant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Actions/SaveReportVariant.php) | `public function handle(CustomReport $report, string $variantRef, array $configuration): CustomReportVariant` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CustomReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Models/CustomReport.php) | `team_id`, `report_ref`, `name`, `measures`, `dimensions`, `filters`, `grouping`, `formulas`, `comparisons`, `layout`, `permissions` |
| [CustomReportExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Models/CustomReportExport.php) | `report_id`, `team_id`, `format`, `status`, `parameters`, `completed_at` |
| [CustomReportVariant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder/src/Models/CustomReportVariant.php) | `report_id`, `team_id`, `variant_ref`, `configuration` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CustomReportsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder-api/src/Http/Controllers/CustomReportsController.php) | `public function index(CustomReportQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCustomReport $action): JsonResponse`<br>`public function variant(Request $request, string $report, SaveReportVariant $action): JsonResponse`<br>`public function export(Request $request, string $report, RequestReportExport $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-custom-report-builder-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-custom-report-builder-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/custom-report-builder')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.custom-report-builder.read')->get('/', [CustomReportsController::class, 'index']);
Route::middleware('ability:accounting.custom-report-builder.write')->group(function (): void {
Route::post('/', [CustomReportsController::class, 'store']);
Route::post('/{report}/variants', [CustomReportsController::class, 'variant']);
Route::post('/{report}/exports', [CustomReportsController::class, 'export']);
```
<!-- layer-implementation-plan:end -->
