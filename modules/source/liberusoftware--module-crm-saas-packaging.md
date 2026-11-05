# liberusoftware/module-crm-saas-packaging: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-saas-packaging](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `crm-saas-packaging`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-saas-packaging` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-saas-packaging` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\SaasPackaging\\SaasPackagingServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\SaasPackaging\\SaasPackagingServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/module.json).

**Declared capabilities:** crm.saas-packaging

**Declared features:** Plans and feature/module entitlements, Limits, trials and signup provisioning, Upgrade, downgrade, suspension and cancellation, Billing integration references

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\SaasPackaging\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/ChangeSubscriptionStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/ChangeSubscriptionStatus.php) | `public function execute(int $teamId, int $actorId, string $status): SaasSubscription` |
| [src/Actions/ProvisionSubscription.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/ProvisionSubscription.php) | `public function execute(int $teamId, int $actorId, array $data): SaasSubscription` |
| [src/Actions/RecordUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/RecordUsage.php) | `public function execute(int $teamId, int $actorId, array $data): SaasUsage` |
| [src/Actions/UpdateSubscription.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/UpdateSubscription.php) | `public function execute(int $teamId, int $actorId, array $data): SaasSubscription` |
| [src/Queries/SaasQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Queries/SaasQuery.php) | `public function plans()`<br>`public function subscription(int $teamId): ?SaasSubscription`<br>`public function usage(int $teamId)` |
| [src/Services/SaasPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Services/SaasPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Events/SubscriptionChanged.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Events/SubscriptionChanged.php) · [src/Models/SaasPlan.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Models/SaasPlan.php) · [src/Models/SaasSubscription.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Models/SaasSubscription.php) · [src/Models/SaasUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Models/SaasUsage.php) · [src/SaasPackagingServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/SaasPackagingServiceProvider.php).

**Legacy review:** 2 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_170000_create_crm_saas_packaging_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/database/migrations/2026_08_25_170000_create_crm_saas_packaging_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/SaasPackaging/SaasPackagingModuleTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/tests/Feature/SaasPackaging/SaasPackagingModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
