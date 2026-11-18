# CRM: Crm Sla And Entitlements Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-sla-and-entitlements). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-crm-sla-and-entitlements-vue-inertia`
**Matching domain module:** `crm-sla-and-entitlements`
**Application:** CRM
**Source feature:** [Crm Sla And Entitlements](../features/crm-sla-and-entitlements.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-sla-and-entitlements.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Service contracts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Coverage:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Business calendars:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Response/resolution targets:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Milestones:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Pauses:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Warnings:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Breaches:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Escalations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Exceptions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-crm-sla-and-entitlements-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `service-contracts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `coverage`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `business-calendars`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `response-resolution-targets`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `milestones`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `pauses`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `warnings`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `breaches`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `escalations`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `exceptions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-sla-and-entitlements` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-sla-and-entitlements-vue-inertia`](https://github.com/liberusoftware/module-crm-sla-and-entitlements-vue-inertia) (`@liberusoftware/module-crm-sla-and-entitlements-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/crm-sla-and-entitlements.md) · [Core plan](../core/crm-sla-and-entitlements.md) · [API plan](../api/crm-sla-and-entitlements.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Service contracts** | Render `service contracts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Coverage** | Render `coverage` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Business calendars** | Render `business calendars` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Response/resolution targets** | Render `response/resolution targets` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Milestones** | Render `milestones` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Pauses** | Render `pauses` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Warnings** | Render `warnings` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Breaches** | Render `breaches` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Escalations** | Render `escalations` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Exceptions** | Render `exceptions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SlaQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Queries/SlaQuery.php) | `public function contracts(int $teamId)`<br>`public function calendars(int $teamId)`<br>`public function entitlements(int $teamId)`<br>`public function cases(int $teamId)`<br>`public function escalations(int $teamId)`<br>`public function exceptions(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCalendar.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/CreateCalendar.php) | `public function execute(int $teamId, int $actorId, array $data): SlaCalendar` |
| [CreateContract.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/CreateContract.php) | `public function execute(int $teamId, int $actorId, array $data): SlaContract` |
| [EvaluateCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/EvaluateCase.php) | `public function execute(int $teamId, int $actorId, int $caseId): array` |
| [OpenCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/OpenCase.php) | `public function execute(int $teamId, int $actorId, array $data): SlaCase` |
| [RequestException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/RequestException.php) | `public function execute(int $teamId, int $actorId, array $data): SlaException` |
| [SetEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/SetEntitlement.php) | `public function execute(int $teamId, int $actorId, array $data): SlaEntitlement` |
| [TransitionCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/TransitionCase.php) | `public function execute(int $teamId, int $actorId, int $caseId, string $transition, array $data = []): SlaCase` |
| [SlaAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Services/SlaAudit.php) | `public function record(int $teamId, ?int $actorId, int $caseId, string $type, array $payload = []): SlaCaseEvent` |
| [SlaPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Services/SlaPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SlaCalendar.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaCalendar.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaCase.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaCaseEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaCaseEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaContract.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaContract.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaEntitlement.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaEscalation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaEscalation.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaException.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [SlaController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements-api/src/Http/Controllers/SlaController.php) | `public function contracts(Request $r, SlaQuery $q): JsonResponse`<br>`public function calendars(Request $r, SlaQuery $q): JsonResponse`<br>`public function entitlements(Request $r, SlaQuery $q): JsonResponse`<br>`public function cases(Request $r, SlaQuery $q): JsonResponse`<br>`public function storeContract(Request $r, CreateContract $a): JsonResponse`<br>`public function storeCalendar(Request $r, CreateCalendar $a): JsonResponse`<br>`public function storeEntitlement(Request $r, SetEntitlement $a): JsonResponse`<br>`public function storeCase(Request $r, OpenCase $a): JsonResponse`<br>`public function transition(Request $r, int $case, string $transition, TransitionCase $a): JsonResponse`<br>`public function evaluate(Request $r, int $case, EvaluateCase $a): JsonResponse`<br>`public function exception(Request $r, RequestException $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-sla-and-entitlements-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/sla-and-entitlements')->group(function (): void {
Route::get('/contracts', [SlaController::class, 'contracts']);
Route::post('/contracts', [SlaController::class, 'storeContract']);
Route::get('/calendars', [SlaController::class, 'calendars']);
Route::post('/calendars', [SlaController::class, 'storeCalendar']);
Route::get('/entitlements', [SlaController::class, 'entitlements']);
Route::post('/entitlements', [SlaController::class, 'storeEntitlement']);
Route::get('/cases', [SlaController::class, 'cases']);
Route::post('/cases', [SlaController::class, 'storeCase']);
Route::post('/cases/{case}/{transition}', [SlaController::class, 'transition'])->whereIn('transition', ['responded', 'pause', 'resume', 'resolve', 'close']);
Route::post('/cases/{case}/evaluate', [SlaController::class, 'evaluate']);
Route::post('/exceptions', [SlaController::class, 'exception']);
```
<!-- layer-implementation-plan:end -->
