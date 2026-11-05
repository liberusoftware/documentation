# liberusoftware/module-control-panel-dns-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament adapter for Control Panel DNS.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-dns-filament](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-control-panel-laravel-filament, `control-panel-dns-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-dns-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-dns-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\DnsFilament\\DnsFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/composer.json) · [module.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/module.json).

**Declared capabilities:** control-panel.dns.filament

**Declared features:** DNS zones, DNS records, DNS templates, DNSSEC, Validation, Providers, Propagation checks

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-control-panel-dns` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\DnsFilament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-control-panel-dns": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/DnsFilamentPlugin.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/DnsFilamentPlugin.php) · [src/DnsFilamentServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/DnsFilamentServiceProvider.php) · [src/Resources/DnsCheckResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/DnsCheckResource.php) · [src/Resources/DnsCheckResource/Pages/CreateDnsCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/DnsCheckResource/Pages/CreateDnsCheck.php) · [src/Resources/DnsCheckResource/Pages/EditDnsCheck.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/DnsCheckResource/Pages/EditDnsCheck.php) · [src/Resources/DnsCheckResource/Pages/ListDnsChecks.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/DnsCheckResource/Pages/ListDnsChecks.php) · [src/Resources/DnsFeatureResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/DnsFeatureResource.php) · [src/Resources/DnsProviderResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/DnsProviderResource.php) · [src/Resources/DnsProviderResource/Pages/ListDnsProviders.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/DnsProviderResource/Pages/ListDnsProviders.php) · [src/Resources/DnsTemplateResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/DnsTemplateResource.php) · [src/Resources/DnsTemplateResource/Pages/ListDnsTemplates.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/DnsTemplateResource/Pages/ListDnsTemplates.php) · [src/Resources/DnsValidationResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/DnsValidationResource.php) · [src/Resources/DnsValidationResource/Pages/ListDnsValidations.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/DnsValidationResource/Pages/ListDnsValidations.php) · [src/Resources/DnssecResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/DnssecResource.php) · [src/Resources/DnssecResource/Pages/ListDnssecKeys.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/DnssecResource/Pages/ListDnssecKeys.php) · [src/Resources/PropagationResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/PropagationResource.php) · [src/Resources/PropagationResource/Pages/ListPropagationChecks.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/PropagationResource/Pages/ListPropagationChecks.php) · [src/Resources/RecordResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/RecordResource.php) · [src/Resources/RecordResource/Pages/CreateRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/RecordResource/Pages/CreateRecord.php) · [src/Resources/RecordResource/Pages/EditRecord.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/RecordResource/Pages/EditRecord.php) · [src/Resources/RecordResource/Pages/ListRecords.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/RecordResource/Pages/ListRecords.php) · [src/Resources/ZoneResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/ZoneResource.php) · [src/Resources/ZoneResource/Pages/CreateZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/ZoneResource/Pages/CreateZone.php) · [src/Resources/ZoneResource/Pages/EditZone.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/ZoneResource/Pages/EditZone.php) · [src/Resources/ZoneResource/Pages/ListZones.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-dns-filament/src/Resources/ZoneResource/Pages/ListZones.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
