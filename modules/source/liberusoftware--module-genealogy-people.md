# liberusoftware/module-genealogy-people: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Liberu genealogy-people module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [genealogy-people](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-genealogy-laravel-filament, `genealogy-people`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-genealogy-people` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `genealogy-people` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Genealogy\\People\\PeopleServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/composer.json) · [module.json](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/module.json).

**Declared capabilities:** genealogy.people, genealogy.people.names, genealogy.people.identities, genealogy.people.attributes, genealogy.people.life-events, genealogy.people.living-status, genealogy.people.merge-candidates, genealogy.people.lifecycle

**Declared features:** genealogy people, genealogy people names, genealogy people identities, genealogy people attributes, genealogy people life-events, genealogy people living-status, genealogy people merge-candidates, genealogy people lifecycle

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-genealogy-core` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Genealogy\\People\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-genealogy-core": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateMergeCandidate.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreateMergeCandidate.php) | `public function execute(array $attributes): MergeCandidate` |
| [src/Actions/CreatePerson.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePerson.php) | `public function execute(array $attributes): Person` |
| [src/Actions/CreatePersonAssociation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonAssociation.php) | `public function execute(array $attributes): PersonAssociation` |
| [src/Actions/CreatePersonIdentity.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonIdentity.php) | `public function execute(array $attributes): PersonIdentity` |
| [src/Actions/CreatePersonLifeEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonLifeEvent.php) | `public function execute(array $attributes): PersonLifeEvent` |
| [src/Actions/CreatePersonName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/CreatePersonName.php) | `public function execute(array $attributes): PersonName` |
| [src/Actions/DeletePerson.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/DeletePerson.php) | `public function execute(Person $person): void` |
| [src/Actions/DeletePersonAssociation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/DeletePersonAssociation.php) | `public function execute(PersonAssociation $association): void` |
| [src/Actions/DeletePersonSupportingRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/DeletePersonSupportingRecord.php) | `public function execute(Model $record): void` |
| [src/Actions/MergePersons.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/MergePersons.php) | `public function execute(Person $primary, Person $duplicate): Person` |
| [src/Actions/RemovePersonAttribute.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/RemovePersonAttribute.php) | `public function execute(Person $person, string $attribute): Person` |
| [src/Actions/ReviewMergeCandidate.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/ReviewMergeCandidate.php) | `public function __construct(private readonly ?MergePersons $mergePersons = null)`<br>`public function execute(MergeCandidate $candidate, string $status, ?string $reason = null): MergeCandidate` |
| [src/Actions/SetPersonLifeStatus.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/SetPersonLifeStatus.php) | `public function execute(Person $person, string $status, ?string $deathDate = null): Person` |
| [src/Actions/UpdatePerson.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/UpdatePerson.php) | `public function execute(Person $person, array $attributes): Person` |
| [src/Actions/UpdatePersonAssociation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/UpdatePersonAssociation.php) | `public function execute(PersonAssociation $association, array $attributes): PersonAssociation` |
| [src/Actions/UpdatePersonAttributes.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/UpdatePersonAttributes.php) | `public function execute(Person $person, array $attributes, bool $replace = false): Person` |
| [src/Actions/UpdatePersonSupportingRecord.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Actions/UpdatePersonSupportingRecord.php) | `public function execute(Model $record, array $attributes): Model` |
| [src/Support/PersonReference.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Support/PersonReference.php) | `public function __construct(private readonly TeamContext $teamContext)`<br>`public function require(mixed $personId): string`<br>`public function existsForTeam(mixed $personId, string $teamId): bool` |

Other non-legacy PHP sources: [src/Capability.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Capability.php) · [src/Events/MergeCandidateReviewed.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Events/MergeCandidateReviewed.php) · [src/Events/PersonAttributesUpdated.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Events/PersonAttributesUpdated.php) · [src/Events/PersonCreated.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Events/PersonCreated.php) · [src/Events/PersonDeleted.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Events/PersonDeleted.php) · [src/Events/PersonMerged.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Events/PersonMerged.php) · [src/Events/PersonUpdated.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Events/PersonUpdated.php) · [src/Models/MergeCandidate.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/MergeCandidate.php) · [src/Models/Person.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/Person.php) · [src/Models/PersonAssociation.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonAssociation.php) · [src/Models/PersonIdentity.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonIdentity.php) · [src/Models/PersonLifeEvent.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonLifeEvent.php) · [src/Models/PersonName.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/Models/PersonName.php) · [src/PeopleServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/src/PeopleServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000000_create_genealogy_people_table.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/database/migrations/2026_08_24_000000_create_genealogy_people_table.php)
- [database/migrations/2026_08_24_020000_add_people_lifecycle_indexes.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/database/migrations/2026_08_24_020000_add_people_lifecycle_indexes.php)
- [database/migrations/2026_08_25_010000_add_public_visibility_to_genealogy_people.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/database/migrations/2026_08_25_010000_add_public_visibility_to_genealogy_people.php)
- [database/migrations/2026_08_25_020000_create_people_supporting_records.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/database/migrations/2026_08_25_020000_create_people_supporting_records.php)
- [database/migrations/2026_08_25_030000_create_person_associations.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/database/migrations/2026_08_25_030000_create_person_associations.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/DomainTest.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/tests/Feature/DomainTest.php)
- [tests/Unit/CapabilityTest.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-people/tests/Unit/CapabilityTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
