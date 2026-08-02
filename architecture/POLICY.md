# Policies and permissions

## Purpose

Liberu separates resource authorization from team context. Laravel policies and gates are authoritative for runtime decisions. Spatie Laravel Permission provides application roles and permissions, and Filament Shield exposes the same authorization model in Filament panels.

## Boundaries

| Concern | Authority |
|---|---|
| Resource/action authorization | Laravel policies and gates |
| Application roles and permissions | `spatie/laravel-permission` |
| Filament resource/page/widget permissions | `bezhansalleh/filament-shield` |
| Workspace membership and current context | Jetstream teams; see [TEAMS.md](TEAMS.md) |
| Team membership roles/permissions | Jetstream team roles and `hasTeamPermission` |

Spatie Permission and Shield must not replace Jetstream teams, team membership, current-team resolution, or Jetstream team roles. A user may have an application permission and still lack access to a particular team resource.

## Implementation rules

- Default to deny and authorize at the domain/action boundary, not only in controllers or UI.
- Scope checks by actor, current team, resource ownership, state, and application permission as applicable.
- Use permission names owned by the module, such as `genealogy.tree.view`; do not invent them in views.
- Keep policy methods small, typed, deterministic, and side-effect free. Use constructor injection in actions/services when external data is needed.
- Apply the same policy to HTTP, Livewire, Filament, console, queue, export, search, notification, and bulk-action paths.
- Invalidate permission caches after role/permission changes and audit actor, scope, before/after values, and reason.
- Keep super-admin or break-glass access explicit, strongly authenticated, limited, and separately audited.
- Never trust a team ID, role name, permission, or resource ID supplied by a client without resolving it against authenticated context.

## Filament Shield

Shield may generate and manage panel permissions for resources, pages, and widgets. Review generated policies and permission keys before enabling them, keep custom permissions in the owning module, and ensure generated UI checks agree with domain policies. Shield is a panel adapter, not a substitute for domain authorization.

## Testing

For every protected action, test allowed, unauthenticated, wrong-team, missing-permission, wrong-owner, invalid-state, and super-admin/break-glass behavior where relevant. Include authorization tests for queued jobs, exports, APIs, and Filament actions.

## References

- [Laravel authorization](https://laravel.com/docs/13.x/authorization)
- [Spatie Laravel Permission](https://spatie.be/docs/laravel-permission/v8/introduction)
- [Filament Shield](https://filamentphp.com/plugins/bezhansalleh-shield)
- [Jetstream teams](https://jetstream.laravel.com/features/teams.html)
- [Teams](TEAMS.md)
