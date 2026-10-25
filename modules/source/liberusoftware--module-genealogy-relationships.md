# liberusoftware/module-genealogy-relationships: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Liberu genealogy-relationships module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [genealogy-relationships](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: genealogy-laravel, `genealogy-relationships`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-genealogy-relationships` |
| Composer version field | `1.0.1` |
| Package type | `liberu-module` |
| Module manifest name | `genealogy-relationships` |
| Module version field | `1.0.1` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Genealogy\\Relationships\\RelationshipsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/composer.json) · [module.json](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/module.json).

**Declared capabilities:** genealogy.relationships, genealogy.relationships.parent, genealogy.relationships.partner, genealogy.relationships.household, genealogy.relationships.adoption, genealogy.relationships.guardianship, genealogy.relationships.uncertain, genealogy.relationships.graph-validation, genealogy.relationships.lifecycle

**Declared features:** genealogy relationships, genealogy relationships parent, genealogy relationships partner, genealogy relationships household, genealogy relationships adoption, genealogy relationships guardianship, genealogy relationships uncertain, genealogy relationships graph-validation, genealogy relationships lifecycle

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-genealogy-core` | `^1.0` |
| `liberusoftware/module-genealogy-people` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Genealogy\\Relationships\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-genealogy-core": "^1.0", "liberusoftware/module-genealogy-people": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateRelationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/CreateRelationship.php) | `public function execute(array $attributes): Relationship` |
| [src/Actions/DeleteRelationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/DeleteRelationship.php) | `public function execute(Relationship $relationship): void` |
| [src/Actions/RecordRelationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/RecordRelationship.php) | `public function execute(array $attributes): Relationship` |
| [src/Actions/UpdateRelationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Actions/UpdateRelationship.php) | `public function __construct(private readonly GraphValidator $validator)`<br>`public function execute(Relationship $relationship, array $attributes): Relationship` |
| [src/Queries/GraphValidator.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Queries/GraphValidator.php) | `public function validate(string $personId, string $relatedPersonId, string $type, ?string $ignoreRelationshipId = null): array`<br>`public function assertValid(string $personId, string $relatedPersonId, string $type, ?string $ignoreRelationshipId = null): void` |
| [src/Queries/ParentGraph.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Queries/ParentGraph.php) | `public function relatedPeople(string $teamId, array $personIds, bool $ancestors): array` |
| [src/Queries/RelationshipCalculator.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Queries/RelationshipCalculator.php) | `public function between(string $firstPersonId, string $secondPersonId, ?string $teamId = null): array` |

Other non-legacy PHP sources: [src/Capability.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Capability.php) · [src/Events/RelationshipCreated.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Events/RelationshipCreated.php) · [src/Events/RelationshipDeleted.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Events/RelationshipDeleted.php) · [src/Events/RelationshipUpdated.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Events/RelationshipUpdated.php) · [src/Listeners/ReconcilePersonMerge.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Listeners/ReconcilePersonMerge.php) · [src/Models/Relationship.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/Models/Relationship.php) · [src/RelationshipsServiceProvider.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/src/RelationshipsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000100_create_genealogy_relationships_table.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/database/migrations/2026_08_24_000100_create_genealogy_relationships_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/DomainTest.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/tests/Feature/DomainTest.php)
- [tests/Unit/CapabilityTest.php](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-relationships/tests/Unit/CapabilityTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
