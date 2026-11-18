# CRM: Customer Self-Service Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customer-self-service). Observed identity: [`liberusoftware/module-crm-customer-self-service-filament`](../../../modules/source/liberusoftware--module-crm-customer-self-service-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-customer-self-service-filament`  
**Matching domain module:** `crm-customer-self-service`  
**Application:** CRM  
**Source feature:** [Customer Self-Service](../features/customer-self-service.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-customer-self-service` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customer portal:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Case submission/status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Knowledge search:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Community links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Appointments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Documents:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Invoices/orders references:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Profile:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Preferences:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-customer-self-service-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `customer-portal`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `case-submission-status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `knowledge-search`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `community-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `appointments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `documents`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `invoices-orders-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `profile`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `preferences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-customer-self-service` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-customer-self-service-filament`](https://github.com/liberusoftware/module-crm-customer-self-service-filament) (`liberusoftware/crm-customer-self-service-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/customer-self-service.md) · [API plan](../api/customer-self-service.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Customer portal** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `customer portal`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Case submission/status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `case submission/status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Knowledge search** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `knowledge search`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Community links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `community links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Appointments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `appointments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Documents** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `documents`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Invoices/orders references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `invoices/orders references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Profile** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `profile`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Preferences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `preferences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CustomerSelfServiceFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service-filament/src/CustomerSelfServiceFilamentServiceProvider.php) · [CreateSelfServiceCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service-filament/src/Resources/Pages/CreateSelfServiceCase.php) · [EditSelfServiceCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service-filament/src/Resources/Pages/EditSelfServiceCase.php) · [ListSelfServiceCases.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service-filament/src/Resources/Pages/ListSelfServiceCases.php) · [SelfServiceCaseResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service-filament/src/Resources/SelfServiceCaseResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SelfServiceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Queries/SelfServiceQuery.php) | `public function profile(int $teamId, int $userId): ?SelfServiceProfile`<br>`public function cases(int $teamId, int $profileId)`<br>`public function search(int $teamId, string $term)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SubmitSelfServiceCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Actions/SubmitSelfServiceCase.php) | `public function __construct(private readonly SelfServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, SelfServiceProfile $profile, array $input): SelfServiceCase` |
| [UpdateSelfServicePreferences.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Actions/UpdateSelfServicePreferences.php) | `public function __construct(private readonly SelfServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, SelfServiceProfile $profile, array $input): SelfServiceProfile` |
| [UpsertSelfServiceProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Actions/UpsertSelfServiceProfile.php) | `public function __construct(private readonly SelfServicePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): SelfServiceProfile` |
| [SelfServicePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Services/SelfServicePolicy.php) | `public function canAccess(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SelfServiceCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceCase.php) | No literal fillable array detected; inspect the model and API schema. |
| [SelfServiceProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceProfile.php) | No literal fillable array detected; inspect the model and API schema. |
| [SelfServiceReference.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceReference.php) | No literal fillable array detected; inspect the model and API schema. |
| [SelfServiceResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-self-service/src/Models/SelfServiceResource.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
