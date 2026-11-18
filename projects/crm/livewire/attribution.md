# CRM: Attribution Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#attribution). Observed identity: [`liberusoftware/module-crm-attribution-livewire`](../../../modules/source/liberusoftware--module-crm-attribution-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-attribution-livewire`  
**Matching domain module:** `crm-attribution`  
**Application:** CRM  
**Source feature:** [Attribution](../features/attribution.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **First/last/multi-touch models:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Campaign members:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Source normalization:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **UTM/click IDs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Offline conversions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Influence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cost allocation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Model comparison:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-attribution-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-attribution::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `first-last-multi-touch-models`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `campaign-members`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `source-normalization`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `utm-click-ids`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `offline-conversions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `influence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cost-allocation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `model-comparison`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-attribution` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/attribution.md) · [API plan](../api/attribution.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **First/last/multi-touch models** | Expose a focused Livewire 4 component and namespaced Blade default view for `first/last/multi-touch models` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Campaign members** | Expose a focused Livewire 4 component and namespaced Blade default view for `campaign members` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Source normalization** | Expose a focused Livewire 4 component and namespaced Blade default view for `source normalization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **UTM/click IDs** | Expose a focused Livewire 4 component and namespaced Blade default view for `utm/click ids` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Offline conversions** | Expose a focused Livewire 4 component and namespaced Blade default view for `offline conversions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Influence** | Expose a focused Livewire 4 component and namespaced Blade default view for `influence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Cost allocation** | Expose a focused Livewire 4 component and namespaced Blade default view for `cost allocation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Model comparison** | Expose a focused Livewire 4 component and namespaced Blade default view for `model comparison` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AttributionLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution-livewire/src/AttributionLivewireServiceProvider.php) · [AttributionBrowser.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution-livewire/src/Components/AttributionBrowser.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AttributionQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Queries/AttributionQuery.php) | `public function touchpoints(int $teamId): Builder`<br>`public function conversions(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordConversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Actions/RecordConversion.php) | `public function execute(int $teamId, array $input): Conversion` |
| [RecordTouchpoint.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Actions/RecordTouchpoint.php) | `public function execute(int $teamId, array $input): Touchpoint` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Models/Conversion.php) | No literal fillable array detected; inspect the model and API schema. |
| [Touchpoint.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Models/Touchpoint.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
