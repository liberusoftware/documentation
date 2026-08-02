# Browser Game Core Modules

This index covers the Laravel 13/PHP 8.5 core Composer packages for the Browser Game domain. Each module is independently installable, testable, versioned, and usable by enterprise applications, small businesses, and personal users. Presentation adapters consume the core package; they do not own its business rules.

| Module                                                  | Core package                                 | Domain specification                               |
| ------------------------------------------------------- | -------------------------------------------- | -------------------------------------------------- |
| [Accounts](accounts.md)                                 | module-browser-game-accounts                 | [Feature](../features/accounts.md)                 |
| [Characters](characters.md)                             | module-browser-game-characters               | [Feature](../features/characters.md)               |
| [Collections](collections.md)                           | module-browser-game-collections              | [Feature](../features/collections.md)              |
| [Combat](combat.md)                                     | module-browser-game-combat                   | [Feature](../features/combat.md)                   |
| [Commerce](commerce.md)                                 | module-browser-game-commerce                 | [Feature](../features/commerce.md)                 |
| [Competition](competition.md)                           | module-browser-game-competition              | [Feature](../features/competition.md)              |
| [Crafting](crafting.md)                                 | module-browser-game-crafting                 | [Feature](../features/crafting.md)                 |
| [Economy](economy.md)                                   | module-browser-game-economy                  | [Feature](../features/economy.md)                  |
| [Game Core](game-core.md)                               | module-browser-game-game-core                | [Feature](../features/game-core.md)                |
| [Items](items.md)                                       | module-browser-game-items                    | [Feature](../features/items.md)                    |
| [Live Ops](live-ops.md)                                 | module-browser-game-live-ops                 | [Feature](../features/live-ops.md)                 |
| [Moderation And Analytics](moderation-and-analytics.md) | module-browser-game-moderation-and-analytics | [Feature](../features/moderation-and-analytics.md) |
| [Quests](quests.md)                                     | module-browser-game-quests                   | [Feature](../features/quests.md)                   |
| [Social](social.md)                                     | module-browser-game-social                   | [Feature](../features/social.md)                   |
| [World](world.md)                                       | module-browser-game-world                    | [Feature](../features/world.md)                    |

## Shared implementation contract

Every core package applies the DDD, Laravel, PHP, database, security, services, jobs, documentation, and testing standards linked from [MODULES.md](../../../architecture/MODULES.md), [Laravel 13](../../../standards/LARAVEL.md), [PHP 8.5](../../../standards/PHP.md), [domain-driven design](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md). It owns its domain model, application use cases, policies, persistence, events, jobs, contracts, lifecycle, recovery, and user-safe operational behavior. API, Filament, Livewire, React, Vue, and Nuxt packages depend on the public core boundary and never reimplement it.
