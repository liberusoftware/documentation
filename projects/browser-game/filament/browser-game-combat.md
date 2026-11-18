# Browser Game: Browser Game Combat Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-combat). Observed identity: [`liberusoftware/module-browser-game-combat-filament`](../../../modules/source/liberusoftware--module-browser-game-combat-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-browser-game-browser-game-combat-filament`  
**Matching domain module:** `browser-game-combat`  
**Application:** Browser Game  
**Source feature:** [Browser Game Combat](../features/browser-game-combat.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `browser-game-combat` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Turn/action rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Abilities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Effects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cooldowns:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Enemies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bosses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Loot:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Logs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Simulation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-browser-game-browser-game-combat-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `turn-action-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `abilities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `effects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cooldowns`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `enemies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bosses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `loot`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `logs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `simulation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `browser-game-combat` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-browser-game-combat-filament`](https://github.com/liberusoftware/module-browser-game-combat-filament) (`liberusoftware/browser-game-combat-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/browser-game-combat.md) · [API plan](../api/browser-game-combat.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Turn/action rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `turn/action rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Abilities** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `abilities`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Effects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `effects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cooldowns** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cooldowns`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Enemies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `enemies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bosses** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bosses`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Loot** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `loot`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Logs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `logs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Simulation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `simulation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CombatFilamentPlugin.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat-filament/src/CombatFilamentPlugin.php) · [CombatFilamentServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat-filament/src/CombatFilamentServiceProvider.php) · [CombatBattleResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat-filament/src/Resources/CombatBattleResource.php) · [CreateCombatBattle.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat-filament/src/Resources/CombatBattleResource/Pages/CreateCombatBattle.php) · [EditCombatBattle.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat-filament/src/Resources/CombatBattleResource/Pages/EditCombatBattle.php) · [ListCombatBattles.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat-filament/src/Resources/CombatBattleResource/Pages/ListCombatBattles.php) · [CombatDefinitionResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat-filament/src/Resources/CombatDefinitionResource.php) · [CreateCombatDefinition.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat-filament/src/Resources/CombatDefinitionResource/Pages/CreateCombatDefinition.php) · [EditCombatDefinition.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat-filament/src/Resources/CombatDefinitionResource/Pages/EditCombatDefinition.php) · [ListCombatDefinitions.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat-filament/src/Resources/CombatDefinitionResource/Pages/ListCombatDefinitions.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CombatQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Queries/CombatQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CombatPolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Policies/CombatPolicy.php) | `public function view(mixed $user, CombatBattle $battle): bool`<br>`public function act(mixed $user, CombatBattle $battle): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CombatAction.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Models/CombatAction.php) | No literal fillable array detected; inspect the model and API schema. |
| [CombatBattle.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Models/CombatBattle.php) | No literal fillable array detected; inspect the model and API schema. |
| [CombatDefinition.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Models/CombatDefinition.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
