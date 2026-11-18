# CRM: Crm Service Analytics React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-service-analytics). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-crm-service-analytics-react-inertia`
**Matching domain module:** `crm-service-analytics`
**Application:** CRM
**Source feature:** [Crm Service Analytics](../features/crm-service-analytics.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-service-analytics.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Volume:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Backlog:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Deflection:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **First response:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Resolution:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reopen:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Transfer:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **SLA:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Satisfaction:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Quality:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Staffing:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Cost-to-serve:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-crm-service-analytics-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `volume`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `backlog`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `deflection`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `first-response`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `resolution`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `reopen`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `transfer`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `sla`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `satisfaction`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `quality`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `staffing`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `cost-to-serve`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-service-analytics` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-crm-service-analytics-react-inertia`](https://github.com/liberusoftware/module-crm-service-analytics-react-inertia) (`@liberusoftware/module-crm-service-analytics-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/crm-service-analytics.md) · [Core plan](../core/crm-service-analytics.md) · [API plan](../api/crm-service-analytics.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Volume** | Render `volume` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Backlog** | Render `backlog` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Deflection** | Render `deflection` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **First response** | Render `first response` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Resolution** | Render `resolution` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Reopen** | Render `reopen` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Transfer** | Render `transfer` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **SLA** | Render `sla` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Satisfaction** | Render `satisfaction` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Quality** | Render `quality` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Staffing** | Render `staffing` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Cost-to-serve** | Render `cost-to-serve` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AnalyticsQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Queries/AnalyticsQuery.php) | `public function snapshots(int $teamId)`<br>`public function metric(int $teamId, string $metric, $from = null, $to = null)`<br>`public function summary(int $teamId, $from = null, $to = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordMetric.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Actions/RecordMetric.php) | `public function execute(int $teamId, int $actorId, array $data): AnalyticsSnapshot` |
| [RecordServiceMetrics.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Actions/RecordServiceMetrics.php) | `public function execute(int $teamId, int $actorId, array $metrics): int` |
| [AnalyticsAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Services/AnalyticsAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): Audit` |
| [AnalyticsPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Services/AnalyticsPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AnalyticsAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Models/AnalyticsAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [AnalyticsSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Models/AnalyticsSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AnalyticsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics-api/src/Http/Controllers/AnalyticsController.php) | `public function index(Request $r, AnalyticsQuery $q)`<br>`public function metric(Request $r, string $metric, AnalyticsQuery $q)`<br>`public function summary(Request $r, AnalyticsQuery $q)`<br>`public function store(Request $r, RecordMetric $a)`<br>`public function batch(Request $r, RecordServiceMetrics $a)` |

**Observed route declarations:**

[modules/crm-service-analytics-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/service-analytics')->group(function (): void {
Route::get('/snapshots', [AnalyticsController::class, 'index']);
Route::get('/metrics/{metric}', [AnalyticsController::class, 'metric']);
Route::get('/summary', [AnalyticsController::class, 'summary']);
Route::post('/snapshots', [AnalyticsController::class, 'store']);
Route::post('/snapshots/batch', [AnalyticsController::class, 'batch']);
```
<!-- layer-implementation-plan:end -->
