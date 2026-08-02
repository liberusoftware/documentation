# Liberu Core Modules

This index covers the Laravel 13/PHP 8.5 core Composer packages for the Liberu domain. Each module is independently installable, testable, versioned, and usable by enterprise applications, small businesses, and personal users. Presentation adapters consume the core package; they do not own its business rules.

| Module                                                                  | Core package                                   | Domain specification                                       |
| ----------------------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------------- |
| [Business Workflow Reconciliation](business-workflow-reconciliation.md) | module-liberu-business-workflow-reconciliation | [Feature](../features/business-workflow-reconciliation.md) |
| [Executive Insights](executive-insights.md)                             | module-liberu-executive-insights               | [Feature](../features/executive-insights.md)               |
| [Platform Orchestration](platform-orchestration.md)                     | module-liberu-platform-orchestration           | [Feature](../features/platform-orchestration.md)           |

## Shared implementation contract

Every core package applies the DDD, Laravel, PHP, database, security, services, jobs, documentation, and testing standards linked from [MODULES.md](../../../architecture/MODULES.md), [Laravel 13](../../../standards/LARAVEL.md), [PHP 8.5](../../../standards/PHP.md), [domain-driven design](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md). It owns its domain model, application use cases, policies, persistence, events, jobs, contracts, lifecycle, recovery, and user-safe operational behavior. API, Filament, Livewire, React, Vue, and Nuxt packages depend on the public core boundary and never reimplement it.
