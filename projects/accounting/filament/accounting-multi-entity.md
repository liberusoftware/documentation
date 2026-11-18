# Accounting: Accounting Multi Entity Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-multi-entity). Observed identity: [`liberusoftware/module-accounting-multi-entity-filament`](../../../modules/source/liberusoftware--module-accounting-multi-entity-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-multi-entity-filament`  
**Matching domain module:** `accounting-multi-entity`  
**Application:** Accounting  
**Source feature:** [Accounting Multi Entity](../features/accounting-multi-entity.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-multi-entity` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Entity books:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Shared master-data policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Access:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Entity switching:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Separate periods/tax:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Standardized mappings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reporting:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-multi-entity-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `entity-books`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `shared-master-data-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `access`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `entity-switching`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `separate-periods-tax`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `standardized-mappings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reporting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-multi-entity` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-multi-entity-filament`](https://github.com/liberusoftware/module-accounting-multi-entity-filament) (`liberusoftware/accounting-multi-entity-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-multi-entity.md) · [API plan](../api/accounting-multi-entity.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Entity books** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `entity books`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Shared master-data policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `shared master-data policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Access** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `access`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Entity switching** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `entity switching`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Separate periods/tax** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `separate periods/tax`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Standardized mappings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `standardized mappings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reporting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reporting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MultiEntityFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity-filament/src/MultiEntityFilamentPlugin.php) · [MultiEntityFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity-filament/src/MultiEntityFilamentServiceProvider.php) · [EntityBookResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity-filament/src/Resources/EntityBookResource.php) · [ListEntityBooks.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-entity-filament/src/Resources/Pages/ListEntityBooks.php).

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
