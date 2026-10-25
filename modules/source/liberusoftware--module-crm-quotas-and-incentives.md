# liberusoftware/module-crm-quotas-and-incentives: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

No Composer description declared.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [crm-quotas-and-incentives](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `crm-quotas-and-incentives`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-crm-quotas-and-incentives` |
| Composer version field | `not declared; may be VCS-derived` |
| Package type | `liberu-module` |
| Module manifest name | `crm-quotas-and-incentives` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\CRM\\QuotasAndIncentives\\QuotasAndIncentivesServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\CRM\\QuotasAndIncentives\\QuotasAndIncentivesServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/module.json).

**Declared capabilities:** crm.quotas-and-incentives

**Declared features:** Quotas, ramps, crediting, splits and territories, Attainment, commission plans, accelerators, adjustments and disputes, Approvals and payroll export adapters

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| — | No Composer runtime requirements declared |

PSR-4 mappings: `{"Liberu\\CRM\\QuotasAndIncentives\\": "src/"}`.

Module resolver requirements: `{"packages": {}}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateCommissionPlan.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/CreateCommissionPlan.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CommissionPlan` |
| [src/Actions/CreateQuota.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/CreateQuota.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Quota` |
| [src/Actions/CreditCommission.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/CreditCommission.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CommissionCredit` |
| [src/Actions/ExportCommissions.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/ExportCommissions.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CommissionExport` |
| [src/Actions/OpenDispute.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/OpenDispute.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CommissionDispute` |
| [src/Actions/ResolveDispute.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/ResolveDispute.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $disputeId, array $input): CommissionDispute` |
| [src/Actions/UpdateQuota.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Actions/UpdateQuota.php) | `public function __construct(private readonly QuotaPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $quotaId, array $input): Quota` |
| [src/Queries/QuotaQuery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Queries/QuotaQuery.php) | `public function quotas(int $teamId)`<br>`public function plans(int $teamId)`<br>`public function credits(int $teamId)`<br>`public function disputes(int $teamId)`<br>`public function exports(int $teamId)` |
| [src/Services/QuotaPolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Services/QuotaPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

Other non-legacy PHP sources: [src/Events/CommissionCredited.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Events/CommissionCredited.php) · [src/Models/CommissionCredit.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionCredit.php) · [src/Models/CommissionDispute.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionDispute.php) · [src/Models/CommissionExport.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionExport.php) · [src/Models/CommissionPlan.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/CommissionPlan.php) · [src/Models/Quota.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/Models/Quota.php) · [src/QuotasAndIncentivesServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/src/QuotasAndIncentivesServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_010000_create_crm_quotas_and_incentives_tables.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/database/migrations/2026_08_26_010000_create_crm_quotas_and_incentives_tables.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Feature/QuotasAndIncentives/QuotasAndIncentivesModuleTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-quotas-and-incentives/tests/Feature/QuotasAndIncentives/QuotasAndIncentivesModuleTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
