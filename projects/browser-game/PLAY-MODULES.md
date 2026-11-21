# Browser Game gameplay modules

This map describes the gameplay extraction proposed for `project-browser-game-laravel-filament`. It follows the domain and adapter boundaries in the [module architecture](../../architecture/MODULES.md). The [source inventory](SOURCE-MODULES.md) records a separate, commit-pinned snapshot of the published capability packages.

| Gameplay domain | Owned behavior and data | Application adapters |
| --- | --- | --- |
| `browser-game-play-adventure` | Player and character progression, quests, achievements, player statistics, starter content, and game setup defaults | `browser-game-play-adventure-api`, `browser-game-play-adventure-filament`, `browser-game-play-adventure-livewire` |
| `browser-game-play-arena` | Combat simulation, opt-in duels, NPC encounters, arena rules, and battle history | `browser-game-play-arena-api`, `browser-game-play-arena-filament`, `browser-game-play-arena-livewire` |
| `browser-game-play-community` | Guilds, rankings, game notifications, and daily rewards | `browser-game-play-community-api`, `browser-game-play-community-filament`, `browser-game-play-community-livewire` |
| `browser-game-play-inventory` | Items, equipment, resources, crafting, and marketplace transactions | `browser-game-play-inventory-api`, `browser-game-play-inventory-filament`, `browser-game-play-inventory-livewire` |

## Composition and upgrade

Composer resolves each `liberusoftware/browser-game-play-*` package through the application checkout and installs it in the matching `modules/` directory. Each adapter declares its corresponding gameplay domain in Composer and in its module manifest. Filament plugins contribute pages, resources, and widgets to the existing host panels. API service providers register the existing route paths and Sanctum middleware. The Livewire adapters supply the existing component classes and their Blade views.

The shipped application enables the gameplay modules by default. Providers register the original migration filenames so Laravel continues to identify previously applied migrations by the same names. Keep the normal Laravel migration and rollback commands when upgrading. The extracted code retains the existing model class names, table and column names, route names, and component aliases for compatibility with existing data and integrations.

These packages are tracked host-path extractions under [module promotion readiness](../../architecture/MODULES.md#301-promotion-readiness). They still share the application's player models and schema. Independent release requires explicit public contracts for cross-domain operations, contained persistence, standalone Testbench suites, and the compatibility and coverage evidence in the promotion standard.

## Verification

From the application root:

```bash
composer install
vendor/bin/pest --testsuite=Modules
XDEBUG_MODE=coverage vendor/bin/pest --coverage --min=100 --coverage-clover=coverage.xml
```

The Modules suite discovers `modules/*/tests/Integration`. The full run includes the host's cross-package and architecture suites and measures executable application and module PHP. Coverage scope and release requirements follow the [testing standard](../../standards/TESTING.md#13-coverage-policy).
