# Maintenance: Module Maintenance Procurement Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-procurement). Observed identity: [`liberusoftware/module-maintenance-procurement-filament`](../../../modules/source/liberusoftware--module-maintenance-procurement-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-maintenance-module-maintenance-procurement-filament`  
**Matching domain module:** `module-maintenance-procurement`  
**Application:** Maintenance  
**Source feature:** [Module Maintenance Procurement](../features/module-maintenance-procurement.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-maintenance-procurement` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Suppliers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Requests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Purchase orders:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Receipts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Returns:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cost allocation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-maintenance-module-maintenance-procurement-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `suppliers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `requests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `purchase-orders`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `receipts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `returns`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cost-allocation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-maintenance-procurement` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-maintenance-procurement-filament`](https://github.com/liberusoftware/module-maintenance-procurement-filament) (`liberusoftware/maintenance-procurement-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-maintenance-procurement.md) · [API plan](../api/module-maintenance-procurement.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Suppliers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `suppliers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Requests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `requests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approvals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approvals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Purchase orders** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `purchase orders`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Receipts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `receipts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Returns** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `returns`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cost allocation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cost allocation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ProcurementFilamentPlugin.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-filament/src/ProcurementFilamentPlugin.php) · [ProcurementFilamentServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-filament/src/ProcurementFilamentServiceProvider.php) · [PurchaseRequestResource.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-filament/src/Resources/PurchaseRequestResource.php) · [CreatePurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-filament/src/Resources/PurchaseRequestResource/Pages/CreatePurchaseRequest.php) · [EditPurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-filament/src/Resources/PurchaseRequestResource/Pages/EditPurchaseRequest.php) · [ListPurchaseRequests.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-filament/src/Resources/PurchaseRequestResource/Pages/ListPurchaseRequests.php) · [VendorContractResource.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-filament/src/Resources/VendorContractResource.php) · [CreateVendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-filament/src/Resources/VendorContractResource/Pages/CreateVendorContract.php) · [EditVendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-filament/src/Resources/VendorContractResource/Pages/EditVendorContract.php) · [ListVendorContracts.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-filament/src/Resources/VendorContractResource/Pages/ListVendorContracts.php) · [VendorEvaluationResource.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-filament/src/Resources/VendorEvaluationResource.php) · [CreateVendorEvaluation.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-filament/src/Resources/VendorEvaluationResource/Pages/CreateVendorEvaluation.php) · [EditVendorEvaluation.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-filament/src/Resources/VendorEvaluationResource/Pages/EditVendorEvaluation.php) · [ListVendorEvaluations.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-filament/src/Resources/VendorEvaluationResource/Pages/ListVendorEvaluations.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApprovePurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/ApprovePurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request, int $approverId): PurchaseRequest` |
| [CreatePurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/CreatePurchaseRequest.php) | `public function handle(int $teamId, array $attributes): PurchaseRequest` |
| [CreateVendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/CreateVendorContract.php) | `public function handle(int $teamId, array $attributes): VendorContract` |
| [CreateVendorPerformanceEvaluation.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/CreateVendorPerformanceEvaluation.php) | `public function handle(int $teamId, array $attributes): VendorPerformanceEvaluation` |
| [DeletePurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/DeletePurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request): void` |
| [DeleteVendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/DeleteVendorContract.php) | `public function handle(int $teamId, VendorContract $contract): void` |
| [DeleteVendorPerformanceEvaluation.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/DeleteVendorPerformanceEvaluation.php) | `public function handle(int $teamId, VendorPerformanceEvaluation $evaluation): void` |
| [RejectPurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/RejectPurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request, int $approverId, ?string $reason = null): PurchaseRequest` |
| [TransitionPurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/TransitionPurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request, string $status, ?int $actorId = null): PurchaseRequest` |
| [TransitionVendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/TransitionVendorContract.php) | `public function handle(int $teamId, VendorContract $contract, string $status): VendorContract` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/PurchaseRequest.php) | `team_id`, `supplier_name`, `title`, `description`, `amount`, `currency`, `status`, `requested_by`, `approved_by`, `metadata` |
| [VendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/VendorContract.php) | `team_id`, `vendor_name`, `contract_number`, `title`, `description`, `contract_type`, `start_date`, `end_date`, `contract_value`, `currency`, `status`, `auto_renewal`, `renewal_date`, `notes`, `metadata` |
| [VendorPerformanceEvaluation.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/VendorPerformanceEvaluation.php) | `team_id`, `vendor_contract_id`, `vendor_name`, `evaluation_date`, `evaluated_by`, `quality_rating`, `timeliness_rating`, `communication_rating`, `cost_effectiveness_rating`, `professionalism_rating`, `overall_rating`, `strengths`, `areas_for_improvement`, `comments`, `would_recommend` |
<!-- layer-implementation-plan:end -->
