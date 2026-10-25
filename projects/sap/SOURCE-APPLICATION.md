# Enterprise SAP: current foundation and target business domains

**Observed application:** `enterprise-sap-laravel` at `b12a8c841c6a9054e52cac99d9ac1f233924a041`, cloned to `/home/liberu/projects/enterprise-sap-laravel`. The full organization listing reached 24 API pages and discovered this repository on page 23. Earlier partial-scan statements that no SAP repository existed were incorrect.

## What the source establishes

The checkout contains **40 immediate module directories** providing shared foundation capabilities and selected presentation adapters. The [source inventory](SOURCE-MODULES.md) records their manifests, and the [source mapping](SOURCE-MAPPING.md) keeps them separate from the 16 enterprise business-domain groups. Existing foundation packages are reused identities, not a new SAP-owned implementation for each capability.

The source README presents the application as an enterprise operations foundation. Its dependency manifest selects identity, teams, audit, settings, files, search, notifications, integrations, analytics, queues, themes and optional runtime services. Read [README.md](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/README.md) and [composer.json](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/composer.json); a package requirement is not proof that every enterprise business workflow is implemented.

## Host composition and presentation

The host [Filament plugin aggregator](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/app/Filament/ModulePlugins.php) resolves the selected module graph, asks manifests for plugins for the requested panel, constructs each plugin and checks its Filament plugin contract. It rejects duplicate plugin IDs. This is concrete cross-module presentation composition: a new enterprise workspace should use declared plugin/extension boundaries rather than copying foundation resources into a SAP package.

[routes/web.php](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/routes/web.php) declares a welcome page and an authenticated `/dashboard` redirect. The inspected redirect sends a super administrator toward the admin panel and other users toward the application dashboard. These host routes do not establish the proposed `/api/v1/enterprise/...` business operations in the detailed designs.

Installed module and theme directories remain tracked according to the source README. The package repository and lockfile govern durable changes; editing an installed host copy alone creates drift. Use the [Composer lifecycle guide](../../guides/COMPOSER.md) and [SAP clone guide](DEVELOPMENT.md).

## Resolver behavior must be read from this version

The host [config/modules.php](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/config/modules.php) uses `MODULES_ENABLED` and `MODULES_DISABLED` as deployment overrides. In the inspected [resolver implementation](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/module-manager/src/ModuleRegistry.php), a module is selected when it is not disabled and either its manifest default is enabled or its name appears in the enabled list. Required package/capability availability and versions are then checked, and dependency ordering/cycles are resolved.

Consequently, installing a package can affect the selected graph when its manifest enables it by default. Review the actual resolved graph, not just empty deployment lists or comments copied from another version. A declared manifest default, selected provider, commercial entitlement and a user's authorization remain distinct concepts.

Use the source-declared module inspection commands in a configured compatible environment. Inspect `module:list`, `module:features`, `module:status` and validation/cache commands through `php artisan list` and the installed command sources. This documentation review did not boot the application or execute its suites.

## Enterprise architecture is a target, not inferred code

The repository's [docs/ENTERPRISE_ARCHITECTURE.md](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/docs/ENTERPRISE_ARCHITECTURE.md) describes organizational structure, financial management, supply chain, people, assets and integrations. Treat that document as architectural intent unless the claimed behavior can be traced to its owning implementation and verified contract. The immediate installed package set is foundation-oriented; it does not establish independent implementations of all 16 domain groups.

The documentation's [composition design](COMPOSITION.md) therefore reuses Accounting, CRM, Billing, Commerce, Maintenance and Control Panel owners where verified contracts fit. The [detailed enterprise designs](design/README.md) specify missing orchestration, records, proposed operations, permissions, failures and per-layer requirements. Their proposed contracts remain clearly labelled while adoption work establishes implementation parity.

## Verification entry points

Source tests include [canonical module discovery](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/tests/Unit/CanonicalModuleDiscoveryTest.php), [Filament plugin composition](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/tests/Unit/ModuleFilamentPluginsTest.php), [team-scoped permissions](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/tests/Feature/TeamScopedPermissionTest.php), and [welcome behavior](https://github.com/liberusoftware/enterprise-sap-laravel/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/tests/Feature/WelcomeLandingTest.php). Their presence is not a passing-run claim. The root Composer manifest declares `test` as `vendor/bin/pest`; use the configured host/test environment and verify affected module consumers before adoption.

Next.js, Nuxt, React/Inertia and mobile enterprise plans can consume the reviewed owner APIs and share appropriate view components. Their proposed business screens do not become implemented because a foundation host exists. Track source, contract, UI parity and operational recovery per enabled workflow.
