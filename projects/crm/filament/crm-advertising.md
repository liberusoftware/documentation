# CRM: Crm Advertising Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-advertising). Observed identity: [`liberusoftware/module-crm-advertising-filament`](../../../modules/source/liberusoftware--module-crm-advertising-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-advertising-filament`  
**Matching domain module:** `crm-advertising`  
**Application:** CRM  
**Source feature:** [Crm Advertising](../features/crm-advertising.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-advertising` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Ad-account connections:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Campaign visibility:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lead-ad ingestion:** resource/table/form/action or page behavior for this module's authorized workflow.
- **CRM audiences:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Offline/server conversions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Spend/performance sync:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attribution:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-advertising-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `ad-account-connections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `campaign-visibility`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lead-ad-ingestion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `crm-audiences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `offline-server-conversions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `spend-performance-sync`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attribution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-advertising` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-advertising-filament`](https://github.com/liberusoftware/module-crm-advertising-filament) (`liberusoftware/crm-advertising-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-advertising.md) · [API plan](../api/crm-advertising.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Ad-account connections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ad-account connections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Campaign visibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `campaign visibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lead-ad ingestion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lead-ad ingestion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **CRM audiences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `crm audiences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Offline/server conversions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `offline/server conversions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Spend/performance sync** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `spend/performance sync`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attribution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attribution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AdvertisingFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising-filament/src/AdvertisingFilamentPlugin.php) · [AdvertisingFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising-filament/src/AdvertisingFilamentServiceProvider.php) · [AdvertisingRecordResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising-filament/src/Resources/AdvertisingRecordResource.php) · [CreateAdvertisingRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising-filament/src/Resources/Pages/CreateAdvertisingRecord.php) · [EditAdvertisingRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising-filament/src/Resources/Pages/EditAdvertisingRecord.php) · [ListAdvertisingRecords.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising-filament/src/Resources/Pages/ListAdvertisingRecords.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AdvertisingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Queries/AdvertisingQuery.php) | `public function records(int $teamId, ?string $kind = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TransitionRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Actions/TransitionRecord.php) | `public function execute(int $teamId, int $id, string $status): AdvertisingRecord` |
| [UpsertRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Actions/UpsertRecord.php) | `public function execute(int $teamId, array $attributes, ?int $id = null): AdvertisingRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AdvertisingRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Models/AdvertisingRecord.php) | `team_id`, `kind`, `name`, `status`, `external_id`, `platform`, `payload`, `starts_at`, `ends_at`, `completed_at` |
<!-- layer-implementation-plan:end -->
