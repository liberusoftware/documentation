# liberusoftware/module-accounting-coding-suggestions: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Accounting coding suggestions domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-coding-suggestions](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-coding-suggestions`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-coding-suggestions` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-coding-suggestions` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\CodingSuggestions\\CodingSuggestionsServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\CodingSuggestions\\CodingSuggestionsServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/module.json).

**Declared capabilities:** accounting.coding-suggestions

**Declared features:** Account and tax suggestions, Dimensions and payees, Confidence and explanations, User feedback, Policy thresholds, Review

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\CodingSuggestions\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ApplySuggestionFeedback.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/ApplySuggestionFeedback.php) | `public function handle(CodingSuggestion $suggestion, array $feedback): CodingSuggestion` |
| [src/Actions/CreateCodingSuggestion.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/CreateCodingSuggestion.php) | `public function handle(array $attributes): CodingSuggestion` |
| [src/Actions/ReviewCodingSuggestion.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/ReviewCodingSuggestion.php) | `public function handle(CodingSuggestion $suggestion, array $review): CodingSuggestion` |
| [src/Actions/SetSuggestionPolicy.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Actions/SetSuggestionPolicy.php) | `public function handle(CodingSuggestion $suggestion, array $policy): CodingSuggestion` |
| [src/Queries/CodingSuggestionQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Queries/CodingSuggestionQuery.php) | `public function forTeam(int $teamId): Collection` |

Other non-legacy PHP sources: [src/CodingSuggestionsServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/CodingSuggestionsServiceProvider.php) · [src/Enums/CodingSuggestionStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Enums/CodingSuggestionStatus.php) · [src/Exceptions/InvalidCodingSuggestion.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Exceptions/InvalidCodingSuggestion.php) · [src/Models/CodingSuggestion.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Models/CodingSuggestion.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_29_000025_create_accounting_coding_suggestions_table.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/database/migrations/2026_08_29_000025_create_accounting_coding_suggestions_table.php)

[src/Enums/CodingSuggestionStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-coding-suggestions/src/Enums/CodingSuggestionStatus.php): `Pending = 'pending'`, `Accepted = 'accepted'`, `Rejected = 'rejected'`, `Reviewed = 'reviewed'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
