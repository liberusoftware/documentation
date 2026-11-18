# CRM: Crm White Label React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-white-label). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-crm-white-label-react-inertia`
**Matching domain module:** `crm-white-label`
**Application:** CRM
**Source feature:** [Crm White Label](../features/crm-white-label.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-white-label.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Brand/domain/email/application settings:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Theme selection:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Custom client experience:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Provider abstraction:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Safe platform attribution policy:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-crm-white-label-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `brand-domain-email-application-settings`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `theme-selection`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `custom-client-experience`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `provider-abstraction`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `safe-platform-attribution-policy`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-white-label` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-crm-laravel-inertia-react`](https://github.com/liberusoftware/project-crm-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-crm-white-label-react-inertia`](https://github.com/liberusoftware/module-crm-white-label-react-inertia) (`@liberusoftware/module-crm-white-label-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/crm-white-label.md) · [Core plan](../core/crm-white-label.md) · [API plan](../api/crm-white-label.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Brand/domain/email/application settings** | Render `brand/domain/email/application settings` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Theme selection** | Render `theme selection` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Custom client experience** | Render `custom client experience` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Provider abstraction** | Render `provider abstraction` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Safe platform attribution policy** | Render `safe platform attribution policy` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [WhiteLabelSettingsQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Queries/WhiteLabelSettingsQuery.php) | `public function forTeam(int $teamId): WhiteLabelSettings` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [UpdateWhiteLabelSettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Actions/UpdateWhiteLabelSettings.php) | `public function execute(int $teamId, int $actorId, array $attributes, ?int $expectedVersion = null): WhiteLabelSettings` |
| [WhiteLabelAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Services/WhiteLabelAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $changes): void` |
| [WhiteLabelPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Services/WhiteLabelPolicy.php) | `public function canManage(int $teamId, int $actorId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WhiteLabelAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Models/WhiteLabelAudit.php) | `team_id`, `actor_id`, `event`, `changes`, `request_id` |
| [WhiteLabelSettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label/src/Models/WhiteLabelSettings.php) | `team_id`, `brand_name`, `custom_domain`, `theme`, `email_settings`, `application_settings`, `client_experience`, `provider`, `show_platform_attribution`, `version` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WhiteLabelController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label-api/src/Http/Controllers/WhiteLabelController.php) | `public function show(Request $request, WhiteLabelSettingsQuery $query): JsonResponse`<br>`public function update(Request $request, UpdateWhiteLabelSettings $update, WhiteLabelSettingsQuery $query, IdempotencyStore $idempotency): JsonResponse` |

**Observed route declarations:**

[modules/crm-white-label-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-white-label-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/white-label')->group(function (): void {
Route::get('/', [WhiteLabelController::class, 'show'])->name('crm.white-label.show');
Route::patch('/', [WhiteLabelController::class, 'update'])->name('crm.white-label.update');
```
<!-- layer-implementation-plan:end -->
