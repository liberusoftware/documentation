# CRM: Crm Events And Webinars Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-events-and-webinars). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-events-and-webinars-nuxt`
**Matching domain module:** `crm-events-and-webinars`
**Application:** CRM
**Source feature:** [Crm Events And Webinars](../features/crm-events-and-webinars.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-events-and-webinars.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-events-and-webinars` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Physical/virtual events:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Registration:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Capacity:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tickets/attendance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sessions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Speakers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reminders:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Check-in:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Recording links:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Follow-up:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provider adapters:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-events-and-webinars-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `physical-virtual-events`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `registration`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `capacity`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tickets-attendance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sessions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `speakers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reminders`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `check-in`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `recording-links`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `follow-up`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provider-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-events-and-webinars` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-events-and-webinars.md)) |
| Capability Nuxt module skeleton | [`module-crm-events-and-webinars-nuxt`](https://github.com/liberusoftware/module-crm-events-and-webinars-nuxt) (`@liberusoftware/module-crm-events-and-webinars-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Physical/virtual events** | Expose composable and Vue 3 component for `physical/virtual events` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-events-and-webinars.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Registration** | Expose composable and Vue 3 component for `registration` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-events-and-webinars.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Capacity** | Expose composable and Vue 3 component for `capacity` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-events-and-webinars.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Tickets/attendance** | Expose composable and Vue 3 component for `tickets/attendance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-events-and-webinars.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Sessions** | Expose composable and Vue 3 component for `sessions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-events-and-webinars.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Speakers** | Expose composable and Vue 3 component for `speakers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-events-and-webinars.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Reminders** | Expose composable and Vue 3 component for `reminders` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-events-and-webinars.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Check-in** | Expose composable and Vue 3 component for `check-in` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-events-and-webinars.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Recording links** | Expose composable and Vue 3 component for `recording links` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-events-and-webinars.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Follow-up** | Expose composable and Vue 3 component for `follow-up` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-events-and-webinars.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Provider adapters** | Expose composable and Vue 3 component for `provider adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-events-and-webinars.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

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
