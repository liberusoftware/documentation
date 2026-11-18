# Control Panel: Control Panel Api And Automation React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-api-and-automation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-control-panel-control-panel-api-and-automation-react-inertia`
**Matching domain module:** `control-panel-api-and-automation`
**Application:** Control Panel
**Source feature:** [Control Panel Api And Automation](../features/control-panel-api-and-automation.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/control-panel-api-and-automation.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Scoped API:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Webhooks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **CLI:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Templates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Schedules:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Orchestration:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Billing/provisioning events:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-control-panel-control-panel-api-and-automation-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `scoped-api`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `webhooks`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `cli`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `templates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `schedules`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `orchestration`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `billing-provisioning-events`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `control-panel-api-and-automation` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-control-panel-laravel-inertia-react`](https://github.com/liberusoftware/project-control-panel-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-control-panel-api-and-automation-react-inertia`](https://github.com/liberusoftware/module-control-panel-api-and-automation-react-inertia) (`@liberusoftware/module-control-panel-api-and-automation-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/control-panel-api-and-automation.md) · [Core plan](../core/control-panel-api-and-automation.md) · [API plan](../api/control-panel-api-and-automation.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Scoped API** | Render `scoped api` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Webhooks** | Render `webhooks` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **CLI** | Render `cli` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Templates** | Render `templates` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Schedules** | Render `schedules` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Orchestration** | Render `orchestration` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Billing/provisioning events** | Render `billing/provisioning events` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListAutomations.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Queries/ListAutomations.php) | `public function execute(int\|string\|null $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |
| [ListWebhooks.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Queries/ListWebhooks.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAutomationSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/CreateAutomationSchedule.php) | `public function execute(array $attributes): AutomationSchedule` |
| [CreateAutomationTemplate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/CreateAutomationTemplate.php) | `public function execute(array $attributes): AutomationTemplate` |
| [PauseWebhook.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/PauseWebhook.php) | `public function execute(WebhookEndpoint $webhook): WebhookEndpoint` |
| [RecordBillingProvisioningEvent.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RecordBillingProvisioningEvent.php) | `public function execute(array $attributes): BillingProvisioningEvent` |
| [RegisterApiCredential.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RegisterApiCredential.php) | `public function execute(array $attributes): ApiCredential` |
| [RegisterAutomation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RegisterAutomation.php) | `public function execute(array $attributes): AutomationDefinition` |
| [RegisterAutomationCommand.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RegisterAutomationCommand.php) | `public function execute(array $attributes): AutomationCommand` |
| [RegisterWebhook.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RegisterWebhook.php) | `public function execute(array $attributes): WebhookEndpoint` |
| [ResumeWebhook.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/ResumeWebhook.php) | `public function execute(WebhookEndpoint $webhook): WebhookEndpoint` |
| [RevokeApiCredential.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Actions/RevokeApiCredential.php) | `public function execute(ApiCredential $credential): ApiCredential` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ApiCredential.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/ApiCredential.php) | `team_id`, `name`, `scopes`, `secret`, `status`, `expires_at`, `last_used_at` |
| [AutomationCommand.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/AutomationCommand.php) | `team_id`, `name`, `description`, `command`, `arguments`, `enabled`, `last_run_at` |
| [AutomationDefinition.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/AutomationDefinition.php) | `team_id`, `name`, `kind`, `status`, `schedule`, `definition`, `credentials` |
| [AutomationSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/AutomationSchedule.php) | `team_id`, `name`, `cron`, `timezone`, `template_id`, `status`, `next_run_at`, `last_run_at` |
| [AutomationTemplate.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/AutomationTemplate.php) | `team_id`, `name`, `version`, `description`, `inputs`, `steps`, `active` |
| [BillingProvisioningEvent.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/BillingProvisioningEvent.php) | `team_id`, `external_id`, `event_type`, `payload`, `status`, `processed_at`, `error` |
| [OrchestrationRun.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/OrchestrationRun.php) | `team_id`, `template_id`, `schedule_id`, `status`, `input`, `output`, `error`, `started_at`, `finished_at`, `idempotency_key` |
| [WebhookEndpoint.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation/src/Models/WebhookEndpoint.php) | `team_id`, `name`, `url`, `events`, `secret`, `status`, `retry_limit`, `last_delivered_at`, `failure_count` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AutomationController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-api/src/Http/Controllers/AutomationController.php) | `public function index(Request $request, ListAutomations $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, RegisterAutomation $register): JsonResponse`<br>`public function credential(Request $request, RegisterApiCredential $register): JsonResponse`<br>`public function webhook(Request $request, RegisterWebhook $register): JsonResponse`<br>`public function revokeCredential(Request $request, string $credential, RevokeApiCredential $revoke): JsonResponse`<br>`public function updateCredential(Request $request, string $credential, UpdateApiCredential $update): JsonResponse`<br>`public function updateWebhook(Request $request, string $webhook, UpdateWebhook $update): JsonResponse`<br>`public function pauseWebhook(Request $request, string $webhook, PauseWebhook $pause): JsonResponse`<br>`public function resumeWebhook(Request $request, string $webhook, ResumeWebhook $resume): JsonResponse`<br>`public function run(Request $request, string $template, StartOrchestration $start): JsonResponse`<br>`public function template(Request $request, CreateAutomationTemplate $create): JsonResponse`<br>`public function schedule(Request $request, CreateAutomationSchedule $create): JsonResponse`<br>`public function command(Request $request, RegisterAutomationCommand $register): JsonResponse`<br>`public function billingEvent(Request $request, RecordBillingProvisioningEvent $record): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-api-and-automation-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-api-and-automation-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/api-and-automation')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [AutomationController::class, 'index'])->name('control-panel.api-and-automation.index');
Route::post('/', [AutomationController::class, 'store'])->name('control-panel.api-and-automation.store');
Route::post('credentials', [AutomationController::class, 'credential'])->name('control-panel.api-and-automation.credentials.store');
Route::patch('credentials/{credential}', [AutomationController::class, 'updateCredential'])->name('control-panel.api-and-automation.credentials.update');
Route::post('credentials/{credential}/revoke', [AutomationController::class, 'revokeCredential'])->name('control-panel.api-and-automation.credentials.revoke');
Route::post('webhooks', [AutomationController::class, 'webhook'])->name('control-panel.api-and-automation.webhooks.store');
Route::patch('webhooks/{webhook}', [AutomationController::class, 'updateWebhook'])->name('control-panel.api-and-automation.webhooks.update');
Route::post('webhooks/{webhook}/pause', [AutomationController::class, 'pauseWebhook'])->name('control-panel.api-and-automation.webhooks.pause');
Route::post('webhooks/{webhook}/resume', [AutomationController::class, 'resumeWebhook'])->name('control-panel.api-and-automation.webhooks.resume');
Route::post('templates/{template}/runs', [AutomationController::class, 'run'])->name('control-panel.api-and-automation.runs.store');
Route::post('templates', [AutomationController::class, 'template'])->name('control-panel.api-and-automation.templates.store');
Route::post('schedules', [AutomationController::class, 'schedule'])->name('control-panel.api-and-automation.schedules.store');
Route::post('commands', [AutomationController::class, 'command'])->name('control-panel.api-and-automation.commands.store');
Route::post('billing-events', [AutomationController::class, 'billingEvent'])->name('control-panel.api-and-automation.billing-events.store');
Route::get('{automation}', [AutomationController::class, 'show'])->name('control-panel.api-and-automation.show');
```
<!-- layer-implementation-plan:end -->
