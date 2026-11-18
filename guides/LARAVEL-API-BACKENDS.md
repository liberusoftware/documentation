# Laravel API Backends and Frontend Clients

Each product has a `project-{product}-laravel-api` repository: a dedicated Laravel 13 / PHP 8.5 HTTP backend that serves the matching product's independently deployed Next.js, Nuxt, React Native, Flutter, Dart mobile, and Dart desktop applications. One deployed product API backend supports multiple web, mobile, and desktop clients against the same authorized domain modules, persistence, and workflow contracts while each client maintains its own UI, build pipeline, and release lifecycle.

The [repository map](../projects/REPOSITORIES.md#laravel-applications) lists every product's `-laravel-api` repository alongside its Filament, Inertia, web, mobile, and desktop presentation repositories. Provisioning a repository does not establish implemented endpoints or product parity; consult each repository's `README.md`, `composer.json`, committed lockfiles, and OpenAPI specification for verified operations.

## 1. Product API backend catalog

| Product | Shared Laravel API backend | Product scope | API module catalog |
| --- | --- | --- | --- |
| Boilerplate Foundation | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | [BOILERPLATE.md](../projects/boilerplate/BOILERPLATE.md) | [43 API plans](../projects/boilerplate/api/README.md) |
| Accounting ERP | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [ACCOUNTING.md](../projects/accounting/ACCOUNTING.md) | [241 API plans](../projects/accounting/api/README.md) |
| Automation | [`project-automation-laravel-api`](https://github.com/liberusoftware/project-automation-laravel-api) | [AUTOMATION.md](../projects/automation/AUTOMATION.md) | [57 API plans](../projects/automation/api/README.md) |
| Billing | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | [BILLING.md](../projects/billing/BILLING.md) | [81 API plans](../projects/billing/api/README.md) |
| Browser Game | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | [BROWSER-GAME.md](../projects/browser-game/BROWSER-GAME.md) | [61 API plans](../projects/browser-game/api/README.md) |
| CMS | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | [CMS.md](../projects/cms/CMS.md) | [252 API plans](../projects/cms/api/README.md) |
| Control Panel | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | [CONTROL-PANEL.md](../projects/control-panel/CONTROL-PANEL.md) | [61 API plans](../projects/control-panel/api/README.md) |
| CRM | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [CRM.md](../projects/crm/CRM.md) | [218 API plans](../projects/crm/api/README.md) |
| Ecommerce | [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) | [ECOMMERCE.md](../projects/ecommerce/ECOMMERCE.md) | [108 API plans](../projects/ecommerce/api/README.md) |
| Enterprise SAP | [`project-enterprise-sap-laravel-api`](https://github.com/liberusoftware/project-enterprise-sap-laravel-api) | [SAP.md](../projects/sap/SAP.md) | [16 API plans](../projects/sap/api/README.md) |
| Genealogy | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | [GENEALOGY.md](../projects/genealogy/GENEALOGY.md) | [62 API plans](../projects/genealogy/api/README.md) |
| Liberu Platform | [`project-liberu-official-laravel-api`](https://github.com/liberusoftware/project-liberu-official-laravel-api) | [LIBERU.md](../projects/LIBERU.md) | [4 API plans](../projects/liberu/api/README.md) |
| Maintenance | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | [MAINTENANCE.md](../projects/maintenance/MAINTENANCE.md) | [60 API plans](../projects/maintenance/api/README.md) |
| Music DAW | [`project-music-daw-laravel-api`](https://github.com/liberusoftware/project-music-daw-laravel-api) | [MUSIC.md](../projects/music/MUSIC.md) | [22 API plans](../projects/music/api/README.md) |
| Real Estate | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | [REAL-ESTATE.md](../projects/real-estate/REAL-ESTATE.md) | [70 API plans](../projects/real-estate/api/README.md) |
| Social Network | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | [SOCIAL-NETWORK.md](../projects/social-network/SOCIAL-NETWORK.md) | [59 API plans](../projects/social-network/api/README.md) |

## 2. Backend ownership and module composition

The `-laravel-api` application is the product's HTTP composition root:

```text
project-{product}-laravel-api (Application composition root)
  ├── Foundation modules (identity-core, organizations-teams, roles-permissions, api-access, audit, webhooks)
  ├── Product domain modules (module-{capability} — owns domain rules, actions, queries, policies, migrations)
  └── Matching API adapters (module-{capability}-api — owns Form Requests, Controllers, API Resources, OpenAPI fragment)
```

1. **One-to-one API adapters:** Every independent domain module that exposes HTTP operations provides a matching `module-{capability}-api` Composer package (installed and tracked under `/modules`). The `-laravel-api` host selects and enables those packages; it never collapses multiple independent domain modules into a monolithic controller layer.
2. **Authoritative domain execution:** Controllers in `module-{capability}-api` validate transport shape, resolve the authenticated actor and active tenant/team/store context from trusted middleware, authorize through the domain policy, and delegate to typed public actions and queries in `module-{capability}`.
3. **Tracked `/modules` policy:** Just like `-laravel-filament` and `-laravel-inertia-*` hosts, `-laravel-api` hosts keep installed `/modules` (and `/themes` where applicable) committed alongside `composer.lock` in accordance with [MODULES.md §6.2](../architecture/MODULES.md#62-tracked-modules-policy).
4. **OpenAPI 3.1 aggregation:** Each `module-{capability}-api` package contributes a validated OpenAPI 3.1 fragment (`openapi/v1/{module}.yaml`). The `-laravel-api` host bundles enabled fragments into a single versioned product specification and fails CI on path, operation-ID, schema, or scope collisions. See [API.md §8](../architecture/API.md#8-openapi-and-contract-registry).

## 3. Implementing a capability slice in `project-{product}-laravel-api`

1. **Initialize and verify the host:**
   ```bash
   git clone https://github.com/liberusoftware/project-boilerplate-laravel-api.git
   cd project-boilerplate-laravel-api
   cp .env.example .env
   composer install
   php artisan key:generate
   php artisan migrate
   php artisan test
   ```
2. **Require the domain and API packages:** Check [SOURCE-MAPPING.md](../projects/README.md) and [observed source references](../modules/source/README.md) for the exact Composer identities. Install the core package and its matching `-api` adapter via Composer so the module installer places them under `/modules/`.
3. **Configure route groups and middleware:**
   - Mount versioned routes under `/api/v1/{module}/{resources}`.
   - Apply `auth:sanctum` (or approved OAuth/service credentials), ability/scope checks (`abilities:{module}.{resource}.{action}`), tenant/team/store context resolution, and endpoint rate limiters.
   - Enforce `Idempotency-Key` middleware on retryable state-changing `POST` commands and `If-Match` ETag preconditions on concurrency-sensitive updates.
   - Format all validation, authorization, conflict, and rate-limit failures as `application/problem+json` ([RFC 9457 Problem Details](../architecture/API.md#11-errors-and-validation)).
4. **Return asynchronous operations where required:** Slow, bulk, or provider-dependent work dispatches an authorized queued job and returns `202 Accepted` with a pollable `/api/v1/operations/{operation_id}` resource rather than blocking the HTTP worker.
5. **Verify and publish the contract:** Run Pest 5 feature/contract tests covering allowed, unauthenticated (`401`), forbidden/wrong-tenant (`403`/`404`), invalid (`422`), stale/conflict (`409`/`412`), and throttled (`429`) paths, validate OpenAPI parity, and publish the updated schema for client generation.

## 4. Client responsibilities and integration matrix

| Client repository suffix | Framework & runtime | Integration with `project-{product}-laravel-api` | Implementation runbook & wayfinder |
| --- | --- | --- | --- |
| `-next-react` | Next.js App Router + React 19.2 | Server Components, Route Handlers, and Server Actions call `API_BASE_URL` (`server-only`); default authenticated fetches to `cache: 'no-store'`; isolate any opt-in cache tags by tenant and actor. | [NEXTJS.md](presentation/NEXTJS.md) · [next-react](../projects/wayfinders/next-react.md) |
| `-nuxt-vue` | Nuxt 4 + Vue 3 | Nitro server handlers and `useFetch`/`$fetch` call `runtimeConfig.apiBase`; scope SSR payload hydration and cache keys by actor and tenant; keep secrets out of `runtimeConfig.public`. | [NUXT.md](presentation/NUXT.md) · [nuxt-vue](../projects/wayfinders/nuxt-vue.md) |
| `-mobile-react` | React Native + Expo | Typed TypeScript API client calls `EXPO_PUBLIC_API_BASE_URL` with OAuth PKCE or Sanctum mobile tokens stored in Keychain/Keystore (`expo-secure-store`); explicit offline draft queue and idempotent retry reconciliation. | [REACT-NATIVE.md](presentation/REACT-NATIVE.md) · [mobile-react](../projects/wayfinders/mobile-react.md) |
| `-mobile-flutter` | Flutter Mobile (`iOS` / `Android`) | Typed Dart DTOs and repositories call `--dart-define=API_BASE_URL=...` with platform-secure credentials; account-isolated local drafts and foreground refresh on resume. | [FLUTTER.md](presentation/FLUTTER.md) · [mobile-flutter](../projects/wayfinders/mobile-flutter.md) |
| `-dart-mobile` | Dart Mobile (`iOS` / `Android`) | Separate Dart/Flutter mobile host and store release identity consuming the same product API with `module_{capability}_dart_mobile` packages. | [DART.md](presentation/DART.md) · [dart-mobile](../projects/wayfinders/dart-mobile.md) |
| `-dart-desktop` | Dart Desktop (`Linux` / `macOS` / `Windows`) | Dedicated desktop Flutter host consuming the product API with `module_{capability}_dart_desktop` packages, keyboard/focus navigation, multi-window draft safety, and authorized print/export. | [DART.md](presentation/DART.md) · [dart-desktop](../projects/wayfinders/dart-desktop.md) |

Clients own presentation, navigation, and local interaction state. They submit explicit commands and render approved DTO projections; authorization, tenancy, pricing, and domain invariants are always rechecked by the `-laravel-api` backend. Clients never connect directly to the database or reimplement server-side business rules.

## 5. Connect, version, and release

- Configure each client with the deployed `-laravel-api` base URL and a supported major contract version (`/api/v1`). The frontend repository URL is never an API endpoint.
- Establish authentication per audience: browser cookie/BFF flows require explicit origin, `SameSite`, and CSRF controls; native mobile and desktop clients use OAuth 2 Authorization Code + PKCE or scoped personal/device tokens in platform-secure storage.
- Deploy backward-compatible `-laravel-api` changes before releasing dependent web, mobile, or desktop clients, and maintain old contract versions across the mobile/desktop binary support window.
- Filament (`-laravel-filament`) and Laravel Inertia (`-laravel-inertia-react`, `-laravel-inertia-vue`) hosts remain full Laravel applications with their own server-side composition and session routes. See [API.md](../architecture/API.md), [MODULES.md](../architecture/MODULES.md), and [IMPLEMENTATION-WAYFINDERS.md](../projects/IMPLEMENTATION-WAYFINDERS.md).
