# CRM: Customer Success Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customer-success). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-customer-success-vue-inertia`
**Matching domain module:** `crm-customer-success`
**Application:** CRM
**Source feature:** [Customer Success](../features/customer-success.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/customer-success.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Customer segments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Lifecycle:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Onboarding plans:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Success plans:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Objectives:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Health scores:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Product/usage signals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Risks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Playbooks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Touchpoints:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Renewals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-customer-success-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `customer-segments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `lifecycle`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `onboarding-plans`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `success-plans`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `objectives`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `health-scores`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `product-usage-signals`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `risks`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `playbooks`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `touchpoints`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `renewals`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-customer-success` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-crm-laravel-inertia-vue`](https://github.com/liberusoftware/project-crm-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-crm-customer-success-vue-inertia`](https://github.com/liberusoftware/module-crm-customer-success-vue-inertia) (`@liberusoftware/module-crm-customer-success-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/customer-success.md) · [Core plan](../core/customer-success.md) · [API plan](../api/customer-success.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Customer segments** | Render `customer segments` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Lifecycle** | Render `lifecycle` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Onboarding plans** | Render `onboarding plans` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Success plans** | Render `success plans` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Objectives** | Render `objectives` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Health scores** | Render `health scores` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Product/usage signals** | Render `product/usage signals` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Risks** | Render `risks` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Playbooks** | Render `playbooks` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Touchpoints** | Render `touchpoints` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Renewals** | Render `renewals` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CustomerSuccessQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Queries/CustomerSuccessQuery.php) | `public function customers(int $teamId)`<br>`public function risks(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [OpenSuccessRisk.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Actions/OpenSuccessRisk.php) | `public function __construct(private readonly CustomerSuccessPolicy $policy)`<br>`public function execute(int $teamId, int $userId, SuccessCustomer $customer, array $input): SuccessRisk` |
| [PlanRenewal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Actions/PlanRenewal.php) | `public function __construct(private readonly CustomerSuccessPolicy $policy)`<br>`public function execute(int $teamId, int $userId, SuccessCustomer $customer, array $input): SuccessRenewal` |
| [RecordHealthSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Actions/RecordHealthSignal.php) | `public function __construct(private readonly CustomerSuccessPolicy $policy)`<br>`public function execute(int $teamId, int $userId, SuccessCustomer $customer, array $input): SuccessSignal` |
| [UpsertSuccessCustomer.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Actions/UpsertSuccessCustomer.php) | `public function __construct(private readonly CustomerSuccessPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): SuccessCustomer` |
| [CustomerSuccessPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Services/CustomerSuccessPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SuccessCustomer.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Models/SuccessCustomer.php) | No literal fillable array detected; inspect the model and API schema. |
| [SuccessRenewal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Models/SuccessRenewal.php) | No literal fillable array detected; inspect the model and API schema. |
| [SuccessRisk.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Models/SuccessRisk.php) | No literal fillable array detected; inspect the model and API schema. |
| [SuccessSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success/src/Models/SuccessSignal.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CustomerSuccessController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success-api/src/Http/Controllers/CustomerSuccessController.php) | `public function __construct(private readonly CustomerSuccessQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(UpsertSuccessCustomer $action): JsonResponse`<br>`public function signal(SuccessCustomer $customer, RecordHealthSignal $action): JsonResponse`<br>`public function risk(SuccessCustomer $customer, OpenSuccessRisk $action): JsonResponse`<br>`public function renewal(SuccessCustomer $customer, PlanRenewal $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-customer-success-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-success-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/customer-success')->group(function (): void {
Route::get('customers', [CustomerSuccessController::class, 'index']);
Route::post('customers', [CustomerSuccessController::class, 'store']);
Route::post('customers/{customer}/signals', [CustomerSuccessController::class, 'signal']);
Route::post('customers/{customer}/risks', [CustomerSuccessController::class, 'risk']);
Route::post('customers/{customer}/renewals', [CustomerSuccessController::class, 'renewal']);
```
<!-- layer-implementation-plan:end -->
