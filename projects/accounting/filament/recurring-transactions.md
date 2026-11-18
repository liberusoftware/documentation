# Accounting: Recurring Transactions Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#recurring-transactions). Observed identity: [`liberusoftware/module-accounting-recurring-transactions-filament`](../../../modules/source/liberusoftware--module-accounting-recurring-transactions-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-recurring-transactions-filament`  
**Matching domain module:** `accounting-recurring-transactions`  
**Application:** Accounting  
**Source feature:** [Recurring Transactions](../features/recurring-transactions.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-recurring-transactions` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Date/amount rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Draft/automatic generation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exceptions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Expiry:** resource/table/form/action or page behavior for this module's authorized workflow.
- **History:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-recurring-transactions-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `date-amount-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `draft-automatic-generation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exceptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `expiry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-recurring-transactions` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-recurring-transactions-filament`](https://github.com/liberusoftware/module-accounting-recurring-transactions-filament) (`liberusoftware/accounting-recurring-transactions-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/recurring-transactions.md) · [API plan](../api/recurring-transactions.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Templates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `templates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Schedules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `schedules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Date/amount rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `date/amount rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Draft/automatic generation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `draft/automatic generation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exceptions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exceptions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Expiry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `expiry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **History** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [RecurringTransactionsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions-filament/src/RecurringTransactionsFilamentPlugin.php) · [RecurringTransactionsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions-filament/src/RecurringTransactionsFilamentServiceProvider.php) · [ListRecurringTemplates.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions-filament/src/Resources/Pages/ListRecurringTemplates.php) · [RecurringTemplateResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions-filament/src/Resources/RecurringTemplateResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveRecurringTemplate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions/src/Actions/ApproveRecurringTemplate.php) | `public function handle(RecurringTemplate $template, ?int $actorId = null): RecurringTemplate` |
| [CreateRecurringTemplate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions/src/Actions/CreateRecurringTemplate.php) | `public function handle(array $attributes): RecurringTemplate` |
| [GenerateRecurringOccurrences.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions/src/Actions/GenerateRecurringOccurrences.php) | `public function handle(RecurringTemplate $template, string $throughDate, ?int $safetyCap = 120): int` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RecurringException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions/src/Models/RecurringException.php) | `template_id`, `occurrence_id`, `kind`, `message`, `status`, `resolved_at`, `metadata` |
| [RecurringOccurrence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions/src/Models/RecurringOccurrence.php) | `template_id`, `occurrence_on`, `idempotency_key`, `status`, `generated_payload`, `error_message`, `generated_at`, `metadata` |
| [RecurringTemplate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-recurring-transactions/src/Models/RecurringTemplate.php) | `team_id`, `name`, `transaction_type`, `frequency`, `starts_on`, `next_run_on`, `ends_on`, `status`, `automatic`, `date_rules`, `amount_rules`, `payload`, `approved_by`, `approved_at`, `metadata` |
<!-- layer-implementation-plan:end -->
