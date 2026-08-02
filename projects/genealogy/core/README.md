# Genealogy Core Modules

This index covers the Laravel 13/PHP 8.5 core Composer packages for the Genealogy domain. Each module is independently installable, testable, versioned, and usable by enterprise applications, small businesses, and personal users. Presentation adapters consume the core package; they do not own its business rules.

| Module                              | Core package                    | Domain specification                     |
| ----------------------------------- | ------------------------------- | ---------------------------------------- |
| [Collaboration](collaboration.md)   | module-genealogy-collaboration  | [Feature](../features/collaboration.md)  |
| [Discovery](discovery.md)           | module-genealogy-discovery      | [Feature](../features/discovery.md)      |
| [Dna](dna.md)                       | module-genealogy-dna            | [Feature](../features/dna.md)            |
| [Evidence](evidence.md)             | module-genealogy-evidence       | [Feature](../features/evidence.md)       |
| [Genealogy Core](genealogy-core.md) | module-genealogy-genealogy-core | [Feature](../features/genealogy-core.md) |
| [Import Export](import-export.md)   | module-genealogy-import-export  | [Feature](../features/import-export.md)  |
| [Media](media.md)                   | module-genealogy-media          | [Feature](../features/media.md)          |
| [People](people.md)                 | module-genealogy-people         | [Feature](../features/people.md)         |
| [Places](places.md)                 | module-genealogy-places         | [Feature](../features/places.md)         |
| [Relationships](relationships.md)   | module-genealogy-relationships  | [Feature](../features/relationships.md)  |
| [Reports](reports.md)               | module-genealogy-reports        | [Feature](../features/reports.md)        |
| [Research](research.md)             | module-genealogy-research       | [Feature](../features/research.md)       |
| [Timeline](timeline.md)             | module-genealogy-timeline       | [Feature](../features/timeline.md)       |
| [Tree Viewer](tree-viewer.md)       | module-genealogy-tree-viewer    | [Feature](../features/tree-viewer.md)    |

## Shared implementation contract

Every core package applies the DDD, Laravel, PHP, database, security, services, jobs, documentation, and testing standards linked from [MODULES.md](../../../architecture/MODULES.md), [Laravel 13](../../../standards/LARAVEL.md), [PHP 8.5](../../../standards/PHP.md), [domain-driven design](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md). It owns its domain model, application use cases, policies, persistence, events, jobs, contracts, lifecycle, recovery, and user-safe operational behavior. API, Filament, Livewire, React, Vue, and Nuxt packages depend on the public core boundary and never reimplement it.
