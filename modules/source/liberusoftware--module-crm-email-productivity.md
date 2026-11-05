# liberusoftware/module-crm-email-productivity: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-email-productivity](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-email-productivity`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-email-productivity` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-email-productivity` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\EmailProductivity\\EmailProductivityServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\EmailProductivity\\EmailProductivityServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/module.json).

**Declared capabilities:** crm.email-productivity

**Declared features:** Mailbox sync, send/log, templates, snippets, scheduling, tracking, signatures, sidebars and provider adapters

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\EmailProductivity\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ConnectMailbox.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/ConnectMailbox.php) | `public function __construct(private readonly EmailProductivityPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailMailbox` |
| [src/Actions/CreateEmailTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/CreateEmailTemplate.php) | `public function __construct(private readonly EmailProductivityPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailTemplate` |
| [src/Actions/RecordEmailEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/RecordEmailEvent.php) | `public function execute(int $teamId, EmailMessage $message, array $input): EmailEvent` |
| [src/Actions/SendEmail.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Actions/SendEmail.php) | `public function __construct(private readonly EmailProductivityPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EmailMessage` |
| [src/Queries/EmailProductivityQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Queries/EmailProductivityQuery.php) | `public function mailboxes(int $teamId)`<br>`public function templates(int $teamId)`<br>`public function messages(int $teamId)` |
| [src/Services/EmailProductivityPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Services/EmailProductivityPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/EmailProductivityServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/EmailProductivityServiceProvider.php) · [src/Models/EmailEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailEvent.php) · [src/Models/EmailMailbox.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailMailbox.php) · [src/Models/EmailMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailMessage.php) · [src/Models/EmailTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/src/Models/EmailTemplate.php).

**Legacy review:** 17 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2024_02_15_000000_create_emails_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/database/migrations/2024_02_15_000000_create_emails_table.php)
- [database/migrations/2024_02_15_000001_create_email_tracking_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/database/migrations/2024_02_15_000001_create_email_tracking_tables.php)
- [database/migrations/2025_01_27_173821_create_message_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/database/migrations/2025_01_27_173821_create_message_table.php)
- [database/migrations/2025_11_20_112532_add_team_to_messages.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/database/migrations/2025_11_20_112532_add_team_to_messages.php)
- [database/migrations/2026_03_03_000002_add_ticket_id_to_messages_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/database/migrations/2026_03_03_000002_add_ticket_id_to_messages_table.php)
- [database/migrations/2026_03_08_000003_add_missing_columns_to_emails_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/database/migrations/2026_03_08_000003_add_missing_columns_to_emails_table.php)
- [database/migrations/2026_07_06_000000_make_tickets_email_id_nullable.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/database/migrations/2026_07_06_000000_make_tickets_email_id_nullable.php)
- [database/migrations/2026_08_27_060000_create_crm_email_productivity_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/database/migrations/2026_08_27_060000_create_crm_email_productivity_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/EmailProductivity/EmailProductivityModuleTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-email-productivity/tests/Feature/EmailProductivity/EmailProductivityModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
