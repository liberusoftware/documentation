# CRM: Crm Prospecting Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-prospecting). Observed identity: [`liberusoftware/module-crm-prospecting-livewire`](../../../modules/source/liberusoftware--module-crm-prospecting-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-prospecting-livewire`  
**Matching domain module:** `crm-prospecting`  
**Application:** CRM  
**Source feature:** [Crm Prospecting](../features/crm-prospecting.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Ideal-customer profiles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Prospect searches:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **List building:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Research queues:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Contact reveal/credits:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Provider provenance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Compliant export/outreach handoff:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-prospecting-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmProspecting::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `ideal-customer-profiles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `prospect-searches`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `list-building`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `research-queues`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `contact-reveal-credits`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `provider-provenance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `compliant-export-outreach-handoff`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-prospecting` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-prospecting.md) · [API plan](../api/crm-prospecting.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Ideal-customer profiles** | Expose a focused Livewire 4 component and namespaced Blade default view for `ideal-customer profiles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Prospect searches** | Expose a focused Livewire 4 component and namespaced Blade default view for `prospect searches` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **List building** | Expose a focused Livewire 4 component and namespaced Blade default view for `list building` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Research queues** | Expose a focused Livewire 4 component and namespaced Blade default view for `research queues` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Contact reveal/credits** | Expose a focused Livewire 4 component and namespaced Blade default view for `contact reveal/credits` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Provider provenance** | Expose a focused Livewire 4 component and namespaced Blade default view for `provider provenance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Compliant export/outreach handoff** | Expose a focused Livewire 4 component and namespaced Blade default view for `compliant export/outreach handoff` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ProspectingDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-livewire/src/Components/ProspectingDashboard.php) · [ProspectingLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-livewire/src/ProspectingLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ProspectingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Queries/ProspectingQuery.php) | `public function profiles(int $teamId)`<br>`public function searches(int $teamId)`<br>`public function prospects(int $teamId)`<br>`public function queue(int $teamId)`<br>`public function exports(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateIdealCustomerProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/CreateIdealCustomerProfile.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): IdealCustomerProfile` |
| [CreateProspectSearch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/CreateProspectSearch.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectSearch` |
| [ImportProspect.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/ImportProspect.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Prospect` |
| [QueueExport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/QueueExport.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectExport` |
| [QueueResearch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/QueueResearch.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectResearchItem` |
| [RevealContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/RevealContact.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectCredit` |
| [UpdateProspect.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/UpdateProspect.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $prospectId, array $input): Prospect` |
| [ProspectingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Services/ProspectingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [IdealCustomerProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/IdealCustomerProfile.php) | No literal fillable array detected; inspect the model and API schema. |
| [Prospect.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/Prospect.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectCredit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectCredit.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectExport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectExport.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectResearchItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectResearchItem.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectSearch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectSearch.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
