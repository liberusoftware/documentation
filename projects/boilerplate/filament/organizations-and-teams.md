# Boilerplate: Organizations and Teams Filament presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#organizations-and-teams). Observed identity: [`liberusoftware/organizations-teams-filament`](../../../modules/source/liberusoftware--organizations-teams-filament.md). This retained spelling maps to `organizations-teams`; it is not another independent module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-organizations-and-teams-filament`
**Matching core package:** [`module-organizations-and-teams`](../core/organizations-and-teams.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Organizations, teams, memberships, invitations, ownership, switching, transfer, and lifecycle.

## Adapter implementation plan

This package presents the Organizations and Teams core capability through Filament 5. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Provide responsive, keyboard-accessible, localized workflows with clear loading, validation, empty, denied, queued, failure, and recovery states.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Organizations and Teams core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-organizations-teams-filament`](https://github.com/liberusoftware/module-organizations-teams-filament) (`liberusoftware/organizations-teams-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/organizations-and-teams.md) · [API plan](../api/organizations-and-teams.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Organizations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `organizations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Teams** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `teams`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Memberships** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `memberships`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Invitations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `invitations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ownership** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ownership`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Switching** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `switching`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transfer** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transfer`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [OrganizationsFilamentPlugin.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/organizations-teams-filament/src/OrganizationsFilamentPlugin.php) · [OrganizationsFilamentServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/organizations-teams-filament/src/OrganizationsFilamentServiceProvider.php) · [TeamResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/organizations-teams-filament/src/Resources/TeamResource.php) · [CreateTeam.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/organizations-teams-filament/src/Resources/TeamResource/Pages/CreateTeam.php) · [EditTeam.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/organizations-teams-filament/src/Resources/TeamResource/Pages/EditTeam.php) · [ListTeams.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/organizations-teams-filament/src/Resources/TeamResource/Pages/ListTeams.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AcceptInvitation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/AcceptInvitation.php) | `public function handle(string $token, Authenticatable $actor, string $email): void` |
| [InviteMember.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/InviteMember.php) | `public function handle(int $teamId, string $email, string $role, int\|string $inviterId, ?\DateTimeImmutable $expiresAt = null): string` |
| [TransferOwnership.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Actions/TransferOwnership.php) | `public function handle(Team $team, int\|string $currentOwner, int\|string $successor, bool $recentlyAuthenticated): void` |
| [OrganizationActor.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Contracts/OrganizationActor.php) | `public function belongsToTeam($team)`<br>`public function ownsTeam($team)` |
| [TeamPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Policies/TeamPolicy.php) | `public function viewAny(OrganizationActor $user): bool`<br>`public function view(OrganizationActor $user, Team $team): bool`<br>`public function create(OrganizationActor $user): bool`<br>`public function update(OrganizationActor $user, Team $team): bool`<br>`public function addTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function updateTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function removeTeamMember(OrganizationActor $user, Team $team): bool`<br>`public function delete(OrganizationActor $user, Team $team): bool` |
| [CurrentTeamResolver.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/organizations-teams/src/Services/CurrentTeamResolver.php) | `public function resolve(Authenticatable $actor, int\|string\|null $requested): ?Team` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Membership.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/Membership.php) | No literal fillable array detected; inspect the model and API schema. |
| [Organization.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/Organization.php) | `name`, `slug`, `owner_id`, `status`, `archived_at` |
| [Team.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/Team.php) | `name`, `personal_team`, `organization_id`, `status` |
| [TeamInvitation.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/organizations-teams/src/Models/TeamInvitation.php) | `email`, `role`, `token_hash`, `invited_by`, `expires_at`, `accepted_at`, `revoked_at` |
<!-- layer-implementation-plan:end -->
