# Build and release presentation layers

Start with the [project repository catalog](../../projects/REPOSITORIES.md) for Boilerplate templates, all product skeletons and layer-specific initialization commands.

Use these implementation runbooks after choosing a capability and its canonical core owner. They describe new skeletons and adapter implementations, not packages that are already published. Confirm actual package names, callable contracts and availability in the [source inventory](../../architecture/SOURCE-INVENTORY.md), the project's `DEVELOPMENT.md` and `SOURCE-MAPPING.md`, and [source references](../../modules/source/README.md). All `example` names, DTOs and routes below are teaching examples to replace with reviewed contracts.

| Surface | Host skeleton pattern | Module foundation & skeleton catalog | Skeleton and implementation | Package and release |
| --- | --- | --- | --- | --- |
| Vue + Inertia | `project-{product}-laravel-inertia-vue` | [`module-boilerplate-vue-inertia`](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../modules/skeletons/laravel-inertia-vue.md) | [Laravel host and Vue pages](INERTIA.md) | [Vue library build](PACKAGES.md#3-vue-library) and [npm release](PACKAGES.md#6-publish-the-reviewed-tarball) |
| React + Inertia | `project-{product}-laravel-inertia-react` | [`module-boilerplate-react-inertia`](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../modules/skeletons/laravel-inertia-react.md) | [Laravel host and React pages](INERTIA.md) | [React library build](PACKAGES.md#2-react-library) and npm release |
| Nuxt (Vue) | `project-{product}-nuxt-vue` | [`module-boilerplate-nuxt`](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../modules/skeletons/nuxt-vue.md) | [Nuxt application and adapter](NUXT.md) | Vue library or explicit Nuxt layer, then npm release |
| Next.js (React) | `project-{product}-next-react` | [`module-boilerplate-nextjs`](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../modules/skeletons/next-react.md) | [Next.js application and adapter](NEXTJS.md) | React library with server/client exports, then npm release |
| React Native, including Expo | `project-{product}-mobile-react` | [`module-boilerplate-react-native`](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../modules/skeletons/mobile-react.md) | [Device application and adapter](REACT-NATIVE.md) | [Metro-compatible npm library](REACT-NATIVE.md#7-build-a-reusable-mobile-package), signed iOS/Android builds |
| Flutter | `project-{product}-mobile-flutter` | [`module-boilerplate-flutter`](https://github.com/liberusoftware/module-boilerplate-flutter) · [catalog](../../modules/skeletons/mobile-flutter.md) | [Device application and Dart package](FLUTTER.md) | Dart/pub release, signed iOS/Android builds |
| Dart desktop | `project-{product}-dart-desktop` | [`module-boilerplate-dart-desktop`](https://github.com/liberusoftware/module-boilerplate-dart-desktop) · [catalog](../../modules/skeletons/dart-desktop.md) | [Separate native desktop application](DART.md) | Dart/pub modules (`module_*_dart_desktop`); Linux, macOS and Windows native builds |
| Dart mobile | `project-{product}-dart-mobile` | [`module-boilerplate-dart-mobile`](https://github.com/liberusoftware/module-boilerplate-dart-mobile) · [catalog](../../modules/skeletons/dart-mobile.md) | [Separate native mobile application](DART.md) | Dart/pub modules (`module_*_dart_mobile`); signed iOS/Android builds |

## Working with the GitHub skeleton repositories

The organization provides **128 application host skeletons** (`project-{product}-{suffix}`, cataloged in [REPOSITORIES.md](../../projects/REPOSITORIES.md)), **16 shared product API backends** (`project-{product}-laravel-api`, documented in [LARAVEL-API-BACKENDS.md](../LARAVEL-API-BACKENDS.md)), and **5,679 capability module skeleton repositories** (`module-{capability}-{suffix}`, cataloged in [modules/skeletons/README.md](../../modules/skeletons/README.md)).

1. **Application host skeletons (`project-{product}-{suffix}`):** Provide the framework shell, pinned toolchain (`.node-version`, `.flutter-version`, `composer.json`, `package.json`, `pubspec.yaml`), lockfiles, and an open GitHub wayfinder issue ([IMPLEMENTATION-ISSUES.md](../../projects/IMPLEMENTATION-ISSUES.md)) containing the technology-specific implementation method, technical specification ([wayfinders/](../../projects/wayfinders/README.md)), and capability checklist.
2. **Capability module skeletons (`module-{capability}-{suffix}`):** Derived from the matching `module-boilerplate-*` template, each repository records its capability key and foundation commit in `module-skeleton.json`. They provide package structure, exports, and typecheck/build scripts—not completed business UI or certified registry releases.
3. **Skeleton-to-feature implementation workflow:**
   - Open the host's wayfinder issue and select a capability from the checklist.
   - Read the capability's `features/{module}.md`, `core/{module}.md`, `api/{module}.md`, and `{layer}/{module}.md` specifications, including its structured feature/aspect matrix and observed source evidence.
   - Ensure the core domain actions/queries and `project-{product}-laravel-api` endpoints (or Laravel Inertia controller routes) are implemented and tested first.
   - Implement each feature/aspect in the matching `module-{capability}-{suffix}` skeleton repository, preserving `module-skeleton.json` provenance and replacing placeholder exports with tested components, hooks/composables, or widgets.
   - Verify the packed module in a clean consumer and compose it into the `project-{product}-{suffix}` host skeleton with end-to-end journey, authorization, tenancy, accessibility, and recovery tests before checking the wayfinder item.

For a concrete source-backed capability, compare the [CRM sales-pipeline walkthrough](../../projects/crm/guides/SALES-PIPELINES.md) with the matching core/API/presentation plans. Use its recorded source contracts as evidence, while keeping any new frontend implementation explicitly planned until built and verified.

## 1. Decide the application boundary

Inertia is hosted by Laravel: a controller invokes an authorized public application action/query and returns Inertia props or redirects. Nuxt, Next.js and mobile applications are separate API consumers. Nuxt uses Vue; Next.js uses React. Neither uses Inertia page visits to fetch an ordinary JSON API. See [presentation architecture](../../architecture/PRESENTATION.md).

Use one canonical core package for a capability, a reviewed API adapter for remote clients, and a presentation adapter for each enabled surface. Keep authentication, tenant resolution, policy, persistence, transactions, idempotency and audit authoritative on the Laravel side. Browser and device packages cannot depend on PHP private classes. Shared frontend DTOs represent the reviewed public contract; they do not define new business rules.

## 2. Establish the foundation before generating screens

1. Choose a product and [adoption profile](../../architecture/ADOPTION.md). Record audience, enabled modules, API versions, runtime/framework versions, supported browsers or devices, and deployment topology.
2. Start the Laravel host from the [boilerplate foundation](../../projects/boilerplate/BOILERPLATE.md) or an existing product clone using [installation](../../INSTALL.md) and its source-backed development instructions. Use PHP 8.5/Laravel 13 for new target architecture; an observed older clone follows its actual manifest until deliberately upgraded.
3. Install compatible canonical core/API packages using their **actual Composer identities** and the [Composer workflow](../COMPOSER.md). The Liberu installer owns placement under `/modules`; do not hand-copy vendor code or infer an npm name from a repository slug. Review/allow only the required Composer plugins.
4. Configure a local database, session store, queues and storage from `.env.example`; generate the local application key and run reviewed migrations against that local database. Never regenerate an existing production key. Run the host's existing tests before adding an adapter.
5. Enable required modules using the host's documented registry/lifecycle integration. There is no assumed universal `module:enable` command. Installation, enablement, entitlement and authorization are separate checks.
6. Review the public action/query and HTTP schemas. Record actor/tenant establishment, fields, pagination, validation, denied access, conflicts, pending operations and reconciliation. Generate DTOs from the reviewed schema or write checked mappers. Never invent an endpoint to match a screen.
7. Add a presentation shell, then implement one vertical journey: sign in, establish workspace context, list authorized records, submit one command, display its authoritative result, and sign out. Expand after that journey passes integration checks.

### Start a foundation clone

For a new local application based on the existing foundation repository:

```bash
git clone https://github.com/liberusoftware/project-boilerplate-laravel-filament.git example-api
cd example-api
cp .env.example .env
composer install
```

Review `composer.json`, `composer.lock`, the repository README and [boilerplate development instructions](../../projects/boilerplate/DEVELOPMENT.md) before proceeding. Configure `.env` for a new local database, URL, session/queue/storage services; then run `php artisan key:generate`, `php artisan migrate` and the declared tests. Run seeders only when documented for that environment. Install any existing frontend from its lock before adding or replacing a presentation entry. Preserve foundation modules and configure the chosen surface through their public hooks rather than layering a second starter-kit identity implementation onto the clone. Change the Git remote only when intentionally creating an independently owned application repository.

## 3. Keep skeletons small and composable

A private application owns routes, navigation, layouts, session integration, configuration, observability and deployment. A reusable adapter owns capability-specific components and transport mapping. It must not import application aliases such as `@/auth` or an application's `App\\` classes. Inject transport/session dependencies at a public boundary. An application can orchestrate several capabilities without becoming a second owner of their records.

For separate releases, use independent repositories. A temporary integration workspace may use this layout:

```text
integration-workspace/       # private package.json; workspaces apps/*, packages/*
  apps/web/                  # selected browser shell, not every framework at once
  apps/mobile/               # selected device shell
  packages/contracts/        # reviewed/generated DTOs, no secrets or UI runtime
  packages/module-example/   # one adapter package with its own manifest
```

Use actual module basenames (`module-<capability>-vue-inertia`, `module-<capability>-react-inertia`, `module-<capability>-nuxt`, or the layer's documented name). A PHP bridge and a JavaScript library have distinct manifests and release artifacts, even when they share a repository. Prefer explicit package exports and application registration to scanning every installed directory at runtime.

## 4. Pin and document the generated baseline

Bootstrap commands using `@latest` are for a new empty directory only. Review the selected versions against the repository standards, record the generator version, commit the resulting manifests and lockfiles, and pin the CI toolchain. Existing clones use `npm ci`, their declared alternative package manager, or `flutter pub get`; do not rerun generators over existing work. Keep app manifests private (`private: true` for npm, `publish_to: none` for Dart). Commit safe example configuration, never credentials.

## 5. Definition of a usable skeleton

A skeleton is ready when a clean clone installs from locks, checks/types and production builds pass, the vertical journey works against the compatible Laravel host, denied/wrong-tenant requests fail at the server, logout removes scoped state, errors preserve safe drafts, and the README lists configuration, commands, supported versions and deployment/recovery steps. For mobile, include two physical-platform release checks, lifecycle/deep-link behavior and store distribution; a browser preview is insufficient.

Follow [package building and npm publishing](PACKAGES.md) after implementation. Publish libraries separately from deploying applications; use prereleases and clean consumers before stable adoption. Do not declare parity across surfaces based on copied module plans.
