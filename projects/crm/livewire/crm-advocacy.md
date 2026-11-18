# CRM: Crm Advocacy Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-advocacy). Observed identity: [`liberusoftware/module-crm-advocacy-livewire`](../../../modules/source/liberusoftware--module-crm-advocacy-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-advocacy-livewire`  
**Matching domain module:** `crm-advocacy`  
**Application:** CRM  
**Source feature:** [Crm Advocacy](../features/crm-advocacy.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **References:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Testimonials:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reviews:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Case-study consent:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Speakers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Advisory boards:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Nominations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Requests:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Recognition history:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-advocacy-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmAdvocacy::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `references`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `testimonials`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reviews`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `case-study-consent`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `speakers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `advisory-boards`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `nominations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `requests`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `recognition-history`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-advocacy` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-advocacy.md) · [API plan](../api/crm-advocacy.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **References** | Expose a focused Livewire 4 component and namespaced Blade default view for `references` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Testimonials** | Expose a focused Livewire 4 component and namespaced Blade default view for `testimonials` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reviews** | Expose a focused Livewire 4 component and namespaced Blade default view for `reviews` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Case-study consent** | Expose a focused Livewire 4 component and namespaced Blade default view for `case-study consent` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Speakers** | Expose a focused Livewire 4 component and namespaced Blade default view for `speakers` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Advisory boards** | Expose a focused Livewire 4 component and namespaced Blade default view for `advisory boards` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Nominations** | Expose a focused Livewire 4 component and namespaced Blade default view for `nominations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Requests** | Expose a focused Livewire 4 component and namespaced Blade default view for `requests` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Recognition history** | Expose a focused Livewire 4 component and namespaced Blade default view for `recognition history` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AdvocacyLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy-livewire/src/AdvocacyLivewireServiceProvider.php) · [AdvocacyWorkspace.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy-livewire/src/Components/AdvocacyWorkspace.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AdvocacyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy/src/Queries/AdvocacyQuery.php) | `public function records(int $teamId, ?string $kind = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TransitionRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy/src/Actions/TransitionRecord.php) | `public function execute(int $teamId, int $id, string $status): AdvocacyRecord` |
| [UpsertRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy/src/Actions/UpsertRecord.php) | `public function execute(int $teamId, array $attributes, ?int $id = null): AdvocacyRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AdvocacyRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advocacy/src/Models/AdvocacyRecord.php) | `team_id`, `kind`, `name`, `status`, `contact_id`, `owner_id`, `payload`, `requested_at`, `approved_at`, `completed_at` |
<!-- layer-implementation-plan:end -->
