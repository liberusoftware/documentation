# liberusoftware/module-control-panel-mail-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament 5 adapter for Control Panel Mail.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [control-panel-mail-filament](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-control-panel-laravel-filament, `control-panel-mail-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-control-panel-mail-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `control-panel-mail-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\ControlPanel\\MailFilament\\MailFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/composer.json) · [module.json](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/module.json).

**Declared capabilities:** control-panel.mail.filament

**Declared features:** Mail domains, Mailboxes, Aliases, Routing, Quotas, Spam and virus controls, DKIM, SPF, DMARC, Delivery diagnostics

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-control-panel-mail` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\ControlPanel\\MailFilament\\": "src/"}`.

Module resolver requirements: `{"packages": {"liberusoftware/module-control-panel-mail": "^1.0"}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/MailFilamentPlugin.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/MailFilamentPlugin.php) · [src/MailFilamentServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/MailFilamentServiceProvider.php) · [src/Resources/DeliveryDiagnosticResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/DeliveryDiagnosticResource.php) · [src/Resources/DeliveryDiagnosticResource/Pages/ListDeliveryDiagnostics.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/DeliveryDiagnosticResource/Pages/ListDeliveryDiagnostics.php) · [src/Resources/DkimKeyResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/DkimKeyResource.php) · [src/Resources/DkimKeyResource/Pages/CreateDkimKey.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/DkimKeyResource/Pages/CreateDkimKey.php) · [src/Resources/DkimKeyResource/Pages/ListDkimKeys.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/DkimKeyResource/Pages/ListDkimKeys.php) · [src/Resources/MailAccountResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailAccountResource.php) · [src/Resources/MailAccountResource/Pages/CreateMailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailAccountResource/Pages/CreateMailAccount.php) · [src/Resources/MailAccountResource/Pages/EditMailAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailAccountResource/Pages/EditMailAccount.php) · [src/Resources/MailAccountResource/Pages/ListMailAccounts.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailAccountResource/Pages/ListMailAccounts.php) · [src/Resources/MailAliasResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailAliasResource.php) · [src/Resources/MailAliasResource/Pages/CreateMailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailAliasResource/Pages/CreateMailAlias.php) · [src/Resources/MailAliasResource/Pages/EditMailAlias.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailAliasResource/Pages/EditMailAlias.php) · [src/Resources/MailAliasResource/Pages/ListMailAliases.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailAliasResource/Pages/ListMailAliases.php) · [src/Resources/MailControlResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailControlResource.php) · [src/Resources/MailControlResource/Pages/ListMailControls.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailControlResource/Pages/ListMailControls.php) · [src/Resources/MailDomainResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailDomainResource.php) · [src/Resources/MailDomainResource/Pages/CreateMailDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailDomainResource/Pages/CreateMailDomain.php) · [src/Resources/MailDomainResource/Pages/EditMailDomain.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailDomainResource/Pages/EditMailDomain.php) · [src/Resources/MailDomainResource/Pages/ListMailDomains.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailDomainResource/Pages/ListMailDomains.php) · [src/Resources/MailFeatureResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailFeatureResource.php) · [src/Resources/MailOperationResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailOperationResource.php) · [src/Resources/MailOperationResource/Pages/ListMailOperations.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailOperationResource/Pages/ListMailOperations.php) · [src/Resources/MailRouteResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailRouteResource.php) · [src/Resources/MailRouteResource/Pages/CreateMailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailRouteResource/Pages/CreateMailRoute.php) · [src/Resources/MailRouteResource/Pages/EditMailRoute.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailRouteResource/Pages/EditMailRoute.php) · [src/Resources/MailRouteResource/Pages/ListMailRoutes.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-mail-filament/src/Resources/MailRouteResource/Pages/ListMailRoutes.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
