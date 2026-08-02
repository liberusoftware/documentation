# Liberu engineering standards

This folder contains reusable coding, framework, frontend, design, testing, and delivery standards. It describes how we implement technology; architectural decisions and ecosystem boundaries remain under [architecture/](../architecture/).

## Technology standards

| Standard | Scope |
|---|---|
| [PHP](PHP.md) | PHP 8.5 language, Composer, typing, errors, security, and runtime practices |
| [PSR](PSR.md) | PHP-FIG interoperability and PSR-12 coding baseline |
| [Laravel](LARAVEL.md) | Laravel 13 application conventions and official framework integrations |
| [Livewire](LIVEWIRE.md) | Livewire 4 server-driven interfaces |
| [Filament](FILAMENT.md) | Filament 5 panels, resources, schemas, tables, widgets, and plugins |
| [React](REACT.md) | React 19.2 presentation packages and Inertia integration |
| [Inertia](INERTIA.md) | Inertia 3 server/client bridge and page protocol |
| [Vue](VUE.md) | Vue 3 presentation packages and Inertia integration |
| [Nuxt](NUXT.md) | Nuxt 4 SSR and API-consuming applications |
| [JavaScript](../technologies/JAVASCRIPT.md) | JavaScript language and browser-runtime standards |
| [TypeScript](../technologies/TYPESCRIPT.md) | TypeScript contracts, strictness, and build standards |

## Design and implementation standards

- [Guidelines](GUIDELINES.md) — daily coding, review, naming, security, and documentation rules.
- [Themes](THEMES.md) — technology-neutral design tokens, theme adapters, assets, and accessibility.
- [Testing](TESTING.md) — test ownership, quality gates, coverage, compatibility, and CI evidence.
- [Documentation](DOCUMENTATION.md) — documentation ownership, structure, examples, and maintenance.
- [CI](CI.md) — workflow, release, and deployment checks.
- [Contributing](CONTRIBUTING.md) — contribution workflow and engineering quality gates.

## Application building blocks

[Laravel](LARAVEL.md) is the host framework. Use the following focused standards when designing a feature:

| Area | Standard |
|---|---|
| Domain and object design | [Object-oriented programming](OBJECT-ORIENTED-PROGRAMMING.md) · [Domain-driven design patterns](DOMAIN-DRIVEN-DESIGN-PATTERNS.md) |
| Application boundaries | [Services](SERVICES.md) · [Contracts](CONTRACTS.md) · [Classes](CLASSES.md) · [Concerns](CONCERNS.md) |
| HTTP and presentation | [Controllers](CONTROLLERS.md) · [API](../architecture/API.md) · [Views](VIEWS.md) · [Blade](BLADE.md) |
| Async and operations | [Jobs](JOBS.md) · [Queues](QUEUES.md) |
| Persistence | [Models](MODELS.md) |

## Version policy

Use the latest stable releases supported by the ecosystem and the application lock file. At this baseline the standards target PHP 8.5, Laravel 13, Livewire 4, Filament 5, React 19.2, Inertia 3, Vue 3, Nuxt 4, Node.js 22+, and TypeScript. Patch releases are resolved through lockfiles and verified in CI; a version change requires review of the affected standard and compatibility matrix.

## Official references

- [PHP](https://www.php.net/docs.php) · [Composer](https://getcomposer.org/doc/)
- [Laravel](https://laravel.com/docs/13.x) · [Livewire](https://livewire.laravel.com/docs)
- [Filament](https://filamentphp.com/docs/5.x) · [Inertia](https://inertiajs.com/docs/v3)
- [React](https://react.dev/) · [Vue](https://vuejs.org/) · [Nuxt](https://nuxt.com/docs/4.x)
- [PHP-FIG](https://www.php-fig.org/psr/) · [TypeScript](https://www.typescriptlang.org/docs/) · [MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
