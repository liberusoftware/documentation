# CRM: Crm Contact Center Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-contact-center). Observed identity: [`liberusoftware/module-crm-contact-center-filament`](../../../modules/source/liberusoftware--module-crm-contact-center-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-contact-center-filament`  
**Matching domain module:** `crm-contact-center`  
**Application:** CRM  
**Source feature:** [Crm Contact Center](../features/crm-contact-center.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-contact-center` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Agent presence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Capacity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Skills:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Routing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Supervisor views:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Whisper/barge policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Quality review:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Workforce demand:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Queue SLA:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Overflow:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-contact-center-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `agent-presence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `capacity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `skills`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `routing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `supervisor-views`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `whisper-barge-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `quality-review`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `workforce-demand`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `queue-sla`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `overflow`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-contact-center` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-contact-center-filament`](https://github.com/liberusoftware/module-crm-contact-center-filament) (`liberusoftware/crm-contact-center-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-contact-center.md) · [API plan](../api/crm-contact-center.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Agent presence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `agent presence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Capacity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `capacity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Skills** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `skills`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Routing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `routing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Supervisor views** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `supervisor views`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Whisper/barge policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `whisper/barge policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Quality review** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quality review`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Workforce demand** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `workforce demand`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Queue SLA** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `queue sla`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Overflow** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `overflow`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ContactCenterFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center-filament/src/ContactCenterFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ContactCenterQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Queries/ContactCenterQuery.php) | `public function agents(int $teamId): Builder`<br>`public function supervisorView(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ReviewQuality.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Actions/ReviewQuality.php) | `public function execute(int $teamId, int $eventId, int $reviewerId, array $scorecard): ContactCenterEvent` |
| [RouteInteraction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Actions/RouteInteraction.php) | `public function execute(int $teamId, string $queueKey, string $requiredSkill, int $slaSeconds = 300): ContactCenterEvent` |
| [SetAgentPresence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Actions/SetAgentPresence.php) | `public function execute(int $teamId, int $userId, string $presence, int $capacity = 1, array $skills = []): ContactCenterAgent` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContactCenterAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Models/ContactCenterAgent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ContactCenterEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-contact-center/src/Models/ContactCenterEvent.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
