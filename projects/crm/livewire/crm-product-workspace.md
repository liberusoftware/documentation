# CRM: CRM Product Workspace Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-product-workspace). Observed identity: [`liberusoftware/module-crm-product-workspace-livewire`](../../../modules/source/liberusoftware--module-crm-product-workspace-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-product-workspace-livewire`  
**Matching domain module:** `crm-product-workspace`  
**Application:** CRM  
**Source feature:** [CRM Product Workspace](../features/crm-product-workspace.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Sales-facing catalog projections:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Bundles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Entitlements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Price-book references:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Product eligibility:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Governed Billing/Ecommerce synchronization:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-product-workspace-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-product-workspace::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `sales-facing-catalog-projections`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `bundles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `entitlements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `price-book-references`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `product-eligibility`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `governed-billing-ecommerce-synchronization`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-product-workspace` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-product-workspace.md) · [API plan](../api/crm-product-workspace.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Sales-facing catalog projections** | Expose a focused Livewire 4 component and namespaced Blade default view for `sales-facing catalog projections` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Bundles** | Expose a focused Livewire 4 component and namespaced Blade default view for `bundles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Entitlements** | Expose a focused Livewire 4 component and namespaced Blade default view for `entitlements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Price-book references** | Expose a focused Livewire 4 component and namespaced Blade default view for `price-book references` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Product eligibility** | Expose a focused Livewire 4 component and namespaced Blade default view for `product eligibility` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Governed Billing/Ecommerce synchronization** | Expose a focused Livewire 4 component and namespaced Blade default view for `governed billing/ecommerce synchronization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ProductDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace-livewire/src/Livewire/ProductDashboard.php) · [ProductWorkspaceLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace-livewire/src/ProductWorkspaceLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ProductWorkspaceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Queries/ProductWorkspaceQuery.php) | `public function products(int $teamId)`<br>`public function entitlements(int $teamId, int $customerId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GrantEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Actions/GrantEntitlement.php) | `public function __construct(private readonly ProductWorkspacePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProductEntitlement` |
| [RecordProductSync.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Actions/RecordProductSync.php) | `public function __construct(private readonly ProductWorkspacePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProductSync` |
| [UpsertWorkspaceProduct.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Actions/UpsertWorkspaceProduct.php) | `public function __construct(private readonly ProductWorkspacePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): WorkspaceProduct` |
| [ProductWorkspacePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Services/ProductWorkspacePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProductBundle.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/ProductBundle.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProductEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/ProductEntitlement.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProductSync.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/ProductSync.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkspaceProduct.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/WorkspaceProduct.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
