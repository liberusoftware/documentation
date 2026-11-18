# Social Network: Social Network Social Core Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-social-core). Observed identity: [`liberusoftware/module-social-network-social-core-filament`](../../../modules/source/liberusoftware--module-social-network-social-core-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-social-network-social-core-filament`  
**Matching domain module:** `social-network-social-core`  
**Application:** Social Network  
**Source feature:** [Social Network Social Core](../features/social-network-social-core.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `social-network-social-core` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Network settings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deployment mode:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Terminology:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Feature policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Shared IDs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Events:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-social-network-social-core-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `network-settings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deployment-mode`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `terminology`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `feature-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `shared-ids`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `events`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `social-network-social-core` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-social-network-social-core-filament`](https://github.com/liberusoftware/module-social-network-social-core-filament) (`liberusoftware/social-network-social-core-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/social-network-social-core.md) · [API plan](../api/social-network-social-core.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Network settings** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `network settings`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deployment mode** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deployment mode`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Terminology** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `terminology`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Feature policy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `feature policy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Shared IDs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `shared ids`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Events** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `events`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [SocialCoreSettings.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-filament/src/Pages/SocialCoreSettings.php) · [SocialCoreFilamentPlugin.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-filament/src/SocialCoreFilamentPlugin.php) · [SocialCoreFilamentServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-core-filament/src/SocialCoreFilamentServiceProvider.php).

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
