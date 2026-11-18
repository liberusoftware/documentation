# CRM: Crm Orders And Payments Workspace Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-orders-and-payments-workspace). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-orders-and-payments-workspace-nuxt`
**Matching domain module:** `crm-orders-and-payments-workspace`
**Application:** CRM
**Source feature:** [Crm Orders And Payments Workspace](../features/crm-orders-and-payments-workspace.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-orders-and-payments-workspace.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-orders-and-payments-workspace` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Payment links:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deposits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Order/subscription references:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Invoice/payment status:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Refunds/disputes visibility:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Billing/Ecommerce handoff:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-orders-and-payments-workspace-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `payment-links`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deposits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `order-subscription-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `invoice-payment-status`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `refunds-disputes-visibility`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `billing-ecommerce-handoff`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-orders-and-payments-workspace` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-orders-and-payments-workspace.md)) |
| Capability Nuxt module skeleton | [`module-crm-orders-and-payments-workspace-nuxt`](https://github.com/liberusoftware/module-crm-orders-and-payments-workspace-nuxt) (`@liberusoftware/module-crm-orders-and-payments-workspace-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Payment links** | Expose composable and Vue 3 component for `payment links` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-orders-and-payments-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Deposits** | Expose composable and Vue 3 component for `deposits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-orders-and-payments-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Order/subscription references** | Expose composable and Vue 3 component for `order/subscription references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-orders-and-payments-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Invoice/payment status** | Expose composable and Vue 3 component for `invoice/payment status` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-orders-and-payments-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Refunds/disputes visibility** | Expose composable and Vue 3 component for `refunds/disputes visibility` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-orders-and-payments-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Billing/Ecommerce handoff** | Expose composable and Vue 3 component for `billing/ecommerce handoff` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-orders-and-payments-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TransactionQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Queries/TransactionQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateTransaction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Actions/CreateTransaction.php) | `public function __construct(private readonly OrdersPaymentsPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PaymentTransaction` |
| [RecordPaymentEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Actions/RecordPaymentEvent.php) | `public function __construct(private readonly OrdersPaymentsPolicy $policy)`<br>`public function execute(int $teamId, int $userId, PaymentTransaction $transaction, array $input): PaymentEvent` |
| [OrdersPaymentsPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Services/OrdersPaymentsPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PaymentEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Models/PaymentEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentTransaction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Models/PaymentTransaction.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [OrdersPaymentsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace-api/src/Http/Controllers/OrdersPaymentsController.php) | `public function index(Request $request, TransactionQuery $query): JsonResponse`<br>`public function store(Request $request, CreateTransaction $action): JsonResponse`<br>`public function event(Request $request, PaymentTransaction $transaction, RecordPaymentEvent $action): JsonResponse` |
<!-- layer-implementation-plan:end -->
