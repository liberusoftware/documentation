# liberusoftware/liberu-platform-orchestration-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Liberu liberu-platform-orchestration-filament module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [liberu-platform-orchestration-filament](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration-filament/composer.json) | `68e5f07a6704` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-automation-laravel-filament, `liberu-platform-orchestration-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/liberu-platform-orchestration-filament` |
| Composer version field | `1.1.2` |
| Package type | `liberu-module` |
| Module manifest name | `liberu-platform-orchestration-filament` |
| Module version field | `1.1.1` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Platform\\PlatformOrchestration\\Filament\\PlatformOrchestrationFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration-filament/composer.json) · [module.json](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration-filament/module.json).

**Declared capabilities:** liberu.platform-orchestration.filament

**Declared features:** filament presentation for platform-orchestration

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/liberu-platform-orchestration` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Platform\\PlatformOrchestration\\Filament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/liberu-platform-orchestration": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/PlatformOrchestrationFilamentServiceProvider.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration-filament/src/PlatformOrchestrationFilamentServiceProvider.php) · [src/Resources/PlatformWorkflowResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration-filament/src/Resources/PlatformWorkflowResource.php) · [src/Resources/PlatformWorkflowResource/Pages/CreatePlatformWorkflow.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration-filament/src/Resources/PlatformWorkflowResource/Pages/CreatePlatformWorkflow.php) · [src/Resources/PlatformWorkflowResource/Pages/EditPlatformWorkflow.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration-filament/src/Resources/PlatformWorkflowResource/Pages/EditPlatformWorkflow.php) · [src/Resources/PlatformWorkflowResource/Pages/ListPlatformWorkflows.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration-filament/src/Resources/PlatformWorkflowResource/Pages/ListPlatformWorkflows.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Unit/BoundaryTest.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-platform-orchestration-filament/tests/Unit/BoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
