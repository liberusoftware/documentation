# liberusoftware/identity-socialstream: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Socialstream/Socialite identity-linking provider adapter.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 1 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/identity-socialstream/composer.json) | `68e5f07a6704` | [Variant 1](#variant-1) | 1 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/identity-socialstream/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 1 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/identity-socialstream/composer.json) | `3ade34046c3d` | [Variant 1](#variant-1) | 1 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/identity-socialstream/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 1 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/identity-socialstream/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 1 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/composer.json) | `63aad94e94c0` | [Variant 3](#variant-3) | 1 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/identity-socialstream/composer.json) | `b12a8c841c6a` | [Variant 1](#variant-1) | 1 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/composer.json) | `577e93db23cc` | [Variant 2](#variant-2) | 1 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/identity-socialstream/composer.json) | `c267d625e264` | [Variant 1](#variant-1) | 1 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/identity-socialstream/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 1 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [identity-socialstream](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/identity-socialstream/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 1 |

Physical source locations: **12**. Reference variants: **3**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `identity-socialstream`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/identity-socialstream` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `identity-socialstream` |
| Module version field | `1.4.1` |
| Category / layers | `"adapter"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Identity\\Socialstream\\Providers\\SocialstreamServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/module.json).

**Declared capabilities:** identity.socialstream

**Declared features:** Social provider redirects, Callbacks, Identity linking, Protected credentials, Account synchronization

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `bursteri/socialstream` | `^7.0` |
| `laravel/socialite` | `^5.0` |
| `liberusoftware/identity-core` | `^1.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\Identity\\Socialstream\\": "src/", "Liberu\\Foundation\\Identity\\Socialstream\\Database\\Factories\\": "database/factories/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/identity-core": "^1.0", "liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateConnectedAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/CreateConnectedAccount.php) | `public function create(mixed $user, string $provider, ProviderUser $providerUser): ConnectedAccount` |
| [src/Actions/CreateUserFromProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/CreateUserFromProvider.php) | `public function __construct(CreatesConnectedAccounts $createsConnectedAccounts)`<br>`public function create(string $provider, ProviderUserContract $providerUser): User` |
| [src/Actions/GenerateRedirectForProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/GenerateRedirectForProvider.php) | `public function generate(string $provider): RedirectResponse` |
| [src/Actions/HandleInvalidState.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/HandleInvalidState.php) | `public function handle(InvalidStateException $exception): Response` |
| [src/Actions/ResolveSocialiteUser.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/ResolveSocialiteUser.php) | `public function resolve(string $provider): User` |
| [src/Actions/SetUserPassword.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/SetUserPassword.php) | `public function set(mixed $user, array $input): void` |
| [src/Actions/UpdateConnectedAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Actions/UpdateConnectedAccount.php) | `public function update(mixed $user, ConnectedAccount $connectedAccount, string $provider, User $providerUser): ConnectedAccount`<br>`public function updateRefreshToken(ConnectedAccount $connectedAccount): ConnectedAccount` |
| [src/Contracts/ConnectedAccountOwner.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Contracts/ConnectedAccountOwner.php) | `public function ownsConnectedAccount($account)` |
| [src/Policies/ConnectedAccountPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Policies/ConnectedAccountPolicy.php) | `public function viewAny(ConnectedAccountOwner $user): bool`<br>`public function view(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool`<br>`public function create(ConnectedAccountOwner $user): bool`<br>`public function update(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool`<br>`public function delete(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool` |

Other non-legacy PHP sources: [src/Models/ConnectedAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Models/ConnectedAccount.php) · [src/Providers/SocialstreamServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/src/Providers/SocialstreamServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_06_29_123954_make_password_nullable_on_users_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/database/migrations/2026_06_29_123954_make_password_nullable_on_users_table.php)
- [database/migrations/2026_06_29_123955_create_connected_accounts_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/database/migrations/2026_06_29_123955_create_connected_accounts_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/identity-socialstream/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: project-genealogy-laravel-filament, `identity-socialstream`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/identity-socialstream` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `identity-socialstream` |
| Module version field | `1.4.1` |
| Category / layers | `"adapter"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Identity\\Socialstream\\Providers\\SocialstreamServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/composer.json) · [module.json](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/module.json).

**Declared capabilities:** identity.socialstream

**Declared features:** Social provider redirects, Callbacks, Identity linking, Protected credentials, Account synchronization

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `bursteri/socialstream` | `^7.0` |
| `laravel/socialite` | `^5.0` |
| `liberusoftware/identity-core` | `^1.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\Identity\\Socialstream\\": "src/", "Liberu\\Foundation\\Identity\\Socialstream\\Database\\Factories\\": "database/factories/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/identity-core": "^1.0", "liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateConnectedAccount.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/src/Actions/CreateConnectedAccount.php) | `public function create(mixed $user, string $provider, ProviderUser $providerUser): ConnectedAccount` |
| [src/Actions/CreateUserFromProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/src/Actions/CreateUserFromProvider.php) | `public function __construct(CreatesConnectedAccounts $createsConnectedAccounts)`<br>`public function create(string $provider, ProviderUserContract $providerUser): User` |
| [src/Actions/GenerateRedirectForProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/src/Actions/GenerateRedirectForProvider.php) | `public function generate(string $provider): RedirectResponse` |
| [src/Actions/HandleInvalidState.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/src/Actions/HandleInvalidState.php) | `public function handle(InvalidStateException $exception): Response` |
| [src/Actions/ResolveSocialiteUser.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/src/Actions/ResolveSocialiteUser.php) | `public function resolve(string $provider): User` |
| [src/Actions/SetUserPassword.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/src/Actions/SetUserPassword.php) | `public function set(mixed $user, array $input): void` |
| [src/Actions/UpdateConnectedAccount.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/src/Actions/UpdateConnectedAccount.php) | `public function update(mixed $user, ConnectedAccount $connectedAccount, string $provider, User $providerUser): ConnectedAccount`<br>`public function updateRefreshToken(ConnectedAccount $connectedAccount): ConnectedAccount` |
| [src/Contracts/ConnectedAccountOwner.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/src/Contracts/ConnectedAccountOwner.php) | `public function ownsConnectedAccount($account)` |
| [src/Policies/ConnectedAccountPolicy.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/src/Policies/ConnectedAccountPolicy.php) | `public function viewAny(ConnectedAccountOwner $user): bool`<br>`public function view(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool`<br>`public function create(ConnectedAccountOwner $user): bool`<br>`public function update(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool`<br>`public function delete(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool` |

Other non-legacy PHP sources: [src/Models/ConnectedAccount.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/src/Models/ConnectedAccount.php) · [src/Providers/SocialstreamServiceProvider.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/src/Providers/SocialstreamServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_06_29_123954_make_password_nullable_on_users_table.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/database/migrations/2026_06_29_123954_make_password_nullable_on_users_table.php)
- [database/migrations/2026_06_29_123955_create_connected_accounts_table.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/database/migrations/2026_06_29_123955_create_connected_accounts_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/identity-socialstream/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 3

Representative: project-crm-laravel-filament, `identity-socialstream`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/identity-socialstream` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `identity-socialstream` |
| Module version field | `1.4.1` |
| Category / layers | `"adapter"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Identity\\Socialstream\\Providers\\SocialstreamServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/module.json).

**Declared capabilities:** identity.socialstream

**Declared features:** Social provider redirects, Callbacks, Identity linking, Protected credentials, Account synchronization

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `bursteri/socialstream` | `^7.0` |
| `laravel/socialite` | `^5.0` |
| `liberusoftware/identity-core` | `^1.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\Identity\\Socialstream\\": "src/", "Liberu\\Foundation\\Identity\\Socialstream\\Database\\Factories\\": "database/factories/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/identity-core": "^1.0", "liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateConnectedAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/src/Actions/CreateConnectedAccount.php) | `public function create(mixed $user, string $provider, ProviderUser $providerUser): ConnectedAccount` |
| [src/Actions/CreateUserFromProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/src/Actions/CreateUserFromProvider.php) | `public function __construct(CreatesConnectedAccounts $createsConnectedAccounts)`<br>`public function create(string $provider, ProviderUserContract $providerUser): User` |
| [src/Actions/GenerateRedirectForProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/src/Actions/GenerateRedirectForProvider.php) | `public function generate(string $provider): RedirectResponse` |
| [src/Actions/HandleInvalidState.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/src/Actions/HandleInvalidState.php) | `public function handle(InvalidStateException $exception): Response` |
| [src/Actions/ResolveSocialiteUser.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/src/Actions/ResolveSocialiteUser.php) | `public function resolve(string $provider): User` |
| [src/Actions/SetUserPassword.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/src/Actions/SetUserPassword.php) | `public function set(mixed $user, array $input): void` |
| [src/Actions/UpdateConnectedAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/src/Actions/UpdateConnectedAccount.php) | `public function update(mixed $user, ConnectedAccount $connectedAccount, string $provider, User $providerUser): ConnectedAccount`<br>`public function updateRefreshToken(ConnectedAccount $connectedAccount): ConnectedAccount` |
| [src/Contracts/ConnectedAccountOwner.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/src/Contracts/ConnectedAccountOwner.php) | `public function ownsConnectedAccount($account)` |
| [src/Policies/ConnectedAccountPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/src/Policies/ConnectedAccountPolicy.php) | `public function viewAny(ConnectedAccountOwner $user): bool`<br>`public function view(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool`<br>`public function create(ConnectedAccountOwner $user): bool`<br>`public function update(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool`<br>`public function delete(ConnectedAccountOwner $user, ConnectedAccount $connectedAccount): bool` |

Other non-legacy PHP sources: [src/Models/ConnectedAccount.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/src/Models/ConnectedAccount.php) · [src/Providers/SocialstreamServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/src/Providers/SocialstreamServiceProvider.php).

**Legacy review:** 10 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/0001_01_01_000002_create_connected_accounts_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/database/migrations/0001_01_01_000002_create_connected_accounts_table.php)
- [database/migrations/2024_02_15_000003_enhance_oauth_and_contacts.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/database/migrations/2024_02_15_000003_enhance_oauth_and_contacts.php)
- [database/migrations/2026_06_29_123954_make_password_nullable_on_users_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/database/migrations/2026_06_29_123954_make_password_nullable_on_users_table.php)
- [database/migrations/2026_06_29_123955_create_connected_accounts_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/database/migrations/2026_06_29_123955_create_connected_accounts_table.php)
- [database/migrations/2026_07_08_000003_encrypt_connected_account_tokens.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/database/migrations/2026_07_08_000003_encrypt_connected_account_tokens.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/identity-socialstream/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
