# CRM: Revenue Intelligence React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-intelligence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-revenue-intelligence-react-inertia`
**Matching domain module:** `crm-revenue-intelligence`
**Application:** CRM
**Source feature:** [Revenue Intelligence](../features/revenue-intelligence.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/revenue-intelligence.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Pipeline inspection:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Health/risk:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Engagement gaps:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Opportunity scoring:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Relationship maps:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **White-space/next-product suggestions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Anomaly detection:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Alerts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-revenue-intelligence-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `pipeline-inspection`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `health-risk`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `engagement-gaps`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `opportunity-scoring`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `relationship-maps`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `white-space-next-product-suggestions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `anomaly-detection`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `alerts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-revenue-intelligence` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-crm-revenue-intelligence-react-inertia`](https://github.com/liberusoftware/module-crm-revenue-intelligence-react-inertia) (`@liberusoftware/module-crm-revenue-intelligence-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/revenue-intelligence.md) · [Core plan](../core/revenue-intelligence.md) · [API plan](../api/revenue-intelligence.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Pipeline inspection** | Render `pipeline inspection` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Health/risk** | Render `health/risk` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Engagement gaps** | Render `engagement gaps` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Opportunity scoring** | Render `opportunity scoring` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Relationship maps** | Render `relationship maps` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **White-space/next-product suggestions** | Render `white-space/next-product suggestions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Anomaly detection** | Render `anomaly detection` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Alerts** | Render `alerts` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [RevenueIntelligenceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Queries/RevenueIntelligenceQuery.php) | `public function insights(int $teamId)`<br>`public function alerts(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/CreateAlert.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueIntelligenceAlert` |
| [RecordInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/RecordInsight.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueInsight` |
| [ResolveAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/ResolveAlert.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $alertId): RevenueIntelligenceAlert` |
| [UpdateInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/UpdateInsight.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $insightId, array $input): RevenueInsight` |
| [RevenueIntelligencePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Services/RevenueIntelligencePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RevenueInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Models/RevenueInsight.php) | No literal fillable array detected; inspect the model and API schema. |
| [RevenueIntelligenceAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Models/RevenueIntelligenceAlert.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [RevenueIntelligenceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence-api/src/Http/Controllers/RevenueIntelligenceController.php) | `public function insights(Request $r, RevenueIntelligenceQuery $q)`<br>`public function insight(Request $r, RecordInsight $a)`<br>`public function alerts(Request $r, RevenueIntelligenceQuery $q)`<br>`public function alert(Request $r, CreateAlert $a)`<br>`public function resolve(Request $r, int $alert, ResolveAlert $a)` |

**Observed route declarations:**

[modules/crm-revenue-intelligence-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/revenue-intelligence')->group(function (): void {
Route::get('/insights', [RevenueIntelligenceController::class, 'insights']);
Route::post('/insights', [RevenueIntelligenceController::class, 'insight']);
Route::get('/alerts', [RevenueIntelligenceController::class, 'alerts']);
Route::post('/alerts', [RevenueIntelligenceController::class, 'alert']);
Route::post('/alerts/{alert}/resolve', [RevenueIntelligenceController::class, 'resolve']);
```
<!-- layer-implementation-plan:end -->
