# Browser Game gameplay module ownership

The shipped Browser Game integration belongs to the existing Browser Game packages. This map describes the application changes under review. The [source inventory](SOURCE-MODULES.md) gives the commit-pinned references for the reusable packages.

| Owning module | Integration with the shipped game | Presentation packages |
| --- | --- | --- |
| `browser-game-quests` | Starter adventure, quests, progression, and achievements. Quest rewards use the existing `browser-game-characters` level calculation. | `browser-game-quests-api`, `browser-game-quests-filament`, `browser-game-quests-livewire` |
| `browser-game-combat` | Arena battles, NPC encounters, duels, and existing battle records | `browser-game-combat-api`, `browser-game-combat-filament`, `browser-game-combat-livewire` |
| `browser-game-social` | Guilds and the shipped community screens for rankings, rewards, and game notifications | `browser-game-social-api`, `browser-game-social-filament`, `browser-game-social-livewire` |
| `browser-game-items` | Inventory and equipment, including the shipped crafting and marketplace integration | `browser-game-items-api`, `browser-game-items-filament`, `browser-game-items-livewire` |

## Composition and upgrades

Each referenced package keeps its established Composer identity. Application integration lives in the owning package's `host/` directory. The application registers those providers and panel contributions through its composition root. This preserves the existing route paths, Sanctum guards, Livewire aliases, model names, table names, and migration filenames. An existing database retains its migration history.

The application resolves the affected packages from the checkout. Build the new lock file in a clean checkout or build directory with a fresh Composer vendor directory. Composer can replace module directories when transitioning an installed package from a distribution archive to a checkout path.

The package publisher excludes `host/` when building standalone releases. Package `src/` and standalone suites retain their reusable contracts. The compatibility code still uses the original shared player schema. Migrating those records and entry points onto the reusable managers requires a data and behavior transition with the evidence in the [module architecture](../../architecture/MODULES.md#301-promotion-readiness).

## Verification

From the application root:

```bash
composer install
composer test:modules
XDEBUG_MODE=coverage composer test:coverage
```

The Modules suite discovers `modules/*/host/tests/Integration`. The full application run includes the host's cross-package and architecture suites and measures executable application and module PHP. Standalone package tests run in their owning repositories. The [testing standard](../../standards/TESTING.md#13-coverage-policy) defines coverage scope and the release gate.
