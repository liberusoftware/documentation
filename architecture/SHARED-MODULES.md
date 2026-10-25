# Reuse and consolidation across projects

Use this guide before adding a capability that another product already owns. Reuse reduces competing implementations and inconsistent releases while keeping product responsibilities clear. A package appearing in several tracked application trees can be an intentional installed copy; the problem is independent ownership or drift, not the number of directories alone.

The [source comparison](SHARED-MODULE-COMPARISON.md) identifies 133 repeated physical package identities at the scanned commits. Of these, 89 have matching tracked runtime files and selected runtime metadata; 44 differ. The inventory also identifies 70 compatibility symlinks, which are alternate paths rather than separate implementations. This gives a concrete review order, not permission to replace divergent modules automatically.

## Choose the owning boundary

| Capability family | Documentation owner | Consumer rule |
| --- | --- | --- |
| Identity, teams, policy, audit, settings, files, localization, generic queues and observability | [Boilerplate foundation](../projects/boilerplate/BOILERPLATE.md) | Reuse foundation contracts; product applications configure them and supply product policy |
| Customer relationship records, sales pipeline, engagement, service relationships | [CRM](../projects/crm/CRM.md) | Other products retain their operational customer references; integrate through published DTOs/events |
| Subscription billing, commercial invoicing and recurring usage | [Billing](../projects/billing/BILLING.md) | Commerce and enterprise workspaces reference Billing records without duplicating the recurring ledger |
| Ledger postings, periods, reconciliation, financial statements and consolidation | [Accounting](../projects/accounting/ACCOUNTING.md) | Operational products submit posting requests and reconcile returned references |
| Physical commerce cart, checkout, order and fulfillment | [Ecommerce](../projects/ecommerce/ECOMMERCE.md) | Preserve commerce modules and existing application implementations during extraction |
| Asset maintenance, inspections and operational work orders | [Maintenance](../projects/maintenance/MAINTENANCE.md) | Keep financial asset accounting and maintenance lifecycle as distinct linked responsibilities |
| Infrastructure provisioning, control and infrastructure operations | [Control Panel](../projects/control-panel/CONTROL-PANEL.md) | Billing triggers authorized provisioning through public contracts rather than embedding control logic |
| Cross-product enterprise workflows and read models | [Enterprise composition](../projects/sap/COMPOSITION.md) | Compose existing domain owners; add orchestration and genuine missing capabilities |

These are architecture ownership rules, not evidence that every owner has a complete released implementation. Confirm the actual package maintainer and canonical repository before adopting a release.

## Interpret repeated source correctly

The comparison measures paths and bytes under declared runtime roots, `module.json`, and selected manifest metadata. Test content is recorded separately. Equal digests prove only equality of those inputs; they do not prove code quality, matching production databases, equal test coverage, complete release contents, or registry availability.

For example, `liberusoftware/activity-comments` and several of its adapters match across the scanned copies. Start their review with release ownership, consumer tests, and dependency pinning. Foundation packages such as `liberusoftware/audit`, `liberusoftware/organizations-teams`, and `liberusoftware/settings` have multiple runtime variants despite matching selected Composer metadata. Their differing paths include migrations and legacy code, so choosing one directory by name could discard data or behavior.

The `liberusoftware/webhooks` copies also differ in selected runtime metadata and action/model paths. Treat these as compatibility work: inspect payload signatures, retries, tenant checks, endpoint secrets, and delivery state before choosing a common version.

## Consolidation procedure

1. Select an identity from the comparison report and inspect every pinned source location. Distinguish intended local host integration from an accidental fork. Read the provider and call sites to determine which classes actually run; `Legacy/` does not automatically mean unused.
2. Record the canonical repository and accountable maintainer, supported package/runtime versions, public contracts, current consumers, migration history, and required extension points. Use actual manifest identities, not design identifiers or guessed repository names.
3. Compare APIs, default configuration, registration rules, tenant behavior, database schemas, and external event formats. Include excluded build/release files and tests. A missing migration is a compatibility difference even when current databases happen to look alike.
4. Move common behavior into the owning package. Keep product-specific policies, UI composition, and adapters in supported extension boundaries. Avoid a foundation package depending on a product's `App\\` classes or declaring relations into product tables.
5. Release a compatible shared version, or a new major with an explicit migration plan when compatibility cannot be maintained. Do not publish incompatible source trees under the same package name/version.
6. Adopt it in one consumer with a targeted dependency update, data backup/recovery rehearsal, schema checks, domain tests, and user journey checks. Reconcile record counts, ownership, and linked identifiers before promotion.
7. Repeat for other consumers and remove obsolete local implementations only after their callers and data have moved. Preserve installed tracked module trees where the application requires them. Never delete a documented capability solely because its package location changes.

## Shared presentation design

Reuse a product's authorized API contracts and framework-independent view models across presentations. Share React components, design tokens, formatting, and schema-derived types between React/Inertia and Next.js when they have no framework navigation/session imports. Keep Inertia page props, visits, and redirects in its adapter. Keep Next.js routing, server/client boundaries, server actions, and cache invalidation in its adapter.

Filament and Livewire can reuse domain actions and validation DTOs while retaining their own lifecycle and rendering behavior. Vue/Inertia and Nuxt follow the same separation. React Native and Flutter consume transport contracts and can share behavior specifications, but their device storage, offline synchronization, and platform UI require explicit implementations.

Do not make a module depend on every presentation package. Select the surface required by the host. An enterprise finance workspace should compose Accounting queries/actions and suitable UI adapters rather than own another financial model in each technology.

## Record adoption evidence

A consolidation change should state the package/version and source commit, consumer versions, schema/data transition, retained product extensions, tests executed, recovery method, and operator sign-off where the application process requires it. Keep release notes and dependency lockfile changes with the relevant consumer update.

This documentation work has compared sources and proposed ownership boundaries; it has not changed or released application packages. The [Composer](../guides/COMPOSER.md) and [npm](../guides/NPM.md) lifecycle guides cover development and publication once an implementation change is authorized in the owning repository.

## Package-specific adoption profiles

The [44 divergent-package profiles](shared-adoption/README.md) add pinned consumer variants, manifest/provider/dependency differences, database/table-operation evidence, contract signatures and data-preserving adoption steps. Use them with the general procedure before choosing a common release.
