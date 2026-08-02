# Crm: Field Service Coordination Core Module

Composer package: module-crm-field-service-coordination

Domain specification: [Field Service Coordination](../features/field-service-coordination.md)

## Implementation plan

Own the domain entities, value objects, aggregates, invariants, domain events, application actions, queries, policies, contracts, persistence, and jobs in this presentation-neutral package. Keep domain logic in src/Domain/, use cases in src/Application/, and Laravel persistence in src/Infrastructure/. Do not depend on API, Filament, Livewire, React, Vue, Nuxt, themes, or provider SDKs.

## Verification

Test domain rules independently, then test persistence, authorization, tenancy, events, migrations, upgrades, and recovery. Presentation adapters consume these contracts and must not reimplement core behavior.
