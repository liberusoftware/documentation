# Browser Game: Browser Game Collections Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-collections). Observed identity: [`liberusoftware/module-browser-game-collections-filament`](../../../modules/source/liberusoftware--module-browser-game-collections-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-browser-game-browser-game-collections-filament`  
**Matching domain module:** `browser-game-collections`  
**Application:** Browser Game  
**Source feature:** [Browser Game Collections](../features/browser-game-collections.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `browser-game-collections` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Achievements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Titles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reputation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Pets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Mounts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Housing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cosmetics:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Collection progress:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-browser-game-browser-game-collections-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `achievements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `titles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reputation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `pets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `mounts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `housing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cosmetics`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `collection-progress`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `browser-game-collections` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-browser-game-collections-filament`](https://github.com/liberusoftware/module-browser-game-collections-filament) (`liberusoftware/browser-game-collections-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/browser-game-collections.md) · [API plan](../api/browser-game-collections.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Achievements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `achievements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Titles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `titles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reputation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reputation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Pets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `pets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Mounts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `mounts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Housing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `housing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cosmetics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cosmetics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Collection progress** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `collection progress`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CollectionsFilamentPlugin.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections-filament/src/CollectionsFilamentPlugin.php) · [CollectionsFilamentServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections-filament/src/CollectionsFilamentServiceProvider.php) · [CollectionsResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections-filament/src/Resources/CollectionsResource.php) · [CreateCollections.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections-filament/src/Resources/CollectionsResource/Pages/CreateCollections.php) · [EditCollections.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections-filament/src/Resources/CollectionsResource/Pages/EditCollections.php) · [ListCollections.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections-filament/src/Resources/CollectionsResource/Pages/ListCollections.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CollectionsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Queries/CollectionsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder`<br>`public function availableAchievements(?string $tenantId, ?string $teamId): Builder`<br>`public function forActor(string $actorId, ?string $tenantId, ?string $teamId): Builder`<br>`public function unlockedForActor(string $actorId, ?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CollectionEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Models/CollectionEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [CollectionProgress.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Models/CollectionProgress.php) | No literal fillable array detected; inspect the model and API schema. |
| [CollectionsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Models/CollectionsRecord.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
