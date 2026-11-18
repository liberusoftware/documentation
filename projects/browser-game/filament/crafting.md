# Browser Game: Crafting Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crafting). Observed identity: [`liberusoftware/module-browser-game-crafting-filament`](../../../modules/source/liberusoftware--module-browser-game-crafting-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-browser-game-crafting-filament`  
**Matching domain module:** `browser-game-crafting`  
**Application:** Browser Game  
**Source feature:** [Crafting](../features/crafting.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `browser-game-crafting` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Recipes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Professions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Resources:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Quality:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Queues:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Discovery:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Salvage:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Outputs:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-browser-game-crafting-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `recipes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `professions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `resources`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `quality`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `queues`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `discovery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `salvage`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `outputs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `browser-game-crafting` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-browser-game-crafting-filament`](https://github.com/liberusoftware/module-browser-game-crafting-filament) (`liberusoftware/browser-game-crafting-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crafting.md) · [API plan](../api/crafting.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Recipes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recipes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Professions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `professions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Resources** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `resources`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Quality** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quality`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Queues** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `queues`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Discovery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `discovery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Salvage** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `salvage`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Outputs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `outputs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CraftingFilamentPlugin.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting-filament/src/CraftingFilamentPlugin.php) · [CraftingFilamentServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting-filament/src/CraftingFilamentServiceProvider.php) · [CraftingResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting-filament/src/Resources/CraftingResource.php) · [CreateCrafting.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting-filament/src/Resources/CraftingResource/Pages/CreateCrafting.php) · [EditCrafting.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting-filament/src/Resources/CraftingResource/Pages/EditCrafting.php) · [ListCrafting.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting-filament/src/Resources/CraftingResource/Pages/ListCrafting.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CraftingQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Queries/CraftingQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CraftingDiscovery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingDiscovery.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingOutput.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingOutput.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingProfession.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingProfession.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingQueue.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingQueue.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingResource.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
