# Liberu tenancy

## Canonical tenancy specification

**Status:** Source of truth
**Applies to:** Laravel 13 applications, PHP 8.5 modules, Jetstream teams, Filament tenants, APIs, jobs, storage, and presentation layers
**Reference implementation:** [`liberusoftware/genealogy-laravel`](https://github.com/liberusoftware/genealogy-laravel)
**Related specifications:** [JETSTREAM.md](JETSTREAM.md) · [TEAMS.md](TEAMS.md) · [POLICY.md](POLICY.md) · [API.md](API.md) · [MODULES.md](MODULES.md) · [SECURITY.md](SECURITY.md)

## Decision

Liberu uses the Jetstream `Team` model as the customer/workspace tenant. A user's membership, selected team, and authorization in that team are separate concerns:

| Concern                          | Authority                                                   | Meaning                                                       |
| -------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------- |
| Identity and authentication      | Jetstream/Fortify/Sanctum                                   | Who is acting and how the request is authenticated            |
| Tenant identity                  | `App\Models\Team`                                           | Which workspace owns the data                                 |
| Membership                       | Jetstream `team_user`                                       | Whether the actor can enter the workspace                     |
| Collaboration tier               | Jetstream membership `role`                                 | What a member may do to that team's records                   |
| Application/global authorization | Laravel policies, gates, Spatie Permission, Filament Shield | Global administration, panel access, and explicit permissions |
| Record isolation                 | `team_id` plus policies/scopes                              | Which rows, files, jobs, and events belong to the workspace   |

“Tenant”, “workspace”, and “team” may be used as presentation synonyms, but the persisted and public contract is `teams.id`. Do not introduce a second organization, tenant, or role system for a module.

## Observed genealogy implementation

The reference application currently uses:

- Laravel Jetstream 5 teams with invitations, personal teams, `Team` ownership, `current_team_id`, and custom team actions.
- Filament 5 app-panel tenancy with `Team` as the tenant model, tenant registration/profile pages, and URLs carrying the tenant identifier.
- A `BelongsToTenant` model trait that adds a `team` relation, a `team` global scope, and create-time `team_id` stamping.
- `TeamsPermission` middleware that resolves the tenant from a Filament route before setting Spatie's permission-team context, then falls back to `current_team_id` on non-tenant routes.
- Jetstream collaboration tiers: `admin` (`create`, `read`, `update`, `delete`, `manage-team`), `editor` (`create`, `read`, `update`, `delete`), `contributor` (`create`, `read`, `update`), and `viewer` (`read`).
- Spatie Permission teams enabled for team-aware role/permission records. Team-less role definitions are reserved for global roles such as `super_admin`; assignments still carry a concrete team.
- `EstablishesTeam` for single-team queued work, with permission context and authentication restored after the job. Cross-team analytical jobs deliberately avoid that concern and stamp every written row from its owning record.
- Team-specific export paths such as `exports/{team_id}` and tests for wrong-team visibility, URL-selected tenants, role separation, job context, and privacy-aware global search.

The existing `tenants` and `tenant_people` migrations are legacy storage and are not the active tenancy boundary. New code must not write them or treat them as interchangeable with `teams` without an approved migration and ADR.

## Tenant context lifecycle

Every request or job that reads or writes tenant-owned data follows this sequence:

```text
Authenticate actor or establish an approved service identity
        ↓
Resolve one team from trusted route/membership/service context
        ↓
Verify membership and required collaboration/policy permission
        ↓
Set request-local team and permission context
        ↓
Apply team-scoped queries, writes, files, events, caches, and logs
        ↓
Clear context at the end of the request/job
```

The route, session, or request body must not grant access by merely naming a team. A team URL is an identifier, not proof of membership. For Filament, `canAccessTenant()` must check `belongsToTeam()` and tenant middleware must resolve the URL tenant before permission checks. For non-Filament routes, resolve an explicit team parameter through the same membership policy; otherwise use the authenticated user's selected team only where the route contract explicitly permits it.

`current_team_id` is a user preference and request default, not an authorization grant. Switching teams must update it only after membership is proven. Missing, deleted, suspended, or inaccessible team context must fail closed for tenant-owned operations.

## Data isolation rules

- Every tenant-owned table has a non-null `team_id` foreign key to `teams.id`, an index beginning with `team_id` where useful, and a deletion policy documented by the owning module.
- New tenant-owned Eloquent models use the shared scoping/stamping mechanism and an explicit `team()` relation. Do not copy a local global scope into each model.
- Global scopes are defense in depth, not a substitute for policies. Every read, relationship, aggregate, search, export, import, notification, broadcast, cache key, and file path must preserve team context.
- Never use ungrouped `orWhere`, unconstrained relationship queries, raw SQL, route model binding, or eager loads that can escape the team predicate.
- `withoutGlobalScopes()` and cross-team queries are permitted only in named, reviewed service/command paths with an explicit purpose, bounded selection, per-row ownership checks, and audit logging.
- Do not accept `team_id` from ordinary client input for authorization. Derive it from trusted context and reject mismatches; privileged provisioning APIs require a dedicated service identity and allowlist.
- A nullable `team_id` is allowed only for a documented global record, migration staging row, or explicit cross-team result. It must never be an accidental fallback.

The reference trait currently returns without applying a scope when there is no authenticated actor or no team. That behavior is retained only for deliberately global/background paths during compatibility work. The target contract is fail-closed: tenant-owned request paths and single-team jobs must reject missing context rather than silently query or create unscoped rows.

## Membership and authorization

Team ownership controls membership administration: owners may rename/delete their team, invite members, change membership tiers, and remove members, subject to application policy and billing/lifecycle rules. Members may access only teams returned by their Jetstream membership/ownership relations.

Collaboration tiers are the least-privilege record capability ladder:

| Tier          | Allowed team-record capabilities         |
| ------------- | ---------------------------------------- |
| `viewer`      | Read                                     |
| `contributor` | Read, create, update                     |
| `editor`      | Read, create, update, delete             |
| `admin`       | Editor capabilities plus team management |

Every resource, relation manager, Livewire action, API operation, queued command, import/export, upload/download, and broadcast must authorize the actual operation. Hidden buttons, navigation, route guards, and global scopes are not authorization. Unknown actions default to deny.

Jetstream membership roles and Spatie roles are not interchangeable. A module that needs a team-record capability uses the Jetstream collaboration contract. A global admin/panel permission uses Laravel policy/gate and the application's global Spatie/Shield contract. If a team-scoped Spatie permission is required for a specialized capability, its team context must be set from trusted membership and it must not bypass the collaboration tier or policy.

## Jobs, events, storage, and caches

Single-team jobs carry an immutable `team_id` and an actor/service reference. Establish that team for the duration of the job, set the permission-team context, authorize the operation, and restore all authentication/permission state in `finally` blocks. Long-lived workers must clear context before and after every job.

Cross-team analytics and matching are exceptional. They use a dedicated service identity, an explicit allowlist and purpose, bounded queries, privacy rules, and per-record ownership stamping. They must not borrow the last worker's team context.

Use team-qualified identifiers for:

- private storage paths, exports, imports, temporary files, and download authorization;
- cache keys, locks, idempotency keys, rate limits, broadcasts, notifications, and search indexes;
- audit records, metrics, logs, tracing attributes, and queued operation resources.

Never put secrets or sensitive personal data in a team identifier, URL, log, cache key, broadcast payload, or job name. Public-team discovery is an explicit privacy-controlled read path, not a relaxation of member isolation; living-person and sensitive genealogy data remain protected by policy.

## API contract

Authenticated API requests use Sanctum as described in [API.md](API.md) and must resolve membership before returning team data. The reference application exposes team CRUD under its authenticated API routes, but new module APIs should follow the versioned API and OpenAPI rules:

- list only teams the actor owns or belongs to;
- authorize `show`, `update`, member management, and deletion with the Team policy;
- validate names, lifecycle state, and visibility server-side;
- never allow a caller to switch context by writing `team_id` onto a resource;
- return concealment-safe `404` responses where team enumeration is sensitive;
- include team context in operation IDs, audit events, idempotency, concurrency, and rate-limit decisions.

Presentation layers consume the matching API contract. Filament resolves the URL tenant, Livewire/React/Inertia/Nuxt preserve server-selected context, and no client-side state can elevate membership or permissions.

## Provisioning and migrations

Team creation is transactional: create the owner relationship, establish the initial selected team, apply default collaboration configuration, and emit an auditable lifecycle event. Invitations are unique per team/email, expiring, single-use, and accepted only by the authenticated account that proves control of the invited address.

Schema changes must:

1. classify every table as global, team-owned, or intentionally cross-team;
2. add and backfill `team_id` from authoritative ownership evidence;
3. quarantine or fail on rows whose ownership cannot be proven;
4. enforce foreign keys, indexes, uniqueness, and nullability after backfill;
5. deploy compatible reads before writes and remove temporary compatibility only after verification;
6. test rollback/restore and prove no cross-team rows are visible.

Never backfill a team foreign key with a guessed constant such as team `1`. The reference permission migration deliberately fails unresolved grants instead of inventing ownership; new migrations follow the same rule.

## Verification requirements

Each tenant-aware module must test, as applicable:

- unauthenticated, no-team, deleted-team, suspended-team, non-member, wrong-team, and wrong-tier requests;
- URL tenant selection on the first request, selected-team fallback on non-tenant routes, and safe team switching;
- reads, writes, relationships, aggregates, search, exports, uploads, downloads, notifications, broadcasts, caches, and route model binding across two teams;
- direct IDs, crafted `team_id`, ungrouped `orWhere`, eager loads, raw queries, bulk actions, retries, and replayed jobs;
- global roles versus team-scoped roles, owner/member lifecycle, invitation expiry, removal, deletion, and role changes;
- queue-worker context reset, single-team job restoration, cross-team analytical stamping, and long-lived worker isolation;
- privacy rules for public teams, living/deceased genealogy data, sensitive DNA/media, audit trails, rate limits, and concealment-safe errors.

Run the reference application's tenancy suites as a model for coverage: `TenantAccessControlTest`, `GlobalScopeAuditTest`, `TeamScopedRolesTest`, `PermissionsFollowTenantTest`, `EstablishesTeamTest`, `BackgroundJobTeamStampingTest`, and the team permission-tier tests.

## Definition of done

Tenancy is complete when the owning module has one authoritative team context, every tenant-owned record and side effect is isolated, every operation is authorized by the correct layer, background work cannot inherit stale state, migrations prove ownership, and two-team negative tests pass. Any exception is explicit, bounded, audited, documented here, and covered by an ADR.

## References

- [Reference tenant scope](https://github.com/liberusoftware/genealogy-laravel/blob/main/app/Traits/BelongsToTenant.php)
- [Reference team/tenant access model](https://github.com/liberusoftware/genealogy-laravel/blob/main/app/Models/User.php)
- [Reference permission-context middleware](https://github.com/liberusoftware/genealogy-laravel/blob/main/app/Http/Middleware/TeamsPermission.php)
- [Reference single-team job context](https://github.com/liberusoftware/genealogy-laravel/blob/main/app/Jobs/Concerns/EstablishesTeam.php)
- [Reference tenancy test suite](https://github.com/liberusoftware/genealogy-laravel/tree/main/tests/Feature/Tenancy)
- [Jetstream](JETSTREAM.md)
- [Teams](TEAMS.md)
- [Policy and permissions](POLICY.md)
- [API authentication and tenancy](API.md#14-authorization-scopes-and-tenancy)
- [Laravel Jetstream teams](https://jetstream.laravel.com/features/teams.html)
- [Filament tenancy](https://filamentphp.com/docs/5.x/panels/tenancy)
- [Spatie Permission teams](https://spatie.be/docs/laravel-permission/v7/basic-usage/teams-permissions)
- [Laravel authorization](https://laravel.com/docs/13.x/authorization)
