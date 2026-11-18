# Real Estate: Parties Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#parties). Observed identity: [`liberusoftware/real-estate-parties-livewire`](../../../modules/source/liberusoftware--real-estate-parties-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-real-estate-parties-livewire`  
**Matching domain module:** `real-estate-parties`  
**Application:** Real Estate  
**Source feature:** [Parties](../features/parties.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Applicants:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Vendors:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Landlords:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tenants:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Buyers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Solicitors:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Contractors:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Relationships:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Consent:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-real-estate-parties-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-real-estate-parties::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `applicants`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `vendors`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `landlords`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tenants`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `buyers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `solicitors`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `contractors`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `relationships`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `consent`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `real-estate-parties` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/parties.md) · [API plan](../api/parties.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Applicants** | Expose a focused Livewire 4 component and namespaced Blade default view for `applicants` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Vendors** | Expose a focused Livewire 4 component and namespaced Blade default view for `vendors` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Landlords** | Expose a focused Livewire 4 component and namespaced Blade default view for `landlords` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Tenants** | Expose a focused Livewire 4 component and namespaced Blade default view for `tenants` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Buyers** | Expose a focused Livewire 4 component and namespaced Blade default view for `buyers` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Solicitors** | Expose a focused Livewire 4 component and namespaced Blade default view for `solicitors` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Contractors** | Expose a focused Livewire 4 component and namespaced Blade default view for `contractors` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Relationships** | Expose a focused Livewire 4 component and namespaced Blade default view for `relationships` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Consent** | Expose a focused Livewire 4 component and namespaced Blade default view for `consent` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ContactEnquiryForm.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-livewire/src/Components/ContactEnquiryForm.php) · [LandlordReviewForm.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-livewire/src/Components/LandlordReviewForm.php) · [PartyList.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-livewire/src/Components/PartyList.php) · [PartyReviewForm.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-livewire/src/Components/PartyReviewForm.php) · [TenantReviewForm.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-livewire/src/Components/TenantReviewForm.php) · [PartiesLivewireServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties-livewire/src/PartiesLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PartyPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Policies/PartyPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Party $party): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Party $party): bool`<br>`public function delete(AuthUser $authUser, Party $party): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Party $party): bool`<br>`public function forceDelete(AuthUser $authUser, Party $party): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Party $party): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Contact.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/Contact.php) | No literal fillable array detected; inspect the model and API schema. |
| [ContactMessage.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/ContactMessage.php) | No literal fillable array detected; inspect the model and API schema. |
| [Party.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/Party.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartyRelationship.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/PartyRelationship.php) | No literal fillable array detected; inspect the model and API schema. |
| [PartyReview.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-parties/src/Models/PartyReview.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
