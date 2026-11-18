# CMS: Content Governance Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#content-governance). Observed identity: [`liberusoftware/module-cms-content-governance-livewire`](../../../modules/source/liberusoftware--module-cms-content-governance-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-content-governance-livewire`  
**Matching domain module:** `cms-content-governance`  
**Application:** CMS  
**Source feature:** [Content Governance](../features/content-governance.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Owners/stewards:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Policy labels:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Review cycles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Retention:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Legal hold:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sensitive-content classification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Compliance evidence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-content-governance-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-cms-content-governance::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `owners-stewards`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `policy-labels`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `review-cycles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `retention`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `legal-hold`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sensitive-content-classification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `compliance-evidence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-content-governance` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/content-governance.md) · [API plan](../api/content-governance.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Owners/stewards** | Expose a focused Livewire 4 component and namespaced Blade default view for `owners/stewards` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Policy labels** | Expose a focused Livewire 4 component and namespaced Blade default view for `policy labels` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Review cycles** | Expose a focused Livewire 4 component and namespaced Blade default view for `review cycles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Retention** | Expose a focused Livewire 4 component and namespaced Blade default view for `retention` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Legal hold** | Expose a focused Livewire 4 component and namespaced Blade default view for `legal hold` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sensitive-content classification** | Expose a focused Livewire 4 component and namespaced Blade default view for `sensitive-content classification` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Compliance evidence** | Expose a focused Livewire 4 component and namespaced Blade default view for `compliance evidence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [GovernanceOverview.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-governance-livewire/src/Livewire/GovernanceOverview.php) · [ContentGovernanceLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-governance-livewire/src/ContentGovernanceLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentGovernanceService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-governance/src/Services/ContentGovernanceService.php) | `public function records(?int $teamId, int $perPage = 25): LengthAwarePaginator`<br>`public function record(string $subjectType, string $subjectKey, array $data = [], ?int $teamId = null): GovernanceRecord`<br>`public function placeLegalHold(GovernanceRecord $record, string $reason): GovernanceRecord`<br>`public function releaseLegalHold(GovernanceRecord $record): GovernanceRecord`<br>`public function addEvidence(GovernanceRecord $record, array $evidence): GovernanceRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [GovernanceRecord.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-governance/src/Models/GovernanceRecord.php) | `team_id`, `subject_type`, `subject_key`, `owner_id`, `steward_id`, `policy_labels`, `classification`, `review_due_at`, `retention_until`, `legal_hold`, `legal_hold_at`, `legal_hold_reason`, `evidence` |
<!-- layer-implementation-plan:end -->
