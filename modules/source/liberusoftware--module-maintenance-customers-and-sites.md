# liberusoftware/module-maintenance-customers-and-sites: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Customers and sites domain module for Liberu Maintenance

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [module-maintenance-customers-and-sites](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/composer.json) | `c267d625e264` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-maintenance-laravel-filament, `module-maintenance-customers-and-sites`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-maintenance-customers-and-sites` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-maintenance-customers-and-sites` |
| Module version field | `0.1.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Modules\\Maintenance\\CustomersAndSites\\CustomersAndSitesServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/composer.json) · [module.json](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/module.json).

**Declared capabilities:** maintenance.customers-and-sites

**Declared features:** Customers, Contacts, Sites, Locations, Access details, Hazards, Service windows

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-maintenance-maintenance-core` | `0.1.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Modules\\Maintenance\\CustomersAndSites\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-maintenance-maintenance-core": "0.1.0", "liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateCustomer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/CreateCustomer.php) | `public function handle(int $teamId, array $attributes): Customer` |
| [src/Actions/CreateSite.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/CreateSite.php) | `public function handle(int $teamId, array $attributes): Site` |
| [src/Actions/DeleteCustomer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/DeleteCustomer.php) | `public function handle(int $teamId, Customer $customer): void` |
| [src/Actions/DeleteSite.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/DeleteSite.php) | `public function handle(int $teamId, Site $site): void` |
| [src/Actions/UpdateCustomer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/UpdateCustomer.php) | `public function handle(int $teamId, Customer $customer, array $attributes): Customer` |
| [src/Actions/UpdateSite.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Actions/UpdateSite.php) | `public function handle(int $teamId, Site $site, array $attributes): Site` |
| [src/Policies/CustomerPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Policies/CustomerPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Customer $customer): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Customer $customer): bool`<br>`public function delete(object $user, Customer $customer): bool` |
| [src/Policies/SitePolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Policies/SitePolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Site $site): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Site $site): bool`<br>`public function delete(object $user, Site $site): bool` |

Other non-legacy PHP sources: [src/CustomersAndSitesServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/CustomersAndSitesServiceProvider.php) · [src/Models/Customer.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Models/Customer.php) · [src/Models/Site.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/src/Models/Site.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_010000_create_maintenance_customers_and_sites_tables.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/database/migrations/2026_08_25_010000_create_maintenance_customers_and_sites_tables.php)
- [database/migrations/2026_08_29_211000_add_legacy_customer_profile_fields.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-customers-and-sites/database/migrations/2026_08_29_211000_add_legacy_customer_profile_fields.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
