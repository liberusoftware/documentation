# Maintenance: Assets Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#assets). Observed identity: [`liberusoftware/module-maintenance-assets-livewire`](../../../modules/source/liberusoftware--module-maintenance-assets-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-maintenance-assets-livewire`  
**Matching domain module:** `maintenance-assets`  
**Application:** Maintenance  
**Source feature:** [Assets](../features/assets.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Hierarchies:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Categories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Specifications:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Meters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Warranties:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Condition:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **QR/barcodes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **History:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-maintenance-assets-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-maintenance-assets::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `hierarchies`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `categories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `specifications`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `meters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `warranties`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `condition`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `qr-barcodes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `history`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `maintenance-assets` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/assets.md) · [API plan](../api/assets.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Hierarchies** | Expose a focused Livewire 4 component and namespaced Blade default view for `hierarchies` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Categories** | Expose a focused Livewire 4 component and namespaced Blade default view for `categories` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Specifications** | Expose a focused Livewire 4 component and namespaced Blade default view for `specifications` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Meters** | Expose a focused Livewire 4 component and namespaced Blade default view for `meters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Warranties** | Expose a focused Livewire 4 component and namespaced Blade default view for `warranties` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Condition** | Expose a focused Livewire 4 component and namespaced Blade default view for `condition` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **QR/barcodes** | Expose a focused Livewire 4 component and namespaced Blade default view for `qr/barcodes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **History** | Expose a focused Livewire 4 component and namespaced Blade default view for `history` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AssetsLivewireServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets-livewire/src/AssetsLivewireServiceProvider.php) · [AssetList.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets-livewire/src/Components/AssetList.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAsset.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Actions/CreateAsset.php) | `public function handle(int $teamId, array $attributes): Asset` |
| [DeleteAsset.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Actions/DeleteAsset.php) | `public function handle(int $teamId, Asset $asset): void` |
| [RecordAssetHistory.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Actions/RecordAssetHistory.php) | `public function handle(int $teamId, Asset $asset, string $type, string $note, ?int $actorId = null): Asset` |
| [UpdateAsset.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Actions/UpdateAsset.php) | `public function handle(int $teamId, Asset $asset, array $attributes): Asset` |
| [AssetPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Policies/AssetPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Asset $asset): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Asset $asset): bool`<br>`public function delete(object $user, Asset $asset): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Asset.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Models/Asset.php) | `team_id`, `name`, `description`, `code`, `category`, `serial_number`, `model`, `manufacturer`, `location`, `purchase_date`, `warranty_expiry`, `notes`, `condition`, `criticality`, `status`, `qr_code`, `barcode`, `sensor_enabled`, `sensor_type`, `sensor_id`, `sensor_config`, `last_sensor_reading_at`, `metadata` |
<!-- layer-implementation-plan:end -->
