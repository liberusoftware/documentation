# liberusoftware/module-crm-customer-self-service: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-customer-self-service](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 18 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `crm-customer-self-service`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-customer-self-service` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-customer-self-service` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\CustomerSelfService\\CustomerSelfServiceServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\CustomerSelfService\\CustomerSelfServiceServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/module.json).

**Declared capabilities:** crm.customer-self-service

**Declared features:** Portal, cases, knowledge, community links, appointments, documents, invoices, orders, profiles and preferences

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\CustomerSelfService\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/SubmitSelfServiceCase.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Actions/SubmitSelfServiceCase.php) | `public function __construct(private readonly SelfServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, SelfServiceProfile $profile, array $input): SelfServiceCase` |
| [src/Actions/UpdateSelfServicePreferences.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Actions/UpdateSelfServicePreferences.php) | `public function __construct(private readonly SelfServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, SelfServiceProfile $profile, array $input): SelfServiceProfile` |
| [src/Actions/UpsertSelfServiceProfile.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Actions/UpsertSelfServiceProfile.php) | `public function __construct(private readonly SelfServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): SelfServiceProfile` |
| [src/Queries/SelfServiceQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Queries/SelfServiceQuery.php) | `public function profile(int $teamId, int $userId): ?SelfServiceProfile`<br>`public function cases(int $teamId, int $profileId)`<br>`public function search(int $teamId, string $term)` |
| [src/Services/SelfServicePolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Services/SelfServicePolicy.php) | `public function canAccess(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/CustomerSelfServiceServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/CustomerSelfServiceServiceProvider.php) · [src/Models/SelfServiceCase.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceCase.php) · [src/Models/SelfServiceProfile.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceProfile.php) · [src/Models/SelfServiceReference.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceReference.php) · [src/Models/SelfServiceResource.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceResource.php).

**Legacy review:** 22 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_27_110000_create_crm_self_service_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/database/migrations/2026_08_27_110000_create_crm_self_service_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **18**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/CustomerSelfService/CustomerSelfServiceModuleTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/CustomerSelfService/CustomerSelfServiceModuleTest.php)
- [tests/Feature/Portal/CreatePortalTicketTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/CreatePortalTicketTest.php)
- [tests/Feature/Portal/CustomerPortalTicketTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/CustomerPortalTicketTest.php)
- [tests/Feature/Portal/PortalAuditTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalAuditTest.php)
- [tests/Feature/Portal/PortalBrandingAssetsTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalBrandingAssetsTest.php)
- [tests/Feature/Portal/PortalBrandingTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalBrandingTest.php)
- [tests/Feature/Portal/PortalDashboardTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalDashboardTest.php)
- [tests/Feature/Portal/PortalDocumentsTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalDocumentsTest.php)
- [tests/Feature/Portal/PortalKbVoteTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalKbVoteTest.php)
- [tests/Feature/Portal/PortalKnowledgeBaseTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalKnowledgeBaseTest.php)
- [tests/Feature/Portal/PortalLogoUploadTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalLogoUploadTest.php)
- [tests/Feature/Portal/PortalNotificationsTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalNotificationsTest.php)
- [tests/Feature/Portal/PortalOnboardingTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalOnboardingTest.php)
- [tests/Feature/Portal/PortalRecentTicketsTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalRecentTicketsTest.php)
- [tests/Feature/Portal/PortalRevokeTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalRevokeTest.php)
- [tests/Feature/Portal/PortalTeamBrandingTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalTeamBrandingTest.php)
- [tests/Feature/Portal/PortalTicketLifecycleTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalTicketLifecycleTest.php)
- [tests/Feature/Portal/PortalTicketThreadTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/tests/Feature/Portal/PortalTicketThreadTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
