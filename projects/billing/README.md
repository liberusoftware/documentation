# Billing — Developer Documentation

**API backend:** [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) is being introduced as this product’s shared Laravel backend for Next.js, Nuxt, Flutter, React Native and Dart mobile/desktop clients. See [backend ownership and integration](../../guides/LARAVEL-API-BACKENDS.md).

**Scope:** Billing modules

## Laravel Filament application

Billing Filament groups host code, database files, views, and tests by capability under `modules/billing-*`. The shared Laravel composition lives in `billing-application`. Separately released billing packages load through Composer and the module registry. See the [development guide](DEVELOPMENT.md#application-module-layout) for paths and verification commands.

## Module indexes

- [Core domain modules](core/README.md) — 82 specification documents
- [API modules](api/README.md) — 82 specification documents
- [Feature specifications](features/README.md) — 82 specification documents
- [Filament modules](filament/README.md) — 82 specification documents
- [Livewire modules](livewire/README.md) — 82 specification documents
- [React modules](react/README.md) — 82 specification documents
- [Vue modules](vue/README.md) — 82 specification documents
- [Nuxt modules](nuxt/README.md) — 82 specification documents
- [Flutter modules](flutter/README.md) — 82 specification documents
- [React Native modules](react-native/README.md) — 82 specification documents

## Source and additional presentation options

- [Observed source modules](SOURCE-MODULES.md) — exact manifest identities and commit-pinned source links.
- [Next.js module plan](nextjs/README.md) — API-consuming React adapters and shared component boundaries.

- [Design-to-source reconciliation](SOURCE-MAPPING.md) — exact package identities, retained aliases, unmatched observed modules, and source implementation references.

- [Project clone development guide](DEVELOPMENT.md) — requirements, actual scripts, setup, module selection, verification and updates.
