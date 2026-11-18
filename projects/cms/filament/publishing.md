# CMS: Publishing Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#publishing). Observed identity: [`liberusoftware/module-cms-publishing-filament`](../../../modules/source/liberusoftware--module-cms-publishing-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-publishing-filament`  
**Matching domain module:** `cms-publishing`  
**Application:** CMS  
**Source feature:** [Publishing](../features/publishing.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-publishing` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Immediate/scheduled publishing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Embargo:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Expiry:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Unpublish/archive:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recurring review:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Atomic release:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cache/index events:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-publishing-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `immediate-scheduled-publishing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `embargo`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `expiry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `unpublish-archive`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recurring-review`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `atomic-release`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cache-index-events`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-publishing` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-cms-laravel-filament`](https://github.com/liberusoftware/project-cms-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-cms-publishing-filament`](https://github.com/liberusoftware/module-cms-publishing-filament) (`liberusoftware/cms-publishing-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/publishing.md) · [API plan](../api/publishing.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Immediate/scheduled publishing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `immediate/scheduled publishing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Embargo** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `embargo`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Expiry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `expiry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Unpublish/archive** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `unpublish/archive`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recurring review** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recurring review`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Atomic release** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `atomic release`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cache/index events** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cache/index events`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PublishingFilamentServiceProvider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-publishing-filament/src/PublishingFilamentServiceProvider.php) · [ListPublicationReleases.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-publishing-filament/src/Resources/Pages/ListPublicationReleases.php) · [PublicationReleaseResource.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-publishing-filament/src/Resources/PublicationReleaseResource.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PublishingService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-publishing/src/Services/PublishingService.php) | `public function create(array $attributes): PublicationRelease`<br>`public function schedule(PublicationRelease $release): PublicationRelease`<br>`public function publish(PublicationRelease $release): PublicationRelease`<br>`public function unpublish(PublicationRelease $release): PublicationRelease`<br>`public function archive(PublicationRelease $release): PublicationRelease`<br>`public function processDue(): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PublicationRelease.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-publishing/src/Models/PublicationRelease.php) | `key`, `state`, `publish_at`, `embargo_until`, `expires_at`, `review_at`, `recurrence`, `targets`, `cache_tags`, `team_id` |
| [PublicationReleaseEvent.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-publishing/src/Models/PublicationReleaseEvent.php) | `release_id`, `event`, `payload`, `occurred_at` |
<!-- layer-implementation-plan:end -->
