# Object-oriented programming standard

Use object-oriented design to model cohesive responsibilities and explicit collaborations, not to create unnecessary layers.

- Favor encapsulation, composition, polymorphism at genuine variation points, and dependency inversion.
- Keep invariants with the object or domain boundary that owns them.
- Use interfaces where consumers need substitution; use concrete classes when abstraction adds no value.
- Keep inheritance shallow and intentional; prefer composition over base-class convenience.
- Separate domain policy, application orchestration, infrastructure adapters, and presentation concerns.

See [PHP classes and objects](https://www.php.net/manual/en/language.oop5.php) and [Domain-driven design patterns](DOMAIN-DRIVEN-DESIGN-PATTERNS.md).
