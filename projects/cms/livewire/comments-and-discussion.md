# CMS: Comments and Discussion Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#comments-and-discussion). Observed identity: [`liberusoftware/module-cms-comments-and-discussion-livewire`](../../../modules/source/liberusoftware--module-cms-comments-and-discussion-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-comments-and-discussion-livewire`  
**Matching domain module:** `cms-comments-and-discussion`  
**Application:** CMS  
**Source feature:** [Comments and Discussion](../features/comments-and-discussion.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Threaded comments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Guest/member policy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Moderation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Subscriptions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Mentions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Spam control:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Editing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reports:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Retention:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-comments-and-discussion-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-cms-comments-and-discussion::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `threaded-comments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `guest-member-policy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `moderation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `subscriptions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `mentions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `spam-control`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `editing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reports`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `retention`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-comments-and-discussion` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/comments-and-discussion.md) · [API plan](../api/comments-and-discussion.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Threaded comments** | Expose a focused Livewire 4 component and namespaced Blade default view for `threaded comments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Guest/member policy** | Expose a focused Livewire 4 component and namespaced Blade default view for `guest/member policy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Moderation** | Expose a focused Livewire 4 component and namespaced Blade default view for `moderation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Subscriptions** | Expose a focused Livewire 4 component and namespaced Blade default view for `subscriptions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Mentions** | Expose a focused Livewire 4 component and namespaced Blade default view for `mentions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Spam control** | Expose a focused Livewire 4 component and namespaced Blade default view for `spam control` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Editing** | Expose a focused Livewire 4 component and namespaced Blade default view for `editing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reports** | Expose a focused Livewire 4 component and namespaced Blade default view for `reports` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Retention** | Expose a focused Livewire 4 component and namespaced Blade default view for `retention` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CommentThread.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-comments-and-discussion-livewire/src/Livewire/CommentThread.php) · [CommentsAndDiscussionLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-comments-and-discussion-livewire/src/CommentsAndDiscussionLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CommentService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-comments-and-discussion/src/Services/CommentService.php) | `public function list(string $type, string $id, ?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function create(array $data, ?int $authorId = null, ?int $teamId = null): Comment`<br>`public function update(Comment $comment, string $body, ?int $actorId = null, bool $moderator = false): Comment`<br>`public function moderate(Comment $comment, string $status): Comment`<br>`public function report(Comment $comment, string $reason, ?int $reporterId = null): CommentReport`<br>`public function subscribe(Comment $comment, int $subscriberId): CommentSubscription`<br>`public function prune(int $retentionDays = 0): int` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Comment.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-comments-and-discussion/src/Models/Comment.php) | `team_id`, `commentable_type`, `commentable_id`, `parent_id`, `author_id`, `guest_name`, `guest_email`, `body`, `status`, `metadata` |
| [CommentReport.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-comments-and-discussion/src/Models/CommentReport.php) | `comment_id`, `reporter_id`, `reason`, `status` |
| [CommentSubscription.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-comments-and-discussion/src/Models/CommentSubscription.php) | `comment_id`, `subscriber_id` |
<!-- layer-implementation-plan:end -->
