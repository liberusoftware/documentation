# liberusoftware/module-genealogy-collaboration-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Liberu genealogy-collaboration-filament module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [genealogy-collaboration-filament](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: genealogy-laravel, `genealogy-collaboration-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-genealogy-collaboration-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `genealogy-collaboration-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Genealogy\\Collaboration\\Filament\\CollaborationFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/composer.json) · [module.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/module.json).

**Declared capabilities:** genealogy.collaboration.filament

**Declared features:** filament presentation for collaboration

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-genealogy-collaboration` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Genealogy\\Collaboration\\Filament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-genealogy-collaboration": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/CollaborationFilamentServiceProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/CollaborationFilamentServiceProvider.php) · [src/Resources/CollaborationDiscussionResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationDiscussionResource.php) · [src/Resources/CollaborationDiscussionResource/Pages/CreateCollaborationDiscussion.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationDiscussionResource/Pages/CreateCollaborationDiscussion.php) · [src/Resources/CollaborationDiscussionResource/Pages/EditCollaborationDiscussion.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationDiscussionResource/Pages/EditCollaborationDiscussion.php) · [src/Resources/CollaborationDiscussionResource/Pages/ListCollaborationDiscussions.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationDiscussionResource/Pages/ListCollaborationDiscussions.php) · [src/Resources/CollaborationInvitationResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationInvitationResource.php) · [src/Resources/CollaborationInvitationResource/Pages/CreateCollaborationInvitation.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationInvitationResource/Pages/CreateCollaborationInvitation.php) · [src/Resources/CollaborationInvitationResource/Pages/ListCollaborationInvitations.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationInvitationResource/Pages/ListCollaborationInvitations.php) · [src/Resources/CollaborationMembershipResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationMembershipResource.php) · [src/Resources/CollaborationMembershipResource/Pages/EditCollaborationMembership.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationMembershipResource/Pages/EditCollaborationMembership.php) · [src/Resources/CollaborationMembershipResource/Pages/ListCollaborationMemberships.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationMembershipResource/Pages/ListCollaborationMemberships.php) · [src/Resources/CollaborationProposalResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationProposalResource.php) · [src/Resources/CollaborationProposalResource/Pages/CreateCollaborationProposal.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationProposalResource/Pages/CreateCollaborationProposal.php) · [src/Resources/CollaborationProposalResource/Pages/EditCollaborationProposal.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationProposalResource/Pages/EditCollaborationProposal.php) · [src/Resources/CollaborationProposalResource/Pages/ListCollaborationProposals.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationProposalResource/Pages/ListCollaborationProposals.php) · [src/Resources/CollaborationSpaceResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationSpaceResource.php) · [src/Resources/CollaborationSpaceResource/Pages/CreateCollaborationSpace.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationSpaceResource/Pages/CreateCollaborationSpace.php) · [src/Resources/CollaborationSpaceResource/Pages/EditCollaborationSpace.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationSpaceResource/Pages/EditCollaborationSpace.php) · [src/Resources/CollaborationSpaceResource/Pages/ListCollaborationSpaces.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/src/Resources/CollaborationSpaceResource/Pages/ListCollaborationSpaces.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Unit/BoundaryTest.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-collaboration-filament/tests/Unit/BoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
