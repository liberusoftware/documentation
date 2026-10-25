# Architecture decisions and boundaries

This folder records Liberu’s ecosystem architecture: ownership, package boundaries, application composition, APIs, tenancy, repositories, security, and cross-product decisions. Reusable implementation and coding rules live in [standards/](../standards/).

## Core architecture

- [Adoption profiles](ADOPTION.md) — progressive deployment and operating choices for personal users, SMEs, and enterprise organizations.
- [Modules](MODULES.md) — package boundaries, dependencies, lifecycle, and composition.
- [API](API.md) — public contracts, authentication, tenancy, errors, and versioning.
- [Repositories](REPOSITORIES.md) — repository ownership and README expectations.
- [Tenancy](TENANCY.md) · [Teams](TEAMS.md) · [Policy](POLICY.md) — context and authorization boundaries.
- [Settings](SETTINGS.md) · [Jetstream](JETSTREAM.md) · [Socialstream](SOCIALSTREAM.md) — shared application capabilities.
- [Security](SECURITY.md) · [Installation](../INSTALL.md) — security policy and environment setup.
- [Mobile](MOBILE.md) — mobile application boundaries, offline behavior, device security, and release architecture.

For language/framework/design standards, start with [standards/README.md](../standards/README.md). For solution selection, see [TECHNOLOGIES.md](../TECHNOLOGIES.md) and [GETTING-STARTED.md](../GETTING-STARTED.md).

- [Source module inventory](SOURCE-INVENTORY.md) — commit-pinned manifests, project coverage, and repeated package identities.

- [Shared module reuse](SHARED-MODULES.md) and [source comparison](SHARED-MODULE-COMPARISON.md) — ownership, drift evidence, and consolidation procedure.

- [Observed implementation references](../modules/source/README.md) and [design-to-source mappings](source-design-mapping.json) — bridge package manifests and existing module plans.

- [Documentation/source synchronization](../guides/DOCUMENTATION-MAINTENANCE.md) — reproducible discovery, references and review.

- [Presentation and package boundaries](PRESENTATION.md) — choose a layer, share UI/contracts, preserve transport and domain ownership.

- [Shared-package adoption profiles](shared-adoption/README.md) — 44 package-specific schema, contract and consumer transition reviews.

- [Documentation objective audit](DOCUMENTATION-AUDIT.md) — requirement coverage, semantic/source review and reproducible validation.
