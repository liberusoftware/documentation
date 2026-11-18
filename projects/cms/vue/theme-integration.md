# CMS: Theme Integration Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#theme-integration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-cms-theme-integration-vue-inertia`
**Matching domain module:** `cms-theme-integration`
**Application:** CMS
**Source feature:** [Theme Integration](../features/theme-integration.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/theme-integration.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Theme selection by site/channel:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Regions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **View contracts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Component registry:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Inheritance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Preview:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Safe fallback:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-cms-theme-integration-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `theme-selection-by-site-channel`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `regions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `view-contracts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `component-registry`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `inheritance`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `preview`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `safe-fallback`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `cms-theme-integration` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-cms-laravel-inertia-vue`](https://github.com/liberusoftware/project-cms-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-cms-theme-integration-vue-inertia`](https://github.com/liberusoftware/module-cms-theme-integration-vue-inertia) (`@liberusoftware/module-cms-theme-integration-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/theme-integration.md) · [Core plan](../core/theme-integration.md) · [API plan](../api/theme-integration.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Theme selection by site/channel** | Render `theme selection by site/channel` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Regions** | Render `regions` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **View contracts** | Render `view contracts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Component registry** | Render `component registry` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Inheritance** | Render `inheritance` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Preview** | Render `preview` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Safe fallback** | Render `safe fallback` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ThemeIntegrationQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Queries/ThemeIntegrationQuery.php) | `public function __construct(private TenantContextInterface $tenant)`<br>`public function bindings(int $perPage = 15, ?int $teamId = null): LengthAwarePaginator`<br>`public function binding(string $siteKey, ?string $channelKey = null, ?int $teamId = null): ?ThemeBinding`<br>`public function bindingById(int\|string $id, ?int $teamId = null): ?ThemeBinding`<br>`public function components(string $themeKey, ?string $region = null, ?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ThemeIntegrationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Services/ThemeIntegrationService.php) | `public function __construct(private ThemeIntegrationQuery $query)`<br>`public function bind(string $siteKey, ?string $channelKey, string $themeKey, string $fallbackThemeKey = 'default', ?int $teamId = null): ThemeBinding`<br>`public function updateBinding(ThemeBinding $binding, array $attributes): ThemeBinding`<br>`public function removeBinding(ThemeBinding $binding): void`<br>`public function select(?string $siteKey, ?string $channelKey = null, ?int $teamId = null): ?ThemeBinding`<br>`public function effectiveTheme(?string $siteKey, ?string $channelKey = null, ?int $teamId = null): string`<br>`public function registerComponent(string $themeKey, string $region, string $componentKey, array $viewContract = [], array $configuration = [], ?int $teamId = null): ThemeComponent`<br>`public function components(string $themeKey, ?string $region = null, ?int $teamId = null): array`<br>`public function previewToken(ThemeBinding $binding): string`<br>`public function preview(ThemeBinding $binding, string $token): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ThemeBinding.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Models/ThemeBinding.php) | `site_key`, `channel_key`, `theme_key`, `fallback_theme_key`, `preview_token`, `preview_expires_at`, `active`, `team_id` |
| [ThemeComponent.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Models/ThemeComponent.php) | `theme_key`, `region`, `component_key`, `view_contract`, `configuration`, `team_id` |
<!-- layer-implementation-plan:end -->
