# Genealogy: Collaboration Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#collaboration). Observed identity: [`liberusoftware/module-genealogy-collaboration-livewire`](../../../modules/source/liberusoftware--module-genealogy-collaboration-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-genealogy-collaboration-livewire`  
**Matching domain module:** `genealogy-collaboration`  
**Application:** Genealogy  
**Source feature:** [Collaboration](../features/collaboration.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Invitations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Roles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Branch/change proposals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Review:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Discussions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Watch lists:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Attribution:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-genealogy-collaboration-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-genealogy-collaboration::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `invitations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `roles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `branch-change-proposals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `review`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `discussions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `watch-lists`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `attribution`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `genealogy-collaboration` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-genealogy-laravel-filament`](https://github.com/liberusoftware/project-genealogy-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/collaboration.md) · [API plan](../api/collaboration.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Invitations** | Expose a focused Livewire 4 component and namespaced Blade default view for `invitations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Roles** | Expose a focused Livewire 4 component and namespaced Blade default view for `roles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Branch/change proposals** | Expose a focused Livewire 4 component and namespaced Blade default view for `branch/change proposals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Review** | Expose a focused Livewire 4 component and namespaced Blade default view for `review` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Discussions** | Expose a focused Livewire 4 component and namespaced Blade default view for `discussions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Watch lists** | Expose a focused Livewire 4 component and namespaced Blade default view for `watch lists` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Attribution** | Expose a focused Livewire 4 component and namespaced Blade default view for `attribution` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CollaborationLivewireServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-livewire/src/CollaborationLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AcceptCollaborationInvitation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/AcceptCollaborationInvitation.php) | `public function execute(CollaborationInvitation $invitation, Authenticatable $actor): CollaborationMembership` |
| [CreateCollaborationDiscussion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/CreateCollaborationDiscussion.php) | `public function execute(array $attributes): CollaborationDiscussion` |
| [CreateCollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/CreateCollaborationProposal.php) | `public function execute(array $attributes): CollaborationProposal` |
| [CreateCollaborationSpace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/CreateCollaborationSpace.php) | `public function execute(array $attributes): CollaborationSpace` |
| [DeleteCollaborationDiscussion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/DeleteCollaborationDiscussion.php) | `public function execute(CollaborationDiscussion $discussion): void` |
| [DeleteCollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/DeleteCollaborationProposal.php) | `public function execute(CollaborationProposal $proposal): void` |
| [DeleteCollaborationSpace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/DeleteCollaborationSpace.php) | `public function execute(CollaborationSpace $space): void` |
| [InviteCollaborationMember.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/InviteCollaborationMember.php) | `public function execute(array $attributes): CollaborationInvitation` |
| [RecordCollaborationAttribution.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/RecordCollaborationAttribution.php) | `public function execute(string $type, string $id, string $action, array $metadata = [], string\|int\|null $actorId = null): CollaborationAttribution` |
| [ReviewCollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/ReviewCollaborationProposal.php) | `public function execute(CollaborationProposal $proposal, string $status, string\|int\|null $reviewerId = null): CollaborationProposal` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CollaborationAttribution.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationAttribution.php) | `team_id`, `actor_id`, `attributable_type`, `attributable_id`, `action`, `metadata`, `created_at` |
| [CollaborationDiscussion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationDiscussion.php) | `team_id`, `space_id`, `proposal_id`, `author_id`, `body`, `status`, `metadata` |
| [CollaborationInvitation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationInvitation.php) | `team_id`, `space_id`, `email`, `role`, `status`, `invited_by`, `expires_at`, `accepted_at`, `revoked_at` |
| [CollaborationMembership.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationMembership.php) | `team_id`, `space_id`, `user_id`, `role`, `status`, `joined_at` |
| [CollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationProposal.php) | `team_id`, `proposer_id`, `reviewer_id`, `title`, `description`, `status`, `reviewed_at`, `metadata` |
| [CollaborationSpace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationSpace.php) | `team_id`, `name`, `status`, `metadata` |
| [CollaborationWatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationWatch.php) | `team_id`, `user_id`, `watchable_type`, `watchable_id` |
| [VirtualEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/VirtualEvent.php) | `team_id`, `created_by`, `title`, `description`, `start_time`, `end_time`, `timezone`, `status`, `platform`, `meeting_id`, `meeting_password`, `meeting_url`, `join_url`, `platform_data`, `max_attendees`, `require_rsvp`, `allow_guests`, `instructions`, `host_email` |
<!-- layer-implementation-plan:end -->
