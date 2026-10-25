# liberusoftware/module-billing-communications-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament adapter for Billing Communications.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-billing-communications-filament](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: billing-laravel, `module-billing-communications-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-billing-communications-filament` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-billing-communications-filament` |
| Module version field | `0.1.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Billing\\Communications\\Filament\\CommunicationsFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/composer.json) · [module.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/module.json).

**Declared capabilities:** billing.communications.filament

**Declared features:** Communications Filament integration

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `~5.1` |
| `liberusoftware/module-billing-communications` | `^0.1` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Billing\\Communications\\Filament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-billing-communications": "^0.1", "liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/CommunicationsFilamentPlugin.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/CommunicationsFilamentPlugin.php) · [src/CommunicationsFilamentServiceProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/CommunicationsFilamentServiceProvider.php) · [src/Concerns/ScopesCurrentTeam.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Concerns/ScopesCurrentTeam.php) · [src/Resources/CommunicationNumberResource.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/CommunicationNumberResource.php) · [src/Resources/CommunicationNumberResource/Pages/CreateCommunicationNumber.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/CommunicationNumberResource/Pages/CreateCommunicationNumber.php) · [src/Resources/CommunicationNumberResource/Pages/ListCommunicationNumbers.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/CommunicationNumberResource/Pages/ListCommunicationNumbers.php) · [src/Resources/CommunicationProviderResource.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/CommunicationProviderResource.php) · [src/Resources/CommunicationProviderResource/Pages/CreateCommunicationProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/CommunicationProviderResource/Pages/CreateCommunicationProvider.php) · [src/Resources/CommunicationProviderResource/Pages/ListCommunicationProviders.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/CommunicationProviderResource/Pages/ListCommunicationProviders.php) · [src/Resources/CommunicationServiceResource.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/CommunicationServiceResource.php) · [src/Resources/CommunicationServiceResource/Pages/CreateCommunicationService.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/CommunicationServiceResource/Pages/CreateCommunicationService.php) · [src/Resources/CommunicationServiceResource/Pages/ListCommunicationServices.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/CommunicationServiceResource/Pages/ListCommunicationServices.php) · [src/Resources/CommunicationUsageImportResource.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/CommunicationUsageImportResource.php) · [src/Resources/CommunicationUsageImportResource/Pages/CreateCommunicationUsageImport.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/CommunicationUsageImportResource/Pages/CreateCommunicationUsageImport.php) · [src/Resources/CommunicationUsageImportResource/Pages/ListCommunicationUsageImports.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/CommunicationUsageImportResource/Pages/ListCommunicationUsageImports.php) · [src/Resources/VoipAccountResource.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/VoipAccountResource.php) · [src/Resources/VoipAccountResource/Pages/CreateVoipAccount.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/VoipAccountResource/Pages/CreateVoipAccount.php) · [src/Resources/VoipAccountResource/Pages/ListVoipAccounts.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-filament/src/Resources/VoipAccountResource/Pages/ListVoipAccounts.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
