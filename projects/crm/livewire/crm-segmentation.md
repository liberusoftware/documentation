# CRM: Crm Segmentation Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-segmentation). Observed identity: [`liberusoftware/module-crm-segmentation-livewire`](../../../modules/source/liberusoftware--module-crm-segmentation-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-crm-segmentation-livewire`  
**Matching domain module:** `crm-segmentation`  
**Application:** CRM  
**Source feature:** [Crm Segmentation](../features/crm-segmentation.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Static/dynamic audiences:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Nested conditions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Behavioral events:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Calculated attributes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exclusions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Estimated counts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Refresh:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Lineage:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-crm-segmentation-livewire` component namespace and service provider; use explicit aliases such as `<livewire:crmCrmSegmentation::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `static-dynamic-audiences`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `nested-conditions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `behavioral-events`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `calculated-attributes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exclusions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `estimated-counts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `refresh`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `lineage`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-segmentation` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/crm-segmentation.md) · [API plan](../api/crm-segmentation.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Static/dynamic audiences** | Expose a focused Livewire 4 component and namespaced Blade default view for `static/dynamic audiences` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Nested conditions** | Expose a focused Livewire 4 component and namespaced Blade default view for `nested conditions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Behavioral events** | Expose a focused Livewire 4 component and namespaced Blade default view for `behavioral events` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Calculated attributes** | Expose a focused Livewire 4 component and namespaced Blade default view for `calculated attributes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Exclusions** | Expose a focused Livewire 4 component and namespaced Blade default view for `exclusions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Estimated counts** | Expose a focused Livewire 4 component and namespaced Blade default view for `estimated counts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Refresh** | Expose a focused Livewire 4 component and namespaced Blade default view for `refresh` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Lineage** | Expose a focused Livewire 4 component and namespaced Blade default view for `lineage` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AudienceDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation-livewire/src/Components/AudienceDashboard.php) · [SegmentationLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation-livewire/src/SegmentationLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SegmentationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Queries/SegmentationQuery.php) | `public function audiences(int $teamId)`<br>`public function members(int $teamId, int $audienceId)`<br>`public function events(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/CreateAudience.php) | `public function execute(int $teamId, int $actorId, array $data): Audience` |
| [RecordBehaviorEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/RecordBehaviorEvent.php) | `public function execute(int $teamId, int $actorId, array $data): BehaviorEvent` |
| [RefreshAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/RefreshAudience.php) | `public function execute(int $teamId, int $actorId, int $audienceId, array $data = []): Audience` |
| [UpdateAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/UpdateAudience.php) | `public function execute(int $teamId, int $actorId, int $audienceId, array $data): Audience` |
| [SegmentationAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Services/SegmentationAudit.php) | `public function record(int $teamId, ?int $actorId, int $audienceId, string $operation, array $details = []): SegmentationLineage` |
| [SegmentationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Services/SegmentationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Audience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/Audience.php) | No literal fillable array detected; inspect the model and API schema. |
| [AudienceMember.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/AudienceMember.php) | No literal fillable array detected; inspect the model and API schema. |
| [BehaviorEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/BehaviorEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [SegmentationLineage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/SegmentationLineage.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
