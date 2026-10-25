# liberusoftware/sessions-devices: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Privacy-conscious session inventory and revocation.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/sessions-devices/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 1 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/sessions-devices/composer.json) | `68e5f07a6704` | [Variant 1](#variant-1) | 1 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/sessions-devices/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 1 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/sessions-devices/composer.json) | `3ade34046c3d` | [Variant 1](#variant-1) | 1 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/sessions-devices/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 1 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/sessions-devices/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 1 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/sessions-devices/composer.json) | `63aad94e94c0` | [Variant 2](#variant-2) | 1 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/sessions-devices/composer.json) | `b12a8c841c6a` | [Variant 1](#variant-1) | 1 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/sessions-devices/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 1 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/sessions-devices/composer.json) | `c267d625e264` | [Variant 1](#variant-1) | 1 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/sessions-devices/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 1 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [sessions-devices](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/sessions-devices/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 1 |

Physical source locations: **12**. Reference variants: **2**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `sessions-devices`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/sessions-devices` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `sessions-devices` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Sessions\\SessionsDevicesServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/sessions-devices/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/sessions-devices/module.json).

**Declared capabilities:** identity.sessions

**Declared features:** Privacy-conscious active-session inventory, Current-session protection, Revocation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/identity-core` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\Sessions\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/identity-core": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Queries/SessionReader.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/sessions-devices/src/Queries/SessionReader.php) | `public function forActor(string\|int $actorId, ?string $currentId = null): Collection`<br>`public function revoke(string\|int $actorId, string $sessionId, ?string $currentId = null): bool`<br>`public function revokeOthers(string\|int $actorId, string $currentId): int` |

Other non-legacy PHP sources: [src/SessionsDevicesServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/sessions-devices/src/SessionsDevicesServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/0001_01_01_000003_create_sessions_table.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/sessions-devices/database/migrations/0001_01_01_000003_create_sessions_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/sessions-devices/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: crm-laravel, `sessions-devices`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/sessions-devices` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `sessions-devices` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Sessions\\SessionsDevicesServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/sessions-devices/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/sessions-devices/module.json).

**Declared capabilities:** identity.sessions

**Declared features:** Privacy-conscious active-session inventory, Current-session protection, Revocation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/identity-core` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\Sessions\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/identity-core": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Queries/SessionReader.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/sessions-devices/src/Queries/SessionReader.php) | `public function forActor(string\|int $actorId, ?string $currentId = null): Collection`<br>`public function revoke(string\|int $actorId, string $sessionId, ?string $currentId = null): bool`<br>`public function revokeOthers(string\|int $actorId, string $currentId): int` |

Other non-legacy PHP sources: [src/SessionsDevicesServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/sessions-devices/src/SessionsDevicesServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/0001_01_01_000003_create_sessions_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/sessions-devices/database/migrations/0001_01_01_000003_create_sessions_table.php)
- [database/migrations/2019_12_14_000001_create_personal_access_tokens_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/sessions-devices/database/migrations/2019_12_14_000001_create_personal_access_tokens_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/sessions-devices/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
