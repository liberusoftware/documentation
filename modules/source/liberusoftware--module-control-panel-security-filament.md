# liberusoftware/module-control-panel-security-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament 5 adapter for Control Panel Security.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-security-filament](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: control-panel-laravel, `control-panel-security-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-security-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-security-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\SecurityFilament\\SecurityFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/composer.json) · [module.json](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/module.json).

**Declared capabilities:** control-panel.security.filament

**Declared features:** Hardening, Patching, MFA and RBAC, Secrets, Malware, Intrusion controls, Fail2ban jail and ban management, Vulnerability and compliance status

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-control-panel-security` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\SecurityFilament\\": "src/"}`.

Module resolver requirements: `{"packages": {"liberusoftware/module-control-panel-security": "^1.0"}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/Resources/ComplianceStatusResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/ComplianceStatusResource.php) · [src/Resources/ComplianceStatusResource/Pages/CreateComplianceStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/ComplianceStatusResource/Pages/CreateComplianceStatus.php) · [src/Resources/ComplianceStatusResource/Pages/EditComplianceStatus.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/ComplianceStatusResource/Pages/EditComplianceStatus.php) · [src/Resources/ComplianceStatusResource/Pages/ListComplianceStatuses.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/ComplianceStatusResource/Pages/ListComplianceStatuses.php) · [src/Resources/HardeningControlResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/HardeningControlResource.php) · [src/Resources/HardeningControlResource/Pages/CreateHardeningControl.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/HardeningControlResource/Pages/CreateHardeningControl.php) · [src/Resources/HardeningControlResource/Pages/EditHardeningControl.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/HardeningControlResource/Pages/EditHardeningControl.php) · [src/Resources/HardeningControlResource/Pages/ListHardeningControls.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/HardeningControlResource/Pages/ListHardeningControls.php) · [src/Resources/IntrusionControlResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/IntrusionControlResource.php) · [src/Resources/IntrusionControlResource/Pages/ListIntrusionControls.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/IntrusionControlResource/Pages/ListIntrusionControls.php) · [src/Resources/MalwareScanResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/MalwareScanResource.php) · [src/Resources/MalwareScanResource/Pages/ListMalwareScans.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/MalwareScanResource/Pages/ListMalwareScans.php) · [src/Resources/MfaRbacPolicyResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/MfaRbacPolicyResource.php) · [src/Resources/MfaRbacPolicyResource/Pages/ListMfaRbacPolicies.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/MfaRbacPolicyResource/Pages/ListMfaRbacPolicies.php) · [src/Resources/PatchRecordResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/PatchRecordResource.php) · [src/Resources/PatchRecordResource/Pages/ListPatchRecords.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/PatchRecordResource/Pages/ListPatchRecords.php) · [src/Resources/SecretRecordResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/SecretRecordResource.php) · [src/Resources/SecretRecordResource/Pages/ListSecretRecords.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/SecretRecordResource/Pages/ListSecretRecords.php) · [src/Resources/SecurityFindingResource.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/SecurityFindingResource.php) · [src/Resources/SecurityFindingResource/Pages/CreateSecurityFinding.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/SecurityFindingResource/Pages/CreateSecurityFinding.php) · [src/Resources/SecurityFindingResource/Pages/EditSecurityFinding.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/SecurityFindingResource/Pages/EditSecurityFinding.php) · [src/Resources/SecurityFindingResource/Pages/ListSecurityFindings.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/Resources/SecurityFindingResource/Pages/ListSecurityFindings.php) · [src/SecurityFilamentPlugin.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/SecurityFilamentPlugin.php) · [src/SecurityFilamentServiceProvider.php](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-filament/src/SecurityFilamentServiceProvider.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
