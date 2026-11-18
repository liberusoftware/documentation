# CRM: Customer Data Platform Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customer-data-platform). Observed identity: [`liberusoftware/module-crm-customer-data-platform-livewire`](../../../modules/source/liberusoftware--module-crm-customer-data-platform-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-customer-data-platform-livewire`  
**Matching domain module:** `crm-customer-data-platform`  
**Application:** CRM  
**Source feature:** [Customer Data Platform](../features/customer-data-platform.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Source profiles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Identity resolution:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Unified profiles:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Audience activation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Event ingestion:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Consent-aware calculated attributes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Profile lineage:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-customer-data-platform-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-customer-data-platform::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `source-profiles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `identity-resolution`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `unified-profiles`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `audience-activation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `event-ingestion`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `consent-aware-calculated-attributes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `profile-lineage`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-customer-data-platform` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/customer-data-platform.md) · [API plan](../api/customer-data-platform.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Source profiles** | Expose a focused Livewire 4 component and namespaced Blade default view for `source profiles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Identity resolution** | Expose a focused Livewire 4 component and namespaced Blade default view for `identity resolution` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Unified profiles** | Expose a focused Livewire 4 component and namespaced Blade default view for `unified profiles` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Audience activation** | Expose a focused Livewire 4 component and namespaced Blade default view for `audience activation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Event ingestion** | Expose a focused Livewire 4 component and namespaced Blade default view for `event ingestion` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Consent-aware calculated attributes** | Expose a focused Livewire 4 component and namespaced Blade default view for `consent-aware calculated attributes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Profile lineage** | Expose a focused Livewire 4 component and namespaced Blade default view for `profile lineage` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [CdpDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform-livewire/src/Livewire/CdpDashboard.php) · [CustomerDataPlatformLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform-livewire/src/CustomerDataPlatformLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CdpQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Queries/CdpQuery.php) | `public function profiles(int $teamId)`<br>`public function audiences(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateCdpAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/ActivateCdpAudience.php) | `public function __construct(private readonly CdpPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CdpAudience $audience, string $destination): CdpAudience` |
| [CreateCdpAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/CreateCdpAudience.php) | `public function __construct(private readonly CdpPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CdpAudience` |
| [IngestCdpEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/IngestCdpEvent.php) | `public function execute(int $teamId, CdpProfile $profile, array $input): CdpEvent` |
| [UpsertCdpProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/UpsertCdpProfile.php) | `public function __construct(private readonly CdpPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CdpProfile` |
| [CdpPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Services/CdpPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CdpAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpAudience.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpIdentity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpIdentity.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpProfile.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
