# Generic domain feature scopes

This is the module-level entry point for framework-neutral domain capabilities. It defines what a capability does without coupling the domain to Laravel, API, Filament, Livewire, React, Vue, or Nuxt.

## Canonical specifications

The authoritative feature index remains [root `features/README.md`](../../features/README.md). Product feature scopes remain under each project and must not be duplicated in this directory.

| Scope                             | Canonical domain documentation                                    |
| --------------------------------- | ----------------------------------------------------------------- |
| All product domain capabilities   | [Feature specifications](../../features/README.md)                |
| Liberu cross-product capabilities | [Liberu feature scopes](../../projects/liberu/features/README.md) |

## Implementation mapping

After reading a domain feature specification, use the matching implementation index:

See [Domain module implementation](IMPLEMENTATION.md) for the Laravel package boundary and the expected controllers, services, models, migrations, factories, seeders, jobs, views, and tests.

- [API](../api/README.md)
- [Filament](../filament/README.md)
- [Livewire](../livewire/README.md)
- [React + Inertia](../react/README.md)
- [Vue + Inertia](../vue/README.md)
- [Nuxt](../nuxt/README.md)

Each implementation belongs under the relevant `projects/<project>/<technology>/` scope. Keep domain rules framework-neutral and place framework-specific behavior in the appropriate adapter.
