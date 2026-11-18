# Social Network: Social Network Notifications Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-notifications). Observed identity: [`liberusoftware/module-social-network-notifications-livewire`](../../../modules/source/liberusoftware--module-social-network-notifications-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-social-network-social-network-notifications-livewire`  
**Matching domain module:** `social-network-notifications`  
**Application:** Social Network  
**Source feature:** [Social Network Notifications](../features/social-network-notifications.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Preferences:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **In-app/email/push delivery:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Grouping:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Digests:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quiet hours:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Read state:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-social-network-social-network-notifications-livewire` component namespace and service provider; use explicit aliases such as `<livewire:socialnetworkSocialNetworkNotifications::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `preferences`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `in-app-email-push-delivery`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `grouping`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `digests`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quiet-hours`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `read-state`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `social-network-notifications` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/social-network-notifications.md) · [API plan](../api/social-network-notifications.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Preferences** | Expose a focused Livewire 4 component and namespaced Blade default view for `preferences` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **In-app/email/push delivery** | Expose a focused Livewire 4 component and namespaced Blade default view for `in-app/email/push delivery` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Grouping** | Expose a focused Livewire 4 component and namespaced Blade default view for `grouping` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Digests** | Expose a focused Livewire 4 component and namespaced Blade default view for `digests` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Quiet hours** | Expose a focused Livewire 4 component and namespaced Blade default view for `quiet hours` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Read state** | Expose a focused Livewire 4 component and namespaced Blade default view for `read state` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ListNotifications.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications-livewire/src/Components/ListNotifications.php) · [NotificationsLivewireServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications-livewire/src/NotificationsLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateNotification.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/CreateNotification.php) | `public function __construct(private Dispatcher $events)`<br>`public function handle(string $profileId, string $kind, array $payload = [], string $channel = 'in_app', ?string $groupKey = null): SocialNotification` |
| [DismissNotification.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/DismissNotification.php) | `public function __construct(private NotificationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile, string $id): SocialNotification` |
| [MarkAllRead.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/MarkAllRead.php) | `public function __construct(private NotificationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile): int` |
| [MarkRead.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/MarkRead.php) | `public function __construct(private NotificationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile, string $id): SocialNotification` |
| [UnreadCount.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/UnreadCount.php) | `public function __construct(private NotificationAuthorizer $authorizer)`<br>`public function handle(Profile $profile): int` |
| [UpdatePreferences.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Actions/UpdatePreferences.php) | `public function __construct(private NotificationAuthorizer $authorizer)`<br>`public function handle(Profile $profile, array $data): NotificationPreference` |
| [NotificationAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Contracts/NotificationAuthorizer.php) | `public function manage(Profile $profile): void`<br>`public function view(Profile $profile): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [NotificationPreference.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Models/NotificationPreference.php) | `profile_id`, `channels`, `quiet_hours`, `digest` |
| [SocialNotification.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-notifications/src/Models/SocialNotification.php) | `id`, `profile_id`, `kind`, `group_key`, `state`, `channel`, `payload`, `read_at` |
<!-- layer-implementation-plan:end -->
