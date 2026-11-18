# Accounting: Accounting Credit Notes And Adjustments Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-credit-notes-and-adjustments). Observed identity: [`liberusoftware/module-accounting-credit-notes-and-adjustments-filament`](../../../modules/source/liberusoftware--module-accounting-credit-notes-and-adjustments-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-credit-notes-and-adjustments-filament`  
**Matching domain module:** `accounting-credit-notes-and-adjustments`  
**Application:** Accounting  
**Source feature:** [Accounting Credit Notes And Adjustments](../features/accounting-credit-notes-and-adjustments.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-credit-notes-and-adjustments` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Full/partial credits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reasons:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Invoice allocation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Refund/store-credit references:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tax correction:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audit:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-credit-notes-and-adjustments-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `full-partial-credits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reasons`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `invoice-allocation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `refund-store-credit-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tax-correction`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audit`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-credit-notes-and-adjustments` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-credit-notes-and-adjustments-filament`](https://github.com/liberusoftware/module-accounting-credit-notes-and-adjustments-filament) (`liberusoftware/accounting-credit-notes-and-adjustments-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-credit-notes-and-adjustments.md) · [API plan](../api/accounting-credit-notes-and-adjustments.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Full/partial credits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `full/partial credits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reasons** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reasons`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Invoice allocation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `invoice allocation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Refund/store-credit references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `refund/store-credit references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tax correction** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tax correction`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Audit** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audit`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CreditNotesAndAdjustmentsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments-filament/src/CreditNotesAndAdjustmentsFilamentPlugin.php) · [CreditNotesAndAdjustmentsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments-filament/src/CreditNotesAndAdjustmentsFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CreditNoteQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Queries/CreditNoteQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateCreditNote.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Actions/AllocateCreditNote.php) | `public function handle(CreditNote $note, string $invoiceRef, float $amount): CreditNoteAllocation` |
| [ApproveCreditNote.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Actions/ApproveCreditNote.php) | `public function handle(CreditNote $note, int $actor): CreditNote` |
| [CreateCreditNote.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Actions/CreateCreditNote.php) | `public function handle(array $attributes): CreditNote` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CreditNote.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Models/CreditNote.php) | `team_id`, `customer_id`, `credit_ref`, `status`, `reason`, `currency`, `amount`, `allocated_amount`, `tax_amount`, `refund_reference`, `store_credit_reference`, `approved_by`, `approved_at`, `evidence`, `metadata` |
| [CreditNoteAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-credit-notes-and-adjustments/src/Models/CreditNoteAllocation.php) | `credit_note_id`, `team_id`, `invoice_ref`, `amount` |
<!-- layer-implementation-plan:end -->
