# CRM: Enrichment Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#enrichment). Observed identity: [`liberusoftware/module-crm-enrichment-filament`](../../../modules/source/liberusoftware--module-crm-enrichment-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-enrichment-filament`  
**Matching domain module:** `crm-enrichment`  
**Application:** CRM  
**Source feature:** [Enrichment](../features/enrichment.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-enrichment` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Company/contact firmographic:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Demographic:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Technographic:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Social:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Verification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Change monitoring:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Confidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Field-level provenance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provider adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-enrichment-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `company-contact-firmographic`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `demographic`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `technographic`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `social`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `verification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `change-monitoring`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `confidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `field-level-provenance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provider-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-enrichment` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-enrichment-filament`](https://github.com/liberusoftware/module-crm-enrichment-filament) (`liberusoftware/crm-enrichment-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/enrichment.md) · [API plan](../api/enrichment.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Company/contact firmographic** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `company/contact firmographic`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Demographic** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `demographic`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Technographic** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `technographic`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Social** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `social`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Verification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `verification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Change monitoring** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `change monitoring`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Confidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `confidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Field-level provenance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `field-level provenance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provider adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [EnrichmentFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment-filament/src/EnrichmentFilamentServiceProvider.php) · [EnrichmentProfileResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment-filament/src/Resources/EnrichmentProfileResource.php) · [CreateEnrichmentProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment-filament/src/Resources/Pages/CreateEnrichmentProfile.php) · [EditEnrichmentProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment-filament/src/Resources/Pages/EditEnrichmentProfile.php) · [ListEnrichmentProfiles.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment-filament/src/Resources/Pages/ListEnrichmentProfiles.php).

| Observed core query | Public method signatures |
| --- | --- |
| [EnrichmentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Queries/EnrichmentQuery.php) | `public function profiles(int $teamId)`<br>`public function changes(int $teamId, int $profileId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordChange.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Actions/RecordChange.php) | `public function __construct(private readonly EnrichmentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, EnrichmentProfile $profile, array $input): EnrichmentChange` |
| [RecordProvenance.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Actions/RecordProvenance.php) | `public function __construct(private readonly EnrichmentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, EnrichmentProfile $profile, array $input): EnrichmentField` |
| [UpsertEnrichment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Actions/UpsertEnrichment.php) | `public function __construct(private readonly EnrichmentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): EnrichmentProfile` |
| [VerifyProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Actions/VerifyProfile.php) | `public function __construct(private readonly EnrichmentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, EnrichmentProfile $profile, bool $verified): EnrichmentProfile` |
| [EnrichmentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Services/EnrichmentPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EnrichmentChange.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Models/EnrichmentChange.php) | No literal fillable array detected; inspect the model and API schema. |
| [EnrichmentField.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Models/EnrichmentField.php) | No literal fillable array detected; inspect the model and API schema. |
| [EnrichmentProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-enrichment/src/Models/EnrichmentProfile.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
