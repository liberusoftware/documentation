# Billing: Catalog Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#catalog). Observed identity: [`liberusoftware/module-billing-catalog-livewire`](../../../modules/source/liberusoftware--module-billing-catalog-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-billing-catalog-livewire`  
**Matching domain module:** `billing-catalog`  
**Application:** Billing  
**Source feature:** [Catalog](../features/catalog.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Products:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Plans:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Add-ons:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Bundles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Configurable options:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Eligibility:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Channels:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Lifecycle:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-billing-catalog-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-billing-catalog::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `products`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `plans`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `add-ons`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `bundles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `configurable-options`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `eligibility`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `channels`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `lifecycle`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `billing-catalog` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/catalog.md) · [API plan](../api/catalog.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Products** | Expose a focused Livewire 4 component and namespaced Blade default view for `products` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Plans** | Expose a focused Livewire 4 component and namespaced Blade default view for `plans` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Add-ons** | Expose a focused Livewire 4 component and namespaced Blade default view for `add-ons` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Bundles** | Expose a focused Livewire 4 component and namespaced Blade default view for `bundles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Configurable options** | Expose a focused Livewire 4 component and namespaced Blade default view for `configurable options` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Eligibility** | Expose a focused Livewire 4 component and namespaced Blade default view for `eligibility` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Channels** | Expose a focused Livewire 4 component and namespaced Blade default view for `channels` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Lifecycle** | Expose a focused Livewire 4 component and namespaced Blade default view for `lifecycle` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CatalogLivewireServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-livewire/src/CatalogLivewireServiceProvider.php) · [CatalogRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-livewire/src/Components/CatalogRecords.php) · [ProductCatalog.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog-livewire/src/Components/ProductCatalog.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListCatalogRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Queries/ListCatalogRecords.php) | `public function execute(string $model, ?int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListProducts.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Queries/ListProducts.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCatalogRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/CreateCatalogRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(string $model, array $attributes): CatalogRecord` |
| [CreateProduct.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/CreateProduct.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Product` |
| [TransitionCatalogLifecycle.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/TransitionCatalogLifecycle.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CatalogRecord $record, CatalogStatus $status): CatalogRecord` |
| [TransitionProductLifecycle.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/TransitionProductLifecycle.php) | `public function execute(Product $product, ProductStatus $status): Product` |
| [CatalogRecordPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Policies/CatalogRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, CatalogRecord $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, CatalogRecord $record): bool` |
| [ProductPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Policies/ProductPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Product $product): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Product $product): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Addon.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Addon.php) | No literal fillable array detected; inspect the model and API schema. |
| [Bundle.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Bundle.php) | No literal fillable array detected; inspect the model and API schema. |
| [CatalogRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/CatalogRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [Channel.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Channel.php) | No literal fillable array detected; inspect the model and API schema. |
| [ConfigurableOption.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/ConfigurableOption.php) | No literal fillable array detected; inspect the model and API schema. |
| [Eligibility.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Eligibility.php) | No literal fillable array detected; inspect the model and API schema. |
| [Plan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Plan.php) | No literal fillable array detected; inspect the model and API schema. |
| [Product.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Product.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
