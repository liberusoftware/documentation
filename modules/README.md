# Module indexes

This directory maps Liberu’s reusable module scopes. The indexes separate framework-neutral domain capabilities from technology-specific implementations.

## Indexes

- [Generic domain feature scopes](features/README.md) — framework-neutral capabilities and links to their canonical specifications.
- [Core module implementations](core/README.md) — domain-driven Composer packages containing reusable business logic and persistence.
- [API implementations](api/README.md) — HTTP contracts and API adapters.
- [Filament implementations](filament/README.md) — administrative and operational UI.
- [Livewire implementations](livewire/README.md) — server-driven Laravel UI.
- [React + Inertia implementations](react/README.md) — React presentation adapters.
- [Vue + Inertia implementations](vue/README.md) — Vue presentation adapters.
- [Nuxt implementations](nuxt/README.md) — Nuxt application adapters.

The generic domain specifications are not duplicated here. Their canonical index is [features/README.md](features/README.md), with product-specific scopes under `projects/<project>/features/`. Technology-specific indexes link to the matching API, Filament, Livewire, React, Vue, and Nuxt scope documentation under each project.
