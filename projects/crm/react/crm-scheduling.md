# CRM: Crm Scheduling React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-scheduling). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-crm-scheduling-react-inertia`
**Matching domain module:** `crm-scheduling`
**Application:** CRM
**Source feature:** [Crm Scheduling](../features/crm-scheduling.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-scheduling.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Personal/team/round-robin links:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Availability:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Buffers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Minimum notice:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Questions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reminders:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reschedule/cancel:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **No-show:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Routing:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Calendar adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-crm-scheduling-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `personal-team-round-robin-links`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `availability`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `buffers`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `minimum-notice`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `questions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `reminders`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `reschedule-cancel`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `no-show`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `routing`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `calendar-adapters`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-scheduling` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-crm-scheduling-react-inertia`](https://github.com/liberusoftware/module-crm-scheduling-react-inertia) (`@liberusoftware/module-crm-scheduling-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/crm-scheduling.md) · [Core plan](../core/crm-scheduling.md) · [API plan](../api/crm-scheduling.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Personal/team/round-robin links** | Render `personal/team/round-robin links` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Availability** | Render `availability` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Buffers** | Render `buffers` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Minimum notice** | Render `minimum notice` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Questions** | Render `questions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Reminders** | Render `reminders` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Reschedule/cancel** | Render `reschedule/cancel` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **No-show** | Render `no-show` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Routing** | Render `routing` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Calendar adapters** | Render `calendar adapters` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SchedulingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Queries/SchedulingQuery.php) | `public function links(int $teamId)`<br>`public function bookings(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ChangeBookingStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Actions/ChangeBookingStatus.php) | `public function execute(int $teamId, int $actorId, int $bookingId, string $status, array $data = []): Booking` |
| [CreateBooking.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Actions/CreateBooking.php) | `public function execute(int $teamId, int $actorId, array $data): Booking` |
| [CreateSchedulingLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Actions/CreateSchedulingLink.php) | `public function execute(int $teamId, int $actorId, array $data): SchedulingLink` |
| [SchedulingAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Services/SchedulingAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): Audit` |
| [SchedulingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Services/SchedulingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Booking.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Models/Booking.php) | No literal fillable array detected; inspect the model and API schema. |
| [SchedulingAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Models/SchedulingAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [SchedulingLink.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling/src/Models/SchedulingLink.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [SchedulingController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling-api/src/Http/Controllers/SchedulingController.php) | `public function links(Request $r, SchedulingQuery $q)`<br>`public function storeLink(Request $r, CreateSchedulingLink $a)`<br>`public function bookings(Request $r, SchedulingQuery $q)`<br>`public function storeBooking(Request $r, CreateBooking $a)`<br>`public function status(Request $r, int $booking, string $status, ChangeBookingStatus $a)` |

**Observed route declarations:**

[modules/crm-scheduling-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-scheduling-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/scheduling')->group(function (): void {
Route::get('/links', [SchedulingController::class, 'links']);
Route::post('/links', [SchedulingController::class, 'storeLink']);
Route::get('/bookings', [SchedulingController::class, 'bookings']);
Route::post('/bookings', [SchedulingController::class, 'storeBooking']);
Route::post('/bookings/{booking}/{status}', [SchedulingController::class, 'status'])->whereIn('status', ['confirmed', 'rescheduled', 'cancelled', 'no_show']);
```
<!-- layer-implementation-plan:end -->
