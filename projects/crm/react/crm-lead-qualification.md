# CRM: Crm Lead Qualification React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-lead-qualification). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-crm-lead-qualification-react-inertia`
**Matching domain module:** `crm-lead-qualification`
**Application:** CRM
**Source feature:** [Crm Lead Qualification](../features/crm-lead-qualification.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-lead-qualification.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Lifecycle stages:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Fit/engagement scoring:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **MQL/PQL/SQL/service-qualified rules:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Qualification frameworks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Disqualification:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Nurture:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Conversion:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-crm-lead-qualification-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `lifecycle-stages`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `fit-engagement-scoring`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `mql-pql-sql-service-qualified-rules`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `qualification-frameworks`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `disqualification`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `nurture`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `conversion`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-lead-qualification` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-crm-lead-qualification-react-inertia`](https://github.com/liberusoftware/module-crm-lead-qualification-react-inertia) (`@liberusoftware/module-crm-lead-qualification-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/crm-lead-qualification.md) · [Core plan](../core/crm-lead-qualification.md) · [API plan](../api/crm-lead-qualification.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Lifecycle stages** | Render `lifecycle stages` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Fit/engagement scoring** | Render `fit/engagement scoring` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **MQL/PQL/SQL/service-qualified rules** | Render `mql/pql/sql/service-qualified rules` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Qualification frameworks** | Render `qualification frameworks` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Disqualification** | Render `disqualification` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Nurture** | Render `nurture` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Conversion** | Render `conversion` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [LeadQualificationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Queries/LeadQualificationQuery.php) | `public function forTeam(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConvertQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/ConvertQualification.php) | `public function execute(LeadQualification $qualification, ?int $actorId, ?string $reason = null): LeadQualification` |
| [CreateFramework.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/CreateFramework.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): QualificationFramework` |
| [CreateQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/CreateQualification.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): LeadQualification` |
| [DisqualifyQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/DisqualifyQualification.php) | `public function execute(LeadQualification $qualification, ?int $actorId, string $reason): LeadQualification` |
| [EnrollNurture.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/EnrollNurture.php) | `public function execute(LeadQualification $qualification, ?int $actorId, array $attributes): NurtureEnrollment` |
| [EvaluateQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/EvaluateQualification.php) | `public function execute(LeadQualification $qualification, ?int $actorId): LeadQualification` |
| [RecordQualificationEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/RecordQualificationEvent.php) | `public function __construct(private readonly LeadQualificationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, QualifiedLead $lead, array $input): QualificationEvent` |
| [ScoreLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/ScoreLead.php) | `public function __construct(private readonly LeadQualificationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, QualifiedLead $lead, array $input): QualifiedLead` |
| [TransitionLifecycle.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/TransitionLifecycle.php) | `public function execute(LeadQualification $qualification, ?int $actorId, string $stage, ?string $reason = null): LeadQualification` |
| [UpdateScores.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Actions/UpdateScores.php) | `public function execute(LeadQualification $qualification, ?int $actorId, array $scores): LeadQualification` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [LeadQualification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/LeadQualification.php) | `team_id`, `actor_id`, `subject_type`, `subject_id`, `framework_id`, `lifecycle_stage`, `fit_score`, `engagement_score`, `total_score`, `qualification_status`, `disqualification_reason`, `nurture_until`, `converted_at`, `version`, `metadata` |
| [NurtureEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/NurtureEnrollment.php) | `team_id`, `qualification_id`, `actor_id`, `status`, `sequence`, `starts_at`, `ends_at`, `metadata` |
| [QualificationEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualificationEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [QualificationFramework.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualificationFramework.php) | `team_id`, `actor_id`, `name`, `status`, `mql_threshold`, `pql_threshold`, `sql_threshold`, `service_qualified_threshold`, `rules`, `settings` |
| [QualificationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualificationRule.php) | No literal fillable array detected; inspect the model and API schema. |
| [QualifiedLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/QualifiedLead.php) | No literal fillable array detected; inspect the model and API schema. |
| [StageHistory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification/src/Models/StageHistory.php) | `team_id`, `qualification_id`, `actor_id`, `from_stage`, `to_stage`, `reason` |

| Observed API controller | Handler signatures |
| --- | --- |
| [LeadQualificationController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification-api/src/Http/Controllers/LeadQualificationController.php) | `public function index(Request $r, LeadQualificationQuery $q): JsonResponse`<br>`public function store(Request $r, UpsertLead $a): JsonResponse`<br>`public function score(Request $r, QualifiedLead $lead, ScoreLead $a): JsonResponse`<br>`public function event(Request $r, QualifiedLead $lead, RecordQualificationEvent $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-lead-qualification-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-qualification-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/lead-qualification')->group(function (): void {
Route::get('/', [LeadQualificationController::class, 'index']);
Route::post('/', [LeadQualificationController::class, 'store']);
Route::post('{lead}/score', [LeadQualificationController::class, 'score']);
Route::post('{lead}/events', [LeadQualificationController::class, 'event']);
```
<!-- layer-implementation-plan:end -->
