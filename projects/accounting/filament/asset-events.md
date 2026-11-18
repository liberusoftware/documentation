# Accounting: Asset Events Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#asset-events). Observed identity: [`liberusoftware/module-accounting-asset-events-filament`](../../../modules/source/liberusoftware--module-accounting-asset-events-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-asset-events-filament`  
**Matching domain module:** `accounting-asset-events`  
**Application:** Accounting  
**Source feature:** [Asset Events](../features/asset-events.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-asset-events` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Transfer:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Improvement:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Revaluation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Impairment:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Disposal:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sale:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Write-off:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Gain/loss:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Complete history:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-asset-events-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `transfer`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `improvement`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `revaluation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `impairment`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `disposal`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sale`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `write-off`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `gain-loss`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `complete-history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-asset-events` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-asset-events-filament`](https://github.com/liberusoftware/module-accounting-asset-events-filament) (`liberusoftware/accounting-asset-events-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/asset-events.md) · [API plan](../api/asset-events.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Transfer** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transfer`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Improvement** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `improvement`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Revaluation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `revaluation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Impairment** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `impairment`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Disposal** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `disposal`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sale** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sale`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Write-off** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `write-off`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Gain/loss** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gain/loss`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Complete history** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `complete history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AssetEventsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events-filament/src/AssetEventsFilamentServiceProvider.php) · [AssetEventResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events-filament/src/Resources/AssetEventResource.php) · [CreateAssetEvent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events-filament/src/Resources/Pages/CreateAssetEvent.php) · [ListAssetEvents.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events-filament/src/Resources/Pages/ListAssetEvents.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AssetEventQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events/src/Queries/AssetEventQuery.php) | `public function paginate(int $teamId, ?int $assetId = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordAssetEvent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events/src/Actions/RecordAssetEvent.php) | `public function handle(array $attributes): AssetEvent` |
| [AssetEventPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events-api/src/Policies/AssetEventPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AssetEvent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events/src/Models/AssetEvent.php) | `team_id`, `asset_id`, `event_type`, `event_date`, `description`, `source_type`, `source_id`, `old_values`, `new_values`, `evidence`, `actor_id` |
| [Asset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-asset-events-api/src/Models/Asset.php) | `asset_name`, `asset_cost`, `useful_life_years`, `depreciation_method`, `salvage_value`, `acquisition_date`, `is_active` |
<!-- layer-implementation-plan:end -->
