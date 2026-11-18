# CMS: Module Cms Theme Integration Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-theme-integration). Observed identity: [`liberusoftware/module-cms-theme-integration-livewire`](../../../modules/source/liberusoftware--module-cms-theme-integration-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-theme-integration-livewire`  
**Matching domain module:** `module-cms-theme-integration`  
**Application:** CMS  
**Source feature:** [Module Cms Theme Integration](../features/module-cms-theme-integration.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Theme selection by site/channel:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Regions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **View contracts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Component registry:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Inheritance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Preview:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Safe fallback:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-theme-integration-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsThemeIntegration::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `theme-selection-by-site-channel`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `regions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `view-contracts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `component-registry`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `inheritance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `preview`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `safe-fallback`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-theme-integration` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-theme-integration.md) · [API plan](../api/module-cms-theme-integration.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Theme selection by site/channel** | Expose a focused Livewire 4 component and namespaced Blade default view for `theme selection by site/channel` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Regions** | Expose a focused Livewire 4 component and namespaced Blade default view for `regions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **View contracts** | Expose a focused Livewire 4 component and namespaced Blade default view for `view contracts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Component registry** | Expose a focused Livewire 4 component and namespaced Blade default view for `component registry` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Inheritance** | Expose a focused Livewire 4 component and namespaced Blade default view for `inheritance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Preview** | Expose a focused Livewire 4 component and namespaced Blade default view for `preview` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Safe fallback** | Expose a focused Livewire 4 component and namespaced Blade default view for `safe fallback` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ThemePreview.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-theme-integration-livewire/src/Livewire/ThemePreview.php) · [ThemeIntegrationLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-theme-integration-livewire/src/ThemeIntegrationLivewireServiceProvider.php).

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
