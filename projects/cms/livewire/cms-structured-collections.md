# CMS: Cms Structured Collections Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-structured-collections). Observed identity: [`liberusoftware/module-cms-structured-collections-livewire`](../../../modules/source/liberusoftware--module-cms-structured-collections-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-structured-collections-livewire`  
**Matching domain module:** `cms-structured-collections`  
**Application:** CMS  
**Source feature:** [Cms Structured Collections](../features/cms-structured-collections.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Reusable records:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Directories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **FAQs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Testimonials:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Profiles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Locations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Datasets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Custom collection types:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-structured-collections-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsStructuredCollections::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `reusable-records`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `directories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `faqs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `testimonials`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `profiles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `locations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `datasets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `custom-collection-types`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-structured-collections` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-structured-collections.md) · [API plan](../api/cms-structured-collections.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Reusable records** | Expose a focused Livewire 4 component and namespaced Blade default view for `reusable records` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Directories** | Expose a focused Livewire 4 component and namespaced Blade default view for `directories` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **FAQs** | Expose a focused Livewire 4 component and namespaced Blade default view for `faqs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Testimonials** | Expose a focused Livewire 4 component and namespaced Blade default view for `testimonials` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Profiles** | Expose a focused Livewire 4 component and namespaced Blade default view for `profiles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Locations** | Expose a focused Livewire 4 component and namespaced Blade default view for `locations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Datasets** | Expose a focused Livewire 4 component and namespaced Blade default view for `datasets` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Custom collection types** | Expose a focused Livewire 4 component and namespaced Blade default view for `custom collection types` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [StructuredCollectionBrowser.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-structured-collections-livewire/src/Livewire/StructuredCollectionBrowser.php) · [StructuredCollectionsLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-structured-collections-livewire/src/StructuredCollectionsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [StructuredCollectionQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-structured-collections/src/Queries/StructuredCollectionQuery.php) | `public function __construct(private CollectionQuery $legacy)`<br>`public function paginate(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function collection(string $slug): ?Collection`<br>`public function records(string $slug, int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function record(string $collection, string $slug): ?CollectionItem`<br>`public function recordForMutation(string $collection, string $slug): ?CollectionItem` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [StructuredCollectionMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-structured-collections/src/Actions/StructuredCollectionMutationService.php) | `public function __construct(private CollectionMutationService $legacy)`<br>`public function create(array $attributes): Collection`<br>`public function update(Collection $collection, array $attributes): Collection`<br>`public function delete(Collection $collection): void`<br>`public function createRecord(Collection $collection, array $attributes): CollectionItem`<br>`public function updateRecord(CollectionItem $record, array $attributes): CollectionItem`<br>`public function deleteRecord(CollectionItem $record): void` |
<!-- layer-implementation-plan:end -->
