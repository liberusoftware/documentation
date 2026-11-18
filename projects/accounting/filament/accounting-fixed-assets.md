# Accounting: Accounting Fixed Assets Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-fixed-assets). Observed identity: [`liberusoftware/module-accounting-fixed-assets-filament`](../../../modules/source/liberusoftware--module-accounting-fixed-assets-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-fixed-assets-filament`  
**Matching domain module:** `accounting-fixed-assets`  
**Application:** Accounting  
**Source feature:** [Accounting Fixed Assets](../features/accounting-fixed-assets.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-fixed-assets` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Asset register:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Categories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Acquisition:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Capitalization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Components:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Locations/custodians:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Books:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Supporting documents:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-fixed-assets-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `asset-register`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `categories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `acquisition`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `capitalization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `components`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `locations-custodians`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `books`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `supporting-documents`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-fixed-assets` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-fixed-assets-filament`](https://github.com/liberusoftware/module-accounting-fixed-assets-filament) (`liberusoftware/accounting-fixed-assets-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-fixed-assets.md) · [API plan](../api/accounting-fixed-assets.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Asset register** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `asset register`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Categories** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `categories`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Acquisition** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `acquisition`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Capitalization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `capitalization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Components** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `components`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Locations/custodians** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `locations/custodians`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Books** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `books`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Supporting documents** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `supporting documents`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [FixedAssetsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets-filament/src/FixedAssetsFilamentPlugin.php) · [FixedAssetsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets-filament/src/FixedAssetsFilamentServiceProvider.php) · [AssetResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets-filament/src/Resources/AssetResource.php) · [ListAssets.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets-filament/src/Resources/Pages/ListAssets.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AssetQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Queries/AssetQuery.php) | `public function paginate(?int $teamId = null, ?AssetStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function registerSummary(Asset $asset): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AcquireAsset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AcquireAsset.php) | `public function handle(AssetCategory $category, array $attributes): Asset` |
| [AddAssetComponent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AddAssetComponent.php) | `public function handle(Asset $asset, array $attributes): AssetComponent` |
| [AddAssetDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AddAssetDocument.php) | `public function handle(Asset $asset, array $attributes): AssetDocument` |
| [ArchiveAsset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/ArchiveAsset.php) | `public function handle(Asset $asset): Asset` |
| [AssignAssetCustodian.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AssignAssetCustodian.php) | `public function handle(Asset $asset, AssetCustodian $custodian): Asset` |
| [AssignAssetLocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AssignAssetLocation.php) | `public function handle(Asset $asset, AssetLocation $location): Asset` |
| [CapitalizeAsset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CapitalizeAsset.php) | `public function handle(Asset $asset, string $bookReference): Asset` |
| [CreateCategory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CreateCategory.php) | `public function handle(array $attributes): AssetCategory` |
| [CreateCustodian.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CreateCustodian.php) | `public function handle(array $attributes): AssetCustodian` |
| [CreateLocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CreateLocation.php) | `public function handle(array $attributes): AssetLocation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Asset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/Asset.php) | `team_id`, `asset_ref`, `name`, `category_id`, `status`, `acquired_on`, `capitalized_on`, `cost`, `salvage_value`, `net_book_value`, `currency`, `location_id`, `custodian_id`, `location_ref`, `custodian_ref`, `metadata` |
| [AssetBook.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetBook.php) | `asset_id`, `book_ref`, `cost`, `accumulated_depreciation`, `net_book_value`, `last_depreciated_on`, `metadata` |
| [AssetCategory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetCategory.php) | `team_id`, `category_ref`, `name`, `asset_account_ref`, `depreciation_account_ref`, `useful_life_months`, `depreciation_method`, `metadata` |
| [AssetComponent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetComponent.php) | `asset_id`, `component_ref`, `name`, `cost`, `useful_life_months`, `metadata` |
| [AssetCustodian.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetCustodian.php) | `team_id`, `custodian_ref`, `name`, `email`, `metadata` |
| [AssetDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetDocument.php) | `asset_id`, `document_ref`, `kind`, `file_ref`, `description`, `checksum`, `attached_by`, `attached_at`, `metadata` |
| [AssetLocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetLocation.php) | `team_id`, `location_ref`, `name`, `metadata` |
<!-- layer-implementation-plan:end -->
