# Module indexes

This directory maps Liberu’s reusable module scopes. The indexes separate framework-neutral domain capabilities from technology-specific implementations.

## Guides

- [Authoring a module](authoring/README.md) — the step-by-step sequence for creating a package, its tests, its presentation companion, and its release.

## Indexes

- [Generic domain feature scopes](features/README.md) — framework-neutral capabilities and links to their canonical specifications.
- [Core module implementations](core/README.md) — domain-driven Composer packages containing reusable business logic and persistence.
- [API implementations](api/README.md) — HTTP contracts and API adapters.
- [Filament implementations](filament/README.md) — administrative and operational UI.
- [Livewire implementations](livewire/README.md) — server-driven Laravel UI.
- [React + Inertia implementations](react/README.md) — React presentation adapters.
- [Vue + Inertia implementations](vue/README.md) — Vue presentation adapters.
- [Next.js plans](nextjs/README.md) — independently deployed React presentation adapters consuming Laravel APIs.
- [Nuxt implementations](nuxt/README.md) — Nuxt application adapters.
- [Mobile implementations](mobile/README.md) — shared mobile boundaries and platform adapters.
- [React Native + Expo implementations](react-native/README.md) — React Native mobile adapters.
- [Flutter implementations](flutter/README.md) — Flutter/Dart mobile adapters.

The generic domain specifications are not duplicated here. Their canonical index is [features/README.md](features/README.md), with product-specific scopes under `projects/<project>/features/`. Technology-specific indexes link to the matching API, Filament, Livewire, React, Vue, Nuxt, React Native, and Flutter scope documentation under each project.

## Source and package lifecycle

- [Observed source inventory](../architecture/SOURCE-INVENTORY.md) — exact identities and application source locations.
- [Shared ownership and reuse](../architecture/SHARED-MODULES.md) — consolidate common behavior without losing product capabilities.
- [Composer lifecycle](../guides/COMPOSER.md) and [npm lifecycle](../guides/NPM.md) — local development, updates, and publishing.

- [Observed package implementation references](source/README.md) — exact metadata, source callables, migrations, route/schema files and verification entry points, grouped by package identity.

- [Presentation delivery and package guide](../architecture/PRESENTATION.md) — host responsibilities and reusable contracts for every supported layer.
