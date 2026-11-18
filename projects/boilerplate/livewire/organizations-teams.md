# Boilerplate: Organizations Teams Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#organizations-teams). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-boilerplate-organizations-teams-livewire`  
**Matching domain module:** `organizations-teams`  
**Application:** Boilerplate  
**Source feature:** [Organizations Teams](../features/organizations-teams.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Organizations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Teams:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Memberships:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Invitations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Ownership:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Switching:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Transfer:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Lifecycle:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-boilerplate-organizations-teams-livewire` component namespace and service provider; use explicit aliases such as `<livewire:boilerplateOrganizationsTeams::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `organizations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `teams`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `memberships`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `invitations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `ownership`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `switching`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `transfer`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `lifecycle`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `organizations-teams` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/organizations-teams.md) · [API plan](../api/organizations-teams.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Organizations** | Expose a focused Livewire 4 component and namespaced Blade default view for `organizations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Teams** | Expose a focused Livewire 4 component and namespaced Blade default view for `teams` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Memberships** | Expose a focused Livewire 4 component and namespaced Blade default view for `memberships` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Invitations** | Expose a focused Livewire 4 component and namespaced Blade default view for `invitations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Ownership** | Expose a focused Livewire 4 component and namespaced Blade default view for `ownership` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Switching** | Expose a focused Livewire 4 component and namespaced Blade default view for `switching` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Transfer** | Expose a focused Livewire 4 component and namespaced Blade default view for `transfer` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Lifecycle** | Expose a focused Livewire 4 component and namespaced Blade default view for `lifecycle` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AcceptInvitation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/AcceptInvitation.php) | `public function handle(string $token, Authenticatable $actor, string $email): void` |
| [InviteMember.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/InviteMember.php) | `public function handle(int $teamId, string $email, string $role, int\|string $inviterId, ?\DateTimeImmutable $expiresAt = null): string` |
| [TransferOwnership.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/TransferOwnership.php) | `public function handle(Team $team, int\|string $currentOwner, int\|string $successor, bool $recentlyAuthenticated): void` |
| [OrganizationActor.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Contracts/OrganizationActor.php) | `public function belongsToTeam($team)`<br>`public function ownsTeam($team)` |
| [TeamPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Policies/TeamPolicy.php) | `public function viewAny(OrganizationActor $user): bool`<br>`public function view(OrganizationActor $user, Team $team): bool`<br>`public function create(OrganizationActor $user): bool`<br>`public function update(OrganizationActor $user, Team $team): bool`<br>`public function addTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function updateTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function removeTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function delete(OrganizationActor $user, Team $team): bool` |
| [CurrentTeamResolver.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Services/CurrentTeamResolver.php) | `public function resolve(Authenticatable $actor, int\|string\|null $requested): ?Team` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Membership.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/Membership.php) | No literal fillable array detected; inspect the model and API schema. |
| [Organization.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/Organization.php) | `name`, `slug`, `owner_id`, `status`, `archived_at` |
| [Team.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/Team.php) | `name`, `personal_team`, `organization_id`, `status` |
| [TeamInvitation.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/TeamInvitation.php) | `email`, `role`, `token_hash`, `invited_by`, `expires_at`, `accepted_at`, `revoked_at` |
<!-- layer-implementation-plan:end -->
