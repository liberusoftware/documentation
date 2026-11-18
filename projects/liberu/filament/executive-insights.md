# Liberu: Executive Insights Filament 5

**Existing cross-project implementations:** the [platform reuse guide](../REUSE.md) identifies the observed prefixed/unprefixed package families, namespaces, tables and adoption constraints. This scope is their composition/design home; it does not require a third independent implementation.

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#executive-insights). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one presentation implementation

**Package:** `module-liberu-executive-insights-filament`
**Matching domain module:** `liberu-executive-insights`
**Application:** Liberu Business Platform
**Source feature:** [Executive Insights](../features/executive-insights.md)
**Standard:** [FILAMENT](../../../standards/FILAMENT.md) · [Modules](../../../architecture/MODULES.md) · [API architecture](../../../architecture/API.md)

## 1. Purpose and ownership

This optional Filament 5 package presents exactly one new Liberu cross-product module. Provide an authorized operational panel for this module's registry, evidence, recovery, and reporting workflows. It depends only on the module's public contracts and must not duplicate or replace behavior owned by Accounting, CRM, Billing, Control Panel, Ecommerce, Automation, Maintenance, SAP, CMS, or another existing project.

## 2. Required surfaces

- composition manifest and module capability visibility;
- authorized workflow status, evidence, and failure/recovery states;
- tenant/team/role-aware filtering and denial behavior;
- localization, accessibility, audit context, and operational telemetry;
- explicit loading, empty, stale, validation, unauthorized, forbidden, offline, and server-error states where applicable.

## 3. Boundary rules

- The matching domain module owns invariants, persistence, policies, actions, events, and recovery semantics.
- Consume only documented module/API contracts; never access private tables, models, or another module's internal presentation package.
- Preserve correlation IDs, idempotency, concurrency, audit, tenant context, and authorization outcomes.
- Themes may style documented extension points but cannot change permissions, workflows, or source-of-truth ownership.

## 4. Verification

- Test allowed, denied, wrong-team/tenant, invalid, duplicate, stale/concurrent, timeout, partial-failure, replay, compensation, and recovery paths relevant to the adapter.
- Test package registration, collision boundaries, contract compatibility, accessibility, localization/RTL, security, and production build/render behavior.
- Prove that no existing project module or feature is reimplemented; this package exposes only the new Liberu cross-product capability.

## 5. Definition of done

- Package identity and dependency point one-to-one to the matching new domain module.
- Public routes, props, events, resources, components, and extension points are documented and namespaced.
- CI passes contract, authorization, tenant isolation, accessibility, compatibility, and failure/recovery checks.
- Release notes, migration guidance, runbook, and uninstall/disable behavior are complete.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-liberu-official-laravel-filament`](https://github.com/liberusoftware/project-liberu-official-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-planned-liberu-executive-insights-0532ffee-filament`](https://github.com/liberusoftware/module-planned-liberu-executive-insights-0532ffee-filament) (`liberusoftware/planned-liberu-executive-insights-0532ffee-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/executive-insights.md) · [API plan](../api/executive-insights.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Metric registry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `metric registry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cross-product projections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cross-product projections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Evidence drill-through** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `evidence drill-through`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Decision snapshots** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `decision snapshots`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Data-quality operations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `data-quality operations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
