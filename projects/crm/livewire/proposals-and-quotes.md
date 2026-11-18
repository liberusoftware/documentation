# CRM: Proposals and Quotes Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#proposals-and-quotes). Observed identity: [`liberusoftware/module-crm-proposals-and-quotes-livewire`](../../../modules/source/liberusoftware--module-crm-proposals-and-quotes-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-proposals-and-quotes-livewire`  
**Matching domain module:** `crm-proposals-and-quotes`  
**Application:** CRM  
**Source feature:** [Proposals and Quotes](../features/proposals-and-quotes.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Branded templates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sections:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Scope:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Line items:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Optional choices:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Versions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Comments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Approvals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Delivery:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Engagement:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Acceptance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Expiry:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-proposals-and-quotes-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-proposals-and-quotes::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `branded-templates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sections`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `scope`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `line-items`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `optional-choices`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `versions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `comments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `approvals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `delivery`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `engagement`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `acceptance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `expiry`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-proposals-and-quotes` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/proposals-and-quotes.md) · [API plan](../api/proposals-and-quotes.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Branded templates** | Expose a focused Livewire 4 component and namespaced Blade default view for `branded templates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sections** | Expose a focused Livewire 4 component and namespaced Blade default view for `sections` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Scope** | Expose a focused Livewire 4 component and namespaced Blade default view for `scope` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Line items** | Expose a focused Livewire 4 component and namespaced Blade default view for `line items` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Optional choices** | Expose a focused Livewire 4 component and namespaced Blade default view for `optional choices` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Versions** | Expose a focused Livewire 4 component and namespaced Blade default view for `versions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Comments** | Expose a focused Livewire 4 component and namespaced Blade default view for `comments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Approvals** | Expose a focused Livewire 4 component and namespaced Blade default view for `approvals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Delivery** | Expose a focused Livewire 4 component and namespaced Blade default view for `delivery` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Engagement** | Expose a focused Livewire 4 component and namespaced Blade default view for `engagement` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Acceptance** | Expose a focused Livewire 4 component and namespaced Blade default view for `acceptance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Expiry** | Expose a focused Livewire 4 component and namespaced Blade default view for `expiry` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ProposalDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes-livewire/src/Components/ProposalDashboard.php) · [ProposalsAndQuotesLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes-livewire/src/ProposalsAndQuotesLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ProposalQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Queries/ProposalQuery.php) | `public function templates(int $teamId)`<br>`public function proposals(int $teamId)`<br>`public function versions(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddProposalComment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/AddProposalComment.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalEvent` |
| [ChangeProposalStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/ChangeProposalStatus.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $proposalId, string $status): Proposal` |
| [CreateProposal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposal.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Proposal` |
| [CreateProposalTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposalTemplate.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalTemplate` |
| [CreateProposalVersion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/CreateProposalVersion.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProposalVersion` |
| [UpdateProposal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Actions/UpdateProposal.php) | `public function __construct(private readonly ProposalPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $proposalId, array $input): Proposal` |
| [ProposalPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Services/ProposalPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Proposal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/Proposal.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalTemplate.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProposalVersion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-proposals-and-quotes/src/Models/ProposalVersion.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
