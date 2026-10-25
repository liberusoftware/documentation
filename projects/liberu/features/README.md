# Liberu platform feature specifications

<!-- catalogue-status:start -->
This index preserves **4 module documents/spellings**. Counts are specifications, not released packages or deployed features. Exact source identities and aliases are in the [source map](../SOURCE-MAPPING.md); [shared ownership](../../../architecture/SHARED-MODULES.md) and [Next.js adapter homes](../../../modules/nextjs/OWNERSHIP.md) prevent alternate spellings from becoming competing implementations.
<!-- catalogue-status:end -->

These are new cross-product capabilities required by the Liberu business platform. They do not duplicate the product modules listed in the other `projects/*` scopes. Each feature owns only the cross-product contract and composition behavior described here.

| Module document | Source/target reference | Related plans |
| --- | --- | --- |
| [Business Workflow Reconciliation](business-workflow-reconciliation.md) | [Target/source map](../SOURCE-MAPPING.md#business-workflow-reconciliation) | [core](../core/business-workflow-reconciliation.md) · [api](../api/business-workflow-reconciliation.md) · [nextjs](../nextjs/business-workflow-reconciliation.md) |
| [Executive Insights](executive-insights.md) | [Target/source map](../SOURCE-MAPPING.md#executive-insights) | [core](../core/executive-insights.md) · [api](../api/executive-insights.md) · [nextjs](../nextjs/executive-insights.md) |
| [Platform Orchestration](platform-orchestration.md) | [Target/source map](../SOURCE-MAPPING.md#platform-orchestration) | [core](../core/platform-orchestration.md) · [api](../api/platform-orchestration.md) · [nextjs](../nextjs/platform-orchestration.md) |
| [Revenue and Care Orchestration](revenue-and-care-orchestration.md) | [Target/source map](../SOURCE-MAPPING.md#revenue-and-care-orchestration) | [core](../core/revenue-and-care-orchestration.md) · [api](../api/revenue-and-care-orchestration.md) · [nextjs](../nextjs/revenue-and-care-orchestration.md) |

Product-specific behavior remains owned by the existing application scope and module that supplies it.
