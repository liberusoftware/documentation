# Social Network: Social Network Social Core Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-social-core). Observed identity: [`liberusoftware/module-social-network-social-core-livewire`](../../../modules/source/liberusoftware--module-social-network-social-core-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-social-network-social-network-social-core-livewire`  
**Matching domain module:** `social-network-social-core`  
**Application:** Social Network  
**Source feature:** [Social Network Social Core](../features/social-network-social-core.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Network settings:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deployment mode:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Terminology:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Feature policy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Shared IDs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Events:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-social-network-social-network-social-core-livewire` component namespace and service provider; use explicit aliases such as `<livewire:socialnetworkSocialNetworkSocialCore::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `network-settings`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deployment-mode`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `terminology`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `feature-policy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `shared-ids`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `events`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `social-network-social-core` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/social-network-social-core.md) · [API plan](../api/social-network-social-core.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Network settings** | Expose a focused Livewire 4 component and namespaced Blade default view for `network settings` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deployment mode** | Expose a focused Livewire 4 component and namespaced Blade default view for `deployment mode` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Terminology** | Expose a focused Livewire 4 component and namespaced Blade default view for `terminology` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Feature policy** | Expose a focused Livewire 4 component and namespaced Blade default view for `feature policy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Shared IDs** | Expose a focused Livewire 4 component and namespaced Blade default view for `shared ids` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Events** | Expose a focused Livewire 4 component and namespaced Blade default view for `events` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [DeploymentMode.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-livewire/src/Components/DeploymentMode.php) · [Events.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-livewire/src/Components/Events.php) · [FeaturePolicy.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-livewire/src/Components/FeaturePolicy.php) · [NetworkSettings.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-livewire/src/Components/NetworkSettings.php) · [SharedIds.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-livewire/src/Components/SharedIds.php) · [SocialCoreSettings.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-livewire/src/Components/SocialCoreSettings.php) · [Terminology.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-livewire/src/Components/Terminology.php) · [SocialCoreLivewireServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-livewire/src/SocialCoreLivewireServiceProvider.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GetSocialNetworkSettings.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Actions/GetSocialNetworkSettings.php) | `public function __construct(private SocialNetworkSettingsRepository $settings)`<br>`public function handle(int\|string $teamId): SocialNetworkSettings` |
| [UpdateSocialNetworkSettings.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Actions/UpdateSocialNetworkSettings.php) | `public function __construct( private SocialNetworkSettingsRepository $settings, private SocialNetworkSettingsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(int\|string $teamId, array $attributes, int\|string\|null $actorId = null): SocialNetworkSettings` |
| [SocialNetworkSettingsAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Contracts/SocialNetworkSettingsAuthorizer.php) | `public function authorize(int\|string $teamId): void` |
| [SocialNetworkSettingsRepository.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Contracts/SocialNetworkSettingsRepository.php) | `public function forTeam(int\|string $teamId): SocialNetworkSettings` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SocialNetworkSettings.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core/src/Models/SocialNetworkSettings.php) | `id`, `team_id`, `deployment_mode`, `network_settings`, `terminology`, `feature_policy`, `shared_ids` |
<!-- layer-implementation-plan:end -->
