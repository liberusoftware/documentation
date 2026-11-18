# Real Estate: Lettings Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#lettings). Observed identity: [`liberusoftware/real-estate-lettings-livewire`](../../../modules/source/liberusoftware--real-estate-lettings-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-real-estate-lettings-livewire`  
**Matching domain module:** `real-estate-lettings`  
**Application:** Real Estate  
**Source feature:** [Lettings](../features/lettings.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Applications:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Referencing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deposits:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Agreements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Move-in/out:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Renewals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rent changes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Notices:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-real-estate-lettings-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-real-estate-lettings::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `applications`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `referencing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deposits`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `agreements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `move-in-out`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `renewals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rent-changes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `notices`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `real-estate-lettings` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-real-estate-laravel-filament`](https://github.com/liberusoftware/project-real-estate-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/lettings.md) · [API plan](../api/lettings.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Applications** | Expose a focused Livewire 4 component and namespaced Blade default view for `applications` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Referencing** | Expose a focused Livewire 4 component and namespaced Blade default view for `referencing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deposits** | Expose a focused Livewire 4 component and namespaced Blade default view for `deposits` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Agreements** | Expose a focused Livewire 4 component and namespaced Blade default view for `agreements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Move-in/out** | Expose a focused Livewire 4 component and namespaced Blade default view for `move-in/out` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Renewals** | Expose a focused Livewire 4 component and namespaced Blade default view for `renewals` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Rent changes** | Expose a focused Livewire 4 component and namespaced Blade default view for `rent changes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Notices** | Expose a focused Livewire 4 component and namespaced Blade default view for `notices` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [LettingList.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-livewire/src/Components/LettingList.php) · [RentalApplicationForm.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-livewire/src/Components/RentalApplicationForm.php) · [LettingsLivewireServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings-livewire/src/LettingsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListLettings.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Queries/ListLettings.php) | `public function handle(int\|string $teamId, ?string $capability = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [LettingPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Policies/LettingPolicy.php) | `public function view($user, Letting $letting): bool`<br>`public function update($user, Letting $letting): bool`<br>`public function delete($user, Letting $letting): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [LeaseAgreement.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/LeaseAgreement.php) | No literal fillable array detected; inspect the model and API schema. |
| [Letting.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/Letting.php) | No literal fillable array detected; inspect the model and API schema. |
| [RentalApplication.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/RentalApplication.php) | No literal fillable array detected; inspect the model and API schema. |
| [RentalCharge.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-lettings/src/Models/RentalCharge.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
