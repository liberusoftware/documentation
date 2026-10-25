# liberusoftware/two-factor-authentication: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

TOTP enforcement policy and one-time recovery-code primitives.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/two-factor-authentication/composer.json) | `39a49babafc0` | [Variant 2](#variant-2) | 1 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/two-factor-authentication/composer.json) | `68e5f07a6704` | [Variant 2](#variant-2) | 1 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/two-factor-authentication/composer.json) | `4743bdfebd1c` | [Variant 2](#variant-2) | 1 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/two-factor-authentication/composer.json) | `3ade34046c3d` | [Variant 2](#variant-2) | 1 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/two-factor-authentication/composer.json) | `790fdffebd3a` | [Variant 2](#variant-2) | 1 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/two-factor-authentication/composer.json) | `1797f25d705f` | [Variant 2](#variant-2) | 1 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 1 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/two-factor-authentication/composer.json) | `b12a8c841c6a` | [Variant 2](#variant-2) | 1 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/two-factor-authentication/composer.json) | `577e93db23cc` | [Variant 2](#variant-2) | 1 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/two-factor-authentication/composer.json) | `c267d625e264` | [Variant 2](#variant-2) | 1 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/two-factor-authentication/composer.json) | `178d8015b601` | [Variant 2](#variant-2) | 1 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [two-factor-authentication](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/two-factor-authentication/composer.json) | `08bbc484b50f` | [Variant 2](#variant-2) | 1 |

Physical source locations: **12**. Reference variants: **2**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: crm-laravel, `two-factor-authentication`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/two-factor-authentication` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `two-factor-authentication` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\TwoFactor\\TwoFactorServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication/module.json).

**Declared capabilities:** identity.two-factor

**Declared features:** TOTP enforcement, Trusted-device policy, Single-use recovery primitives

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/contracts` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/identity-core` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\TwoFactor\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/identity-core": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/TwoFactorRecovery.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication/src/Contracts/TwoFactorRecovery.php) | `public function recover(Authenticatable $subject, Authenticatable $administrator, string $reason): void` |

Other non-legacy PHP sources: [src/Enforcement/TwoFactorPolicy.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication/src/Enforcement/TwoFactorPolicy.php) · [src/Recovery/RecoveryCodeHasher.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication/src/Recovery/RecoveryCodeHasher.php) · [src/TrustedDevices/TrustedDeviceManager.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication/src/TrustedDevices/TrustedDeviceManager.php) · [src/TwoFactorServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication/src/TwoFactorServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_06_29_123952_add_two_factor_columns_to_users_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication/database/migrations/2026_06_29_123952_add_two_factor_columns_to_users_table.php)
- [database/migrations/2026_08_01_060000_create_two_factor_trusted_devices_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication/database/migrations/2026_08_01_060000_create_two_factor_trusted_devices_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: accounting-erp-laravel, `two-factor-authentication`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/two-factor-authentication` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `two-factor-authentication` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\TwoFactor\\TwoFactorServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/two-factor-authentication/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/two-factor-authentication/module.json).

**Declared capabilities:** identity.two-factor

**Declared features:** TOTP enforcement, Trusted-device policy, Single-use recovery primitives

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/contracts` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/identity-core` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\TwoFactor\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/identity-core": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/TwoFactorRecovery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/two-factor-authentication/src/Contracts/TwoFactorRecovery.php) | `public function recover(Authenticatable $subject, Authenticatable $administrator, string $reason): void` |

Other non-legacy PHP sources: [src/Enforcement/TwoFactorPolicy.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/two-factor-authentication/src/Enforcement/TwoFactorPolicy.php) · [src/Recovery/RecoveryCodeHasher.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/two-factor-authentication/src/Recovery/RecoveryCodeHasher.php) · [src/TrustedDevices/TrustedDeviceManager.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/two-factor-authentication/src/TrustedDevices/TrustedDeviceManager.php) · [src/TwoFactorServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/two-factor-authentication/src/TwoFactorServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_06_29_123952_add_two_factor_columns_to_users_table.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/two-factor-authentication/database/migrations/2026_06_29_123952_add_two_factor_columns_to_users_table.php)
- [database/migrations/2026_08_01_060000_create_two_factor_trusted_devices_table.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/two-factor-authentication/database/migrations/2026_08_01_060000_create_two_factor_trusted_devices_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/two-factor-authentication/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
