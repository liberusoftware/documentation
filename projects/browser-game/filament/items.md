# Browser Game: Items Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#items). Observed identity: [`liberusoftware/module-browser-game-items-filament`](../../../modules/source/liberusoftware--module-browser-game-items-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-browser-game-items-filament`  
**Matching domain module:** `browser-game-items`  
**Application:** Browser Game  
**Source feature:** [Items](../features/items.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `browser-game-items` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Definitions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Inventory:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Equipment:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Durability:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Binding:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Containers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Stack rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provenance:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-browser-game-items-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `definitions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `inventory`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `equipment`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `durability`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `binding`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `containers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `stack-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provenance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `browser-game-items` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-browser-game-items-filament`](https://github.com/liberusoftware/module-browser-game-items-filament) (`liberusoftware/browser-game-items-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/items.md) · [API plan](../api/items.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Definitions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `definitions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Inventory** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `inventory`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Equipment** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `equipment`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Durability** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `durability`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Binding** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `binding`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Containers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `containers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Stack rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `stack rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provenance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provenance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ItemsFilamentPlugin.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items-filament/src/ItemsFilamentPlugin.php) · [ItemsFilamentServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items-filament/src/ItemsFilamentServiceProvider.php) · [ItemsResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items-filament/src/Resources/ItemsResource.php) · [CreateItem.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items-filament/src/Resources/ItemsResource/Pages/CreateItem.php) · [EditItem.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items-filament/src/Resources/ItemsResource/Pages/EditItem.php) · [ListItems.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items-filament/src/Resources/ItemsResource/Pages/ListItems.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ItemsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Queries/ItemsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [InventoryEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Models/InventoryEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [ItemsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Models/ItemsRecord.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
