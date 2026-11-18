# Real Estate: Property Management Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#property-management). Observed identity: [`liberusoftware/real-estate-property-management-livewire`](../../../modules/source/liberusoftware--real-estate-property-management-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-real-estate-property-management-livewire`  
**Matching domain module:** `real-estate-property-management`  
**Application:** Real Estate  
**Source feature:** [Property Management](../features/property-management.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Rent schedule:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Statements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Inspections:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Compliance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Maintenance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Contractors:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Owner approvals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-real-estate-property-management-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-real-estate-property-management::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `rent-schedule`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `statements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `inspections`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `compliance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `maintenance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `contractors`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `owner-approvals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `real-estate-property-management` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/property-management.md) · [API plan](../api/property-management.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Rent schedule** | Expose a focused Livewire 4 component and namespaced Blade default view for `rent schedule` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Statements** | Expose a focused Livewire 4 component and namespaced Blade default view for `statements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Inspections** | Expose a focused Livewire 4 component and namespaced Blade default view for `inspections` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Compliance** | Expose a focused Livewire 4 component and namespaced Blade default view for `compliance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Maintenance** | Expose a focused Livewire 4 component and namespaced Blade default view for `maintenance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Contractors** | Expose a focused Livewire 4 component and namespaced Blade default view for `contractors` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Owner approvals** | Expose a focused Livewire 4 component and namespaced Blade default view for `owner approvals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [MaintenanceRequestForm.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-livewire/src/Components/MaintenanceRequestForm.php) · [ManagementRecordList.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-livewire/src/Components/ManagementRecordList.php) · [PropertyManagementLivewireServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-livewire/src/PropertyManagementLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListManagementRecords.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Queries/ListManagementRecords.php) | `public function handle(int\|string $teamId, ?string $capability = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ManagementRecordPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Policies/ManagementRecordPolicy.php) | `public function view($user, ManagementRecord $record): bool`<br>`public function update($user, ManagementRecord $record): bool`<br>`public function delete($user, ManagementRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Inspection.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/Inspection.php) | No literal fillable array detected; inspect the model and API schema. |
| [MaintenanceRequest.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/MaintenanceRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [ManagementRecord.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/ManagementRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [VendorQuote.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/VendorQuote.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkOrder.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/WorkOrder.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkOrderUpdate.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/WorkOrderUpdate.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
