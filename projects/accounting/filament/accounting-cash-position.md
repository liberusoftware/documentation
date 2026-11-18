# Accounting: Accounting Cash Position Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-cash-position). Observed identity: [`liberusoftware/module-accounting-cash-position-filament`](../../../modules/source/liberusoftware--module-accounting-cash-position-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-cash-position-filament`  
**Matching domain module:** `accounting-cash-position`  
**Application:** Accounting  
**Source feature:** [Accounting Cash Position](../features/accounting-cash-position.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-cash-position` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Available/ledger balances:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Outstanding receipts/payments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Committed cash:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Entity/currency views:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Freshness:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-cash-position-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `available-ledger-balances`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `outstanding-receipts-payments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `committed-cash`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `entity-currency-views`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `freshness`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-cash-position` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-cash-position-filament`](https://github.com/liberusoftware/module-accounting-cash-position-filament) (`liberusoftware/accounting-cash-position-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-cash-position.md) · [API plan](../api/accounting-cash-position.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Available/ledger balances** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `available/ledger balances`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Outstanding receipts/payments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `outstanding receipts/payments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Committed cash** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `committed cash`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Entity/currency views** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `entity/currency views`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Freshness** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `freshness`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CashPositionFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position-filament/src/CashPositionFilamentPlugin.php) · [CashPositionFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position-filament/src/CashPositionFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CashPositionQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position/src/Queries/CashPositionQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCashPosition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position/src/Actions/CreateCashPosition.php) | `public function handle(array $attributes): CashPosition` |
| [RefreshCashPosition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position/src/Actions/RefreshCashPosition.php) | `public function handle(CashPosition $position, array $balances): CashPosition` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CashPosition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position/src/Models/CashPosition.php) | `team_id`, `view_ref`, `entity_ref`, `currency`, `ledger_balance`, `available_balance`, `outstanding_receipts`, `outstanding_payments`, `committed_cash`, `refreshed_at` |
<!-- layer-implementation-plan:end -->
