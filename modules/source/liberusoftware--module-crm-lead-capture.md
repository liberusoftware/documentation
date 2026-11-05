# liberusoftware/module-crm-lead-capture: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-lead-capture](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-lead-capture`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-lead-capture` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-lead-capture` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\LeadCapture\\LeadCaptureServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\LeadCapture\\LeadCaptureServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/module.json).

**Declared capabilities:** crm.lead-capture

**Declared features:** Manual, import, API and multichannel lead capture, Forms, surveys, QR, chat, calls, ads, events, referrals and source metadata

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\LeadCapture\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CaptureLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CaptureLead.php) | `public function __construct(private readonly LeadCapturePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CapturedLead`<br>`public function executeLegacy(int $teamId, ?int $actorId, array $input): LeadCapture` |
| [src/Actions/CreateCaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CreateCaptureForm.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureForm` |
| [src/Actions/CreateCaptureQrCode.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/CreateCaptureQrCode.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureQrCode` |
| [src/Actions/RecordCaptureEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/RecordCaptureEvent.php) | `public function __construct(private readonly LeadCapturePolicy $policy)`<br>`public function execute(int $teamId, int $userId, CapturedLead $lead, array $input): CaptureEvent` |
| [src/Actions/RecordReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/RecordReferral.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): CaptureReferral` |
| [src/Actions/SubmitCaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/SubmitCaptureForm.php) | `public function execute(CaptureForm $form, ?int $actorId, array $payload): LeadCapture` |
| [src/Actions/UpdateCaptureStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Actions/UpdateCaptureStatus.php) | `public function execute(LeadCapture $capture, string $status, ?string $failureReason = null): LeadCapture` |
| [src/Queries/CaptureQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Queries/CaptureQuery.php) | `public function forTeam(int $teamId)` |
| [src/Services/CaptureDeduplicator.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/CaptureDeduplicator.php) | `public function key(array $attributes): string`<br>`public function find(int $teamId, string $key): ?LeadCapture` |
| [src/Services/CaptureReport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/CaptureReport.php) | `public function summarize(int $teamId, Carbon $from, Carbon $until): array` |
| [src/Services/LeadCapturePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Services/LeadCapturePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Events/CaptureFormSubmitted.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Events/CaptureFormSubmitted.php) · [src/Events/LeadCaptured.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Events/LeadCaptured.php) · [src/LeadCaptureServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/LeadCaptureServiceProvider.php) · [src/Models/CaptureEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureEvent.php) · [src/Models/CaptureForm.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureForm.php) · [src/Models/CaptureQrCode.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureQrCode.php) · [src/Models/CaptureReferral.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CaptureReferral.php) · [src/Models/CapturedLead.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/CapturedLead.php) · [src/Models/LeadCapture.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/src/Models/LeadCapture.php).

**Legacy review:** 9 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_110000_create_crm_lead_capture_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/database/migrations/2026_08_24_110000_create_crm_lead_capture_tables.php)
- [database/migrations/2026_08_26_200000_create_crm_lead_capture_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/database/migrations/2026_08_26_200000_create_crm_lead_capture_tables.php)
- [database/migrations/2026_08_30_130000_add_import_key_to_leads.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/database/migrations/2026_08_30_130000_add_import_key_to_leads.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/LeadCapture/LeadCaptureModuleTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-lead-capture/tests/Feature/LeadCapture/LeadCaptureModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
