# CMS: Accessibility Assistant Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accessibility-assistant). Observed identity: [`liberusoftware/module-cms-accessibility-assistant-livewire`](../../../modules/source/liberusoftware--module-cms-accessibility-assistant-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-accessibility-assistant-livewire`  
**Matching domain module:** `cms-accessibility-assistant`  
**Application:** CMS  
**Source feature:** [Accessibility Assistant](../features/accessibility-assistant.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Authoring checks for headings:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Links:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tables:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Alternatives:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Contrast metadata:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Language:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Captions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exceptions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-accessibility-assistant-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-cms-accessibility-assistant::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `authoring-checks-for-headings`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `links`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tables`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `alternatives`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `contrast-metadata`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `language`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `captions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exceptions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-accessibility-assistant` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accessibility-assistant.md) · [API plan](../api/accessibility-assistant.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Authoring checks for headings** | Expose a focused Livewire 4 component and namespaced Blade default view for `authoring checks for headings` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Links** | Expose a focused Livewire 4 component and namespaced Blade default view for `links` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Tables** | Expose a focused Livewire 4 component and namespaced Blade default view for `tables` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Alternatives** | Expose a focused Livewire 4 component and namespaced Blade default view for `alternatives` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Contrast metadata** | Expose a focused Livewire 4 component and namespaced Blade default view for `contrast metadata` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Language** | Expose a focused Livewire 4 component and namespaced Blade default view for `language` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Captions** | Expose a focused Livewire 4 component and namespaced Blade default view for `captions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Exceptions** | Expose a focused Livewire 4 component and namespaced Blade default view for `exceptions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AccessibilityAnalyzer.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-accessibility-assistant-livewire/src/Livewire/AccessibilityAnalyzer.php) · [AccessibilityAssistantLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-accessibility-assistant-livewire/src/AccessibilityAssistantLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AccessibilityAssistantService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-accessibility-assistant/src/Services/AccessibilityAssistantService.php) | `public function analyze(string $html, array $exceptions = []): array` |
<!-- layer-implementation-plan:end -->
