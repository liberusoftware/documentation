# Liberu Core Modules

<!-- catalogue-status:start -->
This index preserves **4 module documents/spellings**. Counts are specifications, not released packages or deployed features. Exact source identities and aliases are in the [source map](../SOURCE-MAPPING.md); [shared ownership](../../../architecture/SHARED-MODULES.md) and [Next.js adapter homes](../../../modules/nextjs/OWNERSHIP.md) prevent alternate spellings from becoming competing implementations.
<!-- catalogue-status:end -->

This index covers the Laravel 13/PHP 8.5 core Composer packages for the Liberu domain. Each module is independently installable, testable, versioned, and usable by enterprise applications, small businesses, and personal users. Presentation adapters consume the core package; they do not own its business rules.

| Module document | Source/target reference | Related plans |
| --- | --- | --- |
| [Business Workflow Reconciliation Core Module](business-workflow-reconciliation.md) | [Target/source map](../SOURCE-MAPPING.md#business-workflow-reconciliation) | [api](../api/business-workflow-reconciliation.md) · [nextjs](../nextjs/business-workflow-reconciliation.md) |
| [Executive Insights Core Module](executive-insights.md) | [Target/source map](../SOURCE-MAPPING.md#executive-insights) | [api](../api/executive-insights.md) · [nextjs](../nextjs/executive-insights.md) |
| [Platform Orchestration Core Module](platform-orchestration.md) | [Target/source map](../SOURCE-MAPPING.md#platform-orchestration) | [api](../api/platform-orchestration.md) · [nextjs](../nextjs/platform-orchestration.md) |
| [Revenue and Care Orchestration Core](revenue-and-care-orchestration.md) | [Target/source map](../SOURCE-MAPPING.md#revenue-and-care-orchestration) | [api](../api/revenue-and-care-orchestration.md) · [nextjs](../nextjs/revenue-and-care-orchestration.md) |

## Shared implementation contract

Every core package applies the DDD, Laravel, PHP, database, security, services, jobs, documentation, and testing standards linked from [MODULES.md](../../../architecture/MODULES.md), [Laravel 13](../../../standards/LARAVEL.md), [PHP 8.5](../../../standards/PHP.md), [domain-driven design](../../../standards/DOMAIN-DRIVEN-DESIGN-PATTERNS.md), and [testing](../../../standards/TESTING.md). It owns its domain model, application use cases, policies, persistence, events, jobs, contracts, lifecycle, recovery, and user-safe operational behavior. API, Filament, Livewire, React, Vue, and Nuxt packages depend on the public core boundary and never reimplement it.
