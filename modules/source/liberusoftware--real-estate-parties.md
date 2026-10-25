# liberusoftware/real-estate-parties: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral real-estate parties, relationships, and consent.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [real-estate-parties](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: real-estate-laravel, `real-estate-parties`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/real-estate-parties` |
| Composer version field | `1.0.1` |
| Package type | `liberu-module` |
| Module manifest name | `real-estate-parties` |
| Module version field | `1.0.1` |
| Category / layers | `"product"` |
| Manifest provider(s) | `"Liberu\\RealEstate\\Parties\\PartiesServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/composer.json) · [module.json](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/module.json).

**Declared capabilities:** real-estate.parties

**Declared features:** Applicants, Vendors, Landlords, Tenants, Buyers, Solicitors, Contractors, Tourists, Guides, Relationships, Consent, Landlord reviews, Tenant reviews

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/validation` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\RealEstate\\Parties\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Policies/PartyPolicy.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Policies/PartyPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Party $party): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Party $party): bool`<br>`public function delete(AuthUser $authUser, Party $party): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Party $party): bool`<br>`public function forceDelete(AuthUser $authUser, Party $party): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Party $party): bool`<br>`public function reorder(AuthUser $authUser): bool` |

Other non-legacy PHP sources: [src/Application/CreateContact.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Application/CreateContact.php) · [src/Application/CreateContactMessage.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Application/CreateContactMessage.php) · [src/Application/CreateParty.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Application/CreateParty.php) · [src/Application/CreatePartyRelationship.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Application/CreatePartyRelationship.php) · [src/Application/DeleteParty.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Application/DeleteParty.php) · [src/Application/DeletePartyRelationship.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Application/DeletePartyRelationship.php) · [src/Application/ManagePartyConsent.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Application/ManagePartyConsent.php) · [src/Application/SubmitPartyReview.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Application/SubmitPartyReview.php) · [src/Application/UpdateParty.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Application/UpdateParty.php) · [src/Domain/PartiesCapabilityDefinition.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Domain/PartiesCapabilityDefinition.php) · [src/Domain/PartyType.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Domain/PartyType.php) · [src/Models/Contact.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/Contact.php) · [src/Models/ContactMessage.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/ContactMessage.php) · [src/Models/Party.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/Party.php) · [src/Models/PartyRelationship.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/PartyRelationship.php) · [src/Models/PartyReview.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/PartyReview.php) · [src/PartiesServiceProvider.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/PartiesServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_23_000002_create_real_estate_parties_table.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/database/migrations/2026_08_23_000002_create_real_estate_parties_table.php)
- [database/migrations/2026_08_25_000001_create_real_estate_party_relationships_table.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/database/migrations/2026_08_25_000001_create_real_estate_party_relationships_table.php)
- [database/migrations/2026_08_30_000001_create_real_estate_party_reviews.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/database/migrations/2026_08_30_000001_create_real_estate_party_reviews.php)
- [database/migrations/2026_08_30_000017_create_real_estate_contacts_and_contact_messages.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/database/migrations/2026_08_30_000017_create_real_estate_contacts_and_contact_messages.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
