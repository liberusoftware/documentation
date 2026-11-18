# CRM: Dialer and Outreach Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#dialer-and-outreach). Observed identity: [`liberusoftware/module-crm-dialer-and-outreach-filament`](../../../modules/source/liberusoftware--module-crm-dialer-and-outreach-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-dialer-and-outreach-filament`  
**Matching domain module:** `crm-dialer-and-outreach`  
**Application:** CRM  
**Source feature:** [Dialer and Outreach](../features/dialer-and-outreach.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-dialer-and-outreach` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Power/preview/progressive dialing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Prioritized lists:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Scripts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Local-time policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Retries:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Voicemail drop:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Answer detection adapters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Outcomes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Compliance controls:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-dialer-and-outreach-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `power-preview-progressive-dialing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `prioritized-lists`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `scripts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `local-time-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `retries`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `voicemail-drop`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `answer-detection-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `outcomes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `compliance-controls`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-dialer-and-outreach` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-dialer-and-outreach-filament`](https://github.com/liberusoftware/module-crm-dialer-and-outreach-filament) (`liberusoftware/crm-dialer-and-outreach-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/dialer-and-outreach.md) · [API plan](../api/dialer-and-outreach.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Power/preview/progressive dialing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `power/preview/progressive dialing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Prioritized lists** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `prioritized lists`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Scripts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `scripts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Local-time policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `local-time policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Retries** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `retries`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Voicemail drop** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `voicemail drop`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Answer detection adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `answer detection adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Outcomes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `outcomes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Compliance controls** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `compliance controls`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DialerAndOutreachFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach-filament/src/DialerAndOutreachFilamentServiceProvider.php) · [DialerListResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach-filament/src/Resources/DialerListResource.php) · [CreateDialerList.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach-filament/src/Resources/Pages/CreateDialerList.php) · [EditDialerList.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach-filament/src/Resources/Pages/EditDialerList.php) · [ListDialerLists.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach-filament/src/Resources/Pages/ListDialerLists.php).

| Observed core query | Public method signatures |
| --- | --- |
| [DialerQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Queries/DialerQuery.php) | `public function lists(int $teamId)`<br>`public function calls(int $teamId, int $listId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDialerList.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Actions/CreateDialerList.php) | `public function __construct(private readonly DialerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): DialerList` |
| [QueueDialerCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Actions/QueueDialerCall.php) | `public function __construct(private readonly DialerPolicy $policy)`<br>`public function execute(int $teamId, int $userId, DialerList $list, array $input): DialerCall` |
| [RecordCallOutcome.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Actions/RecordCallOutcome.php) | `public function execute(int $teamId, int $userId, DialerCall $call, array $input): DialerEvent` |
| [RetryDialerCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Actions/RetryDialerCall.php) | `public function execute(int $teamId, DialerCall $call, int $maxAttempts = 3): DialerCall` |
| [DialerPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Services/DialerPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DialerCall.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Models/DialerCall.php) | No literal fillable array detected; inspect the model and API schema. |
| [DialerEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Models/DialerEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [DialerList.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-dialer-and-outreach/src/Models/DialerList.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
