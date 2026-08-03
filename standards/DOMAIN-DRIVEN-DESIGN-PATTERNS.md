# Domain-driven design patterns standard

Use domain-driven design to make ownership, language, invariants, and integration boundaries explicit. Do not introduce tactical patterns without a domain or lifecycle problem they solve.

- Define bounded contexts/modules around cohesive business capabilities and ubiquitous language.
- Use entities and aggregates for identity and invariants, value objects for constrained values, and domain services for cohesive rules that do not belong to one entity.
- Use application actions/services to coordinate a use case, repositories only where persistence abstraction is meaningful, and read models/query objects for optimized reads.
- Publish domain events after committed local changes; use outbox/inbox, sagas, and compensating actions for distributed workflows.
- Keep aggregates small, enforce consistency boundaries, and never expose private persistence as a cross-module contract.

See [MODULES.md](../architecture/MODULES.md), [API.md](../architecture/API.md), and [Martin Fowler's DDD bliki](https://martinfowler.com/tags/domain%20driven%20design.html).

## Delivery checklist

Name the bounded context, owner, aggregates, consistency boundary, public commands/queries/events, persistence owner, policies, and excluded behavior. Keep aggregates small and transactions local. Use events and explicit compensation across modules, and verify that API/UI adapters consume public actions rather than private models or tables.
