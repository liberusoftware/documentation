# CRM: Crm Advertising Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-advertising). Observed identity: [`liberusoftware/module-crm-advertising-livewire`](../../../modules/source/liberusoftware--module-crm-advertising-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-advertising-livewire`  
**Matching domain module:** `crm-advertising`  
**Application:** CRM  
**Source feature:** [Crm Advertising](../features/crm-advertising.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Ad-account connections:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Campaign visibility:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Lead-ad ingestion:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **CRM audiences:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Offline/server conversions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Spend/performance sync:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Attribution:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-advertising-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmAdvertising::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `ad-account-connections`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `campaign-visibility`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `lead-ad-ingestion`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `crm-audiences`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `offline-server-conversions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `spend-performance-sync`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `attribution`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-advertising` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-advertising.md) · [API plan](../api/crm-advertising.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Ad-account connections** | Expose a focused Livewire 4 component and namespaced Blade default view for `ad-account connections` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Campaign visibility** | Expose a focused Livewire 4 component and namespaced Blade default view for `campaign visibility` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Lead-ad ingestion** | Expose a focused Livewire 4 component and namespaced Blade default view for `lead-ad ingestion` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **CRM audiences** | Expose a focused Livewire 4 component and namespaced Blade default view for `crm audiences` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Offline/server conversions** | Expose a focused Livewire 4 component and namespaced Blade default view for `offline/server conversions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Spend/performance sync** | Expose a focused Livewire 4 component and namespaced Blade default view for `spend/performance sync` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Attribution** | Expose a focused Livewire 4 component and namespaced Blade default view for `attribution` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AdvertisingLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising-livewire/src/AdvertisingLivewireServiceProvider.php) · [AdvertisingWorkspace.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising-livewire/src/Components/AdvertisingWorkspace.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AdvertisingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Queries/AdvertisingQuery.php) | `public function records(int $teamId, ?string $kind = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TransitionRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Actions/TransitionRecord.php) | `public function execute(int $teamId, int $id, string $status): AdvertisingRecord` |
| [UpsertRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Actions/UpsertRecord.php) | `public function execute(int $teamId, array $attributes, ?int $id = null): AdvertisingRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AdvertisingRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Models/AdvertisingRecord.php) | `team_id`, `kind`, `name`, `status`, `external_id`, `platform`, `payload`, `starts_at`, `ends_at`, `completed_at` |
<!-- layer-implementation-plan:end -->
