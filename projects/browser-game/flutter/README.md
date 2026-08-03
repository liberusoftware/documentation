# Browser Game Flutter + Dart implementations

**Scope:** [Browser Game](../BROWSER-GAME.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [Flutter technology](../../../technologies/FLUTTER.md) · [Flutter standard](../../../standards/FLUTTER.md)

This index defines the optional Flutter + Dart adapter boundary for the Browser Game project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

## Implementation plan

- Consume the matching versioned API contract; do not query private tables or duplicate Laravel authorization, tenant resolution, audit, or business rules.
- Provide platform-appropriate navigation, screens/widgets, forms, validation feedback, loading/empty/denied/offline/conflict/recovery states, and localization.
- Document native permissions, secure credential storage, deep links, push notifications, cache classification, offline mutation policy, and supported OS/device matrix.
- Test API schemas and authorization, state transitions, accessibility, localization, lifecycle interruptions, permission denial, offline recovery, and signed release builds.
- Keep package naming consistent: `module-{independent-module-name}-flutter`; host applications choose only the adapters they need.

## Related module indexes

- [Core domain modules](../core/README.md)
- [API modules](../api/README.md)
- [All mobile project indexes](../../../modules/mobile/README.md)
- [Flutter + Dart module standard](../../../modules/flutter/README.md)

This project may ship no mobile client, one mobile client, or both. A missing adapter is an explicit product decision and must not be interpreted as permission to move domain behavior into the client.

## Complete module index

The following 15 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                                  | Package                                              | Core                                        | API                                       |
| ------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------- | ----------------------------------------- |
| [Accounts](accounts.md)                                 | module-browser-game-accounts-flutter                 | [Core](../core/accounts.md)                 | [API](../api/accounts.md)                 |
| [Characters](characters.md)                             | module-browser-game-characters-flutter               | [Core](../core/characters.md)               | [API](../api/characters.md)               |
| [Collections](collections.md)                           | module-browser-game-collections-flutter              | [Core](../core/collections.md)              | [API](../api/collections.md)              |
| [Combat](combat.md)                                     | module-browser-game-combat-flutter                   | [Core](../core/combat.md)                   | [API](../api/combat.md)                   |
| [Commerce](commerce.md)                                 | module-browser-game-commerce-flutter                 | [Core](../core/commerce.md)                 | [API](../api/commerce.md)                 |
| [Competition](competition.md)                           | module-browser-game-competition-flutter              | [Core](../core/competition.md)              | [API](../api/competition.md)              |
| [Crafting](crafting.md)                                 | module-browser-game-crafting-flutter                 | [Core](../core/crafting.md)                 | [API](../api/crafting.md)                 |
| [Economy](economy.md)                                   | module-browser-game-economy-flutter                  | [Core](../core/economy.md)                  | [API](../api/economy.md)                  |
| [Game Core](game-core.md)                               | module-browser-game-game-core-flutter                | [Core](../core/game-core.md)                | [API](../api/game-core.md)                |
| [Items](items.md)                                       | module-browser-game-items-flutter                    | [Core](../core/items.md)                    | [API](../api/items.md)                    |
| [Live Ops](live-ops.md)                                 | module-browser-game-live-ops-flutter                 | [Core](../core/live-ops.md)                 | [API](../api/live-ops.md)                 |
| [Moderation And Analytics](moderation-and-analytics.md) | module-browser-game-moderation-and-analytics-flutter | [Core](../core/moderation-and-analytics.md) | [API](../api/moderation-and-analytics.md) |
| [Quests](quests.md)                                     | module-browser-game-quests-flutter                   | [Core](../core/quests.md)                   | [API](../api/quests.md)                   |
| [Social](social.md)                                     | module-browser-game-social-flutter                   | [Core](../core/social.md)                   | [API](../api/social.md)                   |
| [World](world.md)                                       | module-browser-game-world-flutter                    | [Core](../core/world.md)                    | [API](../api/world.md)                    |
