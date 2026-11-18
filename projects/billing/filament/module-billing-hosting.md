# Billing: Module Billing Hosting Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-hosting). Observed identity: [`liberusoftware/module-billing-hosting-filament`](../../../modules/source/liberusoftware--module-billing-hosting-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-module-billing-hosting-filament`  
**Matching domain module:** `module-billing-hosting`  
**Application:** Billing  
**Source feature:** [Module Billing Hosting](../features/module-billing-hosting.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-billing-hosting` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Hosting accounts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Control-panel adapters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **SSL:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Resources:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lifecycle operations:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-module-billing-hosting-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `hosting-accounts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `control-panel-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ssl`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `resources`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lifecycle-operations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-billing-hosting` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-billing-hosting-filament`](https://github.com/liberusoftware/module-billing-hosting-filament) (`liberusoftware/billing-hosting-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-billing-hosting.md) · [API plan](../api/module-billing-hosting.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Hosting accounts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `hosting accounts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Plans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `plans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Control-panel adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `control-panel adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **SSL** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ssl`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Resources** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `resources`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Lifecycle operations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lifecycle operations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [HostingFilamentPlugin.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting-filament/src/HostingFilamentPlugin.php) · [HostingFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting-filament/src/HostingFilamentServiceProvider.php) · [HostingAccountResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting-filament/src/Resources/HostingAccountResource.php) · [CreateHostingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting-filament/src/Resources/HostingAccountResource/Pages/CreateHostingAccount.php) · [ListHostingAccounts.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting-filament/src/Resources/HostingAccountResource/Pages/ListHostingAccounts.php) · [HostingCapabilityResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting-filament/src/Resources/HostingCapabilityResource.php) · [CreateHostingCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting-filament/src/Resources/HostingCapabilityResource/Pages/CreateHostingCapability.php) · [ListHostingCapabilities.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting-filament/src/Resources/HostingCapabilityResource/Pages/ListHostingCapabilities.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListHostingRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Queries/ListHostingRecords.php) | `public function handle(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateHostingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/CreateHostingAccount.php) | `public function handle(int $teamId, array $attributes): HostingAccount` |
| [CreateHostingCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/CreateHostingCapability.php) | `public function handle(int $teamId, array $attributes): HostingCapability` |
| [CreateHostingServer.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/CreateHostingServer.php) | `public function handle(int $teamId, array $attributes): HostingServer` |
| [PerformHostingOperation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/PerformHostingOperation.php) | `public function __construct(private HostingDriverRegistry $drivers)`<br>`public function handle(HostingAccount $account, string $operation): HostingAccount` |
| [TransitionHostingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/TransitionHostingAccount.php) | `public function handle(HostingAccount $account, string $status): HostingAccount` |
| [TransitionHostingCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Actions/TransitionHostingCapability.php) | `public function handle(HostingCapability $capability, string $status): HostingCapability` |
| [ControlPanelDriver.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Contracts/ControlPanelDriver.php) | `public function unsuspend(array $attributes): array`<br>`public function changePackage(array $attributes): array`<br>`public function addAddon(array $attributes): array`<br>`public function removeAddon(array $attributes): array` |
| [HostingDriver.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Contracts/HostingDriver.php) | `public function key(): string`<br>`public function provision(array $attributes): array`<br>`public function suspend(array $attributes): array`<br>`public function terminate(array $attributes): array` |
| [HostingAccountPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Policies/HostingAccountPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, HostingAccount $record): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, HostingAccount $record): bool` |
| [HostingCapabilityPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Policies/HostingCapabilityPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function update(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [HostingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Models/HostingAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [HostingCapability.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Models/HostingCapability.php) | No literal fillable array detected; inspect the model and API schema. |
| [HostingServer.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-hosting/src/Models/HostingServer.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
