# liberusoftware/module-crm-documents-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-documents-filament](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents-filament/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `crm-documents-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-documents-filament` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `module-crm-documents-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\CRM\\DocumentsFilament\\DocumentsFilamentServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\DocumentsFilament\\DocumentsFilamentServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents-filament/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents-filament/module.json).

**Declared capabilities:** crm.documents.filament

**Declared features:** Document resource

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\DocumentsFilament\\": "src/"}`.

Module resolver requirements: `{"modules": ["crm-documents"]}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/DocumentsFilamentServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents-filament/src/DocumentsFilamentServiceProvider.php) · [src/Resources/CrmDocumentResource.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents-filament/src/Resources/CrmDocumentResource.php) · [src/Resources/Pages/CreateCrmDocument.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents-filament/src/Resources/Pages/CreateCrmDocument.php) · [src/Resources/Pages/EditCrmDocument.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents-filament/src/Resources/Pages/EditCrmDocument.php) · [src/Resources/Pages/ListCrmDocuments.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-documents-filament/src/Resources/Pages/ListCrmDocuments.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
