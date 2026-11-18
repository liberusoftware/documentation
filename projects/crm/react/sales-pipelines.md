# CRM: Sales Pipelines React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-pipelines). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-sales-pipelines-react-inertia`
**Matching domain module:** `crm-sales-pipelines`
**Application:** CRM
**Source feature:** [Sales Pipelines](../features/sales-pipelines.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/sales-pipelines.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Multiple pipelines:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Stages:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Opportunities:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Products:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Values:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Probabilities:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Close dates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Competitors:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Dependencies:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Stage history:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rotting:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Loss reasons:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-sales-pipelines-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `multiple-pipelines`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `stages`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `opportunities`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `products`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `values`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `probabilities`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `close-dates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `competitors`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `dependencies`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `stage-history`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `rotting`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `loss-reasons`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-sales-pipelines` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-crm-sales-pipelines-react-inertia`](https://github.com/liberusoftware/module-crm-sales-pipelines-react-inertia) (`@liberusoftware/module-crm-sales-pipelines-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/sales-pipelines.md) · [Core plan](../core/sales-pipelines.md) · [API plan](../api/sales-pipelines.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Multiple pipelines** | Render `multiple pipelines` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Stages** | Render `stages` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Opportunities** | Render `opportunities` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Products** | Render `products` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Values** | Render `values` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Probabilities** | Render `probabilities` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Close dates** | Render `close dates` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Competitors** | Render `competitors` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Dependencies** | Render `dependencies` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Stage history** | Render `stage history` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Rotting** | Render `rotting` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Loss reasons** | Render `loss reasons` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PipelineQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Queries/PipelineQuery.php) | `public function pipelines(int $teamId)`<br>`public function stages(int $teamId, int $pipelineId)`<br>`public function opportunities(int $teamId)`<br>`public function rottingOpportunities(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CloseOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CloseOpportunity.php) | `public function execute(int $teamId, int $actorId, int $id, string $status, ?string $reason = null): Opportunity` |
| [CreateOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreateOpportunity.php) | `public function execute(int $teamId, int $actorId, array $data): Opportunity` |
| [CreatePipeline.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreatePipeline.php) | `public function execute(int $teamId, int $actorId, array $data): SalesPipeline` |
| [CreateStage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/CreateStage.php) | `public function execute(int $teamId, int $actorId, array $data): SalesStage` |
| [MoveOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Actions/MoveOpportunity.php) | `public function execute(int $teamId, int $actorId, int $id, array $data): Opportunity` |
| [PipelineAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Services/PipelineAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [PipelinePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Services/PipelinePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Opportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/Opportunity.php) | No literal fillable array detected; inspect the model and API schema. |
| [SalesPipeline.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/SalesPipeline.php) | No literal fillable array detected; inspect the model and API schema. |
| [SalesStage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/SalesStage.php) | No literal fillable array detected; inspect the model and API schema. |
| [StageHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines/src/Models/StageHistory.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PipelineController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-api/src/Http/Controllers/PipelineController.php) | `public function pipelines(Request $r, PipelineQuery $q)`<br>`public function pipeline(Request $r, CreatePipeline $a)`<br>`public function stage(Request $r, CreateStage $a)`<br>`public function opportunities(Request $r, PipelineQuery $q)`<br>`public function rottingOpportunities(Request $r, PipelineQuery $q)`<br>`public function opportunity(Request $r, CreateOpportunity $a)`<br>`public function move(Request $r, int $opportunity, MoveOpportunity $a)`<br>`public function close(Request $r, int $opportunity, string $status, CloseOpportunity $a)` |

**Observed route declarations:**

[modules/crm-sales-pipelines-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-pipelines-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/sales-pipelines')->group(function (): void {
Route::get('/pipelines', [PipelineController::class, 'pipelines']);
Route::post('/pipelines', [PipelineController::class, 'pipeline']);
Route::post('/stages', [PipelineController::class, 'stage']);
Route::get('/opportunities', [PipelineController::class, 'opportunities']);
Route::get('/opportunities/rotting', [PipelineController::class, 'rottingOpportunities']);
Route::post('/opportunities', [PipelineController::class, 'opportunity']);
Route::post('/opportunities/{opportunity}/move', [PipelineController::class, 'move']);
Route::post('/opportunities/{opportunity}/close/{status}', [PipelineController::class, 'close'])->whereIn('status', ['won', 'lost']);
```
<!-- layer-implementation-plan:end -->

Read the [source-backed sales-pipeline walkthrough](../guides/SALES-PIPELINES.md) for actual actions, routes, permissions, UI behavior and differences from the target design.
