# liberusoftware/module-accounting-matching-intelligence: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Matching suggestions, confidence, evidence, feedback and safe automation thresholds.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-matching-intelligence](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-matching-intelligence`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-matching-intelligence` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-matching-intelligence` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\MatchingIntelligence\\MatchingIntelligenceServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\MatchingIntelligence\\MatchingIntelligenceServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/module.json).

**Declared capabilities:** accounting.matching-intelligence

**Declared features:** Matching suggestions, Confidence and evidence, Feedback, Safe automation thresholds

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\MatchingIntelligence\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ConfigureThreshold.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/ConfigureThreshold.php) | `public function handle(array $attributes): AutomationThreshold` |
| [src/Actions/CreateSuggestion.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/CreateSuggestion.php) | `public function handle(array $attributes, array $evidence = []): MatchingSuggestion` |
| [src/Actions/DecideSuggestion.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/DecideSuggestion.php) | `public function handle(MatchingSuggestion $suggestion, string $actor, bool $accept = true, bool $automate = false): MatchingSuggestion` |
| [src/Actions/RecordFeedback.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Actions/RecordFeedback.php) | `public function handle(MatchingSuggestion $suggestion, string $actor, string $type, ?string $comment = null): MatchingFeedback` |
| [src/Queries/MatchingQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Queries/MatchingQuery.php) | `public function suggestions(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function automationEligible(?int $teamId = null, int $perPage = 25): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/Enums/FeedbackType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Enums/FeedbackType.php) · [src/Enums/SuggestionStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Enums/SuggestionStatus.php) · [src/Events/SuggestionCreated.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Events/SuggestionCreated.php) · [src/Events/SuggestionDecided.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Events/SuggestionDecided.php) · [src/Exceptions/InvalidMatch.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Exceptions/InvalidMatch.php) · [src/MatchingIntelligenceServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/MatchingIntelligenceServiceProvider.php) · [src/Models/AutomationThreshold.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/AutomationThreshold.php) · [src/Models/MatchingEvidence.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/MatchingEvidence.php) · [src/Models/MatchingFeedback.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/MatchingFeedback.php) · [src/Models/MatchingSuggestion.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Models/MatchingSuggestion.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_012000_create_accounting_matching_intelligence_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/database/migrations/2026_08_26_012000_create_accounting_matching_intelligence_tables.php)

[src/Enums/FeedbackType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Enums/FeedbackType.php): `Correct = 'correct'`, `Incorrect = 'incorrect'`, `Partial = 'partial'`.

[src/Enums/SuggestionStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-matching-intelligence/src/Enums/SuggestionStatus.php): `Suggested = 'suggested'`, `Accepted = 'accepted'`, `Rejected = 'rejected'`, `Automated = 'automated'`, `Expired = 'expired'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
