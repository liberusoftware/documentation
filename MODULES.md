# Liberu Composable Package and Module Architecture

## Canonical Implementation Specification

**Status:** Source of truth
**Applies to:** All Liberu repositories, Composer packages, applications, and distributions
**Target stack:** Laravel 13, PHP 8.5, Filament 5, Livewire 4
**Related specifications:** [BOILERPLATE.md](BOILERPLATE.md) and [THEMES.md](THEMES.md)

## 1. Purpose

Liberu is a composable Laravel ecosystem built from independently reusable Composer packages. Modules use one unified design approach and may be mixed into different repository-based projects whenever their capabilities are required. Applications remain independent, while their modules are designed—within declared dependencies and compatibility constraints—to work in any Liberu repository and, where practical, any compatible Laravel application.

Each module is developed and released from an independent GitHub repository under the [`liberusoftware`](https://github.com/liberusoftware) organization. Composer resolves module versions, while the custom Liberu Composer installer places module packages in the host application's `/modules` directory instead of `/vendor`.

This document defines how Liberu capabilities are decomposed, packaged, named, discovered, installed, integrated, presented, tested, versioned, and operated. Product scopes define *what* to build. This document defines *where behavior belongs and how its boundaries interact*.

The governing principle is:

> Build a capability once, package it independently, and compose it into every application that needs it.

## 2. Architectural vocabulary

| Term | Meaning |
|---|---|
| Repository | Independent development, governance, and release workspace for an application, module, theme, or distribution |
| Composer package | Smallest independently versioned, installable, dependency-declaring code unit |
| Capability | Cohesive business or platform responsibility exposed through a stable public boundary |
| Module | An installed package capability represented in the runtime registry and subject to enablement/lifecycle rules |
| Product | A domain ecosystem such as CMS, Billing, or Ecommerce, normally composed from several packages |
| Application | Deployable Laravel host that selects packages, panels, routes, infrastructure, configuration, and enabled capabilities |
| Distribution package | Implementation-free Composer metapackage that installs a supported package set for convenience |
| Provider adapter | Package implementing a provider-neutral contract for one external system or regional implementation |
| Presentation package | Optional Filament, Livewire, API, or other interface adapter built on domain packages |
| Theme | Presentation assets and rendering overrides governed by `THEMES.md`; never a domain capability |

These terms are not interchangeable. In particular, installing code with Composer does not automatically enable or entitle its runtime capability.

For the standard module model, one independent GitHub repository contains one primary module Composer package. Aggregate/distribution and contract-only repositories are permitted where their category requires a different shape.

## 3. Architectural hierarchy

Dependencies point downward toward more stable and reusable abstractions:

```text
Application / Distribution
           |
Product and Presentation Packages
           |
Reusable Capability Core + Provider Adapters
           |
Domain Contracts and Shared Value Types
           |
Boilerplate Foundation
```

The four functional levels are:

1. **Foundation:** generic application infrastructure defined by `BOILERPLATE.md`.
2. **Reusable capabilities:** provider-neutral business capabilities usable by several products.
3. **Product capabilities:** behavior genuinely specific to one product domain.
4. **Applications and distributions:** deployable compositions and convenience dependency sets.

An application consumes the lowest-level package that provides what it needs. It must not install an entire product repository to obtain one capability.

## 4. Mandatory architecture rules

1. A repository is not automatically a package.
2. A product is not automatically a capability or module.
3. One package has one cohesive primary responsibility and one authoritative owner.
4. Reusable behavior is extracted only when it has a stable boundary and genuine reuse; speculative abstractions are avoided.
5. Applications compose packages; packages never depend on an application's `App\\` classes.
6. Dependencies point toward reusable contracts and foundation, never toward a consuming product.
7. Provider-neutral core packages never depend on provider adapters or vendor SDKs.
8. Provider-specific data and SDK usage remain inside the corresponding adapter package.
9. Domain packages never depend on Filament, themes, or another optional presentation layer.
10. Modules communicate through public contracts, commands, queries, events, registries, or stable identifiers—not another package's internal classes or tables.
11. Required dependencies are explicit, directional, version-constrained, and cycle-free.
12. Installation, runtime enablement, authorization, and commercial entitlement are distinct concerns.
13. Disabling or uninstalling a module never silently deletes data.
14. Side effects are authorized, auditable, idempotent, observable, and recoverable.
15. Shared foundation behavior is consumed from `BOILERPLATE.md`, not reimplemented by products.
16. Modules follow the same manifest, lifecycle, extension, testing, and documentation approach across all repositories.
17. A module must not assume which Liberu product application hosts it; product-specific optimization is declared without creating an unnecessary hard dependency.
18. Every module has an independent `liberusoftware` GitHub repository and a complete README unless an approved ADR documents an exception.

## 5. Package categories

Every package declares exactly one primary category.

### 5.1 Foundation packages

Foundation packages implement cross-repository application infrastructure: module management, identity, organizations, authorization, audit, settings, localization, currency context, notifications, files, queues, and observability. Their canonical feature boundaries are defined only in `BOILERPLATE.md`.

Foundation must not become a miscellaneous shared-code layer. A class belongs here only when it is domain-neutral and broadly reusable.

### 5.2 Contract packages

Contract packages define stable boundaries for capabilities with several consumers or implementations. They contain interfaces, immutable DTOs/value objects, enums, capability descriptors, and shared exceptions. They do not contain provider SDKs, Eloquent models, migrations, UI, or orchestration.

Examples: `liberu/payment-contracts`, `liberu/tax-contracts`, `liberu/search-contracts`, and `liberu/ai-contracts`.

Use a separate contract package only when consumers need the abstraction without the core implementation. Otherwise, keep the public contracts in the capability package to avoid package fragmentation.

### 5.3 Capability core packages

Capability packages own provider-neutral business behavior, orchestration, persistence, policies, and events reusable across products. Examples include `liberu/payment-core`, `liberu/subscription-core`, `liberu/media-core`, and `liberu/customer-core`.

A core package depends on contracts but not on an external provider implementation. It discovers optional implementations through explicit registration.

### 5.4 Provider and regional adapter packages

An adapter connects one contract to one external provider, protocol, jurisdiction, or platform. Examples include `liberu/payment-stripe`, `liberu/storage-s3`, `liberu/ai-openai`, and `liberu/tax-uk`.

Each adapter owns its SDK, credentials/configuration, provider identifiers, webhook receipts, mappings, rate-limit behavior, retries, sandbox support, and reconciliation logic. A provider adapter can be installed without changing the consuming domain.

### 5.5 Product packages

Product packages contain behavior specific to a product ecosystem, such as `liberu/cms-publishing`, `liberu/ecommerce-cart`, `liberu/crm-opportunities`, or `liberu/billing-invoices`. They may consume foundation and reusable capabilities but cannot duplicate them.

### 5.6 Presentation packages

Presentation is an optional adapter over domain packages. Typical packages include `liberu/cms-filament`, `liberu/ecommerce-filament`, or more granular packages where independent installation warrants it.

- A Filament package may provide plugins, resources, pages, widgets, forms, tables, actions, and navigation.
- A Livewire presentation package may provide interactive application components.
- An API presentation package may provide controllers, requests, resources, and route registration.
- Presentation packages depend on the domain contracts/actions they expose; domain packages never depend on them.
- Blade/CSS/JavaScript/assets and theme overrides also comply with `THEMES.md`.

### 5.7 Aggregate distribution packages

An aggregate such as `liberu/ecommerce` may require a supported set of packages for convenient installation. It contains no domain implementation, migrations, or provider assumptions. Users remain free to install only `liberu/ecommerce-catalog` or another subset.

## 6. Repository design

Applications and modules are independent repositories. An application repository composes released module packages; a module repository owns one cohesive capability and can be installed into multiple applications.

Application repository:

```text
cms-laravel/
├── modules/             # Composer-installed Liberu modules; tracked in Git
│   ├── cms-core/
│   ├── cms-content/
│   ├── cms-pages/
│   └── cms-filament/
├── app/                 # application-specific composition only
├── bootstrap/
├── config/
├── routes/
├── tests/               # cross-package/application tests
├── composer.json        # module requirements + Liberu installer plugin
└── composer.lock
```

Module source repository:

```text
github.com/liberusoftware/cms-content/
├── composer.json
├── module.json
├── README.md
├── CHANGELOG.md
├── src/
├── database/
├── resources/
└── tests/
```

The root application owns Laravel bootstrapping, environment/deployment configuration, package selection, panel composition, application routes, and cross-module integration tests. Reusable domain behavior does not remain under root `app/`.

The independent module repository owns implementation, releases, issues, tests, coverage, documentation, and its compatibility matrix. Product repositories consume tagged versions and contribute generic fixes back to the module repository rather than maintaining divergent copies.

## 6.1 Composer installation policy

The canonical custom installer package is `liberu/composer-installer`. It is a Composer plugin trusted through Composer's `allow-plugins` configuration and handles at least these package types:

| Composer package type | Install location |
|---|---|
| `liberu-module` | `<project-root>/modules/{module-name}` |
| `liberu-theme` | `<project-root>/themes/{theme-name}` |

Module `composer.json` files declare `"type": "liberu-module"` and a stable installer name in Composer `extra` metadata. The plugin must validate names, reject absolute paths and traversal, detect collisions, install deterministically, support install/update/remove, and remain compatible with Composer 2 security and plugin APIs.

Only Liberu module/theme package code uses the custom locations. Composer itself, Laravel/framework packages, vendor SDKs, and ordinary third-party libraries remain under `/vendor`. Modules continue to use Composer-generated autoloading; applications must not create a competing manual class scanner.

An application must explicitly require both the selected modules and the installer plugin. `composer.lock` remains authoritative for resolved versions. Production builds use non-interactive, locked, reproducible Composer installation and fail if the installer plugin or declared path policy is unavailable.

## 6.2 Tracked `/modules` policy

The current decision is **not to add `/modules` to `.gitignore`**. Installed module contents are committed in each consuming application repository alongside `composer.json` and `composer.lock`.

This policy provides visible and reviewable module changes, deterministic deployment inputs, and an application-level record of the exact composed code. It also requires discipline:

- run Composer commands to add/update/remove modules; never edit installed module files directly in a consuming application;
- make source changes in the module's independent repository, release a version, then update the consuming application;
- commit `composer.json`, `composer.lock`, and the corresponding `/modules` changes together;
- review installed-code diffs and release notes during dependency updates;
- CI performs a clean locked install and fails if it produces an uncommitted `/modules` diff;
- security/dependency tooling scans both `/vendor` and `/modules` as appropriate;
- merge conflicts in generated installed content are resolved by Composer from the intended lockfile, not by hand-merging module code.

This is an explicit current policy and may change only through an ADR with a migration plan. Regardless of tracking policy, the independent module repository remains the source of truth.

## 7. Standard package layout

```text
payment-core/             # root of its independent GitHub repository
├── composer.json
├── module.json
├── README.md
├── CHANGELOG.md
├── config/payment.php
├── database/
│   ├── factories/
│   ├── migrations/
│   └── seeders/
├── resources/
│   ├── lang/
│   └── views/           # functional defaults only, if needed
├── routes/              # only routes owned by this package
├── src/
│   ├── Actions/
│   ├── Contracts/
│   ├── Data/
│   ├── Domain/
│   ├── Events/
│   ├── Exceptions/
│   ├── Jobs/
│   ├── Listeners/
│   ├── Models/
│   ├── Policies/
│   ├── Providers/
│   ├── Queries/
│   ├── Services/
│   └── PaymentServiceProvider.php
└── tests/
    ├── Architecture/
    ├── Feature/
    └── Unit/
```

Create only directories the package uses. `src/` is its PSR-4 root. Filament classes belong in a separate presentation package rather than a `src/Filament` directory in the domain package. Composer installs this repository under `/modules/payment-core` in a consuming project.

## 8. Package independence

Every package that represents an architectural boundary must, where technically meaningful:

- have its own Composer metadata, namespace, service provider, manifest, configuration, migrations, tests, changelog, and documentation;
- declare PHP, Laravel, Liberu, framework, and extension dependencies explicitly;
- avoid unrelated product dependencies and application-specific helpers/configuration;
- boot in a clean supported Laravel host with only declared requirements installed;
- expose safe extension points instead of requiring source publication or copying;
- be independently testable and versionable even when released with a coordinated repository version.
- publish tagged releases from its independent `liberusoftware` repository and declare which applications/framework versions are tested.

Do not create a package for every class or table. Split when responsibility, dependency direction, optional installation, release cadence, provider isolation, ownership, or reuse requires a boundary.

## 9. Naming conventions

Composer names communicate domain, capability, and role:

| Package role | Convention | Example |
|---|---|---|
| Product capability | `liberu/{product}-{capability}` | `liberu/cms-publishing` |
| Shared contract | `liberu/{capability}-contracts` | `liberu/payment-contracts` |
| Shared core | `liberu/{capability}-core` | `liberu/payment-core` |
| Provider adapter | `liberu/{capability}-{provider}` | `liberu/payment-stripe` |
| Presentation adapter | `liberu/{product-or-capability}-{surface}` | `liberu/cms-filament` |
| Aggregate distribution | `liberu/{product}` | `liberu/ecommerce` |

Additional conventions:

| Item | Convention | Example |
|---|---|---|
| Namespace | `Liberu\\{Domain}\\{Capability}` | `Liberu\\Payment\\Core` |
| Manifest name | Stable Composer-aligned kebab-case | `payment-core` |
| Database tables | Package-owned prefix where useful | `payment_transactions` |
| Routes | Package-prefixed names | `billing.invoices.show` |
| Permissions | `{module}.{resource}.{action}` | `billing.invoices.refund` |
| Events | Past-tense domain fact | `PaymentCaptured` |
| Commands/actions | Imperative intent | `CapturePayment` |

Released names are public contracts. Renaming requires compatibility aliases or a documented migration.

## 10. Composer and manifest contracts

Composer is authoritative for code installation and static dependency resolution. Module packages declare `"type": "liberu-module"`, require the appropriate installer compatibility, and contain `module.json`:

```json
{
  "$schema": "https://schemas.liberu.dev/module/v1.json",
  "name": "payment-core",
  "display_name": "Payments",
  "description": "Provider-neutral payment orchestration.",
  "version": "1.0.0",
  "category": "capability",
  "provider": "Liberu\\Payment\\Core\\PaymentServiceProvider",
  "requires": {
    "php": "^8.5",
    "laravel": "^13.0",
    "packages": { "liberu/payment-contracts": "^1.0" }
  },
  "suggests": { "liberu/payment-stripe": "^1.0" },
  "capabilities": ["payments.orchestrate"],
  "default_enabled": false
}
```

The manifest describes runtime capability, lifecycle, compatibility, and optional relationships; it does not replace Composer. Contract-only packages and metapackages need no runtime provider or enablement entry unless they expose runtime capability.

CI validates the versioned schema, Composer/manifest consistency, dependency ranges, unique names/capabilities, category rules, cycles, providers, and referenced resources. Deployment configuration—not the package manifest—decides enablement.

The manifest also declares tested host families and any intentional product optimization. Compatibility is capability-based: a module may be installed in another repository when required contracts and versions are present. Missing optional capabilities disable the related integration gracefully; missing required capabilities fail dependency validation with an actionable message.

## 11. Installation, enablement, and entitlement

```text
Installed  -> code is present through Composer
Enabled    -> capability is active in this application/deployment
Entitled   -> actor, tenant, site, or plan may use the enabled capability
Authorized -> current actor may perform this operation on this record
```

These gates are evaluated independently. An installed Stripe adapter may be enabled for one site, commercially entitled for one plan, and still unavailable to an actor lacking refund permission.

Feature flags control rollout behavior inside an enabled capability. They do not substitute for Composer dependencies, installation migrations, entitlement, or authorization.

## 12. Discovery and lifecycle

The module manager performs deterministic startup:

1. Read manifests from Composer package metadata and configured local paths.
2. Validate manifest, Composer, application, and framework compatibility.
3. Resolve required dependencies, capabilities, and cycles.
4. Read installed version and deployment enablement state.
5. Sort enabled modules topologically with a stable tie-breaker.
6. Register service providers and cache the resolved registry in production.
7. Boot routes, policies, commands, events, schedules, views, and presentation plugins.

The lifecycle is:

| Action | Required behavior |
|---|---|
| Install | Validate dependencies, run idempotent migrations/hooks, and record version |
| Enable | Confirm installation/dependencies and expose capability entry points |
| Disable | Stop new entry points and schedules while retaining data and safe background handling |
| Upgrade | Run ordered migrations/hooks with compatibility and recovery guidance |
| Uninstall | Require explicit retention/export choice; preserve data by default |

Production lifecycle changes use deployments or privileged audited jobs, locks, progress reporting, and interruption recovery. Schema changes never run inside an ordinary web request.

## 13. Dependency inversion and provider adapters

The required direction is:

```text
Consuming product -> capability contract <- capability core
                                         <- provider adapter -> vendor SDK/API
```

For payments:

```text
ecommerce-checkout -> payment-contracts <- payment-core
                                        <- payment-stripe -> Stripe SDK
                                        <- payment-paypal -> PayPal SDK
```

Ecommerce and Billing depend on provider-neutral payment contracts/core. They never call a Stripe class, persist a Stripe intent identifier, or switch on provider names. `payment-stripe` alone uses the Stripe SDK and owns Stripe identifiers/webhook mappings.

This is dependency inversion: high-level domain policy and low-level adapters both depend on stable abstractions. Laravel container bindings or explicit registries connect them at application composition time.

## 14. Registries, strategies, and factories

Use an explicit capability registry when multiple implementations may coexist or be selected per tenant/site/context:

```text
PaymentGateway contract
        |
PaymentGatewayRegistry
        |-- StripePaymentGateway
        |-- PayPalPaymentGateway
        `-- AdyenPaymentGateway
```

- **Registry:** discovers named implementations and their declared capabilities.
- **Strategy:** selects behavior through a common contract without provider conditionals in consumers.
- **Factory/resolver:** creates a correctly configured implementation for trusted context.
- **Adapter:** translates provider concepts into domain contracts and back.

Registrations are explicit, collision-checked, cacheable, and inspectable. Resolution failures are actionable. Do not use a service locator throughout domain code; inject the narrow contract or an orchestration service.

## 15. Other required design patterns

- **Ports and adapters:** domain actions/contracts are ports; HTTP, Filament, queues, persistence, and providers are adapters.
- **Application service/action:** one use case coordinates authorization, domain objects, persistence, and events without embedding logic in controllers/components.
- **Command/query separation:** mutations express intent; authorized queries return purpose-built read models without exposing internal repositories.
- **Domain events:** immutable, past-tense facts decouple downstream work and projections.
- **Outbox/inbox:** transactionally publish events and deduplicate asynchronous consumption.
- **State machine:** model valid lifecycle transitions, guards, side effects, and terminal states explicitly.
- **Saga/process manager:** coordinate long-running cross-package workflows with recorded state and compensation.
- **Anti-corruption layer:** translate external or legacy terminology at the adapter boundary rather than leaking it into the domain.
- **Specification/policy:** encapsulate reusable eligibility and authorization rules with testable inputs.
- **Decorator/middleware:** add telemetry, caching, retries, or policy around contracts without changing domain implementations.

Patterns solve demonstrated design forces; they are not mandatory ceremony. Public abstractions must earn their maintenance cost through clarity, substitution, testing, or reuse.

## 16. Public package boundaries

A package may expose only documented surfaces:

- contracts and immutable DTOs/value objects;
- actions/commands for requested state changes;
- authorized queries or read models;
- versioned domain events describing completed facts;
- registries and capability descriptors;
- documented routes, APIs, commands, permissions, and extension points.

Models, migrations, tables, repositories, internal services, framework listeners, and provider payloads are private unless explicitly documented. Consumers must not instantiate another package's concrete internals merely because Composer autoloading makes them visible.

## 17. Data and database ownership

Each package owns its schema and authoritative writes. For example:

```text
payment-core       -> payments, payment_transactions
payment-stripe     -> stripe_payment_intents, stripe_webhook_receipts
ecommerce-orders   -> orders, order_items
billing-invoices   -> invoices, invoice_items
```

- Provider identifiers live in provider adapter tables, never consuming product tables.
- Cross-package references use stable platform identifiers, normally ULIDs, plus documented contracts.
- Direct cross-package foreign keys are used only for an explicit required dependency and cannot force an optional package to exist.
- A package never queries or mutates another package's tables directly.
- Shared concepts such as identity have one explicit owner; product packages add domain profiles keyed to that owner.
- Cross-product reporting consumes governed events/read models rather than coupling transactional schemas.
- Expand schema before new code depends on it and contract only after old consumers retire.
- Uninstall does not drop production data automatically.

## 18. Events, queues, and workflows

- Events carry stable identifiers and necessary facts, not serialized Eloquent models or provider payloads.
- Schemas are versioned; breaking changes publish a new version with a transition plan.
- Consumers are idempotent and account for duplicates and relevant out-of-order delivery.
- External calls, bulk work, file processing, and slow projections use queued jobs.
- Jobs declare actor/tenant context, timeout, retry, backoff, uniqueness, cancellation, and failure behavior.
- Publish transactional events through an outbox or after-commit mechanism; consumers persist inbox/deduplication state where needed.
- Long-running cross-package workflows record state and provide compensation or operator recovery.

Synchronous calls are appropriate for validation or queries that must complete inside one request and have a required dependency. Events are appropriate for facts and optional/asynchronous reactions. Do not use events to hide a required response or transactional invariant.

## 19. Service providers and application composition

`register()` binds contracts and merges configuration without request state or side effects. `boot()` registers package-owned routes, policies, commands, events, schedules, views, and publishable resources. Providers are idempotent and safe during configuration/route caching, CLI, queue, scheduler, test, and HTTP runtimes.

The application composition root selects:

- installed packages and provider adapters;
- enabled runtime modules and site/tenant configuration;
- concrete contract bindings and registry selections;
- Filament panels and presentation plugins;
- queue, cache, storage, database, broadcast, and observability infrastructure;
- deployment-specific security and entitlement policy.

Packages supply safe defaults and extension points. They do not inspect the host application's concrete classes or silently override unrelated bindings.

## 20. Filament, Livewire, API, and themes

Filament is an integration layer, not a domain dependency:

```text
Application panel
    `-- CMS Filament plugin -> CMS domain packages

CMS domain packages -X-> Filament
```

The root application defines panels. Presentation packages contribute explicit plugins. Domain packages remain usable through APIs, console commands, jobs, custom Livewire applications, or third-party Laravel applications without Filament installed.

- Controllers, Livewire components, and Filament actions invoke authorized application actions; they do not own domain rules.
- APIs use versioned resources, consistent errors, pagination, rate limits, and idempotency keys for retried writes.
- Filament resources apply policies and tenant scope to pages, actions, relation managers, exports, and global search.
- Themes may override stable views and assets but cannot replace routes, validation, policies, or business actions.
- CSS, JavaScript, Blade, layout, media, and Livewire presentation requirements follow `THEMES.md`.

## 21. External integrations and webhooks

Each provider adapter documents authentication, capabilities, provider mapping, webhook verification, rate limits, timeouts, retries, idempotency, sandbox behavior, observability, data residency, and reconciliation.

Webhook ingestion verifies authenticity, persists a receipt before processing, deduplicates provider event IDs, returns promptly, and processes asynchronously. Synchronizations use cursors/checkpoints with operator-visible replay and reconciliation. Provider outages degrade only dependent capabilities where possible.

## 22. Identity, tenancy, authorization, and configuration

Foundation behavior is consumed from `BOILERPLATE.md`. Domain packages:

- reference stable identity/organization/team identifiers and own only domain-specific profiles;
- accept trusted tenant/actor context through contracts rather than resolving it independently;
- declare permissions following `{module}.{resource}.{action}` and enforce policies at every entry point;
- keep configuration typed, validated, cache-compatible, and free of committed secrets;
- treat feature flags as temporary rollout controls with owner, telemetry, and removal date;
- require recent authentication, approval, or separation of duties where domain risk warrants it.

## 23. Observability and operations

Every runtime package supplies structured logs with correlation/module/tenant/actor identifiers, critical workflow metrics, required-versus-optional health checks, failed-job visibility, safe replay, and redaction rules. Operational packages include runbooks for expected failures, migrations, rollback, reconciliation, and provider outage.

Applications establish SLOs and alerts for end-to-end workflows; package telemetry provides the attributable signals without requiring knowledge of a specific monitoring vendor.

## 24. Testing strategy

Every package requires:

- unit tests for domain rules and value objects;
- feature tests for actions, policies, validation, persistence, and tenant isolation;
- contract tests shared by every implementation of a public contract;
- event/API schema compatibility tests;
- migration and upgrade tests from supported released versions;
- architecture tests preventing forbidden dependency directions, `App\\` coupling, domain-to-Filament dependencies, provider SDK leakage, and cross-package table access;
- failure tests for retries, duplicates, concurrency, partial workflows, authorization denial, and provider errors;
- an independent-install test in a minimal Laravel application.

Product repositories add composition tests proving their selected packages, provider adapters, plugins, and cross-package workflows work together. Distribution packages test dependency resolution but contain no implementation tests of their own.

## 25. Security and compliance

- Validate input at trust boundaries and encode output for its context.
- Apply least privilege to database, queue, storage, provider, package, and operator access.
- Audit security-sensitive reads and privileged mutations without logging secrets or regulated payloads.
- Define data classification, purpose, consent, retention, export, deletion, legal hold, and residency behavior per owning package.
- Scan Composer/npm dependencies and assets and maintain a vulnerability-response policy.
- Threat-model authentication, payments, files, webhooks, automation, and infrastructure capabilities.
- Prevent an optional module, adapter, or presentation package from widening authorization granted by its owning domain.

## 26. Versioning and release lifecycle

Packages use semantic versioning. Their public surface includes documented PHP contracts, configuration keys, commands, routes, APIs, events, permissions, manifest capabilities, registry keys, and extension points.

- Patch releases contain compatible fixes.
- Minor releases add backward-compatible behavior and may deprecate surfaces.
- Major releases contain incompatible changes with migration documentation.
- Deprecations identify replacement and planned removal version.

Each module repository releases independently while applications coordinate compatible version sets through Composer constraints and lockfiles. Compatibility matrices record supported PHP, Laravel, Filament/Livewire where relevant, database, package, provider, and tested Liberu application versions. Compatibility is not assumed merely because code can be installed.

## 27. Worked composition examples

### 27.1 Payments shared by products

```text
liberu/payment-contracts
          |
liberu/payment-core
          |
    +-----+----------------+
    |                      |
payment-stripe       payment-paypal
    |                      |
    +----------+-----------+
               |
        application registry
          /            \
ecommerce-checkout   billing-invoices
```

No product owns Stripe. Ecommerce owns cart/checkout/order policy. Billing owns invoice/collection policy. Payments owns authorization/capture/refund orchestration. Stripe owns translation to and from Stripe.

### 27.2 CMS product ecosystem

```text
cms-laravel
├── cms-core
├── cms-content
├── cms-pages
├── cms-media
├── cms-navigation
├── cms-publishing
├── cms-workflows
├── cms-api
└── cms-filament
```

A custom application may install content, pages, and API without navigation, workflows, the complete CMS aggregate, or Filament.

### 27.3 Full application composition

```text
Hosting commerce application
├── boilerplate foundation packages
├── cms-content + cms-media + cms-filament
├── ecommerce-catalog + ecommerce-cart + ecommerce-checkout
├── billing-subscriptions + billing-invoices
├── payment-core + payment-stripe
├── control-panel-provisioning
└── selected themes
```

The application is the composition root. It selects bindings, panels, enabled modules, entitlements, providers, and themes while all reusable behavior remains in packages.

## 28. Package implementation process

1. Define one capability, its terminology, owner, data, invariants, consumers, and exclusions.
2. Decide whether it belongs to foundation, shared capability, product, provider, presentation, or distribution.
3. Record dependency direction and package split in an ADR; reject cycles and speculative abstractions.
4. Extract the smallest provider-neutral contract needed by real consumers.
5. Implement core behavior without provider, application, or presentation dependencies.
6. Implement each provider or regional adapter separately and apply shared contract tests.
7. Add presentation packages independently where a surface is required.
8. Add Composer metadata, manifest/lifecycle, migrations, events, policies, telemetry, and documentation.
9. Test installation and operation in a clean Laravel application.
10. Compose and test the package in its primary product repository.
11. Add it to an aggregate distribution only when a supported convenience set is useful.

## 29. Documentation requirements

Every module repository contains a professionally written `README.md` stating purpose, screenshots/examples where useful, category, ownership/maintainers, Composer installation, `/modules` install behavior, dependencies, supported/tested applications, enablement, entitlement expectations, configuration, migrations, permissions, public contracts/events, data ownership, routes/commands/jobs, extension points, provider behavior, security/data classification, telemetry, failure recovery, testing, coverage, changelog/releases, contribution guidance, and upgrade/uninstall instructions.

Module CI generates test coverage in a machine-readable format and a browsable report where the test framework supports it. The README displays the current CI and coverage status/badge and explains how to run the tests locally. Coverage is evidence, not a substitute for meaningful unit, feature, contract, architecture, integration, security, and failure-path tests. Generated HTML coverage output is retained as a CI artifact or release asset and is not normally committed to source.

Repositories document the package map and dependency diagram. Applications document selected packages, bindings, enabled capabilities, panels, providers, themes, and deliberate exclusions. Significant boundary decisions use ADRs.

## 30. Definition of done

A package is complete when:

- its capability, category, owner, exclusions, dependencies, and manifest are approved;
- it is independently installable and does not depend on `App\\`, an unrelated product, provider implementation, or presentation framework;
- install, enable, disable, upgrade, failure, and recovery paths work where applicable;
- persistence and provider data remain inside their owning package;
- domain behavior and entry points are authorized, tenant-safe, idempotent, and auditable;
- public contracts/events are versioned, documented, and covered by consumer/implementation tests;
- presentation is optional and complies with `THEMES.md`;
- architecture, security, compatibility, migration, and product-composition tests pass;
- logs, metrics, health checks, alerts, runbooks, changelog, and upgrade notes are available.
- the independent GitHub repository, README, CI workflow, generated coverage report, release tag, and tested-host compatibility evidence are available;
- a clean locked install places the module in `/modules`, and the consuming repository has no unexpected Composer-generated diff.

## 31. GitHub issue mapping

Create one epic per package boundary—not automatically one epic per repository. Recommended child issues:

1. Approve capability ownership, package category, terminology, dependency ADR, and exclusions.
2. Scaffold Composer package, namespace, manifest, provider, configuration, and lifecycle.
3. Define public contracts, DTOs, registries, events, and contract tests.
4. Implement domain rules, actions, persistence, policies, audit, and failure behavior.
5. Implement provider/regional adapters with webhook, retry, idempotency, and reconciliation support.
6. Implement optional Filament, Livewire, API, console, and theme extension packages.
7. Add independent-install, architecture, migration, compatibility, security, and product-composition tests.
8. Add telemetry, health checks, operational runbook, README, changelog, adoption example, and upgrade guide.

Each issue states user outcome, owning package, category, dependencies, public surfaces, requirements, acceptance criteria, tests, observability, security/data considerations, migration impact, and explicit exclusions.
