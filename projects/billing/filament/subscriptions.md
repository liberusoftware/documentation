# Billing: Subscriptions Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#subscriptions). Observed identity: [`liberusoftware/module-billing-subscriptions-filament`](../../../modules/source/liberusoftware--module-billing-subscriptions-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-subscriptions-filament`  
**Matching domain module:** `billing-subscriptions`  
**Application:** Billing  
**Source feature:** [Subscriptions](../features/subscriptions.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `billing-subscriptions` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Activation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Renewal:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Trial:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Upgrade/downgrade:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Pause:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cancellation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Entitlement state:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-subscriptions-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `activation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `renewal`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `trial`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `upgrade-downgrade`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `pause`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cancellation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `entitlement-state`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `billing-subscriptions` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-billing-subscriptions-filament`](https://github.com/liberusoftware/module-billing-subscriptions-filament) (`liberusoftware/billing-subscriptions-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/subscriptions.md) · [API plan](../api/subscriptions.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Activation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `activation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Renewal** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `renewal`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Trial** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `trial`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Upgrade/downgrade** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `upgrade/downgrade`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Pause** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `pause`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cancellation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cancellation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Entitlement state** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `entitlement state`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [SubscriptionResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions-filament/src/Resources/SubscriptionResource.php) · [CreateSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions-filament/src/Resources/SubscriptionResource/Pages/CreateSubscription.php) · [ListSubscriptions.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions-filament/src/Resources/SubscriptionResource/Pages/ListSubscriptions.php) · [SubscriptionsFilamentPlugin.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions-filament/src/SubscriptionsFilamentPlugin.php) · [SubscriptionsFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions-filament/src/SubscriptionsFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListSubscriptions.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Queries/ListSubscriptions.php) | `public function execute(?int $teamId, int $perPage = 25, ?int $customerId = null, ?SubscriptionStatus $status = null): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ActivateSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Subscription` |
| [CancelSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/CancelSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription): Subscription` |
| [ChangeSubscriptionPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ChangeSubscriptionPlan.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription, ?int $pricingPlanId): Subscription` |
| [ExpireSubscriptions.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ExpireSubscriptions.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(?int $teamId = null, ?CarbonInterface $asOf = null): int` |
| [PauseSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/PauseSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription): Subscription` |
| [RenewSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/RenewSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription, ?int $periodDays = null): Subscription` |
| [ResumeSubscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/ResumeSubscription.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription): Subscription` |
| [UpdateEntitlementState.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Actions/UpdateEntitlementState.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Subscription $subscription, array $entitlements): Subscription` |
| [SubscriptionPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Policies/SubscriptionPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Subscription $subscription): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Subscription $subscription): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Subscription.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-subscriptions/src/Models/Subscription.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
