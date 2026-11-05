# liberusoftware/real-estate-lettings: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral letting lifecycle and operational records.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [real-estate-lettings](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-real-estate-laravel-filament, `real-estate-lettings`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/real-estate-lettings` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `real-estate-lettings` |
| Module version field | `1.0.0` |
| Category / layers | `"product"` |
| Manifest provider(s) | `"Liberu\\RealEstate\\Lettings\\LettingsServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\RealEstate\\Lettings\\LettingsServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/composer.json) · [module.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/module.json).

**Declared capabilities:** real-estate.lettings

**Declared features:** Applications, Referencing, Deposits, Agreements, Move-in/out, Renewals, Rent changes, Notices, Tenancy agreement lifecycle, Recurring rental charges

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/validation` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\RealEstate\\Lettings\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Policies/LettingPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Policies/LettingPolicy.php) | `public function view($user, Letting $letting): bool`<br>`public function update($user, Letting $letting): bool`<br>`public function delete($user, Letting $letting): bool` |
| [src/Queries/ListLettings.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Queries/ListLettings.php) | `public function handle(int\|string $teamId, ?string $capability = null, int $perPage = 25): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/Application/CreateLeaseAgreement.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Application/CreateLeaseAgreement.php) · [src/Application/CreateLetting.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Application/CreateLetting.php) · [src/Application/CreateRentalApplication.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Application/CreateRentalApplication.php) · [src/Application/CreateRentalCharge.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Application/CreateRentalCharge.php) · [src/Application/DecideRentalApplication.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Application/DecideRentalApplication.php) · [src/Application/RecordLettingFailure.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Application/RecordLettingFailure.php) · [src/Application/RenewLeaseAgreement.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Application/RenewLeaseAgreement.php) · [src/Application/ServeLeaseNotice.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Application/ServeLeaseNotice.php) · [src/Application/TransitionLetting.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Application/TransitionLetting.php) · [src/Application/UpdateLetting.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Application/UpdateLetting.php) · [src/Application/UpdateLettingDetails.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Application/UpdateLettingDetails.php) · [src/Application/UpdateRentalApplicationScreening.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Application/UpdateRentalApplicationScreening.php) · [src/Application/UpdateRentalCharge.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Application/UpdateRentalCharge.php) · [src/Domain/Events/LettingCreated.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Domain/Events/LettingCreated.php) · [src/Domain/Events/LettingStatusChanged.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Domain/Events/LettingStatusChanged.php) · [src/Domain/LeaseAgreementStatus.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Domain/LeaseAgreementStatus.php) · [src/Domain/LettingCapability.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Domain/LettingCapability.php) · [src/Domain/LettingCapabilityDefinition.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Domain/LettingCapabilityDefinition.php) · [src/Domain/LettingStatus.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Domain/LettingStatus.php) · [src/Domain/RentalApplicationStatus.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Domain/RentalApplicationStatus.php) · [src/Domain/RentalChargeStatus.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Domain/RentalChargeStatus.php) · [src/LettingsServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/LettingsServiceProvider.php) · [src/Models/LeaseAgreement.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/LeaseAgreement.php) · [src/Models/Letting.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/Letting.php) · [src/Models/RentalApplication.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/RentalApplication.php) · [src/Models/RentalCharge.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/RentalCharge.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_23_000020_create_real_estate_lettings_table.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/database/migrations/2026_08_23_000020_create_real_estate_lettings_table.php)
- [database/migrations/2026_08_30_000006_create_real_estate_rental_applications.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/database/migrations/2026_08_30_000006_create_real_estate_rental_applications.php)
- [database/migrations/2026_08_30_000009_create_real_estate_lease_agreements.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/database/migrations/2026_08_30_000009_create_real_estate_lease_agreements.php)
- [database/migrations/2026_08_30_000010_create_real_estate_rental_charges.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/database/migrations/2026_08_30_000010_create_real_estate_rental_charges.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
