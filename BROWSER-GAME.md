# Liberu Browser Game

## Product Scope

**Purpose:** Persistent browser-based role-playing game with progression, world simulation, economy, social play, competition, and live operations.
**Architecture:** Game capabilities follow [MODULES.md](MODULES.md); player/admin presentation and media follow [THEMES.md](THEMES.md).

**Foundation:** Consume relevant modules from [BOILERPLATE.md](BOILERPLATE.md); this scope defines game behavior only.

## Outcomes

- Deliver fair, explainable progression and strategic short-session play across devices.
- Maintain authoritative, cheat-resistant character, combat, inventory, and economy state.
- Support safe community play, seasonal content, moderation, balancing, and reversible live operations.

## Module plan

| Module | Responsibilities |
|---|---|
| Game Core | Worlds/shards, game clock, rulesets, content versions, feature flags, and maintenance state |
| Accounts | Player identity, sessions, age/region policy, bans, recovery, privacy, and account lifecycle |
| Characters | Creation, race/class/background, statistics, skills, experience, level, health, and respec |
| World | Regions, locations, maps, travel, encounters, NPCs, resources, weather, and unlocks |
| Combat | Turn/action rules, abilities, effects, cooldowns, enemies, bosses, loot, logs, and simulation |
| Quests | Storylines, objectives, prerequisites, branching, dialogue, rewards, repeatability, and progress |
| Items | Definitions, inventory, equipment, durability, binding, containers, stack rules, and provenance |
| Crafting | Recipes, professions, resources, quality, queues, discovery, salvage, and outputs |
| Economy | Currencies, faucets/sinks, vendors, pricing, trading, auction house, fees, and anti-abuse controls |
| Social | Friends, parties, chat, mail, guilds, alliances, permissions, activity, and reporting |
| Competition | PvP modes, matchmaking, seasons, rankings, leaderboards, rewards, and anti-collusion |
| Collections | Achievements, titles, reputation, pets, mounts, housing, cosmetics, and collection progress |
| Live Ops | Daily activities, events, seasons, content schedules, announcements, grants, and rollback |
| Commerce | Premium membership, entitlements, store, regional pricing, receipts, refunds, and parental controls |
| Moderation and Analytics | Reports, sanctions, appeals, telemetry, funnels, balance, economy, fraud, and health |

## Required workflows

1. **Character progression:** create → tutorial → activity/combat → earn validated rewards → update stats/unlocks → record provenance.
2. **Combat:** validate participants/loadout/action → resolve deterministically on server → persist atomically → grant loot once → publish combat log.
3. **Trade:** lock assets/currency → validate ownership/rules → exchange atomically → charge fees → record immutable ledger entries.
4. **Season:** stage content/rules/rewards → simulate/test → publish → monitor → conclude and distribute once → archive/roll over.
5. **Moderation:** detect/report → preserve evidence → investigate → sanction → notify → appeal/review → expire or uphold.

## Product requirements

- Server-authorize all state changes; clients submit intent and never determine rewards, timers, combat, ownership, or prices.
- Use ledgers and unique transaction IDs for currencies, items, rewards, purchases, trades, and administrative grants.
- Version game content and rules so in-flight actions, replays, audits, and balancing remain explainable.
- Define energy/timer, death/recovery, loot, progression, matchmaking, season, and reset policies explicitly.
- Make scheduled actions and reward claims idempotent and resilient to refresh, retry, concurrency, and queue delay.
- Provide accessible responsive views, keyboard support, reduced motion, clear timers, and nonvisual alternatives for map/combat information.
- Separate cosmetic/premium entitlements from competitive power unless the published product policy explicitly states otherwise.

## Integrations

Identity, notifications, payments, storage/CDN, chat safety, analytics, localization, and optional external login use replaceable drivers. Payment state is reconciled; loss of analytics or optional media cannot block gameplay.

## Quality and fairness gates

- Property-test combat formulas, reward bounds, item/currency conservation, crafting, cooldowns, and progression curves.
- Test concurrent combat actions, duplicate claims, auctions, trades, inventory limits, disconnects, clock skew, and season boundaries.
- Maintain abuse controls for bots, multi-accounting, collusion, market manipulation, spam, and privileged admin actions.
- Simulate economic faucets/sinks and progression before releases; monitor inflation, concentration, churn, win rates, and anomalous acquisition.

## Delivery phases

1. Core, Accounts, Characters, World basics, Combat, Items, Quests, and admin content tools.
2. Crafting, Economy, trading/auction, Social, guilds/parties, achievements, and notifications.
3. PvP/Competition, bosses, collections, housing/pets/mounts, events, seasons, and analytics.
4. Premium commerce, advanced live operations, localization, and continued world/content expansion.

## Definition of done

Core loops are server-authoritative, concurrency-safe, balanced, observable, accessible, recoverable, and protected by immutable economy provenance and controlled live operations. Each module maps to a GitHub epic.
