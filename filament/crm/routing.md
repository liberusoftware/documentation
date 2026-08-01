# CRM: Routing Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-routing-filament`  
**Matching domain module:** `crm-routing`  
**Application:** CRM  
**Source feature:** [Routing](../../features/crm/routing.md)  
**Architecture:** [FILAMENT.md](../../FILAMENT.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-routing` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Rule:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Territory:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Skill:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Language:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Availability:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Workload:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Value:** resource/table/form/action or page behavior for this module's authorized workflow.
- **SLA:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Round-robin assignment with fallback and acceptance timers:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-routing-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `rule`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `territory`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `skill`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `language`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `availability`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `workload`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `value`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sla`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `round-robin-assignment-with-fallback-and-acceptance-timers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-routing` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
