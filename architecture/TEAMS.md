# Teams

## Purpose

Jetstream teams are Liberu's workspace boundary. They provide membership, invitations, ownership, current-team context, and team roles. This document complements [JETSTREAM.md](JETSTREAM.md); it does not define a second tenancy or permission system.

## Model

- A team is a durable workspace boundary for users and team-owned data.
- A user may belong to multiple teams and has one current team per session/context.
- Team switching changes the active context only; it never grants membership or permission.
- Team ownership is distinct from application roles and from Filament panel access.
- Domain records that belong to a team must carry an explicit team relationship or use a documented aggregate boundary.

## Membership lifecycle

1. Create a team through the Jetstream `CreateTeam` action.
2. Invite members through `InviteTeamMember`; invitations must be signed, expiring, single-use, revocable, and auditable.
3. Accept an invitation before creating active membership and assign the permitted Jetstream team role.
4. Resolve current team and active membership at every request, job, notification, export, and API operation.
5. On removal, suspension, transfer, or deletion, revoke derived access and reconcile queued work, tokens, sessions, and shared resources.

## Authorization

Use `belongsToTeam`, `hasTeamPermission`, and resource policies together. Team roles group team permissions; they are not Spatie roles. Application permissions from [POLICY.md](POLICY.md) do not override team membership or resource ownership.

```php
public function update(User $user, Tree $tree): bool
{
    return $user->belongsToTeam($tree->team)
        && $user->hasTeamPermission($tree->team, 'genealogy.tree.update')
        && $user->can('update', $tree);
}
```

The final policy may use a domain-specific action instead of combining checks inline. Keep authorization server-side and deny by default.

## Data and operations

- Resolve team context from authenticated state, never from an untrusted request field alone.
- Prevent cross-team reads, writes, search results, notifications, files, exports, jobs, and cache keys.
- Require recent authentication for ownership transfer, deletion, membership administration, and changes to sensitive team permissions.
- Audit creation, invitations, acceptance, role changes, switching where material, removal, transfer, suspension, and deletion.
- Define retention, export, archival, deletion, and legal-hold behavior before shipping team-owned data.

## Verification

Test multiple-team membership, current-team switching, expired/revoked invitations, duplicate membership, owner transfer, removal, suspended users, queued jobs with stale context, API tokens, wrong-team object access, and team deletion recovery.

## References

- [Jetstream](JETSTREAM.md)
- [Jetstream team documentation](https://jetstream.laravel.com/features/teams.html)
- [Policies and permissions](POLICY.md)
- [Boilerplate team foundation](../projects/boilerplate/BOILERPLATE.md#8-organizations-and-teams)
