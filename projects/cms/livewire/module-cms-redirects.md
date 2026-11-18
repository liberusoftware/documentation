# CMS: Module Cms Redirects Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-redirects). Observed identity: [`liberusoftware/module-cms-redirects-livewire`](../../../modules/source/liberusoftware--module-cms-redirects-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-redirects-livewire`  
**Matching domain module:** `module-cms-redirects`  
**Application:** CMS  
**Source feature:** [Module Cms Redirects](../features/module-cms-redirects.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Redirect records:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Imports:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Automatic slug-change redirects:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Chains/loops:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Hit counts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Expiry:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **404 suggestions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-redirects-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsRedirects::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `redirect-records`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `imports`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `automatic-slug-change-redirects`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `chains-loops`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `hit-counts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `expiry`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `404-suggestions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-redirects` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-redirects.md) · [API plan](../api/module-cms-redirects.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Redirect records** | Expose a focused Livewire 4 component and namespaced Blade default view for `redirect records` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Imports** | Expose a focused Livewire 4 component and namespaced Blade default view for `imports` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Automatic slug-change redirects** | Expose a focused Livewire 4 component and namespaced Blade default view for `automatic slug-change redirects` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Chains/loops** | Expose a focused Livewire 4 component and namespaced Blade default view for `chains/loops` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Hit counts** | Expose a focused Livewire 4 component and namespaced Blade default view for `hit counts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Expiry** | Expose a focused Livewire 4 component and namespaced Blade default view for `expiry` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **404 suggestions** | Expose a focused Livewire 4 component and namespaced Blade default view for `404 suggestions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [RedirectLookup.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-redirects-livewire/src/Livewire/RedirectLookup.php) · [RedirectsLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-redirects-livewire/src/RedirectsLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RedirectService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-redirects/src/Services/RedirectService.php) | `public function create(string $from, string $to, int $statusCode = 301, ?string $source = null, ?int $teamId = null): Redirect`<br>`public function resolve(string $path, int $maxHops = 10, ?int $teamId = null): array`<br>`public function import(iterable $rows, ?int $teamId = null): int`<br>`public function recordSlugChange(string $oldPath, string $newPath, ?int $teamId = null): Redirect`<br>`public function suggestions(string $missingPath, int $limit = 5, ?int $teamId = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Redirect.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-redirects/src/Models/Redirect.php) | `from_path`, `to_path`, `status_code`, `hit_count`, `expires_at`, `active`, `source`, `team_id` |
<!-- layer-implementation-plan:end -->
