# CMS: Cms Content Access Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-content-access). Observed identity: [`liberusoftware/module-cms-content-access-livewire`](../../../modules/source/liberusoftware--module-cms-content-access-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-cms-content-access-livewire`  
**Matching domain module:** `cms-content-access`  
**Application:** CMS  
**Source feature:** [Cms Content Access](../features/cms-content-access.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Per-site/type/record/field visibility:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Audience rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Scheduled access:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Private links:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Content partitioning:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Preview authorization:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-cms-content-access-livewire` component namespace and service provider; use explicit aliases such as `<livewire:cmsCmsContentAccess::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `per-site-type-record-field-visibility`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `audience-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `scheduled-access`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `private-links`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `content-partitioning`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `preview-authorization`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-content-access` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/cms-content-access.md) · [API plan](../api/cms-content-access.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Per-site/type/record/field visibility** | Expose a focused Livewire 4 component and namespaced Blade default view for `per-site/type/record/field visibility` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Audience rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `audience rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Scheduled access** | Expose a focused Livewire 4 component and namespaced Blade default view for `scheduled access` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Private links** | Expose a focused Livewire 4 component and namespaced Blade default view for `private links` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Content partitioning** | Expose a focused Livewire 4 component and namespaced Blade default view for `content partitioning` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Preview authorization** | Expose a focused Livewire 4 component and namespaced Blade default view for `preview authorization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AccessChecker.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-access-livewire/src/Livewire/AccessChecker.php) · [ContentAccessLivewireServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-content-access-livewire/src/ContentAccessLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentAccessService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-access/src/Services/ContentAccessService.php) | `public function rule(string $subjectType, string $subjectKey, array $data = [], ?int $teamId = null): AccessRule`<br>`public function canAccess(string $subjectType, string $subjectKey, ?int $teamId, array $audiences = [], bool $preview = false, ?string $privateToken = null): bool`<br>`public function createPrivateLink(string $subjectType, string $subjectKey, ?int $teamId, ?int $maxUses = null): string`<br>`public function consumePrivateLink(string $token, string $subjectType, string $subjectKey, ?int $teamId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccessRule.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-access/src/Models/AccessRule.php) | `team_id`, `subject_type`, `subject_key`, `visibility`, `audiences`, `fields`, `available_from`, `available_until`, `preview_allowed` |
| [PrivateLink.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-access/src/Models/PrivateLink.php) | `team_id`, `token_hash`, `subject_type`, `subject_key`, `expires_at`, `uses`, `max_uses`, `revoked_at` |
<!-- layer-implementation-plan:end -->
