# Browser Game React Native + Expo implementations

**Scope:** [Browser Game](../BROWSER-GAME.md)
**Architecture:** [Mobile](../../../architecture/MOBILE.md) · [API](../api/README.md) · [Core](../core/README.md)
**Technology:** [React Native technology](../../../technologies/REACT-NATIVE.md) · [React Native standard](../../../standards/REACT-NATIVE.md)

This index defines the optional React Native + Expo adapter boundary for the Browser Game project. Each future module adapter must map one-to-one to an existing core/API capability, preserve the server contract, and remain independently testable. Product-specific domain behavior stays in the project feature and core documentation.

## Implementation plan

- Consume the matching versioned API contract; do not query private tables or duplicate Laravel authorization, tenant resolution, audit, or business rules.
- Provide platform-appropriate navigation, screens/widgets, forms, validation feedback, loading/empty/denied/offline/conflict/recovery states, and localization.
- Document native permissions, secure credential storage, deep links, push notifications, cache classification, offline mutation policy, and supported OS/device matrix.
- Test API schemas and authorization, state transitions, accessibility, localization, lifecycle interruptions, permission denial, offline recovery, and signed release builds.
- Keep package naming consistent: `module-{independent-module-name}-react-native`; host applications choose only the adapters they need.

## Related module indexes

- [Core domain modules](../core/README.md)
- [API modules](../api/README.md)
- [All mobile project indexes](../../../modules/mobile/README.md)
- [React Native + Expo module standard](../../../modules/react-native/README.md)

This project may ship no mobile client, one mobile client, or both. A missing adapter is an explicit product decision and must not be interpreted as permission to move domain behavior into the client.

## Complete module index

The following 15 adapters map one-to-one to the project core and API indexes. Each module document is the implementation plan for this surface.

| Module                                                  | Package                                                   | Core                                        | API                                       |
| ------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------- | ----------------------------------------- |
| [Accounts](accounts.md)                                 | module-browser-game-accounts-react-native                 | [Core](../core/accounts.md)                 | [API](../api/accounts.md)                 |
| [Characters](characters.md)                             | module-browser-game-characters-react-native               | [Core](../core/characters.md)               | [API](../api/characters.md)               |
| [Collections](collections.md)                           | module-browser-game-collections-react-native              | [Core](../core/collections.md)              | [API](../api/collections.md)              |
| [Combat](combat.md)                                     | module-browser-game-combat-react-native                   | [Core](../core/combat.md)                   | [API](../api/combat.md)                   |
| [Commerce](commerce.md)                                 | module-browser-game-commerce-react-native                 | [Core](../core/commerce.md)                 | [API](../api/commerce.md)                 |
| [Competition](competition.md)                           | module-browser-game-competition-react-native              | [Core](../core/competition.md)              | [API](../api/competition.md)              |
| [Crafting](crafting.md)                                 | module-browser-game-crafting-react-native                 | [Core](../core/crafting.md)                 | [API](../api/crafting.md)                 |
| [Economy](economy.md)                                   | module-browser-game-economy-react-native                  | [Core](../core/economy.md)                  | [API](../api/economy.md)                  |
| [Game Core](game-core.md)                               | module-browser-game-game-core-react-native                | [Core](../core/game-core.md)                | [API](../api/game-core.md)                |
| [Items](items.md)                                       | module-browser-game-items-react-native                    | [Core](../core/items.md)                    | [API](../api/items.md)                    |
| [Live Ops](live-ops.md)                                 | module-browser-game-live-ops-react-native                 | [Core](../core/live-ops.md)                 | [API](../api/live-ops.md)                 |
| [Moderation And Analytics](moderation-and-analytics.md) | module-browser-game-moderation-and-analytics-react-native | [Core](../core/moderation-and-analytics.md) | [API](../api/moderation-and-analytics.md) |
| [Quests](quests.md)                                     | module-browser-game-quests-react-native                   | [Core](../core/quests.md)                   | [API](../api/quests.md)                   |
| [Social](social.md)                                     | module-browser-game-social-react-native                   | [Core](../core/social.md)                   | [API](../api/social.md)                   |
| [World](world.md)                                       | module-browser-game-world-react-native                    | [Core](../core/world.md)                    | [API](../api/world.md)                    |
