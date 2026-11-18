# CRM: Crm Personalization Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-personalization). Observed identity: [`liberusoftware/module-crm-personalization-livewire`](../../../modules/source/liberusoftware--module-crm-personalization-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-personalization-livewire`  
**Matching domain module:** `crm-personalization`  
**Application:** CRM  
**Source feature:** [Crm Personalization](../features/crm-personalization.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Rules and decisioning for content:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Offer:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Channel:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Send time:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Locale:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Lifecycle:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Customer attributes with holdouts and fallback:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-personalization-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmPersonalization::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `rules-and-decisioning-for-content`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `offer`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `channel`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `send-time`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `locale`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `lifecycle`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `customer-attributes-with-holdouts-and-fallback`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-personalization` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-personalization.md) · [API plan](../api/crm-personalization.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Rules and decisioning for content** | Expose a focused Livewire 4 component and namespaced Blade default view for `rules and decisioning for content` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Offer** | Expose a focused Livewire 4 component and namespaced Blade default view for `offer` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Channel** | Expose a focused Livewire 4 component and namespaced Blade default view for `channel` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Send time** | Expose a focused Livewire 4 component and namespaced Blade default view for `send time` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Locale** | Expose a focused Livewire 4 component and namespaced Blade default view for `locale` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Lifecycle** | Expose a focused Livewire 4 component and namespaced Blade default view for `lifecycle` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Customer attributes with holdouts and fallback** | Expose a focused Livewire 4 component and namespaced Blade default view for `customer attributes with holdouts and fallback` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [PersonalizationDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization-livewire/src/Components/PersonalizationDashboard.php) · [PersonalizationLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization-livewire/src/PersonalizationLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PersonalizationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Queries/PersonalizationQuery.php) | `public function rules(int $teamId)`<br>`public function decisions(int $teamId)`<br>`public function outcomes(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePersonalizationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/CreatePersonalizationRule.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PersonalizationRule` |
| [DecidePersonalization.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/DecidePersonalization.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PersonalizationDecision` |
| [RecordPersonalizationOutcome.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/RecordPersonalizationOutcome.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PersonalizationOutcome` |
| [UpdatePersonalizationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Actions/UpdatePersonalizationRule.php) | `public function __construct(private readonly PersonalizationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $ruleId, array $input): PersonalizationRule` |
| [PersonalizationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Services/PersonalizationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PersonalizationDecision.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Models/PersonalizationDecision.php) | No literal fillable array detected; inspect the model and API schema. |
| [PersonalizationOutcome.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Models/PersonalizationOutcome.php) | No literal fillable array detected; inspect the model and API schema. |
| [PersonalizationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-personalization/src/Models/PersonalizationRule.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
