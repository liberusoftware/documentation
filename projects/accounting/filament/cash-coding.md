# Accounting: Cash Coding Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cash-coding). Observed identity: [`liberusoftware/module-accounting-cash-coding-filament`](../../../modules/source/liberusoftware--module-accounting-cash-coding-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-cash-coding-filament`  
**Matching domain module:** `accounting-cash-coding`  
**Application:** Accounting  
**Source feature:** [Cash Coding](../features/cash-coding.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-cash-coding` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **High-volume statement coding:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bulk rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tax/dimensions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payee creation policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Review:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Posting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Undo constraints:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-cash-coding-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `high-volume-statement-coding`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bulk-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tax-dimensions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payee-creation-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `review`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `posting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `undo-constraints`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-cash-coding` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-cash-coding-filament`](https://github.com/liberusoftware/module-accounting-cash-coding-filament) (`liberusoftware/accounting-cash-coding-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/cash-coding.md) · [API plan](../api/cash-coding.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **High-volume statement coding** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `high-volume statement coding`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bulk rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bulk rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tax/dimensions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tax/dimensions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payee creation policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payee creation policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Review** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `review`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Posting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `posting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Undo constraints** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `undo constraints`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CashCodingFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding-filament/src/CashCodingFilamentPlugin.php) · [CashCodingFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding-filament/src/CashCodingFilamentServiceProvider.php) · [CashCodingBatchResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding-filament/src/Resources/CashCodingBatchResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CashCodingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Queries/CashCodingQuery.php) | `public function forTeam(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCashCodingBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Actions/CreateCashCodingBatch.php) | `public function handle(array $attributes): CashCodingBatch` |
| [TransitionCashCodingBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Actions/TransitionCashCodingBatch.php) | `public function review(CashCodingBatch $batch, ?int $actor = null): CashCodingBatch`<br>`public function post(CashCodingBatch $batch, ?int $actor = null): CashCodingBatch`<br>`public function undo(CashCodingBatch $batch, string $reason): CashCodingBatch` |
| [CashCodingPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding-api/src/Policies/CashCodingPolicy.php) | `public function viewAny($user): bool`<br>`public function view($user, CashCodingBatch $batch): bool`<br>`public function create($user): bool`<br>`public function update($user, CashCodingBatch $batch): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CashCodingBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Models/CashCodingBatch.php) | `team_id`, `reference`, `status`, `lines`, `payee_creation_policy`, `total_amount`, `currency`, `created_by`, `reviewed_by`, `posted_by`, `undo_reason`, `posted_at`, `undone_at`, `metadata` |
<!-- layer-implementation-plan:end -->
