# Accounting: VAT Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#vat). Observed identity: [`liberusoftware/module-accounting-vat-filament`](../../../modules/source/liberusoftware--module-accounting-vat-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-vat-filament`  
**Matching domain module:** `accounting-vat`  
**Application:** Accounting  
**Source feature:** [VAT](../features/vat.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-vat` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Input/output VAT:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reverse charge:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Partial exemption hooks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Import/export:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schemes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Boxes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Adjustments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Digital records:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audit trail:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-vat-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `input-output-vat`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reverse-charge`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `partial-exemption-hooks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `import-export`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schemes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `boxes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `adjustments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `digital-records`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audit-trail`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-vat` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-vat-filament`](https://github.com/liberusoftware/module-accounting-vat-filament) (`liberusoftware/accounting-vat-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/vat.md) · [API plan](../api/vat.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Input/output VAT** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `input/output vat`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reverse charge** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reverse charge`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Partial exemption hooks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `partial exemption hooks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Import/export** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `import/export`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schemes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schemes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Boxes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `boxes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Adjustments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `adjustments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Digital records** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `digital records`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Audit trail** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `audit trail`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ListVatRecords.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat-filament/src/Resources/Pages/ListVatRecords.php) · [ListVatReturns.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat-filament/src/Resources/Pages/ListVatReturns.php) · [VatRecordResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat-filament/src/Resources/VatRecordResource.php) · [VatReturnResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat-filament/src/Resources/VatReturnResource.php) · [VatFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat-filament/src/VatFilamentPlugin.php) · [VatFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat-filament/src/VatFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [VatReturnBoxes.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Queries/VatReturnBoxes.php) | `public function handle(VatReturn $vatReturn): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddVatAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Actions/AddVatAdjustment.php) | `public function handle(VatReturn $vatReturn, array $attributes): VatAdjustment` |
| [CreateVatReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Actions/CreateVatReturn.php) | `public function handle(array $attributes): VatReturn` |
| [RecordVatDigitalEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Actions/RecordVatDigitalEvidence.php) | `public function handle(VatRecord $vatRecord, array $payload): VatDigitalRecord` |
| [RecordVatTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Actions/RecordVatTransaction.php) | `public function handle(array $attributes): VatRecord` |
| [SubmitVatReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Actions/SubmitVatReturn.php) | `public function handle(VatReturn $vatReturn, ?string $submissionRef = null): VatReturn` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [VatAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Models/VatAdjustment.php) | `vat_return_id`, `box`, `amount`, `reason`, `created_by` |
| [VatDigitalRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Models/VatDigitalRecord.php) | `vat_record_id`, `record_hash`, `payload`, `recorded_at` |
| [VatRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Models/VatRecord.php) | `team_id`, `direction`, `tax_code`, `net_amount`, `tax_amount`, `tax_rate`, `reverse_charge`, `scheme`, `box`, `source_type`, `source_id`, `status`, `occurred_on`, `evidence`, `metadata` |
| [VatReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-vat/src/Models/VatReturn.php) | `team_id`, `period_start`, `period_end`, `scheme`, `status`, `boxes`, `submitted_at`, `submission_ref`, `metadata` |
<!-- layer-implementation-plan:end -->
