# CRM: Customer Data Platform Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customer-data-platform). Observed identity: [`liberusoftware/module-crm-customer-data-platform-filament`](../../../modules/source/liberusoftware--module-crm-customer-data-platform-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-customer-data-platform-filament`  
**Matching domain module:** `crm-customer-data-platform`  
**Application:** CRM  
**Source feature:** [Customer Data Platform](../features/customer-data-platform.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-customer-data-platform` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Source profiles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Identity resolution:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Unified profiles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audience activation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Event ingestion:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Consent-aware calculated attributes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Profile lineage:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-customer-data-platform-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `source-profiles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `identity-resolution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `unified-profiles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audience-activation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `event-ingestion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `consent-aware-calculated-attributes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `profile-lineage`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-customer-data-platform` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-customer-data-platform-filament`](https://github.com/liberusoftware/module-crm-customer-data-platform-filament) (`liberusoftware/crm-customer-data-platform-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/customer-data-platform.md) · [API plan](../api/customer-data-platform.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Source profiles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `source profiles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Identity resolution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `identity resolution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Unified profiles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `unified profiles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Audience activation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audience activation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Event ingestion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `event ingestion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Consent-aware calculated attributes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `consent-aware calculated attributes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Profile lineage** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `profile lineage`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CustomerDataPlatformFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform-filament/src/CustomerDataPlatformFilamentServiceProvider.php) · [CdpProfileResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform-filament/src/Resources/CdpProfileResource.php) · [CreateCdpProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform-filament/src/Resources/Pages/CreateCdpProfile.php) · [EditCdpProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform-filament/src/Resources/Pages/EditCdpProfile.php) · [ListCdpProfiles.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform-filament/src/Resources/Pages/ListCdpProfiles.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CdpQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Queries/CdpQuery.php) | `public function profiles(int $teamId)`<br>`public function audiences(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateCdpAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/ActivateCdpAudience.php) | `public function __construct(private readonly CdpPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CdpAudience $audience, string $destination): CdpAudience` |
| [CreateCdpAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/CreateCdpAudience.php) | `public function __construct(private readonly CdpPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CdpAudience` |
| [IngestCdpEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/IngestCdpEvent.php) | `public function execute(int $teamId, CdpProfile $profile, array $input): CdpEvent` |
| [UpsertCdpProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/UpsertCdpProfile.php) | `public function __construct(private readonly CdpPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CdpProfile` |
| [CdpPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Services/CdpPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CdpAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpAudience.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpIdentity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpIdentity.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpProfile.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
