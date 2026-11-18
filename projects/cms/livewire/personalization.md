# CMS: Personalization Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#personalization). Observed identity: [`liberusoftware/module-cms-personalization-livewire`](../../../modules/source/liberusoftware--module-cms-personalization-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-personalization-livewire`  
**Matching domain module:** `cms-personalization`  
**Application:** CMS  
**Source feature:** [Personalization](../features/personalization.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Audience/context rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Variants:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Eligibility:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Priority:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Fallback:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Consent:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Holdouts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Decision evidence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-personalization-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-cms-personalization::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `audience-context-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `variants`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `eligibility`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `priority`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `fallback`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `consent`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `holdouts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `decision-evidence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-personalization` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/personalization.md) · [API plan](../api/personalization.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Audience/context rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `audience/context rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Variants** | Expose a focused Livewire 4 component and namespaced Blade default view for `variants` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Eligibility** | Expose a focused Livewire 4 component and namespaced Blade default view for `eligibility` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Priority** | Expose a focused Livewire 4 component and namespaced Blade default view for `priority` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Fallback** | Expose a focused Livewire 4 component and namespaced Blade default view for `fallback` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Consent** | Expose a focused Livewire 4 component and namespaced Blade default view for `consent` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Holdouts** | Expose a focused Livewire 4 component and namespaced Blade default view for `holdouts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Decision evidence** | Expose a focused Livewire 4 component and namespaced Blade default view for `decision evidence` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AudiencePreview.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-personalization-livewire/src/Livewire/AudiencePreview.php) · [PersonalizationLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-personalization-livewire/src/PersonalizationLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [DecisionEngine.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-personalization/src/Services/DecisionEngine.php) | `public function decide(string $audienceKey, array $context = [], ?string $subjectKey = null, bool $consent = false): array` |
| [PersonalizationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-personalization/src/Services/PersonalizationService.php) | `public function createAudience(array $attributes, ?int $teamId = null): Audience`<br>`public function updateAudience(Audience $audience, array $attributes): Audience`<br>`public function saveVariant(Audience $audience, array $attributes, ?Variant $variant = null): Variant`<br>`public function deleteVariant(Variant $variant): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Audience.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-personalization/src/Models/Audience.php) | `name`, `key`, `rules`, `requires_consent`, `active`, `team_id` |
| [Decision.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-personalization/src/Models/Decision.php) | `audience_key`, `variant_key`, `subject_key`, `context`, `reason`, `team_id` |
| [Variant.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-personalization/src/Models/Variant.php) | `audience_id`, `key`, `payload`, `priority`, `holdout_percent`, `fallback`, `active`, `team_id` |
<!-- layer-implementation-plan:end -->
