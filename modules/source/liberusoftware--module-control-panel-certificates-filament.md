# liberusoftware/module-control-panel-certificates-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament adapter for Control Panel Certificates.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-certificates-filament](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: control-panel-laravel, `control-panel-certificates-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-certificates-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-certificates-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\CertificatesFilament\\CertificatesFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/composer.json) · [module.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/module.json).

**Declared capabilities:** control-panel.certificates.filament

**Declared features:** ACME accounts, Certificate issuance, Certificate deployment, Certificate renewal, Certificate revocation, Expiry monitoring

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-control-panel-certificates` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\CertificatesFilament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-control-panel-certificates": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/CertificatesFilamentPlugin.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/CertificatesFilamentPlugin.php) · [src/CertificatesFilamentServiceProvider.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/CertificatesFilamentServiceProvider.php) · [src/Resources/AcmeAccountResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/AcmeAccountResource.php) · [src/Resources/AcmeAccountResource/Pages/ListAcmeAccounts.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/AcmeAccountResource/Pages/ListAcmeAccounts.php) · [src/Resources/CertificateDeploymentResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/CertificateDeploymentResource.php) · [src/Resources/CertificateDeploymentResource/Pages/ListCertificateDeployments.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/CertificateDeploymentResource/Pages/ListCertificateDeployments.php) · [src/Resources/CertificateExpiryAlertResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/CertificateExpiryAlertResource.php) · [src/Resources/CertificateExpiryAlertResource/Pages/ListCertificateExpiryAlerts.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/CertificateExpiryAlertResource/Pages/ListCertificateExpiryAlerts.php) · [src/Resources/CertificateLifecycleResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/CertificateLifecycleResource.php) · [src/Resources/CertificateOperationResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/CertificateOperationResource.php) · [src/Resources/CertificateOperationResource/Pages/ListCertificateOperations.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/CertificateOperationResource/Pages/ListCertificateOperations.php) · [src/Resources/CertificateRenewalResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/CertificateRenewalResource.php) · [src/Resources/CertificateRenewalResource/Pages/ListCertificateRenewals.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/CertificateRenewalResource/Pages/ListCertificateRenewals.php) · [src/Resources/CertificateResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/CertificateResource.php) · [src/Resources/CertificateResource/Pages/CreateCertificate.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/CertificateResource/Pages/CreateCertificate.php) · [src/Resources/CertificateResource/Pages/EditCertificate.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/CertificateResource/Pages/EditCertificate.php) · [src/Resources/CertificateResource/Pages/ListCertificates.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-certificates-filament/src/Resources/CertificateResource/Pages/ListCertificates.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
