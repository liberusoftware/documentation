# CRM: Customer Self-Service Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customer-self-service). Observed identity: [`liberusoftware/module-crm-customer-self-service-livewire`](../../../modules/source/liberusoftware--module-crm-customer-self-service-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-customer-self-service-livewire`  
**Matching domain module:** `crm-customer-self-service`  
**Application:** CRM  
**Source feature:** [Customer Self-Service](../features/customer-self-service.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Customer portal:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Case submission/status:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Knowledge search:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Community links:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Appointments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Documents:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Invoices/orders references:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Profile:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Preferences:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-customer-self-service-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-customer-self-service::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `customer-portal`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `case-submission-status`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `knowledge-search`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `community-links`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `appointments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `documents`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `invoices-orders-references`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `profile`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `preferences`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-customer-self-service` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/customer-self-service.md) · [API plan](../api/customer-self-service.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Customer portal** | Expose a focused Livewire 4 component and namespaced Blade default view for `customer portal` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Case submission/status** | Expose a focused Livewire 4 component and namespaced Blade default view for `case submission/status` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Knowledge search** | Expose a focused Livewire 4 component and namespaced Blade default view for `knowledge search` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Community links** | Expose a focused Livewire 4 component and namespaced Blade default view for `community links` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Appointments** | Expose a focused Livewire 4 component and namespaced Blade default view for `appointments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Documents** | Expose a focused Livewire 4 component and namespaced Blade default view for `documents` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Invoices/orders references** | Expose a focused Livewire 4 component and namespaced Blade default view for `invoices/orders references` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Profile** | Expose a focused Livewire 4 component and namespaced Blade default view for `profile` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Preferences** | Expose a focused Livewire 4 component and namespaced Blade default view for `preferences` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [SelfServiceDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service-livewire/src/Livewire/SelfServiceDashboard.php) · [CustomerSelfServiceLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service-livewire/src/CustomerSelfServiceLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SelfServiceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Queries/SelfServiceQuery.php) | `public function profile(int $teamId, int $userId): ?SelfServiceProfile`<br>`public function cases(int $teamId, int $profileId)`<br>`public function search(int $teamId, string $term)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SubmitSelfServiceCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Actions/SubmitSelfServiceCase.php) | `public function __construct(private readonly SelfServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, SelfServiceProfile $profile, array $input): SelfServiceCase` |
| [UpdateSelfServicePreferences.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Actions/UpdateSelfServicePreferences.php) | `public function __construct(private readonly SelfServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, SelfServiceProfile $profile, array $input): SelfServiceProfile` |
| [UpsertSelfServiceProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Actions/UpsertSelfServiceProfile.php) | `public function __construct(private readonly SelfServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): SelfServiceProfile` |
| [SelfServicePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Services/SelfServicePolicy.php) | `public function canAccess(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SelfServiceCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceCase.php) | No literal fillable array detected; inspect the model and API schema. |
| [SelfServiceProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceProfile.php) | No literal fillable array detected; inspect the model and API schema. |
| [SelfServiceReference.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceReference.php) | No literal fillable array detected; inspect the model and API schema. |
| [SelfServiceResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceResource.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
