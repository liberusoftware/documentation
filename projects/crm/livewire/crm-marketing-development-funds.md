# CRM: Crm Marketing Development Funds Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-marketing-development-funds). Observed identity: [`liberusoftware/module-crm-marketing-development-funds-livewire`](../../../modules/source/liberusoftware--module-crm-marketing-development-funds-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-marketing-development-funds-livewire`  
**Matching domain module:** `crm-marketing-development-funds`  
**Application:** CRM  
**Source feature:** [Crm Marketing Development Funds](../features/crm-marketing-development-funds.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Requests:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Budgets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Plans:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Approvals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Evidence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Claims:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reimbursements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **ROI:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-marketing-development-funds-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmMarketingDevelopmentFunds::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `requests`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `budgets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `plans`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `approvals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `evidence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `claims`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reimbursements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `roi`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-marketing-development-funds` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-marketing-development-funds.md) · [API plan](../api/crm-marketing-development-funds.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Requests** | Expose a focused Livewire 4 component and namespaced Blade default view for `requests` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Budgets** | Expose a focused Livewire 4 component and namespaced Blade default view for `budgets` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Plans** | Expose a focused Livewire 4 component and namespaced Blade default view for `plans` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Approvals** | Expose a focused Livewire 4 component and namespaced Blade default view for `approvals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Evidence** | Expose a focused Livewire 4 component and namespaced Blade default view for `evidence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Claims** | Expose a focused Livewire 4 component and namespaced Blade default view for `claims` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reimbursements** | Expose a focused Livewire 4 component and namespaced Blade default view for `reimbursements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **ROI** | Expose a focused Livewire 4 component and namespaced Blade default view for `roi` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [MdfDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds-livewire/src/Components/MdfDashboard.php) · [MarketingDevelopmentFundsLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds-livewire/src/MarketingDevelopmentFundsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [MdfQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Queries/MdfQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateFund.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Actions/CreateFund.php) | `public function __construct(private readonly MdfPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): MdfFund` |
| [CreateMdfRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Actions/CreateMdfRequest.php) | `public function __construct(private readonly MdfPolicy $policy)`<br>`public function execute(int $teamId, int $userId, MdfFund $fund, array $input): MdfRequest` |
| [RecordMdfEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Actions/RecordMdfEvent.php) | `public function __construct(private readonly MdfPolicy $policy)`<br>`public function execute(int $teamId, int $userId, MdfRequest $request, array $input): MdfRequestEvent` |
| [MdfPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Services/MdfPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MdfFund.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Models/MdfFund.php) | No literal fillable array detected; inspect the model and API schema. |
| [MdfRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Models/MdfRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [MdfRequestEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-marketing-development-funds/src/Models/MdfRequestEvent.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
