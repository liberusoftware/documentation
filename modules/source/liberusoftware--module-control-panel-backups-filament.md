# liberusoftware/module-control-panel-backups-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament adapter for Control Panel Backups.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-backups-filament](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-control-panel-laravel-filament, `control-panel-backups-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-backups-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-backups-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\BackupsFilament\\BackupsFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/composer.json) · [module.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/module.json).

**Declared capabilities:** control-panel.backups.filament

**Declared features:** Policies, Snapshots, Destinations, Schedules, Restore, Verification, Retention

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-control-panel-backups` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\BackupsFilament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-control-panel-backups": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/BackupsFilamentPlugin.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/BackupsFilamentPlugin.php) · [src/BackupsFilamentServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/BackupsFilamentServiceProvider.php) · [src/Resources/BackupDestinationResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupDestinationResource.php) · [src/Resources/BackupDestinationResource/Pages/CreateBackupDestination.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupDestinationResource/Pages/CreateBackupDestination.php) · [src/Resources/BackupDestinationResource/Pages/EditBackupDestination.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupDestinationResource/Pages/EditBackupDestination.php) · [src/Resources/BackupDestinationResource/Pages/ListBackupDestinations.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupDestinationResource/Pages/ListBackupDestinations.php) · [src/Resources/BackupEncryptionResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupEncryptionResource.php) · [src/Resources/BackupEncryptionResource/Pages/ListBackupEncryptions.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupEncryptionResource/Pages/ListBackupEncryptions.php) · [src/Resources/BackupExecutionResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupExecutionResource.php) · [src/Resources/BackupExecutionResource/Pages/ListBackupExecutions.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupExecutionResource/Pages/ListBackupExecutions.php) · [src/Resources/BackupFeatureResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupFeatureResource.php) · [src/Resources/BackupPolicyResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupPolicyResource.php) · [src/Resources/BackupPolicyResource/Pages/CreateBackupPolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupPolicyResource/Pages/CreateBackupPolicy.php) · [src/Resources/BackupPolicyResource/Pages/EditBackupPolicy.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupPolicyResource/Pages/EditBackupPolicy.php) · [src/Resources/BackupPolicyResource/Pages/ListBackupPolicies.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupPolicyResource/Pages/ListBackupPolicies.php) · [src/Resources/BackupRestoreResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupRestoreResource.php) · [src/Resources/BackupRestoreResource/Pages/ListBackupRestores.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupRestoreResource/Pages/ListBackupRestores.php) · [src/Resources/BackupScheduleResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupScheduleResource.php) · [src/Resources/BackupScheduleResource/Pages/CreateBackupSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupScheduleResource/Pages/CreateBackupSchedule.php) · [src/Resources/BackupScheduleResource/Pages/EditBackupSchedule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupScheduleResource/Pages/EditBackupSchedule.php) · [src/Resources/BackupScheduleResource/Pages/ListBackupSchedules.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupScheduleResource/Pages/ListBackupSchedules.php) · [src/Resources/BackupSnapshotResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupSnapshotResource.php) · [src/Resources/BackupSnapshotResource/Pages/CreateBackupSnapshot.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupSnapshotResource/Pages/CreateBackupSnapshot.php) · [src/Resources/BackupSnapshotResource/Pages/EditBackupSnapshot.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupSnapshotResource/Pages/EditBackupSnapshot.php) · [src/Resources/BackupSnapshotResource/Pages/ListBackupSnapshots.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/BackupSnapshotResource/Pages/ListBackupSnapshots.php) · [src/Resources/OffsiteTransferResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/OffsiteTransferResource.php) · [src/Resources/OffsiteTransferResource/Pages/ListOffsiteTransfers.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-backups-filament/src/Resources/OffsiteTransferResource/Pages/ListOffsiteTransfers.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
