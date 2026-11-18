# CRM: Crm Client Onboarding Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-client-onboarding). Observed identity: [`liberusoftware/module-crm-client-onboarding-filament`](../../../modules/source/liberusoftware--module-crm-client-onboarding-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-client-onboarding-filament`  
**Matching domain module:** `crm-client-onboarding`  
**Application:** CRM  
**Source feature:** [Crm Client Onboarding](../features/crm-client-onboarding.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-client-onboarding` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Intake:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Domain/provider connections:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Data import:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Snapshot application:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Verification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Launch checklist:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Training:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Handoff:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Health:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-client-onboarding-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `intake`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `domain-provider-connections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `data-import`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `snapshot-application`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `verification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `launch-checklist`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `training`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `handoff`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `health`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-client-onboarding` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-client-onboarding-filament`](https://github.com/liberusoftware/module-crm-client-onboarding-filament) (`liberusoftware/crm-client-onboarding-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-client-onboarding.md) · [API plan](../api/crm-client-onboarding.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Intake** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `intake`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Domain/provider connections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `domain/provider connections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Data import** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `data import`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Snapshot application** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `snapshot application`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Verification** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `verification`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Launch checklist** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `launch checklist`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Training** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `training`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Handoff** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `handoff`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Health** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `health`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ClientOnboardingFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding-filament/src/ClientOnboardingFilamentPlugin.php) · [ClientOnboardingFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding-filament/src/ClientOnboardingFilamentServiceProvider.php) · [ClientOnboardingResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding-filament/src/Resources/ClientOnboardingResource.php) · [CreateClientOnboarding.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding-filament/src/Resources/ClientOnboardingResource/Pages/CreateClientOnboarding.php) · [ListClientOnboardings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding-filament/src/Resources/ClientOnboardingResource/Pages/ListClientOnboardings.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ClientOnboardingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Queries/ClientOnboardingQuery.php) | `public function onboardings(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CompleteOnboardingStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Actions/CompleteOnboardingStep.php) | `public function execute(int $teamId, int $actorId, ClientOnboarding $onboarding, string $kind, string $label, array $evidence = []): ClientOnboardingStep` |
| [StartClientOnboarding.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Actions/StartClientOnboarding.php) | `public function execute(int $teamId, int $ownerId, string $clientKey, array $intake = []): ClientOnboarding` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ClientOnboarding.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Models/ClientOnboarding.php) | No literal fillable array detected; inspect the model and API schema. |
| [ClientOnboardingStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Models/ClientOnboardingStep.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
