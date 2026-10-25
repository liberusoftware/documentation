# Platform reuse across application repositories

The Liberu platform scope composes cross-product workflows. It has no separate `liberu-laravel` application in the requested discovery set, but its implementations are present inside other cloned applications. Absence of a matching application repository must not be read as absence of platform code.

## Ownership decision

Treat the four scopes below as the documentation/design homes. Reuse the observed implementations after contract/data compatibility review; do not implement a third copy merely because the platform scope has no own application clone. Preserve distinct records when the existing families represent different responsibilities. A naming prefix alone cannot decide whether two records or workflows should merge.

The Next.js registry therefore leaves naming unassigned for eight observed PHP identities plus four planned platform scopes (12 plan groups across four naming collisions). This is an explicit adoption gate, not permission to publish incompatible adapters under the same name.

## Source families

### business-workflow-reconciliation

| Family | Observed Composer identity | Declared PSR-4 prefix | Manifest capabilities | Literal created tables |
| --- | --- | --- | --- | --- |
| Unprefixed identity | [liberusoftware/liberu-business-workflow-reconciliation](../../modules/source/liberusoftware--liberu-business-workflow-reconciliation.md) | `Liberu\Platform\BusinessWorkflowReconciliation\` | `liberu.business-workflow-reconciliation`, `liberu.business-workflow-reconciliation.lifecycle` | `liberu_reconciliation_cases` |
| Prefixed identity | [liberusoftware/module-liberu-business-workflow-reconciliation](../../modules/source/liberusoftware--module-liberu-business-workflow-reconciliation.md) | `Liberu\BusinessWorkflowReconciliation\` | `liberu.business.workflow.reconciliation` | `liberu_workflow_runs` |

The families declare different record tables. Map their purposes, identifiers, states and callers before choosing consolidation: one may represent execution/configuration while another represents an outcome, case or snapshot. Keep one writer per record responsibility and link distinct records through stable references; do not discard one table or copy its rows blindly into the other.

The PSR-4 namespaces and capability spellings differ. A package-name edit is not sufficient migration: update imports, bindings, capability requirements, API clients and affected consumers deliberately. Preserve compatibility aliases only where their behavior is verified.

The [platform feature](features/business-workflow-reconciliation.md) remains the target scope. Its [API plan](api/business-workflow-reconciliation.md) and [Next.js plan](nextjs/business-workflow-reconciliation.md) must adopt the reviewed source contract rather than invent a parallel record owner.

### executive-insights

| Family | Observed Composer identity | Declared PSR-4 prefix | Manifest capabilities | Literal created tables |
| --- | --- | --- | --- | --- |
| Unprefixed identity | [liberusoftware/liberu-executive-insights](../../modules/source/liberusoftware--liberu-executive-insights.md) | `Liberu\Platform\ExecutiveInsights\` | `liberu.executive-insights`, `liberu.executive-insights.lifecycle` | `liberu_insight_snapshots` |
| Prefixed identity | [liberusoftware/module-liberu-executive-insights](../../modules/source/liberusoftware--module-liberu-executive-insights.md) | `Liberu\ExecutiveInsights\` | `liberu.executive.insights` | `liberu_metric_definitions` |

The families declare different record tables. Map their purposes, identifiers, states and callers before choosing consolidation: one may represent execution/configuration while another represents an outcome, case or snapshot. Keep one writer per record responsibility and link distinct records through stable references; do not discard one table or copy its rows blindly into the other.

The PSR-4 namespaces and capability spellings differ. A package-name edit is not sufficient migration: update imports, bindings, capability requirements, API clients and affected consumers deliberately. Preserve compatibility aliases only where their behavior is verified.

The [platform feature](features/executive-insights.md) remains the target scope. Its [API plan](api/executive-insights.md) and [Next.js plan](nextjs/executive-insights.md) must adopt the reviewed source contract rather than invent a parallel record owner.

### platform-orchestration

| Family | Observed Composer identity | Declared PSR-4 prefix | Manifest capabilities | Literal created tables |
| --- | --- | --- | --- | --- |
| Unprefixed identity | [liberusoftware/liberu-platform-orchestration](../../modules/source/liberusoftware--liberu-platform-orchestration.md) | `Liberu\Platform\PlatformOrchestration\` | `liberu.platform-orchestration`, `liberu.platform-orchestration.lifecycle` | `liberu_platform_workflows` |
| Prefixed identity | [liberusoftware/module-liberu-platform-orchestration](../../modules/source/liberusoftware--module-liberu-platform-orchestration.md) | `Liberu\PlatformOrchestration\` | `liberu.platform.orchestration` | `liberu_platform_compositions` |

The families declare different record tables. Map their purposes, identifiers, states and callers before choosing consolidation: one may represent execution/configuration while another represents an outcome, case or snapshot. Keep one writer per record responsibility and link distinct records through stable references; do not discard one table or copy its rows blindly into the other.

The PSR-4 namespaces and capability spellings differ. A package-name edit is not sufficient migration: update imports, bindings, capability requirements, API clients and affected consumers deliberately. Preserve compatibility aliases only where their behavior is verified.

The [platform feature](features/platform-orchestration.md) remains the target scope. Its [API plan](api/platform-orchestration.md) and [Next.js plan](nextjs/platform-orchestration.md) must adopt the reviewed source contract rather than invent a parallel record owner.

### revenue-and-care-orchestration

| Family | Observed Composer identity | Declared PSR-4 prefix | Manifest capabilities | Literal created tables |
| --- | --- | --- | --- | --- |
| Unprefixed identity | [liberusoftware/liberu-revenue-and-care-orchestration](../../modules/source/liberusoftware--liberu-revenue-and-care-orchestration.md) | `Liberu\Platform\RevenueAndCareOrchestration\` | `liberu.revenue-and-care-orchestration`, `liberu.revenue-and-care-orchestration.lifecycle` | `liberu_care_plans` |
| Prefixed identity | [liberusoftware/module-liberu-revenue-and-care-orchestration](../../modules/source/liberusoftware--module-liberu-revenue-and-care-orchestration.md) | `Liberu\Platform\RevenueAndCareOrchestration\` | `liberu.revenue-and-care-orchestration`, `liberu.revenue-and-care-orchestration.lifecycle` | `liberu_care_plans` |

The families declare the same table name. Compare column definitions, migration history, model behavior, tenancy and existing rows before any replacement; equal names do not prove compatible schemas.

**Co-installation conflict to resolve:** the families declare an overlapping PSR-4 namespace as well as the same table family. They are not safe to co-install by name alone: class resolution, provider/capability registration and migration ownership need an explicit selected family or reviewed compatibility migration.

The [platform feature](features/revenue-and-care-orchestration.md) remains the target scope. Its [API plan](api/revenue-and-care-orchestration.md) and [Next.js plan](nextjs/revenue-and-care-orchestration.md) must adopt the reviewed source contract rather than invent a parallel record owner.

## Data-preserving adoption

1. Choose the accountable owner and the actual source/release family for each bounded responsibility, supported by consumer and migration evidence. A stable-looking manifest version is insufficient.
2. Enumerate source record IDs, tenant/entity boundaries, states, dependent capabilities and downstream references. Retain separate execution and outcome records where they are different concepts.
3. Implement reviewed contract adapters, additive data transitions/backfills and explicit compatibility/deprecation periods in the owning code project. Verify reconciliation and recovery before redirecting callers.
4. Update actual Composer identities, namespaces, capability requirements, API/transport clients and application lockfiles together through the release process. Do not silently rename installed packages or merge two writers.
5. Adopt one consumer, then verify the other applications and enterprise composition before widening the rollout. Keep per-record identity, audit evidence, permission and retry behavior intact.

This documentation review does not perform those code/data migrations. The [divergent-package profiles](../../architecture/shared-adoption/README.md), [implementation references](../../modules/source/README.md), [shared ownership guide](../../architecture/SHARED-MODULES.md), and [package lifecycle guides](../../guides/COMPOSER.md) provide the concrete review inputs and release sequence.
