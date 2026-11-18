# Accounting: Accounting Collections Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-collections). Observed identity: [`liberusoftware/module-accounting-collections-filament`](../../../modules/source/liberusoftware--module-accounting-collections-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-collections-filament`  
**Matching domain module:** `accounting-collections`  
**Application:** Accounting  
**Source feature:** [Accounting Collections](../features/accounting-collections.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-collections` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Reminder schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Statement runs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Promise-to-pay:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Disputes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Late fees/interest policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Collection stages:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Write-offs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Agency adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-collections-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `reminder-schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `statement-runs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `promise-to-pay`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `disputes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `late-fees-interest-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `collection-stages`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `write-offs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `agency-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-collections` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-collections-filament`](https://github.com/liberusoftware/module-accounting-collections-filament) (`liberusoftware/accounting-collections-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-collections.md) · [API plan](../api/accounting-collections.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Reminder schedules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reminder schedules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Statement runs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `statement runs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Promise-to-pay** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `promise-to-pay`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Disputes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `disputes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Late fees/interest policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `late fees/interest policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Collection stages** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `collection stages`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Write-offs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `write-offs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Agency adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `agency adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CollectionsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections-filament/src/CollectionsFilamentPlugin.php) · [CollectionsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections-filament/src/CollectionsFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CollectionCaseQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Queries/CollectionCaseQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCollectionCase.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/CreateCollectionCase.php) | `public function handle(array $attributes): CollectionCase` |
| [PrepareCollectionStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/PrepareCollectionStatement.php) | `public function handle(CollectionCase $case, array $statement): CollectionCase` |
| [RecordCollectionActivity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/RecordCollectionActivity.php) | `public function reminder(CollectionCase $case, array $reminder): CollectionCase`<br>`public function promise(CollectionCase $case, array $promise): CollectionCase`<br>`public function dispute(CollectionCase $case, array $dispute): CollectionCase` |
| [SendToCollectionAgency.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/SendToCollectionAgency.php) | `public function handle(CollectionCase $case, string $agency): CollectionCase` |
| [WriteOffCollectionCase.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Actions/WriteOffCollectionCase.php) | `public function handle(CollectionCase $case, array $writeOff): CollectionCase` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CollectionCase.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-collections/src/Models/CollectionCase.php) | `team_id`, `case_ref`, `customer_ref`, `balance`, `stage`, `interest_rate`, `reminders`, `statement_run`, `promise_to_pay`, `disputes`, `write_off`, `agency` |
<!-- layer-implementation-plan:end -->
