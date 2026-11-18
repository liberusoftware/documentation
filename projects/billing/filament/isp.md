# Billing: ISP Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#isp). Observed identity: [`liberusoftware/module-billing-isp-filament`](../../../modules/source/liberusoftware--module-billing-isp-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-isp-filament`  
**Matching domain module:** `billing-isp`  
**Application:** Billing  
**Source feature:** [ISP](../features/isp.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `billing-isp` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Access services:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Coverage:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Installation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **RADIUS/AAA:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Usage:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Equipment:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Network adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-isp-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `access-services`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `coverage`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `installation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `radius-aaa`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `usage`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `equipment`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `network-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `billing-isp` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-billing-isp-filament`](https://github.com/liberusoftware/module-billing-isp-filament) (`liberusoftware/billing-isp-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/isp.md) · [API plan](../api/isp.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Access services** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `access services`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Coverage** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `coverage`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Installation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `installation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **RADIUS/AAA** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `radius/aaa`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Usage** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `usage`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Equipment** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `equipment`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Network adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `network adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [IspFilamentPlugin.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp-filament/src/IspFilamentPlugin.php) · [IspFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp-filament/src/IspFilamentServiceProvider.php) · [AccessServiceResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp-filament/src/Resources/AccessServiceResource.php) · [CreateAccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp-filament/src/Resources/AccessServiceResource/Pages/CreateAccessService.php) · [ListAccessServices.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp-filament/src/Resources/AccessServiceResource/Pages/ListAccessServices.php) · [IspCapabilityResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp-filament/src/Resources/IspCapabilityResource.php) · [CreateIspCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp-filament/src/Resources/IspCapabilityResource/Pages/CreateIspCapability.php) · [ListIspCapabilities.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp-filament/src/Resources/IspCapabilityResource/Pages/ListIspCapabilities.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListIspRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Queries/ListIspRecords.php) | `public function handle(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/CreateAccessService.php) | `public function handle(int $teamId, array $attributes): AccessService` |
| [CreateIspCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/CreateIspCapability.php) | `public function handle(int $teamId, array $attributes): IspCapability` |
| [RecordRadiusAccounting.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/RecordRadiusAccounting.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(AccessService $service, array $accounting): RadiusSession` |
| [ResetUsagePeriod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/ResetUsagePeriod.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(AccessService $service): AccessService` |
| [SynchronizeAccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/SynchronizeAccessService.php) | `public function __construct(private DatabaseManager $database, private NetworkAdapterRegistry $adapters)`<br>`public function execute(AccessService $service, string $adapter): AccessService` |
| [TransitionAccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/TransitionAccessService.php) | `public function handle(AccessService $service, string $status): AccessService` |
| [TransitionIspCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Actions/TransitionIspCapability.php) | `public function handle(IspCapability $capability, string $status): IspCapability` |
| [NetworkAdapter.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Contracts/NetworkAdapter.php) | `public function key(): string`<br>`public function install(array $attributes): array`<br>`public function suspend(array $attributes): array`<br>`public function remove(array $attributes): array` |
| [AccessServicePolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Policies/AccessServicePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, AccessService $record): bool`<br>`public function update(?Authenticatable $user, AccessService $record): bool` |
| [IspCapabilityPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Policies/IspCapabilityPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccessService.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Models/AccessService.php) | No literal fillable array detected; inspect the model and API schema. |
| [IspCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Models/IspCapability.php) | No literal fillable array detected; inspect the model and API schema. |
| [RadiusSession.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-isp/src/Models/RadiusSession.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
