# CMS: Cms Digital Asset Management Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-digital-asset-management). Observed identity: [`liberusoftware/module-cms-digital-asset-management-filament`](../../../modules/source/liberusoftware--module-cms-digital-asset-management-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-cms-digital-asset-management-filament`  
**Matching domain module:** `cms-digital-asset-management`  
**Application:** CMS  
**Source feature:** [Cms Digital Asset Management](../features/cms-digital-asset-management.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-digital-asset-management` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Rights:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Licenses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attribution:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Consent/model releases:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Expiry:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Brand assets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Renditions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Distribution:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-cms-digital-asset-management-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `rights`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `licenses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attribution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `consent-model-releases`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `expiry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `brand-assets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `renditions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `distribution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-digital-asset-management` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-digital-asset-management-filament`](https://github.com/liberusoftware/module-cms-digital-asset-management-filament) (`liberusoftware/cms-digital-asset-management-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cms-digital-asset-management.md) · [API plan](../api/cms-digital-asset-management.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Rights** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rights`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Licenses** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `licenses`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attribution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attribution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Consent/model releases** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `consent/model releases`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Expiry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `expiry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Brand assets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `brand assets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Renditions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `renditions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approvals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approvals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Distribution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `distribution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DigitalAssetManagementFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-digital-asset-management-filament/src/DigitalAssetManagementFilamentServiceProvider.php) · [DigitalAssetResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-digital-asset-management-filament/src/Resources/DigitalAssetResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [DigitalAssetManagementService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-digital-asset-management/src/Services/DigitalAssetManagementService.php) | `public function assets(?int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function register(array $data, ?int $teamId = null): DigitalAsset`<br>`public function approve(DigitalAsset $asset): DigitalAsset`<br>`public function addRendition(DigitalAsset $asset, string $name, string $storageKey): DigitalAsset`<br>`public function distribute(DigitalAsset $asset, array $channels): DigitalAsset` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DigitalAsset.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-digital-asset-management/src/Models/DigitalAsset.php) | `team_id`, `name`, `asset_type`, `storage_key`, `license`, `attribution`, `release_reference`, `expires_at`, `renditions`, `status`, `brand_asset`, `approved`, `approved_at`, `distribution` |
<!-- layer-implementation-plan:end -->
