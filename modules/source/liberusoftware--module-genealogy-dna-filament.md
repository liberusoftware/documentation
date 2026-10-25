# liberusoftware/module-genealogy-dna-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Liberu genealogy-dna-filament module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [genealogy-dna-filament](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: genealogy-laravel, `genealogy-dna-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-genealogy-dna-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `genealogy-dna-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Genealogy\\Dna\\Filament\\DnaFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/composer.json) · [module.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/module.json).

**Declared capabilities:** genealogy.dna.filament

**Declared features:** filament presentation for dna

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-genealogy-dna` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Genealogy\\Dna\\Filament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-genealogy-dna": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/DnaFilamentServiceProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/DnaFilamentServiceProvider.php) · [src/Resources/DnaConsentResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaConsentResource.php) · [src/Resources/DnaConsentResource/Pages/ListDnaConsents.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaConsentResource/Pages/ListDnaConsents.php) · [src/Resources/DnaGroupResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaGroupResource.php) · [src/Resources/DnaGroupResource/Pages/CreateDnaGroup.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaGroupResource/Pages/CreateDnaGroup.php) · [src/Resources/DnaGroupResource/Pages/EditDnaGroup.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaGroupResource/Pages/EditDnaGroup.php) · [src/Resources/DnaGroupResource/Pages/ListDnaGroups.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaGroupResource/Pages/ListDnaGroups.php) · [src/Resources/DnaKitResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaKitResource.php) · [src/Resources/DnaKitResource/Pages/CreateDnaKit.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaKitResource/Pages/CreateDnaKit.php) · [src/Resources/DnaKitResource/Pages/EditDnaKit.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaKitResource/Pages/EditDnaKit.php) · [src/Resources/DnaKitResource/Pages/ListDnaKits.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaKitResource/Pages/ListDnaKits.php) · [src/Resources/DnaMatchResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaMatchResource.php) · [src/Resources/DnaMatchResource/Pages/CreateDnaMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaMatchResource/Pages/CreateDnaMatch.php) · [src/Resources/DnaMatchResource/Pages/EditDnaMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaMatchResource/Pages/EditDnaMatch.php) · [src/Resources/DnaMatchResource/Pages/ListDnaMatches.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaMatchResource/Pages/ListDnaMatches.php) · [src/Resources/DnaNoteResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaNoteResource.php) · [src/Resources/DnaNoteResource/Pages/CreateDnaNote.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaNoteResource/Pages/CreateDnaNote.php) · [src/Resources/DnaNoteResource/Pages/ListDnaNotes.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaNoteResource/Pages/ListDnaNotes.php) · [src/Resources/DnaProviderResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaProviderResource.php) · [src/Resources/DnaProviderResource/Pages/CreateDnaProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaProviderResource/Pages/CreateDnaProvider.php) · [src/Resources/DnaProviderResource/Pages/EditDnaProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaProviderResource/Pages/EditDnaProvider.php) · [src/Resources/DnaProviderResource/Pages/ListDnaProviders.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaProviderResource/Pages/ListDnaProviders.php) · [src/Resources/DnaRelationshipResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaRelationshipResource.php) · [src/Resources/DnaRelationshipResource/Pages/CreateDnaRelationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaRelationshipResource/Pages/CreateDnaRelationship.php) · [src/Resources/DnaRelationshipResource/Pages/EditDnaRelationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaRelationshipResource/Pages/EditDnaRelationship.php) · [src/Resources/DnaRelationshipResource/Pages/ListDnaRelationships.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaRelationshipResource/Pages/ListDnaRelationships.php) · [src/Resources/DnaSegmentResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaSegmentResource.php) · [src/Resources/DnaSegmentResource/Pages/CreateDnaSegment.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaSegmentResource/Pages/CreateDnaSegment.php) · [src/Resources/DnaSegmentResource/Pages/EditDnaSegment.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaSegmentResource/Pages/EditDnaSegment.php) · [src/Resources/DnaSegmentResource/Pages/ListDnaSegments.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/src/Resources/DnaSegmentResource/Pages/ListDnaSegments.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Unit/BoundaryTest.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna-filament/tests/Unit/BoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
