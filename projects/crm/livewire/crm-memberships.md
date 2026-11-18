# CRM: Crm Memberships Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-memberships). Observed identity: [`liberusoftware/module-crm-memberships-livewire`](../../../modules/source/liberusoftware--module-crm-memberships-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-memberships-livewire`  
**Matching domain module:** `crm-memberships`  
**Application:** CRM  
**Source feature:** [Crm Memberships](../features/crm-memberships.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Membership plans:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Gated resources:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Lifecycle:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Access grants:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Renewal references:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Community/course bundles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Member portal:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-memberships-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmMemberships::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `membership-plans`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `gated-resources`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `lifecycle`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `access-grants`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `renewal-references`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `community-course-bundles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `member-portal`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-memberships` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-memberships.md) · [API plan](../api/crm-memberships.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Membership plans** | Expose a focused Livewire 4 component and namespaced Blade default view for `membership plans` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Gated resources** | Expose a focused Livewire 4 component and namespaced Blade default view for `gated resources` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Lifecycle** | Expose a focused Livewire 4 component and namespaced Blade default view for `lifecycle` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Access grants** | Expose a focused Livewire 4 component and namespaced Blade default view for `access grants` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Renewal references** | Expose a focused Livewire 4 component and namespaced Blade default view for `renewal references` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Community/course bundles** | Expose a focused Livewire 4 component and namespaced Blade default view for `community/course bundles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Member portal** | Expose a focused Livewire 4 component and namespaced Blade default view for `member portal` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [MemberPortal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships-livewire/src/Components/MemberPortal.php) · [MembershipsLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships-livewire/src/MembershipsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [MembershipQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Queries/MembershipQuery.php) | `public function forTeam(int $teamId)`<br>`public function memberGrants(int $teamId, int $memberId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ChangeGrantStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Actions/ChangeGrantStatus.php) | `public function __construct(private readonly MembershipPolicy $policy)`<br>`public function execute(int $teamId, int $userId, MembershipGrant $grant, array $input): MembershipGrant` |
| [CreatePlan.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Actions/CreatePlan.php) | `public function __construct(private readonly MembershipPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): MembershipPlan` |
| [GrantAccess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Actions/GrantAccess.php) | `public function __construct(private readonly MembershipPolicy $policy)`<br>`public function execute(int $teamId, int $userId, MembershipPlan $plan, array $input): MembershipGrant` |
| [MembershipPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Services/MembershipPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MembershipBundle.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Models/MembershipBundle.php) | No literal fillable array detected; inspect the model and API schema. |
| [MembershipGrant.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Models/MembershipGrant.php) | No literal fillable array detected; inspect the model and API schema. |
| [MembershipPlan.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Models/MembershipPlan.php) | No literal fillable array detected; inspect the model and API schema. |
| [MembershipResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-memberships/src/Models/MembershipResource.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
