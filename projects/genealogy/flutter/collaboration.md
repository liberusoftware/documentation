# Collaboration Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#collaboration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-genealogy-collaboration-flutter
**Matching core package:** module-genealogy-collaboration ([implementation](../core/collaboration.md))
**Matching API package:** module-genealogy-collaboration-api ([contract](../api/collaboration.md))

## Implementation plan

This adapter presents Collaboration for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Collaboration API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/collaboration.md), and [API module](../api/collaboration.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `collaboration`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-genealogy-mobile-flutter`](https://github.com/liberusoftware/project-genealogy-mobile-flutter) | [`module-genealogy-collaboration-flutter`](https://github.com/liberusoftware/module-genealogy-collaboration-flutter) (`module_genealogy_collaboration_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-genealogy-dart-mobile`](https://github.com/liberusoftware/project-genealogy-dart-mobile) | [`module-genealogy-collaboration-dart-mobile`](https://github.com/liberusoftware/module-genealogy-collaboration-dart-mobile) (`module_genealogy_collaboration_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-genealogy-dart-desktop`](https://github.com/liberusoftware/project-genealogy-dart-desktop) | [`module-genealogy-collaboration-dart-desktop`](https://github.com/liberusoftware/module-genealogy-collaboration-dart-desktop) (`module_genealogy_collaboration_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | [API plan](../api/collaboration.md) · [Core plan](../core/collaboration.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Invitations** | Adaptive mobile cards/sheets for `invitations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `invitations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Roles** | Adaptive mobile cards/sheets for `roles` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `roles` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Branch/change proposals** | Adaptive mobile cards/sheets for `branch/change proposals` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `branch/change proposals` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Review** | Adaptive mobile cards/sheets for `review` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `review` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Discussions** | Adaptive mobile cards/sheets for `discussions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `discussions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Watch lists** | Adaptive mobile cards/sheets for `watch lists` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `watch lists` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Attribution** | Adaptive mobile cards/sheets for `attribution` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `attribution` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-genealogy-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

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
