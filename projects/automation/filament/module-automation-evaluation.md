# Automation: Module Automation Evaluation Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-automation-evaluation). Observed identity: [`liberusoftware/automation-evaluation-filament`](../../../modules/source/liberusoftware--automation-evaluation-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-automation-module-automation-evaluation-filament`  
**Matching domain module:** `module-automation-evaluation`  
**Application:** Automation  
**Source feature:** [Module Automation Evaluation](../features/module-automation-evaluation.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-automation-evaluation` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Quality suites:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Regression comparison:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Latency/cost metrics:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Safety checks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Release gates:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-automation-module-automation-evaluation-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `quality-suites`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `regression-comparison`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `latency-cost-metrics`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `safety-checks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `release-gates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-automation-evaluation` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-automation-laravel-filament`](https://github.com/liberusoftware/project-automation-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-automation-evaluation-filament`](https://github.com/liberusoftware/module-automation-evaluation-filament) (`liberusoftware/automation-evaluation-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-automation-evaluation.md) · [API plan](../api/module-automation-evaluation.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Quality suites** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quality suites`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Regression comparison** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `regression comparison`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Latency/cost metrics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `latency/cost metrics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Safety checks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `safety checks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Release gates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `release gates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [EvaluationFilamentPlugin.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-evaluation-filament/src/EvaluationFilamentPlugin.php) · [EvaluationFilamentServiceProvider.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-evaluation-filament/src/EvaluationFilamentServiceProvider.php) · [EvaluationResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-evaluation-filament/src/Resources/EvaluationResource.php) · [CreateEvaluation.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-evaluation-filament/src/Resources/EvaluationResource/Pages/CreateEvaluation.php) · [EditEvaluation.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-evaluation-filament/src/Resources/EvaluationResource/Pages/EditEvaluation.php) · [ListEvaluation.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-evaluation-filament/src/Resources/EvaluationResource/Pages/ListEvaluation.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateEvaluationResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-evaluation/src/Actions/CreateEvaluationResource.php) | `public function execute(string $teamId, string $name, array $payload = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): EvaluationResource` |
| [TransitionEvaluationResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-evaluation/src/Actions/TransitionEvaluationResource.php) | `public function execute(EvaluationResource $resource, string $teamId, string $status, array $allowedStatuses = ['draft', 'active', 'paused', 'completed', 'failed', 'cancelled'], ?string $actorId = null, ?string $correlationId = null): EvaluationResource` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EvaluationResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-evaluation/src/Models/EvaluationResource.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
