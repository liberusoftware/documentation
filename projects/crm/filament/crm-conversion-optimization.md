# CRM: Crm Conversion Optimization Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-conversion-optimization). Observed identity: [`liberusoftware/module-crm-conversion-optimization-filament`](../../../modules/source/liberusoftware--module-crm-conversion-optimization-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-conversion-optimization-filament`  
**Matching domain module:** `crm-conversion-optimization`  
**Application:** CRM  
**Source feature:** [Crm Conversion Optimization](../features/crm-conversion-optimization.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-conversion-optimization` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **A/B and multivariate tests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Traffic allocation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Goals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Statistical policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Popups:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Banners:** resource/table/form/action or page behavior for this module's authorized workflow.
- **CTAs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Personalization rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Experiment reporting:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-conversion-optimization-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `a-b-and-multivariate-tests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `traffic-allocation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `goals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `statistical-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `popups`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `banners`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ctas`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `personalization-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `experiment-reporting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-conversion-optimization` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-conversion-optimization-filament`](https://github.com/liberusoftware/module-crm-conversion-optimization-filament) (`liberusoftware/crm-conversion-optimization-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-conversion-optimization.md) · [API plan](../api/crm-conversion-optimization.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **A/B and multivariate tests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `a/b and multivariate tests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Traffic allocation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `traffic allocation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Goals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `goals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Statistical policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `statistical policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Popups** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `popups`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Banners** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `banners`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **CTAs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ctas`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Personalization rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `personalization rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Experiment reporting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `experiment reporting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ConversionOptimizationFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization-filament/src/ConversionOptimizationFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ConversionReportQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Queries/ConversionReportQuery.php) | `public function experiments(int $teamId): Builder`<br>`public function report(int $teamId, ConversionExperiment $experiment): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateExperiment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Actions/ActivateExperiment.php) | `public function execute(int $teamId, int $userId, ConversionExperiment $experiment): ConversionExperiment` |
| [CreateConversionExperiment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Actions/CreateConversionExperiment.php) | `public function execute(int $teamId, int $userId, array $input): ConversionExperiment` |
| [RecordConversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Actions/RecordConversion.php) | `public function execute(int $teamId, ConversionExperiment $experiment, string $subjectKey, string $variant, string $event, float $value = 1): ConversionObservation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConversionExperiment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Models/ConversionExperiment.php) | No literal fillable array detected; inspect the model and API schema. |
| [ConversionObservation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Models/ConversionObservation.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
