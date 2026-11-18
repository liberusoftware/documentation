# CRM: Routing Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#routing). Observed identity: [`liberusoftware/module-crm-routing-filament`](../../../modules/source/liberusoftware--module-crm-routing-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-routing-filament`  
**Matching domain module:** `crm-routing`  
**Application:** CRM  
**Source feature:** [Routing](../features/routing.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-routing` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Rule:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Territory:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Skill:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Language:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Availability:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Workload:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Value:** resource/table/form/action or page behavior for this module's authorized workflow.
- **SLA:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Round-robin assignment with fallback and acceptance timers:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-routing-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `rule`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `territory`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `skill`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `language`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `availability`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `workload`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `value`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sla`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `round-robin-assignment-with-fallback-and-acceptance-timers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-routing` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-routing-filament`](https://github.com/liberusoftware/module-crm-routing-filament) (`liberusoftware/crm-routing-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/routing.md) · [API plan](../api/routing.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Rule** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rule`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Territory** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `territory`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Skill** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `skill`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Language** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `language`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Availability** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `availability`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Workload** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `workload`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Value** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `value`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **SLA** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sla`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Round-robin assignment with fallback and acceptance timers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `round-robin assignment with fallback and acceptance timers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AssignmentResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-routing-filament/src/Resources/AssignmentResource.php) · [CreateAssignment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-routing-filament/src/Resources/AssignmentResource/Pages/CreateAssignment.php) · [ListAssignments.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-routing-filament/src/Resources/AssignmentResource/Pages/ListAssignments.php) · [RoutingFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-routing-filament/src/RoutingFilamentPlugin.php) · [RoutingFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-routing-filament/src/RoutingFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [RoutingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-routing/src/Queries/RoutingQuery.php) | `public function rules(int $teamId)`<br>`public function agents(int $teamId)`<br>`public function assignments(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AcceptAssignment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-routing/src/Actions/AcceptAssignment.php) | `public function execute(int $teamId, int $actorId, int $id, string $status): RoutingAssignment` |
| [AssignSubject.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-routing/src/Actions/AssignSubject.php) | `public function execute(int $teamId, int $actorId, array $data): RoutingAssignment` |
| [CreateRoutingRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-routing/src/Actions/CreateRoutingRule.php) | `public function execute(int $teamId, int $actorId, array $data): RoutingRule` |
| [UpsertRoutingAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-routing/src/Actions/UpsertRoutingAgent.php) | `public function execute(int $teamId, int $actorId, array $data): RoutingAgent` |
| [RoutingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-routing/src/Services/RoutingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RoutingAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-routing/src/Models/RoutingAgent.php) | No literal fillable array detected; inspect the model and API schema. |
| [RoutingAssignment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-routing/src/Models/RoutingAssignment.php) | No literal fillable array detected; inspect the model and API schema. |
| [RoutingRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-routing/src/Models/RoutingRule.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
