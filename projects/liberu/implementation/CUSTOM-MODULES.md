# Liberu custom module index

These are the cross-product capabilities required by the official websites and staff apps. Existing product capabilities remain in their owning project. The four existing Liberu modules are authoritative domain packages; the four composition modules below are Liberu implementation packages to create only after the listed ADR and contract are approved.

## Existing Liberu domain modules

| Module | Package | Use in official sites/staff apps | Source |
| --- | --- | --- | --- |
| Platform Orchestration | `module-liberu-platform-orchestration` | Manifest, capability graph, lifecycle, release gates, ownership | [Feature](../features/platform-orchestration.md) · [Core](../core/platform-orchestration.md) |
| Executive Insights | `module-liberu-executive-insights` | Governed management and operational read models | [Feature](../features/executive-insights.md) · [Core](../core/executive-insights.md) |
| Business Workflow Reconciliation | `module-liberu-business-workflow-reconciliation` | Cross-system drift, replay, exception, and reconciliation work | [Feature](../features/business-workflow-reconciliation.md) · [Core](../core/business-workflow-reconciliation.md) |
| Revenue and Care Orchestration | `module-liberu-revenue-and-care-orchestration` | Health signals, service recovery, protected outreach, AI action envelope | [Feature](../features/revenue-and-care-orchestration.md) · [Core](../core/revenue-and-care-orchestration.md) |

## New Liberu composition modules

| Module | Package | Owns | Does not own |
| --- | --- | --- | --- |
| [Brand Experience Composition](custom-modules/brand-experience.md) | `module-liberu-brand-experience` | Brand/site registry, domains, navigation composition, theme recipe, cross-site links | CMS content, SEO truth, identity, consent, or domain records |
| [Staff Operations Workspace](custom-modules/staff-operations-workspace.md) | `module-liberu-staff-operations-workspace` | Role-based work centers, task registry, saved queues, cross-product context links | CRM cases, invoices, infrastructure, accounting, or a second workflow engine |
| [Customer Portal Shell](custom-modules/customer-portal-shell.md) | `module-liberu-customer-portal-shell` | Portal navigation, capability cards, safe deep links, status composition, support entry | Customer records, orders, invoices, cases, or entitlement decisions |
| [Service Catalog Composition](custom-modules/service-catalog-composition.md) | `module-liberu-service-catalog-composition` | Liberu product/service presentation, eligibility hints, comparison and handoff metadata | Authoritative catalog, pricing, checkout, subscription, or provisioning |

Each new module requires a package manifest, ADR, public DTOs/events, policy matrix, migration/retention plan, API decision, matching web adapter where needed, mobile mapping, tests, runbook, and owner before implementation begins.

## Shared customizations, not modules

Keep these in the application/theme layer unless an ADR proves independent domain ownership: Liberu design tokens, four site recipes, cross-brand header/footer, consent banner, support launcher, status badges, staff navigation, feature flags, analytics naming, error copy, notification templates, and deployment configuration.
