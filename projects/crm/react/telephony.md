# CRM: Telephony React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#telephony). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-telephony-react-inertia`
**Matching domain module:** `crm-telephony`
**Application:** CRM
**Source feature:** [Telephony](../features/telephony.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/telephony.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Numbers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Caller ID:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **IVR:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Queues:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Business hours:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Skills:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Recording:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Voicemail:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Transfers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Dispositions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Click-to-call:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Call logging:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Provider adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-telephony-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `numbers`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `caller-id`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `ivr`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `queues`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `business-hours`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `skills`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `recording`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `voicemail`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `transfers`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `dispositions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `click-to-call`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `call-logging`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `provider-adapters`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-telephony` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-crm-telephony-react-inertia`](https://github.com/liberusoftware/module-crm-telephony-react-inertia) (`@liberusoftware/module-crm-telephony-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/telephony.md) · [Core plan](../core/telephony.md) · [API plan](../api/telephony.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Numbers** | Render `numbers` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Caller ID** | Render `caller id` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **IVR** | Render `ivr` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Queues** | Render `queues` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Business hours** | Render `business hours` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Skills** | Render `skills` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Recording** | Render `recording` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Voicemail** | Render `voicemail` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Transfers** | Render `transfers` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Dispositions** | Render `dispositions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Click-to-call** | Render `click-to-call` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Call logging** | Render `call logging` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Provider adapters** | Render `provider adapters` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TelephonyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Queries/TelephonyQuery.php) | `public function numbers(int $teamId)`<br>`public function queues(int $teamId)`<br>`public function calls(int $teamId)`<br>`public function settings(int $teamId): ?TelephonySettings` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureTelephony.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/ConfigureTelephony.php) | `public function execute(int $teamId, int $actorId, array $data): TelephonySettings` |
| [CreateTelephonyQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/CreateTelephonyQueue.php) | `public function execute(int $teamId, int $actorId, array $data): TelephonyQueue` |
| [LogTelephonyCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/LogTelephonyCall.php) | `public function execute(int $teamId, int $actorId, array $data): TelephonyCall` |
| [UpdateCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/UpdateCall.php) | `public function execute(int $teamId, int $actorId, int $callId, array $data): TelephonyCall` |
| [UpsertTelephonyNumber.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Actions/UpsertTelephonyNumber.php) | `public function execute(int $teamId, int $actorId, array $data, ?int $id = null): TelephonyNumber` |
| [TelephonyAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Services/TelephonyAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): Audit` |
| [TelephonyPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Services/TelephonyPolicy.php) | `public function canManage(int $teamId, int $userId): bool`<br>`public function isTeamMember(int $teamId, int $userId, array $roles = [], bool $includeOwner = false): bool` |
| [TenantTwilioService.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Services/TenantTwilioService.php) | `public function client(int $teamId): Client`<br>`public function sendMessage(int $teamId, string $to, string $body): object`<br>`public function usage(int $teamId, array $filters = []): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TelephonyAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonyCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyCall.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonyNumber.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyNumber.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonyQueue.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonyQueue.php) | No literal fillable array detected; inspect the model and API schema. |
| [TelephonySettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony/src/Models/TelephonySettings.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [TelephonyController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-api/src/Http/Controllers/TelephonyController.php) | `public function numbers(Request $r, TelephonyQuery $q): JsonResponse`<br>`public function queues(Request $r, TelephonyQuery $q): JsonResponse`<br>`public function settings(Request $r, TelephonyQuery $q): JsonResponse`<br>`public function configure(Request $r, ConfigureTelephony $a): JsonResponse`<br>`public function number(Request $r, UpsertTelephonyNumber $a): JsonResponse`<br>`public function queue(Request $r, CreateTelephonyQueue $a): JsonResponse`<br>`public function calls(Request $r, TelephonyQuery $q): JsonResponse`<br>`public function logCall(Request $r, LogTelephonyCall $a): JsonResponse`<br>`public function updateCall(Request $r, int $call, UpdateCall $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-telephony-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-telephony-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/telephony')->group(function (): void {
Route::get('/numbers', [TelephonyController::class, 'numbers']);
Route::post('/numbers', [TelephonyController::class, 'number']);
Route::get('/queues', [TelephonyController::class, 'queues']);
Route::post('/queues', [TelephonyController::class, 'queue']);
Route::get('/settings', [TelephonyController::class, 'settings']);
Route::put('/settings', [TelephonyController::class, 'configure']);
Route::get('/calls', [TelephonyController::class, 'calls']);
Route::post('/calls', [TelephonyController::class, 'logCall']);
Route::patch('/calls/{call}', [TelephonyController::class, 'updateCall']);
```
<!-- layer-implementation-plan:end -->
