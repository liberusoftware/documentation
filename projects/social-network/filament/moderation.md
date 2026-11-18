# Social Network: Moderation Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#moderation). Observed identity: [`liberusoftware/module-social-network-moderation-filament`](../../../modules/source/liberusoftware--module-social-network-moderation-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-moderation-filament`  
**Matching domain module:** `social-network-moderation`  
**Application:** Social Network  
**Source feature:** [Moderation](../features/moderation.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `social-network-moderation` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Reports:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Queues:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Policy/rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Evidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Actions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Appeals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sanctions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transparency:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-moderation-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `reports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `queues`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `policy-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `actions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `appeals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sanctions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transparency`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `social-network-moderation` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-social-network-moderation-filament`](https://github.com/liberusoftware/module-social-network-moderation-filament) (`liberusoftware/social-network-moderation-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/moderation.md) · [API plan](../api/moderation.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Reports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Queues** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `queues`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Policy/rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `policy/rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Evidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `evidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Actions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `actions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Appeals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `appeals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sanctions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sanctions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transparency** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transparency`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ModerationFilamentPlugin.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation-filament/src/ModerationFilamentPlugin.php) · [ModerationFilamentServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation-filament/src/ModerationFilamentServiceProvider.php) · [Reports.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation-filament/src/Pages/Reports.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateReport.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Actions/CreateReport.php) | `public function __construct(private ModerationAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $reporter, string $targetType, string $targetId, string $reason, ?string $details = null): ModerationReport` |
| [DecideReport.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Actions/DecideReport.php) | `public function __construct(private ModerationAuthorizer $authorizer)`<br>`public function handle(Profile $actor, ModerationReport $report, string $action, ?string $reason = null, array $evidence = []): ModerationDecision` |
| [ModerationAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Contracts/ModerationAuthorizer.php) | `public function report(Profile $reporter): void`<br>`public function decide(Profile $actor): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ModerationDecision.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Models/ModerationDecision.php) | `report_id`, `actor_profile_id`, `action`, `reason`, `evidence` |
| [ModerationReport.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-moderation/src/Models/ModerationReport.php) | `id`, `reporter_profile_id`, `target_type`, `target_id`, `reason`, `details`, `state`, `assigned_to` |
<!-- layer-implementation-plan:end -->
