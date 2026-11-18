# Accounting: Accounting Branch And Location Accounting Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-branch-and-location-accounting). Observed identity: [`liberusoftware/module-accounting-branch-and-location-accounting-filament`](../../../modules/source/liberusoftware--module-accounting-branch-and-location-accounting-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-branch-and-location-accounting-filament`  
**Matching domain module:** `accounting-branch-and-location-accounting`  
**Application:** Accounting  
**Source feature:** [Accounting Branch And Location Accounting](../features/accounting-branch-and-location-accounting.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-branch-and-location-accounting` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Branch/location dimensions or books:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Local sequences/tax:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Allocations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Performance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Statutory requirements:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-branch-and-location-accounting-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `branch-location-dimensions-or-books`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `local-sequences-tax`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `allocations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `performance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `statutory-requirements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-branch-and-location-accounting` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-branch-and-location-accounting-filament`](https://github.com/liberusoftware/module-accounting-branch-and-location-accounting-filament) (`liberusoftware/accounting-branch-and-location-accounting-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-branch-and-location-accounting.md) · [API plan](../api/accounting-branch-and-location-accounting.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Branch/location dimensions or books** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `branch/location dimensions or books`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Local sequences/tax** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `local sequences/tax`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Allocations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `allocations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Performance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `performance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Statutory requirements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `statutory requirements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [BranchLocationAccountingFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting-filament/src/BranchLocationAccountingFilamentPlugin.php) · [BranchLocationAccountingFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting-filament/src/BranchLocationAccountingFilamentServiceProvider.php) · [BranchResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting-filament/src/Resources/BranchResource.php) · [ListBranches.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting-filament/src/Resources/BranchResource/Pages/ListBranches.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BranchQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Queries/BranchQuery.php) | `public function forTeam(int $teamId, ?string $status = null): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateBranchValue.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Actions/AllocateBranchValue.php) | `public function handle(Branch $branch, float $amount): array` |
| [CreateBranch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Actions/CreateBranch.php) | `public function handle(array $attributes): Branch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Branch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Models/Branch.php) | `team_id`, `code`, `name`, `location`, `local_tax_code`, `sequence_prefix`, `allocation_rule`, `performance_target`, `statutory_reference`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->
