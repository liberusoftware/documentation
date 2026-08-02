# Classes standard

Classes should have one cohesive responsibility, explicit dependencies, stable names, and an observable contract.

- Prefer small immutable value objects, focused actions, queries, policies, adapters, and domain services.
- Use constructor injection and explicit visibility/types; avoid service-locator calls and static mutable state.
- Keep constructors cheap; perform I/O in named methods or application actions.
- Make invalid state difficult to create and validate inputs at trust boundaries.
- Test public behavior rather than private implementation details and document exceptions to the standard.

See [PHP](PHP.md), [Object-oriented programming](OBJECT-ORIENTED-PROGRAMMING.md), and [PSR.md](PSR.md).
