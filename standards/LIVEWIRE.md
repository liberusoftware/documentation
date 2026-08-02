# Liberu Livewire 4 Architecture

## Canonical Implementation Specification

**Status:** Source of truth  
**Applies to:** All Liberu Livewire 4 components, full-page components, forms, actions, events, navigation, islands, and theme integrations  
**Target stack:** Laravel 13, PHP 8.5, Filament 5, Livewire 4  
**Related specifications:** [MODULES.md](../architecture/MODULES.md) · [THEMES.md](THEMES.md) · [FILAMENT.md](FILAMENT.md) · [projects/boilerplate/BOILERPLATE.md](../projects/boilerplate/BOILERPLATE.md) · [API.md](../architecture/API.md) · [DOCUMENTATION.md](DOCUMENTATION.md) · [TESTING.md](TESTING.md)

## 1. Purpose

Livewire is an optional presentation adapter over Liberu domain capabilities. It provides server-driven interactive interfaces without owning business rules, persistence rules, authorization decisions, tenant resolution, or visual identity.

This document defines where Livewire 4 logic belongs, how reusable components are named and installed, how packages register components, how applications compose routes and layouts, and how module and theme responsibilities remain separate.

The governing rule is:

> Applications compose Livewire surfaces; module Livewire packages own functional components; theme Livewire packages own presentation-only interaction.

## 2. Mandatory naming rule

All reusable Livewire 4 logic is modular. Its package and repository installer name must:

1. start with `module-` when it exposes module or domain functionality, or `theme-` when it exposes theme presentation;
2. end with `-livewire`;
3. use lowercase kebab-case between the prefix and suffix.

The canonical patterns are:

```text
module-{product-or-capability}-livewire
theme-{theme-name}-livewire
```

Examples:

| Aim | Valid name | Invalid names |
|---|---|---|
| CMS interactive UI | `module-cms-livewire` | `cms-livewire`, `livewire-cms` |
| Billing customer UI | `module-billing-livewire` | `billing-components`, `module-billing` |
| Corporate theme interaction | `theme-corporate-livewire` | `corporate-livewire`, `theme-corporate` |

This rule applies to the independent GitHub repository name, Composer package basename, Liberu installer name, manifest identity, and installed directory. Composer examples are `liberu/module-cms-livewire` and `liberu/theme-corporate-livewire`.

PHP symbols use StudlyCase equivalents:

```text
Liberu\Modules\Cms\Livewire\PostEditor
Liberu\Modules\Cms\Livewire\CmsLivewireServiceProvider
Liberu\Themes\Corporate\Livewire\NavigationMenu
Liberu\Themes\Corporate\Livewire\CorporateLivewireServiceProvider
```

Application-only components may use `App\Livewire` until they become reusable. Once extracted, they follow this package naming rule and must not retain dependencies on the original application's `App\` classes.

## 3. Component namespaces and aliases

Every package owns one stable Livewire component namespace:

```text
module-{scope}::{component}
theme-{theme}::{component}
```

Examples:

```blade
<livewire:module-cms::post-editor :post-id="$postId" />
<livewire:module-billing::invoice-list />
<livewire:theme-corporate::navigation-menu />
```

The alias omits the redundant `-livewire` suffix while retaining the ownership prefix. Component names use lowercase kebab-case and dot notation for nested groups, for example `module-cms::posts.editor`.

Aliases are public interfaces. Package namespaces, component aliases, full-page route names, documented public properties, events, slots, and test identifiers must be stable, globally collision-checked, and documented. Duplicate namespaces or aliases fail during development and CI rather than using last-write-wins behavior.

## 4. Ownership and dependency direction

```text
Application routes, layouts and middleware
├── module-cms-livewire components ─────> CMS domain contracts/actions
├── module-billing-livewire components ─> Billing domain contracts/actions
└── theme-corporate-livewire components ─> supported theme hooks/assets

Domain packages -X-> Livewire
Domain packages -X-> theme packages
Theme packages  -X-> domain internals
```

Responsibilities are divided as follows:

| Owner | Owns | Must not own |
|---|---|---|
| Root application | Route composition, layouts, authentication, middleware, tenant resolution, enabled packages, global navigation and cross-module pages | Duplicated reusable components or package domain behavior |
| `module-*-livewire` | Functional components, component forms, full-page component definitions, presentation validation, view models and interaction adapters | Domain rules, application-specific composition or direct cross-module table access |
| Domain module | Models, policies, authorized actions/queries, persistence, events and business rules | Livewire dependencies, components or hydrated UI state |
| `theme-*-livewire` | Presentation-state components, layouts, styling hooks and supported JavaScript/Alpine integration | Domain mutations, policies, domain resources or validation replacement |

Dependencies point from a module Livewire package to the narrow domain contracts, queries and actions it presents. Theme Livewire packages depend on their theme and presentation contracts, not on private domain implementations. The application may depend on all selected packages because it is the composition root.

## 5. Package and installation model

Every reusable Livewire integration is developed and released from an independent repository under `liberusoftware`.

- A `module-*-livewire` package declares Composer type `liberu-module` and installs to `/modules/{installer-name}`.
- A `theme-*-livewire` package declares Composer type `liberu-theme` and installs to `/themes/{installer-name}`.
- `liberu/composer-installer` performs deterministic installation as specified by `MODULES.md` and `THEMES.md`.
- Composer autoloading is authoritative; the application must not create a competing class or filesystem scanner.
- Installed module and theme directories follow the tracked-directory policies in the related specifications.

Example installation results:

```text
modules/module-cms-livewire/
themes/theme-corporate-livewire/
```

Installation, runtime enablement, route composition, component rendering, authorization, theme activation, and commercial entitlement are separate decisions. Installing a package must not silently expose its full-page components or attach them to every application surface.

## 6. Canonical component format

Reusable Liberu packages use class-based Livewire components by default. This preserves an explicit PHP namespace, predictable Composer autoloading, conventional static analysis, and separation between component orchestration and theme-overridable views.

The canonical mapping is:

```text
src/Livewire/PostEditor.php
resources/views/livewire/post-editor.blade.php
component alias: module-cms::post-editor
```

Livewire 4 single-file components (SFCs) or multi-file components (MFCs) are permitted only when a repository documents why colocation materially improves a small or presentation-heavy component. They remain within the package's registered namespace and must satisfy the same architecture, security, alias, testing and versioning rules.

Package SFC/MFC filenames must not use the optional bolt emoji because it can cause Composer packaging problems. A package does not mix formats casually; its README identifies the default and every intentional exception. Conversion between formats is a refactor only when aliases, inputs, routes, events, slots, behavior and tests remain compatible.

## 7. Standard module Livewire layout

```text
github.com/liberusoftware/module-cms-livewire/
├── composer.json
├── module.json
├── README.md
├── CHANGELOG.md
├── config/cms-livewire.php
├── resources/
│   ├── lang/
│   └── views/
│       └── livewire/
│           ├── post-editor.blade.php
│           └── post-list.blade.php
├── routes/                      # only package-owned route declarations
├── src/
│   ├── Livewire/
│   │   ├── Forms/
│   │   ├── PostEditor.php
│   │   └── PostList.php
│   └── CmsLivewireServiceProvider.php
└── tests/
    ├── Architecture/
    ├── Compatibility/
    ├── Feature/
    ├── Integration/
    ├── Security/
    └── Unit/
```

Create only directories the package uses. Component-specific form objects and presentation helpers remain close to their owning component. Reusable domain behavior moves to the domain module rather than a base component, trait, or form object.

## 8. Standard theme Livewire layout

```text
github.com/liberusoftware/theme-corporate-livewire/
├── composer.json
├── theme.json
├── README.md
├── CHANGELOG.md
├── resources/
│   ├── css/
│   ├── js/
│   ├── lang/
│   └── views/
│       └── livewire/
│           ├── navigation-menu.blade.php
│           └── dialog-manager.blade.php
├── src/
│   ├── Livewire/
│   │   ├── DialogManager.php
│   │   └── NavigationMenu.php
│   └── CorporateLivewireServiceProvider.php
├── tests/
│   ├── Accessibility/
│   ├── Feature/
│   ├── Security/
│   └── Visual/
└── vite.config.js
```

The package follows `THEMES.md` for assets, inheritance, accessibility, localization, security, performance, builds and tracked `/themes` behavior. It owns presentation state such as menus, dialogs, filters and progressive interaction, but invokes authorized module actions for business mutations.

## 9. Registration and bounded discovery

The package service provider registers a bounded Livewire namespace. For canonical class-based components it supplies the component namespace, class namespace/path and view path through the supported Livewire 4 package API, and loads the package's Laravel view namespace.

Conceptual registration:

```php
Livewire::addNamespace(
    namespace: 'module-cms',
    classNamespace: 'Liberu\\Modules\\Cms\\Livewire',
    classPath: __DIR__ . '/Livewire',
    classViewPath: __DIR__ . '/../resources/views/livewire',
);

$this->loadViewsFrom(
    __DIR__ . '/../resources/views',
    'module-cms-livewire',
);
```

Component `render()` methods reference the registered package view namespace, for example `module-cms-livewire::livewire.post-editor`. The exact calls must match the installed Livewire 4 API; the architectural requirement is a bounded package namespace and deterministic registration.

Registration may discover only components beneath the package's own namespace and declared paths. It must not recursively scan the root application, all of `/modules`, all of `/themes`, or `/vendor`.

The resolution sequence is:

```text
Composer installs and autoloads package
        ↓
Liberu registry validates installed/enabled module and dependencies
        ↓
Package provider registers its bounded Livewire namespace
        ↓
Application composes routes/layouts and renders selected components
        ↓
Livewire resolves the stable alias and hydrates authorized state
        ↓
Production caches are built from the resolved configuration
```

Disabled modules do not expose routes or components through application composition. Conditional registration uses trusted configuration and the module/capability registry, never merely `class_exists()` when enablement or entitlement matters.

## 10. Application composition and routes

The root application owns public route topology and deployment-specific concerns including:

- URL paths, domains, route names and navigation placement;
- authentication guards and middleware;
- tenant/site/team context and locale selection;
- layouts and selected theme;
- cross-module pages and component composition;
- deployment-specific feature and entitlement policy.

Packages may provide package-owned route declarations only for cohesive, reusable routes that are part of their public surface. Those routes use named middleware/configuration seams, stable qualified route names, and configurable prefixes where host composition requires them. A package must not claim `/`, `/dashboard`, `/admin`, or another broad application path silently.

Full-page components authorize access independently of navigation visibility. Route parameters are untrusted input and are resolved through tenant-aware queries or bindings. Redirects and `wire:navigate` behavior must preserve authorization, locale, tenancy, history, focus and failure behavior.

## 11. Component responsibilities

A Livewire component is a presentation orchestrator. It may:

- accept and normalize presentation inputs;
- maintain minimal interaction state;
- invoke authorized application actions and queries;
- map domain results and exceptions into typed view state;
- dispatch documented presentation events;
- render accessible loading, empty, error, offline and success states.

It must not:

- implement domain invariants or provider workflows;
- access another module's private model or table;
- use ambient application state instead of explicit context;
- perform unbounded queries during render or hydration;
- treat hidden controls or navigation visibility as authorization;
- make a remote API the authoritative source of business rules.

Application services/actions coordinate mutations. Authorized queries return purpose-built read models. Domain packages remain usable through APIs, commands, jobs, Filament or third-party Laravel applications without Livewire installed.

## 12. State, properties and hydration

Every public property is client-visible serialized state and must be treated as untrusted on every request.

- Keep public state minimal, typed, serializable and presentation-specific.
- Never place secrets, credentials, privileged DTOs or unnecessary personal data in public properties.
- Use locked properties for identifiers that must not be changed by the client, while still authorizing the resolved record in every action.
- Do not assume a property is safe because no `wire:model` field currently exposes it.
- Avoid storing large Eloquent collections or graphs in component state; use bounded computed properties or authorized queries.
- Do not rely on query scopes or constraints surviving model serialization/hydration; reapply authoritative tenant and visibility rules.
- Reset validation and sensitive transient state when dialogs, tenants, records or workflows change.
- Use URL-bound state only for non-sensitive, validated, backward-compatible filter or navigation values.

Protected/private properties are not persisted between Livewire requests. They may hold only reconstructable per-request dependencies or static values and must not be mistaken for durable component state.

## 13. Actions, forms and validation

Livewire actions are remotely invokable server boundaries.

- Every action validates untrusted state and authorizes the operation server-side.
- Identifiers and parameters passed from Blade, Alpine or events are untrusted even when generated by the application.
- Component/form validation improves interaction feedback; domain actions retain authoritative invariants.
- Mutations call domain/application actions rather than writing models ad hoc.
- Destructive actions require clear confirmation, exact scope and domain-supported recovery semantics.
- Retried or duplicate submissions are idempotent where the operation can be repeated.
- Expensive or long-running operations use authorized queued work with visible progress and failure recovery.
- Uploads and downloads use the shared file/storage capability and are validated, authorized, scanned and tenant-scoped.
- Validation errors and domain failures are mapped to translated, accessible feedback without leaking internals.

Public helper methods that are not intended as actions must be protected from arbitrary invocation through the supported Livewire mechanism or made non-public where the framework permits.

## 14. Authorization and tenancy

Authentication is resolved by the application. Policies and authorized domain actions remain authoritative for every mount, query, mutation, download, upload, event listener and background continuation.

- Test both the permitted path and relevant denied paths.
- Reauthorize records after hydration and immediately before mutation.
- Preserve tenant scope across route binding, computed queries, pagination, child components, events and queued work.
- Fail closed when a tenant-bound component lacks a valid tenant context.
- Do not trust a tenant, organization, team, owner or role identifier received from the browser.
- Invalidate or redirect stale components safely after permission, membership or tenant changes.

Hiding a component, button or navigation item never substitutes for authorization.

## 15. Events and component communication

Livewire and browser events coordinate presentation. They are not substitutes for versioned domain events.

- Event names use a documented package-qualified convention such as `module-cms.post-saved`.
- Payloads are minimal, named, serializable and free of secrets or unnecessary personal data.
- Event parameters are untrusted and validated/authorized by listeners.
- Prefer direct props, slots or parent/child composition when the relationship is local and explicit.
- Use targeted or self-directed events instead of global broadcasts where possible.
- Cross-module coordination uses public contracts or application composition, not undocumented event coupling.
- Breaking event-name or payload changes require a major package release.

Global JavaScript listeners return or invoke cleanup functions. Listeners registered around Livewire navigation must not accumulate across page visits.

## 16. Nesting, identity and reusable composition

Parent components own orchestration; child components own isolated interaction state. Inputs flow through documented props and outcomes flow through explicit actions or events.

- Every repeated child has a stable, domain-safe key.
- Keys must not expose sensitive identifiers unnecessarily.
- Do not use deeply nested components to conceal unclear responsibility or chatty request patterns.
- Do not share mutable state implicitly across unrelated components.
- Slots and attribute forwarding preserve documented accessibility and styling contracts.
- A reusable child depends on public value/read models rather than a parent's internal implementation.

Application-level components may compose several module components. They do not reach into the child packages' private PHP classes or views.

## 17. Loading, polling and Livewire 4 islands

Lazy loading, deferred loading, polling and islands are performance tools, not defaults.

- Lazy/deferred content provides a stable accessible placeholder with compatible dimensions where practical.
- Loading, stale, denied, offline, timeout and retry states are explicit.
- Polling is opt-in, visibility-aware, rate-conscious and stopped when the component no longer needs it.
- Islands isolate genuinely independent expensive regions; ordinary fast markup remains in the parent component.
- Island state shared with the root component is designed for concurrent requests and last-response behavior.
- Islands are not placed where Livewire 4 forbids their use, including directly inside loop or conditional control structures; put the control structure inside the island instead.
- Deferred work must not bypass policy or tenant checks merely because it runs in a later request.

Performance changes are justified with measured request count, payload, render/query time or browser evidence. Splitting a component is preferred when it creates a clearer ownership boundary; an island is preferred when only the render boundary needs isolation.

## 18. Navigation and page lifecycle

Use `wire:navigate` only on compatible same-origin application journeys. External, download, target-specific and protocol links retain normal browser behavior.

- Page components declare their layout, title, metadata, authorization and route input contract.
- Navigation preserves focus management, announcements, scroll expectations and browser history.
- Persistent elements do not retain stale actor, tenant, locale or permission state.
- JavaScript hooks account for `livewire:navigate`, `livewire:navigating` and `livewire:navigated` lifecycles.
- Document-level listeners are registered once or cleaned up explicitly.
- Critical authentication, checkout, account and destructive journeys have a safe full-page fallback where progressive enhancement is required.

Redirect destinations are trusted and validated. Components must not create open redirects from public properties or request input.

## 19. Alpine and JavaScript integration

Alpine and JavaScript enhance component-local presentation. Server-side domain state remains authoritative.

- Prefer Livewire's supported component script and lifecycle hooks.
- Keep client state local when the server does not need it; do not entangle it with public Livewire state unnecessarily.
- Treat values passed from `$wire`, `$event`, DOM attributes or third-party scripts as untrusted.
- Clean up observers, timers, global listeners and third-party instances on navigation or component teardown.
- Avoid duplicate Alpine or Livewire installations in package bundles.
- Third-party scripts follow `THEMES.md` consent, CSP, integrity/version and failure rules.
- JavaScript failures must not leave privileged operations appearing successful.

Package JavaScript and CSS use declared, deterministic asset entry points. Components must not depend on undocumented generated DOM or private Livewire internals.

## 20. Rendering, themes and accessibility

Module Livewire packages provide functional, accessible, theme-ready default views. Themes own final layout, tokens, styling and brand presentation.

A `theme-*-livewire` package may provide:

- presentation-state components such as menus, dialogs, filters and carousels;
- supported layouts, slots and view overrides;
- CSS/JavaScript assets and semantic design-token use;
- presentation-only hooks around module components.

It cannot replace policies, validation, routes, domain actions or module data access. Overrides preserve documented props, slots, events, test identifiers, loading states and accessibility behavior.

All components:

- use escaped output by default and sanitize explicitly allowed rich content;
- provide semantic structure, keyboard operation, visible focus and accessible names;
- announce validation, loading and success/error status appropriately;
- support zoom, reflow, reduced motion, forced colors and touch target requirements;
- translate visible strings and format dates, numbers, currencies and timezones through shared context;
- support right-to-left direction with logical properties where applicable;
- preserve meaningful behavior without optional scripts where progressive enhancement is required.

## 21. Performance and resilience

- Bound queries, pagination sizes, serialized payloads and component nesting.
- Avoid database or network work in repeatedly evaluated view expressions.
- Use computed state for derived data and cache only with actor/tenant/locale-safe keys.
- Debounce or defer inputs according to user intent and request cost.
- Prevent duplicate mutations during in-flight requests and communicate disabled/loading states.
- Queue long work rather than extending Livewire request duration.
- Optional modules, metrics, providers or assets fail independently with useful fallback states.
- Log failures with release, actor/tenant-safe and correlation context without serialized component secrets.

Each critical surface defines budgets for initial render, interaction latency, request count, payload size and query count where meaningful.

## 22. Security and privacy

- Treat every Livewire request like an authenticated HTTP endpoint.
- Validate and authorize public state, action parameters, route parameters, uploads and event payloads.
- Protect against mass assignment, insecure direct object references, tenant-scope bypass and enumeration.
- Do not serialize secrets or unnecessary personal information into snapshots, HTML, logs, events or browser storage.
- Rate-limit abusive or expensive operations.
- Apply recent-authentication requirements to privileged identity, payment, ownership and security changes.
- Audit privileged/destructive mutations with actor, tenant, target, outcome and correlation context.
- Ensure error messages and validation feedback do not reveal inaccessible records or internal implementation details.
- Test CSP compatibility and avoid unsafe inline scripts outside the application's nonce mechanism.

Disabling or uninstalling a Livewire presentation package never silently deletes domain data.

## 23. Lifecycle and configuration

The package service provider may:

- merge owned configuration;
- load translations and namespaced views;
- register its bounded component namespace;
- register package-owned routes through a documented registrar;
- register assets and development-only publishable resources;
- contribute an inspectable descriptor to the Liberu presentation registry.

Provider registration does not force rendering or route exposure. The root application resolves enabled packages, theme selection and compatible descriptors before composing surfaces.

Configuration has one owner and safe defaults. Supported options are typed and documented, such as enabled components, route prefix, pagination limits, polling intervals or optional capability integrations. Packages must not inspect arbitrary host classes, mutate unrelated configuration or use process-global mutable component state.

Install, enable, disable, upgrade and uninstall remain distinct lifecycle actions under `MODULES.md` and `THEMES.md`. Cache refresh after package or enablement changes is deterministic and documented.

## 24. Public extension points and versioning

Stable public Livewire surfaces include:

- package namespace and component aliases;
- documented props, slots and attribute behavior;
- action names and accepted inputs intended for consumers;
- presentation event names and payload contracts;
- full-page route names and parameters intended for linking;
- view namespaces, override contracts and test identifiers;
- theme hooks and asset entry points.

Consumers must not subclass internal components, replace private container bindings, edit installed package files, import private views, or depend on undocumented DOM and hydration payloads. Prefer composition, narrow callbacks, public contracts, slots and documented events.

Packages use semantic versioning and release independently. Breaking changes to stable surfaces require a major release and migration guide. Deprecations identify the replacement and planned removal version.

## 25. Testing

Livewire testing follows `TESTING.md`. Tests assert observable behavior through public component boundaries, use the smallest layer that supplies the required evidence, and remain deterministic, isolated and parallel-safe.

| Evidence | Primary owner |
|---|---|
| Component rendering, state, actions, events and namespace registration | `module-*-livewire` or `theme-*-livewire` package |
| Domain invariants invoked by a component | Owning domain package |
| Routes, layouts, theme composition and cross-module workflows | Root application |
| Visual identity, assets and presentation overrides | `theme-*-livewire` plus representative host |
| Minimum/current Livewire, Laravel and PHP compatibility | Independent package CI and host CI |

Every `module-*-livewire` package includes, where relevant:

- architecture tests preventing domain-to-Livewire dependencies, `App\\` coupling and cross-module internal access;
- namespace registration, alias resolution and collision tests;
- render and hydration tests for props, computed state, forms, pagination and nesting;
- action tests for validation, authorization, tenant isolation and delegation to domain actions;
- event tests for names, payloads, targeting and absence of forbidden leakage;
- upload/download, lazy, polling, island and navigation tests when those features are used;
- state tests for loading, empty, offline, stale, denied, error, retry and success behavior;
- security tests for unauthenticated access, insufficient permission, wrong tenant, manipulated identifiers, direct-object references, mass assignment and sensitive-data leakage;
- failure tests for duplicate submissions, retries, concurrency, partial completion and stale state;
- clean installation and boot tests in a minimal supported Laravel/Livewire host;
- compatibility tests for declared Laravel, Livewire and domain-package versions;
- host composition tests for representative routes, layouts and cross-module journeys.

Every `theme-*-livewire` package additionally follows `THEMES.md` and `TESTING.md` for render, accessibility, visual-regression, asset-build, CSP, localization/RTL, graceful-degradation, security and performance evidence. Browser tests are reserved for critical navigation, Alpine/JavaScript, accessibility and interaction behavior that cannot be proved reliably below the browser layer.

Meaningful PHP and Livewire behavior produces line coverage and branch/path coverage where supported reliably. Static CSS, imagery and templates use render, accessibility, visual, build and performance evidence instead of artificial line-coverage tests. Thresholds are risk-based; changed critical code must be thoroughly tested even when the repository threshold passes.

Each repository exposes stable Composer commands such as `composer test`, `composer test:feature`, `composer test:coverage` and `composer test:parallel`, limited to the suites it provides. Tests never contact production services, use live credentials or include production/personal data.

## 26. Continuous integration and compatibility

Pull-request CI runs formatting/linting, static analysis, architecture rules, unit/feature/Livewire tests, relevant security checks and coverage. Expensive browser, visual, mutation, performance and full compatibility jobs may run separately or on a schedule, but all release-required evidence completes before publication.

The compatibility matrix covers declared minimum and current supported PHP, Laravel, Livewire, domain-package and representative host combinations. Composer lowest-dependency testing is used where meaningful. Compatibility claims in manifests and documentation are verified by this matrix.

CI also proves:

- production namespace/alias resolution is deterministic;
- disabled or missing optional capabilities do not leak components or routes;
- navigation and global listener cleanup do not accumulate handlers;
- a clean locked install produces no unexpected `/modules` or `/themes` changes;
- documented Composer commands work;
- coverage and required browser/visual evidence are retained as protected artifacts rather than committed output.

Flaky tests are defects. Temporary quarantine requires an owner, linked issue, risk statement and expiry. Blind reruns do not define a passing result.

## 27. Documentation requirements

Each repository README documents:

- purpose and owning domain/theme;
- exact Composer, repository and installer name;
- installation path, manifest and lifecycle;
- required and optional dependencies;
- supported PHP, Laravel, Livewire and host versions;
- service-provider registration and component namespace;
- component, full-page route, prop, action, event and slot inventory;
- class-based default and any justified SFC/MFC exceptions;
- authentication, authorization, tenant and security behavior;
- loading, offline, failure and progressive-enhancement behavior;
- navigation, Alpine/JavaScript and asset integration;
- theme extension points, accessibility, localization and RTL behavior;
- performance budgets, local tests, CI, coverage and compatibility evidence;
- upgrade, deprecation, cache refresh and uninstall instructions.

Documentation follows `DOCUMENTATION.md`. Examples use public contracts, contain no secrets, identify package/application ownership, and remain executable against supported versions.

## 28. Definition of done

A Livewire 4 integration is ready when:

- its name has the correct `module-` or `theme-` prefix and `-livewire` suffix;
- it is independently packaged, versioned, documented and installed in the correct `/modules` or `/themes` location;
- class-based components use bounded, collision-checked namespaces and package views;
- every SFC/MFC exception is justified, namespaced and package-safe;
- domain logic remains outside Livewire and dependency direction is enforced;
- applications explicitly own route, layout, authentication and tenant composition;
- properties, actions, events, uploads and route inputs are validated, authorized and tenant-safe;
- loading, empty, offline, denied, error and success states are accessible and translated;
- navigation, JavaScript cleanup, islands, lazy behavior and performance are verified where used;
- installation, enablement, disablement, cache refresh and uninstall behavior are tested;
- architecture, feature, security, accessibility and compatibility suites pass;
- meaningful PHP/Livewire coverage is generated and reviewed, with critical browser/visual evidence retained where required;
- tests are deterministic, parallel-safe, free of production dependencies and exercised through documented Composer commands;
- a clean locked Composer install and production cache build are reproducible.

## 29. GitHub issue mapping

Create one Livewire integration epic, then child issues for: package/manifest scaffolding; namespace registration; component inventory; routes and full-page components; state/forms/actions; authorization and tenancy; events and nesting; navigation and JavaScript; lazy loading, polling and islands; theme integration; localization/accessibility; security/performance; compatibility tests; documentation and release.

Each issue identifies the owning `module-*-livewire` or `theme-*-livewire` package, component aliases, target routes/layouts, domain contracts, public props/actions/events/slots, authorization and tenant rules, extension points, failure states, acceptance criteria, tests and explicit exclusions.
