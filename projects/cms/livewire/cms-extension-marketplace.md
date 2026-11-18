# CMS: Cms Extension Marketplace Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-extension-marketplace). Observed identity: [`liberusoftware/module-cms-extension-marketplace-livewire`](../../../modules/source/liberusoftware--module-cms-extension-marketplace-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-extension-marketplace-livewire`  
**Matching domain module:** `cms-extension-marketplace`  
**Application:** CMS  
**Source feature:** [Cms Extension Marketplace](../features/cms-extension-marketplace.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Publishers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Listings:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Categories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Versions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Signing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reviews:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Licensing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Trials:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Security status:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Support:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Distribution:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-extension-marketplace-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsExtensionMarketplace::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `publishers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `listings`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `categories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `versions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `signing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reviews`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `licensing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `trials`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `security-status`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `support`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `distribution`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-extension-marketplace` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-extension-marketplace.md) · [API plan](../api/cms-extension-marketplace.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Publishers** | Expose a focused Livewire 4 component and namespaced Blade default view for `publishers` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Listings** | Expose a focused Livewire 4 component and namespaced Blade default view for `listings` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Categories** | Expose a focused Livewire 4 component and namespaced Blade default view for `categories` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Versions** | Expose a focused Livewire 4 component and namespaced Blade default view for `versions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Signing** | Expose a focused Livewire 4 component and namespaced Blade default view for `signing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reviews** | Expose a focused Livewire 4 component and namespaced Blade default view for `reviews` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Licensing** | Expose a focused Livewire 4 component and namespaced Blade default view for `licensing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Trials** | Expose a focused Livewire 4 component and namespaced Blade default view for `trials` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Security status** | Expose a focused Livewire 4 component and namespaced Blade default view for `security status` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Support** | Expose a focused Livewire 4 component and namespaced Blade default view for `support` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Distribution** | Expose a focused Livewire 4 component and namespaced Blade default view for `distribution` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ExtensionCatalog.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-extension-marketplace-livewire/src/Livewire/ExtensionCatalog.php) · [ExtensionMarketplaceLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-extension-marketplace-livewire/src/ExtensionMarketplaceLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ExtensionMarketplaceQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Queries/ExtensionMarketplaceQuery.php) | `public function catalog(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function find(string $key): ?ExtensionListing` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ExtensionMarketplaceService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Services/ExtensionMarketplaceService.php) | `public function publisher(array $attributes, ?int $teamId = null): ExtensionPublisher`<br>`public function category(array $attributes): ExtensionCategory`<br>`public function listing(array $attributes, ?int $teamId = null): ExtensionListing`<br>`public function version(ExtensionListing $listing, array $attributes): ExtensionVersion`<br>`public function sign(ExtensionVersion $version, string $signature, string $key): ExtensionVersion`<br>`public function security(ExtensionListing $listing, string $status): ExtensionListing`<br>`public function review(ExtensionListing $listing, string $type, int\|string $subject, int $rating, ?string $body = null, ?int $teamId = null): ExtensionReview`<br>`public function license(ExtensionListing $listing, string $subjectType, int\|string $subject, ?int $days = null): ExtensionLicense`<br>`public function trial(ExtensionListing $listing, string $subjectType, int\|string $subject, int $days = 14): ExtensionTrial`<br>`public function support(ExtensionListing $listing, array $attributes): ExtensionSupport`<br>`public function distribute(ExtensionVersion $version, array $attributes): ExtensionDistribution`<br>`public function ratingSummary(ExtensionListing $listing): array`<br>`public function publish(ExtensionListing $listing): ExtensionListing` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ExtensionCategory.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionCategory.php) | `key`, `name`, `description` |
| [ExtensionDistribution.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionDistribution.php) | `version_id`, `channel`, `url`, `checksum`, `status` |
| [ExtensionLicense.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionLicense.php) | `listing_id`, `license_key`, `subject_type`, `subject_id`, `status`, `starts_at`, `ends_at` |
| [ExtensionListing.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionListing.php) | `publisher_id`, `category_id`, `key`, `name`, `description`, `license`, `status`, `security_status`, `metadata`, `team_id` |
| [ExtensionPublisher.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionPublisher.php) | `key`, `name`, `website`, `status`, `team_id` |
| [ExtensionReview.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionReview.php) | `listing_id`, `reviewer_type`, `reviewer_id`, `rating`, `review`, `status`, `team_id` |
| [ExtensionSupport.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionSupport.php) | `listing_id`, `channel`, `url`, `response_hours` |
| [ExtensionTrial.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-extension-marketplace/src/Models/ExtensionTrial.php) | `listing_id`, `subject_type`, `subject_id`, `status`, `starts_at`, `ends_at` |
<!-- layer-implementation-plan:end -->
