#!/usr/bin/env python3
"""Technology profiles for project wayfinder issues and documentation."""

BASE = 'https://github.com/liberusoftware/documentation/blob/main/'

# suffix -> (presentation_layer_dir, label, profile)
LAYERS = {
    'laravel-inertia-react': (
        'react',
        'Laravel Inertia React',
        {
            'boilerplate': 'https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react',
            'api_client': False,
            'boundary': (
                'Laravel routes, sessions and CSRF own mutations; page components receive '
                'allowlisted Inertia props. A separate HTTP API is optional for these pages.'
            ),
            'standards': [
                ('Inertia standard', 'standards/INERTIA.md'),
                ('React standard', 'standards/REACT.md'),
                ('Laravel standard', 'standards/LARAVEL.md'),
                ('Themes', 'standards/THEMES.md'),
            ],
            'guides': [
                ('Foundation and presentation build', 'guides/presentation/README.md'),
                ('Inertia Vue/React implementation runbook', 'guides/presentation/INERTIA.md'),
                ('React package build and npm release', 'guides/presentation/PACKAGES.md'),
            ],
            'module_index': 'modules/react/README.md',
            'adapter_pattern': 'module-{capability}-react-inertia',
            'method': [
                'Clone or open this host from the matching Boilerplate template; install from committed Composer and npm lockfiles; configure local `.env`; run migrations and the host test suite before feature work.',
                'Confirm Inertia 3 middleware is registered once on the `web` group; share only minimal actor, workspace and navigation props—never full models, tokens or secrets.',
                'Install or verify React 19.2 + `@inertiajs/react` + Vite; keep `private: true`, typecheck and build scripts; commit lockfile changes with dependency review.',
                'Resolve pages explicitly under `resources/js/Pages`; keep layouts, navigation and session composition application-owned.',
                'For each capability: read `core/`, `api/` (if used) and `react/` plans plus SOURCE-MAPPING.md; identify the exact Composer/npm identities before requiring packages.',
                'Deliver one vertical journey (auth context → authorized read → command → authoritative result) with loading/empty/denied/validation/conflict states and accessibility.',
                'Prefer public application actions from domain modules; if an HTTP adapter is used inside the host, treat it as an internal transport—do not invent endpoints to match screens.',
                'Keep installed `/modules` and `/themes` tracked in the host; bump source releases and lockfiles together; never fork domain rules into React.',
                'Prove evidence: feature/browser tests for the journey, policy/tenant denial, CSRF/session behavior, SSR/hydration if enabled, clean `composer install` + `npm ci` + production build.',
            ],
            'spec': '''### Host ownership
- This repository is a Laravel application composition root with React pages over Inertia 3.
- Domain modules own persistence, policies, transitions and jobs; React owns UI state, forms and presentation mapping only.
- Routes, middleware, authorization, validation, redirects and shared props remain Laravel-owned.

### Transport and session
- Mutations use Laravel session + CSRF; Inertia form/visit semantics apply (`Link`, `router`, partial reloads, deferred props).
- Controllers invoke authorized public actions/queries and return props or redirects—not ad-hoc REST JSON unless a deliberate API surface exists.
- Preserve correlation IDs, idempotency keys, pagination and concurrency/revision headers where the contract defines them.

### Package and directory contracts
- Reusable adapters follow `{adapter}` and export pages/components without global discovery collisions.
- Application owns `resources/js` boot, Blade root template, Vite entry, navigation and deployment.
- Themes supply tokens/appearance via the theme policy; do not hard-code a second design system.

### Security and tenancy
- Re-check authorization and Team/Store (or tenant) context server-side on every mutation and sensitive query.
- Allowlist page props; exclude private fields from shared/public caches and SSR payloads.
- Revision conflicts and duplicate submits must be visible and recoverable without silent overwrite.

### Verification and release
- Independent domain/adapter tests plus at least one host journey; follow the coverage policy and evidence standard.
- Release with locked installs, reviewed dependency diffs, operational signals and upgrade/rollback notes.''',
        },
    ),
    'laravel-inertia-vue': (
        'vue',
        'Laravel Inertia Vue',
        {
            'boilerplate': 'https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue',
            'api_client': False,
            'boundary': (
                'Laravel routes, sessions and CSRF own mutations; page components receive '
                'allowlisted Inertia props. A separate HTTP API is optional for these pages.'
            ),
            'standards': [
                ('Inertia standard', 'standards/INERTIA.md'),
                ('Vue standard', 'standards/VUE.md'),
                ('Laravel standard', 'standards/LARAVEL.md'),
                ('Themes', 'standards/THEMES.md'),
            ],
            'guides': [
                ('Foundation and presentation build', 'guides/presentation/README.md'),
                ('Inertia Vue/React implementation runbook', 'guides/presentation/INERTIA.md'),
                ('Vue package build and npm release', 'guides/presentation/PACKAGES.md'),
            ],
            'module_index': 'modules/vue/README.md',
            'adapter_pattern': 'module-{capability}-vue-inertia',
            'method': [
                'Clone or open this host from the matching Boilerplate template; install from committed Composer and npm lockfiles; configure local `.env`; run migrations and the host test suite before feature work.',
                'Confirm Inertia 3 middleware is registered once on the `web` group; share only minimal actor, workspace and navigation props—never full models, tokens or secrets.',
                'Install or verify Vue 3 + `@inertiajs/vue3` + Vite; keep `private: true`, `vue-tsc` typecheck and build scripts; commit lockfile changes with dependency review.',
                'Resolve pages explicitly under `resources/js/Pages`; keep layouts, navigation and session composition application-owned.',
                'For each capability: read `core/`, `api/` (if used) and `vue/` plans plus SOURCE-MAPPING.md; identify the exact Composer/npm identities before requiring packages.',
                'Deliver one vertical journey (auth context → authorized read → command → authoritative result) with loading/empty/denied/validation/conflict states and accessibility.',
                'Prefer public application actions from domain modules; if an HTTP adapter is used inside the host, treat it as an internal transport—do not invent endpoints to match screens.',
                'Keep installed `/modules` and `/themes` tracked in the host; bump source releases and lockfiles together; never fork domain rules into Vue.',
                'Prove evidence: feature/browser tests for the journey, policy/tenant denial, CSRF/session behavior, SSR/hydration if enabled, clean `composer install` + `npm ci` + production build.',
            ],
            'spec': '''### Host ownership
- This repository is a Laravel application composition root with Vue SFCs over Inertia 3.
- Domain modules own persistence, policies, transitions and jobs; Vue owns UI state, forms and presentation mapping only.
- Routes, middleware, authorization, validation, redirects and shared props remain Laravel-owned.

### Transport and session
- Mutations use Laravel session + CSRF; Inertia form/visit semantics apply (`Link`, `router`, partial reloads, deferred props).
- Controllers invoke authorized public actions/queries and return props or redirects—not ad-hoc REST JSON unless a deliberate API surface exists.
- Preserve correlation IDs, idempotency keys, pagination and concurrency/revision headers where the contract defines them.

### Package and directory contracts
- Reusable adapters follow `{adapter}` and export pages/components without global discovery collisions.
- Application owns `resources/js` boot, Blade root template, Vite entry, navigation and deployment.
- Themes supply tokens/appearance via the theme policy; do not hard-code a second design system.

### Security and tenancy
- Re-check authorization and Team/Store (or tenant) context server-side on every mutation and sensitive query.
- Allowlist page props; exclude private fields from shared/public caches and SSR payloads.
- Revision conflicts and duplicate submits must be visible and recoverable without silent overwrite.

### Verification and release
- Independent domain/adapter tests plus at least one host journey; follow the coverage policy and evidence standard.
- Release with locked installs, reviewed dependency diffs, operational signals and upgrade/rollback notes.''',
        },
    ),
    'nuxt-vue': (
        'nuxt',
        'Nuxt Vue',
        {
            'boilerplate': 'https://github.com/liberusoftware/project-boilerplate-nuxt-vue',
            'api_client': True,
            'boundary': (
                'Consume the product `-laravel-api` HTTP contracts from an independently deployed Nuxt 4 Vue app; '
                'isolate authenticated SSR caches and hydration by actor and tenant.'
            ),
            'standards': [
                ('Nuxt standard', 'standards/NUXT.md'),
                ('Vue standard', 'standards/VUE.md'),
                ('API architecture', 'architecture/API.md'),
                ('Laravel API backends', 'guides/LARAVEL-API-BACKENDS.md'),
            ],
            'guides': [
                ('Foundation and presentation build', 'guides/presentation/README.md'),
                ('Nuxt implementation runbook', 'guides/presentation/NUXT.md'),
                ('Package build and npm release', 'guides/presentation/PACKAGES.md'),
            ],
            'module_index': 'modules/nuxt/README.md',
            'adapter_pattern': 'module-{capability}-nuxt',
            'method': [
                'Start from the Nuxt Vue Boilerplate (or this product skeleton); `npm ci` from the lockfile; pin Node from `.node-version`; run typecheck/build before feature work.',
                'Configure runtime `apiBase` (server-side) to the matching `project-{product}-laravel-api` origin; never accept arbitrary upstream URLs from the browser; keep credentials out of `runtimeConfig.public`.',
                'Establish auth/session integration for the deployment (cookie/BFF or token) with CSRF/origin rules; Laravel remains authoritative for policy and tenancy.',
                'Generate or validate DTOs against the published OpenAPI/schema; map only allowlisted fields; preserve pagination, errors, conflicts and pending-operation semantics.',
                'Own `app/pages`, layouts and middleware in the application; import reusable Nuxt/Vue adapters explicitly—packages must not install silent global routes.',
                'For SSR: scope fetches and caches to authenticated actor + tenant; default authenticated reads to private/`no-store` until a reviewed cache policy exists.',
                'Implement one vertical journey with loading/empty/denied/validation/conflict/retry states; use deliberate BFF handlers only when the boundary is documented.',
                'Expand capability-by-capability using `nuxt/` plans, SOURCE-MAPPING.md and reviewed package identities; do not invent endpoints for UI convenience.',
                'Prove evidence: contract tests or typed client checks, SSR cache isolation, cross-tenant denial, clean install/build, and deployment env validation.',
            ],
            'spec': '''### Host ownership
- This repository is an independently deployed Nuxt 4 + Vue 3 client. It is not an Inertia host and does not own domain persistence.
- The matching `project-{product}-laravel-api` composes domain + API adapters and publishes the versioned HTTP contract.
- Application owns routes, layouts, runtime config, BFF handlers (if any) and deployment; adapters own capability UI and transport mapping.

### Transport and session
- All product data access uses reviewed HTTP contracts; configure a fixed API base URL per environment.
- Browser cookie sessions require explicit origin, CSRF and cookie-domain design across Nuxt and Laravel hosts.
- Forward only approved credentials/headers; never proxy arbitrary user-selected upstreams.

### Package and directory contracts
- Reusable adapters follow `{adapter}`; share DTOs that mirror the public API—never PHP models.
- Keep capability UI importable; avoid global singleton stores that leak per-user SSR state across requests.
- Themes/tokens remain technology-neutral where shared; Nuxt applies them in application layout.

### Security and tenancy
- Authorize every server handler and rely on Laravel re-authorization for every API call.
- Isolate SSR payloads and caches by actor and tenant; never cache private data under a public URL key alone.
- Map 401/403/409/422/429 distinctly; support idempotent retries and revision conflicts per contract.

### Verification and release
- Verify SSR hydration safety, cache isolation, secret exclusion from client bundles and one full host journey.
- Deploy API-compatible contract versions before dependent clients; monitor auth failures and upstream errors.''',
        },
    ),
    'next-react': (
        'nextjs',
        'Next.js React',
        {
            'boilerplate': 'https://github.com/liberusoftware/project-boilerplate-next-react',
            'api_client': True,
            'boundary': (
                'Consume the product `-laravel-api` HTTP contracts from an independently deployed Next.js App Router app; '
                'specify server/client ownership, private caching and mutation invalidation.'
            ),
            'standards': [
                ('Next.js standard', 'standards/NEXTJS.md'),
                ('React standard', 'standards/REACT.md'),
                ('API architecture', 'architecture/API.md'),
                ('Laravel API backends', 'guides/LARAVEL-API-BACKENDS.md'),
            ],
            'guides': [
                ('Foundation and presentation build', 'guides/presentation/README.md'),
                ('Next.js implementation runbook', 'guides/presentation/NEXTJS.md'),
                ('Package build and npm release', 'guides/presentation/PACKAGES.md'),
            ],
            'module_index': 'modules/nextjs/README.md',
            'adapter_pattern': 'module-{capability}-nextjs',
            'method': [
                'Start from the Next.js React Boilerplate (or this product skeleton); `npm ci`; use `.node-version`; run lint, typecheck and production build before feature work.',
                'Set `API_BASE_URL` (server-only) to the matching `project-{product}-laravel-api` origin; never put credentials in `NEXT_PUBLIC_*`; mark secret-bearing modules with `server-only`.',
                'Choose and document session integration (server cookies/BFF vs token); Laravel re-authorizes every API request; Next entry points authenticate and authorize their own handlers/actions.',
                'Validate/generate DTOs from the published schema; copy allowlisted fields only; preserve pagination, error shapes, conflicts and job/pending semantics.',
                'Own `src/app` routes, layouts, `loading.tsx`/`error.tsx` and deployment; import capability adapters explicitly—no silent global route injection from packages.',
                'Default authenticated fetches to `cache: \'no-store\'` (or equivalent) until a tenant-aware cache policy is reviewed; invalidate after confirmed mutations.',
                'Implement one vertical journey with accessible loading/empty/denied/validation/conflict/retry states; keep write authority in Laravel even when a server action is the browser transport.',
                'Expand using `nextjs/` plans and SOURCE-MAPPING.md; coordinate contract changes in the API/domain owners—not by forking rules into React.',
                'Prove evidence: server/client boundary checks, secret exclusion from bundles, cross-tenant denial, clean install/build and preview/production env separation.',
            ],
            'spec': '''### Host ownership
- This repository is an independently deployed Next.js (App Router) + React client. It does not use Inertia and does not own domain persistence.
- The matching `project-{product}-laravel-api` owns authorization, tenancy, business rules and the versioned OpenAPI contract.
- Application owns `app/` routes, middleware/proxy, environment, deployment and auth integration; adapters own capability UI and typed API helpers.

### Transport and session
- Server components/route handlers call a fixed configured Laravel origin with approved credentials only.
- Cookie authentication needs explicit CSRF, origin, cookie-domain and SameSite design for the real deployment topology.
- Commands use documented operations and idempotency/version headers; show conflicts without overwriting newer data.

### Package and directory contracts
- Reusable adapters follow `{adapter}` with separate client-safe and server-only exports.
- Do not barrel-export server clients into client components; keep ORM/PHP types out of JavaScript packages.
- Shared presentational packages must not import `next/navigation` or Inertia APIs—inject navigation/mutation callbacks.

### Security and tenancy
- Treat every server action/route handler as a public entry point: authenticate, validate, authorize.
- Cache keys must include tenant and permission-sensitive dimensions when caching is enabled.
- Never serialize service credentials or private fields into RSC payloads or client bundles.

### Verification and release
- Test cross-tenant denial, cache isolation, expired sessions, duplicate commands and rollback after API failure.
- Deploy compatible API changes first; roll back frontend artifacts without reversing database migrations.''',
        },
    ),
    'mobile-react': (
        'react-native',
        'React Native Expo',
        {
            'boilerplate': 'https://github.com/liberusoftware/project-boilerplate-mobile-react',
            'api_client': True,
            'boundary': (
                'Consume the product `-laravel-api` with typed clients, secure device credentials, validated deep links, '
                'native accessibility, foreground refresh and explicit offline/reconnect behavior.'
            ),
            'standards': [
                ('React Native standard', 'standards/REACT-NATIVE.md'),
                ('Mobile architecture', 'architecture/MOBILE.md'),
                ('Mobile standard', 'standards/MOBILE.md'),
                ('Laravel API backends', 'guides/LARAVEL-API-BACKENDS.md'),
            ],
            'guides': [
                ('Foundation and presentation build', 'guides/presentation/README.md'),
                ('React Native / Expo implementation runbook', 'guides/presentation/REACT-NATIVE.md'),
            ],
            'module_index': 'modules/react-native/README.md',
            'adapter_pattern': 'module-{capability}-react-native',
            'method': [
                'Start from the React Native Expo Boilerplate; install with the Expo-compatible toolchain; run `expo-doctor`, typecheck and a development build—do not assume Expo Go covers every native module.',
                'Record supported iOS/Android versions, orientations and accessibility requirements; configure bundle IDs, scheme, icons and permissions for this product host.',
                'Point the app at the matching `project-{product}-laravel-api` base URL (public config only); implement the reviewed mobile auth contract (PKCE/OAuth or first-party tokens)—never embed confidential secrets.',
                'Store refresh/session secrets in Keychain/Keystore-backed SecureStore; keep short-lived access tokens in memory where feasible; single-flight refresh; logout revokes and clears scoped caches/queues.',
                'Inject typed API clients per session/workspace; validate every response field; map status codes to typed outcomes; abort in-flight work on context change.',
                'Build native screens (not compressed desktop tables): safe areas, touch targets, screen-reader labels, platform back behavior, deep-link validation.',
                'Define explicit offline/queue/reconciliation rules before enabling draft writes; never present a local draft as an authoritative completed server transaction.',
                'Deliver one vertical journey end-to-end on simulator and at least one physical-platform path; then expand via `react-native/` plans and SOURCE-MAPPING.md.',
                'Prove evidence: auth lifecycle, 401 refresh bounds, tenant denial, connectivity loss/resume, signed build pipeline notes and clean lockfile installs.',
            ],
            'spec': '''### Host ownership
- This repository is a native iOS/Android client (React Native + Expo). It consumes HTTP APIs; it does not run Laravel or own domain tables.
- Application owns navigation, session providers, secure storage adapters, native permissions and store release configuration.
- Reusable adapters supply screens/hooks/DTO mapping for a capability without importing Next.js, DOM or Inertia.

### Transport and session
- Fixed API base URL per environment; HTTPS in production; reachable host for device/emulator networking.
- Use the API’s mobile identity contract; Authorization Code + PKCE for public OAuth clients when applicable.
- Bound timeouts, cancellation and retry; preserve idempotency keys for commands that require them.

### Package and directory contracts
- Prefer `{adapter}` (or the layer’s documented identity) with Metro-compatible exports.
- Keep session/transport/cache as app-injected dependencies; avoid singletons that retain a previous user’s token.
- `EXPO_PUBLIC_*` values are embedded public configuration—never secrets.

### Security and tenancy
- Server remains authoritative for authorization and tenancy; hide unavailable actions for UX only.
- Deep links must be validated (signed routes/state) before acting on them.
- Scoped local caches must clear on logout and workspace/permission changes.

### Verification and release
- Verify on both OS families where the product supports them; record signed build/store evidence separately from unit tests.
- Monitor token refresh failures, crash-free sessions and API error rates after release.''',
        },
    ),
    'mobile-flutter': (
        'flutter',
        'Flutter mobile',
        {
            'boilerplate': 'https://github.com/liberusoftware/project-boilerplate-mobile-flutter',
            'api_client': True,
            'boundary': (
                'Consume the product `-laravel-api` with typed Dart clients, secure device credentials, native widget '
                'semantics, account-isolated drafts and lifecycle/reconnect handling.'
            ),
            'standards': [
                ('Flutter standard', 'standards/FLUTTER.md'),
                ('Mobile architecture', 'architecture/MOBILE.md'),
                ('Mobile standard', 'standards/MOBILE.md'),
                ('Laravel API backends', 'guides/LARAVEL-API-BACKENDS.md'),
            ],
            'guides': [
                ('Foundation and presentation build', 'guides/presentation/README.md'),
                ('Flutter implementation runbook', 'guides/presentation/FLUTTER.md'),
            ],
            'module_index': 'modules/flutter/README.md',
            'adapter_pattern': 'module-{capability}-flutter',
            'method': [
                'Start from the Flutter mobile Boilerplate; use the pinned Flutter/Dart toolchain; `flutter pub get`, `analyze`, `test`, then run on a listed device.',
                'Replace skeleton application IDs/display names/signing with product-owned identifiers; keep `publish_to: none` and commit `pubspec.lock`.',
                'Configure the API base (for example `--dart-define`) to `project-{product}-laravel-api`; treat that value as public configuration, not a secret store.',
                'Implement reviewed mobile auth; store long-lived secrets in platform-secure storage; coordinate refresh in one place; clear credentials and scoped caches on logout.',
                'Separate `data`/`presentation`/`contracts`; inject repositories; widgets emit intent and render state—they do not authorize or open database connections.',
                'Validate JSON into checked DTOs; preserve pagination and error mapping; document real HTTP cancellation behavior (future timeouts alone are insufficient).',
                'Build mobile layouts with semantics, safe areas and platform navigation; define offline/draft reconciliation explicitly before enabling queued writes.',
                'Ship one vertical journey with tests and device evidence; expand using `flutter/` plans and SOURCE-MAPPING.md without duplicating domain rules.',
                'Prove evidence: analyze/test, auth lifecycle, tenant denial, background/resume, and signed `appbundle`/`ipa` build notes for release candidates.',
            ],
            'spec': '''### Host ownership
- This repository is the general Flutter mobile foundation for the product. Domain ownership stays in Laravel modules and the product API host.
- Application owns composition, routes, environment and platform projects; packages own reusable widgets and DTO mapping.
- Do not copy desktop/web layouts; implement native mobile information architecture.

### Transport and session
- Typed Dart HTTP (or approved client) against reviewed OpenAPI operations.
- Secure credential storage and bounded refresh; reauthenticate when refresh fails.
- Local drafts are non-authoritative until the server confirms the transition.

### Package and directory contracts
- Capability packages use Dart/pub (`{adapter}` or documented identity) with explicit supported platforms.
- Path dependencies are for temporary integration only; releases use reviewed hosted/Git versions.
- Avoid adding `package.json` to represent Dart packages.

### Security and tenancy
- Every API call carries the established actor/workspace context required by the contract.
- Isolate caches and draft queues per account/workspace; purge on logout.
- Validate deep links and permission-gated platform features before use.

### Verification and release
- `flutter analyze` and widget tests are necessary but not sufficient—record device and signed-build evidence.
- Support both iOS and Android acceptance for products that ship both stores.''',
        },
    ),
    'dart-mobile': (
        'flutter',
        'Dart mobile',
        {
            'boilerplate': 'https://github.com/liberusoftware/project-boilerplate-dart-mobile',
            'api_client': True,
            'boundary': (
                'A distinct mobile host/release using Flutter/Dart and the product `-laravel-api`; verify touch navigation, '
                'platform lifecycle, secure local state and signed iOS/Android delivery independently of `-mobile-flutter`.'
            ),
            'standards': [
                ('Flutter standard', 'standards/FLUTTER.md'),
                ('Mobile architecture', 'architecture/MOBILE.md'),
                ('Dart presentation guide', 'guides/presentation/DART.md'),
                ('Laravel API backends', 'guides/LARAVEL-API-BACKENDS.md'),
            ],
            'guides': [
                ('Foundation and presentation build', 'guides/presentation/README.md'),
                ('Dart mobile/desktop initialization', 'guides/presentation/DART.md'),
                ('Flutter implementation runbook', 'guides/presentation/FLUTTER.md'),
            ],
            'module_index': 'modules/flutter/README.md',
            'adapter_pattern': 'module-{capability}-flutter',
            'method': [
                'Treat this repository as a separate mobile application root from `-mobile-flutter`: independent release identity, bundle IDs and store listing.',
                'Use the Flutter/Dart versions pinned in `.flutter-version` / `.fvmrc`; `flutter pub get`, `analyze`, `test`, then run on iOS/Android targets.',
                'Consume `project-{product}-laravel-api` with typed clients and secure storage; reuse Flutter-layer plans for widgets/clients while keeping host-specific acceptance mandatory.',
                'Inject session/transport at composition; keep policy and persistence on the server; validate DTOs and error maps against the published contract.',
                'Verify touch navigation, safe areas, permissions, deep links, background/resume, logout clearing and offline reconciliation on both OS families.',
                'Implement one vertical journey before expanding checklist items; link child issues when ownership and acceptance are actionable.',
                'Build signed artifacts (`appbundle`/`ipa`) with reviewed signing config; record store-oriented evidence separately from unit tests.',
                'Keep reusable Dart/Flutter modules in their own pubspecs; replace path dependencies before release.',
                'Prove clean installs from locks and compatibility with the supported API contract versions.',
            ],
            'spec': '''### Host ownership
- `-dart-mobile` is a dedicated mobile product host. Shared Flutter module plans inform widgets/clients; this host still proves its own navigation, storage and release.
- Laravel API backend remains authoritative for domain rules; this app is an API consumer only.

### Transport and session
- Same HTTP contract family as other independent clients; configure API base per environment.
- Platform-secure credentials; explicit reconnect and refresh behavior; no embedded confidential client secrets.

### Package and directory contracts
- Application `publish_to: none`; reusable modules via Dart/pub with declared platforms.
- Flutter supplies the native mobile host (rendering, accessibility, plugins)—not a console-only Dart app.

### Security and tenancy
- Account-isolated local state; purge on logout; validate deep links.
- Never present queued local writes as completed server transactions.

### Verification and release
- Dual-OS mobile acceptance; signed build evidence; API compatibility window documented in the host README.''',
        },
    ),
    'dart-desktop': (
        'flutter',
        'Dart desktop',
        {
            'boilerplate': 'https://github.com/liberusoftware/project-boilerplate-dart-desktop',
            'api_client': True,
            'boundary': (
                'A distinct desktop host/release using Flutter/Dart and the product `-laravel-api`; verify keyboard/focus, '
                'resizing, multi-window consistency, platform storage and safe printing/export independently.'
            ),
            'standards': [
                ('Flutter standard', 'standards/FLUTTER.md'),
                ('Dart presentation guide', 'guides/presentation/DART.md'),
                ('API architecture', 'architecture/API.md'),
                ('Laravel API backends', 'guides/LARAVEL-API-BACKENDS.md'),
            ],
            'guides': [
                ('Foundation and presentation build', 'guides/presentation/README.md'),
                ('Dart mobile/desktop initialization', 'guides/presentation/DART.md'),
                ('Flutter implementation runbook', 'guides/presentation/FLUTTER.md'),
            ],
            'module_index': 'modules/flutter/README.md',
            'adapter_pattern': 'module-{capability}-flutter',
            'method': [
                'Treat this repository as a separate desktop application root: independent release identity and OS packaging from mobile hosts.',
                'Use the pinned Flutter/Dart toolchain; enable Linux/macOS/Windows targets as product support requires; `flutter pub get`, `analyze`, `test`.',
                'Point desktop builds at `project-{product}-laravel-api`; implement desktop-safe credential storage and session lifecycle for the threat model.',
                'Design for keyboard navigation, focus order, resizing, window close/reopen and optional multi-window concurrency without corrupting drafts.',
                'Inject typed API repositories; validate DTOs; keep domain authority on the server; define print/export as authorized, audience-safe operations.',
                'Deliver one vertical journey with desktop interaction evidence; expand via Flutter-layer plans and SOURCE-MAPPING.md.',
                'Build native artifacts (`flutter build linux|macos|windows`) on the matching OS tooling; record installer/notarization requirements separately.',
                'Replace path dependencies with reviewed module versions before release; keep `publish_to: none` on the application pubspec.',
                'Prove clean lock installs, API compatibility and operational recovery notes for desktop deployments.',
            ],
            'spec': '''### Host ownership
- `-dart-desktop` is a dedicated desktop product host using Flutter for windowing/rendering. It consumes the product Laravel API.
- Desktop UX requirements (keyboard, focus, windowing, printing/export) are mandatory acceptance—even when sharing Flutter module plans with mobile.

### Transport and session
- Reviewed HTTP contracts; environment-specific API base; secure local credential storage appropriate to desktop OS.
- Handle connectivity loss without implying server success for local-only state.

### Package and directory contracts
- Application owns platform runners and packaging; reusable UI/contracts are Dart/pub modules with desktop platform support declared.
- Do not assume mobile plugins work on desktop—review each dependency’s platforms.

### Security and tenancy
- Authorize exports/prints/files access; avoid writing private data to shared desktop paths without scoping.
- Clear session-scoped caches on logout; protect local drafts per account.

### Verification and release
- Verify keyboard/focus/resize/window lifecycle on each supported OS; signed/notarized installers as required by the distribution channel.
- Unit/widget tests do not replace native desktop build verification.''',
        },
    ),
}


def link(path: str) -> str:
    return f'{BASE}{path}'


def render_wayfinder_doc(suffix: str) -> str:
    layer, label, profile = LAYERS[suffix]
    lines = [
        f'# Wayfinder technical specification: {label}',
        '',
        f'This is the technology-specific implementation specification for `{suffix}` project hosts. '
        'Product wayfinder issues embed the method and a condensed form of this specification, and link here for the durable reference.',
        '',
        f'- Boilerplate template: {profile["boilerplate"]}',
        f'- Presentation layer directory in product docs: `{layer}/`',
        f'- Adapter identity pattern: `{profile["adapter_pattern"]}`',
        f'- Consumes product `-laravel-api`: {"yes" if profile["api_client"] else "no (Laravel/Inertia host; HTTP API optional)"}',
        '',
        '## Delivery boundary',
        '',
        profile['boundary'],
        '',
        '## Authoritative documentation',
        '',
    ]
    for title, path in profile['standards'] + profile['guides']:
        lines.append(f'- [{title}](../../{path})')
    lines += [
        f'- [Module index](../../{profile["module_index"]})',
        '- [Implementation evidence](../../standards/IMPLEMENTATION-EVIDENCE.md)',
        '- [Testing / coverage policy](../../standards/TESTING.md)',
        '',
        '## Robust implementation method',
        '',
    ]
    for i, step in enumerate(profile['method'], 1):
        lines.append(f'{i}. {step}')
    lines += [
        '',
        '## Technical specification',
        '',
        profile['spec'].replace('{adapter}', profile['adapter_pattern']),
        '',
        '## Related',
        '',
        '- [Implementation wayfinders guide](../IMPLEMENTATION-WAYFINDERS.md)',
        '- [Issue matrix](../IMPLEMENTATION-ISSUES.md)',
        '- [Repository map](../REPOSITORIES.md)',
        '',
    ]
    return '\n'.join(lines)


def write_wayfinder_docs(root):
    out = root / 'projects' / 'wayfinders'
    out.mkdir(parents=True, exist_ok=True)
    index = [
        '# Technology wayfinder specifications',
        '',
        'Each non-Filament project host has a GitHub wayfinder issue. These pages are the durable, technology-specific '
        'implementation method and technical specification those issues follow. Product capability checklists remain in the issues; '
        'framework depth lives in standards and presentation runbooks linked from each page.',
        '',
        '| Technology | Specification | Boilerplate |',
        '| --- | --- | --- |',
    ]
    for suffix, (_, label, profile) in LAYERS.items():
        path = out / f'{suffix}.md'
        path.write_text(render_wayfinder_doc(suffix))
        index.append(
            f'| {label} | [{suffix}.md]({suffix}.md) | [template]({profile["boilerplate"]}) |'
        )
    index += [
        '',
        'Filament programmes and `-laravel-api` backend hosts are outside the general wayfinder publisher; see '
        '[IMPLEMENTATION-WAYFINDERS.md](../IMPLEMENTATION-WAYFINDERS.md) and [LARAVEL-API-BACKENDS.md](../../guides/LARAVEL-API-BACKENDS.md).',
        '',
    ]
    (out / 'README.md').write_text('\n'.join(index))
