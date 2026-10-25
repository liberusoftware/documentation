# liberusoftware/module-control-panel-os-adapters-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament 5 adapter for Control Panel OS Adapters.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-os-adapters-filament](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: control-panel-laravel, `control-panel-os-adapters-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-os-adapters-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-os-adapters-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\OsAdaptersFilament\\OsAdaptersFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/composer.json) · [module.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/module.json).

**Declared capabilities:** control-panel.os-adapters.filament

**Declared features:** Detection, Packages, Services, Firewall, Users, Filesystems, Repositories, Support matrix

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-control-panel-os-adapters` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\OsAdaptersFilament\\": "src/"}`.

Module resolver requirements: `{"packages": {"liberusoftware/module-control-panel-os-adapters": "^1.0"}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/OsAdaptersFilamentPlugin.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/OsAdaptersFilamentPlugin.php) · [src/OsAdaptersFilamentServiceProvider.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/OsAdaptersFilamentServiceProvider.php) · [src/Resources/FirewallRuleResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/FirewallRuleResource.php) · [src/Resources/FirewallRuleResource/Pages/CreateFirewallRule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/FirewallRuleResource/Pages/CreateFirewallRule.php) · [src/Resources/FirewallRuleResource/Pages/EditFirewallRule.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/FirewallRuleResource/Pages/EditFirewallRule.php) · [src/Resources/FirewallRuleResource/Pages/ListFirewallRules.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/FirewallRuleResource/Pages/ListFirewallRules.php) · [src/Resources/OsAdapterResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsAdapterResource.php) · [src/Resources/OsAdapterResource/Pages/CreateOsAdapter.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsAdapterResource/Pages/CreateOsAdapter.php) · [src/Resources/OsAdapterResource/Pages/EditOsAdapter.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsAdapterResource/Pages/EditOsAdapter.php) · [src/Resources/OsAdapterResource/Pages/ListOsAdapters.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsAdapterResource/Pages/ListOsAdapters.php) · [src/Resources/OsPackageResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsPackageResource.php) · [src/Resources/OsPackageResource/Pages/CreateOsPackage.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsPackageResource/Pages/CreateOsPackage.php) · [src/Resources/OsPackageResource/Pages/EditOsPackage.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsPackageResource/Pages/EditOsPackage.php) · [src/Resources/OsPackageResource/Pages/ListOsPackages.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsPackageResource/Pages/ListOsPackages.php) · [src/Resources/OsServiceResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsServiceResource.php) · [src/Resources/OsServiceResource/Pages/CreateOsService.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsServiceResource/Pages/CreateOsService.php) · [src/Resources/OsServiceResource/Pages/EditOsService.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsServiceResource/Pages/EditOsService.php) · [src/Resources/OsServiceResource/Pages/ListOsServices.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/OsServiceResource/Pages/ListOsServices.php) · [src/Resources/SupportMatrixResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/SupportMatrixResource.php) · [src/Resources/SupportMatrixResource/Pages/CreateSupportMatrix.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/SupportMatrixResource/Pages/CreateSupportMatrix.php) · [src/Resources/SupportMatrixResource/Pages/EditSupportMatrix.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/SupportMatrixResource/Pages/EditSupportMatrix.php) · [src/Resources/SupportMatrixResource/Pages/ListSupportMatrix.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-filament/src/Resources/SupportMatrixResource/Pages/ListSupportMatrix.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
