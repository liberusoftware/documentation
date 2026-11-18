# CMS: Cms Block Editor Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-block-editor). Observed identity: [`liberusoftware/module-cms-block-editor-livewire`](../../../modules/source/liberusoftware--module-cms-block-editor-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-block-editor-livewire`  
**Matching domain module:** `cms-block-editor`  
**Application:** CMS  
**Source feature:** [Cms Block Editor](../features/cms-block-editor.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Typed content blocks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Nesting rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Patterns:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reusable/global blocks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Locking:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Transforms:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Previews:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Revision-safe data:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-block-editor-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsBlockEditor::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `typed-content-blocks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `nesting-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `patterns`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reusable-global-blocks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `locking`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `transforms`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `previews`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `revision-safe-data`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-block-editor` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-block-editor.md) · [API plan](../api/cms-block-editor.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Typed content blocks** | Expose a focused Livewire 4 component and namespaced Blade default view for `typed content blocks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Nesting rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `nesting rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Patterns** | Expose a focused Livewire 4 component and namespaced Blade default view for `patterns` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reusable/global blocks** | Expose a focused Livewire 4 component and namespaced Blade default view for `reusable/global blocks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Locking** | Expose a focused Livewire 4 component and namespaced Blade default view for `locking` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Transforms** | Expose a focused Livewire 4 component and namespaced Blade default view for `transforms` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Previews** | Expose a focused Livewire 4 component and namespaced Blade default view for `previews` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Revision-safe data** | Expose a focused Livewire 4 component and namespaced Blade default view for `revision-safe data` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [BlockEditor.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-block-editor-livewire/src/Livewire/BlockEditor.php) · [BlockEditorLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-block-editor-livewire/src/BlockEditorLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [BlockEditorService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-block-editor/src/Services/BlockEditorService.php) | `public function __construct(private BlockTypeRegistry $registry, private BlockRenderer $renderer)`<br>`public function save(?int $teamId, string $subjectType, string $subjectId, array $blocks, ?int $expectedVersion = null): BlockDocument`<br>`public function createPattern(?int $teamId, string $name, array $blocks, bool $reusable = true): BlockPattern`<br>`public function lock(BlockDocument $document, bool $locked = true): BlockDocument` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BlockDocument.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-block-editor/src/Models/BlockDocument.php) | `team_id`, `subject_type`, `subject_id`, `blocks`, `version`, `locked`, `preview_html` |
| [BlockPattern.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-block-editor/src/Models/BlockPattern.php) | `team_id`, `name`, `blocks`, `reusable`, `locked` |
<!-- layer-implementation-plan:end -->
