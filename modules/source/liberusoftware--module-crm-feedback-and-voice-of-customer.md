# liberusoftware/module-crm-feedback-and-voice-of-customer: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-feedback-and-voice-of-customer](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-feedback-and-voice-of-customer`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-feedback-and-voice-of-customer` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-feedback-and-voice-of-customer` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\FeedbackAndVoiceOfCustomer\\FeedbackAndVoiceOfCustomerServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\FeedbackAndVoiceOfCustomer\\FeedbackAndVoiceOfCustomerServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/module.json).

**Declared capabilities:** crm.feedback-and-voice-of-customer

**Declared features:** CSAT, NPS, CES, custom surveys, sampling, delivery, analysis, alerts, cases and trends

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\FeedbackAndVoiceOfCustomer\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateFeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/CreateFeedbackSurvey.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): FeedbackSurvey` |
| [src/Actions/DeliverFeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/DeliverFeedbackSurvey.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackSurvey $survey, ?int $recipientId, string $channel = 'email'): FeedbackDelivery` |
| [src/Actions/OpenFeedbackCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/OpenFeedbackCase.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackResponse $response, ?int $ownerId = null): FeedbackCase` |
| [src/Actions/RecordFeedbackResponse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/RecordFeedbackResponse.php) | `public function execute(int $teamId, FeedbackDelivery $delivery, array $input): FeedbackResponse` |
| [src/Actions/ResolveFeedbackAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Actions/ResolveFeedbackAlert.php) | `public function __construct(private readonly FeedbackPolicy $policy)`<br>`public function execute(int $teamId, int $userId, FeedbackAlert $alert): FeedbackAlert` |
| [src/Queries/FeedbackQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Queries/FeedbackQuery.php) | `public function surveys(int $teamId)`<br>`public function responses(int $teamId, int $surveyId)`<br>`public function trend(int $teamId, int $surveyId): array` |
| [src/Services/FeedbackPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Services/FeedbackPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/FeedbackAndVoiceOfCustomerServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/FeedbackAndVoiceOfCustomerServiceProvider.php) · [src/Models/FeedbackAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackAlert.php) · [src/Models/FeedbackCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackCase.php) · [src/Models/FeedbackDelivery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackDelivery.php) · [src/Models/FeedbackResponse.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackResponse.php) · [src/Models/FeedbackSurvey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/src/Models/FeedbackSurvey.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_27_030000_create_crm_feedback_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/database/migrations/2026_08_27_030000_create_crm_feedback_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/FeedbackAndVoiceOfCustomer/FeedbackAndVoiceOfCustomerModuleTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-feedback-and-voice-of-customer/tests/Feature/FeedbackAndVoiceOfCustomer/FeedbackAndVoiceOfCustomerModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
