# Accounting: Accounting Purchase Requisitions Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-purchase-requisitions). Observed identity: [`liberusoftware/module-accounting-purchase-requisitions-filament`](../../../modules/source/liberusoftware--module-accounting-purchase-requisitions-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-purchase-requisitions-filament`  
**Matching domain module:** `accounting-purchase-requisitions`  
**Application:** Accounting  
**Source feature:** [Accounting Purchase Requisitions](../features/accounting-purchase-requisitions.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-purchase-requisitions` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Requests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Coding:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Budgets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attachments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sourcing handoff:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conversion:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Status:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-purchase-requisitions-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `requests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `coding`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `budgets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attachments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sourcing-handoff`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conversion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-purchase-requisitions` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-purchase-requisitions-filament`](https://github.com/liberusoftware/module-accounting-purchase-requisitions-filament) (`liberusoftware/accounting-purchase-requisitions-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-purchase-requisitions.md) · [API plan](../api/accounting-purchase-requisitions.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Requests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `requests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Coding** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `coding`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Budgets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `budgets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Attachments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `attachments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approvals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approvals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sourcing handoff** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sourcing handoff`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Conversion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `conversion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PurchaseRequisitionsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions-filament/src/PurchaseRequisitionsFilamentPlugin.php) · [PurchaseRequisitionsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions-filament/src/PurchaseRequisitionsFilamentServiceProvider.php) · [PurchaseRequisitionResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions-filament/src/Resources/PurchaseRequisitionResource.php) · [ListPurchaseRequisitions.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions-filament/src/Resources/PurchaseRequisitionResource/Pages/ListPurchaseRequisitions.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateRequisition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions/src/Actions/CreateRequisition.php) | `public function handle(array $attributes): PurchaseRequisition` |
| [RecordApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions/src/Actions/RecordApproval.php) | `public function handle(PurchaseRequisition $requisition, array $attributes): RequisitionApproval` |
| [TransitionRequisition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions/src/Actions/TransitionRequisition.php) | `public function handle(PurchaseRequisition $requisition, RequisitionStatus $status, array $attributes = []): PurchaseRequisition` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PurchaseRequisition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions/src/Models/PurchaseRequisition.php) | `team_id`, `requester_ref`, `title`, `currency`, `total_amount`, `lines`, `coding`, `budget`, `attachments`, `status`, `submitted_at`, `approved_at`, `sourcing_ref`, `converted_ref`, `metadata` |
| [RequisitionApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-requisitions/src/Models/RequisitionApproval.php) | `requisition_id`, `approver_ref`, `decision`, `reason`, `decided_at`, `metadata` |
<!-- layer-implementation-plan:end -->
