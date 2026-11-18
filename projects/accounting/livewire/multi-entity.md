# Accounting: Multi-Entity Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#multi-entity). Observed identity: [`liberusoftware/module-accounting-multi-entity-livewire`](../../../modules/source/liberusoftware--module-accounting-multi-entity-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-multi-entity-livewire`  
**Matching domain module:** `accounting-multi-entity`  
**Application:** Accounting  
**Source feature:** [Multi-Entity](../features/multi-entity.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Entity books:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Shared master-data policy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Access:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Entity switching:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Separate periods/tax:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Standardized mappings:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reporting:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-multi-entity-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-multi-entity::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `entity-books`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `shared-master-data-policy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `access`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `entity-switching`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `separate-periods-tax`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `standardized-mappings`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reporting`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-multi-entity` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/multi-entity.md) · [API plan](../api/multi-entity.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Entity books** | Expose a focused Livewire 4 component and namespaced Blade default view for `entity books` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Shared master-data policy** | Expose a focused Livewire 4 component and namespaced Blade default view for `shared master-data policy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Access** | Expose a focused Livewire 4 component and namespaced Blade default view for `access` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Entity switching** | Expose a focused Livewire 4 component and namespaced Blade default view for `entity switching` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Separate periods/tax** | Expose a focused Livewire 4 component and namespaced Blade default view for `separate periods/tax` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Standardized mappings** | Expose a focused Livewire 4 component and namespaced Blade default view for `standardized mappings` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reporting** | Expose a focused Livewire 4 component and namespaced Blade default view for `reporting` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [EntityBooks.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity-livewire/src/Livewire/EntityBooks.php) · [MultiEntityLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity-livewire/src/MultiEntityLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [EntityQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Queries/EntityQuery.php) | `public function paginate(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function report(EntityBook $entity): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateEntityBook.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/CreateEntityBook.php) | `public function handle(array $attributes): EntityBook` |
| [CreateEntityMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/CreateEntityMapping.php) | `public function handle(EntityBook $entity, string $type, string $source, string $target): EntityMapping` |
| [CreateEntityPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/CreateEntityPeriod.php) | `public function handle(EntityBook $entity, array $attributes): EntityPeriod` |
| [GrantEntityAccess.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/GrantEntityAccess.php) | `public function handle(EntityBook $entity, string $userRef, string $role, array $permissions = [], bool $default = false): EntityAccess` |
| [SetMasterDataPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/SetMasterDataPolicy.php) | `public function handle(EntityBook $entity, string $key, string $mode, array $configuration = []): MasterDataPolicy` |
| [SwitchEntity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Actions/SwitchEntity.php) | `public function handle(EntityBook $entity, string $userRef, string $sessionRef): EntitySwitch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EntityAccess.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntityAccess.php) | `entity_id`, `user_ref`, `role`, `permissions`, `is_default`, `metadata` |
| [EntityBook.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntityBook.php) | `team_id`, `entity_ref`, `code`, `name`, `base_currency`, `timezone`, `tax_registration`, `status`, `metadata` |
| [EntityMapping.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntityMapping.php) | `entity_id`, `mapping_type`, `source_ref`, `target_ref`, `description`, `is_active`, `metadata` |
| [EntityPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntityPeriod.php) | `entity_id`, `period_ref`, `starts_on`, `ends_on`, `tax_configuration`, `status`, `closed_by`, `closed_at`, `metadata` |
| [EntitySwitch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/EntitySwitch.php) | `entity_id`, `user_ref`, `session_ref`, `switched_at`, `metadata` |
| [MasterDataPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity/src/Models/MasterDataPolicy.php) | `entity_id`, `policy_key`, `mode`, `configuration`, `metadata` |
<!-- layer-implementation-plan:end -->
