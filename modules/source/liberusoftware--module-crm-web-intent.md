# liberusoftware/module-crm-web-intent: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

First-party web intent tracking and buyer-intent scoring for Liberu CRM.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-web-intent](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-web-intent`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-web-intent` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-web-intent` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\WebIntent\\WebIntentServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\WebIntent\\WebIntentServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/module.json).

**Declared capabilities:** crm.web-intent

**Declared features:** First-party visits, Account identification adapters, Page and content engagement, Scoring signals, Alerts, Buyer intent, Consent, Lead and account conversion

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/validation` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\CRM\\WebIntent\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ConvertIntent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/ConvertIntent.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $targetType, int $targetId, ?int $visitId, array $metadata, WebIntentPolicy $policy): WebIntentConversion` |
| [src/Actions/CreateAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/CreateAlert.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $title, string $severity, ?int $visitId, ?string $details, WebIntentPolicy $policy): WebIntentAlert` |
| [src/Actions/IdentifyAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/IdentifyAccount.php) | `public function execute(int $teamId, int $actorId, string $visitorKey, string $adapter, ?string $accountName, ?string $accountDomain, int $confidence, array $metadata, WebIntentPolicy $policy): WebIntentIdentification` |
| [src/Actions/RecordEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/RecordEngagement.php) | `public function execute(WebIntentVisit $visit, array $attributes, WebIntentScorer $scorer): WebIntentEngagement` |
| [src/Actions/RecordVisit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/RecordVisit.php) | `public function execute(int $teamId, string $visitorKey, array $attributes = []): WebIntentVisit` |
| [src/Actions/ResolveAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/ResolveAlert.php) | `public function execute(WebIntentAlert $alert, int $actorId, WebIntentPolicy $policy): WebIntentAlert` |
| [src/Actions/SetConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Actions/SetConsent.php) | `public function execute(int $teamId, string $visitorKey, string $purpose, string $status, ?string $policyVersion = null): WebIntentConsent` |
| [src/Queries/WebIntentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Queries/WebIntentQuery.php) | `public function visits(int $teamId): Builder`<br>`public function alerts(int $teamId): Builder`<br>`public function summary(int $teamId): array` |
| [src/Services/WebIntentAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $data = []): void` |
| [src/Services/WebIntentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentPolicy.php) | `public function canManage(int $teamId, int $actorId): bool` |
| [src/Services/WebIntentScorer.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Services/WebIntentScorer.php) | `public function points(string $eventType, ?int $durationSeconds = null): int`<br>`public function level(int $score): string` |

Other non-legacy PHP sources: [src/Events/EngagementRecorded.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Events/EngagementRecorded.php) · [src/Events/VisitRecorded.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Events/VisitRecorded.php) · [src/Models/WebIntentAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentAlert.php) · [src/Models/WebIntentConsent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentConsent.php) · [src/Models/WebIntentConversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentConversion.php) · [src/Models/WebIntentEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentEngagement.php) · [src/Models/WebIntentIdentification.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentIdentification.php) · [src/Models/WebIntentSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentSignal.php) · [src/Models/WebIntentVisit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/Models/WebIntentVisit.php) · [src/WebIntentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/src/WebIntentServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_030000_create_crm_web_intent_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/database/migrations/2026_08_25_030000_create_crm_web_intent_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/WebIntent/WebIntentModuleTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-web-intent/tests/Feature/WebIntent/WebIntentModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
