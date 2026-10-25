# liberusoftware/automation-video: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral video domain module for Liberu Automation.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [module-automation-video](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/composer.json) | `68e5f07a6704` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: automation-laravel, `module-automation-video`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/automation-video` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `module-automation-video` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Modules\\Automation\\Video\\VideoServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/composer.json) · [module.json](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/module.json).

**Declared capabilities:** automation.video.generation-jobs, automation.video.editing-jobs, automation.video.scripts, automation.video.captions, automation.video.audio, automation.video.moderation, automation.video.provenance, automation.video.delivery

**Declared features:** generation jobs, editing jobs, scripts, captions, audio, moderation, provenance, delivery

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Modules\\Automation\\Video\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateVideoResource.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/Actions/CreateVideoResource.php) | `public function execute(string $teamId, string $name, array $payload = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): VideoResource` |
| [src/Actions/TransitionVideoResource.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/Actions/TransitionVideoResource.php) | `public function execute(VideoResource $resource, string $teamId, string $status, array $allowedStatuses = ['draft', 'active', 'paused', 'completed', 'failed', 'cancelled'], ?string $actorId = null, ?string $correlationId = null): VideoResource` |

Other non-legacy PHP sources: [src/Domain/CaptionCue.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/Domain/CaptionCue.php) · [src/Domain/CaptionTrack.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/Domain/CaptionTrack.php) · [src/Domain/VideoDelivery.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/Domain/VideoDelivery.php) · [src/Domain/VideoJob.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/Domain/VideoJob.php) · [src/Domain/VideoModerationDecision.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/Domain/VideoModerationDecision.php) · [src/Domain/VideoProvenance.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/Domain/VideoProvenance.php) · [src/Domain/VideoRequest.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/Domain/VideoRequest.php) · [src/Events/ResourceTransitioned.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/Events/ResourceTransitioned.php) · [src/Models/VideoResource.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/Models/VideoResource.php) · [src/VideoServiceProvider.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/VideoServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_23_000000_create_automation_video_resources_table.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/database/migrations/2026_08_23_000000_create_automation_video_resources_table.php)
- [database/migrations/2026_08_30_000003_add_lifecycle_metadata_to_automation_video_resources.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/database/migrations/2026_08_30_000003_add_lifecycle_metadata_to_automation_video_resources.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Unit/DomainTest.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/tests/Unit/DomainTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
