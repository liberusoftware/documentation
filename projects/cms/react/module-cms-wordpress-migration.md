# CMS: Module Cms Wordpress Migration React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-wordpress-migration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-cms-module-cms-wordpress-migration-react-inertia`
**Matching domain module:** `module-cms-wordpress-migration`
**Application:** CMS
**Source feature:** [Module Cms Wordpress Migration](../features/module-cms-wordpress-migration.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-cms-wordpress-migration.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Posts/pages/custom types:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Taxonomies:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Metadata:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Users/authors:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Comments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Media:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Menus:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Redirects:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Source identifiers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-cms-module-cms-wordpress-migration-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `posts-pages-custom-types`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `taxonomies`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `metadata`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `users-authors`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `comments`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `media`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `menus`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `redirects`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `source-identifiers`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `module-cms-wordpress-migration` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-cms-laravel-inertia-react`](https://github.com/liberusoftware/project-cms-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-cms-wordpress-migration-react-inertia`](https://github.com/liberusoftware/module-cms-wordpress-migration-react-inertia) (`@liberusoftware/module-cms-wordpress-migration-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/module-cms-wordpress-migration.md) · [Core plan](../core/module-cms-wordpress-migration.md) · [API plan](../api/module-cms-wordpress-migration.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Posts/pages/custom types** | Render `posts/pages/custom types` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Taxonomies** | Render `taxonomies` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Metadata** | Render `metadata` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Users/authors** | Render `users/authors` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Comments** | Render `comments` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Media** | Render `media` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Menus** | Render `menus` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Redirects** | Render `redirects` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Source identifiers** | Render `source identifiers` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [WordPressMigrationQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Queries/WordPressMigrationQuery.php) | `public function __construct(private TenantContextInterface $tenant)`<br>`public function migrations(int $perPage = 15, ?int $teamId = null): LengthAwarePaginator`<br>`public function migration(int\|string $id, ?int $teamId = null): ?WordPressMigration`<br>`public function migrationByPublicId(string $publicId, ?int $teamId = null): ?WordPressMigration`<br>`public function records(WordPressMigration $migration, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [WordPressImporterInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Contracts/WordPressImporterInterface.php) | `public function records(WordPressMigration $migration): iterable` |
| [WordPressMigrationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Services/WordPressMigrationService.php) | `public function start(?string $sourceUrl = null, array $options = [], ?int $teamId = null): WordPressMigration`<br>`public function addRecord(WordPressMigration $migration, string $recordType, string $sourceId, array $payload = [], array $sourceIdentifiers = [], ?string $sourceParentId = null): WordPressMigrationRecord`<br>`public function processRecord(WordPressMigrationRecord $record, bool $success = true, ?string $failureReason = null): WordPressMigrationRecord`<br>`public function complete(WordPressMigration $migration): WordPressMigration`<br>`public function fail(WordPressMigration $migration, string $reason): WordPressMigration` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WordPressMigration.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Models/WordPressMigration.php) | `public_id`, `source_url`, `status`, `total_records`, `processed_records`, `failed_records`, `options`, `metadata`, `failure_reason`, `started_at`, `completed_at`, `team_id` |
| [WordPressMigrationRecord.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-wordpress-migration/src/Models/WordPressMigrationRecord.php) | `migration_id`, `record_type`, `source_id`, `source_parent_id`, `status`, `payload`, `source_identifiers`, `failure_reason`, `processed_at`, `team_id` |
<!-- layer-implementation-plan:end -->
