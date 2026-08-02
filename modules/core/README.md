# Core module implementations

## Canonical domain package boundary

Each core document defines the implementation plan for one independent, provider-neutral domain module. The core Composer package is named `module-{independent-module-name}` and owns the domain model, contracts, application actions and queries, policies, persistence, events, jobs, and tests required by that capability.

Core modules are presentation-neutral. API, Filament, Livewire, React, Vue, and Nuxt packages are optional consumers named with the corresponding suffix, such as `module-{independent-module-name}-api` or `module-{independent-module-name}-filament`. They depend on the core package; the core package never depends on a presentation layer.

## Package responsibilities

- Keep entities, value objects, aggregates, domain services, invariants, and domain events in the domain layer.
- Keep use cases, commands, queries, DTOs, authorization decisions, and transaction boundaries in the application layer.
- Keep Eloquent models, migrations, factories, seeders, repositories, Laravel providers, and integrations in infrastructure.
- Expose stable contracts, actions, queries, events, identifiers, and resource data for presentation packages.
- Keep provider SDKs and provider-specific mappings in separate adapter packages.
- Test the core package independently, then test each presentation adapter against the published core contracts.

## Project indexes

Every project with feature specifications has a matching core index. Each index links one-to-one to the core implementation plan for every feature module:

| Project         | Core module index                                            |
| --------------- | ------------------------------------------------------------ |
| Accounting      | [Core modules](../../projects/accounting/core/README.md)     |
| Automation      | [Core modules](../../projects/automation/core/README.md)     |
| Billing         | [Core modules](../../projects/billing/core/README.md)        |
| Browser Game    | [Core modules](../../projects/browser-game/core/README.md)   |
| CMS             | [Core modules](../../projects/cms/core/README.md)            |
| Control Panel   | [Core modules](../../projects/control-panel/core/README.md)  |
| CRM             | [Core modules](../../projects/crm/core/README.md)            |
| Ecommerce       | [Core modules](../../projects/ecommerce/core/README.md)      |
| Genealogy       | [Core modules](../../projects/genealogy/core/README.md)      |
| Liberu platform | [Core modules](../../projects/liberu/core/README.md)         |
| Maintenance     | [Core modules](../../projects/maintenance/core/README.md)    |
| Real Estate     | [Core modules](../../projects/real-estate/core/README.md)    |
| SAP             | [Core modules](../../projects/sap/core/README.md)            |
| Social Network  | [Core modules](../../projects/social-network/core/README.md) |
