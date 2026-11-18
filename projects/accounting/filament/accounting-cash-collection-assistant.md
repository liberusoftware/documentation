# Accounting: Accounting Cash Collection Assistant Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-cash-collection-assistant). Observed identity: [`liberusoftware/module-accounting-cash-collection-assistant-filament`](../../../modules/source/liberusoftware--module-accounting-cash-collection-assistant-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-cash-collection-assistant-filament`  
**Matching domain module:** `accounting-cash-collection-assistant`  
**Application:** Accounting  
**Source feature:** [Accounting Cash Collection Assistant](../features/accounting-cash-collection-assistant.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-cash-collection-assistant` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Invoice-risk prioritization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reminder drafts/timing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Promise tracking:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Outcome feedback:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-cash-collection-assistant-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `invoice-risk-prioritization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reminder-drafts-timing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `promise-tracking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `outcome-feedback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-cash-collection-assistant` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-cash-collection-assistant-filament`](https://github.com/liberusoftware/module-accounting-cash-collection-assistant-filament) (`liberusoftware/accounting-cash-collection-assistant-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-cash-collection-assistant.md) · [API plan](../api/accounting-cash-collection-assistant.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Invoice-risk prioritization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `invoice-risk prioritization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reminder drafts/timing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reminder drafts/timing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Promise tracking** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `promise tracking`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Outcome feedback** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `outcome feedback`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CashCollectionAssistantFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant-filament/src/CashCollectionAssistantFilamentPlugin.php) · [CashCollectionAssistantFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant-filament/src/CashCollectionAssistantFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CashCollectionAssistantQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Queries/CashCollectionAssistantQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCashCollectionAssistant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/CreateCashCollectionAssistant.php) | `public function handle(array $attributes): CashCollectionAssistant` |
| [RecordCollectionPromise.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/RecordCollectionPromise.php) | `public function handle(CashCollectionAssistant $assistant, string $date, string\|float $amount): CashCollectionAssistant` |
| [ScheduleCollectionReminder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/ScheduleCollectionReminder.php) | `public function handle(CashCollectionAssistant $assistant, string $at, ?string $draft = null): CashCollectionAssistant` |
| [SetCollectionDecision.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/SetCollectionDecision.php) | `public function handle(CashCollectionAssistant $assistant, string $field, string $value): CashCollectionAssistant` |
| [UpdateCashCollectionAssistant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Actions/UpdateCashCollectionAssistant.php) | `public function handle(CashCollectionAssistant $assistant, array $attributes): CashCollectionAssistant` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CashCollectionAssistant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-collection-assistant/src/Models/CashCollectionAssistant.php) | `team_id`, `invoice_ref`, `customer_ref`, `risk_score`, `risk_level`, `reminder_status`, `reminder_at`, `promised_amount`, `promised_date`, `promise_status`, `policy_ref`, `approval_status`, `outcome`, `metadata` |
<!-- layer-implementation-plan:end -->
