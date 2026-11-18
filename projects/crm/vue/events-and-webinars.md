# CRM: Events and Webinars Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#events-and-webinars). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-events-and-webinars-vue-inertia`
**Matching domain module:** `crm-events-and-webinars`
**Application:** CRM
**Source feature:** [Events and Webinars](../features/events-and-webinars.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/events-and-webinars.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Physical/virtual events:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Registration:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Capacity:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tickets/attendance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Sessions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Speakers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reminders:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Check-in:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Recording links:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Follow-up:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Provider adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-events-and-webinars-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `physical-virtual-events`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `registration`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `capacity`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `tickets-attendance`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `sessions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `speakers`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `reminders`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `check-in`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `recording-links`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `follow-up`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `provider-adapters`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-events-and-webinars` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-events-and-webinars-vue-inertia`](https://github.com/liberusoftware/module-crm-events-and-webinars-vue-inertia) (`@liberusoftware/module-crm-events-and-webinars-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/events-and-webinars.md) · [Core plan](../core/events-and-webinars.md) · [API plan](../api/events-and-webinars.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Physical/virtual events** | Render `physical/virtual events` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Registration** | Render `registration` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Capacity** | Render `capacity` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Tickets/attendance** | Render `tickets/attendance` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Sessions** | Render `sessions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Speakers** | Render `speakers` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Reminders** | Render `reminders` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Check-in** | Render `check-in` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Recording links** | Render `recording links` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Follow-up** | Render `follow-up` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Provider adapters** | Render `provider adapters` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EventQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Queries/EventQuery.php) | `public function events(int $teamId)`<br>`public function sessions(int $teamId, int $eventId)`<br>`public function attendance(int $teamId, int $eventId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CheckInAttendee.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Actions/CheckInAttendee.php) | `public function execute(int $teamId, EventRegistration $registration): EventRegistration` |
| [CreateEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Actions/CreateEvent.php) | `public function __construct(private readonly EventPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CrmEvent` |
| [RecordEventFollowUp.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Actions/RecordEventFollowUp.php) | `public function __construct(private readonly EventPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CrmEvent $event, array $input): EventFollowUp` |
| [RegisterAttendee.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Actions/RegisterAttendee.php) | `public function execute(int $teamId, CrmEvent $event, array $input): EventRegistration` |
| [EventPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Services/EventPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CrmEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Models/CrmEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [EventFollowUp.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Models/EventFollowUp.php) | No literal fillable array detected; inspect the model and API schema. |
| [EventRegistration.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Models/EventRegistration.php) | No literal fillable array detected; inspect the model and API schema. |
| [EventSession.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars/src/Models/EventSession.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [EventsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars-api/src/Http/Controllers/EventsController.php) | `public function __construct(private readonly EventQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateEvent $action): JsonResponse`<br>`public function register(CrmEvent $event, RegisterAttendee $action): JsonResponse`<br>`public function checkIn(EventRegistration $registration, CheckInAttendee $action): JsonResponse`<br>`public function attendance(CrmEvent $event): JsonResponse`<br>`public function followUp(CrmEvent $event, RecordEventFollowUp $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-events-and-webinars-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-events-and-webinars-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/events-and-webinars')->group(function (): void {
Route::get('/', [EventsController::class, 'index']);
Route::post('/', [EventsController::class, 'store']);
Route::post('{event}/registrations', [EventsController::class, 'register']);
Route::post('registrations/{registration}/check-in', [EventsController::class, 'checkIn']);
Route::get('{event}/attendance', [EventsController::class, 'attendance']);
Route::post('{event}/follow-ups', [EventsController::class, 'followUp']);
```
<!-- layer-implementation-plan:end -->
