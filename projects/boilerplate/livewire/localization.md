# Boilerplate: Localization Livewire presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#localization). Observed identity: [`liberusoftware/localization-core-livewire`](../../../modules/source/liberusoftware--localization-core-livewire.md). This retained spelling maps to `localization-core`; it is not another independent module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-localization-livewire`
**Matching core package:** [`module-localization`](../core/localization.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Locale negotiation, translations, pluralization, RTL direction, timezone, and localized formatting.

## Adapter implementation plan

This package presents the Localization core capability through Livewire 4. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Provide responsive, keyboard-accessible, localized workflows with clear loading, validation, empty, denied, queued, failure, and recovery states.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Localization core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-boilerplate-laravel-filament`](https://github.com/liberusoftware/project-boilerplate-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/localization.md) · [API plan](../api/localization.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Locale negotiation** | Expose a focused Livewire 4 component and namespaced Blade default view for `locale negotiation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Translations** | Expose a focused Livewire 4 component and namespaced Blade default view for `translations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Pluralization** | Expose a focused Livewire 4 component and namespaced Blade default view for `pluralization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rtl direction** | Expose a focused Livewire 4 component and namespaced Blade default view for `rtl direction` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Timezone** | Expose a focused Livewire 4 component and namespaced Blade default view for `timezone` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Localized formatting** | Expose a focused Livewire 4 component and namespaced Blade default view for `localized formatting` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [LanguageSwitcher.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/localization-core-livewire/src/Livewire/LanguageSwitcher.php) · [LocalizationLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/localization-core-livewire/src/LocalizationLivewireServiceProvider.php).
<!-- layer-implementation-plan:end -->
