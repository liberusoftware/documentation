# CRM: Email Marketing Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#email-marketing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-email-marketing-vue-inertia`
**Matching domain module:** `crm-email-marketing`
**Application:** CRM
**Source feature:** [Email Marketing](../features/email-marketing.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/email-marketing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Drag-and-drop and code templates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Personalization:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Dynamic content:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Test sends:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Inbox previews:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Deliverability controls:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Scheduling:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Throttling:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Analytics:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-email-marketing-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `drag-and-drop-and-code-templates`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `personalization`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `dynamic-content`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `test-sends`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `inbox-previews`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `deliverability-controls`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `scheduling`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `throttling`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `analytics`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-email-marketing` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-email-marketing-vue-inertia`](https://github.com/liberusoftware/module-crm-email-marketing-vue-inertia) (`@liberusoftware/module-crm-email-marketing-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/email-marketing.md) · [Core plan](../core/email-marketing.md) · [API plan](../api/email-marketing.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Drag-and-drop and code templates** | Render `drag-and-drop and code templates` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Personalization** | Render `personalization` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Dynamic content** | Render `dynamic content` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Test sends** | Render `test sends` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Inbox previews** | Render `inbox previews` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Deliverability controls** | Render `deliverability controls` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Scheduling** | Render `scheduling` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Throttling** | Render `throttling` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Analytics** | Render `analytics` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EmailMarketingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Queries/EmailMarketingQuery.php) | `public function campaigns(int $teamId)`<br>`public function analytics(int $teamId, int $campaignId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateEmailCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/CreateEmailCampaign.php) | `public function __construct(private readonly EmailMarketingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailCampaign` |
| [RecordMarketingEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/RecordMarketingEvent.php) | `public function execute(int $teamId, EmailCampaign $campaign, array $input): EmailMarketingEvent` |
| [ScheduleCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Actions/ScheduleCampaign.php) | `public function __construct(private readonly EmailMarketingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, EmailCampaign $campaign, array $input): EmailCampaign` |
| [EmailMarketingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Services/EmailMarketingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EmailCampaign.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailCampaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailDelivery.php) | No literal fillable array detected; inspect the model and API schema. |
| [EmailMarketingEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing/src/Models/EmailMarketingEvent.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [EmailMarketingController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing-api/src/Http/Controllers/EmailMarketingController.php) | `public function __construct(private readonly EmailMarketingQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateEmailCampaign $action): JsonResponse`<br>`public function schedule(EmailCampaign $campaign, ScheduleCampaign $action): JsonResponse`<br>`public function event(EmailCampaign $campaign, RecordMarketingEvent $action): JsonResponse`<br>`public function analytics(EmailCampaign $campaign): JsonResponse` |

**Observed route declarations:**

[modules/crm-email-marketing-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-marketing-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/email-marketing')->group(function (): void {
Route::get('campaigns', [EmailMarketingController::class, 'index']);
Route::post('campaigns', [EmailMarketingController::class, 'store']);
Route::post('campaigns/{campaign}/schedule', [EmailMarketingController::class, 'schedule']);
Route::post('campaigns/{campaign}/events', [EmailMarketingController::class, 'event']);
Route::get('campaigns/{campaign}/analytics', [EmailMarketingController::class, 'analytics']);
```
<!-- layer-implementation-plan:end -->
