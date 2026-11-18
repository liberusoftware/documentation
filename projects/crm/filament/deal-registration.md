# CRM: Deal Registration Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#deal-registration). Observed identity: [`liberusoftware/module-crm-deal-registration-filament`](../../../modules/source/liberusoftware--module-crm-deal-registration-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-deal-registration-filament`  
**Matching domain module:** `crm-deal-registration`  
**Application:** CRM  
**Source feature:** [Deal Registration](../features/deal-registration.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-deal-registration` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Partner-submitted leads/deals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Duplicate/conflict checks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Territory rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Protection windows:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Collaboration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attribution:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-deal-registration-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `partner-submitted-leads-deals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `duplicate-conflict-checks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `territory-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `protection-windows`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `collaboration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attribution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-deal-registration` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-deal-registration-filament`](https://github.com/liberusoftware/module-crm-deal-registration-filament) (`liberusoftware/crm-deal-registration-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/deal-registration.md) · [API plan](../api/deal-registration.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Partner-submitted leads/deals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `partner-submitted leads/deals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Duplicate/conflict checks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `duplicate/conflict checks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Territory rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `territory rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Protection windows** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `protection windows`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Collaboration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `collaboration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attribution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attribution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DealRegistrationFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration-filament/src/DealRegistrationFilamentServiceProvider.php) · [DealRegistrationResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration-filament/src/Resources/DealRegistrationResource.php) · [CreateDealRegistration.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration-filament/src/Resources/Pages/CreateDealRegistration.php) · [EditDealRegistration.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration-filament/src/Resources/Pages/EditDealRegistration.php) · [ListDealRegistrations.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration-filament/src/Resources/Pages/ListDealRegistrations.php).

| Observed core query | Public method signatures |
| --- | --- |
| [DealRegistrationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Queries/DealRegistrationQuery.php) | `public function deals(int $teamId)`<br>`public function protected(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveDeal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Actions/ApproveDeal.php) | `public function __construct(private readonly DealRegistrationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, DealRegistration $deal, int $protectionDays = 90): DealRegistration` |
| [CollaborateOnDeal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Actions/CollaborateOnDeal.php) | `public function __construct(private readonly DealRegistrationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, DealRegistration $deal, array $input): DealRegistration` |
| [SubmitDeal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Actions/SubmitDeal.php) | `public function __construct(private readonly DealRegistrationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): DealRegistration` |
| [DealRegistrationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Services/DealRegistrationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DealRegistration.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Models/DealRegistration.php) | No literal fillable array detected; inspect the model and API schema. |
| [DealRegistrationEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-deal-registration/src/Models/DealRegistrationEvent.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
