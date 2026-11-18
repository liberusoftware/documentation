# Accounting: Liberu Business Workflow Reconciliation Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#liberu-business-workflow-reconciliation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-liberu-business-workflow-reconciliation-filament`  
**Matching domain module:** `liberu-business-workflow-reconciliation`  
**Application:** Accounting  
**Source feature:** [Liberu Business Workflow Reconciliation](../features/liberu-business-workflow-reconciliation.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `liberu-business-workflow-reconciliation` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Workflow run registry:** resource/table/form/action or page behavior for this module's authorized workflow.
- **State mapping:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recovery coordination:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audit timeline:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-liberu-business-workflow-reconciliation-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `workflow-run-registry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `state-mapping`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recovery-coordination`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audit-timeline`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `liberu-business-workflow-reconciliation` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-module-liberu-business-workflow-reconciliation-3b42eab6-filament`](https://github.com/liberusoftware/module-module-liberu-business-workflow-reconciliation-3b42eab6-filament) (`liberusoftware/module-liberu-business-workflow-reconciliation-3b42eab6-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/liberu-business-workflow-reconciliation.md) · [API plan](../api/liberu-business-workflow-reconciliation.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Workflow run registry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `workflow run registry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **State mapping** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `state mapping`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recovery coordination** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recovery coordination`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Audit timeline** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audit timeline`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateReconciliationCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation/src/Actions/CreateReconciliationCase.php) | `public function execute(array $attributes): ReconciliationCase` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorkflowRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-business-workflow-reconciliation/src/Models/WorkflowRun.php) | `team_id`, `correlation_id`, `workflow_key`, `contract_version`, `state`, `steps`, `last_error` |
<!-- layer-implementation-plan:end -->
