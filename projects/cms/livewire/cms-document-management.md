# CMS: Cms Document Management Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-document-management). Observed identity: [`liberusoftware/module-cms-document-management-livewire`](../../../modules/source/liberusoftware--module-cms-document-management-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-document-management-livewire`  
**Matching domain module:** `cms-document-management`  
**Application:** CMS  
**Source feature:** [Cms Document Management](../features/cms-document-management.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Documents:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Previews:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **OCR/text extraction adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Versions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Access:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Downloads:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Watermarks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Retention:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-document-management-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsDocumentManagement::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `documents`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `previews`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `ocr-text-extraction-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `versions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `access`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `downloads`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `watermarks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `retention`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-document-management` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-document-management.md) · [API plan](../api/cms-document-management.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Documents** | Expose a focused Livewire 4 component and namespaced Blade default view for `documents` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Previews** | Expose a focused Livewire 4 component and namespaced Blade default view for `previews` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **OCR/text extraction adapters** | Expose a focused Livewire 4 component and namespaced Blade default view for `ocr/text extraction adapters` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Versions** | Expose a focused Livewire 4 component and namespaced Blade default view for `versions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Access** | Expose a focused Livewire 4 component and namespaced Blade default view for `access` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Downloads** | Expose a focused Livewire 4 component and namespaced Blade default view for `downloads` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Watermarks** | Expose a focused Livewire 4 component and namespaced Blade default view for `watermarks` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Retention** | Expose a focused Livewire 4 component and namespaced Blade default view for `retention` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [DocumentBrowser.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-document-management-livewire/src/Livewire/DocumentBrowser.php) · [DocumentManagementLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-document-management-livewire/src/DocumentManagementLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [DocumentManagementService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-document-management/src/Services/DocumentManagementService.php) | `public function documents(?int $teamId, int $perPage = 25): LengthAwarePaginator`<br>`public function create(array $data, ?int $teamId = null): Document`<br>`public function transition(Document $document, string $status): Document`<br>`public function recordDownload(Document $document, ?int $userId = null, ?string $ip = null): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Document.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-document-management/src/Models/Document.php) | `team_id`, `title`, `slug`, `path`, `mime_type`, `size`, `status`, `extracted_text`, `retention_until` |
| [DocumentDownload.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-document-management/src/Models/DocumentDownload.php) | `user_id`, `ip_address`, `downloaded_at` |
<!-- layer-implementation-plan:end -->
