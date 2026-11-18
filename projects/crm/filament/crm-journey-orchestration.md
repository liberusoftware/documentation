# CRM: Crm Journey Orchestration Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-journey-orchestration). Observed identity: [`liberusoftware/module-crm-journey-orchestration-filament`](../../../modules/source/liberusoftware--module-crm-journey-orchestration-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-journey-orchestration-filament`  
**Matching domain module:** `crm-journey-orchestration`  
**Application:** CRM  
**Source feature:** [Crm Journey Orchestration](../features/crm-journey-orchestration.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-journey-orchestration` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Triggered/scheduled journeys:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Branching:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Waits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Goals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Re-entry:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Suppression:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Frequency caps:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Experiments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Stop-on-response:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Versioned publication:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-journey-orchestration-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `triggered-scheduled-journeys`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `branching`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `waits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `goals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `re-entry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `suppression`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `frequency-caps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `experiments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `stop-on-response`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `versioned-publication`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-journey-orchestration` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-journey-orchestration-filament`](https://github.com/liberusoftware/module-crm-journey-orchestration-filament) (`liberusoftware/crm-journey-orchestration-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-journey-orchestration.md) · [API plan](../api/crm-journey-orchestration.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Triggered/scheduled journeys** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `triggered/scheduled journeys`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Branching** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `branching`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Waits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `waits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Goals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `goals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Re-entry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `re-entry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Suppression** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `suppression`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Frequency caps** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `frequency caps`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Experiments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `experiments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Stop-on-response** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `stop-on-response`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Versioned publication** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `versioned publication`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [JourneyOrchestrationFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration-filament/src/JourneyOrchestrationFilamentServiceProvider.php) · [JourneyResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration-filament/src/Resources/JourneyResource.php) · [CreateJourney.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration-filament/src/Resources/Pages/CreateJourney.php) · [EditJourney.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration-filament/src/Resources/Pages/EditJourney.php) · [ListJourneys.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration-filament/src/Resources/Pages/ListJourneys.php).

| Observed core query | Public method signatures |
| --- | --- |
| [JourneyQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Queries/JourneyQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateJourney.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Actions/CreateJourney.php) | `public function __construct(private readonly JourneyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Journey` |
| [PublishJourney.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Actions/PublishJourney.php) | `public function __construct(private readonly JourneyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Journey $journey, array $input): Journey` |
| [StartJourneyRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Actions/StartJourneyRun.php) | `public function __construct(private readonly JourneyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Journey $journey, array $input): JourneyRun` |
| [StopJourneyRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Actions/StopJourneyRun.php) | `public function __construct(private readonly JourneyPolicy $policy)`<br>`public function execute(int $teamId, int $userId, JourneyRun $run, array $input): JourneyEvent` |
| [JourneyPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Services/JourneyPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Journey.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Models/Journey.php) | No literal fillable array detected; inspect the model and API schema. |
| [JourneyEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Models/JourneyEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [JourneyRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-journey-orchestration/src/Models/JourneyRun.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
