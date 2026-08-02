# Automation Core Modules

This index covers the Laravel 13/PHP 8.5 core Composer packages for the Automation domain. Each module is independently installable, testable, versioned, and usable by enterprise applications, small businesses, and personal users. Presentation adapters consume the core package; they do not own its business rules.

| Module                                | Core package                      | Domain specification                      |
| ------------------------------------- | --------------------------------- | ----------------------------------------- |
| [Ai Gateway](ai-gateway.md)           | module-automation-ai-gateway      | [Feature](../features/ai-gateway.md)      |
| [Approvals](approvals.md)             | module-automation-approvals       | [Feature](../features/approvals.md)       |
| [Automation Core](automation-core.md) | module-automation-automation-core | [Feature](../features/automation-core.md) |
| [Connectors](connectors.md)           | module-automation-connectors      | [Feature](../features/connectors.md)      |
| [Data Processing](data-processing.md) | module-automation-data-processing | [Feature](../features/data-processing.md) |
| [Evaluation](evaluation.md)           | module-automation-evaluation      | [Feature](../features/evaluation.md)      |
| [Image](image.md)                     | module-automation-image           | [Feature](../features/image.md)           |
| [Prompt Registry](prompt-registry.md) | module-automation-prompt-registry | [Feature](../features/prompt-registry.md) |
| [Rules](rules.md)                     | module-automation-rules           | [Feature](../features/rules.md)           |
| [Video](video.md)                     | module-automation-video           | [Feature](../features/video.md)           |
| [Voice](voice.md)                     | module-automation-voice           | [Feature](../features/voice.md)           |

## Shared implementation contract

Every core package applies the DDD, Laravel, PHP, database, security, services, jobs, documentation, and testing standards linked from [MODULES.md](../../../architecture/MODULES.md), [Laravel 13](../../../standards/LARAVEL.md), [PHP 8.5](../../../standards/PHP.md), [domain-driven design](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md). It owns its domain model, application use cases, policies, persistence, events, jobs, contracts, lifecycle, recovery, and user-safe operational behavior. API, Filament, Livewire, React, Vue, and Nuxt packages depend on the public core boundary and never reimplement it.
