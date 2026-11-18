# Billing: Module Billing Provisioning Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-provisioning). Observed identity: [`liberusoftware/module-billing-provisioning-filament`](../../../modules/source/liberusoftware--module-billing-provisioning-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-module-billing-provisioning-filament`  
**Matching domain module:** `module-billing-provisioning`  
**Application:** Billing  
**Source feature:** [Module Billing Provisioning](../features/module-billing-provisioning.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-billing-provisioning` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Service state machine:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provider drivers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Queued operations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rollback:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Polling:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-module-billing-provisioning-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `service-state-machine`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provider-drivers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `queued-operations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rollback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `polling`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-billing-provisioning` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-billing-provisioning-filament`](https://github.com/liberusoftware/module-billing-provisioning-filament) (`liberusoftware/billing-provisioning-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-billing-provisioning.md) · [API plan](../api/module-billing-provisioning.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Service state machine** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `service state machine`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provider drivers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider drivers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Queued operations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `queued operations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rollback** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rollback`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Polling** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `polling`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ProvisioningFilamentPlugin.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning-filament/src/ProvisioningFilamentPlugin.php) · [ProvisioningFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning-filament/src/ProvisioningFilamentServiceProvider.php) · [ProvisionedServiceResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning-filament/src/Resources/ProvisionedServiceResource.php) · [CreateProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning-filament/src/Resources/ProvisionedServiceResource/Pages/CreateProvisionedService.php) · [ListProvisionedServices.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning-filament/src/Resources/ProvisionedServiceResource/Pages/ListProvisionedServices.php) · [ProvisioningOperationResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning-filament/src/Resources/ProvisioningOperationResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListProvisionedServices.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Queries/ListProvisionedServices.php) | `public function execute(?int $teamId = null): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/CreateProvisionedService.php) | `public function execute(array $attributes): ProvisionedService` |
| [QueueProvisioningOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/QueueProvisioningOperation.php) | `public function execute(ProvisionedService $service, string $operation, array $payload = []): ProvisioningOperation` |
| [ReconcileProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/ReconcileProvisionedService.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(ProvisionedService $service): ProvisionedService` |
| [RunProvisioningOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/RunProvisioningOperation.php) | `public function __construct(private DatabaseManager $database, private ProvisioningDriverRegistry $drivers)`<br>`public function execute(ProvisioningOperation $operation): ProvisioningOperation` |
| [TransitionProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Actions/TransitionProvisionedService.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(ProvisionedService $service, ProvisioningState $state, ?string $error = null): ProvisionedService` |
| [ProvisioningDriver.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Contracts/ProvisioningDriver.php) | `public function provision(ProvisionedService $service): string`<br>`public function deprovision(ProvisionedService $service): void`<br>`public function poll(ProvisionedService $service): array` |
| [ProvisioningPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Policies/ProvisioningPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function update(?object $user, object $record): bool` |
| [ProvisioningDriverRegistry.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Services/ProvisioningDriverRegistry.php) | `public function register(string $provider, ProvisioningDriver $driver): void`<br>`public function resolve(string $provider): ProvisioningDriver` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProvisionedService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Models/ProvisionedService.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProvisioningOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-provisioning/src/Models/ProvisioningOperation.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
