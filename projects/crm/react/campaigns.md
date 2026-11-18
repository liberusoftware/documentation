# CRM: Campaigns React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#campaigns). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-campaigns-react-inertia`
**Matching domain module:** `crm-campaigns`
**Application:** CRM
**Source feature:** [Campaigns](../features/campaigns.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/campaigns.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Campaign hierarchy:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Briefs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Objectives:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Budget:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Assets:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Channels:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Audience:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Owners:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Calendar:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tasks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Costs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Responses:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Influence:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **ROI:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-campaigns-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `campaign-hierarchy`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `briefs`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `objectives`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `budget`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `assets`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `channels`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `audience`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `owners`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `calendar`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `tasks`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `costs`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `responses`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `influence`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `roi`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-campaigns` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-crm-campaigns-react-inertia`](https://github.com/liberusoftware/module-crm-campaigns-react-inertia) (`@liberusoftware/module-crm-campaigns-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/campaigns.md) · [Core plan](../core/campaigns.md) · [API plan](../api/campaigns.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Campaign hierarchy** | Render `campaign hierarchy` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Briefs** | Render `briefs` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Objectives** | Render `objectives` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Budget** | Render `budget` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Assets** | Render `assets` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Channels** | Render `channels` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Audience** | Render `audience` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Owners** | Render `owners` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Calendar** | Render `calendar` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Tasks** | Render `tasks` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Costs** | Render `costs` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Responses** | Render `responses` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Influence** | Render `influence` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **ROI** | Render `roi` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CampaignQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Queries/CampaignQuery.php) | `public function campaigns(int $teamId): Builder`<br>`public function roi(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Actions/CreateCampaign.php) | `public function execute(int $teamId, int $ownerId, array $input): Campaign` |
| [RecordCampaignEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Actions/RecordCampaignEvent.php) | `public function execute(int $teamId, int $actorId, Campaign $campaign, string $type, float $value = 0, array $payload = []): CampaignEvent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Campaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Models/Campaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [CampaignEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns/src/Models/CampaignEvent.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CampaignsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns-api/src/Http/Controllers/CampaignsController.php) | `public function __construct(private readonly CampaignQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateCampaign $a): JsonResponse`<br>`public function event(Campaign $campaign, RecordCampaignEvent $a): JsonResponse`<br>`public function roi(): JsonResponse` |

**Observed route declarations:**

[modules/crm-campaigns-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-campaigns-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/campaigns')->group(function (): void {
Route::get('/', [CampaignsController::class, 'index']);
Route::post('/', [CampaignsController::class, 'store']);
Route::post('{campaign}/events', [CampaignsController::class, 'event']);
Route::get('roi', [CampaignsController::class, 'roi']);
```
<!-- layer-implementation-plan:end -->
