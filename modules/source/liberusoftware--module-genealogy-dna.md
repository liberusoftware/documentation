# liberusoftware/module-genealogy-dna: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Liberu genealogy-dna module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [genealogy-dna](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: genealogy-laravel, `genealogy-dna`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-genealogy-dna` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `genealogy-dna` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Genealogy\\Dna\\DnaServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/composer.json) · [module.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/module.json).

**Declared capabilities:** genealogy.dna, genealogy.dna.kits, genealogy.dna.providers, genealogy.dna.consent, genealogy.dna.match-segments, genealogy.dna.relationships, genealogy.dna.groups, genealogy.dna.notes, genealogy.dna.revocation, genealogy.dna.lifecycle

**Declared features:** genealogy dna, genealogy dna kits, genealogy dna providers, genealogy dna consent, genealogy dna match-segments, genealogy dna relationships, genealogy dna groups, genealogy dna notes, genealogy dna revocation, genealogy dna lifecycle

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/encryption` | `^13.0` |
| `illuminate/filesystem` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-genealogy-core` | `^1.0` |
| `liberusoftware/module-genealogy-people` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Genealogy\\Dna\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-genealogy-core": "^1.0", "liberusoftware/module-genealogy-people": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateDnaGroup.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaGroup.php) | `public function execute(array $attributes): DnaGroup`<br>`public function validate(array $values): void` |
| [src/Actions/CreateDnaKit.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaKit.php) | `public function execute(array $attributes): DnaKit` |
| [src/Actions/CreateDnaMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaMatch.php) | `public function execute(array $attributes): DnaMatch` |
| [src/Actions/CreateDnaNote.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaNote.php) | `public function execute(array $attributes): DnaNote` |
| [src/Actions/CreateDnaProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaProvider.php) | `public function execute(array $attributes): DnaProvider` |
| [src/Actions/CreateDnaRelationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaRelationship.php) | `public function execute(array $attributes): DnaRelationship` |
| [src/Actions/CreateDnaSegment.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/CreateDnaSegment.php) | `public function execute(array $attributes): DnaSegment` |
| [src/Actions/DeleteDnaGroup.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaGroup.php) | `public function execute(DnaGroup $group): void` |
| [src/Actions/DeleteDnaKit.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaKit.php) | `public function __construct(private readonly DnaFileVault $vault)`<br>`public function execute(DnaKit $kit): void` |
| [src/Actions/DeleteDnaMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaMatch.php) | `public function execute(DnaMatch $match): void` |
| [src/Actions/DeleteDnaNote.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaNote.php) | `public function execute(DnaNote $note): void` |
| [src/Actions/DeleteDnaProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaProvider.php) | `public function execute(DnaProvider $provider): void` |
| [src/Actions/DeleteDnaRelationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaRelationship.php) | `public function execute(DnaRelationship $relationship): void` |
| [src/Actions/DeleteDnaSegment.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/DeleteDnaSegment.php) | `public function execute(DnaSegment $segment): void` |
| [src/Actions/GrantDnaConsent.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/GrantDnaConsent.php) | `public function execute(DnaKit $kit, string $scope, ?string $policyVersion = null): DnaConsent` |
| [src/Actions/ImportDnaKit.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/ImportDnaKit.php) | `public function __construct( private readonly DnaFileValidator $validator, private readonly DnaFileVault $vault, )`<br>`public function execute(string $content, array $attributes): DnaKit` |
| [src/Actions/PersistDnaComparison.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/PersistDnaComparison.php) | `public function __construct( private readonly CompareDnaKits $compare, private readonly CreateDnaMatch $createMatch, private readonly CreateDnaSegment $createSegment, )`<br>`public function execute(DnaKit $kitA, DnaKit $kitB): array` |
| [src/Actions/RevokeDnaKit.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/RevokeDnaKit.php) | `public function execute(DnaKit $kit, string $reason): DnaKit` |
| [src/Actions/UpdateDnaGroup.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/UpdateDnaGroup.php) | `public function execute(DnaGroup $group, array $attributes): DnaGroup` |
| [src/Actions/UpdateDnaKit.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/UpdateDnaKit.php) | `public function execute(DnaKit $kit, array $attributes): DnaKit` |
| [src/Actions/UpdateDnaMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/UpdateDnaMatch.php) | `public function execute(DnaMatch $match, array $attributes): DnaMatch` |
| [src/Actions/UpdateDnaProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/UpdateDnaProvider.php) | `public function execute(DnaProvider $provider, array $attributes): DnaProvider` |
| [src/Actions/UpdateDnaRelationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/UpdateDnaRelationship.php) | `public function execute(DnaRelationship $relationship, array $attributes): DnaRelationship` |
| [src/Actions/UpdateDnaSegment.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Actions/UpdateDnaSegment.php) | `public function execute(DnaSegment $segment, array $attributes): DnaSegment` |
| [src/Services/AnalyzeDnaMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/AnalyzeDnaMatch.php) | `public function __construct( private readonly SegmentMatcher $segments, private readonly RelationshipEstimator $relationships, )`<br>`public function analyze(array $kitA, array $kitB): array` |
| [src/Services/CompareDnaKits.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/CompareDnaKits.php) | `public function __construct( private readonly ParseDnaFile $parser, private readonly DnaFileVault $vault, private readonly AnalyzeDnaMatch $analyzer, )`<br>`public function execute(DnaKit $kitA, DnaKit $kitB): array` |
| [src/Services/DnaFileValidator.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/DnaFileValidator.php) | `public function validate(string $content): array`<br>`public function detectFormat(string $firstLine, string $secondLine = ''): ?string` |
| [src/Services/DnaFileVault.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/DnaFileVault.php) | `public function encrypt(string $plaintext): string`<br>`public function decrypt(string $ciphertext): string`<br>`public function store(string $plaintext, string $path, string $disk = 'private'): void`<br>`public function read(string $path, string $disk = 'private'): string`<br>`public function delete(string $path, string $disk = 'private'): void` |
| [src/Services/ParseDnaFile.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/ParseDnaFile.php) | `public function parse(string $content): array` |
| [src/Services/RelationshipEstimator.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/RelationshipEstimator.php) | `public static function labels(): array`<br>`public function estimate(float $totalSharedCm): array` |
| [src/Services/SegmentMatcher.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/SegmentMatcher.php) | `public function match(array $kitA, array $kitB): array` |
| [src/Services/TriangulateDna.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Services/TriangulateDna.php) | `public function execute(array $matches, float $minimumSharedCm = 20.0): array` |

Other non-legacy PHP sources: [src/Capability.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Capability.php) · [src/DnaServiceProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/DnaServiceProvider.php) · [src/Events/DnaMatchesPersisted.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Events/DnaMatchesPersisted.php) · [src/Listeners/ReconcilePersonMerge.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Listeners/ReconcilePersonMerge.php) · [src/Models/DnaConsent.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaConsent.php) · [src/Models/DnaGroup.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaGroup.php) · [src/Models/DnaKit.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaKit.php) · [src/Models/DnaMatch.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaMatch.php) · [src/Models/DnaNote.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaNote.php) · [src/Models/DnaProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaProvider.php) · [src/Models/DnaRelationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaRelationship.php) · [src/Models/DnaSegment.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/src/Models/DnaSegment.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_010000_create_genealogy_dna_kits_table.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/database/migrations/2026_08_24_010000_create_genealogy_dna_kits_table.php)
- [database/migrations/2026_08_24_020000_add_dna_kit_semantics.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/database/migrations/2026_08_24_020000_add_dna_kit_semantics.php)
- [database/migrations/2026_08_24_020001_create_dna_records.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/database/migrations/2026_08_24_020001_create_dna_records.php)
- [database/migrations/2026_08_25_090000_create_genealogy_dna_providers_table.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/database/migrations/2026_08_25_090000_create_genealogy_dna_providers_table.php)
- [database/migrations/2026_08_25_100000_add_dna_kit_file_metadata.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/database/migrations/2026_08_25_100000_add_dna_kit_file_metadata.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/DomainTest.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/tests/Feature/DomainTest.php)
- [tests/Unit/CapabilityTest.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-dna/tests/Unit/CapabilityTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
