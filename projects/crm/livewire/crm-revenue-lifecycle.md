# CRM: Crm Revenue Lifecycle Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-revenue-lifecycle). Observed identity: [`liberusoftware/module-crm-revenue-lifecycle-livewire`](../../../modules/source/liberusoftware--module-crm-revenue-lifecycle-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-revenue-lifecycle-livewire`  
**Matching domain module:** `crm-revenue-lifecycle`  
**Application:** CRM  
**Source feature:** [Crm Revenue Lifecycle](../features/crm-revenue-lifecycle.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Opportunity-to-order orchestration:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Assets/installed products:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Entitlements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Renewals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Upgrades:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Downgrades:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cancellation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Usage signals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Fallout queues:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-revenue-lifecycle-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmRevenueLifecycle::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `opportunity-to-order-orchestration`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `assets-installed-products`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `entitlements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `renewals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `upgrades`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `downgrades`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cancellation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `usage-signals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `fallout-queues`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-revenue-lifecycle` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-revenue-lifecycle.md) · [API plan](../api/crm-revenue-lifecycle.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Opportunity-to-order orchestration** | Expose a focused Livewire 4 component and namespaced Blade default view for `opportunity-to-order orchestration` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Assets/installed products** | Expose a focused Livewire 4 component and namespaced Blade default view for `assets/installed products` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Entitlements** | Expose a focused Livewire 4 component and namespaced Blade default view for `entitlements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Renewals** | Expose a focused Livewire 4 component and namespaced Blade default view for `renewals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Upgrades** | Expose a focused Livewire 4 component and namespaced Blade default view for `upgrades` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Downgrades** | Expose a focused Livewire 4 component and namespaced Blade default view for `downgrades` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cancellation** | Expose a focused Livewire 4 component and namespaced Blade default view for `cancellation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Usage signals** | Expose a focused Livewire 4 component and namespaced Blade default view for `usage signals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Fallout queues** | Expose a focused Livewire 4 component and namespaced Blade default view for `fallout queues` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [RevenueLifecycleDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle-livewire/src/Components/RevenueLifecycleDashboard.php) · [RevenueLifecycleLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle-livewire/src/RevenueLifecycleLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [RevenueQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Queries/RevenueQuery.php) | `public function assets(int $teamId)`<br>`public function orders(int $teamId)`<br>`public function fallout(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateOrder.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/CreateOrder.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueOrder` |
| [ManageAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/ManageAsset.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueAsset` |
| [RecordUsageSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/RecordUsageSignal.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $assetId, array $input): RevenueAsset` |
| [ResolveFallout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/ResolveFallout.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $falloutId, array $input): RevenueFallout` |
| [RevenuePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Services/RevenuePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RevenueAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueAsset.php) | No literal fillable array detected; inspect the model and API schema. |
| [RevenueFallout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueFallout.php) | No literal fillable array detected; inspect the model and API schema. |
| [RevenueOrder.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueOrder.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
