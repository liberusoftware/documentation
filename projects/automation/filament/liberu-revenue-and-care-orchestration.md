# Automation: Liberu Revenue And Care Orchestration Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#liberu-revenue-and-care-orchestration). Observed identity: [`liberusoftware/liberu-revenue-and-care-orchestration-filament`](../../../modules/source/liberusoftware--liberu-revenue-and-care-orchestration-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-automation-liberu-revenue-and-care-orchestration-filament`  
**Matching domain module:** `liberu-revenue-and-care-orchestration`  
**Application:** Automation  
**Source feature:** [Liberu Revenue And Care Orchestration](../features/liberu-revenue-and-care-orchestration.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `liberu-revenue-and-care-orchestration` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Liberu revenue and care orchestration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Liberu revenue and care orchestration lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-automation-liberu-revenue-and-care-orchestration-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `liberu-revenue-and-care-orchestration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `liberu-revenue-and-care-orchestration-lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `liberu-revenue-and-care-orchestration` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-automation-laravel-filament`](https://github.com/liberusoftware/project-automation-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-liberu-revenue-and-care-orchestration-68bcf257-filament`](https://github.com/liberusoftware/module-liberu-revenue-and-care-orchestration-68bcf257-filament) (`liberusoftware/liberu-revenue-and-care-orchestration-68bcf257-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/liberu-revenue-and-care-orchestration.md) · [API plan](../api/liberu-revenue-and-care-orchestration.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Liberu revenue and care orchestration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `liberu revenue and care orchestration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Liberu revenue and care orchestration lifecycle** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `liberu revenue and care orchestration lifecycle`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CarePlanResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-revenue-and-care-orchestration-filament/src/Resources/CarePlanResource.php) · [CreateCarePlan.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-revenue-and-care-orchestration-filament/src/Resources/CarePlanResource/Pages/CreateCarePlan.php) · [EditCarePlan.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-revenue-and-care-orchestration-filament/src/Resources/CarePlanResource/Pages/EditCarePlan.php) · [ListCarePlans.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-revenue-and-care-orchestration-filament/src/Resources/CarePlanResource/Pages/ListCarePlans.php) · [RevenueAndCareOrchestrationFilamentServiceProvider.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-revenue-and-care-orchestration-filament/src/RevenueAndCareOrchestrationFilamentServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCarePlan.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-revenue-and-care-orchestration/src/Actions/CreateCarePlan.php) | `public function execute(array $attributes): CarePlan` |
| [TransitionCarePlan.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-revenue-and-care-orchestration/src/Actions/TransitionCarePlan.php) | `public function execute(CarePlan $record, LifecycleStatus $to): CarePlan` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CarePlan.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/liberu-revenue-and-care-orchestration/src/Models/CarePlan.php) | `tenant_id`, `idempotency_key`, `name`, `status`, `metadata` |
<!-- layer-implementation-plan:end -->
