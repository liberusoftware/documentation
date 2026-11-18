# Accounting: Accounting Document Capture Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-document-capture). Observed identity: [`liberusoftware/module-accounting-document-capture-filament`](../../../modules/source/liberusoftware--module-accounting-document-capture-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-document-capture-filament`  
**Matching domain module:** `accounting-document-capture`  
**Application:** Accounting  
**Source feature:** [Accounting Document Capture](../features/accounting-document-capture.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-document-capture` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Mobile/web/email upload:** resource/table/form/action or page behavior for this module's authorized workflow.
- **OCR/extraction adapters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Supplier matching:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Line/tax capture:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Confidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Duplicate checks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Review:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Source retention:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-document-capture-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `mobile-web-email-upload`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ocr-extraction-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `supplier-matching`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `line-tax-capture`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `confidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `duplicate-checks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `review`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `source-retention`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-document-capture` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-document-capture-filament`](https://github.com/liberusoftware/module-accounting-document-capture-filament) (`liberusoftware/accounting-document-capture-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-document-capture.md) · [API plan](../api/accounting-document-capture.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Mobile/web/email upload** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `mobile/web/email upload`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **OCR/extraction adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ocr/extraction adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Supplier matching** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `supplier matching`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Line/tax capture** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `line/tax capture`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Confidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `confidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Duplicate checks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `duplicate checks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Review** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `review`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Source retention** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `source retention`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [DocumentCaptureFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture-filament/src/DocumentCaptureFilamentPlugin.php) · [DocumentCaptureFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture-filament/src/DocumentCaptureFilamentServiceProvider.php) · [CapturedDocumentResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture-filament/src/Resources/CapturedDocumentResource.php) · [ListCapturedDocuments.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture-filament/src/Resources/Pages/ListCapturedDocuments.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CaptureQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Queries/CaptureQuery.php) | `public function paginate(?int $teamId = null, ?CaptureStatus $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/ArchiveDocument.php) | `public function handle(CapturedDocument $d, ?string $actor = null): CapturedDocument` |
| [ExtractDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/ExtractDocument.php) | `public function handle(CapturedDocument $d, array $extracted, float $confidence, string $adapter, ?string $actor = null): CapturedDocument` |
| [MarkDuplicateDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/MarkDuplicateDocument.php) | `public function handle(CapturedDocument $d, CapturedDocument $original, ?string $actor = null): CapturedDocument` |
| [ReviewDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/ReviewDocument.php) | `public function handle(CapturedDocument $d, bool $approved, ?string $reason = null, ?string $actor = null): CapturedDocument` |
| [UploadDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Actions/UploadDocument.php) | `public function handle(array $a): CapturedDocument` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CaptureEvent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Models/CaptureEvent.php) | `document_id`, `event`, `actor_ref`, `adapter_ref`, `message`, `metadata` |
| [CapturedDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture/src/Models/CapturedDocument.php) | `team_id`, `source_channel`, `file_ref`, `checksum`, `mime_type`, `status`, `supplier_ref`, `document_ref`, `extracted_data`, `confidence`, `duplicate_of`, `retention_until`, `reviewed_by`, `reviewed_at`, `rejection_reason`, `metadata` |
| [Document.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-document-capture-api/src/Models/Document.php) | `documentable_type`, `documentable_id`, `name`, `disk`, `retention_until`, `team_id` |
<!-- layer-implementation-plan:end -->
