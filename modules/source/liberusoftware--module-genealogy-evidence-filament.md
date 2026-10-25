# liberusoftware/module-genealogy-evidence-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Liberu genealogy-evidence-filament module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [genealogy-evidence-filament](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: genealogy-laravel, `genealogy-evidence-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-genealogy-evidence-filament` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `genealogy-evidence-filament` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Genealogy\\Evidence\\Filament\\EvidenceFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/composer.json) · [module.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/module.json).

**Declared capabilities:** genealogy.evidence.filament

**Declared features:** filament presentation for evidence

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.0` |
| `liberusoftware/module-genealogy-evidence` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Genealogy\\Evidence\\Filament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-genealogy-evidence": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/EvidenceFilamentServiceProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/EvidenceFilamentServiceProvider.php) · [src/Resources/AssertionResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/AssertionResource.php) · [src/Resources/AssertionResource/Pages/CreateAssertion.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/AssertionResource/Pages/CreateAssertion.php) · [src/Resources/AssertionResource/Pages/EditAssertion.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/AssertionResource/Pages/EditAssertion.php) · [src/Resources/AssertionResource/Pages/ListAssertions.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/AssertionResource/Pages/ListAssertions.php) · [src/Resources/CitationResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/CitationResource.php) · [src/Resources/CitationResource/Pages/CreateCitation.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/CitationResource/Pages/CreateCitation.php) · [src/Resources/CitationResource/Pages/EditCitation.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/CitationResource/Pages/EditCitation.php) · [src/Resources/CitationResource/Pages/ListCitations.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/CitationResource/Pages/ListCitations.php) · [src/Resources/CitationResource/RelationManagers/PersonLinksRelationManager.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/CitationResource/RelationManagers/PersonLinksRelationManager.php) · [src/Resources/EvidenceEntityResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/EvidenceEntityResource.php) · [src/Resources/EvidenceRecordResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/EvidenceRecordResource.php) · [src/Resources/EvidenceRecordResource/Pages/CreateEvidenceRecord.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/EvidenceRecordResource/Pages/CreateEvidenceRecord.php) · [src/Resources/EvidenceRecordResource/Pages/EditEvidenceRecord.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/EvidenceRecordResource/Pages/EditEvidenceRecord.php) · [src/Resources/EvidenceRecordResource/Pages/ListEvidenceRecords.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/EvidenceRecordResource/Pages/ListEvidenceRecords.php) · [src/Resources/ExtractResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/ExtractResource.php) · [src/Resources/ExtractResource/Pages/CreateExtract.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/ExtractResource/Pages/CreateExtract.php) · [src/Resources/ExtractResource/Pages/EditExtract.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/ExtractResource/Pages/EditExtract.php) · [src/Resources/ExtractResource/Pages/ListExtracts.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/ExtractResource/Pages/ListExtracts.php) · [src/Resources/Pages/CreateEvidenceEntityRecord.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/Pages/CreateEvidenceEntityRecord.php) · [src/Resources/Pages/EditEvidenceEntityRecord.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/Pages/EditEvidenceEntityRecord.php) · [src/Resources/Pages/ListEvidenceEntities.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/Pages/ListEvidenceEntities.php) · [src/Resources/ProofConclusionResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/ProofConclusionResource.php) · [src/Resources/ProofConclusionResource/Pages/CreateProofConclusion.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/ProofConclusionResource/Pages/CreateProofConclusion.php) · [src/Resources/ProofConclusionResource/Pages/EditProofConclusion.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/ProofConclusionResource/Pages/EditProofConclusion.php) · [src/Resources/ProofConclusionResource/Pages/ListProofConclusions.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/ProofConclusionResource/Pages/ListProofConclusions.php) · [src/Resources/RepositoryResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/RepositoryResource.php) · [src/Resources/RepositoryResource/Pages/CreateRepository.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/RepositoryResource/Pages/CreateRepository.php) · [src/Resources/RepositoryResource/Pages/EditRepository.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/RepositoryResource/Pages/EditRepository.php) · [src/Resources/RepositoryResource/Pages/ListRepositories.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/RepositoryResource/Pages/ListRepositories.php) · [src/Resources/SourceResource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/SourceResource.php) · [src/Resources/SourceResource/Pages/CreateSource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/SourceResource/Pages/CreateSource.php) · [src/Resources/SourceResource/Pages/EditSource.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/SourceResource/Pages/EditSource.php) · [src/Resources/SourceResource/Pages/ListSources.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/src/Resources/SourceResource/Pages/ListSources.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Unit/BoundaryTest.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-evidence-filament/tests/Unit/BoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
