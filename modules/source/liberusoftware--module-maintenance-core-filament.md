# liberusoftware/module-maintenance-core-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament 5 adapter for Maintenance Core.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [module-maintenance-core-filament](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/composer.json) | `c267d625e264` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: maintenance-laravel, `module-maintenance-core-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-maintenance-core-filament` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-maintenance-core-filament` |
| Module version field | `0.1.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Modules\\Maintenance\\Core\\Filament\\MaintenanceCoreFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/composer.json) · [module.json](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/module.json).

**Declared capabilities:** maintenance.core.filament

**Declared features:** Organization resource

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-maintenance-maintenance-core` | `0.1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Modules\\Maintenance\\Core\\Filament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-maintenance-maintenance-core": "0.1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/MaintenanceCoreFilamentPlugin.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/MaintenanceCoreFilamentPlugin.php) · [src/MaintenanceCoreFilamentServiceProvider.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/MaintenanceCoreFilamentServiceProvider.php) · [src/Resources/OrganizationResource.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/OrganizationResource.php) · [src/Resources/OrganizationResource/Pages/CreateOrganization.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/OrganizationResource/Pages/CreateOrganization.php) · [src/Resources/OrganizationResource/Pages/EditOrganization.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/OrganizationResource/Pages/EditOrganization.php) · [src/Resources/OrganizationResource/Pages/ListOrganizations.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/OrganizationResource/Pages/ListOrganizations.php) · [src/Resources/PriorityResource.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/PriorityResource.php) · [src/Resources/PriorityResource/Pages/CreatePriority.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/PriorityResource/Pages/CreatePriority.php) · [src/Resources/PriorityResource/Pages/EditPriority.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/PriorityResource/Pages/EditPriority.php) · [src/Resources/PriorityResource/Pages/ListPriorities.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/PriorityResource/Pages/ListPriorities.php) · [src/Resources/ServiceSettingResource.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/ServiceSettingResource.php) · [src/Resources/ServiceSettingResource/Pages/CreateServiceSetting.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/ServiceSettingResource/Pages/CreateServiceSetting.php) · [src/Resources/ServiceSettingResource/Pages/EditServiceSetting.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/ServiceSettingResource/Pages/EditServiceSetting.php) · [src/Resources/ServiceSettingResource/Pages/ListServiceSettings.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/ServiceSettingResource/Pages/ListServiceSettings.php) · [src/Resources/StatusResource.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/StatusResource.php) · [src/Resources/StatusResource/Pages/CreateStatus.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/StatusResource/Pages/CreateStatus.php) · [src/Resources/StatusResource/Pages/EditStatus.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/StatusResource/Pages/EditStatus.php) · [src/Resources/StatusResource/Pages/ListStatuses.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-core-filament/src/Resources/StatusResource/Pages/ListStatuses.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
