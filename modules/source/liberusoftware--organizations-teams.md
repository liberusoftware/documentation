# liberusoftware/organizations-teams: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Organization, team, membership, invitation, ownership, and context foundation.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/composer.json) | `39a49babafc0` | [Variant 3](#variant-3) | 1 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/composer.json) | `68e5f07a6704` | [Variant 2](#variant-2) | 1 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/organizations-teams/composer.json) | `4743bdfebd1c` | [Variant 3](#variant-3) | 1 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/composer.json) | `3ade34046c3d` | [Variant 2](#variant-2) | 1 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/organizations-teams/composer.json) | `790fdffebd3a` | [Variant 2](#variant-2) | 1 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/organizations-teams/composer.json) | `1797f25d705f` | [Variant 3](#variant-3) | 1 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/composer.json) | `63aad94e94c0` | [Variant 1](#variant-1) | 13 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/organizations-teams/composer.json) | `b12a8c841c6a` | [Variant 2](#variant-2) | 1 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/organizations-teams/composer.json) | `577e93db23cc` | [Variant 2](#variant-2) | 1 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/organizations-teams/composer.json) | `c267d625e264` | [Variant 3](#variant-3) | 1 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/organizations-teams/composer.json) | `178d8015b601` | [Variant 3](#variant-3) | 1 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [organizations-teams](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/organizations-teams/composer.json) | `08bbc484b50f` | [Variant 2](#variant-2) | 1 |

Physical source locations: **12**. Reference variants: **3**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-crm-laravel-filament, `organizations-teams`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/organizations-teams` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `organizations-teams` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Organizations\\OrganizationsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/module.json).

**Declared capabilities:** foundation.organizations, foundation.teams

**Declared features:** Teams, Memberships, Invitations, Ownership, Switching, Current-context boundaries

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `laravel/jetstream` | `^5.1` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |
| `spatie/laravel-activitylog` | `^5.0` |

PSR-4 mappings: `{"Liberu\\Foundation\\Organizations\\": "src/", "Liberu\\Foundation\\Organizations\\Database\\Factories\\": "database/factories/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AcceptInvitation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/AcceptInvitation.php) | `public function handle(string $token, Authenticatable $actor, string $email): void` |
| [src/Actions/InviteMember.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/InviteMember.php) | `public function handle(int $teamId, string $email, string $role, int\|string $inviterId, ?\DateTimeImmutable $expiresAt = null): string` |
| [src/Actions/TransferOwnership.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/TransferOwnership.php) | `public function handle(Team $team, int\|string $currentOwner, int\|string $successor, bool $recentlyAuthenticated): void` |
| [src/Contracts/OrganizationActor.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Contracts/OrganizationActor.php) | `public function belongsToTeam($team)`<br>`public function ownsTeam($team)` |
| [src/Policies/TeamPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Policies/TeamPolicy.php) | `public function viewAny(OrganizationActor $user): bool`<br>`public function view(OrganizationActor $user, Team $team): bool`<br>`public function create(OrganizationActor $user): bool`<br>`public function update(OrganizationActor $user, Team $team): bool`<br>`public function addTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function updateTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function removeTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function delete(OrganizationActor $user, Team $team): bool` |
| [src/Services/CurrentTeamResolver.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Services/CurrentTeamResolver.php) | `public function resolve(Authenticatable $actor, int\|string\|null $requested): ?Team` |
| [src/Support/MembershipRolePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Support/MembershipRolePolicy.php) | `public function allows(string $role): bool`<br>`public function normalize(string $role): ?string` |

Other non-legacy PHP sources: [src/Models/Membership.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Models/Membership.php) · [src/Models/Organization.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Models/Organization.php) · [src/Models/Team.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Models/Team.php) · [src/Models/TeamInvitation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Models/TeamInvitation.php) · [src/OrganizationsServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/OrganizationsServiceProvider.php).

**Legacy review:** 68 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2020_05_21_100000_create_teams_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2020_05_21_100000_create_teams_table.php)
- [database/migrations/2020_05_21_200000_create_team_user_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2020_05_21_200000_create_team_user_table.php)
- [database/migrations/2020_05_21_300000_create_team_invitations_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2020_05_21_300000_create_team_invitations_table.php)
- [database/migrations/2024_01_10_000000_create_team_subscriptions_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2024_01_10_000000_create_team_subscriptions_table.php)
- [database/migrations/2024_09_29_093707_add_team_to_resources.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2024_09_29_093707_add_team_to_resources.php)
- [database/migrations/2024_11_17_000000_add_team_id_to-staff_resource_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2024_11_17_000000_add_team_id_to-staff_resource_tables.php)
- [database/migrations/2026_07_06_000001_add_team_id_to_tenant_scoped_tables.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_06_000001_add_team_id_to_tenant_scoped_tables.php)
- [database/migrations/2026_07_06_000002_enable_spatie_teams_columns.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_06_000002_enable_spatie_teams_columns.php)
- [database/migrations/2026_07_06_190000_add_archived_at_to_teams_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_06_190000_add_archived_at_to_teams_table.php)
- [database/migrations/2026_07_06_200000_create_team_backups_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_06_200000_create_team_backups_table.php)
- [database/migrations/2026_07_07_120000_add_team_id_to_tickets_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_07_120000_add_team_id_to_tickets_table.php)
- [database/migrations/2026_07_08_030000_create_territories_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_08_030000_create_territories_table.php)
- [database/migrations/2026_07_08_030001_create_territory_user_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_08_030001_create_territory_user_table.php)
- [database/migrations/2026_07_08_080000_add_portal_branding_to_teams_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_08_080000_add_portal_branding_to_teams_table.php)
- [database/migrations/2026_07_08_100000_add_portal_logo_path_to_teams_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_07_08_100000_add_portal_logo_path_to_teams_table.php)
- [database/migrations/2026_08_01_061000_harden_organization_memberships.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_08_01_061000_harden_organization_memberships.php)
- [database/migrations/2026_08_24_050000_make_legacy_invitation_token_nullable.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_08_24_050000_make_legacy_invitation_token_nullable.php)
- [database/migrations/2026_08_25_000001_add_zernio_profile_id_to_teams.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_08_25_000001_add_zernio_profile_id_to_teams.php)
- [database/migrations/2026_08_30_000001_add_saas_billing_fields_to_team_subscriptions.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_08_30_000001_add_saas_billing_fields_to_team_subscriptions.php)
- [database/migrations/2026_09_06_000000_add_setup_completed_at_to_teams_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/database/migrations/2026_09_06_000000_add_setup_completed_at_to_teams_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **13**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/tests/.gitkeep)
- [tests/Feature/Teams/BackupTeamCommandTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/tests/Feature/Teams/BackupTeamCommandTest.php)
- [tests/Feature/Teams/CloneTeamCommandTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/tests/Feature/Teams/CloneTeamCommandTest.php)
- [tests/Feature/Teams/GenerateTeamBackupJobTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/tests/Feature/Teams/GenerateTeamBackupJobTest.php)
- [tests/Feature/Teams/ImportTeamBackupJobTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/tests/Feature/Teams/ImportTeamBackupJobTest.php)
- [tests/Feature/Teams/ImportTeamBackupServiceTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/tests/Feature/Teams/ImportTeamBackupServiceTest.php)
- [tests/Feature/Teams/ImportTeamCommandTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/tests/Feature/Teams/ImportTeamCommandTest.php)
- [tests/Feature/Teams/RestoreTeamBackupJobTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/tests/Feature/Teams/RestoreTeamBackupJobTest.php)
- [tests/Feature/Teams/RestoreTeamCommandTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/tests/Feature/Teams/RestoreTeamCommandTest.php)
- [tests/Feature/Teams/TeamArchiveTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/tests/Feature/Teams/TeamArchiveTest.php)
- [tests/Feature/Teams/TeamBackupServiceTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/tests/Feature/Teams/TeamBackupServiceTest.php)
- [tests/Feature/Teams/TeamCloneServiceTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/tests/Feature/Teams/TeamCloneServiceTest.php)
- [tests/Feature/Teams/TeamRestoreServiceTest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/tests/Feature/Teams/TeamRestoreServiceTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: project-automation-laravel-filament, `organizations-teams`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/organizations-teams` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `organizations-teams` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Organizations\\OrganizationsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/composer.json) · [module.json](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/module.json).

**Declared capabilities:** foundation.organizations, foundation.teams

**Declared features:** Teams, Memberships, Invitations, Ownership, Switching, Current-context boundaries

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `laravel/jetstream` | `^5.1` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |
| `spatie/laravel-activitylog` | `^5.0` |

PSR-4 mappings: `{"Liberu\\Foundation\\Organizations\\": "src/", "Liberu\\Foundation\\Organizations\\Database\\Factories\\": "database/factories/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AcceptInvitation.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/src/Actions/AcceptInvitation.php) | `public function handle(string $token, Authenticatable $actor, string $email): void` |
| [src/Actions/InviteMember.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/src/Actions/InviteMember.php) | `public function handle(int $teamId, string $email, string $role, int\|string $inviterId, ?\DateTimeImmutable $expiresAt = null): string` |
| [src/Actions/TransferOwnership.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/src/Actions/TransferOwnership.php) | `public function handle(Team $team, int\|string $currentOwner, int\|string $successor, bool $recentlyAuthenticated): void` |
| [src/Contracts/OrganizationActor.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/src/Contracts/OrganizationActor.php) | `public function belongsToTeam($team)`<br>`public function ownsTeam($team)` |
| [src/Policies/TeamPolicy.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/src/Policies/TeamPolicy.php) | `public function viewAny(OrganizationActor $user): bool`<br>`public function view(OrganizationActor $user, Team $team): bool`<br>`public function create(OrganizationActor $user): bool`<br>`public function update(OrganizationActor $user, Team $team): bool`<br>`public function addTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function updateTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function removeTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function delete(OrganizationActor $user, Team $team): bool` |
| [src/Services/CurrentTeamResolver.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/src/Services/CurrentTeamResolver.php) | `public function resolve(Authenticatable $actor, int\|string\|null $requested): ?Team` |

Other non-legacy PHP sources: [src/Models/Membership.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/src/Models/Membership.php) · [src/Models/Organization.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/src/Models/Organization.php) · [src/Models/Team.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/src/Models/Team.php) · [src/Models/TeamInvitation.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/src/Models/TeamInvitation.php) · [src/OrganizationsServiceProvider.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/src/OrganizationsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2020_05_21_100000_create_teams_table.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/database/migrations/2020_05_21_100000_create_teams_table.php)
- [database/migrations/2020_05_21_200000_create_team_user_table.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/database/migrations/2020_05_21_200000_create_team_user_table.php)
- [database/migrations/2020_05_21_300000_create_team_invitations_table.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/database/migrations/2020_05_21_300000_create_team_invitations_table.php)
- [database/migrations/2026_08_01_061000_harden_organization_memberships.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/database/migrations/2026_08_01_061000_harden_organization_memberships.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/organizations-teams/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 3

Representative: project-accounting-erp-laravel-filament, `organizations-teams`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/organizations-teams` |
| Composer version field | `1.5.0` |
| Package type | `liberu-module` |
| Module manifest name | `organizations-teams` |
| Module version field | `1.5.0` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\Organizations\\OrganizationsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/module.json).

**Declared capabilities:** foundation.organizations, foundation.teams

**Declared features:** Teams, Memberships, Invitations, Ownership, Switching, Current-context boundaries

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `laravel/jetstream` | `^5.1` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |
| `spatie/laravel-activitylog` | `^5.0` |

PSR-4 mappings: `{"Liberu\\Foundation\\Organizations\\": "src/", "Liberu\\Foundation\\Organizations\\Database\\Factories\\": "database/factories/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AcceptInvitation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/src/Actions/AcceptInvitation.php) | `public function handle(string $token, Authenticatable $actor, string $email): void` |
| [src/Actions/InviteMember.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/src/Actions/InviteMember.php) | `public function handle(int $teamId, string $email, string $role, int\|string $inviterId, ?\DateTimeImmutable $expiresAt = null): string` |
| [src/Actions/TransferOwnership.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/src/Actions/TransferOwnership.php) | `public function handle(Team $team, int\|string $currentOwner, int\|string $successor, bool $recentlyAuthenticated): void` |
| [src/Contracts/OrganizationActor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/src/Contracts/OrganizationActor.php) | `public function belongsToTeam($team)`<br>`public function ownsTeam($team)` |
| [src/Policies/TeamPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/src/Policies/TeamPolicy.php) | `public function viewAny(OrganizationActor $user): bool`<br>`public function view(OrganizationActor $user, Team $team): bool`<br>`public function create(OrganizationActor $user): bool`<br>`public function update(OrganizationActor $user, Team $team): bool`<br>`public function addTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function updateTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function removeTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function delete(OrganizationActor $user, Team $team): bool` |
| [src/Services/CurrentTeamResolver.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/src/Services/CurrentTeamResolver.php) | `public function resolve(Authenticatable $actor, int\|string\|null $requested): ?Team` |

Other non-legacy PHP sources: [src/Models/Membership.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/src/Models/Membership.php) · [src/Models/Organization.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/src/Models/Organization.php) · [src/Models/Team.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/src/Models/Team.php) · [src/Models/TeamInvitation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/src/Models/TeamInvitation.php) · [src/OrganizationsServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/src/OrganizationsServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2020_05_21_100000_create_teams_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/database/migrations/2020_05_21_100000_create_teams_table.php)
- [database/migrations/2020_05_21_200000_create_team_user_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/database/migrations/2020_05_21_200000_create_team_user_table.php)
- [database/migrations/2020_05_21_300000_create_team_invitations_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/database/migrations/2020_05_21_300000_create_team_invitations_table.php)
- [database/migrations/2026_08_01_061000_harden_organization_memberships.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/database/migrations/2026_08_01_061000_harden_organization_memberships.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/organizations-teams/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
