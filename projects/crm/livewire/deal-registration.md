# CRM: Deal Registration Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#deal-registration). Observed identity: [`liberusoftware/module-crm-deal-registration-livewire`](../../../modules/source/liberusoftware--module-crm-deal-registration-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-deal-registration-livewire`  
**Matching domain module:** `crm-deal-registration`  
**Application:** CRM  
**Source feature:** [Deal Registration](../features/deal-registration.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Partner-submitted leads/deals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Duplicate/conflict checks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Territory rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Approval:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Protection windows:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Collaboration:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Attribution:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-deal-registration-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-deal-registration::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `partner-submitted-leads-deals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `duplicate-conflict-checks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `territory-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `approval`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `protection-windows`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `collaboration`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `attribution`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-deal-registration` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/deal-registration.md) · [API plan](../api/deal-registration.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Partner-submitted leads/deals** | Expose a focused Livewire 4 component and namespaced Blade default view for `partner-submitted leads/deals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Duplicate/conflict checks** | Expose a focused Livewire 4 component and namespaced Blade default view for `duplicate/conflict checks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Territory rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `territory rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Approval** | Expose a focused Livewire 4 component and namespaced Blade default view for `approval` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Protection windows** | Expose a focused Livewire 4 component and namespaced Blade default view for `protection windows` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Collaboration** | Expose a focused Livewire 4 component and namespaced Blade default view for `collaboration` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Attribution** | Expose a focused Livewire 4 component and namespaced Blade default view for `attribution` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [DealDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration-livewire/src/Livewire/DealDashboard.php) · [DealRegistrationLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration-livewire/src/DealRegistrationLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [DealRegistrationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Queries/DealRegistrationQuery.php) | `public function deals(int $teamId)`<br>`public function protected(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveDeal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Actions/ApproveDeal.php) | `public function __construct(private readonly DealRegistrationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, DealRegistration $deal, int $protectionDays = 90): DealRegistration` |
| [CollaborateOnDeal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Actions/CollaborateOnDeal.php) | `public function __construct(private readonly DealRegistrationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, DealRegistration $deal, array $input): DealRegistration` |
| [SubmitDeal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Actions/SubmitDeal.php) | `public function __construct(private readonly DealRegistrationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): DealRegistration` |
| [DealRegistrationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Services/DealRegistrationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DealRegistration.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Models/DealRegistration.php) | No literal fillable array detected; inspect the model and API schema. |
| [DealRegistrationEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Models/DealRegistrationEvent.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
