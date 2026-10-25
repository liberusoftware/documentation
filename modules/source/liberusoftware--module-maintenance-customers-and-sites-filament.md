# liberusoftware/module-maintenance-customers-and-sites-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Customers and sites Filament adapter for Liberu Maintenance

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [module-maintenance-customers-and-sites-filament](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/composer.json) | `c267d625e264` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: maintenance-laravel, `module-maintenance-customers-and-sites-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-maintenance-customers-and-sites-filament` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-maintenance-customers-and-sites-filament` |
| Module version field | `0.1.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Modules\\Maintenance\\CustomersAndSites\\Filament\\CustomersAndSitesFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/composer.json) · [module.json](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/module.json).

**Declared capabilities:** maintenance.customers-and-sites.filament

**Declared features:** Customer resource

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-maintenance-customers-and-sites` | `0.1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Modules\\Maintenance\\CustomersAndSites\\Filament\\": "src/"}`.

Module resolver requirements: `{"packages": {"liberusoftware/module-maintenance-customers-and-sites": "0.1.0"}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/CustomersAndSitesFilamentPlugin.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/CustomersAndSitesFilamentPlugin.php) · [src/CustomersAndSitesFilamentServiceProvider.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/CustomersAndSitesFilamentServiceProvider.php) · [src/Resources/CustomerResource.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/CustomerResource.php) · [src/Resources/CustomerResource/Pages/CreateCustomer.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/CustomerResource/Pages/CreateCustomer.php) · [src/Resources/CustomerResource/Pages/EditCustomer.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/CustomerResource/Pages/EditCustomer.php) · [src/Resources/CustomerResource/Pages/ListCustomers.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/CustomerResource/Pages/ListCustomers.php) · [src/Resources/SiteResource.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/SiteResource.php) · [src/Resources/SiteResource/Pages/CreateSite.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/SiteResource/Pages/CreateSite.php) · [src/Resources/SiteResource/Pages/EditSite.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/SiteResource/Pages/EditSite.php) · [src/Resources/SiteResource/Pages/ListSites.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites-filament/src/Resources/SiteResource/Pages/ListSites.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
