# Enterprise suite developer documentation

**API backend:** [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) is being introduced as this product’s shared Laravel backend for Next.js, Nuxt, Flutter, React Native and Dart mobile/desktop clients. See [backend ownership and integration](../../guides/LARAVEL-API-BACKENDS.md).

Start with the [product scope](SAP.md), then the [composition and delivery design](COMPOSITION.md). Enterprise capability groups compose existing product packages wherever their verified contracts meet the requirement. Package names in specifications remain design identifiers until implementation and release evidence is available.

## Module and presentation plans

- [Feature specifications](features/README.md)
- [Core](core/README.md) and [API](api/README.md)
- [Filament](filament/README.md) and [Livewire](livewire/README.md)
- [React + Inertia](react/README.md) and [Vue + Inertia](vue/README.md)
- [Next.js](nextjs/README.md) and [Nuxt](nuxt/README.md)
- [React Native](react-native/README.md) and [Flutter](flutter/README.md)

Use the [source inventories](../../architecture/SOURCE-INVENTORY.md) to evaluate reuse candidates and the [Composer](../../guides/COMPOSER.md) and [npm](../../guides/NPM.md) guides for module development and releases.

Read the [16 detailed enterprise domain designs](design/README.md) for records, lifecycle, API operations, permissions, integration recovery, and per-layer delivery requirements.

- [Design-to-source reconciliation](SOURCE-MAPPING.md) — exact package identities, retained aliases, unmatched observed modules, and source implementation references.

- [Project clone development guide](DEVELOPMENT.md) — requirements, actual scripts, setup, module selection, verification and updates.

- [Current SAP source and foundation](SOURCE-APPLICATION.md) — observed host composition, resolver behavior, verification sources and the boundary with proposed business-domain contracts.
