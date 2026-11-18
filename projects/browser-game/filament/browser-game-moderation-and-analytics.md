# Browser Game: Browser Game Moderation And Analytics Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-moderation-and-analytics). Observed identity: [`liberusoftware/module-browser-game-moderation-and-analytics-filament`](../../../modules/source/liberusoftware--module-browser-game-moderation-and-analytics-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-browser-game-browser-game-moderation-and-analytics-filament`  
**Matching domain module:** `browser-game-moderation-and-analytics`  
**Application:** Browser Game  
**Source feature:** [Browser Game Moderation And Analytics](../features/browser-game-moderation-and-analytics.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `browser-game-moderation-and-analytics` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Reports:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sanctions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Appeals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Telemetry:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Funnels:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Balance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Economy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fraud:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Health:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-browser-game-browser-game-moderation-and-analytics-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `reports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sanctions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `appeals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `telemetry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `funnels`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `balance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `economy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fraud`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `health`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `browser-game-moderation-and-analytics` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-browser-game-moderation-and-analytics-filament`](https://github.com/liberusoftware/module-browser-game-moderation-and-analytics-filament) (`liberusoftware/browser-game-moderation-and-analytics-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/browser-game-moderation-and-analytics.md) · [API plan](../api/browser-game-moderation-and-analytics.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Reports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sanctions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sanctions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Appeals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `appeals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Telemetry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `telemetry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Funnels** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `funnels`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Balance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `balance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Economy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `economy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fraud** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fraud`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Health** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `health`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ModerationAndAnalyticsFilamentPlugin.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics-filament/src/ModerationAndAnalyticsFilamentPlugin.php) · [ModerationAndAnalyticsFilamentServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics-filament/src/ModerationAndAnalyticsFilamentServiceProvider.php) · [ModerationAndAnalyticsResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics-filament/src/Resources/ModerationAndAnalyticsResource.php) · [CreateModerationAndAnalytics.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics-filament/src/Resources/ModerationAndAnalyticsResource/Pages/CreateModerationAndAnalytics.php) · [EditModerationAndAnalytics.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics-filament/src/Resources/ModerationAndAnalyticsResource/Pages/EditModerationAndAnalytics.php) · [ListModerationAndAnalytics.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics-filament/src/Resources/ModerationAndAnalyticsResource/Pages/ListModerationAndAnalytics.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ModerationAndAnalyticsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Queries/ModerationAndAnalyticsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ModerationAndAnalyticsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Models/ModerationAndAnalyticsRecord.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
