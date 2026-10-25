# liberusoftware/identity-core-filament: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Filament administration adapter for the configured Liberu identity model.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/composer.json) | `39a49babafc0` | [Variant 2](#variant-2) | 6 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/automation-laravel/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/identity-core-filament/composer.json) | `68e5f07a6704` | [Variant 2](#variant-2) | 6 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/identity-core-filament/composer.json) | `4743bdfebd1c` | [Variant 2](#variant-2) | 6 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/boilerplate-laravel/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/identity-core-filament/composer.json) | `3ade34046c3d` | [Variant 2](#variant-2) | 6 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/identity-core-filament/composer.json) | `790fdffebd3a` | [Variant 2](#variant-2) | 6 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/control-panel-laravel/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/identity-core-filament/composer.json) | `1797f25d705f` | [Variant 2](#variant-2) | 6 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/crm-laravel/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-core-filament/composer.json) | `63aad94e94c0` | [Variant 2](#variant-2) | 6 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/identity-core-filament/composer.json) | `b12a8c841c6a` | [Variant 2](#variant-2) | 6 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/genealogy-laravel/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-core-filament/composer.json) | `577e93db23cc` | [Variant 2](#variant-2) | 6 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/identity-core-filament/composer.json) | `c267d625e264` | [Variant 2](#variant-2) | 6 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 6 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [identity-core-filament](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/identity-core-filament/composer.json) | `08bbc484b50f` | [Variant 2](#variant-2) | 6 |

Physical source locations: **12**. Reference variants: **2**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: real-estate-laravel, `identity-core-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/identity-core-filament` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `identity-core-filament` |
| Module version field | `1.4.1` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\IdentityFilament\\IdentityFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/composer.json) · [module.json](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/module.json).

**Declared capabilities:** foundation.identity.filament

**Declared features:** Optional Filament user and role administration surface

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.1` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `liberusoftware/roles-permissions` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\IdentityFilament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/organizations-teams": "^1.0", "liberusoftware/roles-permissions": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/IdentityFilamentPlugin.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/src/IdentityFilamentPlugin.php) · [src/IdentityFilamentServiceProvider.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/src/IdentityFilamentServiceProvider.php) · [src/Resources/UserResource.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/src/Resources/UserResource.php) · [src/Resources/UserResource/Pages/CreateUser.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/src/Resources/UserResource/Pages/CreateUser.php) · [src/Resources/UserResource/Pages/EditUser.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/src/Resources/UserResource/Pages/EditUser.php) · [src/Resources/UserResource/Pages/ListUsers.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/src/Resources/UserResource/Pages/ListUsers.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **6**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/tests/.gitkeep)
- [tests/Feature/UserResourceTest.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/tests/Feature/UserResourceTest.php)
- [tests/Fixtures/RoledUser.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/tests/Fixtures/RoledUser.php)
- [tests/Fixtures/TestPanelProvider.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/tests/Fixtures/TestPanelProvider.php)
- [tests/Pest.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/tests/Pest.php)
- [tests/TestCase.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-core-filament/tests/TestCase.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: accounting-erp-laravel, `identity-core-filament`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/identity-core-filament` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `identity-core-filament` |
| Module version field | `1.4.1` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\IdentityFilament\\IdentityFilamentServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/module.json).

**Declared capabilities:** foundation.identity.filament

**Declared features:** Optional Filament user and role administration surface

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `filament/filament` | `^5.1` |
| `liberusoftware/roles-permissions` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\IdentityFilament\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/roles-permissions": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

No files were found in the indexed contract/action/query/policy/service/presentation roots. Check provider/module classes and the complete source tree; this is not a claim that the package has no behavior.

Other non-legacy PHP sources: [src/IdentityFilamentPlugin.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/src/IdentityFilamentPlugin.php) · [src/IdentityFilamentServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/src/IdentityFilamentServiceProvider.php) · [src/Resources/UserResource.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/src/Resources/UserResource.php) · [src/Resources/UserResource/Pages/CreateUser.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/src/Resources/UserResource/Pages/CreateUser.php) · [src/Resources/UserResource/Pages/EditUser.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/src/Resources/UserResource/Pages/EditUser.php) · [src/Resources/UserResource/Pages/ListUsers.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/src/Resources/UserResource/Pages/ListUsers.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **6**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/tests/.gitkeep)
- [tests/Feature/UserResourceTest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/tests/Feature/UserResourceTest.php)
- [tests/Fixtures/RoledUser.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/tests/Fixtures/RoledUser.php)
- [tests/Fixtures/TestPanelProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/tests/Fixtures/TestPanelProvider.php)
- [tests/Pest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/tests/Pest.php)
- [tests/TestCase.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-core-filament/tests/TestCase.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
