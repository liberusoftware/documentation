# Liberu Filament 5 Architecture

## Canonical Implementation Specification

**Status:** Source of truth  
**Applies to:** All Liberu Filament 5 panels, plugins, resources, pages, widgets, actions, forms, tables, infolists, and admin-theme integrations  
**Target stack:** Laravel 13, PHP 8.5, Filament 5, Livewire 4  
**Related specifications:** [MODULES.md](../architecture/MODULES.md) · [THEMES.md](THEMES.md) · [projects/boilerplate/BOILERPLATE.md](../projects/boilerplate/BOILERPLATE.md) · [API.md](../architecture/API.md) · [DOCUMENTATION.md](DOCUMENTATION.md) · [TESTING.md](TESTING.md)

## 1. Purpose

Filament is an optional presentation adapter over Liberu domain capabilities. It provides administrative and operational interfaces without owning business rules, persistence rules, authorization decisions, or theme identity.

This document defines where Filament 5 logic belongs, how it is named and installed, how panels integrate plugins, how plugins discover resources/pages/widgets, and how module and theme responsibilities remain separate.

The governing rule is:

> Applications own panels; module Filament packages own functional UI; theme Filament packages own supported visual integration.

## 2. Mandatory naming rule

All reusable Filament 5 logic is modular and its package/repository installer name must:

1. start with `module-` when it exposes module or domain functionality, or `theme-` when it exposes theme presentation;
2. end with `-filament`;
3. use lowercase kebab-case between the prefix and suffix.

The canonical pattern is:

```text
module-{independent-module-name}-filament
theme-{theme-name}-filament
```

Examples:

| Aim | Valid name | Invalid names |
|---|---|---|
| CMS content administration | `module-cms-content-filament` | `module-cms-filament`, `cms-content-filament` |
| Billing invoice administration | `module-billing-invoices-filament` | `module-billing-filament`, `billing-admin` |
| Corporate admin styling | `theme-corporate-filament` | `corporate-filament`, `theme-corporate` |

This rule applies to the independent GitHub repository name, Composer package basename, Liberu installer name, and installed directory. Composer examples are `liberu/module-cms-content-filament` and `liberu/theme-corporate-filament`.

PHP symbols use StudlyCase equivalents:

```text
Liberu\Modules\CmsContent\Filament\CmsContentFilamentPlugin
Liberu\Modules\CmsContent\Filament\CmsContentFilamentServiceProvider
Liberu\Themes\Corporate\Filament\CorporateFilamentPlugin
Liberu\Themes\Corporate\Filament\CorporateFilamentServiceProvider
```

Plugin IDs are stable kebab-case identifiers equal to the installer name, for example `module-cms-content-filament`. Panel IDs are application-owned names such as `admin`, `staff`, or `operations` and do not use this package naming rule unless the panel itself is distributed as reusable modular logic.

## 3. Ownership and dependency direction

```text
Application panel
├── module-cms-content-filament plugin ─> CMS Content contracts/actions
├── module-cms-pages-filament plugin ───> CMS Pages contracts/actions
├── module-billing-invoices-filament ───> Billing Invoices contracts/actions
└── theme-corporate-filament plugin ─> supported Filament theme hooks/assets

Domain packages -X-> Filament
Domain packages -X-> theme packages
Theme packages  -X-> domain internals
```

Responsibilities are divided as follows:

| Owner | Owns | Must not own |
|---|---|---|
| Root application | Panel providers, panel URLs/IDs, authentication, middleware, tenancy composition, plugin selection and ordering | Reusable module resources or duplicated package UI |
| `module-*-filament` | Plugins, resources, relation managers, pages, widgets, clusters, actions, forms, tables, infolists, navigation contributions | Domain rules, direct cross-module table access, application-specific panel creation |
| Domain module | Models, policies, authorized actions/queries, persistence, events and business rules | Filament dependencies or Filament classes |
| `theme-*-filament` | Supported CSS/JS assets, colors, icons, render hooks and presentation-only panel configuration | Resources, business actions, policy replacement, validation replacement |

Each module Filament package depends on the public contracts/actions of its one matching domain module plus shared foundation contracts where required. It must not depend on another independent domain module merely to present that module's UI. A theme Filament package depends on the theme and supported Filament contracts, not on domain implementations. The root application may depend on all selected packages because it is the composition root.

### 3.1 One-to-one module ownership

Every independent domain module that requires Filament access has its own matching Filament presentation module. The relationship is one-to-one:

```text
cms-content     -> module-cms-content-filament
cms-pages       -> module-cms-pages-filament
billing-invoices -> module-billing-invoices-filament
```

An umbrella product package such as `module-cms-filament` must not own the Filament logic for several independent CMS modules. Keeping the same boundary on both sides preserves independent installation, enablement, dependencies, ownership, testing, release cadence, and reuse.

The matching Filament module supplies every Filament surface its one domain module requires across administration, authenticated application, staff, operations, tenant, customer, partner, or any other panel. It may contribute different resources, pages, widgets, actions, navigation and configuration to different panels, but it must not contain another independent module's Filament implementation.

Each domain module documents whether it requires Filament access. When it does, its matching `module-{independent-module-name}-filament` package must:

- depend only on that domain module's public contracts/actions and shared foundation contracts;
- maintain a documented matrix of the panels required by that module and the components contributed to each panel;
- implement every declared panel surface or record an explicit, approved exclusion;
- fail CI when a declared panel requirement has no mapped implementation;
- test every panel mapping independently and in representative application compositions.

The application composes as many independent Filament plugins as its selected domain modules require. Attaching a plugin does not bypass module enablement, compatibility, entitlement, authorization, or tenancy rules.

## 4. Package and installation model

Every reusable Filament integration is developed and released from an independent repository under `liberusoftware`.

- A `module-*-filament` package declares Composer type `liberu-module` and installs to `/modules/{installer-name}`.
- Its Composer and module manifests declare its matching domain module as a required dependency and identify no second domain module as presentation ownership.
- A `theme-*-filament` package declares Composer type `liberu-theme` and installs to `/themes/{installer-name}`.
- `liberu/composer-installer` performs deterministic installation as specified by `MODULES.md` and `THEMES.md`.
- Composer autoloading is authoritative; the application must not scan `/modules` or `/themes` to invent an alternative PHP autoloader.
- Installed module and theme directories are committed under the tracked-directory policies in the related specifications.

Example installation results:

```text
modules/module-cms-content-filament/
themes/theme-corporate-filament/
```

Installing a package, enabling its runtime module, attaching its plugin to a panel, authorizing a user, and granting commercial entitlement are separate decisions. No package may attach itself silently to every panel.

## 5. Standard module Filament layout

```text
github.com/liberusoftware/module-cms-content-filament/
├── composer.json
├── module.json
├── README.md
├── CHANGELOG.md
├── resources/
│   ├── lang/
│   └── views/
├── src/
│   ├── Actions/                 # Filament action adapters only
│   ├── Clusters/
│   ├── Concerns/
│   ├── Pages/
│   ├── Resources/
│   │   └── PostResource/
│   │       ├── Pages/
│   │       ├── RelationManagers/
│   │       ├── Schemas/
│   │       └── Tables/
│   ├── Widgets/
│   ├── CmsContentFilamentPlugin.php
│   └── CmsContentFilamentServiceProvider.php
└── tests/
    ├── Architecture/
    ├── Compatibility/
    ├── Feature/
    ├── Integration/
    ├── Security/
    └── Unit/
```

Create only directories that are used. Resource-related pages, relation managers, schemas, and tables stay beneath their resource where Filament 5 conventions allow it. Shared package-local presentation helpers may have a dedicated directory, but domain behavior must be moved into the owning domain module.

## 6. Standard theme Filament layout

```text
github.com/liberusoftware/theme-corporate-filament/
├── composer.json
├── theme.json
├── README.md
├── CHANGELOG.md
├── resources/
│   ├── css/filament.css
│   ├── js/filament.js
│   ├── icons/
│   └── views/
├── src/
│   ├── CorporateFilamentPlugin.php
│   └── CorporateFilamentServiceProvider.php
├── tests/
│   ├── Accessibility/
│   ├── Feature/
│   ├── Security/
│   └── Visual/
└── vite.config.js
```

The package follows `THEMES.md` for assets, inheritance, accessibility, security, performance, builds, and tracked `/themes` behavior. It customizes Filament only through supported Filament 5 APIs. It never edits or publishes vendor files as its extension mechanism.

## 7. Panels belong to applications

The root application defines each `PanelProvider`. A panel owns deployment-specific decisions including:

- stable panel ID, path and domain;
- authentication guard, login and password-reset behavior;
- middleware and authorization gates;
- tenant resolution and tenant-aware middleware;
- enabled module and theme plugins;
- plugin ordering and panel-specific configuration;
- global navigation, notifications, branding fallback and operational policy.

For every selected `module-*-filament` plugin, the application maps the plugin's declared surfaces to the appropriate panels. A single plugin may contribute different components to `admin`, `app`, `staff`, `operations`, tenant, or other panels through typed configuration; it must not assume that all components belong in an admin panel or that every panel exposes the same capabilities.

A reusable package supplies a Filament plugin, not a panel provider. An exception requires an ADR and is appropriate only when the package intentionally distributes a complete application surface. Even then, its reusable package name follows the required `module-` or `theme-` prefix and `-filament` suffix.

Conceptual application composition:

```php
public function panel(Panel $panel): Panel
{
    return $panel
        ->id('admin')
        ->path('admin')
        ->plugins([
            CmsContentFilamentPlugin::make(),
            CmsPagesFilamentPlugin::make(),
            BillingInvoicesFilamentPlugin::make(),
            CorporateFilamentPlugin::make(),
        ]);
}
```

The actual method calls must match the installed Filament 5 API. The architectural requirement is explicit application composition, not a specific bootstrap syntax.

## 8. Plugin contract

Each package exposes one primary, final-by-default plugin class implementing Filament's plugin contract. It has:

- a stable ID following the package installer name;
- a conventional static `make()` constructor;
- explicit, typed configuration methods for supported options;
- a `register()` phase for resources, pages, widgets and panel configuration;
- a `boot()` phase only for behavior requiring the constructed panel;
- safe behavior when optional capabilities are unavailable.

Plugin configuration must be immutable or isolated per plugin/panel instance. It must not use process-global mutable state, infer arbitrary host classes, or read tenant/user state during package registration. Required dependencies fail with an actionable error; optional dependencies omit their UI cleanly.

Service providers load package infrastructure such as translations, views, configuration and assets. They do not decide which application panels receive the plugin.

## 9. Auto-discovery

Auto-discovery is package-local, bounded and deterministic. It reduces registration boilerplate; it does not erase ownership boundaries.

### 9.1 Discovery boundary

A module plugin may use Filament 5 discovery APIs to discover only classes beneath its own Composer namespace and package path:

```text
Resources: Liberu\Modules\CmsContent\Filament\Resources -> src/Resources
Pages:     Liberu\Modules\CmsContent\Filament\Pages     -> src/Pages
Widgets:   Liberu\Modules\CmsContent\Filament\Widgets   -> src/Widgets
Clusters:  Liberu\Modules\CmsContent\Filament\Clusters  -> src/Clusters
```

It must not recursively scan the application, all of `/modules`, all of `/themes`, or `/vendor`. Composer and the Liberu module registry determine which packages exist; the application determines which plugins are attached; the plugin discovers only its own internal Filament classes.

### 9.2 Discovery sequence

```text
Composer installs and autoloads package
        ↓
Liberu registry validates installed/enabled module and dependencies
        ↓
Application builds a named panel and explicitly attaches selected plugins
        ↓
Plugin registers or discovers its package-local resources/pages/widgets
        ↓
Filament applies authorization, tenancy, navigation and panel configuration
        ↓
Filament caches the resolved production component registry
```

Disabled Filament presentation modules do not contribute plugins. A matching plugin contributes no components when its one domain module is disabled. Theme activation is resolved through trusted application/theme configuration before its presentation plugin is attached. Production deployment clears and rebuilds relevant Laravel/Filament caches after package or enablement changes.

Package-local discovery is filtered by the domain-module-to-panel matrix. Discovery must not expose a component merely because its class exists: the matching domain module and target panel surface must both be enabled for that plugin instance.

### 9.3 Explicit registration exceptions

Use explicit registration instead of discovery when:

- a component is conditional on a capability, configuration value, panel, tenant mode, or edition;
- ordering or replacement is significant;
- a class is outside the conventional package namespace;
- a collision or override must be visible and reviewed;
- discovery would expose a component that is not valid for every configured instance of the plugin.

Conditional registration is evaluated from trusted configuration and the module/capability registry, never merely from `class_exists()` when enablement or entitlement matters.

### 9.4 Collision and cache rules

Resource slugs, page routes, widget identifiers, Livewire aliases, navigation groups and plugin IDs must be stable and collision-checked. Module-owned identifiers should be qualified by product/capability where ambiguity is possible. Duplicate identifiers fail during development/CI and produce an actionable deployment failure rather than last-write-wins behavior.

Discovery results must be cacheable and reproducible. Runtime filesystem scans on every request are prohibited in production.

## 10. Resources

A resource is a Filament adapter around an owned domain model and authorized application operations.

- It depends on domain contracts, queries, DTOs and actions rather than embedding business workflows.
- Queries enforce tenant scope and data visibility at their authoritative boundary.
- Pages, relation managers, bulk actions, exports, imports and global search apply the same policies and tenant restrictions.
- Mutations call authorized domain actions; they do not bypass invariants with ad hoc model writes.
- Form schemas validate presentation input, while domain actions retain authoritative validation and invariants.
- Tables and infolists consume purpose-built query/read models where direct model exposure would leak internals.
- Cross-module relationships use public contracts and stable identifiers, not another module's private model or table.

Resources belong to `module-*-filament`, never to `theme-*-filament`.

## 11. Pages

Resource pages live with their resource. Standalone operational pages live under `src/Pages`.

Pages coordinate UI state and invoke application actions or queries. They may not become domain services. Every page declares or inherits authorization, tenant expectations, navigation behavior and failure states. Sensitive data must not be placed in public Livewire properties, URLs, notifications, or logs.

Application-only pages that compose several modules may live in the root application. If they become reusable, they are extracted into a correctly named `module-*-filament` package and depend only on public module boundaries.

## 12. Widgets

Widgets belong to the module that owns the represented capability or metric. They obtain data from authorized queries/read models, use bounded queries, and state their cache/freshness behavior.

- Dashboard inclusion is explicit or package-locally discovered through the plugin.
- Widgets respect panel, user, tenant, timezone, locale and currency context.
- Polling is opt-in, rate-conscious and disabled when unnecessary.
- Empty, loading, stale, denied and error states are intentional.
- A widget must not aggregate another module's private storage; cross-module dashboards use public query contracts or application-level composition.

Themes may style widgets but do not own functional widgets.

## 13. Forms, tables, infolists and actions

These components are presentation definitions. They remain close to the resource/page that uses them unless they are demonstrably reusable inside the same Filament package.

- Actions authorize on the server and invoke domain actions.
- Validation errors are mapped into usable Filament feedback without exposing internals.
- Destructive actions require clear confirmation, exact scope and domain-supported recovery semantics.
- Bulk operations are bounded, queued when necessary, idempotent where retried, and auditable.
- File handling uses the shared file/storage capability and its authorization rules.
- User-facing labels, help and notifications are translated.

Do not create a cross-product dumping ground of generic Filament schemas. Reuse follows a stable public contract and a clear owner.

## 14. Navigation, tenancy and authorization

Navigation visibility is not authorization. Policies and domain/application actions remain authoritative even when an item, page or action is hidden.

Every plugin declares its navigation contributions and lets the application configure groups, ordering and optional visibility through typed plugin options. Packages must not reorder unrelated navigation or silently replace application navigation.

Tenant context is resolved by the application and passed through supported Filament/Laravel mechanisms. Every resource query, relation, search result, widget query, action, import and export must preserve tenant isolation. A missing tenant context fails closed for tenant-bound behavior.

## 15. Theme integration

A `theme-*-filament` package may register:

- compiled CSS and JavaScript entry points;
- semantic colors, typography and supported panel-brand settings;
- reviewed icons and icon aliases;
- supported render hooks and view components;
- presentation-only plugin configuration.

It must preserve Filament authorization, validation, action behavior, responsive behavior, accessibility and upgrade compatibility. It cannot register domain resources/pages/widgets, replace policies, intercept mutations, or depend on private markup/classes. Module views and assets are overridden only through documented stable extension points and the resolution rules in `THEMES.md`.

## 16. Service provider and lifecycle integration

The package service provider is discovered through Composer/Laravel package discovery or declared explicitly according to the package standard. It may:

- merge package configuration;
- load translations and namespaced views;
- register assets, commands and publishable development resources;
- register the plugin in a Liberu presentation-plugin registry.

Registering a plugin descriptor in the Liberu registry does not attach it to a panel. The root application resolves enabled and compatible descriptors, then explicitly composes the chosen instances into each panel. Registration is collision-checked, inspectable and cacheable.

The lifecycle follows `MODULES.md`: install, enable, disable, upgrade and uninstall are distinct. Disabling removes the plugin contribution after cache refresh but does not delete domain data. Uninstall instructions account for package assets and caches without silently deleting business data.

## 17. Configuration and extension points

Configuration has one owner and safe defaults. Package options exposed to applications are typed and documented, for example enabled resources, navigation grouping, polling intervals or optional capability integrations.

Stable public Filament surfaces include:

- plugin class, ID and configuration methods;
- resource/page/widget identifiers and routes intended for linking;
- extension contracts, render-hook names and view namespaces;
- Livewire aliases and public events;
- documented theme tokens and asset entry points.

Consumers must not subclass internal classes, replace private container bindings, edit installed package files, or depend on undocumented Filament/vendor markup. Prefer composition, callbacks with narrow contracts, registries and documented hooks.

## 18. Security, privacy and resilience

- Authenticate through the application panel and authorize every operation server-side.
- Validate untrusted state at Livewire/action boundaries and again at authoritative domain boundaries.
- Escape output by default; sanitize approved rich content with the shared service.
- Protect against mass assignment, insecure direct object references and tenant-scope bypasses.
- Treat imports, exports, uploads, downloads and queued actions as independently authorized operations.
- Do not serialize secrets or unnecessary personal data into Livewire state.
- Rate-limit expensive actions and make retried writes idempotent where applicable.
- Audit privileged and destructive operations with actor, tenant, target and correlation context.
- Optional widgets, metrics or integrations fail independently without breaking the panel.

## 19. Testing

Filament testing follows [TESTING.md](TESTING.md). Tests assert observable behavior through public plugin and component boundaries, use the smallest layer that supplies the required evidence, and remain deterministic, isolated and parallel-safe. Package behavior is proven by its owning package; the root application proves panel composition and representative cross-module journeys.

| Evidence | Primary owner |
|---|---|
| Plugin options, registration, local discovery and component behavior | `module-*-filament` or `theme-*-filament` package |
| Domain invariants invoked by Filament | Owning domain package |
| Panel/plugin/theme composition and cross-module workflows | Root application |
| Visual identity, assets and supported presentation hooks | `theme-*-filament` plus representative host |
| Minimum/current Filament, Livewire, Laravel and PHP compatibility | Independent package CI and host CI |

Every `module-*-filament` package includes, where relevant:

- architecture tests preventing domain-to-Filament dependencies, `App\\` coupling and cross-module internal access;
- boundary tests proving the package presents exactly one matching independent domain module and does not contain another module's Filament logic;
- panel-matrix tests proving every declared admin, app, staff, operations, tenant, or other surface is implemented and registered only on its intended panels;
- conditional-registration tests proving the enabled matching module appears only on declared panels and disabled, missing, incompatible or unauthorized capabilities do not leak UI;
- plugin registration and package-local discovery tests;
- collision tests for plugin/component IDs, routes and aliases;
- resource/page/widget tests for authorization, tenant isolation, validation and empty/error states;
- action tests proving delegation to authoritative domain actions;
- Livewire tests for public state, validation, authorization, events, loading and failure behavior;
- security tests for unauthenticated access, insufficient permission, wrong tenant, direct-object references, hidden fields, mass assignment and sensitive-data leakage;
- failure-path tests for duplicate submission, retry, concurrency, partial completion, stale state, denial and recovery when the component can encounter them;
- clean installation and boot tests in a minimal supported Laravel/Filament host;
- compatibility tests for declared Laravel, Filament, Livewire and domain-package versions;
- application composition tests covering each supported target panel.

Every `theme-*-filament` package additionally follows `THEMES.md` and `TESTING.md` for render, accessibility, visual-regression, asset-build, CSP, localization/RTL, graceful-degradation, security and performance evidence. Browser tests are reserved for a small set of critical interactions that cannot be proved reliably below the browser layer. Tests prove that visual customization does not alter authorization or functional behavior.

Meaningful PHP and Livewire behavior produces line coverage and branch/path coverage where the supported toolchain provides it reliably. Static CSS, imagery and templates use render, accessibility, visual, build and performance evidence instead of artificial line-coverage tests. Thresholds are risk-based; changed critical code must be thoroughly tested even when the repository-wide threshold passes. Machine-readable and HTML coverage reports are retained as protected CI artifacts or approved release assets and are not normally committed.

Each repository exposes stable Composer commands such as `composer test`, `composer test:feature`, `composer test:coverage` and `composer test:parallel`, limited to the suites it actually provides. The documented commands, required databases, coverage driver, browser tooling and asset prerequisites are exercised in CI. Tests never contact production services, use live credentials or include production/personal data.

Pull-request CI runs formatting/linting, static analysis, architecture rules, unit/feature/Livewire tests, relevant security checks and coverage. Expensive browser, visual, mutation, performance and full compatibility jobs may run separately or on a schedule, but all release-required evidence completes before publication. Minimum and current supported PHP/Laravel/Filament/Livewire combinations are tested, with Composer lowest-dependency testing where meaningful.

CI verifies that production discovery/cache generation is deterministic, disabled or missing optional capabilities do not leak components into a panel, and a clean locked installation produces no unexpected `/modules` or `/themes` changes. Flaky tests are defects; any temporary quarantine has an owner, linked issue, risk statement and expiry, and blind reruns do not define success.

## 20. Versioning and documentation

Packages use semantic versioning and release independently. Breaking changes to stable plugin configuration, identifiers, routes, aliases, hooks, view contracts or supported versions require a major release and migration guide.

Each repository README documents:

- purpose and owning domain/theme;
- exact Composer, repository and installer name;
- installation path and module/theme manifest;
- required and optional dependencies;
- supported Laravel, PHP, Filament, Livewire and host versions;
- plugin registration and all typed configuration options;
- resource, page, widget and navigation inventory;
- the identity of its one matching independent domain module;
- the complete panel matrix for that module, including admin, app, staff, operations, tenant and other supported panels;
- approved panel exclusions and optional integrations;
- discovery namespaces/paths and explicit-registration exceptions;
- panels and tenancy modes tested;
- authorization, security and accessibility behavior;
- extension points, theme integration and upgrade/uninstall instructions;
- local tests, CI, coverage and compatibility evidence.

## 21. Definition of done

A Filament 5 integration is ready when:

- its name has the correct `module-` or `theme-` prefix and `-filament` suffix;
- it is independently packaged, versioned, documented and installed in the correct `/modules` or `/themes` location;
- domain logic remains outside Filament and dependency direction is enforced;
- the application explicitly owns panels and selects plugins;
- it presents exactly one matching independent domain module and contains no other module's Filament logic;
- the matching domain module's panel matrix is complete, capability-aware and enforced in CI;
- package-local discovery is bounded, deterministic, collision-checked and cacheable;
- resources, pages, widgets and actions enforce policy and tenant scope and delegate to domain boundaries;
- theme behavior uses only supported visual extension points;
- installation, enablement, disablement, cache refresh and uninstall behavior are tested;
- architecture, feature, security, accessibility and compatibility suites pass;
- meaningful PHP/Livewire coverage is generated and reviewed, and critical browser/visual evidence is retained where required;
- tests are deterministic, parallel-safe, free of production dependencies and exercised through documented Composer commands;
- a clean locked Composer install and production Filament cache build are reproducible.

## 22. GitHub issue mapping

Create one Filament integration epic for each independent domain module requiring Filament access, then child issues for: matching package/manifest scaffolding; panel matrix; plugin contract; admin/app/staff/operations/tenant panel composition as applicable; resource discovery; pages and navigation; widgets; forms/tables/infolists/actions; authorization and tenancy; theme integration; localization/accessibility; discovery/cache collisions; security/performance; compatibility tests; documentation and release.

Each issue identifies the owning `module-*-filament` or `theme-*-filament` package, target panels, domain contracts, discovered and explicitly registered components, authorization/tenant rules, extension points, acceptance criteria, tests and explicit exclusions.
