# liberusoftware/integrations: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider adapter registry and protected connection lifecycle.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/integrations/composer.json) | `39a49babafc0` | [Variant 2](#variant-2) | 1 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/integrations/composer.json) | `68e5f07a6704` | [Variant 1](#variant-1) | 1 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/integrations/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 1 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/integrations/composer.json) | `3ade34046c3d` | [Variant 1](#variant-1) | 1 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/integrations/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 1 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/integrations/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 1 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/composer.json) | `63aad94e94c0` | [Variant 3](#variant-3) | 18 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/integrations/composer.json) | `b12a8c841c6a` | [Variant 1](#variant-1) | 1 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/integrations/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 1 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/integrations/composer.json) | `c267d625e264` | [Variant 1](#variant-1) | 1 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/integrations/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 1 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [integrations](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/integrations/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 1 |

Physical source locations: **12**. Reference variants: **3**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: automation-laravel, `integrations`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/integrations` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `integrations` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Integrations\\IntegrationsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/integrations/composer.json) · [module.json](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/integrations/module.json).

**Declared capabilities:** foundation.integrations

**Declared features:** Provider credentials, Adapter capabilities, OAuth boundaries, Rotation, Connection tests, Sync, Reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\Integrations\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/IntegrationAdapter.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/integrations/src/Contracts/IntegrationAdapter.php) | `public function name(): string`<br>`public function capabilities(): array`<br>`public function test(array $credentials): bool` |
| [src/Support/CredentialVault.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/integrations/src/Support/CredentialVault.php) | `public function seal(array $credentials): string`<br>`public function open(string $sealed): array` |
| [src/Support/IntegrationRegistry.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/integrations/src/Support/IntegrationRegistry.php) | `public function register(IntegrationAdapter $adapter): void`<br>`public function get(string $name): IntegrationAdapter`<br>`public function all(): array` |

Other non-legacy PHP sources: [src/IntegrationsServiceProvider.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/integrations/src/IntegrationsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_01_030100_create_integration_connections_table.php](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/integrations/database/migrations/2026_08_01_030100_create_integration_connections_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/integrations/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: accounting-erp-laravel, `integrations`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/integrations` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `integrations` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Integrations\\IntegrationsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/integrations/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/integrations/module.json).

**Declared capabilities:** foundation.integrations

**Declared features:** Provider credentials, Adapter capabilities, OAuth boundaries, Rotation, Connection tests, Sync, Reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\Integrations\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/IntegrationAdapter.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/integrations/src/Contracts/IntegrationAdapter.php) | `public function name(): string`<br>`public function capabilities(): array`<br>`public function test(array $credentials): bool` |
| [src/Contracts/PaymentProviderAdapter.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/integrations/src/Contracts/PaymentProviderAdapter.php) | `public function sendPayment(array $payment): array`<br>`public function sendBulkPayments(string $title, array $payments, ?string $scheduleFor = null): array` |
| [src/Support/CredentialVault.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/integrations/src/Support/CredentialVault.php) | `public function seal(array $credentials): string`<br>`public function open(string $sealed): array` |
| [src/Support/IntegrationRegistry.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/integrations/src/Support/IntegrationRegistry.php) | `public function register(IntegrationAdapter $adapter): void`<br>`public function get(string $name): IntegrationAdapter`<br>`public function all(): array` |

Other non-legacy PHP sources: [src/IntegrationsServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/integrations/src/IntegrationsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_01_030100_create_integration_connections_table.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/integrations/database/migrations/2026_08_01_030100_create_integration_connections_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/integrations/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 3

Representative: crm-laravel, `integrations`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/integrations` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `integrations` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Integrations\\IntegrationsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/composer.json) · [module.json](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/module.json).

**Declared capabilities:** foundation.integrations

**Declared features:** Provider credentials, Adapter capabilities, OAuth boundaries, Rotation, Connection tests, Sync, Reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\Integrations\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/IntegrationAdapter.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/src/Contracts/IntegrationAdapter.php) | `public function name(): string`<br>`public function capabilities(): array`<br>`public function test(array $credentials): bool` |
| [src/Support/CredentialVault.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/src/Support/CredentialVault.php) | `public function seal(array $credentials): string`<br>`public function open(string $sealed): array` |
| [src/Support/IntegrationRegistry.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/src/Support/IntegrationRegistry.php) | `public function register(IntegrationAdapter $adapter): void`<br>`public function get(string $name): IntegrationAdapter`<br>`public function all(): array` |

Other non-legacy PHP sources: [src/IntegrationsServiceProvider.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/src/IntegrationsServiceProvider.php).

**Legacy review:** 79 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2023_05_20_000000_create_call_settings_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2023_05_20_000000_create_call_settings_table.php)
- [database/migrations/2024_01_10_000000_create_oauth_configurations_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2024_01_10_000000_create_oauth_configurations_table.php)
- [database/migrations/2024_10_13_000000_create_accounting_integrations_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2024_10_13_000000_create_accounting_integrations_table.php)
- [database/migrations/2024_10_22_000000_create_whatsapp_numbers_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2024_10_22_000000_create_whatsapp_numbers_table.php)
- [database/migrations/2026_02_16_000000_add_fields_to_oauth_configurations_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2026_02_16_000000_add_fields_to_oauth_configurations_table.php)
- [database/migrations/2026_07_08_000000_create_sso_connections_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2026_07_08_000000_create_sso_connections_table.php)
- [database/migrations/2026_07_08_000001_encrypt_oauth_configuration_client_secret.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2026_07_08_000001_encrypt_oauth_configuration_client_secret.php)
- [database/migrations/2026_07_08_010000_add_jit_to_sso_connections_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2026_07_08_010000_add_jit_to_sso_connections_table.php)
- [database/migrations/2026_07_08_020000_add_require_sso_to_sso_connections_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2026_07_08_020000_add_require_sso_to_sso_connections_table.php)
- [database/migrations/2026_07_08_050000_add_token_auth_method_to_sso_connections_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2026_07_08_050000_add_token_auth_method_to_sso_connections_table.php)
- [database/migrations/2026_07_08_090000_create_saml_connections_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2026_07_08_090000_create_saml_connections_table.php)
- [database/migrations/2026_07_10_020000_add_jit_to_saml_connections_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2026_07_10_020000_add_jit_to_saml_connections_table.php)
- [database/migrations/2026_07_10_030000_add_slo_url_to_saml_connections_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2026_07_10_030000_add_slo_url_to_saml_connections_table.php)
- [database/migrations/2026_08_01_030100_create_integration_connections_table.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2026_08_01_030100_create_integration_connections_table.php)
- [database/migrations/2026_08_30_000002_add_oauth_tokens_to_configurations.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2026_08_30_000002_add_oauth_tokens_to_configurations.php)
- [database/migrations/2026_08_31_000000_ensure_require_sso_columns.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/database/migrations/2026_08_31_000000_ensure_require_sso_columns.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **18**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/.gitkeep)
- [tests/Feature/Saml/SamlAcsTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Saml/SamlAcsTest.php)
- [tests/Feature/Saml/SamlJitTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Saml/SamlJitTest.php)
- [tests/Feature/Saml/SamlLoginRedirectTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Saml/SamlLoginRedirectTest.php)
- [tests/Feature/Saml/SamlSloTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Saml/SamlSloTest.php)
- [tests/Feature/Saml/SignsSamlResponses.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Saml/SignsSamlResponses.php)
- [tests/Feature/Sso/OidcSingleLogoutTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Sso/OidcSingleLogoutTest.php)
- [tests/Feature/Sso/SamlConfigTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Sso/SamlConfigTest.php)
- [tests/Feature/Sso/SamlValidateConnectionTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Sso/SamlValidateConnectionTest.php)
- [tests/Feature/Sso/SsoClientAuthTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Sso/SsoClientAuthTest.php)
- [tests/Feature/Sso/SsoEnforcementTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Sso/SsoEnforcementTest.php)
- [tests/Feature/Sso/SsoGroupMappingTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Sso/SsoGroupMappingTest.php)
- [tests/Feature/Sso/SsoIdTokenTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Sso/SsoIdTokenTest.php)
- [tests/Feature/Sso/SsoJitProvisioningTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Sso/SsoJitProvisioningTest.php)
- [tests/Feature/Sso/SsoLoginTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Sso/SsoLoginTest.php)
- [tests/Feature/Sso/SsoLogoutAuditTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Sso/SsoLogoutAuditTest.php)
- [tests/Feature/Sso/SsoPkceTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Sso/SsoPkceTest.php)
- [tests/Feature/Sso/SsoTestConnectionTest.php](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/integrations/tests/Feature/Sso/SsoTestConnectionTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
