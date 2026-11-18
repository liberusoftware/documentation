# CMS: Module Cms Notifications And Subscriptions Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-notifications-and-subscriptions). Observed identity: [`liberusoftware/module-cms-notifications-and-subscriptions-filament`](../../../modules/source/liberusoftware--module-cms-notifications-and-subscriptions-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-module-cms-notifications-and-subscriptions-filament`  
**Matching domain module:** `module-cms-notifications-and-subscriptions`  
**Application:** CMS  
**Source feature:** [Module Cms Notifications And Subscriptions](../features/module-cms-notifications-and-subscriptions.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-cms-notifications-and-subscriptions` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Follow content/terms/authors:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Publication/update digests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Frequency:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Channel preferences:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Unsubscribe:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Delivery state:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-module-cms-notifications-and-subscriptions-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `follow-content-terms-authors`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `publication-update-digests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `frequency`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `channel-preferences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `unsubscribe`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `delivery-state`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-cms-notifications-and-subscriptions` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-notifications-and-subscriptions-filament`](https://github.com/liberusoftware/module-cms-notifications-and-subscriptions-filament) (`liberusoftware/cms-notifications-and-subscriptions-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-cms-notifications-and-subscriptions.md) · [API plan](../api/module-cms-notifications-and-subscriptions.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Follow content/terms/authors** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `follow content/terms/authors`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Publication/update digests** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `publication/update digests`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Frequency** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `frequency`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Channel preferences** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `channel preferences`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Unsubscribe** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `unsubscribe`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Delivery state** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `delivery state`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [NotificationsAndSubscriptionsFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-notifications-and-subscriptions-filament/src/NotificationsAndSubscriptionsFilamentServiceProvider.php) · [ListSubscriptions.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-notifications-and-subscriptions-filament/src/Resources/Pages/ListSubscriptions.php) · [SubscriptionResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-notifications-and-subscriptions-filament/src/Resources/SubscriptionResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SubscriptionService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-notifications-and-subscriptions/src/Services/SubscriptionService.php) | `public function follow(string $subscriberType, int\|string $subscriberId, string $subjectType, int\|string $subjectId, string $frequency = 'instant', array $channels = ['mail'], ?string $locale = null, ?int $teamId = null): Subscription`<br>`public function updatePreferences(Subscription $subscription, string $frequency, array $channels, ?string $locale = null): Subscription`<br>`public function unsubscribe(Subscription $subscription): Subscription`<br>`public function queueEvent(string $event, string $subjectType, int\|string $subjectId, array $payload = [], ?int $teamId = null): int`<br>`public function pending(?string $channel = null): array`<br>`public function markSent(Delivery $delivery): Delivery`<br>`public function markFailed(Delivery $delivery): Delivery` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Delivery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-notifications-and-subscriptions/src/Models/Delivery.php) | `subscription_id`, `event`, `channel`, `payload`, `status`, `attempts`, `sent_at`, `failed_at`, `team_id` |
| [Subscription.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-notifications-and-subscriptions/src/Models/Subscription.php) | `subscriber_type`, `subscriber_id`, `subject_type`, `subject_id`, `frequency`, `channels`, `locale`, `active`, `unsubscribed_at`, `team_id` |
<!-- layer-implementation-plan:end -->
