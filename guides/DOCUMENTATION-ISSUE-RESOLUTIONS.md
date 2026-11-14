# Documentation issue decisions

These changes implement the open documentation review requests. They clarify standards and design scope; they do not certify that existing packages already conform. Implementation work remains in the owning repositories.

| Request | Documentation decision |
| --- | --- |
| [#18: Composer adapter naming](https://github.com/liberusoftware/documentation/issues/18) | §9 already distinguishes repository slugs from Composer identities. Preserve that corrected table: new Composer adapters omit `module-`; existing published manifests remain authoritative. |
| [#19: release tags](https://github.com/liberusoftware/documentation/issues/19) | CI examples, triggers and tag condition use bare SemVer such as `1.2.3`. Verify required runs on the tagged commit before release. |
| [#20: tracked module/theme directories](https://github.com/liberusoftware/documentation/issues/20) | Keep `/modules` and `/themes` in host commits, including after promotion. Downstream ignore-policy ADRs do not override the fleet policy. |
| [#21: circular promotion gate](https://github.com/liberusoftware/documentation/issues/21) | Split promotion readiness (provable from a path package) from release readiness (repository, workflows, tag and compatibility evidence). Promotion keeps the host copy tracked. |
| [#22: extraction coverage](https://github.com/liberusoftware/documentation/issues/22) | Greenfield remains 100%. An approved host extraction starts no lower than 80%, ratchets upward, and records risk/ownership/evidence toward 100%. |
| [#23: redundant Commerce prefix](https://github.com/liberusoftware/documentation/issues/23) | Rename the six catalogue capabilities to Core, Customers, Extensions, Functions, Automation Pack and Copilot. Preserve historical documentation URLs and migrate published identities explicitly. |
| [#24: repeated Boilerplate scope](https://github.com/liberusoftware/documentation/issues/24) | Keep one canonical scope body. Distinguish 28 canonical capabilities from README/index files and retained source aliases. Also remove the repeated Ecommerce scope body. |
| [#25: module default views](https://github.com/liberusoftware/documentation/issues/25) | Confirm the resolver step as a runtime requirement for renderable presentation packages; define registration, defaults, fallback/override and isolation tests. Presentation-neutral cores do not gain a UI dependency solely to populate a views directory. |
| [#26: Catering](https://github.com/liberusoftware/documentation/issues/26) | Add one Ecommerce domain owner and core/API/web/mobile/desktop plans, preserving shared ownership and unresolved contract decisions. Implementation/schema remains gated on those decisions. |

Read [module boundaries](../architecture/MODULES.md), [themes](../standards/THEMES.md), [coverage](../standards/TESTING.md), [CI](../standards/CI.md), [Catering](../projects/ecommerce/CATERING.md) and [technology wayfinders](../projects/IMPLEMENTATION-WAYFINDERS.md) for the normative details and delivery tracking.
