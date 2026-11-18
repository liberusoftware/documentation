# CMS: Experimentation Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#experimentation). Observed identity: [`liberusoftware/module-cms-experimentation-filament`](../../../modules/source/liberusoftware--module-cms-experimentation-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-experimentation-filament`  
**Matching domain module:** `cms-experimentation`  
**Application:** CMS  
**Source feature:** [Experimentation](../features/experimentation.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-experimentation` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **A/B/multivariate content tests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Allocation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Goals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Guardrails:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Analysis policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Winner promotion:** resource/table/form/action or page behavior for this module's authorized workflow.
- **History:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-experimentation-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `a-b-multivariate-content-tests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `allocation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `goals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `guardrails`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `analysis-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `winner-promotion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-experimentation` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-experimentation-filament`](https://github.com/liberusoftware/module-cms-experimentation-filament) (`liberusoftware/cms-experimentation-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/experimentation.md) · [API plan](../api/experimentation.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **A/B/multivariate content tests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `a/b/multivariate content tests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Allocation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `allocation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Goals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `goals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Guardrails** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `guardrails`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Analysis policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `analysis policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Winner promotion** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `winner promotion`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **History** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ExperimentationFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-experimentation-filament/src/ExperimentationFilamentServiceProvider.php) · [ExperimentResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-experimentation-filament/src/Resources/ExperimentResource.php) · [ListExperiments.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-experimentation-filament/src/Resources/Pages/ListExperiments.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ExperimentationQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Queries/ExperimentationQuery.php) | `public function list(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function find(string $key): ?Experiment`<br>`public function active(string $key): ?Experiment` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ExperimentationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Services/ExperimentationService.php) | `public function create(array $attributes, ?int $teamId = null): Experiment`<br>`public function start(Experiment $experiment): Experiment`<br>`public function stop(Experiment $experiment): Experiment`<br>`public function allocate(Experiment $experiment, string $subjectKey): ?ExperimentVariant`<br>`public function observe(Experiment $experiment, ExperimentVariant $variant, string $subjectKey, ?string $goalKey, float $value = 1): ExperimentObservation`<br>`public function promote(Experiment $experiment, ExperimentVariant $variant, ?string $reason = null, ?string $actorType = null, int\|string\|null $actorId = null): Experiment` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Experiment.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Models/Experiment.php) | `key`, `name`, `type`, `status`, `allocation_percentage`, `goals`, `guardrails`, `analysis_policy`, `winner_variant_key`, `team_id` |
| [ExperimentObservation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Models/ExperimentObservation.php) | `experiment_id`, `variant_id`, `subject_key`, `goal_key`, `value`, `observed_at` |
| [ExperimentPromotion.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Models/ExperimentPromotion.php) | `experiment_id`, `variant_id`, `actor_type`, `actor_id`, `reason`, `promoted_at` |
| [ExperimentVariant.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-experimentation/src/Models/ExperimentVariant.php) | `experiment_id`, `key`, `name`, `content`, `weight` |
<!-- layer-implementation-plan:end -->
