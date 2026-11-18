# Billing: Customer Portal Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customer-portal). Observed identity: [`liberusoftware/module-billing-customer-portal-filament`](../../../modules/source/liberusoftware--module-billing-customer-portal-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-customer-portal-filament`  
**Matching domain module:** `billing-customer-portal`  
**Application:** Billing  
**Source feature:** [Customer Portal](../features/customer-portal.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `billing-customer-portal` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Profile:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Orders:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Services:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Usage:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Invoices:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tickets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Changes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cancellation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-customer-portal-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `profile`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `orders`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `services`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `usage`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `invoices`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tickets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `changes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cancellation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `billing-customer-portal` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-billing-customer-portal-filament`](https://github.com/liberusoftware/module-billing-customer-portal-filament) (`liberusoftware/billing-customer-portal-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/customer-portal.md) · [API plan](../api/customer-portal.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Profile** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `profile`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Orders** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `orders`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Services** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `services`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Usage** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `usage`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Invoices** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `invoices`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tickets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tickets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Changes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `changes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cancellation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cancellation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CustomerPortalFilamentPlugin.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-filament/src/CustomerPortalFilamentPlugin.php) · [CustomerPortalFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-filament/src/CustomerPortalFilamentServiceProvider.php) · [PortalItemResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-filament/src/Resources/PortalItemResource.php) · [CreatePortalItem.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-filament/src/Resources/PortalItemResource/Pages/CreatePortalItem.php) · [ListPortalItems.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-filament/src/Resources/PortalItemResource/Pages/ListPortalItems.php) · [PortalRequestResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-filament/src/Resources/PortalRequestResource.php) · [CreatePortalRequest.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-filament/src/Resources/PortalRequestResource/Pages/CreatePortalRequest.php) · [ListPortalRequests.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-filament/src/Resources/PortalRequestResource/Pages/ListPortalRequests.php).

| Observed core query | Public method signatures |
| --- | --- |
| [GetCustomerBillingSummary.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Queries/GetCustomerBillingSummary.php) | `public function __construct(private DatabaseManager $database)`<br>`public function handle(int $teamId, int $customerId, ?CarbonInterface $startAt = null, ?CarbonInterface $endAt = null): array` |
| [ListCustomerPortalRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Queries/ListCustomerPortalRecords.php) | `public function handle(int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListPortalItems.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Queries/ListPortalItems.php) | `public function handle(int $teamId, ?string $type = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePortalItem.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/CreatePortalItem.php) | `public function handle(int $teamId, array $attributes): PortalItem` |
| [CreatePortalRequest.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/CreatePortalRequest.php) | `public function handle(int $teamId, array $attributes): PortalRequest` |
| [TransitionPortalItem.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/TransitionPortalItem.php) | `public function handle(PortalItem $item, string $status): PortalItem` |
| [TransitionPortalRequest.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Actions/TransitionPortalRequest.php) | `public function handle(PortalRequest $request, string $status): PortalRequest` |
| [PortalItemPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Policies/PortalItemPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function update(?object $user, object $item): bool`<br>`public function view(?object $user, object $item): bool` |
| [PortalRequestPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Policies/PortalRequestPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, PortalRequest $record): bool`<br>`public function update(?Authenticatable $user, PortalRequest $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PortalItem.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Models/PortalItem.php) | No literal fillable array detected; inspect the model and API schema. |
| [PortalRequest.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal/src/Models/PortalRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [Customer.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-customer-portal-api/src/Models/Customer.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
