# liberusoftware/application: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Required application metadata, health, clocks, identifiers, and secure HTTP defaults.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/composer.json) | `39a49babafc0` | [Variant 3](#variant-3) | 1 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/composer.json) | `68e5f07a6704` | [Variant 2](#variant-2) | 1 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/application/composer.json) | `4743bdfebd1c` | [Variant 2](#variant-2) | 1 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/application/composer.json) | `3ade34046c3d` | [Variant 2](#variant-2) | 1 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/application/composer.json) | `790fdffebd3a` | [Variant 2](#variant-2) | 1 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/application/composer.json) | `1797f25d705f` | [Variant 2](#variant-2) | 1 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 10 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/application/composer.json) | `b12a8c841c6a` | [Variant 2](#variant-2) | 1 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/application/composer.json) | `577e93db23cc` | [Variant 2](#variant-2) | 1 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/application/composer.json) | `c267d625e264` | [Variant 2](#variant-2) | 1 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/application/composer.json) | `178d8015b601` | [Variant 2](#variant-2) | 1 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [application](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/application/composer.json) | `08bbc484b50f` | [Variant 2](#variant-2) | 1 |

Physical source locations: **12**. Reference variants: **3**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `application`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/application` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `application` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\ApplicationCore\\ApplicationCoreServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/module.json).

**Declared capabilities:** foundation.application-core

**Declared features:** Application metadata, Health/readiness, Secure response defaults, Clocks, Shared identifiers

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\ApplicationCore\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/Clock.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Contracts/Clock.php) | `public function now(): \DateTimeImmutable` |
| [src/Contracts/IdentifierFactory.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Contracts/IdentifierFactory.php) | `public function make(): string` |
| [src/Http/Controllers/ReadinessController.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Http/Controllers/ReadinessController.php) | `public function __invoke(ReadinessRegistry $registry): JsonResponse` |
| [src/Support/EnvironmentValidator.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Support/EnvironmentValidator.php) | `public function validate(): void` |
| [src/Support/SystemClock.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Support/SystemClock.php) | `public function now(): \DateTimeImmutable` |
| [src/Support/UuidIdentifierFactory.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Support/UuidIdentifierFactory.php) | `public function make(): string` |

Other non-legacy PHP sources: [src/ApplicationCoreServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/ApplicationCoreServiceProvider.php) · [src/Health/ReadinessCheck.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Health/ReadinessCheck.php) · [src/Health/ReadinessRegistry.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Health/ReadinessRegistry.php) · [src/Http/Middleware/SecurityHeaders.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/src/Http/Middleware/SecurityHeaders.php).

**Legacy review:** 25 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [routes/health.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/routes/health.php)

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/0001_01_01_000001_create_cache_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/database/migrations/0001_01_01_000001_create_cache_table.php)
- [database/migrations/0001_01_01_000002_create_jobs_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/database/migrations/0001_01_01_000002_create_jobs_table.php)
- [database/migrations/2019_09_15_000010_create_tenants_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/database/migrations/2019_09_15_000010_create_tenants_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **10**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/tests/.gitkeep)
- [tests/Feature/Security/AdvertisingAccountEncryptionTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/tests/Feature/Security/AdvertisingAccountEncryptionTest.php)
- [tests/Feature/Security/ConnectedAccountEncryptionTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/tests/Feature/Security/ConnectedAccountEncryptionTest.php)
- [tests/Feature/Security/ContactEmailEncryptionTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/tests/Feature/Security/ContactEmailEncryptionTest.php)
- [tests/Feature/Security/OAuthConfigurationEncryptionTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/tests/Feature/Security/OAuthConfigurationEncryptionTest.php)
- [tests/Feature/Security/PhoneEncryptionTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/tests/Feature/Security/PhoneEncryptionTest.php)
- [tests/Feature/Security/SecurityHardeningTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/tests/Feature/Security/SecurityHardeningTest.php)
- [tests/Feature/Security/SsrfGuardTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/tests/Feature/Security/SsrfGuardTest.php)
- [tests/Feature/Security/TicketAttachmentContentTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/tests/Feature/Security/TicketAttachmentContentTest.php)
- [tests/Feature/Security/WebhookEncryptionTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/application/tests/Feature/Security/WebhookEncryptionTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: automation-laravel, `application`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/application` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `application` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\ApplicationCore\\ApplicationCoreServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/composer.json) · [module.json](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/module.json).

**Declared capabilities:** foundation.application-core

**Declared features:** Application metadata, Health/readiness, Secure response defaults, Clocks, Shared identifiers

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\ApplicationCore\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/Clock.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/src/Contracts/Clock.php) | `public function now(): \DateTimeImmutable` |
| [src/Contracts/IdentifierFactory.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/src/Contracts/IdentifierFactory.php) | `public function make(): string` |
| [src/Http/Controllers/ReadinessController.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/src/Http/Controllers/ReadinessController.php) | `public function __invoke(ReadinessRegistry $registry): JsonResponse` |
| [src/Support/EnvironmentValidator.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/src/Support/EnvironmentValidator.php) | `public function validate(): void` |
| [src/Support/SystemClock.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/src/Support/SystemClock.php) | `public function now(): \DateTimeImmutable` |
| [src/Support/UuidIdentifierFactory.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/src/Support/UuidIdentifierFactory.php) | `public function make(): string` |

Other non-legacy PHP sources: [src/ApplicationCoreServiceProvider.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/src/ApplicationCoreServiceProvider.php) · [src/Health/ReadinessCheck.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/src/Health/ReadinessCheck.php) · [src/Health/ReadinessRegistry.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/src/Health/ReadinessRegistry.php) · [src/Http/Middleware/SecurityHeaders.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/src/Http/Middleware/SecurityHeaders.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [routes/health.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/routes/health.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/application/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 3

Representative: accounting-erp-laravel, `application`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/application` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `application` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\ApplicationCore\\ApplicationCoreServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/module.json).

**Declared capabilities:** foundation.application-core

**Declared features:** Application metadata, Health/readiness, Secure response defaults, Clocks, Shared identifiers

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\ApplicationCore\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/Clock.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/src/Contracts/Clock.php) | `public function now(): \DateTimeImmutable` |
| [src/Contracts/IdentifierFactory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/src/Contracts/IdentifierFactory.php) | `public function make(): string` |
| [src/Http/Controllers/ReadinessController.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/src/Http/Controllers/ReadinessController.php) | `public function __invoke(ReadinessRegistry $registry): JsonResponse` |
| [src/Support/EnvironmentValidator.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/src/Support/EnvironmentValidator.php) | `public function validate(): void` |
| [src/Support/SystemClock.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/src/Support/SystemClock.php) | `public function now(): \DateTimeImmutable` |
| [src/Support/UuidIdentifierFactory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/src/Support/UuidIdentifierFactory.php) | `public function make(): string` |

Other non-legacy PHP sources: [src/ApplicationCoreServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/src/ApplicationCoreServiceProvider.php) · [src/Health/ReadinessCheck.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/src/Health/ReadinessCheck.php) · [src/Health/ReadinessRegistry.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/src/Health/ReadinessRegistry.php) · [src/Http/Middleware/SecurityHeaders.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/src/Http/Middleware/SecurityHeaders.php) · [src/Models/CreditMemoApplication.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/src/Models/CreditMemoApplication.php) · [src/Models/VendorCreditApplication.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/src/Models/VendorCreditApplication.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [routes/health.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/routes/health.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/application/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
