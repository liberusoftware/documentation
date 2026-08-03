# Technology references

This directory is the practical technology map for Liberu. It explains the languages, runtimes, tools, browser platform, and framework integrations used by the applications. The root [technology and solution map](../TECHNOLOGIES.md) describes where each technology fits; [standards/](../standards/) defines the required engineering rules; and [architecture/](../architecture/) defines ownership and system boundaries.

## Start here

| Need                                       | Read                                                                                                                                                                                                                                      |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Understand the platform                    | [GETTING-STARTED.md](../GETTING-STARTED.md) · [INSTALL.md](../INSTALL.md)                                                                                                                                                                 |
| Choose a solution or adapter               | [TECHNOLOGIES.md](../TECHNOLOGIES.md) · [modules/README.md](../modules/README.md)                                                                                                                                                         |
| Build a domain module                      | [modules/core](../modules/core/README.md) · [architecture/MODULES.md](../architecture/MODULES.md)                                                                                                                                         |
| Build an API                               | [modules/api](../modules/api/README.md) · [architecture/API.md](../architecture/API.md)                                                                                                                                                   |
| Build user interfaces                      | [modules/filament](../modules/filament/README.md) · [modules/livewire](../modules/livewire/README.md) · [modules/react](../modules/react/README.md) · [modules/vue](../modules/vue/README.md) · [modules/nuxt](../modules/nuxt/README.md) |
| Check security, accessibility, and quality | [architecture/SECURITY.md](../architecture/SECURITY.md) · [standards/THEMES.md](../standards/THEMES.md) · [standards/TESTING.md](../standards/TESTING.md)                                                                                 |

## Languages, runtimes, and package tools

| Technology  | Reference                   |
| ----------- | --------------------------- |
| PHP 8.5     | [PHP](PHP.md)               |
| Composer    | [Composer](COMPOSER.md)     |
| JavaScript  | [JavaScript](JAVASCRIPT.md) |
| TypeScript  | [TypeScript](TYPESCRIPT.md) |
| Node.js 22+ | [Node.js](NODE.md)          |
| Git         | [Git](GIT.md)               |

## Frameworks and build tools

| Technology | Reference               | Liberu standard                                        |
| ---------- | ----------------------- | ------------------------------------------------------ |
| Laravel 13 | [Laravel](LARAVEL.md)   | [Laravel standard](../standards/LARAVEL.md)            |
| Filament 5 | [Filament](FILAMENT.md) | [Filament standard](../standards/FILAMENT.md)          |
| Livewire 4 | [Livewire](LIVEWIRE.md) | [Livewire standard](../standards/LIVEWIRE.md)          |
| React 19.2 | [React](REACT.md)       | [React standard](../standards/REACT.md)                |
| Inertia 3  | [Inertia](INERTIA.md)   | [Inertia standard](../standards/INERTIA.md)            |
| Vue 3      | [Vue](VUE.md)           | [Vue standard](../standards/VUE.md)                    |
| Nuxt 4     | [Nuxt](NUXT.md)         | [Nuxt standard](../standards/NUXT.md)                  |
| Vite       | [Vite](VITE.md)         | [Theme and asset architecture](../standards/THEMES.md) |

## Web platform, data, and delivery

| Technology                    | Reference                                                               |
| ----------------------------- | ----------------------------------------------------------------------- |
| HTML                          | [HTML](HTML.md)                                                         |
| CSS                           | [CSS](CSS.md)                                                           |
| Accessibility                 | [Web accessibility](ACCESSIBILITY.md)                                   |
| Relational databases          | [Database](DATABASE.md) · [database standard](../standards/DATABASE.md) |
| Containers and local services | [Containers](CONTAINERS.md)                                             |
| Automated testing             | [Testing](TESTING.md) · [testing standard](../standards/TESTING.md)     |

Every guide includes official documentation, a small usage example, and links to a representative Liberu implementation or governing standard. Pin exact versions in the consuming repository's lockfiles and CI matrix; this directory records the portfolio baseline, not a substitute for dependency resolution.
