# CRM: Segmentation Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#segmentation). Observed identity: [`liberusoftware/module-crm-segmentation-filament`](../../../modules/source/liberusoftware--module-crm-segmentation-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-segmentation-filament`  
**Matching domain module:** `crm-segmentation`  
**Application:** CRM  
**Source feature:** [Segmentation](../features/segmentation.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-segmentation` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Static/dynamic audiences:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Nested conditions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Behavioral events:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Calculated attributes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exclusions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Estimated counts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Refresh:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lineage:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-segmentation-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `static-dynamic-audiences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `nested-conditions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `behavioral-events`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `calculated-attributes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exclusions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `estimated-counts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `refresh`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lineage`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-segmentation` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-segmentation-filament`](https://github.com/liberusoftware/module-crm-segmentation-filament) (`liberusoftware/crm-segmentation-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/segmentation.md) · [API plan](../api/segmentation.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Static/dynamic audiences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `static/dynamic audiences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Nested conditions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `nested conditions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Behavioral events** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `behavioral events`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Calculated attributes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `calculated attributes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exclusions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exclusions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Estimated counts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `estimated counts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Refresh** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `refresh`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lineage** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lineage`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AudienceResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation-filament/src/Resources/AudienceResource.php) · [ListAudiences.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation-filament/src/Resources/AudienceResource/Pages/ListAudiences.php) · [SegmentationFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation-filament/src/SegmentationFilamentPlugin.php) · [SegmentationFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation-filament/src/SegmentationFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SegmentationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Queries/SegmentationQuery.php) | `public function audiences(int $teamId)`<br>`public function members(int $teamId, int $audienceId)`<br>`public function events(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/CreateAudience.php) | `public function execute(int $teamId, int $actorId, array $data): Audience` |
| [RecordBehaviorEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/RecordBehaviorEvent.php) | `public function execute(int $teamId, int $actorId, array $data): BehaviorEvent` |
| [RefreshAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/RefreshAudience.php) | `public function execute(int $teamId, int $actorId, int $audienceId, array $data = []): Audience` |
| [UpdateAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/UpdateAudience.php) | `public function execute(int $teamId, int $actorId, int $audienceId, array $data): Audience` |
| [SegmentationAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Services/SegmentationAudit.php) | `public function record(int $teamId, ?int $actorId, int $audienceId, string $operation, array $details = []): SegmentationLineage` |
| [SegmentationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Services/SegmentationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Audience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/Audience.php) | No literal fillable array detected; inspect the model and API schema. |
| [AudienceMember.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/AudienceMember.php) | No literal fillable array detected; inspect the model and API schema. |
| [BehaviorEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/BehaviorEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [SegmentationLineage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/SegmentationLineage.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
