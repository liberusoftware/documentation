# Accounting: Accounting Three Way Matching Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-three-way-matching). Observed identity: [`liberusoftware/module-accounting-three-way-matching-filament`](../../../modules/source/liberusoftware--module-accounting-three-way-matching-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-three-way-matching-filament`  
**Matching domain module:** `accounting-three-way-matching`  
**Application:** Accounting  
**Source feature:** [Accounting Three Way Matching](../features/accounting-three-way-matching.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-three-way-matching` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **PO/receipt/bill matching:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Quantity/price/tax tolerances:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exceptions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Partial matching:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Evidence:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-three-way-matching-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `po-receipt-bill-matching`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `quantity-price-tax-tolerances`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exceptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `partial-matching`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-three-way-matching` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-three-way-matching-filament`](https://github.com/liberusoftware/module-accounting-three-way-matching-filament) (`liberusoftware/accounting-three-way-matching-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-three-way-matching.md) · [API plan](../api/accounting-three-way-matching.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **PO/receipt/bill matching** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `po/receipt/bill matching`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Quantity/price/tax tolerances** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quantity/price/tax tolerances`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exceptions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exceptions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Partial matching** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `partial matching`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MatchRecordResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching-filament/src/Resources/MatchRecordResource.php) · [ListMatches.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching-filament/src/Resources/Pages/ListMatches.php) · [ThreeWayMatchingFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching-filament/src/ThreeWayMatchingFilamentPlugin.php) · [ThreeWayMatchingFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching-filament/src/ThreeWayMatchingFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ExceptionQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Queries/ExceptionQuery.php) | `public function open(?int $matchId = null): Collection` |
| [MatchQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Queries/MatchQuery.php) | `public function paginate(?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/ApproveMatch.php) | `public function handle(MatchRecord $match, int $actorId, ?string $overrideReason = null): MatchRecord` |
| [CaptureMatchEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/CaptureMatchEvidence.php) | `public function handle(MatchRecord $match, string $sourceType, string $sourceId, array $snapshot, ?int $actorId = null): MatchEvidence` |
| [EvaluateMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/EvaluateMatch.php) | `public function handle(array $attributes): MatchRecord` |
| [RejectMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/RejectMatch.php) | `public function handle(MatchRecord $match, string $reason): MatchRecord` |
| [ResolveMatchException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Actions/ResolveMatchException.php) | `public function handle(MatchException $exception, int $actorId, string $resolution, bool $waive = false): MatchException` |
| [ThreeWayMatchingPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching-api/src/Policies/ThreeWayMatchingPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, object $match): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, object $match): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MatchEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Models/MatchEvidence.php) | `match_id`, `source_type`, `source_id`, `snapshot_hash`, `snapshot`, `captured_by`, `metadata` |
| [MatchException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Models/MatchException.php) | `match_id`, `kind`, `severity`, `status`, `expected_value`, `actual_value`, `tolerance`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [MatchRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-three-way-matching/src/Models/MatchRecord.php) | `purchase_order_type`, `purchase_order_id`, `receipt_type`, `receipt_id`, `bill_type`, `bill_id`, `currency`, `ordered_quantity`, `received_quantity`, `billed_quantity`, `ordered_unit_price`, `billed_unit_price`, `expected_tax`, `billed_tax`, `quantity_tolerance`, `price_tolerance`, `tax_tolerance`, `status`, `approved_by`, `approved_at`, `rejected_reason`, `metadata` |
<!-- layer-implementation-plan:end -->
