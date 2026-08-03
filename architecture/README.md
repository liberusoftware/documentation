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

For language/framework/design standards, start with [standards/README.md](../standards/README.md). For solution selection, see [TECHNOLOGIES.md](../TECHNOLOGIES.md) and [GETTING-STARTED.md](../GETTING-STARTED.md).
