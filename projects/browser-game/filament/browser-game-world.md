# Browser Game: Browser Game World Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-world). Observed identity: [`liberusoftware/module-browser-game-world-filament`](../../../modules/source/liberusoftware--module-browser-game-world-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-browser-game-browser-game-world-filament`  
**Matching domain module:** `browser-game-world`  
**Application:** Browser Game  
**Source feature:** [Browser Game World](../features/browser-game-world.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `browser-game-world` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Regions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Locations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Maps:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Travel:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Encounters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **NPCs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Resources:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Weather:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Unlocks:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-browser-game-browser-game-world-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `regions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `locations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `maps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `travel`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `encounters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `npcs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `resources`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `weather`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `unlocks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `browser-game-world` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-browser-game-world-filament`](https://github.com/liberusoftware/module-browser-game-world-filament) (`liberusoftware/browser-game-world-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/browser-game-world.md) · [API plan](../api/browser-game-world.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Regions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `regions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Locations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `locations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Maps** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `maps`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Travel** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `travel`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Encounters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `encounters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **NPCs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `npcs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Resources** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `resources`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Weather** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `weather`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Unlocks** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `unlocks`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [WorldEntityResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-filament/src/Resources/WorldEntityResource.php) · [CreateWorldEntity.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-filament/src/Resources/WorldEntityResource/Pages/CreateWorldEntity.php) · [EditWorldEntity.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-filament/src/Resources/WorldEntityResource/Pages/EditWorldEntity.php) · [ListWorldEntities.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-filament/src/Resources/WorldEntityResource/Pages/ListWorldEntities.php) · [WorldFilamentPlugin.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-filament/src/WorldFilamentPlugin.php) · [WorldFilamentServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-filament/src/WorldFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [WorldQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Queries/WorldQuery.php) | `public function visible(?string $tenantId, ?string $teamId, ?string $kind = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [WorldPolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Policies/WorldPolicy.php) | `public function view(?string $tenantId, ?string $teamId, WorldEntity $entity): bool`<br>`public function manage(?string $actorId, ?string $tenantId, ?string $teamId, WorldEntity $entity): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorldEntity.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldEntity.php) | `tenant_id`, `team_id`, `world_id`, `kind`, `name`, `slug`, `status`, `attributes`, `coordinates`, `unlock_key` |
| [WorldTravel.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldTravel.php) | `tenant_id`, `team_id`, `actor_id`, `origin_id`, `destination_id`, `idempotency_key`, `metadata` |
| [WorldUnlock.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldUnlock.php) | `tenant_id`, `team_id`, `actor_id`, `entity_id`, `unlock_key`, `status`, `metadata`, `idempotency_key`, `granted_at`, `revoked_at` |
<!-- layer-implementation-plan:end -->
