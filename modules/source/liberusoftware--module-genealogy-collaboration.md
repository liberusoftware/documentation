# liberusoftware/module-genealogy-collaboration: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Liberu genealogy-collaboration module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [genealogy-collaboration](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-genealogy-laravel-filament, `genealogy-collaboration`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-genealogy-collaboration` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `genealogy-collaboration` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Genealogy\\Collaboration\\CollaborationServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/composer.json) · [module.json](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/module.json).

**Declared capabilities:** genealogy.collaboration, genealogy.collaboration.invitations, genealogy.collaboration.roles, genealogy.collaboration.proposals, genealogy.collaboration.review, genealogy.collaboration.discussions, genealogy.collaboration.watch-lists, genealogy.collaboration.events, genealogy.collaboration.rsvp, genealogy.collaboration.video-conferencing, genealogy.collaboration.attribution, genealogy.collaboration.lifecycle

**Declared features:** genealogy collaboration, genealogy collaboration invitations, genealogy collaboration roles, genealogy collaboration proposals, genealogy collaboration review, genealogy collaboration discussions, genealogy collaboration watch-lists, genealogy collaboration virtual events, genealogy collaboration event RSVPs, genealogy collaboration attribution, genealogy collaboration lifecycle

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-genealogy-core` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Genealogy\\Collaboration\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-genealogy-core": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AcceptCollaborationInvitation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/AcceptCollaborationInvitation.php) | `public function execute(CollaborationInvitation $invitation, Authenticatable $actor): CollaborationMembership` |
| [src/Actions/CreateCollaborationDiscussion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/CreateCollaborationDiscussion.php) | `public function execute(array $attributes): CollaborationDiscussion` |
| [src/Actions/CreateCollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/CreateCollaborationProposal.php) | `public function execute(array $attributes): CollaborationProposal` |
| [src/Actions/CreateCollaborationSpace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/CreateCollaborationSpace.php) | `public function execute(array $attributes): CollaborationSpace` |
| [src/Actions/DeleteCollaborationDiscussion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/DeleteCollaborationDiscussion.php) | `public function execute(CollaborationDiscussion $discussion): void` |
| [src/Actions/DeleteCollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/DeleteCollaborationProposal.php) | `public function execute(CollaborationProposal $proposal): void` |
| [src/Actions/DeleteCollaborationSpace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/DeleteCollaborationSpace.php) | `public function execute(CollaborationSpace $space): void` |
| [src/Actions/InviteCollaborationMember.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/InviteCollaborationMember.php) | `public function execute(array $attributes): CollaborationInvitation` |
| [src/Actions/RecordCollaborationAttribution.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/RecordCollaborationAttribution.php) | `public function execute(string $type, string $id, string $action, array $metadata = [], string\|int\|null $actorId = null): CollaborationAttribution` |
| [src/Actions/ReviewCollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/ReviewCollaborationProposal.php) | `public function execute(CollaborationProposal $proposal, string $status, string\|int\|null $reviewerId = null): CollaborationProposal` |
| [src/Actions/RevokeCollaborationInvitation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/RevokeCollaborationInvitation.php) | `public function execute(CollaborationInvitation $invitation): CollaborationInvitation` |
| [src/Actions/RsvpToVirtualEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/RsvpToVirtualEvent.php) | `public function execute(VirtualEvent $event, Model $user, string $status, ?string $notes = null): VirtualEventAttendee` |
| [src/Actions/SetCollaborationMembershipRole.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/SetCollaborationMembershipRole.php) | `public function execute(CollaborationMembership $membership, string $role): CollaborationMembership` |
| [src/Actions/ToggleCollaborationWatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/ToggleCollaborationWatch.php) | `public function execute(string $watchableType, string $watchableId, string\|int $userId): ?CollaborationWatch` |
| [src/Actions/UpdateCollaborationDiscussion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/UpdateCollaborationDiscussion.php) | `public function execute(CollaborationDiscussion $discussion, array $attributes): CollaborationDiscussion` |
| [src/Actions/UpdateCollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/UpdateCollaborationProposal.php) | `public function execute(CollaborationProposal $proposal, array $attributes): CollaborationProposal` |
| [src/Actions/UpdateCollaborationSpace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Actions/UpdateCollaborationSpace.php) | `public function execute(CollaborationSpace $space, array $attributes): CollaborationSpace` |
| [src/Contracts/VideoConferencingProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Contracts/VideoConferencingProvider.php) | `public function key(): string`<br>`public function isAvailable(): bool`<br>`public function createMeeting(array $meetingData): array`<br>`public function updateMeeting(array $meetingData): array`<br>`public function deleteMeeting(string $meetingId): bool`<br>`public function meetingDetails(string $meetingId): ?array`<br>`public function attendees(string $meetingId): array`<br>`public function sendInvitations(string $meetingId, array $emails): bool` |
| [src/Services/VideoConferencingService.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Services/VideoConferencingService.php) | `public function createMeeting(VirtualEvent $event, iterable $providers): ?array`<br>`public function updateMeeting(VirtualEvent $event, iterable $providers): ?array`<br>`public function deleteMeeting(VirtualEvent $event, iterable $providers): bool`<br>`public function availablePlatforms(iterable $providers): Collection` |

Other non-legacy PHP sources: [src/Capability.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Capability.php) · [src/CollaborationServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/CollaborationServiceProvider.php) · [src/Events/CollaborationProposalCreated.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Events/CollaborationProposalCreated.php) · [src/Events/CollaborationProposalReviewed.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Events/CollaborationProposalReviewed.php) · [src/Models/CollaborationAttribution.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationAttribution.php) · [src/Models/CollaborationDiscussion.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationDiscussion.php) · [src/Models/CollaborationInvitation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationInvitation.php) · [src/Models/CollaborationMembership.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationMembership.php) · [src/Models/CollaborationProposal.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationProposal.php) · [src/Models/CollaborationSpace.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationSpace.php) · [src/Models/CollaborationWatch.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/CollaborationWatch.php) · [src/Models/VirtualEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/VirtualEvent.php) · [src/Models/VirtualEventAttendee.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/src/Models/VirtualEventAttendee.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_010000_create_genealogy_collaboration_spaces_table.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/database/migrations/2026_08_24_010000_create_genealogy_collaboration_spaces_table.php)
- [database/migrations/2026_08_25_060000_create_genealogy_collaboration_proposals_table.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/database/migrations/2026_08_25_060000_create_genealogy_collaboration_proposals_table.php)
- [database/migrations/2026_08_25_070000_create_genealogy_collaboration_workflows_tables.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/database/migrations/2026_08_25_070000_create_genealogy_collaboration_workflows_tables.php)
- [database/migrations/2026_08_30_030000_create_genealogy_virtual_events_tables.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/database/migrations/2026_08_30_030000_create_genealogy_virtual_events_tables.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/DomainTest.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/tests/Feature/DomainTest.php)
- [tests/Unit/CapabilityTest.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration/tests/Unit/CapabilityTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
