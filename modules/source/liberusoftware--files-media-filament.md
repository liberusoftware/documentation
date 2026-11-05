# liberusoftware/files-media-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Files and Media filament presentation adapter.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [files-media-filament](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/files-media-filament/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 0 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [files-media-filament](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/files-media-filament/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 0 |

Physical source locations: **2**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `files-media-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/files-media-filament` |
| Composer version field | `1.0.1` |
| Package type | `liberu-module` |
| Module manifest name | `files-media-filament` |
| Module version field | `1.0.1` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\FilesMediaFilament\\FilesMediaFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/files-media-filament/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/files-media-filament/module.json).

**Declared capabilities:** foundation.files-media.filament

**Declared features:** Bounded filament presentation for Files and Media, Authorization delegated to the matching core module, Accessible loading, empty, denied, and failure states

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.1` |
| `liberusoftware/files-media` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\FilesMediaFilament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/files-media": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/FilesMediaFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/files-media-filament/src/FilesMediaFilamentPlugin.php) · [src/FilesMediaFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/files-media-filament/src/FilesMediaFilamentServiceProvider.php) · [src/Pages/Overview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/files-media-filament/src/Pages/Overview.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
