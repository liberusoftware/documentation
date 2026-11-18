# CRM: Data Operations Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#data-operations). Observed identity: [`liberusoftware/module-crm-data-operations-livewire`](../../../modules/source/liberusoftware--module-crm-data-operations-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-data-operations-livewire`  
**Matching domain module:** `crm-data-operations`  
**Application:** CRM  
**Source feature:** [Data Operations](../features/data-operations.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Imports/exports:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Field mapping:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Normalization:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Enrichment orchestration:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Duplicate detection/merge:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Formatting:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quality rules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exception queues:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-data-operations-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-data-operations::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `imports-exports`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `field-mapping`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `normalization`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `enrichment-orchestration`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `duplicate-detection-merge`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `formatting`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quality-rules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exception-queues`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-data-operations` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/data-operations.md) · [API plan](../api/data-operations.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Imports/exports** | Expose a focused Livewire 4 component and namespaced Blade default view for `imports/exports` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Field mapping** | Expose a focused Livewire 4 component and namespaced Blade default view for `field mapping` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Normalization** | Expose a focused Livewire 4 component and namespaced Blade default view for `normalization` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Enrichment orchestration** | Expose a focused Livewire 4 component and namespaced Blade default view for `enrichment orchestration` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Duplicate detection/merge** | Expose a focused Livewire 4 component and namespaced Blade default view for `duplicate detection/merge` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Formatting** | Expose a focused Livewire 4 component and namespaced Blade default view for `formatting` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Quality rules** | Expose a focused Livewire 4 component and namespaced Blade default view for `quality rules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Schedules** | Expose a focused Livewire 4 component and namespaced Blade default view for `schedules` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Exception queues** | Expose a focused Livewire 4 component and namespaced Blade default view for `exception queues` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [OperationBrowser.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations-livewire/src/Components/OperationBrowser.php) · [DataOperationsLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations-livewire/src/DataOperationsLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDataOperation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Actions/CreateDataOperation.php) | `public function execute(int $teamId, ?int $actorId, array $attributes, array $mappings = []): DataOperation` |
| [ResolveException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Actions/ResolveException.php) | `public function execute(OperationException $exception, int $actorId): OperationException` |
| [TransitionDataOperation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Actions/TransitionDataOperation.php) | `public function execute(DataOperation $operation, string $status, ?string $reason = null): DataOperation` |
| [DataOperationService.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Services/DataOperationService.php) | `public function mapAndNormalize(array $row, array $mapping): array`<br>`public function duplicateConfidence(array $left, array $right, array $fields): float` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DataOperation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/DataOperation.php) | `team_id`, `actor_id`, `kind`, `status`, `source`, `target`, `options`, `total_rows`, `processed_rows`, `failed_rows`, `failure_reason`, `started_at`, `completed_at` |
| [DuplicateMatch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/DuplicateMatch.php) | `team_id`, `operation_id`, `left_record_id`, `right_record_id`, `confidence`, `status` |
| [FieldMapping.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/FieldMapping.php) | `operation_id`, `source_field`, `target_field`, `transform`, `required` |
| [OperationException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/OperationException.php) | `team_id`, `operation_id`, `row_number`, `payload`, `reason`, `status`, `resolved_by`, `resolved_at` |
| [OperationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/OperationRule.php) | `team_id`, `name`, `kind`, `definition`, `active` |
| [OperationSchedule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/OperationSchedule.php) | `team_id`, `operation_id`, `cron`, `timezone`, `active`, `next_run_at` |
<!-- layer-implementation-plan:end -->
