# CRM: Crm Prospecting Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-prospecting). Observed identity: [`liberusoftware/module-crm-prospecting-filament`](../../../modules/source/liberusoftware--module-crm-prospecting-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-prospecting-filament`  
**Matching domain module:** `crm-prospecting`  
**Application:** CRM  
**Source feature:** [Crm Prospecting](../features/crm-prospecting.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-prospecting` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Ideal-customer profiles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Prospect searches:** resource/table/form/action or page behavior for this module's authorized workflow.
- **List building:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Research queues:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contact reveal/credits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provider provenance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Compliant export/outreach handoff:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-prospecting-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `ideal-customer-profiles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `prospect-searches`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `list-building`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `research-queues`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contact-reveal-credits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provider-provenance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `compliant-export-outreach-handoff`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-prospecting` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-prospecting-filament`](https://github.com/liberusoftware/module-crm-prospecting-filament) (`liberusoftware/crm-prospecting-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-prospecting.md) · [API plan](../api/crm-prospecting.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Ideal-customer profiles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ideal-customer profiles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Prospect searches** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `prospect searches`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **List building** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `list building`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Research queues** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `research queues`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Contact reveal/credits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `contact reveal/credits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provider provenance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider provenance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Compliant export/outreach handoff** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `compliant export/outreach handoff`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ProspectingFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-filament/src/ProspectingFilamentPlugin.php) · [ProspectingFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-filament/src/ProspectingFilamentServiceProvider.php) · [ProspectResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-filament/src/Resources/ProspectResource.php) · [CreateProspect.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-filament/src/Resources/ProspectResource/Pages/CreateProspect.php) · [EditProspect.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-filament/src/Resources/ProspectResource/Pages/EditProspect.php) · [ListProspects.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-filament/src/Resources/ProspectResource/Pages/ListProspects.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ProspectingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Queries/ProspectingQuery.php) | `public function profiles(int $teamId)`<br>`public function searches(int $teamId)`<br>`public function prospects(int $teamId)`<br>`public function queue(int $teamId)`<br>`public function exports(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateIdealCustomerProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/CreateIdealCustomerProfile.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): IdealCustomerProfile` |
| [CreateProspectSearch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/CreateProspectSearch.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectSearch` |
| [ImportProspect.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/ImportProspect.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Prospect` |
| [QueueExport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/QueueExport.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectExport` |
| [QueueResearch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/QueueResearch.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectResearchItem` |
| [RevealContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/RevealContact.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProspectCredit` |
| [UpdateProspect.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Actions/UpdateProspect.php) | `public function __construct(private readonly ProspectingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $prospectId, array $input): Prospect` |
| [ProspectingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Services/ProspectingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [IdealCustomerProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/IdealCustomerProfile.php) | No literal fillable array detected; inspect the model and API schema. |
| [Prospect.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/Prospect.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectCredit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectCredit.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectExport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectExport.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectResearchItem.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectResearchItem.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProspectSearch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting/src/Models/ProspectSearch.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
