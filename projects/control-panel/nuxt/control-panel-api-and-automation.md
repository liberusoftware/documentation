# Control Panel: Control Panel Api And Automation Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-api-and-automation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-control-panel-control-panel-api-and-automation-nuxt`
**Matching domain module:** `control-panel-api-and-automation`
**Application:** Control Panel
**Source feature:** [Control Panel Api And Automation](../features/control-panel-api-and-automation.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/control-panel-api-and-automation.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `control-panel-api-and-automation` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Scoped API:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Webhooks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **CLI:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Schedules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Orchestration:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Billing/provisioning events:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-control-panel-control-panel-api-and-automation-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `scoped-api`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `webhooks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cli`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `schedules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `orchestration`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `billing-provisioning-events`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `control-panel-api-and-automation` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-control-panel-nuxt-vue`](https://github.com/liberusoftware/project-control-panel-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/control-panel-api-and-automation.md)) |
| Capability Nuxt module skeleton | [`module-control-panel-api-and-automation-nuxt`](https://github.com/liberusoftware/module-control-panel-api-and-automation-nuxt) (`@liberusoftware/module-control-panel-api-and-automation-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Scoped API** | Expose composable and Vue 3 component for `scoped api` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-api-and-automation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Webhooks** | Expose composable and Vue 3 component for `webhooks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-api-and-automation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **CLI** | Expose composable and Vue 3 component for `cli` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-api-and-automation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Templates** | Expose composable and Vue 3 component for `templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-api-and-automation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Schedules** | Expose composable and Vue 3 component for `schedules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-api-and-automation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Orchestration** | Expose composable and Vue 3 component for `orchestration` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-api-and-automation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Billing/provisioning events** | Expose composable and Vue 3 component for `billing/provisioning events` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/control-panel-api-and-automation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |

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
