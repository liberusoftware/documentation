# Laravel API backends and frontend clients

Each product is gaining a `project-{product}-laravel-api` repository: a Laravel backend that serves the matching product's Next.js, Nuxt, Flutter, React Native and Dart mobile/desktop applications. One deployed product API can support several of these clients against the same authorized data and workflows. Each client has its own UI, build and release lifecycle.

These repositories are being introduced. The [repository map](../projects/REPOSITORIES.md#laravel-applications) records their intended names alongside the existing hosts; repository provisioning does not establish implemented endpoints or product parity. Use the selected repository's README, manifests, lockfiles and tested API contract for actual setup and supported features.

## Backend ownership

The `-laravel-api` application is the product's API composition root. It selects domain modules and their matching API adapters, configures authentication, tenant/store resolution, routes, rate limits and exposure policy, and publishes the combined versioned OpenAPI contract. Laravel executes authorized domain actions and owns database access, transactions, queues, provider integrations and audit/operational infrastructure through those modules.

`project-ecommerce-laravel-api`, for example, composes Ecommerce capabilities for storefront and device clients. A package such as `module-ecommerce-catering-api` exposes only Catering's HTTP contract and is installed into the host; it is not another product backend. Domain modules remain authoritative for business rules and persistence. See [API composition](../architecture/API.md#20-application-and-project-apis) and [module boundaries](../architecture/MODULES.md).

## Client responsibilities

| Client repository suffix | Integration with the matching `-laravel-api` host |
| --- | --- |
| `-next-react` | Next.js server/client components consume the approved HTTP contract; keep server credentials private and isolate authenticated rendering/caches. |
| `-nuxt-vue` | Nuxt server/client code consumes the same contract; scope SSR payloads and caches to the authenticated user and tenant. |
| `-mobile-react` | React Native/Expo uses a typed API client, approved device authentication, secure credential storage and explicit reconnect behavior. |
| `-mobile-flutter` | Flutter uses typed Dart models/clients and platform-secure credentials; local UI state does not replace server validation. |
| `-dart-mobile`, `-dart-desktop` | Separate Dart/Flutter hosts consume the product API with their own mobile or desktop navigation, storage and release configuration. |

Clients own presentation, navigation and local interaction state. They send commands and render approved DTOs; authorization, tenancy, pricing and other domain invariants are rechecked by the backend. Clients never connect directly to its database or copy its business rules. Browser-only or native capabilities remain subject to each product's surface support plan.

## Connect and release

Configure each client with the deployed API base URL and a supported contract version. The frontend repository URL is not an API endpoint. Agree authentication per audience: browser cookie/session flows require appropriate origins and CSRF handling; device token flows require secure storage and token lifecycle handling. Keep provider secrets on the backend. Follow the [API security contract](../architecture/API.md) rather than assuming the skeleton has these flows implemented.

Publish validated OpenAPI schemas and examples before generating clients. Coordinate compatibility tests, error/pagination formats, revision conflicts and idempotent retries; offline mutations need explicit synchronization rules. Release backend and clients independently while preserving supported contract versions and migration compatibility.

Filament and Laravel Inertia repositories remain application hosts with their own server-side composition. Inertia pages normally use their host's routes and sessions; selecting the new API backend is the deployment boundary for independent clients. Shared capability packages can be reused across hosts. Keep installed `/modules` and `/themes` committed in consuming Laravel hosts alongside their lockfiles, as required by the [module](../architecture/MODULES.md#62-tracked-modules-policy) and [theme](../standards/THEMES.md#32-independent-repositories-and-tracked-themes) policies.
