# Social Network: Social Network Engagement Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-engagement). Observed identity: [`liberusoftware/module-social-network-engagement-filament`](../../../modules/source/liberusoftware--module-social-network-engagement-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-social-network-engagement-filament`  
**Matching domain module:** `social-network-engagement`  
**Application:** Social Network  
**Source feature:** [Social Network Engagement](../features/social-network-engagement.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `social-network-engagement` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Reactions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Comments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Replies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sharing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bookmarks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Counters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Abuse limits:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-social-network-engagement-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `reactions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `comments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `replies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sharing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bookmarks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `counters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `abuse-limits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `social-network-engagement` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-social-network-engagement-filament`](https://github.com/liberusoftware/module-social-network-engagement-filament) (`liberusoftware/social-network-engagement-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/social-network-engagement.md) · [API plan](../api/social-network-engagement.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Reactions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reactions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Comments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `comments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Replies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `replies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sharing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sharing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bookmarks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bookmarks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Counters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `counters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Abuse limits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `abuse limits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [EngagementFilamentPlugin.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement-filament/src/EngagementFilamentPlugin.php) · [EngagementFilamentServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement-filament/src/EngagementFilamentServiceProvider.php) · [Engagements.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement-filament/src/Pages/Engagements.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateEngagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/CreateEngagement.php) | `public function __construct(private EngagementAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $actor, array $attributes): Engagement` |
| [DeleteEngagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/DeleteEngagement.php) | `public function __construct(private EngagementAuthorizer $authorizer)`<br>`public function handle(Profile $actor, Engagement $engagement): void` |
| [ListEngagements.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/ListEngagements.php) | `public function handle(string $targetType, string $targetId, ?string $kind = null, int $limit = 50): Collection`<br>`public function count(string $targetType, string $targetId, ?string $kind = null): int` |
| [UpdateEngagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/UpdateEngagement.php) | `public function handle(Profile $actor, Engagement $engagement, string $body): Engagement` |
| [EngagementAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Contracts/EngagementAuthorizer.php) | `public function create(Profile $actor): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Engagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Models/Engagement.php) | `id`, `actor_profile_id`, `target_type`, `target_id`, `kind`, `reaction_type`, `body` |
<!-- layer-implementation-plan:end -->
