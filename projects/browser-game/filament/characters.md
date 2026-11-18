# Browser Game: Characters Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#characters). Observed identity: [`liberusoftware/module-browser-game-characters-filament`](../../../modules/source/liberusoftware--module-browser-game-characters-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-browser-game-characters-filament`  
**Matching domain module:** `browser-game-characters`  
**Application:** Browser Game  
**Source feature:** [Characters](../features/characters.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `browser-game-characters` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Creation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Race/class/background:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Statistics:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Skills:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Experience:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Level:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Health:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Respec:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-browser-game-characters-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `creation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `race-class-background`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `statistics`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `skills`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `experience`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `level`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `health`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `respec`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `browser-game-characters` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-browser-game-laravel-filament`](https://github.com/liberusoftware/project-browser-game-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-browser-game-characters-filament`](https://github.com/liberusoftware/module-browser-game-characters-filament) (`liberusoftware/browser-game-characters-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/characters.md) · [API plan](../api/characters.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Creation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `creation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Race/class/background** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `race/class/background`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Statistics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `statistics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Skills** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `skills`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Experience** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `experience`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Level** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `level`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Health** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `health`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Respec** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `respec`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CharactersFilamentPlugin.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters-filament/src/CharactersFilamentPlugin.php) · [CharactersFilamentServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters-filament/src/CharactersFilamentServiceProvider.php) · [CharacterResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters-filament/src/Resources/CharacterResource.php) · [CreateCharacter.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters-filament/src/Resources/CharacterResource/Pages/CreateCharacter.php) · [EditCharacter.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters-filament/src/Resources/CharacterResource/Pages/EditCharacter.php) · [ListCharacters.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters-filament/src/Resources/CharacterResource/Pages/ListCharacters.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CharacterQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/Queries/CharacterQuery.php) | `public function forPlayer(string $playerId, ?string $worldId = null): Builder`<br>`public function levelForExperience(int $experience): int` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CharacterPolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/Policies/CharacterPolicy.php) | `public function view(?string $actorId, ?string $teamId, GameCharacter $character): bool`<br>`public function manage(?string $actorId, ?string $teamId, GameCharacter $character): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [GameCharacter.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/Models/GameCharacter.php) | `player_id`, `world_id`, `tenant_id`, `team_id`, `name`, `race`, `class`, `background`, `statistics`, `skills`, `experience`, `level`, `health`, `max_health`, `mana`, `max_mana`, `strength`, `defense`, `agility`, `intelligence`, `stat_points`, `available_skill_points`, `respec_count`, `last_operation_key`, `last_battle_at`, `last_action_at` |
<!-- layer-implementation-plan:end -->
