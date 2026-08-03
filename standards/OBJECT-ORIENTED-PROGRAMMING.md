# Object-oriented programming standard

Use object-oriented design to model cohesive responsibilities and explicit collaborations, not to create unnecessary layers.

- Favor encapsulation, composition, polymorphism at genuine variation points, and dependency inversion.
- Keep invariants with the object or domain boundary that owns them.
- Use interfaces where consumers need substitution; use concrete classes when abstraction adds no value.
- Keep inheritance shallow and intentional; prefer composition over base-class convenience.
- Separate domain policy, application orchestration, infrastructure adapters, and presentation concerns.

See [PHP classes and objects](https://www.php.net/manual/en/language.oop5.php) and [Domain-driven design patterns](DOMAIN-DRIVEN-DESIGN-PATTERNS.md).

## Delivery checklist

Choose an abstraction because a real boundary, variation point, or test seam requires it. Keep domain objects independent of Laravel, inject collaborators, make side effects explicit, and avoid inheritance hierarchies that hide policy or persistence. Review coupling, lifecycle, error behavior, and public API compatibility before release.
