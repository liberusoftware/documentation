# CMS: Module Cms Web Delivery Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-web-delivery). Observed identity: [`liberusoftware/module-cms-web-delivery-livewire`](../../../modules/source/liberusoftware--module-cms-web-delivery-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-module-cms-web-delivery-livewire`  
**Matching domain module:** `module-cms-web-delivery`  
**Application:** CMS  
**Source feature:** [Module Cms Web Delivery](../features/module-cms-web-delivery.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Canonical route rendering:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Response metadata:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cache tags:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Preview mode:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Redirects:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Errors:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Maintenance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Edge invalidation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-module-cms-web-delivery-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsModuleCmsWebDelivery::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `canonical-route-rendering`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `response-metadata`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cache-tags`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `preview-mode`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `redirects`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `errors`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `maintenance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `edge-invalidation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `module-cms-web-delivery` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/module-cms-web-delivery.md) · [API plan](../api/module-cms-web-delivery.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Canonical route rendering** | Expose a focused Livewire 4 component and namespaced Blade default view for `canonical route rendering` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Response metadata** | Expose a focused Livewire 4 component and namespaced Blade default view for `response metadata` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cache tags** | Expose a focused Livewire 4 component and namespaced Blade default view for `cache tags` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Preview mode** | Expose a focused Livewire 4 component and namespaced Blade default view for `preview mode` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Redirects** | Expose a focused Livewire 4 component and namespaced Blade default view for `redirects` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Errors** | Expose a focused Livewire 4 component and namespaced Blade default view for `errors` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Maintenance** | Expose a focused Livewire 4 component and namespaced Blade default view for `maintenance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Edge invalidation** | Expose a focused Livewire 4 component and namespaced Blade default view for `edge invalidation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [RoutePreview.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-web-delivery-livewire/src/Livewire/RoutePreview.php) · [WebDeliveryLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-web-delivery-livewire/src/WebDeliveryLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [DeliveryRouteQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Queries/DeliveryRouteQuery.php) | `public function paginate(int $perPage = 15, string $search = '', ?string $status = null): LengthAwarePaginator`<br>`public function find(string $path): ?DeliveryRoute` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [WebDeliveryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Actions/WebDeliveryService.php) | `public function __construct(private EdgeInvalidationRegistry $edge)`<br>`public function registerRoute(array $attributes): DeliveryRoute`<br>`public function updateRoute(DeliveryRoute $route, array $attributes): DeliveryRoute`<br>`public function deleteRoute(DeliveryRoute $route): void`<br>`public function render(string $path, ?string $previewToken = null): DeliveryResult`<br>`public function issuePreviewToken(DeliveryRoute $route): string`<br>`public function setMaintenance(DeliveryRoute $route, bool $enabled): DeliveryRoute`<br>`public function invalidate(array $cacheTags, string $idempotencyKey, ?string $provider = null, int\|string\|null $teamId = null): DeliveryInvalidation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DeliveryInvalidation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Models/DeliveryInvalidation.php) | `idempotency_key`, `cache_tags`, `status`, `provider`, `failure_reason`, `completed_at`, `team_id` |
| [DeliveryRoute.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Models/DeliveryRoute.php) | `path`, `route_type`, `content_type`, `content_id`, `body`, `canonical_url`, `redirect_url`, `redirect_status`, `metadata`, `cache_tags`, `cache_ttl`, `preview_enabled`, `preview_token_hash`, `preview_expires_at`, `maintenance`, `status`, `error_status`, `error_message`, `team_id` |
<!-- layer-implementation-plan:end -->
