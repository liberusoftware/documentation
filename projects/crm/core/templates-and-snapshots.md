# Crm: Templates And Snapshots Core Module

Composer package: module-crm-templates-and-snapshots

Domain specification: [Templates And Snapshots](../features/templates-and-snapshots.md)

## Implementation plan

Own the domain entities, value objects, aggregates, invariants, domain events, application actions, queries, policies, contracts, persistence, and jobs in this presentation-neutral package. Keep domain logic in src/Domain/, use cases in src/Application/, and Laravel persistence in src/Infrastructure/. Do not depend on API, Filament, Livewire, React, Vue, Nuxt, themes, or provider SDKs.

## Verification

Test domain rules independently, then test persistence, authorization, tenancy, events, migrations, upgrades, and recovery. Presentation adapters consume these contracts and must not reimplement core behavior.
