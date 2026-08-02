# Control Panel Core Modules

This index covers the Laravel 13/PHP 8.5 core Composer packages for the Control Panel domain. Each module is independently installable, testable, versioned, and usable by enterprise applications, small businesses, and personal users. Presentation adapters consume the core package; they do not own its business rules.

| Module                                      | Core package                            | Domain specification                         |
| ------------------------------------------- | --------------------------------------- | -------------------------------------------- |
| [Accounts](accounts.md)                     | module-control-panel-accounts           | [Feature](../features/accounts.md)           |
| [Api And Automation](api-and-automation.md) | module-control-panel-api-and-automation | [Feature](../features/api-and-automation.md) |
| [Backups](backups.md)                       | module-control-panel-backups            | [Feature](../features/backups.md)            |
| [Certificates](certificates.md)             | module-control-panel-certificates       | [Feature](../features/certificates.md)       |
| [Containers](containers.md)                 | module-control-panel-containers         | [Feature](../features/containers.md)         |
| [Control Core](control-core.md)             | module-control-panel-control-core       | [Feature](../features/control-core.md)       |
| [Databases](databases.md)                   | module-control-panel-databases          | [Feature](../features/databases.md)          |
| [Dns](dns.md)                               | module-control-panel-dns                | [Feature](../features/dns.md)                |
| [Files](files.md)                           | module-control-panel-files              | [Feature](../features/files.md)              |
| [Kubernetes](kubernetes.md)                 | module-control-panel-kubernetes         | [Feature](../features/kubernetes.md)         |
| [Mail](mail.md)                             | module-control-panel-mail               | [Feature](../features/mail.md)               |
| [Monitoring](monitoring.md)                 | module-control-panel-monitoring         | [Feature](../features/monitoring.md)         |
| [Os Adapters](os-adapters.md)               | module-control-panel-os-adapters        | [Feature](../features/os-adapters.md)        |
| [Security](security.md)                     | module-control-panel-security           | [Feature](../features/security.md)           |
| [Web Hosting](web-hosting.md)               | module-control-panel-web-hosting        | [Feature](../features/web-hosting.md)        |

## Shared implementation contract

Every core package applies the DDD, Laravel, PHP, database, security, services, jobs, documentation, and testing standards linked from [MODULES.md](../../../architecture/MODULES.md), [Laravel 13](../../../standards/LARAVEL.md), [PHP 8.5](../../../standards/PHP.md), [domain-driven design](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md). It owns its domain model, application use cases, policies, persistence, events, jobs, contracts, lifecycle, recovery, and user-safe operational behavior. API, Filament, Livewire, React, Vue, and Nuxt packages depend on the public core boundary and never reimplement it.
